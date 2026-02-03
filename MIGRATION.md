# Migration Guide: Multi-language Taxonomy and Documentation

This guide documents the migration from language-coupled taxonomy data to a language-neutral structure with separate translation packs.

## v0.1 ID namespace: EV (Taxonomy) → LG (Log/Event Type)

In **AIMO Standard v0.1**, the taxonomy dimension for classifying log/event types (request record, access log, etc.) uses the **LG-** prefix only. The **EV-** prefix is reserved exclusively for **Evidence artifact IDs** (e.g. `evidence[].id`, bundle object identifiers).

- **If you have existing taxonomy codes** such as `EV-001` … `EV-015` (formerly "Evidence Type"): treat them as **LG-001** … **LG-015** in v0.1. Update `evidence[].codes` to use `"LG": ["LG-001", …]` instead of `"EV": ["EV-001", …]`.
- **Validators** reject use of `EV` as a taxonomy dimension in `evidence[].codes`; use `LG` and `LG-xxx` codes only for the log/event dimension.
- See [ID Policy / Namespace (04b)](docs/en/standard/current/04b-id-policy-namespace.md) for the normative definition.

Migration scripts to rename EV-* to LG-* in existing payloads are optional; the mapping is a direct substitution (EV-001 → LG-001, etc.) for the same code set.

### Deterministic conversion table (EV-xxx → LG-xxx)

| Old (taxonomy, forbidden in v0.1) | New (taxonomy, use in `evidence[].codes.LG`) |
|-----------------------------------|-----------------------------------------------|
| EV-001 | LG-001 |
| EV-002 | LG-002 |
| EV-003 | LG-003 |
| EV-004 | LG-004 |
| EV-005 | LG-005 |
| EV-006 | LG-006 |
| EV-007 | LG-007 |
| EV-008 | LG-008 |
| EV-009 | LG-009 |
| EV-010 | LG-010 |
| EV-011 | LG-011 |
| EV-012 | LG-012 |
| EV-013 | LG-013 |
| EV-014 | LG-014 |
| EV-015 | LG-015 |

For codes beyond EV-015, use the same number: EV-NNN → LG-NNN.

### Why the validator rejects old EV in codes (audit uniqueness)

Using **EV** both for (1) Evidence *artifact* IDs (e.g. `evidence[].id`) and (2) taxonomy *codes* for log/event type caused **concept collision**: the same string `EV-001` could mean an artifact identifier or a taxonomy code. For audit and machine processing, v0.1 enforces:

- **EV-** = Evidence artifact ID only (e.g. `EV-20260115-001`).
- **LG-** = Log/Event Type taxonomy dimension only (e.g. `LG-001`).

The reference validator fails with a clear error if it finds `evidence[].codes.EV` so that all payloads have a single, unambiguous interpretation. This ensures citation and traceability remain consistent.

### Before / After JSON example

**Before (invalid in v0.1):**

```json
{
  "evidence": [
    {
      "id": "EV-20260115-001",
      "codes": {
        "FS": ["FS-001"],
        "EV": ["EV-001", "EV-002"]
      }
    }
  ]
}
```

**After (valid in v0.1):**

```json
{
  "evidence": [
    {
      "id": "EV-20260115-001",
      "codes": {
        "FS": ["FS-001"],
        "LG": ["LG-001", "LG-002"]
      }
    }
  ]
}
```

Only the **codes** object changes: replace the dimension key `"EV"` with `"LG"` and each code `EV-NNN` with `LG-NNN`. The **id** field correctly keeps the **EV-** prefix (artifact ID).

## Overview

### Before (Legacy Structure)

```
source_pack/03_taxonomy/
├── dictionary_seed.csv          # SSOT with _en/_ja columns mixed
├── taxonomy_dictionary_v0.1.csv # Same structure
├── taxonomy_en.yaml             # EN-specific generated file
├── taxonomy_ja.yaml             # JA-specific generated file
└── dimensions_en_ja.md          # Mixed EN/JA table
```

**Problems:**
- Adding a new language requires adding columns to the SSOT CSV
- EN pages contained references to Japanese-specific columns
- Documentation described language-specific columns in all language pages

### After (Language-neutral Structure)

