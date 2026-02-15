---
description: AIMO 證據包結構。包含目錄、可追溯性和人工產物的稽核套件格式，用於 AI 治理合規性和稽核員交付。
---
<!-- aimo:translation_status=translated -->

# 證據包

**證據包**是一個稽核套件：一組結構化的人工產物，支援 AI 治理的可解釋性和可追溯性。它不是產品功能，而是為稽核員和合規性提供的交付格式。

## 套件結構和命名

- **套件根目錄命名**：使用一致的模式，例如 `{org}_{system}_{period}_{version}`（例如 `acme_ai-usage_2026-Q1_v1`）。
- **必要檔案**：至少一組符合 [Evidence Pack 範本（EP）](../../standard/current/06-ev-template/) 的證據（EV）集、一份[字典](../../standard/current/05-dictionary/)、一份簡短的**摘要**（套件的執行摘要）和一份**變更日誌**（或其參考）用於記錄套件或其內容的變更。
- **選用附件**：日誌、審查記錄、例外核准、續期記錄；保持命名一致且可從主要 EV/字典中參照。

## 目錄（TOC）

| 章節 | 人工產物 | 是否必要？ | 用途 | 最少欄位 | 驗證 |
| --- | --- | --- | --- | --- | --- |
| 證據 | EV 記錄（JSON/陣列） | 是 | 記錄發生的事情；連結到請求/審查/例外/續期 | id、timestamp、source、summary；選用生命週期參照 | [驗證器](../../validator/)、aimo-ev.schema.json |
| 字典 | dictionary.json | 是 | 代碼和維度的鍵/標籤/說明 | entries（key、label、description） | aimo-dictionary.schema.json |
| 摘要 | summary（文件或欄位） | 是 | 為稽核員提供的單頁概述 | scope、period、key decisions、exceptions | — |
| 變更日誌 | change_log 或參照 | 是 | 套件/內容變更的稽核軌跡 | id、timestamp、actor、change description、references | — |
| 請求 | request 記錄 | 如適用 | 使用申請/請求 | id、timestamp、actor/role、scope、rationale | — |
| 審查/核准 | review 記錄 | 如適用 | 審查和核准結果 | id、timestamp、actor/role、decision、references | — |
| 例外 | exception 記錄 | 如適用 | 包含補償控制和到期日的例外 | id、timestamp、scope、expiry、compensating controls、renewal ref | — |
| 續期 | renewal 記錄 | 如適用 | 重新評估和續期 | id、timestamp、actor/role、decision、references to prior exception/EV | — |

## 規範關係：EV 記錄（索引）與 Evidence Pack（payload）

為避免雙重建構與稽核歧義，以下為**規範**：(1) EV 記錄（JSON）為**索引/台帳**（可機器驗證的可追溯性）。(2) Evidence Pack 檔案（EP-01..EP-07 及清單）為 **payload**。(3) EV 記錄應透過 `evidence_file_ids`（如 EP-01）及/或雜湊參照 payload；[Validator](../../validator/) 檢查參照完整性。(4) **最小提交集**：EV JSON + Dictionary + Summary + Change Log + Evidence Pack（zip）。參見 [Evidence Pack 範本](../../standard/current/06-ev-template/) 了解 EP-01..EP-07 文件類型。

## 可追溯性

- **穩定 ID**：每筆記錄（EV、request、review、exception、renewal、change log entry）都必須具有穩定、唯一的識別碼。
- **交叉參照**：連結 Request → Review → Exception（如有）→ Renewal，並透過參照欄位（例如 `request_id`、`review_id`、`exception_id`、`renewal_id`）將 EV 項目連結到這些記錄。
- **連結**：確保稽核員可以追蹤從 AI 使用（或例外）到請求、核准、任何例外及其補償控制和到期日、以及續期的完整鏈條。

## 稽核員如何使用

稽核員使用證據包來驗證 AI 使用是否經過請求、審查和核准；例外是否有時限且具有補償控制和續期；以及變更是否已記錄。目錄和可追溯性規則讓他們能夠找到所需的人工產物，並追蹤跨請求、審查、例外、續期和 EV 記錄的 ID 和參照。摘要提供快速概覽；變更日誌支援變更控制和問責制。

請參閱[最低證據要求](../minimum-evidence/)以了解必要層級欄位和生命週期群組。

## 營運指引

!!! info "完整性和存取控制"
    雖然 AIMO 不規定特定的控制措施，但採用者應記錄：
    
    - **存取角色**：誰可以建立、讀取、更新或刪除證據
    - **保留政策**：證據保留多長時間以及按照什麼時程
    - **完整性機制**：使用的雜湊、WORM 儲存或數位簽章
    - **稽核軌跡**：套件存取和變更的日誌
    
    請參閱[最低證據要求 > 完整性與存取](../minimum-evidence/#6-integrity-access)以獲取詳細指引。

## 稽核旅程

從本頁面開始，典型的稽核旅程繼續如下：

1. **下一步**：[最低證據要求](../minimum-evidence/) — 按生命週期的必要層級檢查清單
2. **然後**：[覆蓋範圍對應](../../coverage-map/) — 對應到外部框架
3. **驗證**：[驗證器](../../validator/) — 執行結構檢查
4. **下載**：[發布](../../releases/) — 取得發布資產並驗證校驗和
