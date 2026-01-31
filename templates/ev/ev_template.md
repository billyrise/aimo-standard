# EV Template (Human-readable)

This template defines the minimal structure of evidence records and, at bundle root level, optional lifecycle objects (request, review, exception, renewal, change_log). See docs: Evidence Bundle and Minimum Evidence Requirements (Artifacts section). for the full bundle TOC and MUST-level checklist.

## Evidence record (per item in `evidence` array)

### Required fields (MUST)
- id: unique evidence identifier
- timestamp: ISO-8601 timestamp
- source: origin of evidence (system, doc, log, etc.)
- summary: short summary of evidence

### Optional fields (SHOULD where applicable)
- tags: list of keywords
- request_id, review_id, exception_id, renewal_id: references for traceability (see Evidence Bundle traceability rules)

## Bundle root (optional lifecycle objects)

When using the root schema (aimo-standard.schema.json), the following are optional at root level. If present, they support the lifecycle groups in Minimum Evidence Requirements.

- **request**: identifier, timestamp(s), actor/role, scope, rationale (MUST for request lifecycle).
- **review**: identifier, timestamp(s), actor/role, decision, scope, rationale, reference to request (MUST for review/approval lifecycle).
- **exception**: identifier, timestamp(s), scope, expiry, compensating controls, rationale, reference to review/request (MUST for exception lifecycle).
- **renewal**: identifier, timestamp(s), actor/role, decision, references to prior exception/request/review (MUST for renewal lifecycle).
- **change_log**: identifier, timestamp, actor, change description, references (MUST for change control).

Fields above are documented as MUST in the Minimum Evidence Requirements; the schema keeps them optional for backward compatibility.
