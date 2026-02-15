---
description: AIMO Standard 與歐盟 AI 法的對應。AIMO 分類代碼與歐盟 AI 法風險類別及要求之間的可追溯性。
---
<!-- aimo:translation_status=translated -->

# 歐盟 AI 法對應

> 可追溯性捷徑：分類法 → 最低證據 → 驗證器 → 人工監督協議。

- [分類法](../../standard/current/03-taxonomy/)
- [最低證據要求](../../artifacts/minimum-evidence/)
- [日誌結構描述](../../artifacts/log-schemas/)
- [驗證器](../../validator/)
- [人工監督協議](../../governance/human-oversight-protocol/)

本頁將選定的歐盟 AI 法主題（文件、紀錄保存、風險管理、人工監督、透明度）對應至 AIMO 證據與人工產物。僅為高階對應，**不**構成法律意見或保證符合。請對照正式法律文本驗證。

**參考：** 規則 (EU) 2024/1689（人工智慧法）。下列條號均指該規則。

## 對應表

| 框架參照／主題 | AIMO 證據／在 AIMO 中的位置 | 證據包／最低證據 | 人工產物與驗證 | 備註 |
| --- | --- | --- | --- | --- |
| 第 4 條 – AI 素養 | [範圍](../../standard/current/02-scope/) | Summary、EV；review | templates/ev/ | 跨領域；組織能力／培訓證據（高階）。非法律意見。請對照官方文本驗證。 |
| 第 9 條 – 風險管理系統 | [範圍](../../standard/current/02-scope/) | request、review、exception、renewal | templates/ev/ | 高風險 AI 系統（第三章）。非法律意見。請對照官方文本驗證。 |
| 第 10 條 – 資料與資料治理 | [字典](../../standard/current/05-dictionary/) | Dictionary、EV | schemas/jsonschema/；schema_validate_dictionary | 非法律意見。請對照官方文本驗證。 |
| 第 11 條 – 技術文件（高風險） | [EV 範本](../../standard/current/06-ev-template/)、[證據包](../../artifacts/evidence-bundle/) | EV、Dictionary、Summary；request、review | schemas/jsonschema/、templates/ev/；**附件 IV**：見 [範例 > EU 附件 IV 範例](../../examples/)（`examples/evidence_bundle_v01_annex_iv_sample/`）；設定檔：`coverage_map/profiles/eu_ai_act_annex_iv.json`。範例組合符合規範（signatures/、hashes/、具附件 IV 導向技術文件之 payload）。詳見範例（更多範例內容於後續版本提供）。 | 僅高階；非法律意見。請對照官方文本驗證。 |
| 第 12 條 – 紀錄保存 | [證據包](../../artifacts/evidence-bundle/)、[最低證據](../../artifacts/minimum-evidence/) | EV、change_log、request、review | examples/evidence_bundle_minimal/；schema_validate_ev | 非法律意見。請對照官方文本驗證。 |
| 第 13 條 – 對部署者／使用者的透明度與資訊提供 | [範圍](../../standard/current/02-scope/) | Summary、EV；review | templates/ev/ | 高風險情境。非法律意見。請對照官方文本驗證。 |
| 第 14 條 – 人工監督 | [最低證據](../../artifacts/minimum-evidence/) | review、exception | templates/ev/ev_template.md | 非法律意見。請對照官方文本驗證。 |
| 第 15 條 – 準確性、穩健性、資安 | [最低證據](../../artifacts/minimum-evidence/) | EV（證據代碼／風險代碼，高階） | templates/ev/ | 僅高階對應。非法律意見。請對照官方文本驗證。 |
| 第 17 條 – 品質管理系統 | [範圍](../../standard/current/02-scope/) | Summary、review（組織流程） | templates/ev/ | 與第 9 條（風險管理系統）有別。非法律意見。請對照官方文本驗證。 |
| 透明度義務（依使用情境） | [範圍](../../standard/current/02-scope/)、[最低證據](../../artifacts/minimum-evidence/) | Summary、EV；review | templates/ev/ | 適用規定依使用情境（如有限風險、部署者義務）而異。非法律意見。請對照官方文本驗證。 |
| GPAI 模型義務 | [EV 範本](../../standard/current/06-ev-template/)、[證據包](../../artifacts/evidence-bundle/) | EV 範本、證據包（證據結構化架構） | schemas/jsonschema/；schema_validate_ev | AIMO 提供組織證據的架構；實際義務由規則界定。非法律意見。請對照官方文本驗證。 |
| 前言 – 問責 | [證據包](../../artifacts/evidence-bundle/) | EV、request、review、change_log | examples/evidence_bundle_minimal/；schema_validate_ev | 非法律意見。請對照官方文本驗證。 |

## 生效日／適用範圍（高階）

以下對齊**歐盟官方時程**（AI 法服務台／執委會）。**非法律意見**，亦不保證正確性。請一律以**正式法律文本**及主管機關為準。

| 階段 | 日期 | 適用內容（高階） |
| --- | --- | --- |
| 生效 | 2024 年 8 月 | 規則已生效；多數實體義務尚未適用。 |
| 一般規定與禁止 | 2025 年 2 月 2 日 | 禁止作法（不可接受風險）；部分與 AI 素養相關規定。 |
| GPAI 規則與治理 | 2025 年 8 月 2 日 | 指定機構、GPAI、治理、保密、罰則；行為準則。 |
| 多數規則 + 附件 III 高風險 + 第 50 條透明度 | 2026 年 8 月 2 日 | 高風險 AI 系統（附件 III）全面適用、第 50 條透明度義務。 |
| 納入受管制產品之高風險 | 2027 年 8 月 2 日 | 受歐盟產品法規規範之產品內嵌高風險 AI 系統。 |

## 調和標準與推定符合（第 40 條）

依 AI 法在歐盟公報公布**調和標準**後，符合該標準可對相關要求產生**推定符合**。確切清單與日期依標準化工作與公報公布而定。AIMO 對應僅供參考，不授予推定符合。現行狀態請見下方**參考資料**之執委會與 AI 辦公室來源。

## 2026 年 AI 辦公室指引（實務細節）

歐洲執委會表示**AI 辦公室**將於 2026 年擬定**實務指引**，包括：

- 高風險分類
- 第 50 條（透明度）實施
- 事件通報
- 與 QMS 相關要素

上述指引為 AIMO 設定檔與對應圖的**更新觸發**：公布後，採用者應使證據與對應與最新官方指引一致。AIMO 不詮釋亦不保證符合該指引。

!!! warning "非法律意見"
    本頁僅供說明。您必須依正式規則及任何施行或修正法案驗證適用性與日期。AIMO 不提供法律意見亦不保證符合。

## 參考資料

- [規則 (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689)（EUR-Lex）— 人工智慧法
- [歐盟 AI 法實施時程](https://artificialintelligenceact.eu/implementation-timeline)（AI 法服務台／執委會對齊；參考用）
- 歐洲執委會／AI 辦公室 — 指引與時程（請以執委會新聞與 AI 法服務台查詢最新 URL）
- [EPRS — 歐盟 AI 法實施](https://www.europarl.europa.eu/thinktank/) — 議會簡報（參考用）
