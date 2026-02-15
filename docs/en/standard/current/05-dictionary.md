---
description: AIMO Dictionary - Authoritative list of 91 taxonomy codes across 8 dimensions. Complete definitions, labels, and lifecycle information for AI classification.
---
<!-- aimo:translation_status=source -->

# Dictionary

The AIMO Dictionary is the authoritative list of all valid codes within the taxonomy. It provides complete definitions for each code including labels, descriptions, and lifecycle information.

## What is Dictionary

The dictionary provides a complete, machine-readable set of all AIMO taxonomy codes. It contains:

- All 91 codes across 8 dimensions
- Labels and definitions (with translations in language packs)
- Lifecycle metadata (status, version introduced, deprecated, removed)
- Scope notes and examples for code usage

The dictionary enables:

1. **Evidence Templates**: Codes are used in EV templates to classify AI systems
2. **Validator**: The validator checks that all codes exist in the dictionary
3. **Coverage Map**: Codes enable mapping to external frameworks and regulations

!!! info "Single Source of Truth (SSOT)"
    The SSOT for the dictionary is:

    - **Structure**: `data/taxonomy/canonical.yaml` (codes, status, lifecycle)
    - **Translations**: `data/taxonomy/i18n/*.yaml` (labels, definitions per language)

    CSV files are **generated artifacts** for distribution. See [Releases](../../../releases/) for downloads.

!!! note "Standard release version vs dictionary/taxonomy versions"
    The AIMO Standard **release version** (site/release, e.g. `/0.1.2/`) and the **dictionary content version** (or **taxonomy schema version**) are not necessarily the same. In 0.1.x they often align; future releases may version them independently. For audit citations, prefer the Standard release version (`/X.Y.Z/`); in Evidence, state `taxonomy_version` and `dictionary_version` where applicable.

## Column Schema

The canonical dictionary uses **18 columns** (language-neutral structure):

### Identification Columns (5)

| # | Column | Required | Description | Example |
| --- | --- | --- | --- | --- |
| 1 | `standard_id` | Yes | Standard identifier | `AIMO-STD` |
| 2 | `standard_version` | Yes | SemVer format | `0.1.0` *(example; use the Standard release version you align to)* |
| 3 | `dimension_id` | Yes | Two-letter dimension ID | `FS`, `UC`, `DT` |
| 4 | `dimension_name` | Yes | Dimension name | `Functional Scope` |
| 5 | `code` | Yes | Full code | `UC-001` |

### Label and Definition Columns (4)

| # | Column | Required | Description | Example |
| --- | --- | --- | --- | --- |
| 6 | `label` | Yes | Code label (max 50 chars) | `General Q&A` |
| 7 | `definition` | Yes | Code definition (1-2 sentences) | `General question answering...` |
| 8 | `scope_notes` | No | Usage scope clarification | `Low to medium risk...` |
| 9 | `examples` | No | Pipe-separated examples | `chatbot\|recommendation` |

!!! note "Translations"
    The canonical data model separates translations into language packs (`data/taxonomy/i18n/*.yaml`). Each language pack provides localized `dimension_name`, `label`, and `definition` values. See [Localization Guide](../../../contributing/localization/) for details.

### Lifecycle Columns (6)

| # | Column | Required | Description | Example |
| --- | --- | --- | --- | --- |
| 10 | `status` | Yes | `active`, `deprecated`, `removed` | `active` |
| 11 | `introduced_in` | Yes | Version when added | `0.1.0` |
| 12 | `deprecated_in` | No | Version when deprecated | `1.2.0` |
| 13 | `removed_in` | No | Version when removed | `2.0.0` |
| 14 | `replaced_by` | No | Replacement code | `UC-015` |
| 15 | `backward_compatible` | Yes | `true` or `false` | `true` |

### Governance Columns (3)

| # | Column | Required | Description | Example |
| --- | --- | --- | --- | --- |
| 16 | `references` | No | External references | ISO/IEC 42001 |
| 17 | `owner` | No | Responsible party | `AIMO WG` |
| 18 | `last_reviewed_date` | No | Last review (YYYY-MM-DD) | `2026-01-19` |

## Initial Entries

The current dictionary version is **v0.1.0** and contains:

