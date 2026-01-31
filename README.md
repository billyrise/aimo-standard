# AIMO Standard (SSOT)

This repository is the single source of truth (SSOT) for:
- Human-readable specification website (HTML)
- Machine-consumable artifacts (schemas, templates, examples)
- Official PDF releases for audit/approval workflows

## Live Documentation

### Production
- Current (latest): https://standard.aimoaas.com/latest/
- Versions: https://standard.aimoaas.com/latest/standard/versions/

### GitHub Pages (Temporary)
- Current (latest): https://billyrise.github.io/aimo-standard/latest/  (temporary)
- Versions: https://billyrise.github.io/aimo-standard/latest/standard/versions/  (temporary)

## GitHub Releases
- Official PDFs and packaged artifacts are published as GitHub Releases:
  - https://github.com/billyrise/aimo-standard/releases

Each release includes:
- `trust_package.pdf` — English Trust Package (auditor-ready)
- `trust_package.ja.pdf` — Japanese Trust Package
- `aimo-standard-artifacts.zip` — Schemas, templates, examples, validator rules
- `SHA256SUMS.txt` — Checksums for verification

## Repository Layout
- `docs/` : source content for spec website and PDF (EN canonical, JA translated)
- `schemas/` : JSON Schemas for implementers
- `templates/` : reference templates (human + machine readable)
- `examples/` : minimal examples for quick adoption
- `validator/` : validation rules (spec + minimal reference implementation)
- `tooling/` : build/lint scripts

## Principles
- GitHub repo is SSOT; do not hand-edit generated outputs.
- English is canonical; translations use folder-based structure (`docs/en/`, `docs/ja/`, etc.).
- Taxonomy SSOT is `data/taxonomy/canonical.yaml` + `i18n/*.yaml`; CSVs are generated artifacts.
- "Current" and "Past" versions must be clearly accessible.
- Releases must include PDF, checksum, and (when available) build attestation.

## Quick Start (Local)
### 1) Create venv and install dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

### 2) Serve docs locally
```bash
mkdocs serve
```

### 3) Run linters
```bash
python tooling/checks/lint_i18n.py
python tooling/checks/lint_schema.py
```

## Deployment Strategy

### Current Setup (Temporary)
- **Hosting:** GitHub Pages (`https://<ORG>.github.io/aimo-standard/`)
- **Deployment:** Automatic via GitHub Actions on `main` branch push
- **Versioning:** Managed by `mike` (current as `dev` alias `latest`, tagged versions preserved)

### Production
- **Hosting:** `https://standard.aimoaas.com/`
- **Deployment:** Production deployment is active
- **Note:** GitHub Pages (`https://billyrise.github.io/aimo-standard/`) serves as a temporary backup/mirror

## License & Trademarks
- License: see LICENSE.txt and NOTICE.txt
- Trademarks: see TRADEMARKS.md
