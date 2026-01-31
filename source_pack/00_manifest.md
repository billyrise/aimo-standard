# AIMO Standard Content Manifest

**Status**: Single Source of Truth (SSOT) for documentation coverage  
**Last updated**: CU-06.1 (2026-01-31)

This manifest is the canonical checklist for auditor-first documentation. All CU (Change Unit) changes that affect documentation scope must update this file.

---

## How to use this manifest

1. **Before implementing a CU**: Check this manifest to understand current coverage state.
2. **After implementing a CU**: Update the relevant checklist items with implementation status and target pages.
3. **For audits**: Use this manifest to verify that all required content exists and is discoverable.
4. **EN is canonical**: This manifest is maintained in English only. Japanese documentation mirrors the same structure via `*.ja.md` files.

**Rule**: This manifest is SSOT for content coverage; CU changes must update this file.

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

## 7. Trust Package PDF Contents

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

## Change Log

| CU | Date | Changes |
|----|------|---------|
| CU-06 | 2026-01-31 | Added: Responsibility Boundary page, expanded Integrity & Access, Submission Package steps, Non-overclaim consistency, Legal quick links, Audit journey sections |
| CU-06.1 | 2026-01-31 | Created: source_pack/00_manifest.md as SSOT, DIRECTORY_TREE.txt |
| CU-06.2 | 2026-01-31 | Updated: Trust Package PDF includes Responsibility Boundary, framework mappings, Releases appendix |
