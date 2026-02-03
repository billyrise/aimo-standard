---
description: AIMO 證據包範本和使用指南。使用索引管理和稽核就緒格式記錄 AI 治理證據的結構。
---

# Evidence Pack 範本（EP）

本節定義證據包範本及其使用。證據包是一組文件集合，展示 AI 系統的治理和合規性。

## 命名空間：Evidence Pack 文件類型（EP）與 Taxonomy Log/Event Type（LG）

> **重要**：**EP-01..EP-07** 表示*文件類型*（證據包檔案類型）。**LG-001、LG-002、…** 在[分類法](./03-taxonomy.md)中表示*日誌/記錄類型*（請求記錄、審查/核准記錄等）。**EV-** 專用於 Evidence 成果物 ID。請勿混用：EP 用於包結構，LG 用於生命週期證據分類。

## 關鍵原則：索引和差異管理

重要的不僅是個別提交的內容，而是跨證據項目的**索引**和**差異管理**。

證據包作為索引，將 AI 系統連結到其治理人工產物。價值在於：

1. **可追溯性**：連結跨時間的決策、核准和變更
2. **可稽核性**：使稽核員能夠導覽證據結構
3. **可維護性**：追蹤什麼變更了、何時以及為什麼

## MVP 證據集（EP-01 到 EP-07）

以下七種 **Evidence Pack 文件類型**（EP）形成展示 AI 治理的**最小可行集**。每種為文件範本；分類法 **LG** 代碼（請求記錄、審查/核准等）在包內及 `codes.LG` 中用於對*日誌/記錄*證據進行分類。

| ID | 文件類型 | 用途 |
| --- | --- | --- |
| EP-01 | 系統概述 | 記錄 AI 系統及其用途 |
| EP-02 | 資料流 | 對應資料在系統中的移動 |
| EP-03 | 清冊 | 維護 AI 資產目錄 |
| EP-04 | 風險與影響評估 | 評估並記錄風險 |
| EP-05 | 控制與核准 | 記錄控制和核准記錄 |
| EP-06 | 日誌與監控 | 定義日誌和監控設定 |
| EP-07 | 事件與例外 | 追蹤事件和例外 |

## 證據包清單

每個證據包必須包含一個清單檔案，包含：

### 必要中繼資料

| 欄位 | 說明 | 必要 |
| --- | --- | --- |
| `pack_id` | 唯一識別碼（例如 EP-EXAMPLE-001） | 是 |
| `pack_version` | 套件的 SemVer 版本 | 是 |
| `taxonomy_version` | 使用的 AIMO 分類法版本 | 是 |
| `created_date` | 套件建立日期 | 是 |
| `last_updated` | 最後更新日期 | 是 |
| `owner` | 負責方 | 是 |

### AIMO 代碼（8 維度）

每個證據包必須包含所有 8 個維度的代碼。**LG** 維度列出適用於本包的*分類法*日誌/記錄類型（如請求記錄、審查/核准），而非文件類型代碼。文件類型由 `evidence_files[].file_id`（EP-01..EP-07）給出。

```json
{
  "codes": {
    "FS": ["FS-001"],
    "UC": ["UC-001", "UC-002"],
    "DT": ["DT-002"],
    "CH": ["CH-001"],
    "IM": ["IM-001"],
    "RS": ["RS-001", "RS-003"],
    "OB": ["OB-001"],
    "LG": ["LG-001", "LG-002", "LG-008", "LG-009"]
  }
}
```

### 證據檔案清單

每筆記錄透過 **file_id**（EP-01..EP-07）識別包內文件。可選 **ev_codes** 可列出該文件支援的分類法 LG 代碼（LG-xxx）。

```json
{
  "evidence_files": [
    {
      "file_id": "EP-01",
      "filename": "EP-01_system_overview.md",
      "title": "System Overview",
      "required": true
    }
  ]
}
```

## 範本結構

每個證據範本包含：

1. **必要中繼資料區塊** - pack_id、version、taxonomy_version、日期、owner
2. **AIMO 代碼表** - 所有 8 個維度及適用代碼
3. **內容章節** - 領域特定的文件章節
4. **參照** - 連結到相關證據
5. **修訂歷史** - 變更追蹤

### 範本標頭範例

```markdown
# EP-01: 系統概述

---

## 必要中繼資料

| 欄位 | 值 |
| --- | --- |
| **pack_id** | `EP-EXAMPLE-001` |
| **pack_version** | `0.1.0` |
| **taxonomy_version** | `0.1.0` |
| **created_date** | `2026-01-31` |
| **last_updated** | `2026-01-31` |
| **owner** | `AI Governance Team` |

---

## AIMO 代碼（8 維度）

| 維度 | 代碼 | 標籤 |
| --- | --- | --- |
| **FS** | `FS-001` | 終端使用者生產力 |
| **UC** | `UC-001` | 一般問答 |
| **DT** | `DT-002` | 內部 |
| **CH** | `CH-001` | Web UI |
| **IM** | `IM-001` | 獨立 |
| **RS** | `RS-001` | 資料洩漏 |
| **OB** | `OB-001` | 效率 |
| **LG** | `LG-001`, `LG-002` | 請求記錄、審查/核准記錄 |
```

## 下載

### 範本

清單中請使用 **file_id** EP-01..EP-07；檔案名可為 EP-01_... 或相容的 EV-01_...。

- `source_pack/04_evidence_pack/templates/EV-01_system_overview.md` → file_id **EP-01**
- `source_pack/04_evidence_pack/templates/EV-02_data_flow.md` → file_id **EP-02**
- `source_pack/04_evidence_pack/templates/EV-03_inventory.md` → file_id **EP-03**
- `source_pack/04_evidence_pack/templates/EV-04_risk_impact.md` → file_id **EP-04**
- `source_pack/04_evidence_pack/templates/EV-05_controls_approvals.md` → file_id **EP-05**
- `source_pack/04_evidence_pack/templates/EV-06_logging_monitoring.md` → file_id **EP-06**
- `source_pack/04_evidence_pack/templates/EV-07_incident_exception.md` → file_id **EP-07**

### 結構描述和範例

- 結構描述：`source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json`
- 範例：`source_pack/04_evidence_pack/examples/evidence_pack_manifest.example.json`

請參閱[發布](../../releases/index.md)了解可下載的套件。

## 發布模型

> **注意**：主要發布目標是**稽核公司和系統整合商**（範本發布者），而非個別企業。

範本設計為：

1. 被稽核員和顧問採用為標準人工產物
2. 以保留來源署名的方式發布給企業
3. 與 AIMO 標準一起進行版本控制

企業透過其稽核員、顧問或維護與標準版本連結的內部治理團隊接收範本。

## 參照

- [分類法](./03-taxonomy.md) - 維度定義
- [代碼](./04-codes.md) - 代碼格式
- [驗證器](./07-validator.md) - 驗證規則
- [證據包](../../artifacts/evidence-bundle.md) - 套件結構
