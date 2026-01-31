# タクソノミー

AIMOタクソノミーは、AIシステム、その利用、および関連するガバナンス要件を分類するための構造化されたフレームワークを提供します。組織全体で一貫した分類と証跡管理を可能にする**8つの次元**で構成されています。

## 目的と監査の文脈

タクソノミーは監査の観点から2つの主要な目的を果たします：

1. **証跡準備（Evidence Readiness）**: 標準化された分類を使用してAIシステムを体系的に文書化し、証跡の収集とレビューをより効率的にします。

2. **説明可能性（Explainability）**: 組織全体でAIユースケースを説明するための共通の語彙を提供し、監査人やステークホルダーとの明確なコミュニケーションを支援します。

!!! warning "非過大主張"
    AIMO Standardは**説明可能性と証跡準備**を支援します。法的助言の提供、コンプライアンスの保証、規制やフレームワークへの適合の認証を行うものでは**ありません**。詳細は[責任境界](../../governance/responsibility-boundary.md)を参照してください。

## 唯一の正（Single Source of Truth: SSOT）

タクソノミーの正式な定義は機械可読ファイルで管理されています：

| ファイル | 説明 |
| --- | --- |
| `taxonomy_dictionary_v0.1.csv` | 全コードのSSOT（8次元にわたる91コード） |
| `taxonomy_en.yaml` | 英語タクソノミー（CSVから生成） |
| `taxonomy_ja.yaml` | 日本語タクソノミー（CSVから生成） |

**このドキュメントページは説明用です。** 正式な定義については、常に`source_pack/03_taxonomy/`内のSSOTファイルを参照してください。

## コード体系の概要

AIMOは`<DIM>-<TOKEN>`形式のコード体系を使用します：

- `<DIM>`: 2文字の次元識別子（例：FS, UC, DT）
- `<TOKEN>`: 3桁の数値トークン（例：001, 002, 003）

**例：**

- `UC-001`: 一般QA（ユースケース分類）
- `DT-004`: 個人情報（データ種別）
- `CH-003`: IDEプラグイン（チャネル）
- `IM-002`: SaaS連携（統合形態）

## 8つの次元

| 優先度 | ID | 名称（EN） | 名称（JA） | 必須 | 複数選択 | 識別対象 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **FS** | Functional Scope | 機能スコープ | はい | いいえ | どのビジネス機能が支援されるか |
| 2 | **UC** | Use Case Class | ユースケース分類 | はい | はい | どのタイプのタスクが実行されるか |
| 3 | **DT** | Data Type | データ種別 | はい | はい | どのデータ機密性が関与するか |
| 4 | **CH** | Channel | チャネル | はい | はい | ユーザーがどのようにAIにアクセスするか |
| 5 | **IM** | Integration Mode | 統合形態 | はい | いいえ | AIがエンタープライズシステムにどう接続するか |
| 6 | **RS** | Risk Surface | リスク面 | はい | はい | どのリスクが関連するか |
| 7 | **OB** | Outcome / Benefit | 成果 | いいえ | はい | どのベネフィットが期待されるか |
| 8 | **EV** | Evidence Type | 証跡種別 | はい | はい | どの証跡が必要か |

### 使用ルールの要約

| 次元 | 選択 | 監査上の意味 |
| --- | --- | --- |
| FS, IM | 正確に1つ | 責任割当のための主要分類 |
| UC, DT, CH, RS, EV | 1つ以上 | リスクカバレッジのための完全列挙が必要 |
| OB | 0個以上 | 任意；期待されるビジネス価値を文書化 |

## 次元の定義

### FS: Functional Scope / 機能スコープ

AIが支援するビジネス機能による分類。**正確に1つを選択。**

| コード | ラベル（EN） | ラベル（JA） | 説明 |
| --- | --- | --- | --- |
| FS-001 | End-user Productivity | 社内生産性 | 社内生産性向上のAI（執筆、検索、要約） |
| FS-002 | Customer-facing Features | 顧客向け機能 | 顧客向け製品・サービスに組み込まれたAI |
| FS-003 | Developer Tooling | 開発支援 | ソフトウェア開発支援のAI |
| FS-004 | IT Operations | IT運用 | IT運用・システム管理のAI |
| FS-005 | Security Operations | セキュリティ運用 | セキュリティ監視・対応のAI |
| FS-006 | Governance & Compliance | ガバナンス/コンプライアンス | ガバナンス/コンプライアンス業務のAI |

