# Taxonomy

The AIMO Taxonomy provides a structured framework for categorizing AI systems, their uses, and associated governance requirements. It consists of **8 dimensions** that together enable consistent classification and evidence management across organizations.

## Purpose and Audit Context

The taxonomy serves two primary purposes from an audit perspective:

1. **Evidence Readiness**: Enables systematic documentation of AI systems using a standardized classification, making evidence collection and review more efficient.

2. **Explainability**: Provides a common vocabulary for describing AI use cases across the organization, supporting clear communication with auditors and stakeholders.

!!! warning "Non-Overclaim"
    The AIMO Standard supports **explainability and evidence readiness**. It does **not** provide legal advice, guarantee compliance, or certify conformity to any regulation or framework. See [Responsibility Boundary](../../governance/responsibility-boundary.md) for details.

## Single Source of Truth (SSOT)

The authoritative definition of the taxonomy is maintained in machine-readable files:

| File | Description |
| --- | --- |
| `taxonomy_dictionary_v0.1.csv` | SSOT for all codes (91 codes across 8 dimensions) |
| `taxonomy_en.yaml` | English taxonomy (generated from CSV) |
| `taxonomy_ja.yaml` | Japanese taxonomy (generated from CSV) |

**This documentation page is explanatory.** For authoritative definitions, always reference the SSOT files in `source_pack/03_taxonomy/`.

## Code System Overview

AIMO uses a code system with the format `<DIM>-<TOKEN>`, where:

- `<DIM>`: Two-letter dimension identifier (e.g., FS, UC, DT)
- `<TOKEN>`: Three-digit numeric token (e.g., 001, 002, 003)

**Examples:**

- `UC-001`: General Q&A (Use Case Class)
- `DT-004`: Personal Data (Data Type)
- `CH-003`: IDE Plugin (Channel)
- `IM-002`: SaaS Integrated (Integration Mode)

## The 8 Dimensions

| Priority | ID | Name (EN) | Name (JA) | Required | Multi-select | What it distinguishes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **FS** | Functional Scope | 機能スコープ | Yes | No | Which business function is supported |
| 2 | **UC** | Use Case Class | ユースケース分類 | Yes | Yes | What type of task is performed |
| 3 | **DT** | Data Type | データ種別 | Yes | Yes | What data sensitivity is involved |
| 4 | **CH** | Channel | チャネル | Yes | Yes | How users access the AI |
| 5 | **IM** | Integration Mode | 統合形態 | Yes | No | How AI connects to enterprise systems |
| 6 | **RS** | Risk Surface | リスク面 | Yes | Yes | What risks are associated |
| 7 | **OB** | Outcome / Benefit | 成果 | No | Yes | What benefits are expected |
| 8 | **EV** | Evidence Type | 証跡種別 | Yes | Yes | What evidence is required |

### Usage Rules Summary

| Dimension | Selection | Audit Implication |
| --- | --- | --- |
| FS, IM | Exactly 1 | Primary classification for responsibility assignment |
| UC, DT, CH, RS, EV | 1 or more | Complete enumeration required for risk coverage |
| OB | 0 or more | Optional; documents expected business value |

## Dimension Definitions

### FS: Functional Scope / 機能スコープ

Categorizes AI use by the business function it supports. **Select exactly one.**

| Code | Label (EN) | Label (JA) | Description |
| --- | --- | --- | --- |
| FS-001 | End-user Productivity | 社内生産性 | AI for internal productivity (writing, search, summarization) |
| FS-002 | Customer-facing Features | 顧客向け機能 | AI in customer-facing products/services |
| FS-003 | Developer Tooling | 開発支援 | AI for software development |
| FS-004 | IT Operations | IT運用 | AI for IT ops and system administration |
| FS-005 | Security Operations | セキュリティ運用 | AI for security monitoring/response |
| FS-006 | Governance & Compliance | ガバナンス/コンプライアンス | AI for governance/compliance activities |

### UC: Use Case Class / ユースケース分類

Categorizes AI use by the type of task or interaction. **Select one or more.** Full list includes 30 codes; representative examples below.

| Code | Label (EN) | Label (JA) | Description |
| --- | --- | --- | --- |
| UC-001 | General Q&A | 一般QA | General question answering |
| UC-002 | Summarization | 要約 | Summarizing documents/meetings |
| UC-003 | Translation | 翻訳 | Translation between languages |
| UC-004 | Content Drafting | 文章作成 | Generating drafts for documents |
| UC-005 | Code Generation | コード生成 | Generating code or scripts |
| UC-010 | Agentic Automation | エージェント自動化 | Autonomous agents executing actions |

See [Dictionary](./05-dictionary.md) for the complete list of 30 UC codes.

### DT: Data Type / データ種別

Categorizes the sensitivity and classification of data involved. **Select one or more.**

| Code | Label (EN) | Label (JA) | Description |
| --- | --- | --- | --- |
| DT-001 | Public | 公開情報 | Publicly available data |
| DT-002 | Internal | 社内情報 | Non-public internal business data |
| DT-003 | Confidential | 機密情報 | Highly sensitive data with restricted access |
| DT-004 | Personal Data | 個人情報 | Personal data per privacy laws |
| DT-005 | Sensitive Personal Data | 要配慮個人情報 | Special category personal data |
| DT-006 | Credentials | 認証情報 | Authentication secrets and credentials |
| DT-007 | Source Code | ソースコード | Source code and related artifacts |
| DT-008 | Customer Data | 顧客データ | Customer-provided or customer-related data |
| DT-009 | Operational Logs | 運用ログ | System operational logs |
| DT-010 | Security Telemetry | セキュリティテレメトリ | Security monitoring data |

