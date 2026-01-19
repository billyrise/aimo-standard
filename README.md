# AIMO Standard (SSOT)

This repository is the single source of truth (SSOT) for:
- Human-readable specification website (HTML)
- Machine-consumable artifacts (schemas, templates, examples)
- Official PDF releases for audit/approval workflows

## Live Documentation

### Production (Target)
- Current (latest): https://aimoaas.com/standard/  (placeholder - production deployment)
- Versions: https://aimoaas.com/standard/versions/ (placeholder - production deployment)

### GitHub Pages (Temporary)
- Current (latest): https://<ORG>.github.io/aimo-standard/  (temporary - replace <ORG> with actual organization)
- Versions: https://<ORG>.github.io/aimo-standard/versions/  (temporary)

**Note:** The production deployment to `aimoaas.com/standard/` will be configured in a later step. For now, GitHub Pages serves as the temporary hosting location.

## GitHub Releases
- Official PDFs and packaged artifacts are published as GitHub Releases:
  - https://github.com/<ORG>/<REPO>/releases (placeholder - replace <ORG> and <REPO> with actual values)

## Repository Layout
- `docs/` : source content for spec website and PDF (EN canonical, JA translated)
- `schemas/` : JSON Schemas for implementers
- `templates/` : reference templates (human + machine readable)
- `examples/` : minimal examples for quick adoption
- `validator/` : validation rules (spec + minimal reference implementation)
- `tooling/` : build/lint scripts

## Principles
- GitHub repo is SSOT; do not hand-edit generated outputs.
- English is canonical; Japanese follows via `.ja.md` files.
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

### Production Target (Future)
- **Hosting:** `https://aimoaas.com/standard/`
- **Approach:** The SSOT and build pipeline remain unchanged. Only the deployment target will be switched.
- **Options:**
  - Cloudflare Pages (or Workers routing `/standard/` to the built site)
  - Integration with existing `aimoaas.com` hosting infrastructure
- **Note:** This change will be implemented in a subsequent step. The current GitHub Pages setup serves as proof of concept and temporary hosting.

## License & Trademarks
- License: see LICENSE.txt and NOTICE.txt
- Trademarks: see TRADEMARKS.md
