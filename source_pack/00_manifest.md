# AIMO Standard Content Manifest

**Status**: Single Source of Truth (SSOT) for documentation coverage  
**Last updated**: CU-TAX-01 (2026-01-31)

This manifest is the canonical checklist for auditor-first documentation. All CU (Change Unit) changes that affect documentation scope must update this file.

---

## How to use this manifest

1. **Before implementing a CU**: Check this manifest to understand current coverage state.
2. **After implementing a CU**: Update the relevant checklist items with implementation status and target pages.
3. **For audits**: Use this manifest to verify that all required content exists and is discoverable.
4. **EN is canonical**: This manifest is maintained in English only. Japanese documentation mirrors the same structure via `*.ja.md` files.

**Rule**: This manifest is SSOT for content coverage; CU changes must update this file.

---

## Normative SSOT (v0.1)

The following paths are **normative** for AIMO Standard v0.1. The repository does not use a separate `/normative/` directory; normative content lives in the paths below.

| Normative subject | Location (SSOT) |
|-------------------|-----------------|
| **Evidence Bundle structure** | `docs/*/standard/current/09-evidence-bundle-structure.md` — root layout, manifest, integrity (v0.1) |
| **ID policy / namespace** | `docs/*/standard/current/04b-id-policy-namespace.md` — EV (artifact ID) vs LG (taxonomy) separation |
| **JSON Schemas** | `schemas/jsonschema/` — aimo-standard, aimo-dictionary, aimo-ev, evidence_bundle_manifest, evidence_pack_manifest, etc. |
| **Validator rules** | `validator/rules/checks.md`, `validator/rules/checks.yaml` — code format (LG, not EV in taxonomy), schema validation |

---

## 1. Auditors

### 1.1 Trust Package Hub
| Item | Target Page | Status | Notes |
|------|-------------|--------|-------|
| Trust Package overview | `docs/governance/trust-package.md` | ✅ Complete | Hub for audit-ready materials |
| Download links (PDF, zip, checksums) | `docs/governance/trust-package.md` | ✅ Complete | Links to GitHub Releases |
| What you get (contents list) | `docs/governance/trust-package.md` | ✅ Complete | Links to all sub-sections |
| Minimum set for audit-readiness table | `docs/governance/trust-package.md` | ✅ Complete | Quick reference table |
| Audit journey links | `docs/governance/trust-package.md` | ✅ Complete | CU-06 addition |

### 1.2 Evidence Bundle
| Item | Target Page | Status | Notes |
|------|-------------|--------|-------|
| Bundle structure and naming | `docs/artifacts/evidence-bundle.md` | ✅ Complete | |
| Table of contents (TOC) | `docs/artifacts/evidence-bundle.md` | ✅ Complete | Required/optional artifacts |
| Traceability rules | `docs/artifacts/evidence-bundle.md` | ✅ Complete | Stable IDs, cross-references |
| How auditors use this | `docs/artifacts/evidence-bundle.md` | ✅ Complete | |
| Operational guidance box | `docs/artifacts/evidence-bundle.md` | ✅ Complete | CU-06 addition |
| Audit journey links | `docs/artifacts/evidence-bundle.md` | ✅ Complete | CU-06 addition |

### 1.3 Minimum Evidence Requirements
| Item | Target Page | Status | Notes |
|------|-------------|--------|-------|
| Request lifecycle | `docs/artifacts/minimum-evidence.md` | ✅ Complete | MUST fields and linkages |
| Review/Approval lifecycle | `docs/artifacts/minimum-evidence.md` | ✅ Complete | |
| Exception lifecycle | `docs/artifacts/minimum-evidence.md` | ✅ Complete | |
| Renewal lifecycle | `docs/artifacts/minimum-evidence.md` | ✅ Complete | |
| Change Log lifecycle | `docs/artifacts/minimum-evidence.md` | ✅ Complete | |
| Integrity & Access section | `docs/artifacts/minimum-evidence.md` | ✅ Complete | CU-06 expanded |

