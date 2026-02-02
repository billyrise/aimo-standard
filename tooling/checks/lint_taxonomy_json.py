#!/usr/bin/env python3
"""
Lint check for taxonomy_dictionary.json.

Validates the generated taxonomy dictionary JSON against:
1. aimo-dictionary.schema.json (JSON Schema validation)
2. taxonomy_pack_v0.1.json (dimension consistency check)

Usage:
    python tooling/checks/lint_taxonomy_json.py

Exit codes:
    0 - All checks passed
    1 - One or more checks failed
"""

import json
import sys
from pathlib import Path
from typing import Any

try:
    import jsonschema
    from jsonschema import Draft202012Validator
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False

# Paths
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
TAXONOMY_DIR = REPO_ROOT / "source_pack" / "03_taxonomy"
SCHEMA_DIR = REPO_ROOT / "schemas" / "jsonschema"

DICTIONARY_JSON_PATH = TAXONOMY_DIR / "taxonomy_dictionary.json"
DICTIONARY_SCHEMA_PATH = SCHEMA_DIR / "aimo-dictionary.schema.json"
TAXONOMY_PACK_PATH = TAXONOMY_DIR / "taxonomy_pack_v0.1.json"


def load_json(path: Path) -> dict[str, Any]:
    """Load JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_schema(dictionary: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    """Validate dictionary against JSON schema. Returns list of errors."""
    if not HAS_JSONSCHEMA:
        print("WARNING: jsonschema not installed, skipping schema validation")
        return []

    errors: list[str] = []
    validator = Draft202012Validator(schema)

    for error in validator.iter_errors(dictionary):
        path = ".".join(str(p) for p in error.absolute_path) or "(root)"
        errors.append(f"Schema error at {path}: {error.message}")

    return errors


def validate_dimension_consistency(
    dictionary: dict[str, Any], taxonomy_pack: dict[str, Any]
) -> list[str]:
    """
    Validate that dictionary entries are consistent with taxonomy dimensions.
    Returns list of errors.
    """
    errors: list[str] = []

    # Build valid dimension set from taxonomy pack
    valid_dimensions = {d["dimension_id"] for d in taxonomy_pack.get("dimensions", [])}

    entries = dictionary.get("entries", [])

    for i, entry in enumerate(entries):
        code = entry.get("code", "")
        dimension_id = entry.get("dimension_id", "")

        # Check dimension_id is valid
        if dimension_id and dimension_id not in valid_dimensions:
            errors.append(
                f"Entry {i} ({code}): dimension_id '{dimension_id}' not in taxonomy pack"
            )

        # Check code prefix matches dimension_id
        if code and dimension_id:
            prefix = code.split("-")[0] if "-" in code else ""
            if prefix != dimension_id:
                errors.append(
                    f"Entry {i} ({code}): code prefix '{prefix}' doesn't match "
                    f"dimension_id '{dimension_id}'"
                )

        # Check required fields have values
        required_fields = ["code", "label_en", "label_ja", "definition_en"]
        for field in required_fields:
            if not entry.get(field):
                errors.append(f"Entry {i} ({code}): missing required field '{field}'")

        # Check status is valid
        status = entry.get("status", "")
        if status and status not in {"active", "deprecated", "removed"}:
            errors.append(
                f"Entry {i} ({code}): invalid status '{status}'"
            )

    # Check all dimensions have at least one code
    dimension_codes: dict[str, list[str]] = {d: [] for d in valid_dimensions}
    for entry in entries:
        dim = entry.get("dimension_id", "")
        if dim in dimension_codes:
            dimension_codes[dim].append(entry.get("code", ""))

    for dim, codes in dimension_codes.items():
        if not codes:
            errors.append(f"Dimension '{dim}' has no codes in dictionary")

    return errors


def main() -> int:
    errors: list[str] = []

    # Check 1: Files exist
    for path in [DICTIONARY_JSON_PATH, DICTIONARY_SCHEMA_PATH, TAXONOMY_PACK_PATH]:
        if not path.exists():
            print(f"ERROR: {path.relative_to(REPO_ROOT)} does not exist")
            return 1

    # Load files
    try:
        dictionary = load_json(DICTIONARY_JSON_PATH)
        schema = load_json(DICTIONARY_SCHEMA_PATH)
        taxonomy_pack = load_json(TAXONOMY_PACK_PATH)
    except json.JSONDecodeError as e:
        print(f"ERROR: JSON parse error: {e}")
        return 1

    # Check 2: JSON Schema validation
    print(f"Validating: {DICTIONARY_JSON_PATH.relative_to(REPO_ROOT)}")
    schema_errors = validate_schema(dictionary, schema)
    errors.extend(schema_errors)

    # Check 3: Dimension consistency
    print(f"Checking dimension consistency with: {TAXONOMY_PACK_PATH.name}")
    consistency_errors = validate_dimension_consistency(dictionary, taxonomy_pack)
    errors.extend(consistency_errors)

    # Report results
    if errors:
        print("\nERROR: taxonomy_dictionary.json lint failed:")
        for err in errors:
            print(f"  {err}")
        return 1

    entry_count = len(dictionary.get("entries", []))
    print(f"\ntaxonomy_dictionary.json lint OK ({entry_count} entries validated)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
