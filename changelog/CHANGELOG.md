# AIMO Standard Changelog

All notable changes to the AIMO Standard will be documented in this file.

This changelog follows [Semantic Versioning](https://semver.org/) principles:
- **MAJOR**: Breaking changes to schemas, codes, or normative requirements
- **MINOR**: Backward-compatible additions (new fields with defaults, new optional codes)
- **PATCH**: Backward-compatible fixes and clarifications

---

## [0.1.1] - (release date TBD) {#version-011}

### Summary (auditor-facing)

v0.1.1 is a **PATCH** release: backward-compatible additions and clarifications. All v0.1.0 Evidence Bundles and root JSON remain valid. New: optional signature metadata for third-party verification, Coverage Map audit questions (informative), Normative/Informative and standard governance clarifications, and an informative v0.2 roadmap.

### Added

- **Evidence Bundle signing (v0.1.1 optional)**: Manifest `signing.signatures[]` may include `signer_identity`, `signed_at`, `verification_command`, and `canonicalization` (RECOMMENDED for auditor re-performance). Schema: `evidence_bundle_manifest.schema.json`. Documented in [09-evidence-bundle-structure](docs/en/standard/current/09-evidence-bundle-structure.md) and [signature-verification-roadmap](docs/en/artifacts/signature-verification-roadmap.md). Cryptographic verification remains out of scope until v0.2.
- **Coverage Map audit_questions**: `coverage_map.yaml` and Profile schema support optional `audit_questions` (example auditor questions). Methodology and meta note that audit questions are for explanatory use only, not assurance. See [methodology](docs/en/coverage-map/methodology.md) and [aimo-profile.schema.json](schemas/jsonschema/aimo-profile.schema.json).
- **Normative vs Informative**: [00_manifest.md](source_pack/00_manifest.md) now includes a table of Normative vs Informative content. Editing policy (shall/should/may) documented in `.cursor/rules/01-editing-policy.md`.
- **Standard governance**: [VERSIONING.md](VERSIONING.md) section 5: Major version upgrades SHOULD provide a migrator and migration guide; deprecated versions as read-only archives; impact analysis and compatibility statement for significant changes.
- **v0.2 roadmap (informative)**: [source_pack/07_release/v0.2_roadmap.md](source_pack/07_release/v0.2_roadmap.md) and [docs/en/standard/current/10-roadmap-v0.2.md](docs/en/standard/current/10-roadmap-v0.2.md): audit object SSOT, Evidence-as-Code, output profiles, Test library, lifecycle, JNC, OSCAL linkage. Target 2026 Q4–2027.
- **Justified Non-Compliance (JNC)**: Informative [justified-non-compliance.md](docs/en/artifacts/justified-non-compliance.md) describing a possible future extension; not normative in v0.1.1.
- **Evidence Bundle future extensions**: [09-evidence-bundle-structure](docs/en/standard/current/09-evidence-bundle-structure.md) adds a short "Future extensions" note on Control/Requirement linkage and OSCAL.
- **Validator**: When validating a bundle with `--format json`, output now includes `signing_metadata` (v0.1.1 fields from manifest) when present.
- **EU AI Act Annex IV (pulled forward)**: Official sample Evidence Bundle [examples/evidence_bundle_v01_annex_iv_sample/](examples/evidence_bundle_v01_annex_iv_sample/) for high-risk AI technical documentation (Annex IV). Profile [coverage_map/profiles/eu_ai_act_annex_iv.json](coverage_map/profiles/eu_ai_act_annex_iv.json) extended with `audit_questions` for auditor use. Documented in [Examples](docs/en/examples/index.md) and [EU AI Act mapping](docs/en/coverage-map/eu-ai-act.md). Rationale: EU applicability phase from 2026-08; see [REPORTS/v0.1.1_update_plan.md](REPORTS/v0.1.1_update_plan.md) §0.4.

### Changed

- **09-evidence-bundle-structure**: v0.1.1 optional signature fields table; Integrity note (v0.1 / v0.1.1 / v0.2); link to signature-verification-roadmap.
- **coverage_map.yaml**: `meta.methodology` and two mappings extended with `audit_questions`; version set to 0.1.1.
- **coverage_map/profiles/iso42001.json**: Optional `audit_questions` array added.
- **aimo-profile.schema.json**: Optional top-level `audit_questions` (array of strings).

---

## [0.1.0] - (release date TBD)

### Summary (auditor-facing)

v0.1 defines the **normative** Evidence Bundle structure, ID namespace (EV/LG) separation, Profiles for framework mapping, and Validator as a submission gate. This is a **breaking** release for taxonomy code usage (EV→LG). **v0.1 audit submission minimum**: root JSON with `version`, `dictionary`, `evidence`; or an Evidence Bundle directory with manifest, indexes (sha256), signing (at least one signature targeting manifest), and hash_chain. Scope MUST vs reserved: [v0.1_object_model_scope](source_pack/07_release/v0.1_object_model_scope.md). One-page structure: [09-evidence-bundle-structure](docs/en/standard/current/09-evidence-bundle-structure.md), [minimum-evidence](docs/artifacts/minimum-evidence.md).

### Breaking

- **ID namespace**: Taxonomy dimension for log/event type is **LG** only. **EV-** is reserved for Evidence artifact IDs. Validators **reject** `evidence[].codes.EV` with a normative error; use `evidence[].codes.LG` with `LG-001` … `LG-015`. See [04b-id-policy-namespace](docs/en/standard/current/04b-id-policy-namespace.md) and [MIGRATION.md](MIGRATION.md).
- **Validator rules**: Code format in `validator/rules/checks.md` / `checks.yaml` is `^(FS|UC|DT|CH|IM|RS|OB|LG)-\d{3}$` for taxonomy; EV is artifact ID only.
- **Evidence Bundle signing**: At least one entry in `signing.signatures` must have `targets` including `manifest.json` (manifest signing is mandatory). Empty `signatures` array is invalid. Schema and validator enforce this.

### Added

- **Evidence Bundle (v0.1 normative)**: Root structure and [09-evidence-bundle-structure](docs/en/standard/current/09-evidence-bundle-structure.md), `evidence_bundle_manifest.schema.json`, `validate_bundle()` in validator. Example: `examples/evidence_bundle_v01_minimal` (manifest, object_index, payload_index, hash_chain, signatures). CI runs Bundle validation in quality-gate and release.
- **ID policy**: [04b-id-policy-namespace](docs/en/standard/current/04b-id-policy-namespace.md) (10 languages). v0.1 prefix inventory: EV, LG, SC in use; RQ, CT, CL, TP, FD, RM, AP, CH, PR reserved.
- **Profiles**: `schemas/jsonschema/aimo-profile.schema.json` and `coverage_map/profiles/` (ISO 42001, NIST AI RMF, EU AI Act Annex IV). Profile JSONs are normative conversion specs; validator `--validate-profiles` enforces schema. Coverage Map YAML remains Informative.
- **Validator**: `--format json` and `--format sarif` for machine-readable and GitHub Code Scanning output. Exit codes: 0 = pass, 1 = fail. SARIF uploaded in CI for submission gate visibility.
- **Normative SSOT**: [00_manifest.md](source_pack/00_manifest.md) documents normative paths and v0.1 scope. [v0.1_object_model_scope.md](source_pack/07_release/v0.1_object_model_scope.md) defines v0.1 MUST (Evidence, dictionary, bundle structure) and reserved/future objects (D1/D5/D6 when object schemas exist).

### Changed

- **MIGRATION.md**: Section "v0.1 ID namespace: EV (Taxonomy) → LG (Log/Event Type)" with conversion table, validator rationale, and before/after JSON. v0.1 scope and audit minimum set referenced.
- **evidence-bundle-coverage-map.md** (EN/JA): Normative vs Informative (Coverage Map YAML vs Profile JSONs), v0.1 official profiles (3), update policy.
- **Docs**: Normative strengthening for audit citation (/latest vs /version), Evidence Bundle MUST checklist (EN/JA), Validator json/sarif and exit codes.

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
- **LG** (Log/Event Type): 7 codes (LG-001 to LG-007); formerly EV (Evidence Type) in pre-v0.1 (EV- is now reserved for Evidence artifact IDs only)

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
