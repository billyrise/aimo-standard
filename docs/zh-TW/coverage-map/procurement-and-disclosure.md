---
description: 採購與揭露疊加（英國、日本）。英國 ATRS、英國採購指引、日本政府 GenAI 採購與 AI 商業指引。僅為參考對應。
---
<!-- aimo:translation_status=translated -->

# 採購與揭露疊加（英國、日本）

本頁說明 AIMO 證據與選定**英國**及**日本**採購與揭露架構之間的**參考對應**。旨在**透過複用 AIMO 證據減輕負擔**。僅為**參考對應**；AIMO 不保證完全滿足政府要求。請對照下列官方來源驗證。

## 主要來源

**英國**

- [Algorithmic Transparency Recording Standard (ATRS) Hub](https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub) — GOV.UK（範本、指引、已發布紀錄）
- [ATRS 範本](https://www.gov.uk/government/publications/algorithmic-transparency-template) — 公共部門官方範本
- [使用 ATRS 的組織指引](https://www.gov.uk/government/publications/guidance-for-organisations-using-the-algorithmic-transparency-standard/algorithmic-transparency-recording-standard-guidance-for-public-sector-bodies) — GOV.UK

**日本**

- [數位廳 — GenAI 採購與利用指引](https://www.digital.go.jp/news/3579c42d-b11c-4756-b66e-3d3e35175623) — 數位廳（內閣官房）
- [AI 商業指引](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/index.html) — 經濟產業省／總務省

## 對應表（英國）

| 政府要求（主題） | AIMO 人工產物 | 在 Evidence Bundle 中的位置 | 驗證器覆蓋 | 備註 |
| --- | --- | --- | --- | --- |
| ATRS — 問責／負責人 | Summary、review | manifest；objects／（EV、Summary）；payload_index | schema_validate_ev | 參考對應；不保證完全符合。 |
| ATRS — 系統／模型描述 | Dictionary、EV | objects／；schemas/jsonschema/aimo-dictionary.schema.json | schema_validate_dictionary | 於外部表單附上正式 ATRS 紀錄；以 logical_id 連結。 |
| ATRS — 風險考量 | Dictionary、request、review、exception | objects／；templates/ev/ | schema_validate_ev | 設定檔：`coverage_map/profiles/uk_atrs_procurement.json`。 |
| 採購 — 供應商證據 | request、review、exception；Evidence Bundle | manifest、object_index、payload_index；examples/evidence_bundle_minimal/ | schema_validate_ev | 以組合結構化證據；英國正式指引仍為權威。 |

## 對應表（日本）

| 政府要求（主題） | AIMO 人工產物 | 在 Evidence Bundle 中的位置 | 驗證器覆蓋 | 備註 |
| --- | --- | --- | --- | --- |
| GenAI 採購檢查表（數位廳） | 外部表單（檢查表原文）；Dictionary、Summary | payload_index；外部表單節；manifest 參照 | N/A（附件） | 參考對應；不保證完全符合。設定檔：`coverage_map/profiles/jp_gov_genai_procurement.json`。 |
| AI 商業指引 — 治理／可追溯性 | Summary、dictionary、request、review、change_log | objects／；manifest；templates/ev/ | schema_validate_dictionary、schema_validate_ev | 在有利於可追溯性時將清單項目對應至 AIMO 分類法。 |
| 風險／責任文件 | Dictionary、EV、review、exception | objects／；schemas/jsonschema/ | schema_validate_ev | 請對照數位廳與經產省／總務省正式指引驗證。 |

## 英國：ATRS 與 AI 採購（摘要）

| 主題 | AIMO 證據／對應 | 備註 |
| --- | --- | --- |
| **英國 ATRS**（AI 透明度紀錄） | Summary、review（問責負責人）、evidence（模型／系統描述）、dictionary（風險考量）。設定檔：`coverage_map/profiles/uk_atrs_procurement.json`。 | 於外部表單附上或參照 ATRS 式透明度紀錄；以 logical_id 連結組合物件。 |
| **英國採購指引** | Request、review、exception；以證據包供供應商評鑑。 | 以 AIMO 組合結構化證據供採購評鑑；正式英國指引仍為權威。 |

## 日本：政府 GenAI 採購與 AI 商業指引（摘要）

| 主題 | AIMO 證據／對應 | 備註 |
| --- | --- | --- |
| **日本政府 GenAI 採購檢查表** | 將檢查表作為外部表單附上（例如 payload：JP_PROCUREMENT_CHECKLIST）；於 manifest 中參照。設定檔：`coverage_map/profiles/jp_gov_genai_procurement.json`。 | 僅參考對應；AIMO 不取代正式檢查表。 |
| **AI 商業指引** | Summary、dictionary；在有利於可追溯性時將檢查表項目對應至 AIMO 分類代碼。 | 供可解釋性使用；請對照日本正式指引驗證。 |

## 使用方式

- **外部表單**：將英國或日本正式範本／檢查表**原樣**附上（PDF、DOC 等），進行雜湊，並列於證據包 [payload_index](../../standard/current/09-evidence-bundle-structure/) 或 [EV 範本外部表單章節](../../standard/current/06-ev-template/)。於 manifest 與對應圖中以 logical_id 參照。
- **設定檔**：上列設定檔定義選用的機器可讀對應；不施加法律或契約義務。

級別請見 [符合性](../../conformance/)；疊加摘要請見 [最低證據 — 法規疊加](../../artifacts/minimum-evidence/)。
