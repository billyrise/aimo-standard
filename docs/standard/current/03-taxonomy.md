# Taxonomy

The AIMO Taxonomy provides a structured classification system for categorizing AI systems, their uses, and associated governance requirements. It consists of **8 dimensions** with **91 codes** that enable consistent classification and evidence management across organizations.

## Purpose

The taxonomy serves three primary purposes from an audit perspective:

1. **Explainability**: Provides a common vocabulary for describing AI use cases across the organization, supporting clear communication with auditors and stakeholders.

2. **Evidence Readiness**: Enables systematic documentation of AI systems using a standardized classification, making evidence collection and review more efficient.

3. **Comparability**: Allows organizations to compare AI use cases across different contexts using consistent terminology.

## What It Is Not (Non-Overclaim)

!!! warning "Important"
    The AIMO Standard supports **explainability and evidence readiness**. It does **not** provide legal advice, guarantee compliance, or certify conformity to any regulation or framework. See [Responsibility Boundary](../../governance/responsibility-boundary.md) for details.

The taxonomy is a classification system only. It does not:

- Guarantee compliance with any law or regulation
- Replace professional legal, security, or compliance advice
- Certify conformity to external frameworks (ISO, NIST, EU AI Act, etc.)
- Provide risk assessments or control recommendations

## Dimensions Overview

AIMO uses 8 dimensions to classify AI use cases. Each dimension has a unique 2-letter prefix.

| ID | Name (EN) | Name (JA) | Code Count | Description |
| --- | --- | --- | --- | --- |
| **FS** | Functional Scope | 機能スコープ | 6 | Which business function is supported |
| **UC** | Use Case Class | ユースケース分類 | 30 | What type of task is performed |
| **DT** | Data Type | データ種別 | 10 | What data classifications are involved |
| **CH** | Channel | チャネル | 8 | How users access the AI |
| **IM** | Integration Mode | 統合形態 | 7 | How AI connects to enterprise systems |
| **RS** | Risk Surface | リスク面 | 8 | What risks are associated |
| **OB** | Outcome / Benefit | 成果 | 7 | What benefits are expected |
| **EV** | Evidence Type | 証跡種別 | 15 | What evidence is required |

**Total: 91 codes across 8 dimensions**

### Usage Rules

| Dimension | Selection | Audit Implication |
| --- | --- | --- |
| FS, IM | Exactly 1 | Primary classification for responsibility assignment |
| UC, DT, CH, RS, EV | 1 or more | Complete enumeration required for risk coverage |
| OB | 0 or more | Optional; documents expected business value |

## Dimension Definitions

### FS: Functional Scope / 機能スコープ

Categorizes AI use by the business function it supports. **Select exactly one.**

| Code | Label (EN) | Label (JA) | Definition |
| --- | --- | --- | --- |
| FS-001 | End-user Productivity | 社内生産性 | AI used to improve productivity of internal end users (writing, search, summarization, meeting notes). |
| FS-002 | Customer-facing Features | 顧客向け機能 | AI embedded in product/service features provided to customers. |
| FS-003 | Developer Tooling | 開発支援 | AI used to assist software development and engineering tasks. |
| FS-004 | IT Operations | IT運用 | AI used for IT operations and system administration (monitoring, incident handling). |
| FS-005 | Security Operations | セキュリティ運用 | AI used for security monitoring/response (SOC, detection, triage). |
| FS-006 | Governance & Compliance | ガバナンス/コンプライアンス | AI used to support governance/compliance activities (policy, audit evidence). |

### UC: Use Case Class / ユースケース分類

Categorizes AI use by the type of task or interaction. **Select one or more.** Full list includes 30 codes; representative examples below.

| Code | Label (EN) | Label (JA) | Definition |
| --- | --- | --- | --- |
| UC-001 | General Q&A | 一般QA | General question answering and conversational use. |
| UC-002 | Summarization | 要約 | Summarizing documents, meetings, or messages. |
| UC-003 | Translation | 翻訳 | Translation between languages. |
| UC-004 | Content Drafting | 文章作成 | Generating drafts for emails, documents, or reports. |
| UC-005 | Code Generation | コード生成 | Generating code or scripts. |
| UC-006 | Code Review | コードレビュー | Reviewing code for issues and improvements. |
| UC-009 | Search/RAG | 検索/RAG | RAG-based retrieval and question answering. |
| UC-010 | Agentic Automation | エージェント自動化 | Autonomous or semi-autonomous agents executing actions. |