### CH: Channel / チャネル

Categorizes how users access or interact with the AI. **Select one or more.**

| Code | Label (EN) | Label (JA) | Description |
| --- | --- | --- | --- |
| CH-001 | Web UI | Web UI | Via web user interface |
| CH-002 | API | API | Via programmatic API integration |
| CH-003 | IDE Plugin | IDEプラグイン | Via IDE/editor plugin |
| CH-004 | ChatOps | チャット連携 | Via Slack/Teams integrations |
| CH-005 | Desktop App | デスクトップアプリ | Via native desktop application |
| CH-006 | Mobile App | モバイルアプリ | Via native mobile application |
| CH-007 | Embedded Widget | 埋め込みウィジェット | Embedded in other applications |
| CH-008 | Batch/CLI | バッチ/CLI | Via command-line or batch processing |

### IM: Integration Mode / 統合形態

Categorizes how AI is integrated into enterprise systems. **Select exactly one.**

| Code | Label (EN) | Label (JA) | Description |
| --- | --- | --- | --- |
| IM-001 | Standalone | 単体利用 | Used standalone without enterprise integration |
| IM-002 | SaaS Integrated | SaaS連携 | SaaS application with AI features |
| IM-003 | Enterprise App Embedded | 社内アプリ組込み | AI embedded in internal applications |
| IM-004 | RPA/Workflow | ワークフロー/RPA | AI invoked within workflow automation |
| IM-005 | On-prem / Private | オンプレ/プライベート | AI in private/on-prem environment |
| IM-006 | Hybrid Cloud | ハイブリッドクラウド | Combination of cloud and on-prem |
| IM-007 | Multi-tenant SaaS | マルチテナントSaaS | Shared SaaS infrastructure |

### RS: Risk Surface / リスク面

Categorizes the types of risks associated with the AI use. **Select one or more.**

| Code | Label (EN) | Label (JA) | Description |
| --- | --- | --- | --- |
| RS-001 | Data Leakage | 情報漏えい | Risk of unintended data disclosure |
| RS-002 | Security Abuse | 悪用/攻撃 | Risk of system abuse for malicious purposes |
| RS-003 | Compliance Breach | 法令/規程違反 | Risk of violating laws/regulations/policies |
| RS-004 | IP Infringement | 知財侵害 | Risk of copyright/patent/trade secret infringement |
| RS-005 | Model Misuse | モデル誤用 | Risk from inappropriate model use or over-reliance |
| RS-006 | Bias/Fairness | バイアス/公平性 | Risk of discriminatory outputs |
| RS-007 | Availability | 可用性 | Risk of service disruption |
| RS-008 | Supply Chain | サプライチェーン | Risk from third-party dependencies |

### OB: Outcome / Benefit / 成果

Categorizes the expected outcomes or benefits from AI use. **Optional; select zero or more.**

| Code | Label (EN) | Label (JA) | Description |
| --- | --- | --- | --- |
| OB-001 | Efficiency | 効率化 | Improves time/cost efficiency |
| OB-002 | Quality | 品質向上 | Improves quality/accuracy of outputs |
| OB-003 | Revenue | 売上貢献 | Contributes to revenue growth |
| OB-004 | Risk Reduction | リスク低減 | Reduces operational/security/compliance risk |
| OB-005 | Innovation | 新規性/革新 | Enables new capabilities or innovations |
| OB-006 | Customer Satisfaction | 顧客満足度 | Improves customer experience |
| OB-007 | Employee Experience | 従業員体験 | Improves employee productivity/satisfaction |

### EV: Evidence Type / 証跡種別

Categorizes the types of evidence required or collected. **Select one or more.** The following are **MVP required** evidence types (EV-001 to EV-007):

| Code | Label (EN) | Label (JA) | Description |
| --- | --- | --- | --- |
| EV-001 | System Overview | システム概要 | Overview of the AI system |
| EV-002 | Data Flow | データフロー | Data flow diagram and description |
| EV-003 | Inventory | AI資産台帳 | Inventory of AI systems/models |
| EV-004 | Risk & Impact Assessment | リスク影響評価 | Risk and impact assessment |
| EV-005 | Controls & Approvals | 統制/承認 | Control measures and approvals |
| EV-006 | Logging & Monitoring | ログ監視 | Logging and monitoring configuration |
| EV-007 | Incident & Exception | インシデント/例外 | Incident and exception handling |

Additional evidence types (EV-008 to EV-015) are available for extended documentation. See [Dictionary](./05-dictionary.md) for the complete list.

## SSOT References

| Resource | Path | Description |
| --- | --- | --- |
| Dictionary CSV | `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv` | All 91 codes with full metadata |
| Taxonomy YAML (EN) | `source_pack/03_taxonomy/taxonomy_en.yaml` | Generated English taxonomy |
| Taxonomy YAML (JA) | `source_pack/03_taxonomy/taxonomy_ja.yaml` | Generated Japanese taxonomy |
| Taxonomy Pack Schema | `source_pack/03_taxonomy/schemas/taxonomy_pack.schema.json` | JSON Schema for validation |

## Downloads

Download the complete taxonomy package from the [Releases](../../releases/index.md) page.

## Related Pages

- [Codes](./04-codes.md) - Code format, naming conventions, and lifecycle
- [Dictionary](./05-dictionary.md) - Complete code listings and column definitions
- [Evidence Templates](./06-ev-template.md) - MVP evidence templates
- [Responsibility Boundary](../../governance/responsibility-boundary.md) - Non-overclaim statement
