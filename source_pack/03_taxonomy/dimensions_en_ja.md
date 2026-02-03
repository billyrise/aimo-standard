# Dimension Names EN/JA Mapping

**Status**: Generated from data/taxonomy/
**DO NOT EDIT MANUALLY** - regenerate with: `python tooling/taxonomy/build_artifacts.py`

---

## Dimension Definitions

| ID | Name (EN) | Name (JA) | Code Count | Prefix |
| --- | --- | --- | --- | --- |
| **CH** | Channel | チャネル | 8 | `CH-` |
| **DT** | Data Type | データ種別 | 10 | `DT-` |
| **FS** | Functional Scope | 機能スコープ | 6 | `FS-` |
| **IM** | Integration Mode | 統合形態 | 7 | `IM-` |
| **LG** | Log/Event Type | ログ/記録種別 | 15 | `LG-` |
| **OB** | Outcome / Benefit | 成果 | 7 | `OB-` |
| **RS** | Risk Surface | リスク面 | 8 | `RS-` |
| **UC** | Use Case Class | ユースケース分類 | 30 | `UC-` |

---

## Code Summary by Dimension

### CH: Channel / チャネル

| Code | Label (EN) | Label (JA) | Status |
| --- | --- | --- | --- |
| CH-001 | Web UI | Web UI | active |
| CH-002 | API | API | active |
| CH-003 | IDE Plugin | IDEプラグイン | active |
| CH-004 | ChatOps | チャット連携 | active |
| CH-005 | Desktop App | デスクトップアプリ | active |
| CH-006 | Mobile App | モバイルアプリ | active |
| CH-007 | Email | メール | active |
| CH-008 | Command Line | CLI | active |

### DT: Data Type / データ種別

| Code | Label (EN) | Label (JA) | Status |
| --- | --- | --- | --- |
| DT-001 | Public | 公開情報 | active |
| DT-002 | Internal | 社内情報 | active |
| DT-003 | Confidential | 機密情報 | active |
| DT-004 | Personal Data | 個人情報 | active |
| DT-005 | Sensitive Personal Data | 要配慮個人情報 | active |
| DT-006 | Credentials | 認証情報 | active |
| DT-007 | Source Code | ソースコード | active |
| DT-008 | Customer Data | 顧客データ | active |
| DT-009 | Operational Logs | 運用ログ | active |
| DT-010 | Security Telemetry | セキュリティテレメトリ | active |

### FS: Functional Scope / 機能スコープ

| Code | Label (EN) | Label (JA) | Status |
| --- | --- | --- | --- |
| FS-001 | End-user Productivity | 社内生産性 | active |
| FS-002 | Customer-facing Features | 顧客向け機能 | active |
| FS-003 | Developer Tooling | 開発支援 | active |
| FS-004 | IT Operations | IT運用 | active |
| FS-005 | Security Operations | セキュリティ運用 | active |
| FS-006 | Governance & Compliance | ガバナンス/コンプライアンス | active |

### IM: Integration Mode / 統合形態

| Code | Label (EN) | Label (JA) | Status |
| --- | --- | --- | --- |
| IM-001 | Standalone | 単体利用 | active |
| IM-002 | SaaS Integrated | SaaS連携 | active |
| IM-003 | Enterprise App Embedded | 社内アプリ組込み | active |
| IM-004 | RPA/Workflow | ワークフロー/RPA | active |
| IM-005 | On-prem / Private | オンプレ/プライベート | active |
| IM-006 | Managed Service | マネージド | active |
| IM-007 | Shadow / Unmanaged | シャドー/未管理 | active |

### LG: Log/Event Type / ログ/記録種別

