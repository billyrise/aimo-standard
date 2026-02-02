# Translation Synchronization Specification

This document defines the translation synchronization strategy for AIMO Standard multilingual documentation.

## Overview

AIMO uses a **"Translation Freshness Tracking"** approach to maintain consistency between English (source) and translated content.

### Supported Languages

| Code | Language | Native Name | Status |
|------|----------|-------------|--------|
| `en` | English | English | Canonical (source) |
| `ja` | Japanese | 日本語 | Active |
| `es` | Spanish | Español | Active |
| `fr` | French | Français | Active |
| `de` | German | Deutsch | Active |
| `pt` | Portuguese | Português | Active |
| `it` | Italian | Italiano | Active |
| `zh` | Simplified Chinese | 简体中文 | Active |
| `zh-TW` | Traditional Chinese | 繁體中文 | Active |
| `ko` | Korean | 한국어 | Active |

## Translation Freshness Tracking

### Concept

Each translated file contains metadata tracking which version of the English source it was translated from:

```yaml
---
# TRANSLATION METADATA - DO NOT REMOVE
source_file: en/standard/current/01-overview.md
source_commit: abc1234  # Git commit hash of source when translated
source_hash: sha256:...  # Content hash for non-git environments
translation_date: 2026-02-02
translator: human|machine|hybrid
translation_status: current|outdated|needs_review
---
```

### Workflow

1. **On English Update**: When `docs/en/*` files are modified:
   - `sync_translations.py --check` detects changes
   - Creates GitHub Issue or adds to translation dashboard
   - CI warns but does not block (translations can lag behind)

2. **On Translation Update**: When `docs/{lang}/*` files are updated:
   - Update `source_commit`, `source_hash`, `translation_date`
   - Set `translation_status: current`

3. **Automated Detection**: CI runs `sync_translations.py --check`:
   - Compares current EN hash vs recorded `source_hash`
   - Reports outdated translations
   - Optionally generates translation diff

## File Structure

```
docs/
├── en/                     # Canonical source (English)
│   ├── index.md
│   ├── standard/
│   │   └── current/
│   │       ├── 01-overview.md
│   │       └── ...
│   └── ...
├── ja/                     # Japanese translation
│   ├── index.md
│   ├── standard/
│   │   └── current/
│   │       ├── 01-overview.md
│   │       └── ...
│   └── ...
├── es/                     # Spanish translation
├── fr/                     # French translation
├── de/                     # German translation
├── pt/                     # Portuguese translation
├── it/                     # Italian translation
├── zh/                     # Simplified Chinese
├── zh-TW/                  # Traditional Chinese
└── ko/                     # Korean translation
```

## Translation Priority Tiers

Not all pages require immediate translation. Priority is based on page importance:

### Tier 1: Critical (Must Translate)
- `index.md` (homepage)
- `standard/index.md`
- `standard/current/*.md` (all specification pages)
- `governance/index.md`
- `releases/index.md`

### Tier 2: High Priority
- `coverage-map/index.md`
- `coverage-map/methodology.md`
- `artifacts/index.md`
- `validator/index.md`

### Tier 3: Standard
- All other pages

## Tooling

### `sync_translations.py`

Main synchronization tool with the following commands:

```bash
# Check all translations for freshness
python tooling/i18n/sync_translations.py --check

# Check specific language
python tooling/i18n/sync_translations.py --check --lang ja

# Generate translation report
python tooling/i18n/sync_translations.py --report

# Initialize new language (copy EN as base)
python tooling/i18n/sync_translations.py --init-lang es

# Update metadata after translation
python tooling/i18n/sync_translations.py --update-meta docs/ja/index.md
```

### `lint_i18n.py`

Quality checks (extended for new languages):
- Language purity (no CJK in EN, no Latin-only in CJK pages)
- Required pages exist
- Heading structure consistency
- Deprecated phrase detection

## Automated Translation Workflow

### Initial Translation (Machine + Review)

For initial population of new languages:

1. Copy English source: `cp -r docs/en/* docs/{lang}/`
2. Add translation metadata headers
3. Queue for machine translation (optional, external service)
4. Mark as `translation_status: needs_review`
5. Human review and approval
6. Update to `translation_status: current`

### Continuous Updates

When English content is updated:

1. `sync_translations.py` detects hash mismatch
2. Generates diff showing what changed in EN
3. Creates translation task (GitHub Issue or external tracker)
4. Translator updates translation
5. Run `sync_translations.py --update-meta` to refresh hash

## Taxonomy Translation

Taxonomy uses a separate SSOT structure:

```
data/taxonomy/
├── canonical.yaml           # Language-neutral structure
└── i18n/
    ├── en.yaml              # English labels
    ├── ja.yaml              # Japanese labels
    ├── es.yaml              # Spanish labels
    └── ...                  # Other languages
```

Generate taxonomy i18n packs:
```bash
python tooling/taxonomy/build_i18n_taxonomy.py --add-lang es --lang-name "Español"
```

## CI Integration

### Quality Gate (Non-blocking)

```yaml
# .github/workflows/quality-gate.yml
- name: Check Translation Freshness
  run: python tooling/i18n/sync_translations.py --check || true
  continue-on-error: true  # Warn, don't fail
```

### Pre-release Check

```yaml
# .github/workflows/prepare-release.yml
- name: Translation Coverage Report
  run: python tooling/i18n/sync_translations.py --report
```

## Best Practices

1. **English First**: Always update English, then translations
2. **Atomic Updates**: Update EN and critical translations in same PR when possible
3. **Review Threshold**: If >30% of a page changed, consider full re-translation
4. **Fallback**: Missing translations fall back to English automatically
5. **No Machine Publish**: Machine translations should always be reviewed before marking as `current`

## Migration Notes

### Existing Japanese Content

Japanese translations (`docs/ja/`) predate this system. Migration:
1. Add translation metadata headers
2. Compute current EN hash as baseline
3. Mark as `translation_status: current` (assume reviewed)

### Adding New Languages

Follow the 5-step process in [Localization Guide](../../docs/en/contributing/localization.md):
1. Generate taxonomy pack
2. Create docs folder (copy EN)
3. Update mkdocs.yml
4. Translate content
5. Verify build
