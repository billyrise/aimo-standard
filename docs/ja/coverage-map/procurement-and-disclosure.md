---
description: 調達・開示オーバーレイ（英国・日本）。英国 ATRS、英国調達ガイダンス、日本政府 GenAI 調達・AI ビジネスガイドライン。参照マッピングのみ。
---
<!-- aimo:translation_status=translated -->

# 調達・開示オーバーレイ（英国・日本）

本ページは、AIMO のエビデンスと、**英国**および**日本**の調達・開示フレームワークの一部との**参照マッピング**を説明します。**参照マッピングのみ**であり、AIMO は公式チェックリストや政府ガイダンスに代わるものではありません。

## 英国: ATRS と AI 調達

| トピック | AIMO エビデンス / マッピング | 備考 |
| --- | --- | --- |
| **英国 ATRS**（AI 透明性記録） | Summary、review（説明責任担当）、evidence（モデル/システム説明）、dictionary（リスク考慮）。プロファイル: `coverage_map/profiles/uk_atrs_procurement.json`。 | External Forms に ATRS 型透明性記録を添付または参照；logical_id でバンドルオブジェクトにリンク。 |
| **英国調達ガイダンス** | Request、review、exception；Evidence Bundle を供給者評価に利用。 | AIMO バンドルで調達評価用エビデンスを構造化；公式英国ガイダンスが権威。 |

## 日本: 政府 GenAI 調達・AI ビジネスガイドライン

| トピック | AIMO エビデンス / マッピング | 備考 |
| --- | --- | --- |
| **日本政府 GenAI 調達チェックリスト** | チェックリストを External Form として添付（例: payload: JP_PROCUREMENT_CHECKLIST）；manifest で参照。プロファイル: `coverage_map/profiles/jp_gov_genai_procurement.json`。 | 参照マッピングのみ；AIMO は公式チェックリストに代わりません。 |
| **AI ビジネスガイドライン** | Summary、dictionary；トレーサビリティに有用な場合、チェックリスト項目を AIMO タクソノミーコードにマッピング。 | 説明可能性に利用；公式日本ガイダンスで確認。 |

## 利用方法

- **External Forms**: 英国または日本の公式テンプレート/チェックリストを**そのまま**添付（PDF、DOC 等）、ハッシュし、Evidence Bundle の [payload_index](../../standard/current/09-evidence-bundle-structure/) または [EV テンプレート External Forms 節](../../standard/current/06-ev-template/)に記載。manifest とカバレッジマッピングで logical_id により参照。
- **プロファイル**: 上記プロファイルはオプションの機械可読マッピングを定義し、法的・契約上の義務を課しません。

レベルは [適合性](../../conformance/)、オーバーレイ概要は [最低証拠 — 規制オーバーレイ](../../artifacts/minimum-evidence/) を参照。
