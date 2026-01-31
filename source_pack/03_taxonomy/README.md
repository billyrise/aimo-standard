# Taxonomy (Authoring SSOT)

**Status**: Authoring input — Single Source of Truth (SSOT)  
**Canonical language**: English (EN)  
**Last updated**: CU-TAX-01 (2026-01-31)

This directory contains the taxonomy definitions for the AIMO Standard. The taxonomy provides dimensions, codes, and dictionary entries for evidence categorization.

---

## SSOT Declaration

This directory is the **Single Source of Truth (SSOT)** for:

- **Taxonomy** — 8 dimensions for classifying AI use cases and evidence
- **Code System** — Dimension namespaces and code format (PREFIX-###)
- **Dictionary** — 91 defined codes with EN/JA labels and definitions

All other representations in `docs/`, `schemas/`, `templates/`, and `examples/` are **derived** from the files in this directory.

---

## Directory Contents

| File | Purpose | Status |
| --- | --- | --- |
| `taxonomy_dictionary_v0.1.csv` | SSOT: 91 codes across 8 dimensions (21 columns) | ✅ Complete |
| `dictionary_seed.csv` | Identical copy for legacy/API compatibility | ✅ Complete |
| `taxonomy_en.yaml` | Generated English taxonomy (dimensions + codes) | ✅ Generated |
| `taxonomy_ja.yaml` | Generated Japanese taxonomy (dimensions + codes) | ✅ Generated |
| `code_system.csv` | Generated dimension namespaces and prefixes | ✅ Generated |
| `dimensions_en_ja.md` | Generated dimension names EN/JA mapping | ✅ Generated |
| `taxonomy_pack_v0.1.json` | Taxonomy pack for programmatic access | ✅ Complete |
| `schemas/` | JSON schemas for validation | ✅ Complete |

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

### Step 1: Edit the SSOT CSV (English canonical)

Edit `taxonomy_dictionary_v0.1.csv` first. English definitions are canonical.

### Step 2: Sync legacy file

Ensure `dictionary_seed.csv` is identical to `taxonomy_dictionary_v0.1.csv`:

```bash
cp source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv source_pack/03_taxonomy/dictionary_seed.csv
```

### Step 3: Validate the CSV

```bash
python tooling/checks/lint_taxonomy_dictionary.py
```

### Step 4: Regenerate derived files

```bash
python tooling/taxonomy/build_taxonomy_assets.py
```

This regenerates:
- `taxonomy_en.yaml`
- `taxonomy_ja.yaml`
- `code_system.csv`
- `dimensions_en_ja.md`

### Step 5: Update manifest

Update `source_pack/00_manifest.md` with the CU changes.

### Step 6: Commit together

Commit the SSOT CSV and regenerated files together.

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
