# PDF Generation

## Overview

The Trust Package PDF is an auditor-ready document bundling key governance and compliance materials.

**Outputs** (stored under `dist/`, not committed):

- `trust_package.pdf` — English Trust Package
- `trust_package.ja.pdf` — Japanese Trust Package (optional)
- `aimo-standard-artifacts.zip` — Schemas, templates, examples, validator rules
- `SHA256SUMS.txt` — Checksums for verification

## Local Build

### Prerequisites

1. Install Python dependencies:

```bash
pip install -r requirements.txt
pip install -r tooling/requirements.txt
```

2. Install system dependencies for WeasyPrint:

**macOS:**

```bash
brew install pango cairo gdk-pixbuf libffi
```

**Ubuntu/Debian:**

```bash
# Core libraries
sudo apt-get install -y libpango-1.0-0 libpangocairo-1.0-0 libcairo2 libgdk-pixbuf2.0-0

# Fonts (required for Japanese PDF)
sudo apt-get install -y fonts-noto-cjk fonts-noto-core fonts-noto-color-emoji
```

**Note:** For Japanese PDF generation, ensure `LANG=C.UTF-8` and `LC_ALL=C.UTF-8` are set in your environment.

### Build Commands

```bash
# Build EN PDF + artifacts zip
python tooling/release/build_assets.py

# Build EN + JA PDFs + artifacts zip
python tooling/release/build_assets.py --ja

# Build PDFs only (no zip)
python tooling/release/build_assets.py --pdf-only

# Build zip only (no PDFs)
python tooling/release/build_assets.py --zip-only

# Specify version explicitly
python tooling/release/build_assets.py --version 1.0.0
```

### Output

All artifacts are placed in `dist/`:

```
dist/
├── trust_package.pdf
├── trust_package.ja.pdf    (if --ja)
├── aimo-standard-artifacts.zip
└── SHA256SUMS.txt
```

## CI/CD

The GitHub Actions release workflow (`release.yml`) automatically:

1. Runs quality gates (lint, test)
2. Builds PDFs and artifacts zip
3. Generates checksums
4. Uploads all assets to the GitHub Release

## Trust Package Contents

The PDF includes:

- Trust Package overview
- Conformance levels
- Coverage Map index and methodology
- Evidence Bundle structure
- Minimum Evidence requirements

## Artifacts Zip Contents

The zip includes:

- `schemas/jsonschema/*` — JSON Schemas
- `templates/ev/*` — Evidence templates
- `examples/*` — Sample bundles
- `coverage_map/coverage_map.yaml` — Coverage mapping
- `validator/rules/*` — Validation rules
- `VERSIONING.md`, `GOVERNANCE.md`, `SECURITY.md`, etc.
