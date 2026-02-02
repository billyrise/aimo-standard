---
description: AIMO Validator - Ensures Evidence Packs conform to AIMO Standard schemas. Validation rules, error handling, and reference implementation for compliance checks.
# TRANSLATION METADATA - DO NOT REMOVE
source_file: en/standard/current/07-validator.md
source_hash: d72cf764d049937a
translation_date: 2026-02-02
translator: pending
translation_status: needs_translation
---

# Validator

The AIMO Validator ensures that Evidence Packs and related artifacts conform to the AIMO Standard schemas and requirements.

See also: [Human Oversight Protocol](../../governance/human-oversight-protocol.md) — responsibility boundary for machine vs. human review.

## Validator in practice

For a 30-second quickstart (install, run, interpret output), see [Validator hub](../../validator/index.md).

## Validator MVP Requirements

The minimum viable validator MUST perform the following checks:

### 1. Required Field Validation

Check that all mandatory fields are present:

| Artifact | Required Fields |
| --- | --- |
| Evidence Pack Manifest | pack_id, pack_version, taxonomy_version, created_date, last_updated, codes, evidence_files |
| Codes Object | FS, UC, DT, CH, IM, RS, EV (OB optional) |
| Evidence File Entry | file_id, filename, ev_type, title |

### 2. Dimension Code Validation

Check that each required dimension has at least one code:

| Dimension | Requirement |
| --- | --- |
| FS (Functional Scope) | Exactly 1 code |
| UC (Use Case Class) | At least 1 code |
| DT (Data Type) | At least 1 code |
| CH (Channel) | At least 1 code |
| IM (Integration Mode) | Exactly 1 code |
| RS (Risk Surface) | At least 1 code |
| OB (Outcome / Benefit) | Optional (0 or more) |
| EV (Evidence Type) | At least 1 code |

### 3. Dictionary Existence Check

Validate that all codes exist in the taxonomy dictionary:

- Load the taxonomy dictionary for the specified `taxonomy_version`
- Verify each code in the manifest exists in the dictionary
- Report invalid codes with their dimension and value

### 4. Code Format Validation

Check that all codes match the expected format:

```regex
^(FS|UC|DT|CH|IM|RS|OB|EV)-\d{3}$
```

### 5. Schema Validation

Validate against JSON Schemas:

| Schema | Purpose |
| --- | --- |
| `evidence_pack_manifest.schema.json` | Evidence Pack manifests |
| `taxonomy_pack.schema.json` | Taxonomy pack definitions |
| `changelog.schema.json` | Changelog entries |

## Validation Rules

### Rule: Required Dimensions

```yaml
rule_id: required_dimensions
description: All required dimensions must have at least one code
severity: error
check: |
  - FS: exactly 1
  - UC: at least 1
  - DT: at least 1
  - CH: at least 1
  - IM: exactly 1
  - RS: at least 1
  - EV: at least 1
```

### Rule: Valid Codes

```yaml
rule_id: valid_codes
description: All codes must exist in the taxonomy dictionary
severity: error
check: |
  For each code in manifest.codes:
    - Code exists in dictionary for specified taxonomy_version
    - Code status is 'active' (warn if 'deprecated')
```

### Rule: Code Format

```yaml
rule_id: code_format
description: All codes must match the standard format
severity: error
pattern: "^(FS|UC|DT|CH|IM|RS|OB|EV)-\\d{3}$"
```

### Rule: Version Format

```yaml
rule_id: version_format
description: Versions must be valid SemVer
severity: error
pattern: "^\\d+\\.\\d+\\.\\d+$"
fields:
  - pack_version
  - taxonomy_version
```

## Error Output Format

Validation errors are reported in the following format:

```
<path>: <severity>: <message>
```

**Examples:**

```
codes.FS: error: Required dimension 'FS' has no codes
codes.UC[0]: error: Code 'UC-999' does not exist in dictionary v0.1.0
pack_version: error: Invalid version format 'v1.0' (expected SemVer)
codes.RS[1]: warning: Code 'RS-002' is deprecated in v0.2.0
```

## What Validator Does NOT Check

The validator focuses on structural conformance, not content quality:

| Aspect | Reason |
| --- | --- |
| Content accuracy | Validator checks structure, not meaning |
| Evidence completeness | Templates are guides, not enforced formats |
| Cross-reference resolution | File existence not verified |
| Timestamp validity | ISO-8601 not strictly validated |
| ID uniqueness | Not currently enforced |
| Integrity hashes | Adopter responsibility |

## Reference Implementation

A reference implementation is provided in Python:

```
validator/src/validate.py
```

### Usage

```bash
python validator/src/validate.py <manifest.json>
```

### Example Output

```
Validating: evidence_pack_manifest.json
Taxonomy version: 0.1.0

Checking required dimensions...
  FS: OK (1 code)
  UC: OK (3 codes)
  DT: OK (1 code)
  CH: OK (1 code)
  IM: OK (1 code)
  RS: OK (3 codes)
  OB: OK (2 codes)
  EV: OK (7 codes)

Checking code validity...
  All codes valid.

Validation: PASSED
```

## Versioning Policy

Validator rules follow SemVer:

- **MAJOR**: Breaking rule changes (new required checks that fail existing valid packs)
- **MINOR**: New optional checks, warnings, or informational messages
- **PATCH**: Bug fixes that don't change validation outcomes

## Schema References

| Schema | Location |
| --- | --- |
| Evidence Pack Manifest | `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json` |
| Taxonomy Pack | `source_pack/03_taxonomy/schemas/taxonomy_pack.schema.json` |
| Changelog | `source_pack/03_taxonomy/schemas/changelog.schema.json` |

## References

- [Taxonomy](./03-taxonomy.md) - Dimension definitions
- [Codes](./04-codes.md) - Code format
- [Dictionary](./05-dictionary.md) - Code dictionary
- [Validator Rules](../../validator/index.md) - Full rule documentation
