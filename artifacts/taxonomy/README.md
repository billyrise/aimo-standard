# Taxonomy Artifacts

**Status**: Generated distribution files  
**DO NOT EDIT MANUALLY** - regenerate with: `python tooling/taxonomy/build_artifacts.py`

This directory contains **single-language CSV files** for distribution to end users.

---

## Directory Structure

```
artifacts/taxonomy/
├── README.md           # This file
├── current/            # Current version (symlink or copy)
│   ├── en/
│   │   └── taxonomy_dictionary.csv
│   └── ja/
│       └── taxonomy_dictionary.csv
└── {version}/          # Versioned releases (e.g., 0.1.0/)
    ├── en/
    │   └── taxonomy_dictionary.csv
    └── ja/
        └── taxonomy_dictionary.csv
```

## File Format

Each language-specific CSV (`taxonomy_dictionary.csv`) contains:

| Column | Description |
| --- | --- |
| `code` | Unique code identifier (e.g., `FS-001`) |
| `dimension` | Dimension ID (e.g., `FS`) |
| `dimension_name` | Dimension name in this language |
| `label` | Code label in this language |
| `definition` | Code definition in this language |
| `status` | Code status (`active`, `deprecated`, `removed`) |
| `introduced_in` | Version when code was introduced |
| `scope_notes` | Usage notes (English) |
| `examples` | Example use cases (pipe-separated) |

**Note**: Each file contains only the specified language's translations. No mixed-language columns.

## Which File Should I Use?

| Your Language | File to Use |
| --- | --- |
| English | `artifacts/taxonomy/current/en/taxonomy_dictionary.csv` |
| Japanese | `artifacts/taxonomy/current/ja/taxonomy_dictionary.csv` |
| Other | Check if your language is available; if not, use English |

## Single Source of Truth (SSOT)

The SSOT for taxonomy is:

| Type | Location | Purpose |
| --- | --- | --- |
| Structure | `data/taxonomy/canonical.yaml` | Codes, status, lifecycle |
| English | `data/taxonomy/i18n/en.yaml` | English labels and definitions |
| Japanese | `data/taxonomy/i18n/ja.yaml` | Japanese labels and definitions |
| Other | `data/taxonomy/i18n/{lang}.yaml` | Additional language translations |

**These CSV files are derived** from the SSOT and regenerated on each release.

## Legacy Files

For backward compatibility, English-Japanese mixed CSV files are maintained in:

```
source_pack/03_taxonomy/legacy/
```

**Warning**: Legacy files will NOT gain new language columns. For new languages, use the per-language artifacts.

## Generation Command

```bash
# Generate all configured languages
python tooling/taxonomy/build_artifacts.py --version current --langs en ja

# Generate specific version
python tooling/taxonomy/build_artifacts.py --version 0.1.0 --langs en ja

# Add a new language (requires i18n pack first)
python tooling/taxonomy/build_i18n_taxonomy.py --add-lang es --lang-name "Español"
python tooling/taxonomy/build_artifacts.py --version current --langs en ja es
```

## Adding a New Language

1. Create i18n pack: `python tooling/taxonomy/build_i18n_taxonomy.py --add-lang {code} --lang-name "{Name}"`
2. Translate `data/taxonomy/i18n/{code}.yaml`
3. Regenerate artifacts: `python tooling/taxonomy/build_artifacts.py --version current --langs en ja {code}`

The legacy mixed-language CSV is NOT updated. New languages are only available via per-language artifacts.

---

## Language Codes (BCP47)

| Code | Language |
| --- | --- |
| `en` | English |
| `ja` | Japanese (日本語) |
| `es` | Spanish (Español) |
| `de` | German (Deutsch) |
| `ko` | Korean (한국어) |
| `zh-Hans` | Simplified Chinese (简体中文) |
| `zh-Hant` | Traditional Chinese (繁體中文) |
