---
description: 調達・開示オーバーレイ（英国、日本）。UK ATRS、英国調達ガイド、日本政府 GenAI 調達・AI ビジネスガイドライン。参照マッピングのみ。
---

# Procurement & Disclosure Overlays (UK, Japan)

本ページは AIMO エビデンスと **英国**・**日本** の調達・開示フレームワークとの**参照マッピング**を記述します。**参照マッピングのみ**であり、AIMO は公式チェックリストや政府ガイドに取って代わるものではありません。

## UK: ATRS and AI procurement

| Topic | AIMO evidence / mapping | Notes |
| --- | --- | --- |
| **UK ATRS** (AI Transparency Record) | Summary, review (accountability owner), evidence (model/system description), dictionary (risk considerations). Profile: `coverage_map/profiles/uk_atrs_procurement.json`. | External Forms で ATRS 型透明性記録を添付または参照；logical_id でバンドルオブジェクトにリンク。 |
| **UK procurement guidance** | Request, review, exception; Evidence Bundle for supplier evaluation. | 調達評価用エビデンスの構造化に AIMO バンドルを使用；公式英国ガイドが権威。 |

## Japan: Government GenAI procurement and AI Business Guidelines

| Topic | AIMO evidence / mapping | Notes |
| --- | --- | --- |
| **JP government GenAI procurement checklist** | External Form としてチェックリストを添付（例: payload: JP_PROCUREMENT_CHECKLIST）；manifest で参照。Profile: `coverage_map/profiles/jp_gov_genai_procurement.json`. | 参照マッピングのみ；AIMO は公式チェックリストに取って代わらない。 |
| **AI Business Guidelines** | Summary, dictionary；チェックリスト項目を AIMO タクソノミーコードにマッピング。 | 説明可能性用；公式日本ガイドで確認。 |

## How to use

- **External Forms**: 英国・日本の公式テンプレート/チェックリストを**そのまま**（PDF, DOC 等）添付し、ハッシュを記録し、Evidence Bundle の [payload_index](../../standard/current/09-evidence-bundle-structure/) または [EV Template External Forms section](../../standard/current/06-ev-template/) に列挙。manifest とカバレッジマッピングで logical_id により参照。
- **Profiles**: 上記プロファイルは任意の機械可読マッピングを定義し、法的・契約上の義務を課さない。

[Conformance](../../conformance/) のレベルと [Minimum Evidence — Regulatory overlays](../../artifacts/minimum-evidence/) のオーバーレイ概要を参照。
