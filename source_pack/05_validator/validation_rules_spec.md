# Validation Rules Specification (Authoring SSOT)

**Status**: Authoring input — not user-facing documentation  
**Canonical language**: English (EN)

This document defines the validation rules for the AIMO Standard. It mirrors `validator/rules/checks.md` and `validator/rules/checks.yaml`.

---

## Rule Definitions

### check: schema_validate_root

| Property | Value |
| --- | --- |
| **ID** | `schema_validate_root` |
| **Description** | Validate root object against `aimo-standard.schema.json` |
| **Required** | Yes |
| **Input** | Root JSON object (bundle) |
| **Schema** | `schemas/jsonschema/aimo-standard.schema.json` |
| **Error** | Schema validation failure messages |

**What it checks**:
- Root object has required fields: `version`, `dictionary`, `evidence`
- `dictionary` conforms to `aimo-dictionary.schema.json`
- `evidence` is an array of objects conforming to `aimo-ev.schema.json`
- No additional properties beyond those defined in schema

---

### check: schema_validate_dictionary

| Property | Value |
| --- | --- |
| **ID** | `schema_validate_dictionary` |
| **Description** | Validate dictionary object against `aimo-dictionary.schema.json` |
| **Required** | Yes |
| **Input** | Dictionary object |
| **Schema** | `schemas/jsonschema/aimo-dictionary.schema.json` |
| **Error** | Schema validation failure messages |

**What it checks**:
- Dictionary has required field: `entries`
- Each entry has required fields: `key`, `label`, `description`
- No additional properties beyond those defined in schema

---

### check: schema_validate_ev

| Property | Value |
| --- | --- |
| **ID** | `schema_validate_ev` |
| **Description** | Validate each evidence record against `aimo-ev.schema.json` |
| **Required** | Yes |
| **Input** | Each EV object in the `evidence` array |
| **Schema** | `schemas/jsonschema/aimo-ev.schema.json` |
| **Error** | Schema validation failure messages with path |

**What it checks**:
- Each EV record has required fields: `id`, `timestamp`, `source`, `summary`
- `tags` (if present) is an array of strings
- No additional properties beyond those defined in schema

---

## Machine-Readable Definition

From `validator/rules/checks.yaml`:

```yaml
version: 0.1
checks:
  - id: schema_validate_root
    description: Validate root object against aimo-standard.schema.json
    required: true
  - id: schema_validate_ev
    description: Validate each evidence record against aimo-ev.schema.json
    required: true
  - id: schema_validate_dictionary
    description: Validate dictionary object against aimo-dictionary.schema.json
    required: true
```

---

## Normative Statement

From `validator/rules/checks.md`:

> 1. MUST validate JSON artifacts against the published JSON Schemas.
> 2. MUST reject additionalProperties where schemas disallow them.
> 3. MUST ensure required fields exist.

---

## What Validator Does NOT Check

| Aspect | Reason |
| --- | --- |
| Content accuracy | Validator checks structure, not meaning |
| Traceability linkages | Cross-reference resolution not implemented |
| Timestamp validity | ISO-8601 format not strictly validated |
| ID uniqueness | Not currently enforced |
| Integrity controls | Adopter responsibility |

---

## Error Output Format

```
<path>: <message>
```

Example:
```
evidence.0.id: 'id' is a required property
dictionary.entries.0.key: 'key' is a required property
```

---

## Authoring Notes

- This spec mirrors `validator/rules/checks.md` (normative definition).
- `checks.yaml` is the machine-readable representation.
- New validation rules require updates to both this spec and `checks.yaml`.
