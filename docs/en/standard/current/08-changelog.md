---
description: AIMO Standard changelog and versioning policy. Documents version history, semantic versioning rules, and migration guidance between releases.
---

# Changelog

This section documents the versioning policy and change history for the AIMO Standard.

## Versioning Policy

AIMO Standard follows [Semantic Versioning](https://semver.org/) (SemVer):

### Version Format: MAJOR.MINOR.PATCH

| Change Type | Version Bump | Examples |
| --- | --- | --- |
| **MAJOR** | X.0.0 | Breaking schema changes, code removal, required field changes |
| **MINOR** | 0.X.0 | New codes, new optional fields, new dimensions (optional) |
| **PATCH** | 0.0.X | Documentation fixes, definition clarifications, validator bug fixes |

### Breaking vs. Compatible Changes

**Breaking Changes (MAJOR):**

- Removal of codes (after deprecation period)
- Changes to required fields in schemas
- Structural changes that invalidate existing documents
- Changes to code format patterns

**Backward Compatible Changes (MINOR):**

- Adding new codes to existing dimensions
- Adding new optional fields to schemas
- Adding new optional dimensions
- Adding new evidence templates

**Non-breaking Changes (PATCH):**

- Documentation corrections
- Clarification of existing definitions
- Translation improvements
- Validator bug fixes

## Deprecation Policy

### Deprecation Process

1. **Mark as Deprecated**: Code or feature is marked with `status: deprecated` and `deprecated_in: X.Y.Z`
2. **Deprecation Period**: At least one MINOR version must pass before removal
3. **Provide Replacement**: If applicable, `replaced_by` indicates the replacement
4. **Remove in MAJOR**: Removal occurs in the next MAJOR version

### Example Lifecycle

```
v0.0.1: FS-007 introduced (status: active)
v0.1.0: FS-007 deprecated (status: deprecated, replaced_by: FS-008)
v0.2.0: FS-007 still available with deprecation warning
v1.0.0: FS-007 removed (status: removed)
```

### Using Deprecated Codes

- Deprecated codes remain valid for validation
- Validator SHOULD emit a warning for deprecated codes
- New implementations SHOULD use replacement codes
- Existing documents MAY continue using deprecated codes until migration

## Release Artifacts

Each official release includes:

| Artifact | Description |
| --- | --- |
| Versioned site snapshot | `https://standard.aimoaas.com/0.0.1/` |
| PDF specification | `trust_package.pdf` |
| Asset package (ZIP) | Schemas, templates, dictionary |
| Checksums | SHA-256 hashes for integrity |
| Changelog | This document |

## Change History

### Unreleased (namespace and normative fixes)

**Summary:** Resolves EV code collision, clarifies EV (index) vs Evidence Pack (payload), and hardens /dev against audit miscitation.

#### Changed

- **Evidence Pack document types (EP namespace):** Evidence Pack file types use **EP-01..EP-07** (document type). Taxonomy **EV-001, EV-002, …** remain event/evidence types (Request Record, Review/Approval, etc.). See [Evidence Pack Template](./06-ev-template.md). Schema: `evidence_files[].file_id` pattern is `^EP-\\d{2}$`; `ev_type` is optional.
- **Normative relationship:** [Evidence Bundle](../../artifacts/evidence-bundle.md) now states normatively: EV records (JSON) are the index/ledger; Evidence Pack files are the payload; EV records SHOULD reference payload by evidence_file_ids (e.g. EP-01) and/or hashes; minimum submission set = EV JSON + Dictionary + Summary + Change Log + Evidence Pack.
- **/dev anti-miscitation:** Development preview pages show a red banner: "Development Preview — Not for audit citation. Use /latest/ or a versioned URL." Canonical for /dev/ pages points to /latest/; noindex remains in place.

### Version 0.0.1 (2026-02-02)

**Summary:** Initial release of AIMO Standard with 8-dimension code system, Evidence Pack templates, and comprehensive governance documentation.

#### Added

**Code System (8 Dimensions)**

| Dimension | Codes Added | Description |
| --- | --- | --- |
| FS | FS-001 to FS-006 | Functional Scope |
| UC | UC-001 to UC-010 | Use Case Class |
| DT | DT-001 to DT-008 | Data Type |
| CH | CH-001 to CH-006 | Channel |
| IM | IM-001 to IM-005 | Integration Mode |
| RS | RS-001 to RS-005 | Risk Surface |
| OB | OB-001 to OB-005 | Outcome / Benefit |
| EV | EV-001 to EV-007 | Evidence Type |

**Schemas**

- `taxonomy_pack.schema.json`: Taxonomy pack definition
- `changelog.schema.json`: Changelog entries
- `evidence_pack_manifest.schema.json`: Evidence Pack manifests
- `shadow-ai-discovery.schema.json`: Shadow AI discovery evidence
- `agent-activity.schema.json`: Agent activity evidence

**Evidence Pack Templates (MVP)**

- EV-01: System Overview
- EV-02: Data Flow
- EV-03: AI Inventory
- EV-04: Risk & Impact Assessment
- EV-05: Controls & Approvals
- EV-06: Logging & Monitoring
- EV-07: Incident & Exception Handling

**Documentation**

- Taxonomy documentation with 8-dimension definitions
- Code System format specification
- Dictionary CSV format specification
- Versioning and change policy
- Validator MVP requirements
- Human Oversight Protocol
- Coverage Map (ISO 42001, NIST AI RMF, EU AI Act, ISMS)
- Trust Package

#### Backward Compatibility

This is the initial release; no backward compatibility concerns.

---

## Machine-Readable Changelog

A machine-readable changelog is available:

- `changelog/changelog.json`

This file follows the `changelog.schema.json` schema and can be parsed programmatically.

## References

- [Taxonomy](./03-taxonomy.md) - Dimension definitions
- [Dictionary](./05-dictionary.md) - Code dictionary
- [Versioning Policy](../../governance/index.md) - Versioning policy (see VERSIONING.md in repository root)
