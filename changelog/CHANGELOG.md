# AIMO Standard Changelog

All notable changes to the AIMO Standard will be documented in this file.

This changelog follows [Semantic Versioning](https://semver.org/) principles:
- **MAJOR**: Breaking changes to schemas, codes, or normative requirements
- **MINOR**: Backward-compatible additions (new fields with defaults, new optional codes)
- **PATCH**: Backward-compatible fixes and clarifications

---

## [0.1.0] - (release date TBD)

### Summary
v0.1 establishes normative Evidence Bundle structure, ID namespace (EV/LG) separation, Profiles for framework mapping, and Validator output formats. This is a **breaking** release for taxonomy code usage (EV→LG migration).

### Breaking

- **ID namespace**: Taxonomy dimension for log/event type is **LG** only. **EV-** is reserved for Evidence artifact IDs. Validators reject `evidence[].codes.EV`; use `evidence[].codes.LG` with `LG-001` … `LG-015`. See [04b-id-policy-namespace](docs/en/standard/current/04b-id-policy-namespace.md) and [MIGRATION.md](MIGRATION.md).
- **Validator rules**: Code format in `validator/rules/checks.md` / `checks.yaml` is `^(FS|UC|DT|CH|IM|RS|OB|LG)-\d{3}$` for taxonomy; EV is artifact ID only.

### Added

- **Evidence Bundle (v0.1 normative)**: Root structure and [09-evidence-bundle-structure](docs/en/standard/current/09-evidence-bundle-structure.md), `evidence_bundle_manifest.schema.json`, `validate_bundle()` in validator. Example: `examples/evidence_bundle_v01_minimal` (manifest, object_index, payload_index, hash_chain, signatures). CI runs Bundle validation in quality-gate and release.
- **ID policy**: [04b-id-policy-namespace](docs/en/standard/current/04b-id-policy-namespace.md) (10 languages). v0.1 prefix inventory: EV, LG, SC in use; RQ, CT, CL, TP, FD, RM, AP, CH, PR reserved.
- **Profiles**: `schemas/jsonschema/aimo-profile.schema.json` and `coverage_map/profiles/` (ISO 42001, NIST AI RMF, EU AI Act Annex IV). Coverage Map YAML remains Informative; Profile JSONs are normative conversion specs.
- **Validator**: `--format json` and `--format sarif` for machine-readable and Code Scanning output. Exit codes: 0 = pass, 1 = fail.
- **Normative SSOT**: [00_manifest.md](source_pack/00_manifest.md) documents normative paths (09, 04b, schemas, validator rules). [v0.1_object_model_scope.md](source_pack/07_release/v0.1_object_model_scope.md) defines v0.1 MUST (Evidence, dictionary) and optional/future objects.

### Changed

- **MIGRATION.md**: New section "v0.1 ID namespace: EV (Taxonomy) → LG (Log/Event Type)" for migration from EV-* to LG-* taxonomy codes.
- **evidence-bundle-coverage-map.md** (EN/JA): Relationship between Coverage Map (Informative) and Profile JSONs (normative) documented.

---

## [0.0.3] - 2026-02-02

### Summary
Complete translations for all 8 new languages (312 files translated).

### Changed
- Translated all 39 documentation files to Spanish, French, German, Portuguese, Italian, Simplified Chinese, Traditional Chinese, and Korean
- Total: 312 files translated (39 files × 8 languages)

---

## [0.0.2] - 2026-02-02

### Summary
Add multilingual support for 10 languages with translation freshness tracking system.

### Added

#### Multilingual Support (10 Languages)
- **English** (en): Canonical source
- **Japanese** (ja): Existing translation
- **Spanish** (es): New language
- **French** (fr): New language
- **German** (de): New language
- **Portuguese** (pt): New language
- **Italian** (it): New language
- **Simplified Chinese** (zh): New language
- **Traditional Chinese** (zh-TW): New language
- **Korean** (ko): New language

#### Translation Tooling
- `sync_translations.py`: Translation freshness tracking tool
- `TRANSLATION_SYNC_SPEC.md`: Technical specification for translation workflow
- Translation metadata in frontmatter for tracking source changes
- Taxonomy i18n packs for all 10 languages

#### Documentation
- Updated localization guide with translation sync workflow
- Extended `lint_i18n.py` to support all 10 languages

### Changed
- `mkdocs.yml`: Added 8 new language configurations
- Language selector now shows all 10 languages

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