| Dimension | Name | Active Codes | Deprecated | Total |
| --- | --- | --- | --- | --- |
| FS | Functional Scope | 6 | 0 | 6 |
| UC | Use Case Class | 30 | 0 | 30 |
| DT | Data Type | 10 | 0 | 10 |
| CH | Channel | 8 | 0 | 8 |
| IM | Integration Mode | 7 | 0 | 7 |
| RS | Risk Surface | 8 | 0 | 8 |
| OB | Outcome / Benefit | 7 | 0 | 7 |
| LG | Log/Event Type | 15 | 0 | 15 |
| **Total** | | **91** | **0** | **91** |

!!! note "Complete Code Listings"
    The complete list of 91 codes is available in the generated CSV artifacts. This documentation page provides column definitions and usage guidance. For detailed code definitions:

    - **Download**: See [Releases](../../../releases/) for per-language CSV files
    - **Per-language CSV**: `artifacts/taxonomy/current/{lang}/taxonomy_dictionary.csv`
    - **Legacy EN/JA mixed CSV**: `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` (frozen, for backward compatibility only)

## Update Policy

### Adding New Codes

1. Assign the next available number within the dimension (e.g., `UC-031` after `UC-030`)
2. Set `status` to `active`
3. Set `introduced_in` to the current version
4. Set `backward_compatible` to `true`
5. Provide label and definition (add translations to language packs)

### Modifying Existing Codes

| Change Type | Allowed | Version Impact |
| --- | --- | --- |
| Definition clarification | Yes | PATCH |
| Scope notes update | Yes | PATCH |
| Label change (meaning preserved) | Yes | MINOR |
| Meaning change | No | Create new code instead |

### Deprecating Codes

1. Set `status` to `deprecated`
2. Set `deprecated_in` to current version
3. Set `replaced_by` to the new code (if applicable)
4. Code remains functional for backward compatibility
5. Document the reason in scope_notes

### Removing Codes

1. Deprecate for at least one MINOR version first
2. Set `status` to `removed`
3. Set `removed_in` to current MAJOR version
4. Code is no longer valid for new evidence

### Compatibility Policy

| Action | Version Impact | Backward Compatible |
| --- | --- | --- |
| Add new code | MINOR | Yes |
| Deprecate code | MINOR | Yes |
| Clarify definition | PATCH | Yes |
| Remove code | MAJOR | No |
| Change code meaning | Not allowed | - |

## How to Use

### In Evidence Templates

Each Evidence Pack template includes an 8-dimension codes table:

```markdown
## AIMO Codes (8 Dimensions)

| Dimension | Code(s) | Label |
| --- | --- | --- |
| **FS** | `FS-001` | End-user Productivity |
| **UC** | `UC-001`, `UC-002` | General Q&A, Summarization |
| **DT** | `DT-002`, `DT-004` | Internal, Personal Data |
| **CH** | `CH-001` | Web UI |
| **IM** | `IM-002` | SaaS Integrated |
| **RS** | `RS-001`, `RS-003` | Data Leakage, Compliance Breach |
| **OB** | `OB-001` | Efficiency |
| **LG** | `LG-001`, `LG-002` | Request Record, Review/Approval Record |
```

### In Validator

The validator checks:

1. All codes referenced in evidence exist in the dictionary
2. Code format matches the expected pattern (`PREFIX-###`)
3. Deprecated codes trigger warnings
4. Removed codes are rejected

### Extension Guidelines

Organizations MAY extend the dictionary with custom codes:

**Extension Prefix:**

```
X-<ORG>-<DIM>-<TOKEN>
```

Example: `X-ACME-UC-901` for ACME Corporation's custom use case code.

**Extension Rules:**

1. Custom codes MUST NOT conflict with standard codes
2. Custom codes SHOULD be documented in a local extension dictionary
3. When exchanging evidence with external parties, use only standard codes

## Downloads

See [Releases](../../../releases/) for downloadable packages containing the dictionary and related files.

## Related Pages

- [Taxonomy](../03-taxonomy/) - Dimension definitions and code tables
- [Codes](../04-codes/) - Code format, naming, and lifecycle
- [Evidence Templates](../06-ev-template/) - How codes are used in templates
- [Validator](../07-validator/) - Code validation rules
- [Changelog](../08-changelog/) - Version history
