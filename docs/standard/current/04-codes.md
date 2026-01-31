# Codes

This section defines the AIMO Code System format, naming conventions, and lifecycle management.

## Code Format

All AIMO codes follow the format: **`<DIM>-<TOKEN>`**

| Component | Description | Format | Example |
| --- | --- | --- | --- |
| `<DIM>` | Dimension identifier | 2 uppercase letters | FS, UC, DT |
| `-` | Separator | Hyphen | - |
| `<TOKEN>` | Unique token within dimension | 3 digits (zero-padded) | 001, 002, 003 |

### Naming Conventions

1. **Prefix stability**: The two-letter dimension prefix (FS, UC, etc.) is fixed and will not change.
2. **Zero-padding**: Tokens are always 3 digits, zero-padded (e.g., `001` not `1`).
3. **Sequential assignment**: New codes are assigned the next available number within a dimension.
4. **No reuse**: Removed codes are never reassigned to different meanings.

**Examples:**

- `FS-001` - Functional Scope: End-user Productivity
- `UC-005` - Use Case Class: Code Generation
- `DT-004` - Data Type: Personal Data
- `CH-003` - Channel: IDE Plugin
- `IM-002` - Integration Mode: SaaS Integrated
- `RS-001` - Risk Surface: Data Leakage
- `OB-001` - Outcome/Benefit: Efficiency
- `EV-001` - Evidence Type: System Overview

## Dimension Identifiers

| ID | Dimension Name | Token Type | Required | Multi-select |
| --- | --- | --- | --- | --- |
| **FS** | Functional Scope | Numeric (001-999) | Yes | No |
| **UC** | Use Case Class | Numeric (001-999) | Yes | Yes |
| **DT** | Data Type | Numeric (001-999) | Yes | Yes |
| **CH** | Channel | Numeric (001-999) | Yes | Yes |
| **IM** | Integration Mode | Numeric (001-999) | Yes | No |
| **RS** | Risk Surface | Numeric (001-999) | Yes | Yes |
| **OB** | Outcome / Benefit | Numeric (001-999) | No | Yes |
| **EV** | Evidence Type | Numeric (001-999) | Yes | Yes |

## Code Composition

When documenting an AI system, codes from multiple dimensions are combined. The **composition priority** determines the order when listing codes:

1. FS (Functional Scope)
2. UC (Use Case Class)
3. DT (Data Type)
4. CH (Channel)
5. IM (Integration Mode)
6. RS (Risk Surface)
7. OB (Outcome / Benefit)
8. EV (Evidence Type)

**Example composition:**

```
FS: FS-001
UC: UC-001, UC-002
DT: DT-002, DT-004
CH: CH-001
IM: IM-002
RS: RS-001, RS-003
OB: OB-001
EV: EV-001, EV-002, EV-003, EV-004, EV-005, EV-006, EV-007
```

## Usage Guidelines

### Required Dimensions

For each AI system or use case, you MUST specify at least one code from each required dimension:

- FS (exactly one)
- UC (one or more)
- DT (one or more)
- CH (one or more)
- IM (exactly one)
- RS (one or more)
- EV (one or more)

### Optional Dimensions

- OB (zero or more)

### Multi-select Dimensions

When `multi_select: true`, multiple codes from the same dimension can be selected. For example, an AI system might process both `DT-002` (Internal) and `DT-004` (Personal Data).

### Single-select Dimensions

When `multi_select: false`, exactly one code must be selected from the dimension. For example, each AI system has one primary `FS` (Functional Scope) and one `IM` (Integration Mode).

## Code Lifecycle

### Status Values

| Status | Description | Validator Behavior |
| --- | --- | --- |
| `active` | Currently valid and in use | Accepted |
| `deprecated` | Still valid but scheduled for removal | Accepted with warning |
| `removed` | No longer valid; do not use | Rejected |

### Lifecycle Metadata Fields

The dictionary tracks lifecycle with these fields:

| Field | Description | Example |
| --- | --- | --- |
| `introduced_in` | Version when code was added | `0.1.0` |
| `deprecated_in` | Version when marked deprecated | `1.2.0` |
| `removed_in` | Version when removed | `2.0.0` |
| `replaced_by` | Replacement code(s) | `UC-015` |

### Deprecation Rules

1. Codes MUST be marked `deprecated` for at least one MINOR version before removal
2. Deprecated codes include `deprecated_in` version and `replaced_by` if applicable
3. Removal occurs only in MAJOR version increments
4. Deprecated codes remain valid for backward compatibility during the deprecation period

**Example timeline:**

| Version | Status | Action |
| --- | --- | --- |
| 0.1.0 | `active` | Code `UC-010` introduced |
| 1.2.0 | `deprecated` | Marked deprecated, `replaced_by: UC-015` |
| 2.0.0 | `removed` | No longer accepted by validator |

### Versioning

Code changes follow [Semantic Versioning](./08-changelog.md):

- **MAJOR**: Code removal or breaking changes
- **MINOR**: New codes added, codes deprecated
- **PATCH**: Definition clarifications only (no structural changes)

### Backward Compatibility

The `backward_compatible` field indicates whether a change breaks existing usage:

| Value | Meaning |
| --- | --- |
| `true` | Existing evidence using this code remains valid |
| `false` | Existing evidence may need updates (MAJOR version change) |

## Validation

The validator checks:

1. All required dimensions have at least one code
2. Single-select dimensions have exactly one code
3. All codes exist in the current taxonomy dictionary
4. Code format matches `<DIM>-<TOKEN>` pattern
5. Deprecated codes are flagged with warnings

See [Validator](./07-validator.md) for implementation details.

## Machine-Readable References

Access the complete code definitions in machine-readable formats:

| Resource | Format | Path |
| --- | --- | --- |
| Dictionary | CSV | `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv` |
| Taxonomy (EN) | YAML | `source_pack/03_taxonomy/taxonomy_en.yaml` |
| Taxonomy (JA) | YAML | `source_pack/03_taxonomy/taxonomy_ja.yaml` |
| Code System | CSV | `source_pack/03_taxonomy/code_system.csv` |

## References

- [Taxonomy](./03-taxonomy.md) - Full dimension definitions
- [Dictionary](./05-dictionary.md) - Complete code listings
- [Validator](./07-validator.md) - Validation rules
- [Changelog](./08-changelog.md) - Version history
