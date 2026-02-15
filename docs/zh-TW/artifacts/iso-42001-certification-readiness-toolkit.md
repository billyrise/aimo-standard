---
description: ISO/IEC 42001 認證就緒工具包。使用 AIMO 產物與 ISO 42001 對齊的稽核就緒證據的最短路徑。僅支援就緒；不授予認證。
---
<!-- aimo:translation_status=translated -->

# ISO/IEC 42001 認證就緒工具包

本頁為使用 AIMO 產物產出與 **ISO/IEC 42001** 對齊的**稽核就緒證據**的**實務與採用導向**指南。旨在**支援就緒**，**不**授予認證。認證決定由**認可認證機構**作出。

## 目標

產出經驗證器檢查的、支援 ISO/IEC 42001 型控制（情境、領導、規劃、支援、運作、績效評估、改進）的 Evidence Bundle，使稽核方能高效定位並驗證證據。

## 五步工作流

| 步驟 | 行動 |
| --- | --- |
| **1. 確定範圍與 AI 清單** | 用 scope_ref 定義範圍；使用 [分類法](../../standard/current/03-taxonomy/) 與 [字典](../../standard/current/05-dictionary/) 對 AI 系統分類。 |
| **2. 建立管理體系產物** | 建立或引用政策、角色及與 PDCA 對齊的產物。以 [AIMO-MS / AIMO-Controls](../../conformance/) 為結構；參照 [Evidence Pack 範本](../../standard/current/06-ev-template/)（EP-01..EP-07）。 |
| **3. 產出 Evidence Bundle 與最低證據** | 依 [Evidence Bundle 結構](../../standard/current/09-evidence-bundle-structure/) 建構 manifest、object_index、payload_index、hash_chain、signing。依 [最低證據要求](minimum-evidence.md) 包含 request、review、exception、renewal、change_log。 |
| **4. 執行驗證器 + 校驗和 + 變更控制** | 執行 `python validator/src/validate.py <bundle_path> --validate-profiles`。記錄驗證器版本與輸出。產生 SHA-256 校驗和；維護引用受影響物件的 change log。 |
| **5. 準備稽核包** | 將套件打包（zip 等）；提供校驗和。可選附上 [稽核報告輸出](../../standard/current/07-validator/)（audit-json / audit-html）。引用標準時使用帶版本 URL（如 `/0.1.2/`）。Audit-Ready 級別增加 [Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index) 與 [External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is)。 |

## 清單：ISO 42001 條款族 → AIMO 產物 → 證據輸出

| ISO 42001 條款族 | AIMO 產物 | 證據輸出 |
| --- | --- | --- |
| 情境 (4.1) | Summary、Dictionary、scope_ref | manifest scope_ref；Summary；Dictionary |
| 領導/方針 (5.x) | Summary、review、dictionary | 審查記錄；方針引用 |
| 規劃 (6.x) | request、review、exception、EV、Dictionary | 申請/核准；EV 或 Dictionary 中的風險/目標 |
| 支援 (7.x) | Summary、review、EV、change_log | 文件；能力/意識證據 |
| 運作 (8.x) | EV、request、review、exception | 運作控制；適用性 |
| 績效評估 (9.x) | EV、change_log、review、renewal | 監測；內審；管理審查 |
| 改進 (10.x) | exception、renewal、change_log | 矯正措施；持續改進 |

參見 [Coverage Map — ISO/IEC 42001](../../coverage-map/iso-42001/) 與 [ISO/IEC 42006](https://www.iso.org/standard/42006) 了解稽核機構預期。

## 穩妥表述

- **宜用**：「我們使用 AIMO 產物支援 ISO/IEC 42001 就緒；認證決定由認可認證機構作出。」
- **勿用**：「經 AIMO 認證符合 ISO 42001」或「AIMO 認證合規」。

## 相關

- [符合性](../../conformance/) — 級別（Foundation、Operational、Audit-Ready）與聲明用語
- [Trust Package](../../governance/trust-package/) — 面向稽核方的材料
- [Responsibility Boundary](../../governance/responsibility-boundary/) — AIMO 提供與不提供的內容