### 1.4 Coverage Map
| Item | Target Page | Status | Notes |
|------|-------------|--------|-------|
| Methodology (what mapping is/is not) | `docs/coverage-map/methodology.md` | ✅ Complete | |
| How to use in audit | `docs/coverage-map/methodology.md` | ✅ Complete | |
| ISO 42001 mapping | `docs/coverage-map/iso-42001.md` | ✅ Complete | |
| NIST AI RMF mapping | `docs/coverage-map/nist-ai-rmf.md` | ✅ Complete | |
| EU AI Act mapping | `docs/coverage-map/eu-ai-act.md` | ✅ Complete | |
| ISMS mapping | `docs/coverage-map/isms.md` | ✅ Complete | |
| Non-overclaim statement | `docs/coverage-map/methodology.md` | ✅ Complete | CU-06 addition |
| Audit journey links | `docs/coverage-map/methodology.md` | ✅ Complete | CU-06 addition |

### 1.5 Validator
| Item | Target Page | Status | Notes |
|------|-------------|--------|-------|
| Validator hub | `docs/validator/index.md` | ✅ Complete | |
| Validator spec | `docs/standard/current/07-validator.md` | ✅ Complete | |

### 1.6 Examples
| Item | Target Page | Status | Notes |
|------|-------------|--------|-------|
| Minimal sample bundle | `examples/minimal/` | ✅ Complete | |
| Evidence bundle minimal | `examples/evidence_bundle_minimal/` | ✅ Complete | |

### 1.7 Taxonomy & Dictionary (SSOT)
| Item | Target Page | Status | Notes |
|------|-------------|--------|-------|
| Taxonomy overview (8 dimensions) | `docs/standard/current/03-taxonomy.md` | ✅ Complete | CU-TX-03: audit context, SSOT refs |
| Code format and lifecycle | `docs/standard/current/04-codes.md` | ✅ Complete | CU-TX-03: naming, deprecation |
| Dictionary (21 columns) | `docs/standard/current/05-dictionary.md` | ✅ Complete | CU-TX-03: 91 codes, usage |
| Dictionary SSOT (CSV) | `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv` | ✅ Complete | CU-TX-01: 91 codes, 8 dimensions |
| Taxonomy YAML (EN/JA) | `source_pack/03_taxonomy/taxonomy_en.yaml` | ✅ Complete | CU-TX-02: generated from CSV |
| Code System CSV | `source_pack/03_taxonomy/code_system.csv` | ✅ Complete | CU-TX-02: dimension namespaces |
| Dimensions mapping | `source_pack/03_taxonomy/dimensions_en_ja.md` | ✅ Complete | CU-TX-02: EN/JA table |

---

## 2. Security

### 2.1 Responsibility Boundary
| Item | Target Page | Status | Notes |
|------|-------------|--------|-------|
| What AIMO provides | `docs/governance/responsibility-boundary.md` | ✅ Complete | CU-06 new page |
| What AIMO does NOT provide | `docs/governance/responsibility-boundary.md` | ✅ Complete | CU-06 new page |
| Assumptions | `docs/governance/responsibility-boundary.md` | ✅ Complete | CU-06 new page |
| Adopter responsibilities | `docs/governance/responsibility-boundary.md` | ✅ Complete | CU-06 new page |

### 2.2 Evidence Integrity & Access
| Item | Target Page | Status | Notes |
|------|-------------|--------|-------|
| Access control guidance | `docs/artifacts/minimum-evidence.md` | ✅ Complete | CU-06 expanded |
| Retention guidance | `docs/artifacts/minimum-evidence.md` | ✅ Complete | CU-06 expanded |
| Immutability options | `docs/artifacts/minimum-evidence.md` | ✅ Complete | CU-06 expanded |
| Audit trail expectations | `docs/artifacts/minimum-evidence.md` | ✅ Complete | CU-06 expanded |

### 2.3 Security Disclosure
| Item | Target Page | Status | Notes |
|------|-------------|--------|-------|
| SECURITY.md link | `docs/governance/index.md` | ✅ Complete | Links to repo root |

