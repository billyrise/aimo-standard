import json
import sys
from pathlib import Path
from typing import Any
from jsonschema import Draft202012Validator, RefResolver

ROOT = Path(__file__).resolve().parents[2]
SCHEMAS_DIR = ROOT / "schemas" / "jsonschema"
TAXONOMY_DIR = ROOT / "source_pack" / "03_taxonomy"
DICTIONARY_JSON_PATH = TAXONOMY_DIR / "taxonomy_dictionary.json"


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

def main():
    if len(sys.argv) != 2:
        print("Usage: python validator/src/validate.py <path-to-root-json>", file=sys.stderr)
        sys.exit(2)

    p = Path(sys.argv[1])
    payload = json.loads(p.read_text(encoding="utf-8"))
    
    # Step 1: Schema validation
    try:
        validate_json(payload)
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

    # Step 2: Dictionary consistency check
    dict_errors, dict_warnings = validate_dictionary_consistency(payload)
    
    # Print warnings
    for warn in dict_warnings:
        print(f"WARNING: {warn}", file=sys.stderr)
    
    # Print errors and exit if any
    if dict_errors:
        print("\nDictionary consistency check failed:", file=sys.stderr)
        for err in dict_errors:
            print(f"  {err}", file=sys.stderr)
        sys.exit(1)

    print("OK")
    sys.exit(0)

if __name__ == "__main__":
    main()
