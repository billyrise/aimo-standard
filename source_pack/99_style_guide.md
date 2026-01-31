# Style Guide (Authoring SSOT)

**Status**: Authoring input — not user-facing documentation  
**Canonical language**: English (EN)

This document defines terminology, translation rules, and style conventions for AIMO Standard documentation.

---

## 1. Canonical Terminology Glossary (EN → JA)

### Core Concepts

| EN Term | JA Term | Definition | Source |
| --- | --- | --- | --- |
| AIMO Standard | AIMO Standard / AIMOスタンダード | The overall specification and artifacts | — |
| Trust Package | トラストパッケージ | Auditor-ready materials bundle | `governance/trust-package` |
| Evidence Bundle | エビデンスバンドル | Structured set of audit artifacts | `artifacts/evidence-bundle` |
| Evidence (EV) | エビデンス / 証跡 | Individual evidence record | `artifacts/evidence-bundle` |
| Dictionary | 辞書 | Key/label/description mapping | `standard/current/05-dictionary` |
| Taxonomy | タクソノミー | Dimension and code classification | `standard/current/03-taxonomy` |
| Validator | バリデータ | Structural consistency checker | `validator/index` |
| Coverage Map | カバレッジマップ | External framework mapping | `coverage-map/index` |

### Governance Terms

| EN Term | JA Term | Definition | Source |
| --- | --- | --- | --- |
| Responsibility Boundary | 責任境界 | Scope of what AIMO provides/doesn't | `governance/responsibility-boundary` |
| Non-overclaim statement | 非過大主張声明 | Disclaimer about limitations | `governance/responsibility-boundary` |
| Conformance | 適合性 | Compliance with standard | `conformance/index` |
| Minimum Evidence Requirements | 最低限のエビデンス要件 | MUST-level checklist | `artifacts/minimum-evidence` |

### Lifecycle Terms

| EN Term | JA Term | Definition |
| --- | --- | --- |
| Request | 申請 | Application/request for AI use |
| Review / Approval | 審査 / 承認 | Review and approval process |
| Exception | 例外 | Deviation with compensating controls |
| Renewal / Re-evaluation | 更新 / 再評価 | Periodic re-assessment |
| Change Log | 変更管理 / 変更ログ | Audit trail of changes |
| Integrity & Access | 完全性 / アクセス制御 | Evidence protection controls |

### Technical Terms

| EN Term | JA Term | Notes |
| --- | --- | --- |
| Schema | スキーマ | Keep as katakana |
| JSON | JSON | Keep as acronym |
| SHA-256 | SHA-256 | Keep as-is |
| Checksum | チェックサム | Keep as katakana |
| WORM storage | WORMストレージ | Keep acronym |

---

## 2. Translation Priority Rules

### Rule 0: Language Separation (EN/JA Purity)

**English canonical pages (`.md`) must be English-only.** Localization happens in per-locale pages (`.ja.md`, etc.).

**Prohibited in EN pages:**

- Japanese columns in tables (e.g., `Label (JA)`, `Name (JA)`)
- Japanese text in parentheses (e.g., `(日本語: …)`)
- Dual-language headings (e.g., `### FS: Functional Scope / 機能スコープ`)
- Any hiragana, katakana, or kanji characters in prose

**Allowed in EN pages:**

- References to JA file paths (e.g., `taxonomy_ja.yaml`)
- CSV column names that describe JA content (e.g., `label_ja`, `dimension_name_ja`)
- SSOT CSV files may contain both EN and JA data; docs reference the CSV, not embed the values

**Allowed in JA pages:**

- English terms in parentheses (e.g., `機能スコープ (Functional Scope)`)
- Technical terms kept in English (JSON, API, AIMO, etc.)

**CI Enforcement:**

The `lint_lang_purity.py` check (if enabled) validates that EN pages (`docs/**/*.md` excluding `*.ja.md`) contain no Japanese characters outside code blocks.

### Rule 1: English is Canonical

All normative statements are authored in English first. Japanese translations are derivative.

### Rule 2: Heading Parity

EN and JA files must have matching heading levels. This is enforced by `lint_i18n.py`.

