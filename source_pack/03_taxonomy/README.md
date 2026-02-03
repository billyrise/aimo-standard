# Taxonomy (Derived Assets)

**Status**: Derived/generated files  
**SSOT Location**: `data/taxonomy/` (canonical.yaml + i18n/*.yaml)  
**Last updated**: CU-TAX-02 (2026-01-31)

This directory contains derived taxonomy assets for the AIMO Standard.

---

## SSOT Declaration (IMPORTANT)

⚠ **The SSOT has moved to `data/taxonomy/`**

| Type | SSOT Location | Purpose |
| --- | --- | --- |
| Structure | `data/taxonomy/canonical.yaml` | Codes, status, lifecycle (language-neutral) |
| English | `data/taxonomy/i18n/en.yaml` | English labels and definitions |
| Japanese | `data/taxonomy/i18n/ja.yaml` | Japanese labels and definitions |
| Other | `data/taxonomy/i18n/{lang}.yaml` | Additional language translations |

Files in this directory are **generated** from the SSOT. Do not edit directly.

---

## Directory Contents

| File/Dir | Purpose | Status |
| --- | --- | --- |
| `legacy/` | Legacy EN/JA mixed CSV (backward compatibility) | ✅ Frozen |
| `taxonomy_dictionary.json` | Generated: JSON format for schema validation | ✅ Generated |
| `taxonomy_en.yaml` | Generated: English taxonomy (dimensions + codes) | ✅ Generated |
| `taxonomy_ja.yaml` | Generated: Japanese taxonomy (dimensions + codes) | ✅ Generated |
| `code_system.csv` | Generated: Dimension namespaces and prefixes | ✅ Generated |
| `dimensions_en_ja.md` | Generated: Dimension names EN/JA mapping | ✅ Generated |
| `taxonomy_pack_v0.1.json` | Taxonomy pack for programmatic access | ✅ Complete |
| `schemas/` | JSON schemas for validation | ✅ Complete |

### Legacy Files (Frozen)

The `legacy/` directory contains:

- `taxonomy_dictionary_v0.1.csv` — EN/JA mixed CSV (21 columns, **no new language columns**)
- `dictionary_seed.csv` — Compatibility alias

**Warning**: Legacy files are frozen. New languages are NOT added to these files. Use `artifacts/taxonomy/{version}/{lang}/` for per-language CSVs.

---

## 8 Dimensions

| ID | Name (EN) | Name (JA) | Code Count | Purpose |
| --- | --- | --- | --- | --- |
| **FS** | Functional Scope | 機能スコープ | 6 | What function is AI supporting? |
| **UC** | Use Case Class | ユースケース分類 | 30 | What type of task is being performed? |
| **DT** | Data Type | データ種別 | 10 | What data classifications are involved? |
| **CH** | Channel | チャネル | 8 | How do users interact with the AI? |
| **IM** | Integration Mode | 統合形態 | 7 | How is AI integrated into systems? |
| **RS** | Risk Surface | リスク面 | 8 | What risk categories apply? |
| **OB** | Outcome / Benefit | 成果 | 7 | What outcomes are expected? |
| **EV** | Evidence Type | 証跡種別 | 15 | What evidence is required? |

**Total**: 91 codes across 8 dimensions

---

## CSV Column Specification (21 columns)

The SSOT CSV (`taxonomy_dictionary_v0.1.csv` and `dictionary_seed.csv`) uses the following columns:

| # | Column | Required | Description |
| --- | --- | --- | --- |
| 1 | `standard_id` | Yes | Always "AIMO-STD" |
| 2 | `standard_version` | Yes | SemVer (e.g., "0.1.0") |
| 3 | `dimension_id` | Yes | One of: FS, UC, DT, CH, IM, RS, OB, EV |
| 4 | `dimension_name_en` | Yes | English dimension name |
| 5 | `dimension_name_ja` | Yes | Japanese dimension name |
| 6 | `code` | Yes | Unique code (PREFIX-###) |
| 7 | `label_en` | Yes | English label |
| 8 | `label_ja` | Yes | Japanese label |
| 9 | `definition_en` | Yes | English definition |
| 10 | `definition_ja` | Yes | Japanese definition |
| 11 | `scope_notes` | No | Usage/scope notes |
| 12 | `examples` | No | Pipe-separated examples |
| 13 | `status` | Yes | active, deprecated, or removed |
| 14 | `introduced_in` | Yes | Version introduced |
| 15 | `deprecated_in` | No | Version deprecated (if applicable) |
| 16 | `removed_in` | No | Version removed (if applicable) |
| 17 | `replaced_by` | No | Replacement code (if deprecated) |
| 18 | `backward_compatible` | Yes | true/false |
| 19 | `references` | No | External references |
| 20 | `owner` | No | Working group owner |
| 21 | `last_reviewed_date` | No | ISO date of last review |

---

## Update Workflow

### New SSOT-First Workflow

1. **Edit the SSOT** in `data/taxonomy/`:
   - Structure changes → `canonical.yaml`
   - English translations → `i18n/en.yaml`
   - Japanese translations → `i18n/ja.yaml`

2. **Validate SSOT**:
   ```bash
   python tooling/checks/lint_taxonomy_ssot.py
   ```

3. **Regenerate all derived files**:
   ```bash
   python tooling/taxonomy/build_artifacts.py --version current --langs en ja
   ```

4. **Update manifest** (`source_pack/00_manifest.md`)

5. **Commit together**

### Adding a New Language

1. Create i18n pack:
   ```bash
   python tooling/taxonomy/build_i18n_taxonomy.py --add-lang es --lang-name "Español"
   ```

2. Translate `data/taxonomy/i18n/es.yaml`

3. Regenerate artifacts:
   ```bash
   python tooling/taxonomy/build_artifacts.py --version current --langs en ja es
   ```

**Note**: Legacy CSV files are NOT updated. New languages are only available via `artifacts/taxonomy/`.

---

## Compatibility Policy

### ID Stability

- **Code IDs are immutable** — once assigned, a code ID never changes
- Use `deprecated` status instead of removing codes
- Provide `replaced_by` for deprecated codes

### Deprecation Flow

1. Set `status` to `deprecated`
2. Set `deprecated_in` to current version
3. Set `replaced_by` to the new code (if applicable)
4. Code remains functional for backward compatibility

### Removal (major version only)

1. Set `status` to `removed`
2. Set `removed_in` to current major version
3. Code is no longer valid for new evidence

---

## CI Quality Gates

The following checks run in CI:

```bash
# Validate CSV structure and uniqueness
python tooling/checks/lint_taxonomy_dictionary.py

# Validate derived files match SSOT
python tooling/taxonomy/build_taxonomy_assets.py --check
```

---

## Related Files

| Location | Description |
| --- | --- |
| `docs/standard/current/03-taxonomy.md` | User-facing taxonomy documentation |
| `docs/standard/current/04-codes.md` | Code format and usage documentation |
| `docs/standard/current/05-dictionary.md` | Dictionary documentation |
| `schemas/jsonschema/aimo-dictionary.schema.json` | JSON Schema for dictionary |
| `tooling/taxonomy/build_taxonomy_assets.py` | Asset generation script |
| `tooling/checks/lint_taxonomy_dictionary.py` | CSV validation script |

---

## Authoring Notes

- **English is canonical**: Edit EN definitions first, then JA follows
- **Do NOT edit generated files**: Files marked "Generated" are overwritten by the build script
- **Use stable IDs**: Code IDs must follow PREFIX-### format
- **Version tracking**: All codes have `introduced_in` for traceability
- **Non-overclaim**: Taxonomy is a classification system, not a compliance guarantee
