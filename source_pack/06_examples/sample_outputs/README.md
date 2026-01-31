# Sample Outputs (Authoring SSOT)

**Status**: Placeholder directory for sample output files  
**Canonical language**: English (EN)

This directory is intended to contain sample output files (completed evidence bundles, validation results).

---

## Purpose

Sample outputs demonstrate:
- Completed evidence bundles in proper format
- Validator output (success and error cases)
- Checksum files
- Bundle packaging

---

## What Belongs Here

| File type | Description | Source |
| --- | --- | --- |
| Completed bundles | `root.json` with all sections | From `sample_inputs/` transformation |
| Dictionary files | `dictionary.json` with entries | Extracted from bundle |
| Validation logs | Validator stdout/stderr | From `validate.py` execution |
| Checksum files | `SHA256SUMS.txt` | From `sha256sum` command |
| Package archives | `evidence_bundle.zip` | From `zip` command |

---

## Validation Output Examples

### Success case

```
$ python validator/src/validate.py root.json
OK
```

### Error case

```
$ python validator/src/validate.py invalid.json
Schema validation failed:
evidence.0.id: 'id' is a required property
dictionary.entries.0.key: 'key' is a required property
```

---

## Anonymization Requirements

Same as `sample_inputs/`:
- No PII, credentials, or sensitive data
- Use fictional dates and organization names
- Review for business sensitivity

---

## Current Status

This directory is a placeholder. Sample outputs will be added as authoritative examples are developed.

**TBD**: Add sample output files corresponding to inputs.

---

## Existing Examples

The repository already contains examples at:
- `examples/minimal/` — minimal sample files
- `examples/evidence_bundle_minimal/` — minimal complete bundle

These can be referenced for output format guidance.

---

## Authoring Notes

- Outputs should correspond to inputs in `sample_inputs/`.
- Include both success and error scenarios.
- Demonstrate full workflow from input to packaged bundle.
