---
description: AIMO Evidence Bundle構造。TOC、追跡可能性、AIガバナンスコンプライアンスと監査人への提出用アーティファクトを含む監査パッケージ形式。
---

# Evidence Bundle（証跡バンドル）

**Evidence Bundle** は監査用パッケージであり、AIガバナンスの説明可能性と追跡可能性を支える構造化されたアーティファクトの集合である。製品機能ではなく、監査・コンプライアンス向けの成果物形式である。

## ルート必須構成（規範）

バンドルの**ルート構成**は [Evidence Bundle ルート構造（v0.1）](../standard/current/09-evidence-bundle-structure.md) で規範的に定義する。バンドルルートには以下が MUST で存在すること：**manifest.json**、**objects/**、**payloads/**、**signatures/**、**hashes/**。**Integrity**（マニフェスト、sha256、署名の存在）は規範であり [Validator](../validator/index.md) が検証する。**Custody**（保管・アクセス制御）は実装側で定義する。

## バンドル構造と命名

- **バンドルルート命名**: `{org}_{system}_{period}_{version}` など一貫した形式を用いる（例: `acme_ai-usage_2026-Q1_v1`）。
- **必須ファイル**: [Evidence Pack テンプレート（EP）](../standard/current/06-ev-template.md) に整合した証跡（EV）セット、[Dictionary](../standard/current/05-dictionary.md)、バンドル概要の **Summary**、およびバンドル・内容の変更を記録する **Change Log**（またはその参照）を少なくとも含める。
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

## 規範的関係：EV レコード（索引）と Evidence Pack（ペイロード）

二重構築と監査上の曖昧さを避けるため、以下を**規範**とします。

1. **EV レコード（JSON）**は**索引／台帳**であり、機械検証可能なトレーサビリティを提供します。実施内容（申請・審査・例外・更新・変更）を記録し、安定IDと相互参照を MUST で持ちます。
2. **Evidence Pack ファイル**（EP-01..EP-07 のドキュメントとマニフェスト）は**ペイロード**であり、索引が参照する人間／ツール可読な証跡です。
3. **リンク**: EV レコードは `evidence_file_ids`（例：EP-01, EP-02）および／または暗号学的ハッシュでペイロードを参照することを SHOULD とします。[Validator](../validator/index.md) は、これらの参照が存在する場合（例：参照された file_id が Evidence Pack マニフェストに存在し、任意のハッシュが一致すること）に参照整合性をチェックします。
4. **監査提出の最小セット**: **EV JSON**（root/records）+ **Dictionary** + **Summary** + **Change Log** + **Evidence Pack**（マニフェスト＋ファイル、例：zip）。これら全体が適合の対象となります。

実装者は単一の情報源を維持します。EV 索引がパックを参照し、パックは Taxonomy EV コード（申請記録、審査/承認記録など）の意味を再定義しません。[Evidence Pack テンプレート](../standard/current/06-ev-template.md) で EP-01..EP-07 のドキュメント種別を参照してください。

## 追跡可能性（Traceability）

- **安定ID**: 各レコード（EV、request、review、exception、renewal、change log エントリ）は安定した一意の識別子を MUST で持つ。
- **相互参照**: Request → Review → Exception（あれば）→ Renewal をリンクし、EV 項目は参照フィールド（例: request_id, review_id, exception_id, renewal_id）でこれらにリンクする。
- **リンク**: 監査人が AI 利用（または例外）から申請・承認・例外（代替統制・有効期限）・更新までの鎖を追えるようにする。

## 監査での利用

監査では、Evidence Bundle を用いて、AI 利用が申請・審査・承認されていること、例外が有効期限と代替統制・更新と紐づいていること、変更が記録されていることを確認する。TOC と追跡可能性のルールにより、必要なアーティファクトの所在と、request / review / exception / renewal / EV 間の ID と参照の追跡が可能となる。Summary で概要を把握し、Change Log で変更管理と説明責任を支える。

MUST レベルのフィールドとライフサイクル区分は [Minimum Evidence Requirements](minimum-evidence.md) を参照。

## 運用ガイダンス

!!! info "Integrity（規範）と Custody（実装側）"
    - **Integrity** は v0.1 で規範とする。バンドルには manifest.json、object_index/payload_index の sha256、signatures/ にマニフェスト参照署名が必須。[Validator](../validator/index.md) がこれらを満たさないバンドルを拒否する。
    - **Custody**（アクセス制御・保持・WORM）は実装側で定義する。採用者はアクセスロール、保持ポリシー、監査証跡を文書化すること。詳細は [Minimum Evidence Requirements > Integrity & Access](minimum-evidence.md#6-integrity-access) を参照。

## 監査ジャーニー

本ページから、典型的な監査ジャーニーは以下のように続く：

1. **次へ**: [Minimum Evidence Requirements](minimum-evidence.md) — ライフサイクル別 MUST チェックリスト
2. **一枚まとめ**: [Evidence Bundle Coverage Map（テンプレ）](evidence-bundle-coverage-map.md) — スコープ・エビデンス種別・コントロール対応・除外・整合性（informative）
3. **続いて**: [Coverage Map](../coverage-map/index.md) — 外部フレームワークへのマッピング
4. **検証**: [Validator](../validator/index.md) — 構造チェックを実行
5. **ダウンロード**: [Releases](../../releases/) — リリースアセットを取得し、チェックサムを検証
