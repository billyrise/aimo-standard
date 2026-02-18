---
description: AIMO Standard と EU AI 法のマッピング。AIMO タクソノミーコードと EU AI 法リスク区分・要求とのトレーサビリティ。
---
<!-- aimo:translation_status=translated -->

# EU AI 法マッピング

> トレーサビリティ: タクソノミー → 最低証拠 → Validator → 人間監督プロトコル。

- [タクソノミー](../../standard/current/03-taxonomy/)
- [最低証拠要件](../../artifacts/minimum-evidence/)
- [ログスキーマ](../../artifacts/log-schemas/)
- [Validator](../../validator/)
- [人間監督プロトコル](../../governance/human-oversight-protocol/)

本ページは、選定した EU AI 法のテーマ（文書化、記録保存、リスク管理、人間監督、透明性）を AIMO のエビデンス・アーティファクトにマッピングします。概要レベルであり、**法務助言**や適合保証を構成しません。正式な法文で確認してください。

**参照:** 規則 (EU) 2024/1689（人工知能法）。以下、条番号は同規則を指します。

## マッピング表

| フレームワーク参照 / トピック | AIMO エビデンス / AIMO 内の位置 | Evidence Bundle / 最低証拠 | アーティファクト・検証 | 備考 |
| --- | --- | --- | --- | --- |
| 第4条 – AI リテラシー | [スコープ](../../standard/current/02-scope/) | Summary、EV；review | templates/ev/ | 横断的；組織能力・研修のエビデンス（概要）。法務助言ではない。公式テキストで確認。 |
| 第9条 – リスクマネジメントシステム | [スコープ](../../standard/current/02-scope/) | request、review、exception、renewal | templates/ev/ | 高リスク AI システム（第3編）。法務助言ではない。公式テキストで確認。 |
| 第10条 – データ・データガバナンス | [辞書](../../standard/current/05-dictionary/) | Dictionary、EV | schemas/jsonschema/；schema_validate_dictionary | 法務助言ではない。公式テキストで確認。 |
| 第11条 – 技術文書（高リスク） | [EV テンプレート](../../standard/current/06-ev-template/)、[Evidence Bundle](../../artifacts/evidence-bundle/) | EV、Dictionary、Summary；request、review | schemas/jsonschema/、templates/ev/；**附属書 IV**: [例 > EU 附属書 IV サンプル](../../examples/)（`examples/evidence_bundle_v01_annex_iv_sample/`）；プロファイル: `coverage_map/profiles/eu_ai_act_annex_iv.json`。サンプルバンドルは規範準拠（signatures/、hashes/、附属書 IV 向け技術文書の payload）。例を参照（追加サンプルは将来リリース）。 | 概要のみ；法務助言ではない。公式テキストで確認。 |
| 第12条 – 記録保存 | [Evidence Bundle](../../artifacts/evidence-bundle/)、[最低証拠](../../artifacts/minimum-evidence/) | EV、change_log、request、review | examples/evidence_bundle_minimal/；schema_validate_ev | 法務助言ではない。公式テキストで確認。 |
| 第13条 – デプロイヤー・利用者への透明性・情報提供 | [スコープ](../../standard/current/02-scope/) | Summary、EV；review | templates/ev/ | 高リスク文脈。法務助言ではない。公式テキストで確認。 |
| 第14条 – 人間監督 | [最低証拠](../../artifacts/minimum-evidence/) | review、exception | templates/ev/ev_template.md | 法務助言ではない。公式テキストで確認。 |
| 第15条 – 正確性・ロバスト性・サイバーセキュリティ | [最低証拠](../../artifacts/minimum-evidence/) | EV（証拠コード/リスクコード、概要） | templates/ev/ | 概要マッピングのみ。法務助言ではない。公式テキストで確認。 |
| 第17条 – 品質マネジメントシステム | [スコープ](../../standard/current/02-scope/) | Summary、review（組織プロセス） | templates/ev/ | 第9条（リスクマネジメントシステム）とは別。法務助言ではない。公式テキストで確認。 |
| 透明性義務（ユースケース依存） | [スコープ](../../standard/current/02-scope/)、[最低証拠](../../artifacts/minimum-evidence/) | Summary、EV；review | templates/ev/ | 適用規定はユースケース（限定リスク、デプロイヤー義務等）による。法務助言ではない。公式テキストで確認。 |
| GPAI モデル義務 | [EV テンプレート](../../standard/current/06-ev-template/)、[Evidence Bundle](../../artifacts/evidence-bundle/) | EV テンプレート、Evidence Bundle（エビデンス構造化フレーム） | schemas/jsonschema/；schema_validate_ev | AIMO はエビデンス整理の枠組みを提供；実際の義務は規則で定義。法務助言ではない。公式テキストで確認。 |
| 前文 – 説明責任 | [Evidence Bundle](../../artifacts/evidence-bundle/) | EV、request、review、change_log | examples/evidence_bundle_minimal/；schema_validate_ev | 法務助言ではない。公式テキストで確認。 |

## 施行日・適用（概要）

以下は **EU 公式タイムライン**（AI 法サービスデスク/委員会）に沿った概要です。**法務助言ではなく**、正確性を保証しません。**正式な法文**と所管当局で必ず確認してください。

| 段階 | 日付 | 適用内容（概要） |
| --- | --- | --- |
| 発効 | 2024年8月 | 規則発効；実体義務の多くは未適用。 |
| 一般規定・禁止 | 2025年2月2日 | 禁止行為（容認不能リスク）；AI リテラシー関連規定の一部。 |
| GPAI 規則・ガバナンス | 2025年8月2日 | 指定機関、GPAI、ガバナンス、秘密保持、罰則；行動規範。 |
| 主要規則・附属書 III 高リスク・第50条透明性 | 2026年8月2日 | 高リスク AI システム（附属書 III）の完全適用、第50条透明性義務。 |
| 規制製品に組み込まれた高リスク | 2027年8月2日 | EU 製品法の対象となる製品に組み込まれた高リスク AI システム。 |

## 調和標準と適合推定（第40条）

AI 法に基づき EU 官報で**調和標準**が公布されると、それへの適合は対応する要求への**適合推定**となり得ます。一覧・日付は標準化作業と官報公布に依存します。AIMO のマッピングは参考であり、適合推定を与えません。現状は欧州委員会の [AI 法標準化](https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation) ページおよび**参考文献**を参照してください。

## 2026年 AI オフィスガイドライン（実施詳細）

欧州委員会は **AI オフィス**が 2026 年に**実務ガイドライン**を策定する旨示しており、以下を含みます：

- 高リスク分類
- 第50条（透明性）の実施
- インシデント報告
- QMS 関連要素

これらガイドラインは AIMO のプロファイル・カバレッジマッピングの**更新トリガー**です：公布後、採用者はエビデンスとマッピングを最新の公式ガイダンスに合わせてください。AIMO はこれらガイドラインの解釈や適合を保証しません。

!!! warning "法務助言ではない"
    本ページは説明目的のみです。適用範囲・日付は正式な規則および施行・改正法で確認してください。AIMO は法務助言も適合保証も提供しません。

!!! note "法的注記 / 参考マッピング"
    本ページは**参考**であり、法的解釈は正式な規則（EUR-Lex）および欧州委員会公表物に基づいてください。AIMO は法務助言も適合保証も提供しません。

## 参考文献

**一次ソース**

- [規則 (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689)（EUR-Lex）— 人工知能法（法文）
- [EU AI 法の実施タイムライン](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act) — 欧州委員会 AI 法サービスデスク（実施タイムライン）
- [AI 法の標準化](https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation) — 欧州委員会デジタル戦略（調和標準・適合推定）

**その他**

- 欧州委員会 / AI オフィス — ガイドライン・タイムライン（AI 法サービスデスク・委員会ニュースで最新 URL を確認）
- [EPRS — EU AI 法実施](https://www.europarl.europa.eu/thinktank/) — 議会ブリーフィング（参考）
