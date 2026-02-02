---
description: AIMO Evidence Bundle構造。TOC、追跡可能性、AIガバナンスコンプライアンスと監査人への提出用アーティファクトを含む監査パッケージ形式。
---

# Evidence Bundle（証跡バンドル）

**Evidence Bundle** は監査用パッケージであり、AIガバナンスの説明可能性と追跡可能性を支える構造化されたアーティファクトの集合である。製品機能ではなく、監査・コンプライアンス向けの成果物形式である。

## バンドル構造と命名

- **バンドルルート命名**: `{org}_{system}_{period}_{version}` など一貫した形式を用いる（例: `acme_ai-usage_2026-Q1_v1`）。
- **必須ファイル**: [EV Template](../standard/current/06-ev-template.md) に整合した証跡（EV）セット、[Dictionary](../standard/current/05-dictionary.md)、バンドル概要の **Summary**、およびバンドル・内容の変更を記録する **Change Log**（またはその参照）を少なくとも含める。
- **任意添付**: ログ、審査記録、例外承認、更新記録など。命名を統一し、EV/辞書から参照可能にすること。

## 目次（TOC）

| セクション | アーティファクト | 必須 | 目的 | 最小フィールド | 検証 |
| --- | --- | --- | --- | --- | --- |
| Evidence | EV レコード（JSON/配列） | はい | 実施内容の記録；request/review/exception/renewal へのリンク | id, timestamp, source, summary；任意でライフサイクル参照 | [Validator](../validator/index.md)、aimo-ev.schema.json |
| Dictionary | dictionary.json | はい | コード・次元のキー/ラベル/説明 | entries（key, label, description） | aimo-dictionary.schema.json |
| Summary | summary（文書またはフィールド） | はい | 監査向け1ページ概要 | スコープ、期間、主要判断、例外 | — |
| Change log | change_log または参照 | はい | バンドル/内容変更の監査証跡 | id, timestamp, actor, 変更内容, references | — |
| Request | 申請記録 | 該当時 | 利用の申請 | id, timestamp, actor/role, scope, rationale | — |
| Review/Approval | 審査/承認記録 | 該当時 | 審査・承認結果 | id, timestamp, actor/role, decision, references | — |
| Exception | 例外記録 | 該当時 | 代替統制・有効期限付き例外 | id, timestamp, scope, expiry, compensating controls, renewal ref | — |
| Renewal | 更新記録 | 該当時 | 再評価・更新 | id, timestamp, actor/role, decision, 先行 exception/EV への参照 | — |

## 追跡可能性（Traceability）

- **安定ID**: 各レコード（EV、request、review、exception、renewal、change log エントリ）は安定した一意の識別子を MUST で持つ。
- **相互参照**: Request → Review → Exception（あれば）→ Renewal をリンクし、EV 項目は参照フィールド（例: request_id, review_id, exception_id, renewal_id）でこれらにリンクする。
- **リンク**: 監査人が AI 利用（または例外）から申請・承認・例外（代替統制・有効期限）・更新までの鎖を追えるようにする。

## 監査での利用

監査では、Evidence Bundle を用いて、AI 利用が申請・審査・承認されていること、例外が有効期限と代替統制・更新と紐づいていること、変更が記録されていることを確認する。TOC と追跡可能性のルールにより、必要なアーティファクトの所在と、request / review / exception / renewal / EV 間の ID と参照の追跡が可能となる。Summary で概要を把握し、Change Log で変更管理と説明責任を支える。

MUST レベルのフィールドとライフサイクル区分は [Minimum Evidence Requirements](minimum-evidence.md) を参照。

## 運用ガイダンス

!!! info "完全性とアクセス制御"
    AIMO は特定の統制を規定しないが、採用者は以下を文書化すべきである：
    
    - **アクセスロール**: 誰が証跡を作成・閲覧・更新・削除できるか
    - **保持ポリシー**: 証跡をどのくらいの期間、どのスケジュールで保持するか
    - **完全性メカニズム**: 使用するハッシュ、WORM ストレージ、デジタル署名
    - **監査証跡**: バンドルへのアクセスと変更のログ
    
    詳細は [Minimum Evidence Requirements > Integrity & Access](minimum-evidence.md#6-integrity-access完全性アクセス制御) を参照。

## 監査ジャーニー

本ページから、典型的な監査ジャーニーは以下のように続く：

1. **次へ**: [Minimum Evidence Requirements](minimum-evidence.md) — ライフサイクル別 MUST チェックリスト
2. **続いて**: [Coverage Map](../coverage-map/index.md) — 外部フレームワークへのマッピング
3. **検証**: [Validator](../validator/index.md) — 構造チェックを実行
4. **ダウンロード**: [Releases](../releases/index.md) — リリースアセットを取得し、チェックサムを検証