---

## 3. IT Ops

### 3.1 Releases
| Item | Target Page | Status | Notes |
|------|-------------|--------|-------|
| Download latest release | `docs/releases/index.md` | ✅ Complete | |
| Release assets table | `docs/releases/index.md` | ✅ Complete | |
| Verifying downloads (checksums) | `docs/releases/index.md` | ✅ Complete | |
| Artifacts zip contents | `docs/releases/index.md` | ✅ Complete | |
| Changelog link | `docs/releases/index.md` | ✅ Complete | |

### 3.2 Submission Package
| Item | Target Page | Status | Notes |
|------|-------------|--------|-------|
| Step-by-step preparation | `docs/governance/trust-package.md` | ✅ Complete | CU-06 addition |
| Submission steps summary | `docs/releases/index.md` | ✅ Complete | CU-06 addition |

### 3.3 Validator Usage
| Item | Target Page | Status | Notes |
|------|-------------|--------|-------|
| How to run validator | `docs/validator/index.md` | ✅ Complete | |
| Validator rules | `validator/rules/` | ✅ Complete | |

---

## 4. Legal / Procurement

### 4.1 Non-overclaim Statement
| Item | Target Page | Status | Notes |
|------|-------------|--------|-------|
| Canonical statement (SSOT) | `docs/governance/responsibility-boundary.md` | ✅ Complete | CU-06 new |
| Reference in Trust Package | `docs/governance/trust-package.md` | ✅ Complete | CU-06 addition |
| Reference in Methodology | `docs/coverage-map/methodology.md` | ✅ Complete | CU-06 addition |
| Reference in Releases | `docs/releases/index.md` | ✅ Complete | CU-06 addition |
| Reference in Minimum Evidence | `docs/artifacts/minimum-evidence.md` | ✅ Complete | Existing |

### 4.2 Licensing & Trademarks
| Item | Target Page | Status | Notes |
|------|-------------|--------|-------|
| LICENSE.txt link | `docs/governance/index.md` | ✅ Complete | |
| NOTICE.txt link | `docs/governance/index.md` | ✅ Complete | |
| TRADEMARKS.md link | `docs/governance/index.md` | ✅ Complete | |

### 4.3 Governance
| Item | Target Page | Status | Notes |
|------|-------------|--------|-------|
| GOVERNANCE.md link | `docs/governance/index.md` | ✅ Complete | |
| VERSIONING.md link | `docs/governance/index.md` | ✅ Complete | |

---

## 5. Navigation & Discovery (2-Click Rule)

### 5.1 Home Page Quick Links
| Audience | Target | Status | Notes |
|----------|--------|--------|-------|
| For auditors | `docs/index.md` | ✅ Complete | Links to Trust Package, Evidence Bundle, etc. |
| For security | `docs/index.md` | ✅ Complete | Links to Trust Package, Responsibility Boundary, etc. |
| For IT ops | `docs/index.md` | ✅ Complete | Links to Releases, Validator, etc. |
| For legal/procurement | `docs/index.md` | ✅ Complete | CU-06 addition |

### 5.2 Audit Journey
| Step | From Page | To Page | Status |
|------|-----------|---------|--------|
| 1 | Home | Trust Package | ✅ Complete |
| 2 | Trust Package | Evidence Bundle | ✅ Complete |
| 3 | Evidence Bundle | Minimum Evidence | ✅ Complete |
| 4 | Minimum Evidence | Coverage Map | ✅ Complete |
| 5 | Coverage Map Methodology | Framework tables | ✅ Complete |
| 6 | Framework tables | Validator | ✅ Complete |
| 7 | Validator | Releases | ✅ Complete |

---

## 6. Schemas, Templates, Examples

