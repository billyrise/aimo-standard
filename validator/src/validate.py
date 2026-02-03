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
    "Invalid taxonomy dimension: 'EV' is reserved for Evidence Artifact IDs. "
    "Use 'LG' for log/event taxonomy codes."
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

    # 3) object_index and payload_index: each file exists and sha256 matches
    for i, obj in enumerate(manifest.get("object_index", [])):
        rel = obj.get("path", "")
        if ".." in rel or rel.startswith("/"):
            errors.append(f"object_index[{i}]: path must be relative and not contain ../: {rel!r}")
            continue
        fp = bundle_root / rel
        if not fp.is_file():
            errors.append(f"object_index[{i}]: file not found: {rel}")
            continue
        want = (obj.get("sha256") or "").lower().strip()
        if len(want) != 64 or not all(c in "0123456789abcdef" for c in want):
            errors.append(f"object_index[{i}]: invalid sha256 (must be 64 hex)")
            continue
        got = sha256_file(fp)
        if got != want:
            errors.append(f"object_index[{i}]: sha256 mismatch for {rel}")

    for i, pl in enumerate(manifest.get("payload_index", [])):
        rel = pl.get("path", "")
        if ".." in rel or rel.startswith("/"):
            errors.append(f"payload_index[{i}]: path must be relative and not contain ../: {rel!r}")
            continue
        fp = bundle_root / rel
        if not fp.is_file():
            errors.append(f"payload_index[{i}]: file not found: {rel}")
            continue
        want = (pl.get("sha256") or "").lower().strip()
        if len(want) != 64 or not all(c in "0123456789abcdef" for c in want):
            errors.append(f"payload_index[{i}]: invalid sha256 (must be 64 hex)")
            continue
        got = sha256_file(fp)
        if got != want:
            errors.append(f"payload_index[{i}]: sha256 mismatch for {rel}")

    # 4) signatures/ must contain at least one file (v0.1: existence and target reference)
    sig_dir = bundle_root / "signatures"
    sig_files = [f for f in sig_dir.iterdir()] if sig_dir.is_dir() else []
    if not sig_files:
        errors.append("signatures/ must contain at least one signature file (manifest reference required in v0.1)")

    return errors


def main():
    if len(sys.argv) != 2:
        print("Usage: python validator/src/validate.py <path-to-root-json | path-to-bundle-dir>", file=sys.stderr)
        sys.exit(2)

    p = Path(sys.argv[1]).resolve()
    if not p.exists():
        print(f"Path not found: {p}", file=sys.stderr)
        sys.exit(2)

    # Bundle mode: directory with manifest.json
    if p.is_dir():
        bundle_errors = validate_bundle(p)
        if bundle_errors:
            print(BUNDLE_INTEGRITY_REJECT_MESSAGE, file=sys.stderr)
            for err in bundle_errors:
                print(f"  {err}", file=sys.stderr)
            sys.exit(1)
        print("OK")
        sys.exit(0)

    # Root JSON mode: single file (legacy)
    payload = json.loads(p.read_text(encoding="utf-8"))

    # Step 1: Reject codes.EV before schema (clear, human-readable reason)
    pre_errors = reject_codes_ev_before_schema(payload)
    if pre_errors:
        print(CODES_EV_REJECT_MESSAGE, file=sys.stderr)
        for err in pre_errors:
            print(f"  {err}", file=sys.stderr)
        sys.exit(1)

    # Step 2: Schema validation
    try:
        validate_json(payload)
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

    # Step 3: Dictionary consistency check
    dict_errors, dict_warnings = validate_dictionary_consistency(payload)
    for warn in dict_warnings:
        print(f"WARNING: {warn}", file=sys.stderr)
    if dict_errors:
        print("\nDictionary consistency check failed:", file=sys.stderr)
        for err in dict_errors:
            print(f"  {err}", file=sys.stderr)
        sys.exit(1)

    print("OK")
    sys.exit(0)

if __name__ == "__main__":
    main()
