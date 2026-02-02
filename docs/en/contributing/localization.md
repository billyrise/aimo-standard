---
description: AIMO localization guide - i18n structure, maintenance workflow, and SSOT principles for multilingual documentation.
---

# Localization Guide

This page documents the localization (i18n) structure, maintenance workflow, and SSOT (Single Source of Truth) principles for the AIMO Standard documentation.

## Language Purity Policy

**Each language page should contain only that language's content.**

| Rule | Description |
| --- | --- |
| **EN pages** | Must not contain CJK characters or references to language-specific columns (e.g., `_ja` suffixes) |
| **JA pages** | Must not explain EN-specific terminology as if it were the canonical structure |
| **Exceptions** | Listed in `MIXED_LANGUAGE_ALLOWLIST` in `tooling/checks/lint_i18n.py` |

This policy ensures:
1. Readers see only their selected language
2. Adding new languages doesn't require updating existing pages
3. CI can automatically detect violations

## Language Structure

The AIMO Standard documentation uses a **folder-based i18n structure**:

```
docs/
├── en/           # English (canonical)
├── ja/           # Japanese
├── es/           # Future: Spanish
├── de/           # Future: German
├── ko/           # Future: Korean
├── zh-hans/      # Future: Simplified Chinese
└── zh-hant/      # Future: Traditional Chinese
```

- **English is canonical**: The `docs/en/` folder is the authoritative source for documentation content.
- **Other languages mirror the structure**: Each language folder (`ja/`, etc.) maintains the same file structure as `en/`.
- **Same file names**: All languages use `.md` extension (no language suffix in filenames).

## Taxonomy Data Model

The taxonomy uses a **language-neutral canonical structure** with separate translation packs:

```
data/
└── taxonomy/
    ├── canonical.yaml           # Language-neutral (codes, status, lifecycle)
    └── i18n/
        ├── en.yaml              # English labels and definitions
        ├── ja.yaml              # Japanese labels and definitions
        └── {lang}.yaml          # Additional languages (empty template)
```

### Canonical Structure (`canonical.yaml`)

Contains language-neutral data:

- Code identifiers (e.g., `FS-001`, `UC-001`)
- Status (`active`, `deprecated`, `removed`)
- Lifecycle metadata (`introduced_in`, `deprecated_in`, `removed_in`, `replaced_by`)
- Scope notes and examples (in English, as technical references)

### Translation Packs (`i18n/*.yaml`)

Each language pack contains:

- Dimension names (e.g., "Functional Scope")
- Code labels (e.g., "End-user Productivity")
- Code definitions

**Fallback**: If a translation is missing, the system uses English.

## SSOT Principle

AIMO uses a **SSOT-first architecture** for taxonomy data:

| Asset Type | SSOT Location | Description |
| --- | --- | --- |
| **Taxonomy (structure)** | `data/taxonomy/canonical.yaml` | Language-neutral structure (SSOT) |
| **Taxonomy (i18n)** | `data/taxonomy/i18n/*.yaml` | Per-language translations (SSOT) |
| **Coverage Map** | `coverage_map/coverage_map.yaml` | Framework-to-evidence mapping |
| **Schemas** | `schemas/jsonschema/` | JSON validation schemas |

### Derived Files

The following files are **generated** from the SSOT and should NOT be edited manually:

| File | Generated From | Generator |
| --- | --- | --- |
| `artifacts/taxonomy/{version}/{lang}/taxonomy_dictionary.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_en.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_ja.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/code_system.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/dimensions_en_ja.md` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_dictionary.json` | canonical + i18n | `build_artifacts.py` |

### Language Codes (BCP47)

AIMO uses BCP47 language codes:

| Code | Language |
| --- | --- |
| `en` | English |
| `ja` | Japanese (日本語) |
| `es` | Spanish (Español) |
| `de` | German (Deutsch) |
| `ko` | Korean (한국어) |
| `zh-Hans` | Simplified Chinese (简体中文) |
| `zh-Hant` | Traditional Chinese (繁體中文) |

### Legacy CSV Files (Frozen)

The legacy EN/JA mixed CSV files in `source_pack/03_taxonomy/legacy/` are:

- **Frozen at 21 columns** — no new language columns will be added
- **Maintained for backward compatibility** — existing integrations can continue to use them
- **CI-enforced** — adding `label_es`, `definition_de`, etc. will fail the build

For new languages, use the per-language artifacts in `artifacts/taxonomy/{version}/{lang}/`.

## Update Workflows

### Taxonomy Updates (New SSOT-First Workflow)

1. Edit the SSOT in `data/taxonomy/`:
   - Structure changes → `canonical.yaml`
   - English translations → `i18n/en.yaml`
   - Japanese translations → `i18n/ja.yaml`
2. Run validation: `python tooling/checks/lint_taxonomy_ssot.py`
3. Regenerate all derived files: `python tooling/taxonomy/build_artifacts.py --version current --langs en ja`
4. Update documentation pages as needed
5. Commit all changes together

### Coverage Map Updates

1. Edit `coverage_map/coverage_map.yaml` (the SSOT)
2. Update the corresponding framework page tables (`docs/en/coverage-map/*.md`)
3. Update Japanese translations (`docs/ja/coverage-map/*.md`)
4. Commit all changes together

### Documentation Updates

1. Edit the English source (`docs/en/...`)
2. Update the corresponding Japanese file (`docs/ja/...`)
3. Run `python tooling/checks/lint_i18n.py` to verify heading consistency
4. Run `mkdocs build --strict` to verify build
5. Commit all changes together

## Adding a New Language (5 Steps)

To add a new language (e.g., Spanish):

### Step 1: Generate Taxonomy Pack

```bash
python tooling/taxonomy/build_i18n_taxonomy.py --add-lang es --lang-name "Español"
```

Creates `data/taxonomy/i18n/es.yaml` with English references as comments.

### Step 2: Create Docs Folder

```bash
mkdir -p docs/es && cp -r docs/en/* docs/es/
```

### Step 3: Update mkdocs.yml

```yaml
plugins:
  - i18n:
      languages:
        - locale: es
          name: Español
          build: true
```

### Step 4: Translate

- Translate `data/taxonomy/i18n/es.yaml`
- Translate files in `docs/es/`

### Step 5: Verify

```bash
python tooling/checks/lint_i18n.py && mkdocs build --strict
```

!!! success "Done"
    New language is now available at `/dev/es/`

## File Naming Conventions

| Pattern | Example | Description |
| --- | --- | --- |
| `index.md` | `docs/en/governance/index.md` | Section landing page |
| `{topic}.md` | `docs/en/governance/trust-package.md` | Topic page |
| `{NN}-{topic}.md` | `docs/en/standard/current/03-taxonomy.md` | Numbered specification page |

## Quality Checks

Run these checks before committing:

```bash
# i18n structure, heading consistency, and deprecated phrase detection
python tooling/checks/lint_i18n.py

# Schema and manifest lints
python tooling/checks/lint_schema.py
python tooling/checks/lint_manifest.py

# Taxonomy SSOT lints
python tooling/checks/lint_taxonomy_ssot.py --required-langs en
python tooling/checks/lint_legacy_csv.py
python tooling/checks/lint_taxonomy_dictionary.py
python tooling/checks/lint_taxonomy_json.py

# Taxonomy artifacts up to date
python tooling/taxonomy/build_artifacts.py --check

# Build verification
mkdocs build --strict
```

## Related Pages

- [Releases](../releases/index.md) — Downloadable packages
- [Governance](../governance/index.md) — Project governance