| Item | Location | Status | Notes |
|------|----------|--------|-------|
| aimo-ev.schema.json | `schemas/jsonschema/` | ✅ Complete | |
| aimo-dictionary.schema.json | `schemas/jsonschema/` | ✅ Complete | |
| aimo-standard.schema.json | `schemas/jsonschema/` | ✅ Complete | |
| EV template (JSON) | `templates/ev/ev_template.json` | ✅ Complete | |
| EV template (MD) | `templates/ev/ev_template.md` | ✅ Complete | |
| Minimal sample | `examples/minimal/` | ✅ Complete | |
| Evidence bundle minimal | `examples/evidence_bundle_minimal/` | ✅ Complete | |

---

---

## 7. Taxonomy SSOT

### 7.0 Taxonomy Dictionary as SSOT

**The single source of truth (SSOT) for the AIMO Code System is:**

```
source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv
```

This CSV file defines all dimension codes, labels, definitions, and lifecycle metadata. All other representations (docs, schemas, templates, examples) are **derived** from this CSV.

**Update workflow:**
1. Edit `taxonomy_dictionary_v0.1.csv` first
2. Run `python tooling/checks/lint_taxonomy_dictionary.py` to validate
3. Update derived files as listed below

### 7.0.1 Taxonomy SSOT Reflection Targets

Changes to `taxonomy_dictionary_v0.1.csv` must be reflected in:

| Target | Type | Notes |
| --- | --- | --- |
| `docs/standard/current/03-taxonomy.md` | Docs | Dimension definitions, code tables |
| `docs/standard/current/03-taxonomy.ja.md` | Docs | Japanese version |
| `docs/standard/current/04-codes.md` | Docs | Code format, usage |
| `docs/standard/current/04-codes.ja.md` | Docs | Japanese version |
| `docs/standard/current/05-dictionary.md` | Docs | CSV column definitions, counts |
| `docs/standard/current/05-dictionary.ja.md` | Docs | Japanese version |
| `source_pack/03_taxonomy/schemas/taxonomy_pack.schema.json` | Schema | Dimension enum if changed |
| `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json` | Schema | Code patterns if changed |
| `source_pack/04_evidence_pack/templates/EV-*.md` | Templates | AIMO codes table |
| `source_pack/04_evidence_pack/examples/evidence_pack_manifest.example.json` | Example | Code values |

### 7.0.2 Canonical SSOT vs. Compatibility Alias

| File | Status | Description |
| --- | --- | --- |
| `taxonomy_dictionary_v0.1.csv` | **Canonical SSOT** | The single source of truth (versioned, validated by CI). All edits go here first. |
| `dictionary_seed.csv` | Compatibility Alias | Kept for backward compatibility with legacy tools/scripts. MUST be identical to SSOT. Do not edit directly. |

**Rule**: When updating codes, edit `taxonomy_dictionary_v0.1.csv` only. Then sync to `dictionary_seed.csv` via copy:

```bash
cp source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv source_pack/03_taxonomy/dictionary_seed.csv
```

**Deprecation Plan**: `dictionary_seed.csv` will be deprecated in a future major version. New integrations should reference the canonical file directly.

### 7.0.3 Taxonomy Derived Assets (CU-TX-02)

The following files are **generated from the SSOT CSV** and MUST NOT be edited manually:

| File | Description | Generated By |
| --- | --- | --- |
| `taxonomy_en.yaml` | English taxonomy (dimensions + codes) | `build_taxonomy_assets.py` |
| `taxonomy_ja.yaml` | Japanese taxonomy (dimensions + codes) | `build_taxonomy_assets.py` |
| `code_system.csv` | Dimension namespaces and prefixes | `build_taxonomy_assets.py` |
| `dimensions_en_ja.md` | Dimension mapping table (EN/JA) | `build_taxonomy_assets.py` |

**Regeneration Command:**

```bash
python tooling/taxonomy/build_taxonomy_assets.py
```

**CI Check (validates derived files match SSOT):**

```bash
python tooling/taxonomy/build_taxonomy_assets.py --check
```

**Update Workflow:**
1. Edit `taxonomy_dictionary_v0.1.csv` (the SSOT)
2. Run `python tooling/checks/lint_taxonomy_dictionary.py` to validate
3. Run `python tooling/taxonomy/build_taxonomy_assets.py` to regenerate derived files
4. Commit both the CSV and regenerated files together

