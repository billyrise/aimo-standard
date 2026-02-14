---
description: AIMO Code System format and naming conventions. Defines code structure (XX-NNN), lifecycle states, versioning, and deprecation policies for taxonomy codes.
---

# Codes

This page defines the AIMO Code System format, naming conventions, and lifecycle management.

## Code Format

All AIMO codes follow the format: **`<PREFIX>-<TOKEN>`**

| Component | Description | Format | Example |
| --- | --- | --- | --- |
| `<PREFIX>` | Dimension identifier | 2 uppercase letters | FS, UC, DT |
| `-` | Separator | Hyphen | - |
| `<TOKEN>` | Unique token within dimension | 3 digits (zero-padded) | 001, 002, 003 |

### Examples

- `FS-001` - Functional Scope: End-user Productivity
- `UC-005` - Use Case Class: Code Generation
- `DT-004` - Data Type: Personal Data
- `CH-003` - Channel: IDE Plugin
- `IM-002` - Integration Mode: SaaS Integrated
- `RS-001` - Risk Surface: Data Leakage
- `OB-001` - Outcome/Benefit: Efficiency
- `LG-001` - Log/Event Type: Request Record

## Namespaces

The AIMO taxonomy uses 8 dimension namespaces:

| ID | Name | Prefix | Code Count |
| --- | --- | --- | --- |
| **FS** | Functional Scope | `FS-` | 6 |
| **UC** | Use Case Class | `UC-` | 30 |
| **DT** | Data Type | `DT-` | 10 |
| **CH** | Channel | `CH-` | 8 |
| **IM** | Integration Mode | `IM-` | 7 |
| **RS** | Risk Surface | `RS-` | 8 |
| **OB** | Outcome / Benefit | `OB-` | 7 |
| **LG** | Log/Event Type | `LG-` | 15 |

**Total: 91 codes across 8 dimensions**

### Namespace Rules

1. **Prefix is fixed**: The two-letter dimension prefix (FS, UC, etc.) is permanent and will never change.
2. **Zero-padding**: Tokens are always 3 digits, zero-padded (e.g., `001` not `1`).
3. **Sequential assignment**: New codes are assigned the next available number within a dimension.
4. **No reuse**: Removed codes are never reassigned to different meanings.

## Stability Rules

Code stability is a critical principle for audit traceability.

### ID Immutability

- **Code IDs are immutable** — once assigned, a code ID never changes meaning
- A code like `UC-001` will always mean "General Q&A" for its entire lifecycle
- If the meaning needs to change, a new code is created instead

### No Reuse Policy

- Deprecated or removed codes are **never reassigned** to different meanings
- This ensures historical evidence remains valid and traceable
- Example: If `UC-010` is deprecated, a new use case gets `UC-031` (not `UC-010`)

### Deprecation Before Removal

- Codes must be marked `deprecated` for at least one MINOR version before removal
- Removal only occurs in MAJOR version increments
- See [Lifecycle](#lifecycle) section for details

## Usage

### Required Dimensions

For each AI system or use case, you MUST specify at least one code from each required dimension:

| Dimension | Selection | Notes |
| --- | --- | --- |
| FS | Exactly 1 | Primary business function |
| UC | 1 or more | Task types performed |
| DT | 1 or more | Data classifications |
| CH | 1 or more | Access channels |
| IM | Exactly 1 | Integration mode |
| RS | 1 or more | Risk categories |
| LG | 1 or more | Log/event types |

### Optional Dimensions

| Dimension | Selection | Notes |
| --- | --- | --- |
| OB | 0 or more | Expected benefits (optional) |

### Code Composition

When documenting an AI system, codes from multiple dimensions are combined. The **composition priority** determines the order when listing codes:

1. FS (Functional Scope)
2. UC (Use Case Class)
3. DT (Data Type)
4. CH (Channel)
5. IM (Integration Mode)
6. RS (Risk Surface)
7. OB (Outcome / Benefit)
8. LG (Log/Event Type)

See [ID Policy / Namespace](../04b-id-policy-namespace/): **EV-** is reserved for Evidence *artifact* IDs only; taxonomy log/event dimension uses **LG-** (e.g. LG-001 … LG-015).

**Example composition:**

```
FS: FS-001
UC: UC-001, UC-002
DT: DT-002, DT-004
CH: CH-001
IM: IM-002
RS: RS-001, RS-003
OB: OB-001
LG: LG-001, LG-002
```

## Lifecycle

### Status Values

| Status | Description | Validator Behavior |
| --- | --- | --- |
| `active` | Currently valid and in use | Accepted |
| `deprecated` | Still valid but scheduled for removal | Accepted with warning |
| `removed` | No longer valid; do not use | Rejected |

### Lifecycle Metadata Fields

The dictionary tracks lifecycle with these fields:

| Field | Required | Description | Example |
| --- | --- | --- | --- |
| `status` | Yes | Current status | `active` |
| `introduced_in` | Yes | Version when code was added | `0.1.0` |
| `deprecated_in` | No | Version when marked deprecated | `1.2.0` |
| `removed_in` | No | Version when removed | `2.0.0` |
| `replaced_by` | No | Replacement code(s) | `UC-015` |
| `backward_compatible` | Yes | Whether change breaks existing usage | `true` |

### Deprecation Rules

1. Codes MUST be marked `deprecated` for at least one MINOR version before removal
2. Deprecated codes include `deprecated_in` version and `replaced_by` if applicable
3. Removal occurs only in MAJOR version increments
4. Deprecated codes remain valid for backward compatibility during the deprecation period

**Example timeline:**

| Version | Status | Action |
| --- | --- | --- |
| 0.1.0 | `active` | Code `UC-010` introduced |
| 1.2.0 | `deprecated` | Marked deprecated, `replaced_by: UC-031` |
| 2.0.0 | `removed` | No longer accepted by validator |

### Versioning

Code changes follow [Semantic Versioning](../08-changelog/):

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
4. Code format matches `<PREFIX>-<TOKEN>` pattern (e.g., `UC-001`)
5. Deprecated codes are flagged with warnings

See [Validator](../07-validator/) for implementation details.

## SSOT Reference

!!! info "Source of Truth"
    The authoritative definitions are `data/taxonomy/canonical.yaml` and `data/taxonomy/i18n/*.yaml`. The file `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` is **generated** from the SSOT. This page is explanatory. See [Localization Guide](../../../contributing/localization/) for update workflows.

## Related Pages

- [Taxonomy](../03-taxonomy/) - Full dimension definitions
- [Dictionary](../05-dictionary/) - Complete code listings and column definitions
- [Validator](../07-validator/) - Validation rules
- [Changelog](../08-changelog/) - Version history
