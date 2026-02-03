# Validator Checks (Normative)

This document defines validator checks aligned with the AIMO Taxonomy.

## Checks

### Required Checks

1. **MUST** validate JSON artifacts against the published JSON Schemas.
2. **MUST** reject additionalProperties where schemas disallow them.
3. **MUST** ensure required fields exist.
4. **MUST** validate AIMO code format: `^(FS|UC|DT|CH|IM|RS|OB|LG)-\d{3}$` (taxonomy dimensions). The **EV-** prefix is reserved for Evidence artifact IDs only; taxonomy dimension for log/event type is **LG** only. Use of **EV** in `evidence[].codes` is rejected with a normative error.

### Recommended Checks

5. **SHOULD** verify `taxonomy_version` is specified in evidence records.
6. **SHOULD** verify required dimensions (FS, UC, DT, CH, IM, RS, LG) each have at least one code.
7. **SHOULD** warn when deprecated codes are used.

## Code Format Validation

The validator checks that all codes in the `codes` object match the pattern:

```
^(FS|UC|DT|CH|IM|RS|OB|LG)-\d{3}$
```

(Taxonomy dimension for log/event type is **LG** only. **EV-** is reserved for Evidence artifact IDs; use of EV in codes is rejected by the validator.)

Examples of valid codes:
- `FS-001`, `UC-015`, `DT-004`, `CH-003`, `IM-002`, `RS-008`, `OB-007`, `LG-001`

Examples of invalid codes:
- `FS-1` (wrong token format)
- `XX-001` (invalid dimension)
- `FS001` (missing hyphen)

## Dictionary Validation

Dictionary entries are validated for:

1. **Required fields**: `code`, `label_en`, `label_ja`, `definition_en`
2. **Code format**: Must match the AIMO code pattern
3. **Status values**: Must be `active`, `deprecated`, or `removed`

## Notes

- `checks.yaml` is the machine-readable representation of this document.
- Full code existence validation against `taxonomy_dictionary_v0.1.csv` is available via `lint_taxonomy_dictionary.py`.
- The root schema allows optional lifecycle objects at root: request, review, exception, renewal, change_log.

## References

- [Taxonomy](../../docs/standard/current/03-taxonomy.md) - Dimension definitions
- [Codes](../../docs/standard/current/04-codes.md) - Code format and lifecycle
- [Dictionary](../../docs/standard/current/05-dictionary.md) - Column definitions
