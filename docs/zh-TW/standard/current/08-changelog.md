---
description: AIMO 標準變更日誌和版本政策。記錄版本歷史、語意化版本規則，以及發布之間的遷移指引。
---

# 變更日誌

本節記錄 AIMO 標準的版本政策和變更歷史。

## 版本政策

AIMO 標準遵循[語意化版本控制](https://semver.org/)（SemVer）：

### 版本格式：MAJOR.MINOR.PATCH

| 變更類型 | 版本提升 | 範例 |
| --- | --- | --- |
| **MAJOR** | X.0.0 | 破壞性結構描述變更、代碼移除、必要欄位變更 |
| **MINOR** | 0.X.0 | 新代碼、新選用欄位、新維度（選用） |
| **PATCH** | 0.0.X | 文件修復、定義澄清、驗證器錯誤修復 |

### 破壞性與相容變更

**破壞性變更（MAJOR）：**

- 移除代碼（在棄用期之後）
- 結構描述中必要欄位的變更
- 使現有文件無效的結構變更
- 代碼格式模式的變更

**向後相容變更（MINOR）：**

- 向現有維度新增代碼
- 向結構描述新增選用欄位
- 新增選用維度
- 新增證據範本

**非破壞性變更（PATCH）：**

- 文件更正
- 現有定義的澄清
- 翻譯改進
- 驗證器錯誤修復

## 棄用政策

### 棄用流程

1. **標記為已棄用**：代碼或功能標記為 `status: deprecated` 和 `deprecated_in: X.Y.Z`
2. **棄用期**：移除前至少必須經過一個 MINOR 版本
3. **提供替代**：如適用，`replaced_by` 指示替代
4. **在 MAJOR 中移除**：移除在下一個 MAJOR 版本發生

### 範例生命週期

```
v0.0.1: FS-007 引入 (status: active)
v0.1.0: FS-007 棄用 (status: deprecated, replaced_by: FS-008)
v0.2.0: FS-007 仍可用並顯示棄用警告
v1.0.0: FS-007 移除 (status: removed)
```

### 使用已棄用的代碼

- 已棄用的代碼對驗證仍然有效
- 驗證器應對已棄用的代碼發出警告
- 新實作應使用替代代碼
- 現有文件可以繼續使用已棄用的代碼直到遷移

## 發布人工產物

每個官方發布包含：

| 人工產物 | 說明 |
| --- | --- |
| 版本化網站快照 | `https://standard.aimoaas.com/0.0.1/` |
| PDF 規格 | `trust_package.pdf` |
| 資產套件（ZIP） | 結構描述、範本、字典 |
| 校驗和 | 完整性的 SHA-256 雜湊 |
| 變更日誌 | 本文件 |

## 變更歷史

### 未發布（命名空間與規範修正）

**摘要：** 解決 EV 代碼衝突，明確 EV（索引）與 Evidence Pack（payload）關係，強化 /dev 防稽核誤引用。Evidence Pack 文件類型：EP-01..EP-07；Taxonomy EV 保留為事件類型。EV↔Evidence Pack 規範關係已文件化。/dev 增加橫幅與 canonical。

### 版本 0.0.1 (2026-02-02)

**摘要：**AIMO 標準的初始發布，包含 8 維度代碼系統、證據包範本和全面的治理文件。

#### 新增

**代碼系統（8 維度）**

| 維度 | 新增的代碼 | 說明 |
| --- | --- | --- |
| FS | FS-001 到 FS-006 | 功能範圍 |
| UC | UC-001 到 UC-010 | 使用案例類別 |
| DT | DT-001 到 DT-008 | 資料類型 |
| CH | CH-001 到 CH-006 | 通道 |
| IM | IM-001 到 IM-005 | 整合模式 |
| RS | RS-001 到 RS-005 | 風險面 |
| OB | OB-001 到 OB-005 | 成果 / 效益 |
| EV | EV-001 到 EV-007 | 證據類型 |

**結構描述**

- `taxonomy_pack.schema.json`：分類套件定義
- `changelog.schema.json`：變更日誌條目
- `evidence_pack_manifest.schema.json`：證據包清單
- `shadow-ai-discovery.schema.json`：Shadow AI 發現證據
- `agent-activity.schema.json`：代理活動證據

**證據包範本（MVP）**

- EV-01：系統概述
- EV-02：資料流
- EV-03：AI 清冊
- EV-04：風險與影響評估
- EV-05：控制與核准
- EV-06：日誌與監控
- EV-07：事件與例外處理

**文件**

- 具有 8 維度定義的分類法文件
- 代碼系統格式規格
- 字典 CSV 格式規格
- 版本控制和變更政策
- 驗證器 MVP 要求
- 人工監督協議
- 覆蓋範圍對應（ISO 42001、NIST AI RMF、歐盟 AI 法案、ISMS）
- 信任套件

#### 向後相容性

這是初始發布；無向後相容性問題。

---

## 機器可讀變更日誌

機器可讀變更日誌可在以下位置取得：

- `changelog/changelog.json`

此檔案遵循 `changelog.schema.json` 結構描述，可以程式化解析。

## 參照

- [分類法](./03-taxonomy.md) - 維度定義
- [字典](./05-dictionary.md) - 代碼字典
- [版本政策](../../governance/index.md) - 版本政策（請參閱儲存庫根目錄的 VERSIONING.md）
