# Dictionary

The AIMO Dictionary is the authoritative list of all valid codes within the taxonomy. It provides complete definitions for each code including labels, descriptions, and lifecycle information.

## Purpose and Audit Context

The dictionary serves as the **machine-readable reference** for:

1. **Evidence Templates**: Codes are used in EV templates to classify AI systems
2. **Validator**: The validator checks that all codes exist in the dictionary
3. **Coverage Map**: Codes enable mapping to external frameworks and regulations

!!! info "SSOT Principle"
    The dictionary CSV (`taxonomy_dictionary_v0.1.csv`) is the Single Source of Truth for all codes. Documentation pages (including this one) are derived explanations. When in doubt, refer to the CSV.

## Dictionary Format

The dictionary is distributed as a CSV file with **21 columns**:

| Column | Required | Description |
| --- | --- | --- |
| `standard_id` | Yes | Standard identifier (AIMO-STD) |
| `standard_version` | Yes | Version of the standard |
| `dimension_id` | Yes | Two-letter dimension ID (FS, UC, DT, etc.) |
| `dimension_name_en` | Yes | English dimension name |
| `dimension_name_ja` | Yes | Japanese dimension name |
| `code` | Yes | Full code (e.g., UC-001) |
| `label_en` | Yes | English label |
| `label_ja` | Yes | Japanese label |
| `definition_en` | Yes | English definition |
| `definition_ja` | Yes | Japanese definition |
| `scope_notes` | No | Clarifying notes on usage scope |
| `examples` | No | Pipe-separated examples |
| `status` | Yes | active, deprecated, or removed |
| `introduced_in` | Yes | Version when code was added |
| `deprecated_in` | No | Version when marked deprecated |
| `removed_in` | No | Version when removed |
| `replaced_by` | No | Replacement code if deprecated |
| `backward_compatible` | Yes | Whether change is backward compatible |
| `references` | No | External references |
| `owner` | Yes | Responsible party |
| `last_reviewed_date` | Yes | Last review date (YYYY-MM-DD) |

## Current Dictionary

The current dictionary version is **v0.1.0**.

**Download:** `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv`

### Code Counts by Dimension

| Dimension | Active Codes | Deprecated | Total |
| --- | --- | --- | --- |
| FS (Functional Scope) | 6 | 0 | 6 |
| UC (Use Case Class) | 30 | 0 | 30 |
| DT (Data Type) | 10 | 0 | 10 |
| CH (Channel) | 8 | 0 | 8 |
| IM (Integration Mode) | 7 | 0 | 7 |
| RS (Risk Surface) | 8 | 0 | 8 |
| OB (Outcome / Benefit) | 7 | 0 | 7 |
| EV (Evidence Type) | 15 | 0 | 15 |
| **Total** | **91** | **0** | **91** |

## CSV Column Definitions

### Identification Fields

- **standard_id**: Always `AIMO-STD` for the AIMO Standard
- **standard_version**: SemVer format (e.g., `0.1.0`)
- **dimension_id**: Two uppercase letters (FS, UC, DT, CH, IM, RS, OB, EV)
- **code**: Format `<DIM>-<TOKEN>` (e.g., `UC-001`)

### Label and Definition Fields

- **label_en / label_ja**: Short labels (max 50 characters recommended)
- **definition_en / definition_ja**: Full definitions (1-2 sentences)
- **scope_notes**: Clarifications on when to use/not use the code
- **examples**: Pipe-separated examples (e.g., `chatbot|recommendation`)

### Lifecycle Fields

- **status**: Current status of the code
  - `active`: Valid and in use
  - `deprecated`: Valid but scheduled for removal
  - `removed`: No longer valid
- **introduced_in**: Version when the code was first added
- **deprecated_in**: Version when marked as deprecated (empty if not deprecated)
- **removed_in**: Version when removed (empty if not removed)
- **replaced_by**: Replacement code(s) if deprecated
- **backward_compatible**: `true` if the change doesn't break existing usage

### Governance Fields

- **references**: External standards or documents referenced
- **owner**: Responsible party (e.g., `AIMO WG`)
- **last_reviewed_date**: Date of last review (YYYY-MM-DD)

## How Codes Are Used

### In Evidence Templates

Each EV template includes an 8-dimension codes table:

```markdown
## AIMO Codes (8 Dimensions)

| Dimension | Code(s) | Label |
| --- | --- | --- |
| **FS** | `FS-001` | End-user Productivity |
| **UC** | `UC-001`, `UC-002` | General Q&A, Summarization |
| ...
```

### In Validator

The validator checks:

1. All codes referenced in evidence exist in the dictionary
2. Code format matches the expected pattern
3. Deprecated codes trigger warnings
4. Removed codes are rejected

### In Coverage Map

Codes enable traceability to external frameworks:

```
UC-001 (General Q&A) → ISO/IEC 42001:2023 A.5.2.1
DT-004 (Personal Data) → GDPR Article 4(1)
```

## Backward Compatibility Policy

The `backward_compatible` field guides migration:

| Field Value | Implication | Auditor Action |
| --- | --- | --- |
| `true` | Existing evidence remains valid | No action required |
| `false` | Existing evidence may need updates | Review affected evidence |

### Version Compatibility Matrix

| Evidence Version | Dictionary Version | Compatibility |
| --- | --- | --- |
| 0.1.x | 0.1.x | Full |
| 0.1.x | 0.2.x | Full (new codes added, none removed) |
| 0.1.x | 1.0.x | Review required (breaking changes possible) |

## Audit Verification Points

When reviewing evidence, auditors should verify:

| Check | What to Look For |
| --- | --- |
| **Definition clarity** | Does `definition_en/ja` clearly describe the code's meaning? |
| **Status validity** | Is the code `active` (not `deprecated` or `removed`)? |
| **Version alignment** | Does `introduced_in` ≤ evidence's `taxonomy_version`? |
| **Completeness** | Are all required dimensions covered? |

## Extension Guidelines

Organizations MAY extend the dictionary with custom codes following these rules:

### Extension Prefix

Custom codes SHOULD use an organization-specific prefix:

```
X-<ORG>-<DIM>-<TOKEN>
```

Example: `X-ACME-UC-901` for ACME Corporation's custom use case code.

### Extension Requirements

1. Custom codes MUST NOT conflict with standard codes
2. Custom codes SHOULD be documented in a local extension dictionary
3. Extensions SHOULD be submitted to AIMO WG for potential standardization
4. When exchanging evidence with external parties, use only standard codes

## Schema Reference

The dictionary is validated against the taxonomy pack schema:

- **Taxonomy Pack Schema**: `source_pack/03_taxonomy/schemas/taxonomy_pack.schema.json`
- **Taxonomy Pack JSON**: `source_pack/03_taxonomy/taxonomy_pack_v0.1.json`

## Downloads

| File | Description |
| --- | --- |
| `taxonomy_dictionary_v0.1.csv` | Full dictionary in CSV format (91 codes) |
| `taxonomy_en.yaml` | English taxonomy (generated from CSV) |
| `taxonomy_ja.yaml` | Japanese taxonomy (generated from CSV) |
| `taxonomy_pack_v0.1.json` | Taxonomy pack with dimension metadata |
| `taxonomy_pack.schema.json` | JSON Schema for taxonomy pack |

See [Releases](../../releases/index.md) for downloadable packages.

## References

- [Taxonomy](./03-taxonomy.md) - Dimension definitions
- [Codes](./04-codes.md) - Code format and usage
- [Evidence Templates](./06-ev-template.md) - How codes are used in templates
- [Validator](./07-validator.md) - Code validation rules
- [Changelog](./08-changelog.md) - Version history
