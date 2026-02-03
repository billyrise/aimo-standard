import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any
from jsonschema import Draft202012Validator, RefResolver

ROOT = Path(__file__).resolve().parents[2]
SCHEMAS_DIR = ROOT / "schemas" / "jsonschema"
TAXONOMY_DIR = ROOT / "source_pack" / "03_taxonomy"
DICTIONARY_JSON_PATH = TAXONOMY_DIR / "taxonomy_dictionary.json"
PROFILES_DIR = ROOT / "coverage_map" / "profiles"
PROFILE_SCHEMA_NAME = "aimo-profile.schema.json"

# Fixed message for Evidence Bundle integrity failure (audit-facing).
BUNDLE_INTEGRITY_REJECT_MESSAGE = (
    "Invalid Evidence Bundle: manifest integrity requirements not satisfied "
    "(missing sha256/signature/index mismatch)."
)


def load_schema(name: str) -> dict:
    p = SCHEMAS_DIR / name
    return json.loads(p.read_text(encoding="utf-8"))


def load_taxonomy_dictionary() -> dict[str, dict[str, Any]]:
    """Load taxonomy dictionary and build code lookup.
    
    Returns dict mapping code -> {status, label_en, ...}
    """
    if not DICTIONARY_JSON_PATH.exists():
        return {}
    
    data = json.loads(DICTIONARY_JSON_PATH.read_text(encoding="utf-8"))
    lookup: dict[str, dict[str, Any]] = {}
    for entry in data.get("entries", []):
        code = entry.get("code", "")
        if code:
            lookup[code] = entry
    return lookup

def make_resolver():
    store = {
        "aimo-standard.schema.json": load_schema("aimo-standard.schema.json"),
        "aimo-dictionary.schema.json": load_schema("aimo-dictionary.schema.json"),
        "aimo-ev.schema.json": load_schema("aimo-ev.schema.json"),
    }
    # Allow relative $ref like "aimo-dictionary.schema.json"
    return RefResolver.from_schema(store["aimo-standard.schema.json"], store=store)

def validate_json(payload: dict) -> None:
    schema = load_schema("aimo-standard.schema.json")
    resolver = make_resolver()
    validator = Draft202012Validator(schema, resolver=resolver)
    errors = sorted(validator.iter_errors(payload), key=lambda e: e.path)
    if errors:
        msgs = []
        for e in errors[:50]:
            path = ".".join([str(x) for x in e.path]) if e.path else "<root>"
            msgs.append(f"{path}: {e.message}")
        raise ValueError("Schema validation failed:\n" + "\n".join(msgs))


# Fixed message for pre-schema rejection of codes.EV (human-readable, normative).
CODES_EV_REJECT_MESSAGE = (
    "Invalid taxonomy dimension: 'EV' is reserved for Evidence artifact IDs. "
    "Use 'LG' for Log/Event Type."
)


def reject_codes_ev_before_schema(payload: dict) -> list[str]:
    """Reject use of EV as taxonomy dimension in evidence.codes *before* schema validation.
    EV is reserved for Evidence artifact IDs; taxonomy log/event dimension uses LG."""
    errors: list[str] = []
    for ev_idx, evidence in enumerate(payload.get("evidence", [])):
        codes_obj = evidence.get("codes") if isinstance(evidence, dict) else None
        if isinstance(codes_obj, dict) and "EV" in codes_obj:
            ev_id = evidence.get("id", f"evidence[{ev_idx}]") if isinstance(evidence, dict) else f"evidence[{ev_idx}]"
            errors.append(f"{ev_id}: {CODES_EV_REJECT_MESSAGE}")
    return errors