See [Dictionary](./05-dictionary.md) for the complete list of 30 UC codes.

### DT: Data Type / データ種別

Categorizes the sensitivity and classification of data involved. **Select one or more.**

| Code | Label (EN) | Label (JA) | Definition |
| --- | --- | --- | --- |
| DT-001 | Public | 公開情報 | Data that is publicly available and intended for public disclosure. |
| DT-002 | Internal | 社内情報 | Non-public internal business data. |
| DT-003 | Confidential | 機密情報 | Highly sensitive internal data requiring restricted access. |
| DT-004 | Personal Data | 個人情報 | Personal data as defined by applicable privacy laws. |
| DT-005 | Sensitive Personal Data | 要配慮個人情報 | Special category/sensitive personal data. |
| DT-006 | Credentials | 認証情報 | Authentication secrets and credentials. |
| DT-007 | Source Code | ソースコード | Source code and related artifacts. |
| DT-008 | Customer Data | 顧客データ | Customer-provided or customer-related data. |
| DT-009 | Operational Logs | 運用ログ | Operational or system logs used for monitoring and troubleshooting. |
| DT-010 | Security Telemetry | セキュリティテレメトリ | Security telemetry such as alerts and detections. |

### CH: Channel / チャネル

Categorizes how users access or interact with the AI. **Select one or more.**

| Code | Label (EN) | Label (JA) | Definition |
| --- | --- | --- | --- |
| CH-001 | Web UI | Web UI | Use via a web user interface. |
| CH-002 | API | API | Use via programmatic API integration. |
| CH-003 | IDE Plugin | IDEプラグイン | Use via IDE/editor plugin. |
| CH-004 | ChatOps | チャット連携 | Use via chat platforms (Slack/Teams) integrations. |
| CH-005 | Desktop App | デスクトップアプリ | Use via native desktop application. |
| CH-006 | Mobile App | モバイルアプリ | Use via native mobile application. |
| CH-007 | Email | メール | Use via email interface or email-based automation. |
| CH-008 | Command Line | CLI | Use via command-line interface. |

### IM: Integration Mode / 統合形態

Categorizes how AI is integrated into enterprise systems. **Select exactly one.**

| Code | Label (EN) | Label (JA) | Definition |
| --- | --- | --- | --- |
| IM-001 | Standalone | 単体利用 | Used standalone without integration into enterprise systems. |
| IM-002 | SaaS Integrated | SaaS連携 | SaaS application integrates AI features. |
| IM-003 | Enterprise App Embedded | 社内アプリ組込み | AI embedded into internal enterprise applications. |
| IM-004 | RPA/Workflow | ワークフロー/RPA | AI invoked within workflow automation or RPA. |
| IM-005 | On-prem / Private | オンプレ/プライベート | AI hosted in private/on-prem environment. |
| IM-006 | Managed Service | マネージド | Use via managed service with enterprise controls. |
| IM-007 | Shadow / Unmanaged | シャドー/未管理 | Use outside of approved governance controls. |

### RS: Risk Surface / リスク面

Categorizes the types of risks associated with the AI use. **Select one or more.**

| Code | Label (EN) | Label (JA) | Definition |
| --- | --- | --- | --- |
| RS-001 | Data Leakage | 情報漏えい | Risk of unintended data disclosure. |
| RS-002 | Security Abuse | 悪用/攻撃 | Risk that the system is abused for malicious purposes. |
| RS-003 | Compliance Breach | 法令/規程違反 | Risk of violating laws/regulations/policies. |
| RS-004 | IP Infringement | 知財侵害 | Risk of infringing copyright/patent/trade secrets. |
| RS-005 | Model Misuse | モデル誤用 | Risk from inappropriate model use or over-reliance. |
| RS-006 | Bias/Fairness | 偏り/公平性 | Risk of unfair or biased outcomes. |
| RS-007 | Safety | 安全性 | Risk of harmful content or unsafe recommendations. |
| RS-008 | Third-party Risk | 第三者リスク | Vendors, sub-processors, and model provider risks. |

### OB: Outcome / Benefit / 成果

Categorizes the expected outcomes or benefits from AI use. **Optional; select zero or more.**

