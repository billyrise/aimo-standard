# Validator Checks (Normative)

This document defines validator checks.

## Checks
1. MUST validate JSON artifacts against the published JSON Schemas.
2. MUST reject additionalProperties where schemas disallow them.
3. MUST ensure required fields exist.

## Notes
- This is the normative definition of checks.
- `checks.yaml` is the machine-readable representation of this document.
- The root schema (aimo-standard.schema.json) allows optional lifecycle objects at root: request, review, exception, renewal, change_log. If present, they are not structurally validated beyond being objects; content expectations are defined in docs (Evidence Bundle, Minimum Evidence Requirements).