def validate_dictionary_consistency(payload: dict) -> tuple[list[str], list[str]]:
    """Validate that evidence codes exist in taxonomy dictionary.
    
    Returns (errors, warnings) tuple.
    - errors: codes that don't exist or have status "removed"
    - warnings: codes that have status "deprecated"
    """
    errors: list[str] = []
    warnings: list[str] = []
    
    dictionary = load_taxonomy_dictionary()
    if not dictionary:
        warnings.append(
            "taxonomy_dictionary.json not found, skipping dictionary consistency check"
        )
        return errors, warnings
    
    evidence_list = payload.get("evidence", [])
    
    for ev_idx, evidence in enumerate(evidence_list):
        ev_id = evidence.get("id", f"evidence[{ev_idx}]")
        codes_obj = evidence.get("codes", {})
        
        for dimension, codes in codes_obj.items():
            if not isinstance(codes, list):
                continue
            
            for code in codes:
                if code not in dictionary:
                    errors.append(
                        f"{ev_id}: code '{code}' not found in taxonomy dictionary"
                    )
                else:
                    status = dictionary[code].get("status", "")
                    if status == "removed":
                        errors.append(
                            f"{ev_id}: code '{code}' has status 'removed' "
                            f"and cannot be used"
                        )
                    elif status == "deprecated":
                        replaced_by = dictionary[code].get("replaced_by", "")
                        if replaced_by:
                            warnings.append(
                                f"{ev_id}: code '{code}' is deprecated, "
                                f"consider using '{replaced_by}' instead"
                            )
                        else:
                            warnings.append(
                                f"{ev_id}: code '{code}' is deprecated"
                            )
    
    return errors, warnings


