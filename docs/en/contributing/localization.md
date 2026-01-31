# Localization Guide

This page documents the localization (i18n) structure, maintenance workflow, and SSOT (Single Source of Truth) principles for the AIMO Standard documentation.

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

AIMO uses multiple Single Source of Truth files:

| Asset Type | SSOT Location | Description |
| --- | --- | --- |
| **Taxonomy (source)** | `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv` | Master CSV with all data |
| **Taxonomy (canonical)** | `data/taxonomy/canonical.yaml` | Language-neutral structure |
| **Taxonomy (i18n)** | `data/taxonomy/i18n/*.yaml` | Per-language translations |
| **Coverage Map** | `coverage_map/coverage_map.yaml` | Framework-to-evidence mapping |
| **Schemas** | `schemas/jsonschema/` | JSON validation schemas |

### Derived Files

The following files are **generated** and should NOT be edited manually:

| File | Generated From | Generator |
| --- | --- | --- |
| `data/taxonomy/canonical.yaml` | `taxonomy_dictionary_v0.1.csv` | `build_i18n_taxonomy.py` |
| `data/taxonomy/i18n/en.yaml` | `taxonomy_dictionary_v0.1.csv` | `build_i18n_taxonomy.py` |
| `data/taxonomy/i18n/ja.yaml` | `taxonomy_dictionary_v0.1.csv` | `build_i18n_taxonomy.py` |
| `source_pack/03_taxonomy/taxonomy_en.yaml` | `taxonomy_dictionary_v0.1.csv` | `build_taxonomy_assets.py` |
| `source_pack/03_taxonomy/taxonomy_ja.yaml` | `taxonomy_dictionary_v0.1.csv` | `build_taxonomy_assets.py` |
| `source_pack/03_taxonomy/code_system.csv` | `taxonomy_dictionary_v0.1.csv` | `build_taxonomy_assets.py` |
| `source_pack/03_taxonomy/dimensions_en_ja.md` | `taxonomy_dictionary_v0.1.csv` | `build_taxonomy_assets.py` |
| `source_pack/03_taxonomy/taxonomy_dictionary.json` | `taxonomy_dictionary_v0.1.csv` | `build_taxonomy_assets.py` |

## Update Workflows

### Taxonomy Updates

1. Edit the SSOT CSV (`source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv`)
2. Run validation: `python tooling/checks/lint_taxonomy_dictionary.py`
3. Regenerate legacy assets: `python tooling/taxonomy/build_taxonomy_assets.py`
4. Regenerate i18n assets: `python tooling/taxonomy/build_i18n_taxonomy.py`
5. Sync `dictionary_seed.csv` as compatibility copy
6. Update documentation pages as needed
7. Commit all changes together

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

## Adding a New Language

To add a new language (e.g., Spanish):

### Step 1: Create Taxonomy Translation Pack

```bash
python tooling/taxonomy/build_i18n_taxonomy.py --add-lang es --lang-name "Español"
```

This creates `data/taxonomy/i18n/es.yaml` with an empty template containing English references as comments.

### Step 2: Create Documentation Structure

```bash
mkdir -p docs/es
cp -r docs/en/* docs/es/
```

### Step 3: Update MkDocs Configuration

Add the language to `mkdocs.yml`:

```yaml
plugins:
  - i18n:
      languages:
        # ... existing languages ...
        - locale: es
          name: Español
          build: true
```

### Step 4: Translate Content

1. Translate taxonomy labels in `data/taxonomy/i18n/es.yaml`
2. Translate documentation files in `docs/es/`
3. Run `mkdocs build --strict` to verify

## File Naming Conventions

| Pattern | Example | Description |
| --- | --- | --- |
| `index.md` | `docs/en/governance/index.md` | Section landing page |
| `{topic}.md` | `docs/en/governance/trust-package.md` | Topic page |
| `{NN}-{topic}.md` | `docs/en/standard/current/03-taxonomy.md` | Numbered specification page |

## Quality Checks

Run these checks before committing:

```bash
# i18n structure and heading consistency
python tooling/checks/lint_i18n.py

# All other lints
python tooling/checks/lint_schema.py
python tooling/checks/lint_manifest.py
python tooling/checks/lint_taxonomy_dictionary.py
python tooling/checks/lint_taxonomy_json.py

# Taxonomy assets up to date
python tooling/taxonomy/build_taxonomy_assets.py --check
python tooling/taxonomy/build_i18n_taxonomy.py --check

# Build verification
mkdocs build --strict
```

## Related Pages

- [Releases](../releases/index.md) — Downloadable packages
- [Governance](../governance/index.md) — Project governance