```
data/
└── taxonomy/
    ├── canonical.yaml           # Language-neutral (codes, status, lifecycle)
    └── i18n/
        ├── en.yaml              # English translations
        ├── ja.yaml              # Japanese translations
        └── {lang}.yaml          # Add new languages here

source_pack/03_taxonomy/
├── dictionary_seed.csv          # Legacy compatibility (still generated)
├── taxonomy_dictionary_v0.1.csv # Legacy compatibility
└── ...                          # Legacy files maintained for compatibility
```

**Benefits:**
- Adding a new language = adding one file (`data/taxonomy/i18n/{lang}.yaml`)
- Each documentation page only describes language-neutral concepts
- Clear separation of structure (canonical) vs. content (i18n)

## Migration Steps

### Step 1: Update SSOT CSV (if editing taxonomy)

The canonical SSOT is still `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv`. This file retains `_en` and `_ja` suffixed columns for backward compatibility with existing tooling.

When adding new codes:
1. Edit the SSOT CSV with both EN and JA values
2. Run `python tooling/taxonomy/build_i18n_taxonomy.py` to regenerate i18n packs
3. Run `python tooling/taxonomy/build_taxonomy_assets.py` to regenerate legacy files

### Step 2: Documentation Updates

Documentation pages should describe **language-neutral** column schemas:

**Before (docs/en/...):**
```markdown
| 4 | `dimension_name_en` | Yes | English dimension name |
| 5 | `dimension_name_ja` | Yes | Japanese dimension name |
```

**After (docs/en/...):**
```markdown
| 4 | `dimension_name` | Yes | Dimension name |
```

Add a note pointing to the localization guide:
```markdown
!!! note "Translations"
    Translations are in language packs (`data/taxonomy/i18n/*.yaml`).
```

### Step 3: Adding a New Language

To add a new language (e.g., Spanish):

1. **Generate empty language pack:**
   ```bash
   python tooling/taxonomy/build_i18n_taxonomy.py --add-lang es --lang-name "Español"
   ```

2. **Translate the language pack:**
   Edit `data/taxonomy/i18n/es.yaml` with translations.

3. **Create documentation folder:**
   ```bash
   mkdir -p docs/es
   cp -r docs/en/* docs/es/
   ```

4. **Update mkdocs.yml:**
   ```yaml
   plugins:
     - i18n:
         languages:
           - locale: es
             name: Español
             build: true
   ```

5. **Translate documentation:**
   Translate files in `docs/es/`

### Step 4: Verification

Run all checks to verify migration:

```bash
# i18n quality gates
python tooling/checks/lint_i18n.py

# Taxonomy validation
python tooling/checks/lint_taxonomy_dictionary.py

# Generated assets check
python tooling/taxonomy/build_taxonomy_assets.py --check
python tooling/taxonomy/build_i18n_taxonomy.py --check

# Full build
mkdocs build --strict
```

## Backward Compatibility

### URL Preservation

Existing URLs are preserved:
- `/dev/` → English documentation (unchanged)
- `/dev/ja/` → Japanese documentation (unchanged)

### File Compatibility

Legacy files are still generated and maintained:
- `taxonomy_en.yaml` / `taxonomy_ja.yaml` → Still generated
- `dimensions_en_ja.md` → Still generated
- `taxonomy_dictionary.json` → Still generated

These files are kept for backward compatibility with external tools that may depend on them.

## Allowlist for Mixed-Language Content

Some pages legitimately contain mixed-language content (e.g., translation mapping tables). These are listed in `tooling/checks/lint_i18n.py`:

```python
MIXED_LANGUAGE_ALLOWLIST = [
    "contributing/localization.md",
]
```

To add a new exception, add the relative path (from language directory) to this list.

## Troubleshooting

### CI Fails with "Language-specific content in EN file"

This means an EN page contains Japanese-specific references (like `_ja` column names). Fix by:
1. Removing language-specific column descriptions
2. Using language-neutral terminology
3. Or adding the page to `MIXED_LANGUAGE_ALLOWLIST` if it legitimately needs mixed content

### Missing Translations

If a translation is missing in a language pack, the system falls back to English. This is by design to allow incremental translation.