### UC: Use Case Class / ユースケース分類

タスクまたは対話の種類によるAI利用の分類。**1つ以上を選択。** 完全なリストには30コードが含まれます；以下は代表的な例です。

| コード | ラベル（EN） | ラベル（JA） | 説明 |
| --- | --- | --- | --- |
| UC-001 | General Q&A | 一般QA | 一般的な質問応答 |
| UC-002 | Summarization | 要約 | 文書・会議の要約 |
| UC-003 | Translation | 翻訳 | 言語間翻訳 |
| UC-004 | Content Drafting | 文章作成 | 文書の下書き生成 |
| UC-005 | Code Generation | コード生成 | コードやスクリプトの生成 |
| UC-010 | Agentic Automation | エージェント自動化 | 自律エージェントによるアクション実行 |

30個のUCコードの完全なリストは[辞書](./05-dictionary.md)を参照してください。

### DT: Data Type / データ種別

関与するデータの機密性と分類。**1つ以上を選択。**

| コード | ラベル（EN） | ラベル（JA） | 説明 |
| --- | --- | --- | --- |
| DT-001 | Public | 公開情報 | 公開されているデータ |
| DT-002 | Internal | 社内情報 | 非公開の社内業務データ |
| DT-003 | Confidential | 機密情報 | アクセス制限が必要な高機密データ |
| DT-004 | Personal Data | 個人情報 | プライバシー法令で定義される個人データ |
| DT-005 | Sensitive Personal Data | 要配慮個人情報 | 要配慮個人情報（特別カテゴリ） |
| DT-006 | Credentials | 認証情報 | 認証情報（パスワード、APIキー等） |
| DT-007 | Source Code | ソースコード | ソースコードおよび関連アーティファクト |
| DT-008 | Customer Data | 顧客データ | 顧客から提供された、または顧客に関連するデータ |
| DT-009 | Operational Logs | 運用ログ | システム運用ログ |
| DT-010 | Security Telemetry | セキュリティテレメトリ | セキュリティ監視データ |

### CH: Channel / チャネル

ユーザーがAIにアクセス・対話する方法。**1つ以上を選択。**

| コード | ラベル（EN） | ラベル（JA） | 説明 |
| --- | --- | --- | --- |
| CH-001 | Web UI | Web UI | WebブラウザUI経由 |
| CH-002 | API | API | API連携経由 |
| CH-003 | IDE Plugin | IDEプラグイン | IDE/エディタプラグイン経由 |
| CH-004 | ChatOps | チャット連携 | Slack/Teams連携経由 |
| CH-005 | Desktop App | デスクトップアプリ | ネイティブデスクトップアプリ経由 |
| CH-006 | Mobile App | モバイルアプリ | ネイティブモバイルアプリ経由 |
| CH-007 | Embedded Widget | 埋め込みウィジェット | 他のアプリケーションに埋め込み |
| CH-008 | Batch/CLI | バッチ/CLI | コマンドラインまたはバッチ処理経由 |

### IM: Integration Mode / 統合形態

AIがエンタープライズシステムに統合される形態。**正確に1つを選択。**

| コード | ラベル（EN） | ラベル（JA） | 説明 |
| --- | --- | --- | --- |
| IM-001 | Standalone | 単体利用 | 企業システム統合なしの単体利用 |
| IM-002 | SaaS Integrated | SaaS連携 | AI機能を持つSaaSアプリケーション |
| IM-003 | Enterprise App Embedded | 社内アプリ組込み | 社内アプリにAIを組み込む |
| IM-004 | RPA/Workflow | ワークフロー/RPA | ワークフロー自動化内でのAI呼び出し |
| IM-005 | On-prem / Private | オンプレ/プライベート | プライベート/オンプレ環境でのAI |
| IM-006 | Hybrid Cloud | ハイブリッドクラウド | クラウドとオンプレの組み合わせ |
| IM-007 | Multi-tenant SaaS | マルチテナントSaaS | 共有SaaSインフラストラクチャ |

