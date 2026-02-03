---
description: AIMO 驗證器 - 確保證據包符合 AIMO 標準結構描述。驗證規則、錯誤處理，以及合規性檢查的參考實作。
---

# 驗證器

AIMO 驗證器確保證據包和相關人工產物符合 AIMO 標準結構描述和要求。

另請參閱：[人工監督協議](../../governance/human-oversight-protocol.md) — 機器與人工審查的責任邊界。

## 驗證器實務

如需 30 秒快速入門（安裝、執行、解讀輸出），請參閱[驗證器中心](../../validator/index.md)。

## 驗證器 MVP 要求

最小可行驗證器必須執行以下檢查：

### 1. 必要欄位驗證

檢查所有必要欄位是否存在：

| 人工產物 | 必要欄位 |
| --- | --- |
| 證據包清單 | pack_id、pack_version、taxonomy_version、created_date、last_updated、codes、evidence_files |
| Codes 物件 | FS、UC、DT、CH、IM、RS、EV（OB 選用） |
| 證據檔案條目 | file_id（EP-01..EP-07）、filename、title（ev_type / ev_codes 可選） |

### 2. 維度代碼驗證

檢查每個必要維度至少有一個代碼：

| 維度 | 要求 |
| --- | --- |
| FS（功能範圍） | 正好 1 個代碼 |
| UC（使用案例類別） | 至少 1 個代碼 |
| DT（資料類型） | 至少 1 個代碼 |
| CH（通道） | 至少 1 個代碼 |
| IM（整合模式） | 正好 1 個代碼 |
| RS（風險面） | 至少 1 個代碼 |
| OB（成果 / 效益） | 選用（0 或更多） |
| LG（日誌/記錄類型） | 至少 1 個代碼 |

### 3. 字典存在檢查

驗證所有代碼存在於分類字典中：

- 載入指定 `taxonomy_version` 的分類字典
- 驗證清單中的每個代碼存在於字典中
- 報告無效代碼及其維度和值

### 4. 代碼格式驗證

檢查所有代碼符合預期格式：

```regex
^(FS|UC|DT|CH|IM|RS|OB|LG)-\d{3}$
```

### 5. 結構描述驗證

對照 JSON Schema 驗證：

| 結構描述 | 用途 |
| --- | --- |
| `evidence_pack_manifest.schema.json` | 證據包清單 |
| `taxonomy_pack.schema.json` | 分類套件定義 |
| `changelog.schema.json` | 變更日誌條目 |

## 驗證規則

### 規則：必要維度

```yaml
rule_id: required_dimensions
description: 所有必要維度必須至少有一個代碼
severity: error
check: |
  - FS: 正好 1
  - UC: 至少 1
  - DT: 至少 1
  - CH: 至少 1
  - IM: 正好 1
  - RS: 至少 1
  - LG: 至少 1
```

### 規則：有效代碼

```yaml
rule_id: valid_codes
description: 所有代碼必須存在於分類字典中
severity: error
check: |
  對於清單中的每個代碼：
    - 代碼存在於指定 taxonomy_version 的字典中
    - 代碼狀態為 'active'（如果為 'deprecated' 則警告）
```

### 規則：代碼格式

```yaml
rule_id: code_format
description: 所有代碼必須符合標準格式
severity: error
pattern: "^(FS|UC|DT|CH|IM|RS|OB|LG)-\\d{3}$"
```

### 規則：版本格式

```yaml
rule_id: version_format
description: 版本必須是有效的 SemVer
severity: error
pattern: "^\\d+\\.\\d+\\.\\d+$"
fields:
  - pack_version
  - taxonomy_version
```

## 錯誤輸出格式

驗證錯誤以以下格式報告：

```
<path>: <severity>: <message>
```

**範例：**

```
codes.FS: error: Required dimension 'FS' has no codes
codes.UC[0]: error: Code 'UC-999' does not exist in dictionary v0.1.0
pack_version: error: Invalid version format 'v1.0' (expected SemVer)
codes.RS[1]: warning: Code 'RS-002' is deprecated in v0.2.0
```

## 驗證器不檢查什麼

驗證器專注於結構符合性，而非內容品質：

| 面向 | 原因 |
| --- | --- |
| 內容準確性 | 驗證器檢查結構，而非含義 |
| 證據完整性 | 範本是指南，而非強制格式 |
| 交叉參照解析 | 不驗證檔案存在 |
| 時間戳記有效性 | 不嚴格驗證 ISO-8601 |
| ID 唯一性 | 目前不強制執行 |
| 完整性雜湊 | 採用者責任 |

## 參考實作

Python 中提供參考實作：

```
validator/src/validate.py
```

### 使用

```bash
python validator/src/validate.py <manifest.json>
```

### 範例輸出

```
Validating: evidence_pack_manifest.json
Taxonomy version: 0.1.0

Checking required dimensions...
  FS: OK (1 code)
  UC: OK (3 codes)
  DT: OK (1 code)
  CH: OK (1 code)
  IM: OK (1 code)
  RS: OK (3 codes)
  OB: OK (2 codes)
  LG: OK (7 codes)

Checking code validity...
  All codes valid.

Validation: PASSED
```

## 版本政策

驗證器規則遵循 SemVer：

- **MAJOR**：破壞性規則變更（使現有有效套件失敗的新必要檢查）
- **MINOR**：新的選用檢查、警告或資訊訊息
- **PATCH**：不變更驗證結果的錯誤修復

## 結構描述參照

| 結構描述 | 位置 |
| --- | --- |
| 證據包清單 | `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json` |
| 分類套件 | `source_pack/03_taxonomy/schemas/taxonomy_pack.schema.json` |
| 變更日誌 | `source_pack/03_taxonomy/schemas/changelog.schema.json` |

## 參照

- [分類法](./03-taxonomy.md) - 維度定義
- [代碼](./04-codes.md) - 代碼格式
- [字典](./05-dictionary.md) - 代碼字典
- [驗證器規則](../../validator/index.md) - 完整規則文件
