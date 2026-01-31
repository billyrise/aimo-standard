# EV Template — Minimum (Authoring SSOT)

**Status**: Authoring input — not user-facing documentation  
**Canonical language**: English (EN)

This document defines the minimum authoring template for Evidence (EV) records. It is extracted from `templates/ev/ev_template.md` and aligned with `schemas/jsonschema/aimo-ev.schema.json`.

---

## Minimum EV Record Structure

An EV record MUST contain the following fields:

| Field | Type | Required | Description | Schema reference |
| --- | --- | --- | --- | --- |
| `id` | string | **MUST** | Unique evidence identifier | `aimo-ev.schema.json#/properties/id` |
| `timestamp` | string | **MUST** | ISO-8601 timestamp | `aimo-ev.schema.json#/properties/timestamp` |
| `source` | string | **MUST** | Origin of evidence (system, doc, log, etc.) | `aimo-ev.schema.json#/properties/source` |
| `summary` | string | **MUST** | Short summary of evidence | `aimo-ev.schema.json#/properties/summary` |

---

## JSON Example (Minimum)

```json
{
  "id": "EV-000001",
  "timestamp": "2026-01-01T00:00:00Z",
  "source": "example-system",
  "summary": "Example evidence record."
}
```

**Source**: `templates/ev/ev_template.json`

---

## Field Guidelines

### id

- **Format**: Recommended pattern `EV-{sequence}` (e.g., `EV-000001`).
- **Uniqueness**: Must be unique within the Evidence Bundle.
- **Stability**: Once assigned, id should not change.

### timestamp

- **Format**: ISO-8601 (e.g., `2026-01-15T10:00:00Z`).
- **Timezone**: UTC preferred; if local, include offset.
- **Meaning**: When the evidence was created or recorded.

### source

- **Examples**: `"production-log"`, `"hr-system"`, `"manual-review"`, `"audit-tool"`.
- **Purpose**: Traceability to origin system or process.

### summary

- **Length**: Concise; 1-2 sentences recommended.
- **Content**: What the evidence shows or proves.

---

## Validation

Minimum EV records are validated against `schemas/jsonschema/aimo-ev.schema.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://aimoaas.com/standard/schemas/aimo-ev.schema.json",
  "title": "AIMO EV (Evidence) Record",
  "type": "object",
  "additionalProperties": false,
  "required": ["id", "timestamp", "source", "summary"],
  "properties": {
    "id": { "type": "string" },
    "timestamp": { "type": "string", "description": "ISO-8601 timestamp" },
    "source": { "type": "string" },
    "summary": { "type": "string" },
    "tags": {
      "type": "array",
      "items": { "type": "string" }
    }
  }
}
```

---

## Authoring Notes

- This is the minimum template; see `ev_template_full.md` for optional fields.
- User-facing template is at `templates/ev/ev_template.md`.
- Schema is at `schemas/jsonschema/aimo-ev.schema.json`.
