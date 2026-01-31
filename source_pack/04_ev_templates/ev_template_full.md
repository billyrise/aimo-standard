# EV Template — Full (Authoring SSOT)

**Status**: Authoring input — not user-facing documentation  
**Canonical language**: English (EN)

This document defines the full authoring template for Evidence (EV) records, including optional fields and lifecycle objects. It extends `ev_template_min.md`.

---

## Full EV Record Structure

### Required Fields (MUST)

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Unique evidence identifier |
| `timestamp` | string | ISO-8601 timestamp |
| `source` | string | Origin of evidence |
| `summary` | string | Short summary |

### Optional Fields (SHOULD where applicable)

| Field | Type | Description | Use case |
| --- | --- | --- | --- |
| `tags` | array[string] | Keywords for categorization | Filtering, search |
| `request_id` | string | Reference to request record | Traceability |
| `review_id` | string | Reference to review/approval record | Traceability |
| `exception_id` | string | Reference to exception record | Exception handling |
| `renewal_id` | string | Reference to renewal record | Re-evaluation tracking |

---

## JSON Example (Full)

```json
{
  "id": "EV-001",
  "timestamp": "2026-01-15T10:00:00Z",
  "source": "example-system",
  "summary": "Minimal evidence record for Evidence Bundle example.",
  "tags": ["example", "evidence-bundle"],
  "request_id": "REQ-001",
  "review_id": "REV-001"
}
```

---

## Bundle Root Lifecycle Objects

When using the root schema (`aimo-standard.schema.json`), the following lifecycle objects are optional at bundle root level. If present, they support the lifecycle groups in Minimum Evidence Requirements.

### request

```json
{
  "id": "REQ-001",
  "timestamp": "2026-01-10T09:00:00Z",
  "actor": "requester",
  "scope": "Example AI use",
  "rationale": "Minimal bundle example"
}
```

**MUST fields** (per Minimum Evidence Requirements):
- id, timestamp, actor/role, scope, rationale

### review

```json
{
  "id": "REV-001",
  "timestamp": "2026-01-12T14:00:00Z",
  "actor": "reviewer",
  "decision": "approved",
  "rationale": "Within policy",
  "references": ["REQ-001"]
}
```

**MUST fields**:
- id, timestamp, actor/role, decision, scope, rationale, reference to request

### exception

```json
{
  "id": "EXC-001",
  "timestamp": "2026-01-14T11:00:00Z",
  "scope": "Exception scope description",
  "expiry": "2026-07-14",
  "compensating_controls": "Description of compensating controls",
  "rationale": "Reason for exception",
  "references": ["REQ-001", "REV-001"]
}
```

**MUST fields**:
- id, timestamp, scope, expiry, compensating controls, rationale, references

### renewal

```json
{
  "id": "REN-001",
  "timestamp": "2026-07-10T09:00:00Z",
  "actor": "reviewer",
  "decision": "renewed",
  "references": ["EXC-001", "REQ-001"]
}
```

**MUST fields**:
- id, timestamp, actor/role, decision, references to prior exception/request/review

### change_log

```json
{
  "id": "CHG-001",
  "timestamp": "2026-01-15T10:00:00Z",
  "actor": "system",
  "change_description": "Initial bundle creation",
  "references": ["EV-001"]
}
```

**MUST fields**:
- id, timestamp, actor, change description, references

---

## Complete Bundle Root Example

```json
{
  "version": "v0.1.0",
  "dictionary": {
    "entries": [
      { "key": "REQ-001", "label": "Request", "description": "AI use request" },
      { "key": "EV-001", "label": "Evidence", "description": "Use evidence record" }
    ]
  },
  "evidence": [
    {
      "id": "EV-001",
      "timestamp": "2026-01-15T10:00:00Z",
      "source": "example-system",
      "summary": "Minimal evidence record.",
      "tags": ["example"]
    }
  ],
  "request": { ... },
  "review": { ... },
  "change_log": { ... }
}
```

**Source**: `examples/evidence_bundle_minimal/root.json`

---

## Schema Reference

Root schema: `schemas/jsonschema/aimo-standard.schema.json`

```json
{
  "required": ["version", "dictionary", "evidence"],
  "properties": {
    "version": { "type": "string" },
    "dictionary": { "$ref": "aimo-dictionary.schema.json" },
    "evidence": { "type": "array", "items": { "$ref": "aimo-ev.schema.json" } },
    "request": { "type": "object" },
    "review": { "type": "object" },
    "exception": { "type": "object" },
    "renewal": { "type": "object" },
    "change_log": { "type": "object" }
  }
}
```

**Note**: Lifecycle objects (request, review, exception, renewal, change_log) are schema-optional but Minimum Evidence Requirements specify MUST fields when present.

---

## Authoring Notes

- This template combines EV records with bundle-level lifecycle objects.
- User-facing template is at `templates/ev/ev_template.md`.
- Fields above are documented as MUST in Minimum Evidence Requirements; schema keeps them optional for backward compatibility.