def sha256_file(path: Path) -> str:
    """Return lowercase 64-char hex SHA-256 of file at path."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _check_path_under_root(
    bundle_root: Path,
    path_str: str,
    subdir: str | None = None,
    label: str = "path",
) -> tuple[bool, Path | None, str | None]:
    """
    Ensure path is relative, has no .. segment, and resolves under bundle root.
    If subdir is set (e.g. 'signatures'), path_str is relative to bundle_root/subdir.
    Returns (ok, resolved_path, error_message).
    """
    if not path_str or not isinstance(path_str, str):
        return False, None, f"{label}: path required"
    if path_str.startswith("/"):
        return False, None, f"{label}: path must be relative (no leading /): {path_str!r}"
    if ".." in path_str:
        return False, None, f"{label}: path must not contain ..: {path_str!r}"
    base = (bundle_root / subdir) if subdir else bundle_root
    try:
        resolved = (base / path_str).resolve()
    except Exception as e:
        return False, None, f"{label}: invalid path {path_str!r}: {e}"
    root_resolved = bundle_root.resolve()
    try:
        resolved.relative_to(root_resolved)
    except ValueError:
        return False, None, f"{label}: path escapes bundle root: {path_str!r}"
    return True, resolved, None


def validate_bundle(bundle_root: Path) -> list[str]:
    """
    Validate Evidence Bundle at bundle_root (directory).
    Pre-schema: required dirs and manifest.json. Then schema validate manifest.
    Then: every object_index/payload_index file exists and sha256 matches.
    Then: signatures/ contains at least one file (v0.1: existence only).
    Returns list of error messages; empty if valid.
    """
    errors: list[str] = []
    bundle_root = bundle_root.resolve()

    # 1) Required structure
    required_dirs = ["objects", "payloads", "signatures", "hashes"]
    for d in required_dirs:
        if not (bundle_root / d).is_dir():
            errors.append(f"Missing required directory: {d}/")
    manifest_path = bundle_root / "manifest.json"
    if not manifest_path.is_file():
        errors.append("Missing required file: manifest.json")
    if errors:
        return errors

    # 2) Load and schema-validate manifest
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errors.append(f"manifest.json invalid JSON: {e}")
        return errors

    schema = load_schema("evidence_bundle_manifest.schema.json")
    try:
        Draft202012Validator(schema).validate(manifest)
    except Exception as e:
        errors.append(f"manifest.json schema validation failed: {e}")
        return errors

    # 3) Path safety and resolve-under-root for all path-bearing fields
    for i, obj in enumerate(manifest.get("object_index", [])):
        rel = obj.get("path", "")
        ok, resolved, err = _check_path_under_root(bundle_root, rel, subdir=None, label=f"object_index[{i}].path")
        if not ok:
            errors.append(err or f"object_index[{i}]: invalid path")
            continue
        if not (resolved and resolved.is_file()):
            errors.append(f"object_index[{i}]: file not found: {rel}")
            continue
        want = (obj.get("sha256") or "").lower().strip()
        if len(want) != 64 or not all(c in "0123456789abcdef" for c in want):
            errors.append(f"object_index[{i}]: invalid sha256 (must be 64 hex)")
            continue
        got = sha256_file(resolved)
        if got != want:
            errors.append(f"object_index[{i}]: sha256 mismatch for {rel}")

    for i, pl in enumerate(manifest.get("payload_index", [])):
        rel = pl.get("path", "")
        ok, resolved, err = _check_path_under_root(bundle_root, rel, subdir=None, label=f"payload_index[{i}].path")
        if not ok:
            errors.append(err or f"payload_index[{i}]: invalid path")
            continue
        if not (resolved and resolved.is_file()):
            errors.append(f"payload_index[{i}]: file not found: {rel}")
            continue
        want = (pl.get("sha256") or "").lower().strip()
        if len(want) != 64 or not all(c in "0123456789abcdef" for c in want):
            errors.append(f"payload_index[{i}]: invalid sha256 (must be 64 hex)")
            continue
        got = sha256_file(resolved)
        if got != want:
            errors.append(f"payload_index[{i}]: sha256 mismatch for {rel}")

    # 4) signing.signatures: each path exists under signatures/; path safe; targets includes manifest.json (v0.1)
    signatures = (manifest.get("signing") or {}).get("signatures") or []
    if not signatures:
        errors.append("signing.signatures must contain at least one entry (v0.1)")
    else:
        has_manifest_target = False
        for i, sig in enumerate(signatures):
            path_str = sig.get("path", "")
            ok, resolved, err = _check_path_under_root(
                bundle_root, path_str, subdir="signatures", label=f"signing.signatures[{i}].path"
            )
            if not ok:
                errors.append(err or f"signing.signatures[{i}]: invalid path")
                continue
            if not (resolved and resolved.is_file()):
                errors.append(f"signing.signatures[{i}]: signature file not found: signatures/{path_str}")
                continue
            targets = sig.get("targets") or []
            if "manifest.json" in targets:
                has_manifest_target = True
        if not has_manifest_target:
            errors.append("signing.signatures: at least one entry must have targets including manifest.json (v0.1 MUST)")

    # 5) hash_chain: path exists under hashes/; path safe; covers includes manifest.json and objects/index.json (v0.1)
    hc = manifest.get("hash_chain") or {}
    hc_path = hc.get("path", "")
    ok, resolved, err = _check_path_under_root(
        bundle_root, hc_path, subdir="hashes", label="hash_chain.path"
    )
    if not ok and hc_path:
        errors.append(err or "hash_chain.path: invalid path")
    elif ok and resolved:
        if not resolved.is_file():
            errors.append(f"hash_chain.path: file not found: hashes/{hc_path}")
    # v0.1: covers MUST include manifest.json and objects/index.json (always check when hash_chain present)
    if hc:
        covers = hc.get("covers") or []
        if "manifest.json" not in covers:
            errors.append("hash_chain.covers must include manifest.json (v0.1 MUST)")
        if "objects/index.json" not in covers:
            errors.append("hash_chain.covers must include objects/index.json (v0.1 MUST)")

    return errors


def run_validation(path: Path) -> tuple[bool, list[str], list[str]]:
    """
    Run validation on path (file or bundle dir). Returns (valid, errors, warnings).
    """
    errors: list[str] = []
    warnings: list[str] = []

    if not path.exists():
        return False, [f"Path not found: {path}"], []

    if path.is_dir():
        bundle_errors = validate_bundle(path)
        if bundle_errors:
            errors.append(BUNDLE_INTEGRITY_REJECT_MESSAGE)
            errors.extend(bundle_errors)
            return False, errors, []
        return True, [], []

    # Root JSON mode
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON: {e}"], []

    pre_errors = reject_codes_ev_before_schema(payload)
    if pre_errors:
        errors.append(CODES_EV_REJECT_MESSAGE)
        errors.extend(pre_errors)
        return False, errors, []

    try:
        validate_json(payload)
    except Exception as e:
        errors.append(str(e))
        return False, errors, []

    dict_errors, dict_warnings = validate_dictionary_consistency(payload)
    warnings.extend(dict_warnings)
    if dict_errors:
        errors.append("Dictionary consistency check failed")
        errors.extend(dict_errors)
        return False, errors, warnings

    return True, [], warnings


def emit_sarif(errors: list[str], path_str: str) -> dict:
    """Produce minimal SARIF 2.1.0 run for GitHub Code Scanning / human readers."""
    results = [
        {
            "ruleId": "aimo-standard/validation",
            "level": "error",
            "message": {"text": err},
            "locations": [{"physicalLocation": {"artifactLocation": {"uri": path_str}, "region": {"startLine": 1}}}],
        }
        for err in errors
    ]
    return {
        "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
        "version": "2.1.0",
        "runs": [
            {
                "tool": {"driver": {"name": "AIMO Validator", "version": "0.1", "rules": [{"id": "aimo-standard/validation", "name": "AIMO validation"}]}},
                "results": results,
            }
        ],
    }


def validate_profiles(profiles_dir: Path | None = None) -> tuple[bool, list[str]]:
    """
    Validate all profile JSONs in coverage_map/profiles/ against aimo-profile.schema.json.
    Enforces profile_id (PR-*), target (enum), target_version, and mappings structure.
    Returns (valid, list of error messages).
    """
    errors: list[str] = []
    directory = (profiles_dir or PROFILES_DIR).resolve()
    if not directory.is_dir():
        return False, [f"Profiles directory not found: {directory}"]

    try:
        schema = load_schema(PROFILE_SCHEMA_NAME)
    except Exception as e:
        return False, [f"Failed to load {PROFILE_SCHEMA_NAME}: {e}"]

    validator = Draft202012Validator(schema)
    json_files = sorted(directory.glob("*.json"))
    if not json_files:
        return False, [f"No *.json files in {directory}"]

    for path in json_files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{path.name}: invalid JSON: {e}")
            continue
        for err in validator.iter_errors(data):
            loc = ".".join(str(x) for x in err.path) if err.path else "<root>"
            errors.append(f"{path.name}: {loc}: {err.message}")

    return len(errors) == 0, errors


def main():
    parser = argparse.ArgumentParser(
        description="Validate AIMO root JSON, Evidence Bundle directory, and/or profile JSONs.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=None,
        help="Path to root JSON file or bundle directory (optional if --validate-profiles is used)",
    )
    parser.add_argument(
        "--format",
        choices=["default", "json", "sarif"],
        default="default",
        help="Output format: default (human), json (machine), sarif (Code Scanning)",
    )
    parser.add_argument(
        "--validate-profiles",
        action="store_true",
        help="Validate profile JSONs in coverage_map/profiles/ against aimo-profile.schema.json",
    )
    args = parser.parse_args()

    path_valid = True
    errors: list[str] = []
    warnings: list[str] = []
    path_str = ""

    if args.path is not None:
        p = args.path.resolve()
        path_str = str(p)
        path_valid, errors, warnings = run_validation(p)
    elif not args.validate_profiles:
        parser.error("Either path or --validate-profiles (or both) is required")

    profiles_valid = True
    profile_errors: list[str] = []
    if args.validate_profiles:
        profiles_valid, profile_errors = validate_profiles()

    valid = path_valid and profiles_valid
    if not profiles_valid:
        errors = errors + profile_errors

    if args.format == "json":
        out = {
            "valid": valid,
            "errors": errors,
            "warnings": warnings,
            "path": path_str or None,
            "profiles_valid": profiles_valid if args.validate_profiles else None,
        }
        print(json.dumps(out, indent=2, ensure_ascii=False))
    elif args.format == "sarif":
        sarif = emit_sarif(errors, path_str or "profiles") if errors else emit_sarif([], path_str or "profiles")
        print(json.dumps(sarif, indent=2, ensure_ascii=False))
    else:
        if errors:
            for err in errors:
                print(err, file=sys.stderr)
        else:
            for w in warnings:
                print(f"WARNING: {w}", file=sys.stderr)
            if args.validate_profiles and profiles_valid and (args.path is None or path_valid):
                print("Profile validation: OK")
            if args.path is not None and path_valid:
                print("OK")

    sys.exit(0 if valid else 1)

if __name__ == "__main__":
    main()