---

## 8. CU-07 Source Pack Authoring SSOT

### 8.1 Source Pack Overview

The Source Pack (`source_pack/`) is the authoring SSOT for AIMO Standard documentation. It provides reproducible inputs for generating docs, schemas, and templates without relying on chat context.

**Principles**:
- English is canonical; Japanese is derivative
- Do not invent content; use TBD placeholders when authoritative source is unavailable
- Source Pack is authoring input, not user-facing documentation
- Never contradict published docs; record gaps in Gap Log instead

### 8.2 Docs Page to Source Pack Mapping

| Docs Page | Source Pack Upstream | Canonical Lang | Notes |
| --- | --- | --- | --- |
| `governance/trust-package` | `01_positioning.md` | EN | Audit journey, value proposition |
| `governance/responsibility-boundary` | `01_positioning.md` | EN | Non-goals, RACI, non-overclaim |
| `conformance/index` | `02_conformance.md` | EN | MUST/SHOULD definitions, levels |
| `artifacts/evidence-bundle` | `04_ev_templates/evidence_bundle_toc.md` | EN | TOC structure, traceability |
| `artifacts/minimum-evidence` | `02_conformance.md`, `04_ev_templates/ev_template_full.md` | EN | Lifecycle MUST fields |
| `coverage-map/methodology` | `01_positioning.md` | EN | Non-overclaim reference |
| `standard/current/03-taxonomy` | `03_taxonomy/taxonomy_dictionary_v0.1.csv` | EN | SSOT for taxonomy |
| `standard/current/04-codes` | `03_taxonomy/taxonomy_dictionary_v0.1.csv`, `code_system.csv` | EN | SSOT + derived code system |
| `standard/current/05-dictionary` | `03_taxonomy/taxonomy_dictionary_v0.1.csv` | EN | SSOT for dictionary |
| `standard/current/06-ev-template` | `04_ev_templates/ev_template_min.md`, `ev_template_full.md` | EN | Schema field alignment |
| `standard/current/07-validator` | `05_validator/validation_rules_spec.md` | EN | Rule definitions |
| `validator/index` | `05_validator/reference_impl_notes.md` | EN | Usage, implementation notes |
| `examples/index` | `06_examples/minimal_e2e_story.md` | EN | Narrative walkthrough |
| `releases/index` | `07_release/version_policy_notes.md` | EN | SemVer summary |
| `standard/current/08-changelog` | `07_release/changelog_draft.md` | EN | Template for changelog entries |
| (All docs) | `99_style_guide.md` | EN | Terminology glossary, translation rules |

### 8.3 Source Pack Directory Structure

```
source_pack/
├── 00_manifest.md              # This file (SSOT for content coverage)
├── 01_positioning.md           # Audiences, value prop, non-goals, audit journey
├── 02_conformance.md           # MUST/SHOULD, conformance levels, how-to-claim
├── 03_taxonomy/
│   ├── README.md                        # Taxonomy SSOT format and update guide
│   ├── taxonomy_dictionary_v0.1.csv     # SSOT: Canonical dictionary (91 codes)
│   ├── dictionary_seed.csv              # Compatibility alias (keep for legacy; do not edit directly)
│   ├── taxonomy_dictionary.json         # Generated: JSON format for validation
│   ├── taxonomy_en.yaml                 # Generated: EN taxonomy
│   ├── taxonomy_ja.yaml                 # Generated: JA taxonomy
│   ├── code_system.csv                  # Generated: Code namespaces
│   └── dimensions_en_ja.md              # Generated: EN/JA dimension mapping
├── 04_ev_templates/
│   ├── ev_template_min.md      # Minimum EV template (MUST fields)
│   ├── ev_template_full.md     # Full EV template (+ optional fields)
│   └── evidence_bundle_toc.md  # Bundle TOC structure
├── 05_validator/
│   ├── validation_rules_spec.md    # Human-readable rule spec
│   └── reference_impl_notes.md     # validate.py implementation notes
├── 06_examples/
│   ├── minimal_e2e_story.md    # End-to-end narrative
│   ├── sample_inputs/README.md # Placeholder for input samples
│   └── sample_outputs/README.md # Placeholder for output samples
├── 07_release/
│   ├── changelog_draft.md      # Changelog template
│   └── version_policy_notes.md # VERSIONING.md summary
├── 99_style_guide.md           # Glossary, translation rules, prohibited phrases
└── DIRECTORY_TREE.txt          # Repository structure snapshot
```