| Code | Label (EN) | Label (JA) | Status |
| --- | --- | --- | --- |
| LG-001 | Request Record | 申請記録 | active |
| LG-002 | Review/Approval Record | 審査/承認記録 | active |
| LG-003 | Exception Record | 例外記録 | active |
| LG-004 | Renewal/Re-evaluation Record | 更新/再評価記録 | active |
| LG-005 | Change Log Entry | 変更管理記録 | active |
| LG-006 | Integrity Proof | 完全性証明 | active |
| LG-007 | Access Log | アクセスログ | active |
| LG-008 | Model/Service Inventory | AI資産台帳 | active |
| LG-009 | Risk Assessment | リスク評価 | active |
| LG-010 | Control Mapping | 統制マッピング | active |
| LG-011 | Training/Guidance | 教育/ガイダンス | active |
| LG-012 | Monitoring Evidence | 監視証跡 | active |
| LG-013 | Incident Record | インシデント記録 | active |
| LG-014 | Third-party Assessment | 第三者評価 | active |
| LG-015 | Attestation/Sign-off | 宣誓/サインオフ | active |

### OB: Outcome / Benefit / 成果

| Code | Label (EN) | Label (JA) | Status |
| --- | --- | --- | --- |
| OB-001 | Efficiency | 効率化 | active |
| OB-002 | Quality | 品質向上 | active |
| OB-003 | Revenue | 売上貢献 | active |
| OB-004 | Risk Reduction | リスク低減 | active |
| OB-005 | Innovation | 新規性/革新 | active |
| OB-006 | Customer Satisfaction | 顧客満足 | active |
| OB-007 | Employee Experience | 従業員体験 | active |

### RS: Risk Surface / リスク面

| Code | Label (EN) | Label (JA) | Status |
| --- | --- | --- | --- |
| RS-001 | Data Leakage | 情報漏えい | active |
| RS-002 | Security Abuse | 悪用/攻撃 | active |
| RS-003 | Compliance Breach | 法令/規程違反 | active |
| RS-004 | IP Infringement | 知財侵害 | active |
| RS-005 | Model Misuse | モデル誤用 | active |
| RS-006 | Bias/Fairness | 偏り/公平性 | active |
| RS-007 | Safety | 安全性 | active |
| RS-008 | Third-party Risk | 第三者リスク | active |

### UC: Use Case Class / ユースケース分類

| Code | Label (EN) | Label (JA) | Status |
| --- | --- | --- | --- |
| UC-001 | General Q&A | 一般QA | active |
| UC-002 | Summarization | 要約 | active |
| UC-003 | Translation | 翻訳 | active |
| UC-004 | Content Drafting | 文章作成 | active |
| UC-005 | Code Generation | コード生成 | active |
| UC-006 | Code Review | コードレビュー | active |
| UC-007 | Data Analysis | データ分析 | active |
| UC-008 | Classification/Tagging | 分類/タグ付け | active |
| UC-009 | Search/RAG | 検索/RAG | active |
| UC-010 | Agentic Automation | エージェント自動化 | active |
| UC-011 | Security Triage | セキュリティ一次対応 | active |
| UC-012 | Policy/Control Mapping | 規程/統制マッピング | active |
| UC-013 | Customer Support | 顧客対応 | active |
| UC-014 | Sales Enablement | 営業支援 | active |
| UC-015 | HR Support | 人事支援 | active |
| UC-016 | Finance Analysis | 財務分析 | active |
| UC-017 | Legal Drafting | 法務ドラフト | active |
| UC-018 | Procurement Support | 調達支援 | active |
| UC-019 | IT Helpdesk | ITヘルプデスク | active |
| UC-020 | Documentation | ドキュメント整備 | active |
| UC-021 | Knowledge Base | ナレッジベース | active |
| UC-022 | Monitoring/Observability | 監視/可観測性 | active |
| UC-023 | Incident Response | インシデント対応 | active |
| UC-024 | Threat Modeling | 脅威モデリング | active |
| UC-025 | Control Testing | 統制テスト | active |
| UC-026 | Training/Learning | 研修/学習 | active |
| UC-027 | Marketing Content | マーケティング | active |
| UC-028 | Research | 調査/リサーチ | active |
| UC-029 | Decision Support | 意思決定支援 | active |
| UC-030 | Other | その他 | active |

---

## Generation Info

- **Source**: `data/taxonomy/canonical.yaml` + `i18n/*.yaml`
- **Generated**: 2026-02-03
- **Total Codes**: 91
