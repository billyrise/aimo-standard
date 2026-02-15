---
description: AIMO 最低證據要求。依生命週期（申請、審查、核准、變更、更新）劃分的 MUST 級清單，用於 AI 治理證據就緒。
---
<!-- aimo:translation_status=translated -->

# 最低證據要求（Minimum Evidence Requirements）

本頁為面向稽核方與實作方的**最低證據要求**清單，依生命週期分組定義 MUST 級最低證據要求，用以支援可解釋性與證據就緒；不提供法律意見亦不保證合規。

準備或審查提交物時，請與 [Evidence Bundle](../evidence-bundle/) 及 [Validator](../../standard/current/07-validator/) 一併使用本頁。

## 1) 申請（Request）

- **MUST 欄位**：識別碼、時間戳記、執行者/角色、範圍（申請內容）、理由（rationale）。
- **MUST 關聯**：審查及記錄使用的 EV 項須可引用申請 id。
- **證明內容**：使用在核准與實施前已申請並劃定範圍。

## 2) 審查 / 核准（Review / Approval）

- **MUST 欄位**：識別碼、時間戳記、執行者/角色、決定（核准/拒絕/有條件）、範圍、理由、對申請的引用。
- **MUST 關聯**：EV 及後續例外或更新須可引用審查 id。
- **證明內容**：在使用（或例外）前已進行規定的審查與核准。

## 3) 例外（Exception）

- **MUST 欄位**：識別碼、時間戳記、範圍、到期（或截止日）、補償性控制、理由、對審查/申請的引用。
- **MUST 關聯**：例外 → 補償性控制；例外 → 到期；例外 → 更新（再評估到期時）。
- **證明內容**：偏離有時限、具備補償性控制並與更新關聯。

## 4) 更新 / 再評估（Renewal / Re-evaluation）

- **MUST 欄位**：識別碼、時間戳記、執行者/角色、決定（續期/撤銷/有條件）、對先前例外/申請/審查/EV 的引用。
- **MUST 關聯**：更新引用被續期的例外或核准；EV 項可引用更新 id。
- **證明內容**：例外與核准依既定基準再評估並續期或撤銷。

## 5) 變更日誌（Change Log）

- **MUST 欄位**：識別碼、時間戳記、執行者/角色、變更說明、引用（如受影響的 EV、申請、審查、例外、更新）。
- **MUST 關聯**：變更日誌條目引用其修改或觸發的產物。
- **證明內容**：對套件或其內容的變更已記錄且可追溯。

## 6) 完整性與存取（Integrity & Access）

證據完整性與存取控制對稽核依賴至關重要。AIMO 不規定具體技術控制，採用方應文件化如何滿足這些預期。

### 存取控制指南

| 面向 | 指南 |
| --- | --- |
| **角色型存取** | 定義角色（如證據建立者、審查者、稽核員、管理員）並文件化誰可建立、讀取、更新或刪除證據。 |
| **最小權限** | 僅授予必要最小存取；寫入權限限於授權人員。 |
| **存取日誌** | 為稽核線索記錄存取事件（誰、何時、何事）。 |
| **職責分離** | 在可行範圍內將證據建立與核准角色分離。 |

### 保留指南

| 面向 | 指南 |
| --- | --- |
| **保留期** | 依法規要求與組織政策（如財務稽核 5–7 年）定義並文件化保留期。 |
| **保留排程** | 維護排程，說明保留哪些證據、保留多久、何時可處置。 |
| **訴訟保留** | 支援在訴訟或調查中暫停正常保留/刪除的流程。 |

### 不可竄改選項

| 選項 | 說明 |
| --- | --- |
| **密碼學雜湊** | 為證據檔案產生 SHA-256（或更強）雜湊；單獨儲存雜湊以供驗證。 |
| **WORM 儲存** | 對證據歸檔使用一次寫入多次讀取（WORM）儲存以防竄改。 |
| **僅附加日誌** | 使用僅附加稽核日誌進行變更追蹤。 |
| **數位簽章** | 對證據套件簽章以證明來源並偵測竄改。 |

### 稽核線索預期

