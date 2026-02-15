---
description: 採購與揭露疊加（英國、日本）。英國 ATRS、英國採購指引、日本政府 GenAI 採購與 AI 商業指引。僅為參考對應。
---
<!-- aimo:translation_status=translated -->

# 採購與揭露疊加（英國、日本）

本頁說明 AIMO 證據與選定**英國**及**日本**採購與揭露架構之間的**參考對應**。僅為**參考對應**；AIMO 不取代正式檢查表或政府指引。

## 英國：ATRS 與 AI 採購

| 主題 | AIMO 證據／對應 | 備註 |
| --- | --- | --- |
| **英國 ATRS**（AI 透明度紀錄） | Summary、review（問責負責人）、evidence（模型／系統描述）、dictionary（風險考量）。設定檔：`coverage_map/profiles/uk_atrs_procurement.json`。 | 於外部表單附上或參照 ATRS 式透明度紀錄；以 logical_id 連結組合物件。 |
| **英國採購指引** | Request、review、exception；以證據包供供應商評鑑。 | 以 AIMO 組合結構化證據供採購評鑑；正式英國指引仍為權威。 |

## 日本：政府 GenAI 採購與 AI 商業指引

| 主題 | AIMO 證據／對應 | 備註 |
| --- | --- | --- |
| **日本政府 GenAI 採購檢查表** | 將檢查表作為外部表單附上（例如 payload：JP_PROCUREMENT_CHECKLIST）；於 manifest 中參照。設定檔：`coverage_map/profiles/jp_gov_genai_procurement.json`。 | 僅參考對應；AIMO 不取代正式檢查表。 |
| **AI 商業指引** | Summary、dictionary；在有利於可追溯性時將檢查表項目對應至 AIMO 分類代碼。 | 供可解釋性使用；請對照日本正式指引驗證。 |

## 使用方式

- **外部表單**：將英國或日本正式範本／檢查表**原樣**附上（PDF、DOC 等），進行雜湊，並列於證據包 [payload_index](../../standard/current/09-evidence-bundle-structure/) 或 [EV 範本外部表單章節](../../standard/current/06-ev-template/)。於 manifest 與對應圖中以 logical_id 參照。
- **設定檔**：上列設定檔定義選用的機器可讀對應；不施加法律或契約義務。

級別請見 [符合性](../../conformance/)；疊加摘要請見 [最低證據 — 法規疊加](../../artifacts/minimum-evidence/)。