### RS: Risk Surface / リスク面

AI利用に関連するリスクの種類。**1つ以上を選択。**

| コード | ラベル（EN） | ラベル（JA） | 説明 |
| --- | --- | --- | --- |
| RS-001 | Data Leakage | 情報漏えい | 意図しないデータ開示のリスク |
| RS-002 | Security Abuse | 悪用/攻撃 | 悪意ある目的での悪用リスク |
| RS-003 | Compliance Breach | 法令/規程違反 | 法令・規程・契約の違反リスク |
| RS-004 | IP Infringement | 知財侵害 | 著作権・特許・営業秘密の侵害リスク |
| RS-005 | Model Misuse | モデル誤用 | 不適切なモデル利用・過信のリスク |
| RS-006 | Bias/Fairness | バイアス/公平性 | 差別的な出力のリスク |
| RS-007 | Availability | 可用性 | サービス中断のリスク |
| RS-008 | Supply Chain | サプライチェーン | サードパーティ依存のリスク |

### OB: Outcome / Benefit / 成果

AI利用から期待される成果・ベネフィット。**任意；0個以上を選択。**

| コード | ラベル（EN） | ラベル（JA） | 説明 |
| --- | --- | --- | --- |
| OB-001 | Efficiency | 効率化 | 時間・コスト効率の改善 |
| OB-002 | Quality | 品質向上 | 成果物の品質・精度向上 |
| OB-003 | Revenue | 売上貢献 | 売上成長への寄与 |
| OB-004 | Risk Reduction | リスク低減 | 運用・セキュリティ・コンプライアンスリスクの低減 |
| OB-005 | Innovation | 新規性/革新 | 新たな能力・イノベーションの実現 |
| OB-006 | Customer Satisfaction | 顧客満足度 | 顧客体験の向上 |
| OB-007 | Employee Experience | 従業員体験 | 従業員の生産性・満足度向上 |

### EV: Evidence Type / 証跡種別

必要な/収集する証跡の種類。**1つ以上を選択。** 以下は**MVP必須**の証跡種別です（EV-001からEV-007）：

| コード | ラベル（EN） | ラベル（JA） | 説明 |
| --- | --- | --- | --- |
| EV-001 | System Overview | システム概要 | AIシステムの概要 |
| EV-002 | Data Flow | データフロー | データフロー図と説明 |
| EV-003 | Inventory | AI資産台帳 | AIシステム/モデルの台帳 |
| EV-004 | Risk & Impact Assessment | リスク影響評価 | リスクと影響の評価 |
| EV-005 | Controls & Approvals | 統制/承認 | 統制措置と承認記録 |
| EV-006 | Logging & Monitoring | ログ監視 | ログと監視の設定 |
| EV-007 | Incident & Exception | インシデント/例外 | インシデントと例外の対応 |

追加の証跡種別（EV-008からEV-015）は拡張ドキュメント用に利用可能です。完全なリストは[辞書](./05-dictionary.md)を参照してください。

## SSOT参照

| リソース | パス | 説明 |
| --- | --- | --- |
| Dictionary CSV | `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv` | 全91コードと完全なメタデータ |
| Taxonomy YAML (EN) | `source_pack/03_taxonomy/taxonomy_en.yaml` | 生成された英語タクソノミー |
| Taxonomy YAML (JA) | `source_pack/03_taxonomy/taxonomy_ja.yaml` | 生成された日本語タクソノミー |
| Taxonomy Pack Schema | `source_pack/03_taxonomy/schemas/taxonomy_pack.schema.json` | バリデーション用JSON Schema |

## ダウンロード

完全なタクソノミーパッケージは[リリース](../../releases/index.md)ページからダウンロードできます。

## 関連ページ

- [コード](./04-codes.md) - コードフォーマット、命名規則、ライフサイクル
- [辞書](./05-dictionary.md) - 完全なコード一覧と列定義
- [証跡テンプレート](./06-ev-template.md) - MVP証跡テンプレート
- [責任境界](../../governance/responsibility-boundary.md) - 非過大主張声明
