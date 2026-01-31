# Taxonomy (Authoring SSOT)

**Status**: Authoring input — not user-facing documentation  
**Canonical language**: English (EN)

This directory contains the taxonomy definitions for the AIMO Standard. The taxonomy provides dimensions, codes, and dictionary seeds for evidence categorization.

---

## Directory Contents

| File | Purpose | Status |
| --- | --- | --- |
| `taxonomy_en.yaml` | English taxonomy definitions (SSOT) | Placeholder — TBD |
| `taxonomy_ja.yaml` | Japanese taxonomy translations | Placeholder — TBD |
| `code_system.csv` | Code namespace definitions | Header only — TBD |
| `dimensions_en_ja.md` | Dimension names EN/JA mapping table | Populated from existing docs |
| `dictionary_seed.csv` | Initial dictionary entries seed | Header only — TBD |

---

## Intended SSOT Format

### taxonomy_*.yaml

```yaml
version: "0.1.0"
dimensions:
  - id: dimension_id
    name_en: "English name"
    name_ja: "日本語名"
    description_en: "English description"
    description_ja: "日本語説明"
    codes:
      - id: code_id
        label_en: "English label"
        label_ja: "日本語ラベル"
```

### code_system.csv

```csv
namespace,prefix,description,example
```

### dictionary_seed.csv

```csv
key,label_en,label_ja,description_en,description_ja
```

---

## How to Update

1. **Edit taxonomy_en.yaml first** (English is canonical).
2. **Update taxonomy_ja.yaml** to match structure and add Japanese translations.
3. **Regenerate user-facing docs** from these files (process TBD).
4. **Run lint checks** to ensure consistency.

---

## Current Status

The AIMO Standard specification notes that taxonomy is TBD:

> From `docs/standard/current/03-taxonomy.md`:
> "TBD: define dimensions and their relationships. This section will become normative once finalized."

> From `docs/standard/current/04-codes.md`:
> "TBD: define code namespaces, formats, and examples."

> From `docs/standard/current/05-dictionary.md`:
> "TBD: initial entries and extension rules."

Until authoritative taxonomy content is defined, this directory contains placeholder files with structure only.

---

## Authoring Notes

- Do NOT invent taxonomy entries. Use placeholders marked "TBD".
- Once authoritative source is available, populate from that source.
- Any schema changes to taxonomy require MAJOR version bump per VERSIONING.md.