### 8.4 Gap Log

Mismatches found during CU-07 but NOT fixed (to avoid changing published docs):

| Gap ID | Description | Location | Action |
| --- | --- | --- | --- |
| GAP-001 | ~~Taxonomy content is TBD in docs~~ | `standard/current/03-taxonomy.md` | **RESOLVED** (CU-TX-01): Full 8-dimension taxonomy now in docs |
| GAP-002 | ~~Codes content is TBD in docs~~ | `standard/current/04-codes.md` | **RESOLVED** (CU-TX-01): Full code system now in docs |
| GAP-003 | ~~Dictionary content is TBD in docs~~ | `standard/current/05-dictionary.md` | **RESOLVED** (CU-TX-01): Full dictionary now in docs |
| GAP-004 | Conformance levels are minimal | `conformance/index.md` | Source Pack documents current state; expansion planned for future CU |

---

## 9. Trust Package PDF Contents

The Trust Package PDF (`trust_package.pdf`, `trust_package.ja.pdf`) includes the following pages in order:

| # | Page | Description |
|---|------|-------------|
| 1 | `governance/trust-package` | Overview, download links, what you get |
| 2 | `governance/responsibility-boundary` | Scope, assumptions, adopter responsibilities (CU-06) |
| 3 | `artifacts/evidence-bundle` | Structure, TOC, traceability |
| 4 | `artifacts/minimum-evidence` | Lifecycle checklist, integrity & access |
| 5 | `coverage-map/methodology` | What mapping is/is not, how to use |
| 6 | `coverage-map/iso-42001` | ISO/IEC 42001 mapping |
| 7 | `coverage-map/nist-ai-rmf` | NIST AI RMF mapping |
| 8 | `coverage-map/eu-ai-act` | EU AI Act mapping |
| 9 | `coverage-map/isms` | ISMS mapping |
| 10 | `releases/index` | Appendix: download, verification, submission |

**Build script**: `tooling/release/build_assets.py`

---

## 10. CU-22 SEO & Canonical Hardening

### 10.1 Overview

CU-22 establishes SEO best practices and canonical URL configuration for the AIMO Standard documentation site at `https://standard.aimoaas.com/`.

### 10.2 Checklist

| Item | Status | Notes |
|------|--------|-------|
| site_url fixed to `https://standard.aimoaas.com/` | ✅ Complete | mkdocs.yml |
| robots.txt present | ✅ Complete | `docs/robots.txt` → `site/robots.txt` |
| sitemap.xml present | ✅ Complete | Auto-generated by mkdocs-static-i18n (includes hreflang alternates) |
| hreflang in sitemap.xml | ✅ Complete | Automatic via mkdocs-static-i18n 1.3.0+ |
| hreflang in HTML head | ✅ Complete | Via `docs/overrides/main.html` template |
| canonical tags | ✅ Complete | Automatic via mkdocs-material theme |
| x-default hreflang | ✅ Complete | Points to EN as default language |

### 10.3 Verification Commands

```bash
# Build site with strict mode
python -m mkdocs build --strict

# Verify robots.txt exists
ls -la site/robots.txt

# Verify sitemap.xml exists with hreflang
head -20 site/sitemap.xml

# Verify canonical tag in EN page
grep 'rel="canonical"' site/index.html

# Verify canonical tag in JA page
grep 'rel="canonical"' site/ja/index.html

# Verify hreflang links in EN page
grep 'hreflang' site/index.html

# Verify hreflang links in JA page
grep 'hreflang' site/ja/index.html
```

### 10.4 Expected Output