**Example**:
```markdown
# EN: Evidence Bundle          →  # JA: エビデンスバンドル
## Bundle structure            →  ## バンドル構造
### Required fields            →  ### 必須フィールド
```

### Rule 3: Technical Terms

- **Established technical terms**: Use katakana (エビデンス, バリデータ, スキーマ)
- **Acronyms**: Keep in English (EV, JSON, AIMO, SHA-256)
- **Process terms**: Use native Japanese (申請, 審査, 承認)

### Rule 4: MUST/SHOULD Keywords

| Option | EN | JA | When to use |
| --- | --- | --- | --- |
| A | MUST | 必須 / しなければならない | Formal specifications |
| B | MUST | MUST（必須） | When EN keyword visibility needed |

### Rule 5: Admonitions

Preserve admonition types in translation:

| EN | JA |
| --- | --- |
| `!!! warning` | `!!! warning "警告"` |
| `!!! info` | `!!! info "情報"` |
| `!!! note` | `!!! note "注記"` |
| `!!! tip` | `!!! tip "ヒント"` |

---

## 3. Prohibited Language (Overclaim Phrases)

The following phrases are prohibited to avoid overclaiming:

| Prohibited phrase | Why problematic | Alternative |
| --- | --- | --- |
| "guarantees compliance" | AIMO doesn't guarantee | "supports compliance efforts" |
| "certifies conformity" | AIMO doesn't certify | "helps demonstrate alignment" |
| "provides legal advice" | AIMO is not legal counsel | "supports evidence documentation" |
| "ensures security" | AIMO doesn't implement controls | "documents security expectations" |
| "compliant with [regulation]" | Implies certification | "supports explainability for [regulation]" |
| "fully covers [framework]" | Overstates mapping | "provides informative mapping to [framework]" |
| "audit-proof" | Overstates readiness | "audit-ready" |
| "legally binding" | Overreaches scope | Remove or qualify |

### Canonical Non-Overclaim Statement

Always reference the canonical statement from `docs/governance/responsibility-boundary.md`:

> **Important**: The AIMO Standard supports **explainability and evidence readiness**. It does **not** provide legal advice, guarantee compliance, or certify conformity to any regulation or framework. Adopters must verify claims against authoritative texts and obtain professional advice as appropriate.

---

## 4. Tone and Style Rules

### Auditor/Legal Safe Tone

| Do | Don't |
| --- | --- |
| Use precise, factual language | Use marketing language |
| Qualify claims appropriately | Make absolute claims |
| Reference authoritative sources | Assert authority |
| Use passive voice for objectivity | Use first person (we, our) |

### Examples

| Bad | Good |
| --- | --- |
| "AIMO ensures you're compliant" | "AIMO supports evidence documentation" |
| "Our validator guarantees correctness" | "The validator checks structural consistency" |
| "This covers all requirements" | "This provides informative mapping" |

### Formatting Conventions

| Element | Convention |
| --- | --- |
| File paths | Backticks: \`schemas/jsonschema/\` |
| Code | Fenced code blocks with language |
| Tables | Use tables for structured data |
| Admonitions | MkDocs admonition syntax |
| Links | Relative links within docs |

---

## 5. Document Structure

### Standard Page Structure

```markdown
# Page Title

Introduction paragraph.

## Section 1

Content.

## Section 2

Content.

## Related Pages

- [Link 1](path.md)
- [Link 2](path.md)
```

### Authoring SSOT Page Structure

```markdown
# Topic (Authoring SSOT)

**Status**: Authoring input — not user-facing documentation  
**Canonical language**: English (EN)

Introduction.

---

## Section 1

Content.

---

## Authoring Notes

- Notes for authors.
```

---

## 6. Review Checklist

Before publishing:

- [ ] English version complete and accurate
- [ ] Japanese translation matches heading structure
- [ ] No prohibited overclaim phrases
- [ ] Technical terms use correct glossary entries
- [ ] Links are relative and working
- [ ] Admonitions use correct syntax
- [ ] i18n lint passes

---

## Authoring Notes

- This guide is the SSOT for terminology and style.
- All new terms should be added to the glossary.
- Prohibited phrases should be reviewed in all new content.
