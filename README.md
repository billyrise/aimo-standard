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

## Release Process

The release process is fully automated via GitHub Actions, with a two-step workflow to prevent version mismatch errors.

**Quality gates:** Both **prepare-release** and **release** run the same critical quality gates (including `lint_hidden_unicode`, `lint_schema`, and Evidence Bundle validator). A release cannot succeed if the repo would fail the PR quality-gate checks — no bypass.

### Step 1: Prepare Release (Automated Version Bump)

1. Go to **Actions** → **prepare-release** → **Run workflow**
2. Enter the new version number (e.g., `0.1.x`) — do NOT include the `v` prefix
3. Click **Run workflow**

This will:
- Run quality gates (hidden-unicode, schema lint, Evidence Bundle v0.1 minimal validation)
- Automatically update all version references (Versions pages, Cite pages, CITATION.cff)
- Verify consistency with `check_release_consistency.py`
- Create a PR with all changes

### Step 2: Tag and Release (Automated Deployment)

1. Review and merge the PR created in Step 1
2. Create and push the release tag:
   ```bash
   git tag v0.1.x
   git push origin v0.1.x
   ```

This will automatically:
- Run the same full quality gates as PR (bidi, hidden-unicode, schema, lints, pytest, Evidence Bundle validator)
- Run consistency checks (fails if versions don't match)
- Build docs with `mkdocs build --strict`
- Deploy via `mike` with `latest` alias update
- Create GitHub Release with assets (PDFs, ZIPs, checksums)
- Generate build provenance attestations

### Release Assets

Each release includes:
| Asset | Description |
| ----- | ----------- |
| `trust_package.pdf` | English Trust Package (auditor-ready) |
| `trust_package.ja.pdf` | Japanese Trust Package |
| `aimo-standard-artifacts.zip` | Schemas, templates, examples, validator rules |
| `aimo-standard-X.Y.Z-src.zip` | Source code snapshot |
| `aimo-standard-X.Y.Z-site.zip` | Built documentation site |
| `SHA256SUMS.txt` | SHA-256 checksums for verification |

### Prerequisites for Automated PR Creation

The `prepare-release` workflow uses [peter-evans/create-pull-request](https://github.com/peter-evans/create-pull-request).
For this to work, ensure:
- **Repository Settings** → **Actions** → **General** → **Workflow permissions**:
  - Select "Read and write permissions"
  - Check "Allow GitHub Actions to create and approve pull requests"

## Deployment Strategy

### Current Setup (Temporary)
- **Hosting:** GitHub Pages (`https://<ORG>.github.io/aimo-standard/`)
- **Deployment:** Automatic via GitHub Actions on `main` branch push
- **Versioning:** Managed by `mike` (current as `dev` alias `latest`, tagged versions preserved)

### Production
- **Hosting:** `https://standard.aimoaas.com/`
- **Deployment:** Production deployment is active
- **Note:** GitHub Pages (`https://billyrise.github.io/aimo-standard/`) serves as a temporary backup/mirror

## Governance & Policies

| Resource | Description |
| -------- | ----------- |
| [Governance (Website)](https://standard.aimoaas.com/latest/governance/) | Full governance documentation |
| [Trust Package](https://standard.aimoaas.com/latest/governance/trust-package/) | Auditor-ready materials |
| [SECURITY.md](SECURITY.md) | Security policy and vulnerability reporting |
| [CITATION.cff](CITATION.cff) | How to cite AIMO Standard |
| [LICENSE.txt](LICENSE.txt) | Apache-2.0 license |
| [NOTICE.txt](NOTICE.txt) | Attribution notice |
| [TRADEMARKS.md](TRADEMARKS.md) | Trademark usage guidelines |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Community guidelines |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |
