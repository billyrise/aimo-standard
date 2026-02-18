---
description: 調達・開示オーバーレイ（英国・日本）。英国 ATRS、英国調達ガイダンス、日本政府 GenAI 調達・AI ビジネスガイドライン。参照マッピングのみ。
---
<!-- aimo:translation_status=translated -->

# 調達・開示オーバーレイ（英国・日本）

本ページは、AIMO のエビデンスと**英国**・**日本**の調達・開示フレームワークの一部との**参照マッピング**を説明します。目的は**既に AIMO で整える証跡の再利用による負担軽減**です。**参考マッピングであり**、政府要求の完全充足を保証するものではありません。以下の一次ソースで確認してください。

## 一次ソース

**英国**

- [Algorithmic Transparency Recording Standard (ATRS) Hub](https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub) — GOV.UK（テンプレート、ガイダンス、公開記録）
- [ATRS テンプレート](https://www.gov.uk/government/publications/algorithmic-transparency-template) — 公共セクター向け公式テンプレート
- [ATRS 利用組織向けガイダンス](https://www.gov.uk/government/publications/guidance-for-organisations-using-the-algorithmic-transparency-standard/algorithmic-transparency-recording-standard-guidance-for-public-sector-bodies) — GOV.UK

**日本**

- [デジタル庁 — 生成AIの調達・利活用に係るガイドライン](https://www.digital.go.jp/news/3579c42d-b11c-4756-b66e-3d3e35175623) — デジタル庁：「行政の進化と革新のための生成AIの調達・利活用に係るガイドライン」
- [AI事業者ガイドライン](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/index.html) — 経済産業省・総務省

## マッピング表（英国）

| 政府要求（トピック） | AIMO 成果物 | Evidence Bundle 内の格納場所 | Validator カバレッジ | 注記 |
| --- | --- | --- | --- | --- |
| ATRS — 説明責任・オーナー | Summary、review | manifest；objects/（EV、Summary）；payload_index | schema_validate_ev | 参考マッピング；完全適合を保証しない。 |
| ATRS — システム/モデル説明 | Dictionary、EV | objects/；schemas/jsonschema/aimo-dictionary.schema.json | schema_validate_dictionary | 公式 ATRS 記録を External Forms に添付；logical_id でリンク。 |
| ATRS — リスク考慮 | Dictionary、request、review、exception | objects/；templates/ev/ | schema_validate_ev | プロファイル: `coverage_map/profiles/uk_atrs_procurement.json`。 |
| 調達 — 供給者エビデンス | request、review、exception；Evidence Bundle | manifest、object_index、payload_index；examples/evidence_bundle_minimal/ | schema_validate_ev | バンドルでエビデンスを構造化；英国ガイダンスが権威。 |

## マッピング表（日本）

| 政府要求（トピック） | AIMO 成果物 | Evidence Bundle 内の格納場所 | Validator カバレッジ | 注記 |
| --- | --- | --- | --- | --- |
| GenAI 調達チェックリスト（デジタル庁） | External Form（チェックリストをそのまま）；Dictionary、Summary | payload_index；External Forms 節；manifest 参照 | N/A（添付） | 参考マッピング；完全適合を保証しない。プロファイル: `coverage_map/profiles/jp_gov_genai_procurement.json`。 |
| AI 事業者ガイドライン — ガバナンス・トレーサビリティ | Summary、dictionary、request、review、change_log | objects/；manifest；templates/ev/ | schema_validate_dictionary、schema_validate_ev | トレーサビリティに有用な項目を AIMO タクソノミーにマッピング。 |
| リスク・説明責任の文書化 | Dictionary、EV、review、exception | objects/；schemas/jsonschema/ | schema_validate_ev | デジタル庁・経産省/総務省の公式ガイダンスで確認。 |

## 英国: ATRS と AI 調達（概要）

| トピック | AIMO エビデンス / マッピング | 備考 |
| --- | --- | --- |
| **英国 ATRS**（AI 透明性記録） | Summary、review（説明責任担当）、evidence（モデル/システム説明）、dictionary（リスク考慮）。プロファイル: `coverage_map/profiles/uk_atrs_procurement.json`。 | External Forms に ATRS 型透明性記録を添付または参照；logical_id でバンドルオブジェクトにリンク。 |
| **英国調達ガイダンス** | Request、review、exception；Evidence Bundle を供給者評価に利用。 | AIMO バンドルで調達評価用エビデンスを構造化；公式英国ガイダンスが権威。 |

## 日本: 政府 GenAI 調達・AI ビジネスガイドライン（概要）

| トピック | AIMO エビデンス / マッピング | 備考 |
| --- | --- | --- |
| **日本政府 GenAI 調達チェックリスト** | チェックリストを External Form として添付（例: payload: JP_PROCUREMENT_CHECKLIST）；manifest で参照。プロファイル: `coverage_map/profiles/jp_gov_genai_procurement.json`。 | 参照マッピングのみ；AIMO は公式チェックリストに代わりません。 |
| **AI ビジネスガイドライン** | Summary、dictionary；トレーサビリティに有用な場合、チェックリスト項目を AIMO タクソノミーコードにマッピング。 | 説明可能性に利用；公式日本ガイダンスで確認。 |

## 利用方法

- **External Forms**: 英国または日本の公式テンプレート/チェックリストを**そのまま**添付（PDF、DOC 等）、ハッシュし、Evidence Bundle の [payload_index](../../standard/current/09-evidence-bundle-structure/) または [EV テンプレート External Forms 節](../../standard/current/06-ev-template/)に記載。manifest とカバレッジマッピングで logical_id により参照。
- **プロファイル**: 上記プロファイルはオプションの機械可読マッピングを定義し、法的・契約上の義務を課しません。

レベルは [適合性](../../conformance/)、オーバーレイ概要は [最低証拠 — 規制オーバーレイ](../../artifacts/minimum-evidence/) を参照。
