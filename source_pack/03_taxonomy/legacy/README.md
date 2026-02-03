# Legacy Taxonomy Files

**Status**: Legacy compatibility files  
**DO NOT ADD NEW LANGUAGE COLUMNS** - see below for rationale

This directory contains legacy English-Japanese mixed CSV files for backward compatibility with existing integrations.

---

## Important Notice

⚠ **These files are maintained for backward compatibility only.**

- **New languages will NOT be added** to these files
- **New integrations should use** `artifacts/taxonomy/{version}/{lang}/taxonomy_dictionary.csv`
- **Column structure is frozen** at 21 columns (no new `label_*` or `definition_*` columns)

## Files

| File | Description | Status |
| --- | --- | --- |
| `taxonomy_dictionary_v0.1.csv` | Master CSV with EN/JA columns (21 columns) | ✅ Frozen |
| `dictionary_seed.csv` | Alias for backward compatibility | ✅ Frozen |

## Column Structure (Frozen)

The following 21 columns will NOT change:

1. `standard_id`
2. `standard_version`
3. `dimension_id`
4. `dimension_name_en`
5. `dimension_name_ja`
6. `code`
7. `label_en`
8. `label_ja`
9. `definition_en`
10. `definition_ja`
11. `scope_notes`
12. `examples`
13. `status`
14. `introduced_in`
15. `deprecated_in`
16. `removed_in`
17. `replaced_by`
18. `backward_compatible`
19. `references`
20. `owner`
21. `last_reviewed_date`

## Why No New Language Columns?

Adding `label_es`, `definition_es`, `label_de`, `definition_de`, etc. would cause:

1. **Column explosion**: Each new language adds 2+ columns
2. **Maintenance burden**: All downstream tools must update parsers
3. **Schema instability**: Breaking changes for every language addition

## Alternative: Per-Language Artifacts

For new languages, use the per-language CSV files:

```
artifacts/taxonomy/{version}/{lang}/taxonomy_dictionary.csv
```

Each file contains only the specified language with a stable column structure.

## SSOT Location

The Single Source of Truth for taxonomy is:

| Type | Location |
| --- | --- |
| Structure | `data/taxonomy/canonical.yaml` |
| Translations | `data/taxonomy/i18n/{lang}.yaml` |

These legacy files are **generated** from the SSOT for backward compatibility.

## CI Enforcement

The following checks prevent accidental column addition:

```bash
# Fails if legacy CSV contains new language suffix columns
python tooling/checks/lint_legacy_csv.py
```

---

## Deprecation Timeline

| Version | Status |
| --- | --- |
| 0.1.x | Legacy files maintained |
| 1.0.0 | Legacy files deprecated (warning in CI) |
| 2.0.0 | Legacy files may be removed |

New integrations should migrate to per-language artifacts before 1.0.0.
