---
description: AIMO localization guide - i18n structure, maintenance workflow, and SSOT principles for multilingual documentation.
---
<!-- aimo:translation_status=source -->

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
├── es/           # Spanish (Español)
├── fr/           # French (Français)
├── de/           # German (Deutsch)
├── pt/           # Portuguese (Português)
├── it/           # Italian (Italiano)
├── zh/           # Simplified Chinese
├── zh-TW/        # Traditional Chinese
└── ko/           # Korean
```

- **English is canonical**: The `docs/en/` folder is the authoritative source for documentation content.
- **Other languages mirror the structure**: Each language folder (`ja/`, etc.) maintains the same file structure as `en/`.
- **Same file names**: All languages use `.md` extension (no language suffix in filenames).
- **Fallback to English**: Missing translations automatically fall back to English content.

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

| Code | Language | Status |
| --- | --- | --- |
| `en` | English | Canonical (source) |
| `ja` | Japanese | Active |
| `es` | Spanish (Español) | Active |
| `fr` | French (Français) | Active |
| `de` | German (Deutsch) | Active |
| `pt` | Portuguese (Português) | Active |
| `it` | Italian (Italiano) | Active |
| `zh` | Simplified Chinese | Active |
| `zh-TW` | Traditional Chinese | Active |
| `ko` | Korean | Active |

### Legacy CSV Files (Frozen)

The legacy EN/JA mixed CSV files in `source_pack/03_taxonomy/legacy/` are:

- **Frozen at 21 columns** — no new language columns will be added
- **Maintained for backward compatibility** — existing integrations can continue to use them
- **CI-enforced** — adding `label_es`, `definition_de`, etc. will fail the build

For new languages, use the per-language artifacts in `artifacts/taxonomy/{version}/{lang}/`.

## Translation Freshness Tracking

AIMO uses a **Translation Freshness Tracking** system to maintain consistency between English (source) and translated content.

### How It Works

1. Each translated file contains metadata tracking which version of the English source it was translated from
2. When English content is updated, the system detects outdated translations
3. CI warns about outdated translations but does not block (translations can lag behind)

### Translation Metadata

Translated files include frontmatter metadata:

```yaml
---
# TRANSLATION METADATA - DO NOT REMOVE
source_file: en/standard/current/01-overview.md
source_hash: abc123def456
translation_date: 2026-02-02
translator: human|machine|hybrid
translation_status: current|outdated|needs_review
---
```

### Translation status marker (hidden)

Every doc page includes a **hidden HTML comment** in the source (immediately after the frontmatter) so that scripts and tools can detect whether the page is the English source or a translated/untranslated variant. It is not visible on the rendered site.

| Value | Meaning |
| --- | --- |
| `<!-- aimo:translation_status=source -->` | English canonical page (`docs/en/`). |
| `<!-- aimo:translation_status=translated -->` | This locale’s content is a translation of the English source. |
| `<!-- aimo:translation_status=untranslated -->` | This locale’s file exists but content is still the English copy; translation pending. |

**How to use**

- To list untranslated pages: `grep -r "aimo:translation_status=untranslated" docs/`
- When adding a new language or page, run `python tooling/i18n/add_translation_markers.py` to insert or fix markers. Use `--strict` to detect untranslated by comparing the first 400 characters of the body with the English file.
- After translating a page, set the marker to `translated` (or re-run the script so it can update the marker).

### Using the Sync Tool

```bash
# Check all translations for freshness
python tooling/i18n/sync_translations.py --check

# Check specific language
python tooling/i18n/sync_translations.py --check --lang ja

# Generate translation report
python tooling/i18n/sync_translations.py --report

# Initialize new language (copy EN as base)
python tooling/i18n/sync_translations.py --init-lang es

# Update metadata after completing translation
python tooling/i18n/sync_translations.py --update-meta docs/ja/index.md
```

For detailed technical specification, see `tooling/i18n/TRANSLATION_SYNC_SPEC.md`.

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
2. Update translations as needed (or mark them for later update)
3. Run `python tooling/i18n/sync_translations.py --check` to see outdated translations
4. Run `python tooling/checks/lint_i18n.py` to verify heading consistency
5. Run `mkdocs build --strict` to verify build
6. Commit all changes together

!!! note "Translation Priority"
    Not all translations need to be updated immediately. Tier 1 (critical) pages should be prioritized:
    
    - `index.md`
    - `standard/current/*.md`
    - `governance/index.md`
    - `releases/`

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

- [Releases](../../releases/) — Downloadable packages
- [Governance](../../governance/) — Project governance