| Code | Label (EN) | Label (JA) | Definition |
| --- | --- | --- | --- |
| OB-001 | Efficiency | 効率化 | Improves time/cost efficiency. |
| OB-002 | Quality | 品質向上 | Improves quality/accuracy of outputs. |
| OB-003 | Revenue | 売上貢献 | Contributes to revenue growth. |
| OB-004 | Risk Reduction | リスク低減 | Reduces operational/security/compliance risk. |
| OB-005 | Innovation | 新規性/革新 | Enables new capabilities or innovations. |
| OB-006 | Customer Satisfaction | 顧客満足 | Improves customer satisfaction. |
| OB-007 | Employee Experience | 従業員体験 | Improves employee experience. |

### EV: Evidence Type / 証跡種別

Categorizes the types of evidence required or collected. **Select one or more.**

| Code | Label (EN) | Label (JA) | Definition |
| --- | --- | --- | --- |
| EV-001 | Request Record | 申請記録 | Evidence that an AI use/service was requested and described. |
| EV-002 | Review/Approval Record | 審査/承認記録 | Evidence that a review/approval was performed. |
| EV-003 | Exception Record | 例外記録 | Evidence that an exception was granted and tracked. |
| EV-004 | Renewal/Re-evaluation Record | 更新/再評価記録 | Evidence that renewal or re-evaluation occurred. |
| EV-005 | Change Log Entry | 変更管理記録 | Evidence of changes and their approvals. |
| EV-006 | Integrity Proof | 完全性証明 | Evidence of integrity (hash, signature, WORM). |
| EV-007 | Access Log | アクセスログ | Evidence of access control and access history. |
| EV-008 | Model/Service Inventory | AI資産台帳 | Inventory record of models/services used. |
| EV-009 | Risk Assessment | リスク評価 | Documented risk assessment for the use/service. |
| EV-010 | Control Mapping | 統制マッピング | Control mapping evidence to external frameworks. |
| EV-011 | Training/Guidance | 教育/ガイダンス | Evidence of training or guidance provided to users. |
| EV-012 | Monitoring Evidence | 監視証跡 | Evidence of monitoring and ongoing oversight. |
| EV-013 | Incident Record | インシデント記録 | Evidence of incident handling related to AI use. |
| EV-014 | Third-party Assessment | 第三者評価 | Evidence of vendor or third-party assessment. |
| EV-015 | Attestation/Sign-off | 宣誓/サインオフ | Formal attestation or sign-off record. |

## How to Use

### Relationship with Evidence

Each Evidence (EV) document references codes from multiple dimensions to classify the AI system or use case being documented. The 8-dimension classification enables:

- **Consistent categorization** across the organization
- **Risk-based filtering** by dimension values
- **Framework mapping** via Coverage Map

### Referencing the Dictionary

For complete code definitions including scope notes and examples, refer to the [Dictionary](./05-dictionary.md).

### Example Classification

```
FS: FS-001 (End-user Productivity)
UC: UC-001 (General Q&A), UC-002 (Summarization)
DT: DT-002 (Internal), DT-004 (Personal Data)
CH: CH-001 (Web UI)
IM: IM-002 (SaaS Integrated)
RS: RS-001 (Data Leakage), RS-003 (Compliance Breach)
OB: OB-001 (Efficiency)
EV: EV-001 (Request Record), EV-002 (Review/Approval Record)
```

## SSOT Reference

The authoritative definition of the taxonomy is maintained in:

| Resource | Path |
| --- | --- |
| Dictionary CSV (SSOT) | `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv` |
| Taxonomy YAML (EN) | `source_pack/03_taxonomy/taxonomy_en.yaml` |
| Taxonomy YAML (JA) | `source_pack/03_taxonomy/taxonomy_ja.yaml` |
| Code System CSV | `source_pack/03_taxonomy/code_system.csv` |
| Dimensions EN/JA | `source_pack/03_taxonomy/dimensions_en_ja.md` |

**This documentation page is explanatory.** For authoritative definitions, always reference the SSOT files in `source_pack/03_taxonomy/`.

### Update Workflow

1. Edit the SSOT CSV (`taxonomy_dictionary_v0.1.csv`) first
2. Run `python tooling/checks/lint_taxonomy_dictionary.py` to validate
3. Run `python tooling/taxonomy/build_taxonomy_assets.py` to regenerate derived files
4. Update documentation pages as needed
5. Commit all changes together

## Related Pages

- [Codes](./04-codes.md) - Code format, naming conventions, and lifecycle
- [Dictionary](./05-dictionary.md) - Complete code listings and column definitions
- [Evidence Templates](./06-ev-template.md) - How to use codes in evidence
- [Responsibility Boundary](../../governance/responsibility-boundary.md) - Non-overclaim statement