- **robots.txt**: Conservative directives with sitemap reference
- **sitemap.xml**: All pages with `<xhtml:link rel="alternate" hreflang="en|ja" ...>` elements
- **HTML head (EN pages)**: `<link rel="canonical" href="https://standard.aimoaas.com/...">` with EN/JA/x-default alternates
- **HTML head (JA pages)**: `<link rel="canonical" href="https://standard.aimoaas.com/ja/...">` with EN/JA/x-default alternates

### 10.5 Files Added/Modified

| File | Change | Purpose |
|------|--------|---------|
| `mkdocs.yml` | Modified | Added `custom_dir: docs/overrides` |
| `docs/robots.txt` | Added | SEO robots directives |
| `docs/overrides/main.html` | Added | hreflang link injection template |

---

## Change Log

| CU | Date | Changes |
|----|------|---------|
| CU-06 | 2026-01-31 | Added: Responsibility Boundary page, expanded Integrity & Access, Submission Package steps, Non-overclaim consistency, Legal quick links, Audit journey sections |
| CU-06.1 | 2026-01-31 | Created: source_pack/00_manifest.md as SSOT, DIRECTORY_TREE.txt |
| CU-06.2 | 2026-01-31 | Updated: Trust Package PDF includes Responsibility Boundary, framework mappings, Releases appendix |
| CU-06.3 | 2026-01-31 | Added: CI guardrail lint_manifest.py to enforce SSOT requirements |
| CU-06.4 | 2026-01-31 | Added: RACI matrix, operational profiles table, auditor verification procedure |
| CU-07 | 2026-01-31 | Added: Complete Source Pack authoring SSOT under source_pack/. Created 01_positioning.md, 02_conformance.md, 03_taxonomy/, 04_ev_templates/, 05_validator/, 06_examples/, 07_release/, 99_style_guide.md. Added docs-to-source-pack mapping table and Gap Log. |
| CU-22 | 2026-01-31 | Added: SEO & canonical hardening. Fixed site_url to https://standard.aimoaas.com/. Added robots.txt, hreflang alternates (sitemap.xml + HTML head via template override). All pages now have canonical and x-default links. |
| CU-TX-01 | 2026-01-31 | Added: Taxonomy Dictionary SSOT (`taxonomy_dictionary_v0.1.csv`) with 91 codes across 8 dimensions. Added `lint_taxonomy_dictionary.py` to CI quality gates. Updated manifest with SSOT declaration and reflection targets. Resolved GAP-001, GAP-002, GAP-003. |
| CU-TX-02 | 2026-01-31 | Added: `tooling/taxonomy/build_taxonomy_assets.py` to generate derived files from CSV SSOT. Generated `taxonomy_en.yaml`, `taxonomy_ja.yaml`, `code_system.csv`, `dimensions_en_ja.md`. Added `--check` mode to CI quality gates. |
| CU-TX-03 | 2026-01-31 | Updated: `docs/standard/current/03-taxonomy.md`, `04-codes.md`, `05-dictionary.md` and their JA counterparts. Added audit context, SSOT references, Non-overclaim links, usage rules, lifecycle metadata, and corrected code counts (91 codes). |
| CU-TX-04 | 2026-01-31 | Updated: schemas (aimo-dictionary/ev/standard.schema.json) with code patterns and taxonomy fields. Updated templates/examples with real taxonomy codes. Updated validator checks. Added taxonomy files to release artifacts. |
| CU-TX-05 | 2026-01-31 | Updated: manifest with Taxonomy & Dictionary section (1.7). Added taxonomy/dictionary links to Trust Package, index.md audit journey and quick links. |
| CU-TAX-01 | 2026-01-31 | Finalized: source_pack/03_taxonomy/ as SSOT. Created dictionary_seed.csv (91 codes, 8 dimensions). Updated README.md with SSOT declaration, column spec, update workflow, compatibility policy. Confirmed taxonomy_en.yaml, taxonomy_ja.yaml, code_system.csv, dimensions_en_ja.md are fully populated. |