| 要素 | 需文件化內容 |
| --- | --- |
| **變更日誌** | 記錄誰在何時因何變更了何內容（見 Change Log 生命週期群組）。 |
| **存取日誌** | 記錄誰在何時以何目的存取證據。 |
| **系統日誌** | 保留支援證據完整性主張的相關系統日誌（認證、授權）。 |
| **驗證記錄** | 文件化定期完整性驗證（雜湊核對、稽核審查）。 |

### 證明內容

- **證據已保全**：雜湊、WORM、簽章等完整性機制表明證據未被竄改。
- **存取受控**：存取日誌與角色定義表明誰有存取權及最小權限已落實。
- **支援稽核依賴**：綜合上述要素使稽核方對證據可靠性有信心。

### 建議運行設定

依風險承受度與法規要求選擇設定；僅為建議，非強制。

| 面向 | 輕量 | 標準 | 嚴格 |
| --- | --- | --- | --- |
| **用途** | 內部試點、低風險 AI | 生產系統、中等風險 | 受監管產業、高風險 AI |
| **保留期** | 1–2 年 | 5–7 年 | 7–10+ 年或法規最低 |
| **不可竄改** | SHA-256 雜湊 | SHA-256 + 僅附加日誌 | WORM 儲存 + 數位簽章 |
| **存取控制** | 角色型（基礎） | 角色型 + 存取日誌 | 職責分離 + 完整稽核線索 |
| **稽核線索** | 僅變更日誌 | 變更日誌 + 存取日誌 | 完整系統日誌 + 定期驗證 |
| **驗證頻率** | 依需求 | 季 | 月或持續 |
| **Validator 使用** | 選用 | 提交前必須 | 必須 + 自動化 CI 檢查 |

!!! note "保留期為示例"
    所示保留期僅為示例。組織須依適用法律、契約、產業要求及內部政策決定保留期。

!!! tip "如何選擇"
    - **輕量**：適用於實驗、內部工具或正式稽核可能性低的低風險情境。
    - **標準**：適用於多數生產部署，可能接受稽核但非持續。
    - **嚴格**：適用於受監管產業（金融、醫療、政府）或風險影響顯著的 AI 系統。

## 重要說明

本最低集支援可解釋性與證據就緒；本身不提供法律意見亦不保證合規。

套件結構與 TOC 見 [Evidence Bundle](../evidence-bundle/)；欄位級對齊見 [EV Template](../../standard/current/06-ev-template/) 與 schemas。[Log Schemas](../log-schemas/) 為 Shadow AI 發現與代理活動證據的規範化日誌格式。

## 法規疊加（參考）

以下**疊加**描述在特定法規或採購情境中常被要求的額外證據，僅供**參考**；請將官方範本/清單原樣附於 EV Template 的 [External Forms 節](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is)，並在 manifest 中以 logical_id 引用。

| 疊加 | 通常預期的額外產物 | 附於 | 設定（選用） |
| --- | --- | --- | --- |
| **EU 高風險** | 風險管理、技術文件（Annex IV）、日誌、人類監督、透明性（Art 50）、事件通報 | payload_index；Evidence Bundle + Annex IV 設定 | `eu_ai_act_annex_iv.json`、`eu_ai_act_high_risk.json` |
| **EU GPAI CoP** | Model Documentation Form（透明性、著作權、安全與保障） | External Forms；logical_id 如 GPAI_MODEL_DOC_FORM | `eu_gp_ai_cop.json` |
| **NIST GenAI** | GenAI 設定產物（模型適配、評估、監測） | payload_index；change_log；External Forms / GenAI 記錄 | `nist_ai_600_1_genai.json` |
| **UK ATRS / 採購** | ATRS 透明性記錄、課責負責人、採購評估說明 | External Forms；Summary、review | `uk_atrs_procurement.json` |
| **JP 採購** | 政府 GenAI 採購清單、AI 商業指南清單 | External Forms；logical_id 如 JP_PROCUREMENT_CHECKLIST | `jp_gov_genai_procurement.json` |

設定檔名格式為 `coverage_map/profiles/<target>_<purpose>.json`，均含 `target_version`。英國與日本見 [Coverage Map — Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/)；EU 與 NIST 見 [EU AI Act](../../coverage-map/eu-ai-act/) 與 [NIST AI RMF](../../coverage-map/nist-ai-rmf/)。
