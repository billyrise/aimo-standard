# Reference Implementation Notes (Authoring SSOT)

**Status**: Authoring input — not user-facing documentation  
**Canonical language**: English (EN)

This document provides notes on the reference validator implementation (`validator/src/validate.py`).

---

## Overview

The reference validator is a Python script that validates AIMO evidence bundles against JSON schemas.

| Property | Value |
| --- | --- |
| **Location** | `validator/src/validate.py` |
| **Language** | Python 3.x |
| **Dependencies** | `jsonschema` (see `requirements.txt`) |
| **Schema version** | JSON Schema Draft 2020-12 |

---

## Usage

```bash
python validator/src/validate.py <path-to-root-json>
```

### Exit codes

| Code | Meaning |
| --- | --- |
| 0 | Validation passed ("OK") |
| 1 | Validation failed (errors printed to stderr) |
| 2 | Usage error (wrong arguments) |

---

## Implementation Details

### Schema Loading

```python
ROOT = Path(__file__).resolve().parents[2]
SCHEMAS_DIR = ROOT / "schemas" / "jsonschema"

def load_schema(name: str) -> dict:
    p = SCHEMAS_DIR / name
    return json.loads(p.read_text(encoding="utf-8"))
```

Schemas are loaded from `schemas/jsonschema/` relative to repository root.

### Resolver Setup

```python
def make_resolver():
    store = {
        "aimo-standard.schema.json": load_schema("aimo-standard.schema.json"),
        "aimo-dictionary.schema.json": load_schema("aimo-dictionary.schema.json"),
        "aimo-ev.schema.json": load_schema("aimo-ev.schema.json"),
    }
    return RefResolver.from_schema(store["aimo-standard.schema.json"], store=store)
```

The resolver enables `$ref` resolution for relative schema references.

### Validation

```python
def validate_json(payload: dict) -> None:
    schema = load_schema("aimo-standard.schema.json")
    resolver = make_resolver()
    validator = Draft202012Validator(schema, resolver=resolver)
    errors = sorted(validator.iter_errors(payload), key=lambda e: e.path)
    if errors:
        # Format and raise error
```

Uses `Draft202012Validator` from `jsonschema` library.

---

## Where Rules Live

| Rule source | Location | Format |
| --- | --- | --- |
| Normative definition | `validator/rules/checks.md` | Markdown |
| Machine-readable | `validator/rules/checks.yaml` | YAML |
| Implementation | `validator/src/validate.py` | Python |
| Schemas | `schemas/jsonschema/*.json` | JSON Schema |

---

## Extending the Validator

To add a new validation rule:

1. **Define in checks.md**: Add normative rule description.
2. **Add to checks.yaml**: Add machine-readable entry.
3. **Implement in validate.py**: Add validation logic.
4. **Update tests**: Add test cases in `validator/tests/test_validate.py`.
5. **Update this spec**: Document in `validation_rules_spec.md`.

---

## Test Suite

Location: `validator/tests/test_validate.py`

Run tests:
```bash
python -m pytest validator/tests/ -q
```

---

## Known Limitations

| Limitation | Description |
| --- | --- |
| No cross-reference validation | IDs referenced in `request_id`, `review_id`, etc. are not validated to exist |
| No timestamp format validation | ISO-8601 format is documented but not strictly enforced |
| No ID uniqueness check | Duplicate IDs are not detected |
| Single file validation | Bundle with multiple files requires root.json to inline or reference |

---

## Authoring Notes

- This implementation is reference quality; adopters may use their own validation.
- The validator is intentionally minimal; advanced features may be added in future versions.
- Breaking changes to validation require MAJOR version bump.
