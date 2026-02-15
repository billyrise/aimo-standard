---
description: Shadow AI Discovery Log Schema - Vendor-neutral format for documenting detection, inventory, and remediation of unapproved AI usage in enterprises.
---
<!-- aimo:translation_status=source -->

# Shadow AI Discovery Log Schema

## Purpose

This schema defines a vendor-neutral format for logs that document the detection, inventory, and remediation of **unapproved AI usage (Shadow AI)**. It enables organizations to:

- Maintain an auditable record of Shadow AI detection events
- Normalize logs from various sources (CASB, proxy, IdP, EDR, SaaS audit logs) into a consistent format
- Support evidence submission for compliance and audit purposes

## Normalization principles

| Principle | Description |
| --- | --- |
| **Vendor-neutral** | No dependency on specific vendor log formats; applicable to Netskope, Zscaler, Microsoft Defender, and others |
| **Minimal required fields** | Only essential fields are MUST; organizations can omit optional fields |
| **Extensible** | `additionalProperties: true` allows vendor-specific or organization-specific extensions |
| **Privacy-aware** | Fields are designed to reference (not embed) sensitive content |

## Required fields (MUST)

| Field | Type | Description | Example |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | Timestamp of the event | `2026-01-15T09:30:00Z` |
| `actor_id` | string | User or service identifier | `user@example.com` |
| `actor_type` | string | Type of actor | `user` or `service` |
| `source_system` | string | System that detected the event | `proxy`, `casb`, `idp`, `edr`, `saas_audit` |
| `ai_service` | string | AI product or domain accessed | `chat.openai.com`, `claude.ai` |
| `action` | string | Action performed | `chat`, `upload`, `download`, `tool_execute`, `api_call` |
| `data_classification` | string | Data classification level | `public`, `internal`, `confidential`, `restricted` |
| `decision` | string | Policy decision applied | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | Reference to related evidence | `sha256:abc123...` or `urn:evidence:...` |
| `record_id` | string | Unique identifier for this record | `evt-20260115-001` |

## Optional fields (SHOULD/MAY)

| Field | Type | Description |
| --- | --- | --- |
| `session_id` | string | Session identifier |
| `device_id` | string | Device identifier |
| `ip` | string | IP address |
| `user_agent` | string | User agent string |
| `department` | string | Organizational department |
| `project_id` | string | Project identifier |
| `prompt_category` | string | Category of the prompt/query |
| `model_family` | string | AI model family (e.g., GPT-4, Claude) |
| `destination` | string | Destination URL or endpoint |
| `policy_id` | string | Policy that triggered the decision |
| `remediation_ticket` | string | Remediation ticket reference |

## Privacy/Security notes

!!! warning "Data handling"
    - **Do not embed** PII, credentials, or prompt content directly in log fields.
    - Use `evidence_ref` to reference separately stored sensitive content.
    - Apply appropriate access controls to log storage.
    - Consider data retention policies aligned with [Minimum Evidence Requirements](../../minimum-evidence/).

## JSON Schema

Download: [shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "event_time", "actor_id", "actor_type", "source_system",
    "ai_service", "action", "data_classification", "decision",
    "evidence_ref", "record_id"
  ],
  "properties": {
    "event_time": { "type": "string", "format": "date-time" },
    "actor_id": { "type": "string", "minLength": 1 },
    "actor_type": { "type": "string", "enum": ["user", "service"] },
    "source_system": { "type": "string", "minLength": 1 },
    "ai_service": { "type": "string", "minLength": 1 },
    "action": { "type": "string", "minLength": 1 },
    "data_classification": { "type": "string", "minLength": 1 },
    "decision": { "type": "string", "enum": ["allow", "block", "needs_review", "unknown"] },
    "evidence_ref": { "type": "string", "minLength": 1 },
    "record_id": { "type": "string", "minLength": 1 }
  },
  "additionalProperties": true
}
```

## Related pages

- [Log Schemas index](../)
- [Agent Activity Log](../agent-activity/)
- [Minimum Evidence Requirements](../../minimum-evidence/)
- [Taxonomy: IM-007 Shadow/Unmanaged](../../../standard/current/03-taxonomy/)
