# EV Template (Human-readable)

This template defines the structure of evidence records aligned with the AIMO Taxonomy.

**Reference Documentation:**

- [Taxonomy](../../docs/standard/current/03-taxonomy.md) - Dimension definitions
- [Codes](../../docs/standard/current/04-codes.md) - Code format and lifecycle
- [Dictionary](../../docs/standard/current/05-dictionary.md) - Complete code listings

---

## Evidence Record Structure

### Required Fields (MUST)

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Unique evidence identifier |
| `timestamp` | string | ISO-8601 timestamp |
| `source` | string | Origin of evidence (system, doc, log, etc.) |
| `summary` | string | Short summary of evidence |

### Taxonomy Fields (SHOULD)

| Field | Type | Description |
| --- | --- | --- |
| `taxonomy_version` | string | Version of taxonomy dictionary (e.g., `0.1.0`) |
| `codes` | object | AIMO taxonomy codes by dimension (see below) |

### Optional Fields

| Field | Type | Description |
| --- | --- | --- |
| `tags` | array | Additional freeform tags for searching |
| `request_id` | string | Reference to request record |
| `review_id` | string | Reference to review record |
| `exception_id` | string | Reference to exception record |
| `renewal_id` | string | Reference to renewal record |

---

## AIMO Codes Structure

The `codes` object contains taxonomy codes by dimension. Format: `<DIM>-<NNN>`

```json
"codes": {
  "FS": ["FS-001"],
  "UC": ["UC-001", "UC-002"],
  "DT": ["DT-002", "DT-004"],
  "CH": ["CH-001"],
  "IM": ["IM-002"],
  "RS": ["RS-001"],
  "OB": ["OB-001"],
  "EV": ["EV-001", "EV-002"]
}
```

### Dimension Requirements

| Dimension | Required | Selection | Description |
| --- | --- | --- | --- |
| **FS** | Yes | Exactly 1 | Functional Scope |
| **UC** | Yes | 1 or more | Use Case Class |
| **DT** | Yes | 1 or more | Data Type |
| **CH** | Yes | 1 or more | Channel |
| **IM** | Yes | Exactly 1 | Integration Mode |
| **RS** | Yes | 1 or more | Risk Surface |
| **OB** | No | 0 or more | Outcome/Benefit |
| **EV** | Yes | 1 or more | Evidence Type |

---

## Bundle Root (Optional Lifecycle Objects)

When using the root schema (`aimo-standard.schema.json`), the following are optional at root level:

- **request**: identifier, timestamp(s), actor/role, scope, rationale
- **review**: identifier, timestamp(s), actor/role, decision, scope, rationale
- **exception**: identifier, timestamp(s), scope, expiry, compensating controls
- **renewal**: identifier, timestamp(s), actor/role, decision, references
- **change_log**: identifier, timestamp, actor, change description

See [Evidence Bundle](../../docs/artifacts/evidence-bundle.md) for full documentation.

---

## Validation

Evidence records are validated against:

1. **Schema**: `schemas/jsonschema/aimo-ev.schema.json`
2. **Code format**: Pattern `^(FS|UC|DT|CH|IM|RS|OB|EV)-\d{3}$`
3. **Dictionary**: Codes should exist in `taxonomy_dictionary_v0.1.csv`

Run: `python validator/src/validate.py <path-to-root.json>`
