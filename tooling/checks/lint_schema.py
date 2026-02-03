#!/usr/bin/env python3
"""
Schema Lint - Validates JSON Schema files and example conformance.

Checks:
1. All schemas in schemas/jsonschema/ are valid JSON Schema (draft 2020-12)
2. Example files in examples/ conform to their corresponding schemas

Schema-Example Mappings:
- evidence_pack_manifest.schema.json ↔ examples/evidence_pack/*.json
- aimo-dictionary.schema.json ↔ examples/**/dictionary.json, sample_dictionary.json
- aimo-ev.schema.json ↔ examples/**/sample_ev.json
- aimo-standard.schema.json ↔ examples/**/root.json

Usage:
    python tooling/checks/lint_schema.py

Exit codes:
    0 - All schemas valid and examples conform
    1 - Errors found
"""

import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator, ValidationError

# Try to import referencing for local $ref resolution
try:
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT202012
    HAS_REFERENCING = True
except ImportError:
    HAS_REFERENCING = False

ROOT = Path(__file__).resolve().parents[2]
SCHEMAS = ROOT / "schemas" / "jsonschema"
EXAMPLES = ROOT / "examples"
SOURCE_PACK_EV = ROOT / "source_pack" / "04_evidence_pack"

# Mapping of schema filename to example file patterns
SCHEMA_EXAMPLE_MAP = {
    "evidence_pack_manifest.schema.json": [
        "examples/evidence_pack/*.json",
        "source_pack/04_evidence_pack/examples/*.json",
    ],
    "evidence_bundle_manifest.schema.json": [
        "examples/evidence_bundle_v01_minimal/manifest.json",
    ],
    "aimo-dictionary.schema.json": [
        "examples/**/dictionary.json",
        "examples/**/sample_dictionary.json",
    ],
    "aimo-ev.schema.json": [
        "examples/**/sample_ev.json",
    ],
    "aimo-standard.schema.json": [
        "examples/**/root.json",
    ],
}


def build_schema_registry():
    """Build a registry of all local schemas for $ref resolution."""
    if not HAS_REFERENCING:
        return None
    
    resources = []
    for schema_file in SCHEMAS.glob("*.json"):
        try:
            schema = json.loads(schema_file.read_text(encoding="utf-8"))
            schema_id = schema.get("$id", schema_file.name)
            
            # Create resource with both the full $id and just the filename
            resource = Resource.from_contents(schema, default_specification=DRAFT202012)
            resources.append((schema_id, resource))
            
            # Also register with just the filename for relative $ref resolution
            resources.append((schema_file.name, resource))
        except Exception:
            pass
    
    registry = Registry()
    for uri, resource in resources:
        registry = registry.with_resource(uri, resource)
    
    return registry


def validate_example(schema_path: Path, example_path: Path, registry=None) -> list[str]:
    """Validate an example file against a schema. Returns list of errors."""
    errors = []
    
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        if registry is not None:
            validator = Draft202012Validator(schema, registry=registry)
        else:
            validator = Draft202012Validator(schema)
    except Exception as e:
        errors.append(f"Schema load error {schema_path.name}: {e}")
        return errors
    
    try:
        example = json.loads(example_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errors.append(f"Invalid JSON in {example_path.relative_to(ROOT)}: {e}")
        return errors
    
    try:
        for error in validator.iter_errors(example):
            path = ".".join(str(p) for p in error.absolute_path) if error.absolute_path else "(root)"
            errors.append(
                f"{example_path.relative_to(ROOT)}: {path}: {error.message}"
            )
    except Exception as e:
        # Catch $ref resolution errors
        errors.append(f"{example_path.relative_to(ROOT)}: Validation error: {e}")
    
    return errors


def main():
    errors = []
    validated_schemas = 0
    validated_examples = 0
    
    print("=== Schema Syntax Check ===")
    
    # 1. Validate all schemas
    for p in sorted(SCHEMAS.glob("*.json")):
        try:
            schema = json.loads(p.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            validated_schemas += 1
            print(f"  OK: {p.name}")
        except Exception as e:
            errors.append(f"Schema syntax error in {p.name}: {e}")
            print(f"  FAIL: {p.name}")
    
    print()
    print("=== Example Validation ===")
    
    # Build registry for local $ref resolution
    registry = build_schema_registry()
    if registry is None:
        print("  NOTE: referencing module not available, $ref resolution may fail")
    
    # 2. Validate examples against schemas
    for schema_name, patterns in SCHEMA_EXAMPLE_MAP.items():
        schema_path = SCHEMAS / schema_name
        if not schema_path.exists():
            print(f"  SKIP: {schema_name} (schema not found)")
            continue
        
        example_files = []
        for pattern in patterns:
            # Convert pattern to glob-friendly format
            if pattern.startswith("examples/"):
                base_dir = ROOT
            elif pattern.startswith("source_pack/"):
                base_dir = ROOT
            else:
                base_dir = EXAMPLES
            
            # Handle patterns like "examples/**/*.json"
            if "**" in pattern:
                # Split into directory and file pattern
                glob_pattern = pattern
            else:
                glob_pattern = pattern
            
            for match in base_dir.glob(pattern):
                if match.is_file():
                    example_files.append(match)
        
        if not example_files:
            print(f"  SKIP: {schema_name} (no examples found)")
            continue
        
        for example_path in example_files:
            example_errors = validate_example(schema_path, example_path, registry=registry)
            if example_errors:
                errors.extend(example_errors)
                print(f"  FAIL: {example_path.relative_to(ROOT)} vs {schema_name}")
            else:
                validated_examples += 1
                print(f"  OK: {example_path.relative_to(ROOT)} vs {schema_name}")
    
    print()
    print(f"Validated: {validated_schemas} schemas, {validated_examples} examples")
    
    if errors:
        print()
        print("=" * 60)
        print("ERRORS:")
        print("=" * 60)
        for e in errors:
            print(f"  {e}")
        print()
        print("schema lint FAILED", file=sys.stderr)
        sys.exit(1)

    print()
    print("schema lint OK")
    sys.exit(0)


if __name__ == "__main__":
    main()
