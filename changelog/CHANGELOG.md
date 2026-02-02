# AIMO Standard Changelog

All notable changes to the AIMO Standard will be documented in this file.

This changelog follows [Semantic Versioning](https://semver.org/) principles:
- **MAJOR**: Breaking changes to schemas, codes, or normative requirements
- **MINOR**: Backward-compatible additions (new fields with defaults, new optional codes)
- **PATCH**: Backward-compatible fixes and clarifications

---

## [0.0.1] - 2026-02-02

### Summary
Initial release of AIMO Standard with 8-dimension code system, Evidence Pack templates, and comprehensive governance documentation.

### Added

#### Code System (8 Dimensions)
- **FS** (Functional Scope): 6 codes (FS-001 to FS-006)
- **UC** (Use Case Class): 10 initial codes (UC-001 to UC-010)
- **DT** (Data Type): 8 codes (DT-001 to DT-008)
- **CH** (Channel): 6 codes (CH-001 to CH-006)
- **IM** (Integration Mode): 5 codes (IM-001 to IM-005)
- **RS** (Risk Surface): 5 codes (RS-001 to RS-005)
- **OB** (Outcome / Benefit): 5 codes (OB-001 to OB-005)
- **EV** (Evidence Type): 7 codes (EV-001 to EV-007)

#### Schemas
- `taxonomy_pack.schema.json`: Schema for taxonomy pack definition
- `changelog.schema.json`: Schema for changelog entries
- `evidence_pack_manifest.schema.json`: Schema for Evidence Pack manifests
- `shadow-ai-discovery.schema.json`: Shadow AI discovery evidence
- `agent-activity.schema.json`: Agent activity evidence

#### Evidence Pack Templates (MVP)
- EV-01: System Overview
- EV-02: Data Flow
- EV-03: AI Inventory
- EV-04: Risk & Impact Assessment
- EV-05: Controls & Approvals
- EV-06: Logging & Monitoring
- EV-07: Incident & Exception Handling

#### Documentation
- Taxonomy documentation with 8-dimension definitions
- Code System format specification (`<DIM>-<TOKEN>`)
- Dictionary CSV format specification
- Versioning and change policy
- Validator MVP requirements
- Human Oversight Protocol
- Coverage Map (ISO 42001, NIST AI RMF, EU AI Act, ISMS)
- Trust Package

### Backward Compatibility
This is the initial release; no backward compatibility concerns.

---

## Versioning Policy

### SemVer Rules
- **MAJOR** (X.0.0): Breaking changes
  - Removal of codes (must be deprecated first)
  - Schema structure changes that break existing documents
  - Changes to required fields
- **MINOR** (0.X.0): Backward-compatible additions
  - New codes added to existing dimensions
  - New optional fields in schemas
  - New dimensions (optional by default)
- **PATCH** (0.0.X): Fixes and clarifications
  - Documentation corrections
  - Validator bug fixes
  - Clarification of existing definitions

### Deprecation Policy
1. Codes or features to be removed MUST be marked `deprecated` for at least one MINOR version
2. Deprecated items MUST include `deprecated_in` version and `replaced_by` reference if applicable
3. Removal occurs in the next MAJOR version after deprecation period

---

## Distribution

This changelog is distributed as part of the AIMO Standard release package:
- `changelog/CHANGELOG.md` (this file)
- `changelog/changelog.json` (machine-readable format)

---

## References

- [AIMO Standard Specification](https://standard.aimoaas.com/)
- [Taxonomy Dictionary](../source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv)
- [Evidence Pack Templates](../source_pack/04_evidence_pack/templates/)
