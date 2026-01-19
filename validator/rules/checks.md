# Validator Checks (Normative)

This document defines validator checks.

## Checks
1. MUST validate JSON artifacts against the published JSON Schemas.
2. MUST reject additionalProperties where schemas disallow them.
3. MUST ensure required fields exist.

## Notes
- This is the normative definition of checks.
- `checks.yaml` is the machine-readable representation of this document.
