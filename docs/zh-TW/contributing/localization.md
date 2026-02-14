---
description: AIMO 在地化指南 - 多語言文件的 i18n 結構、維護工作流程和 SSOT 原則。
---

# 在地化指南

本頁記錄 AIMO 標準文件的在地化（i18n）結構、維護工作流程和 SSOT（單一事實來源）原則。

## 語言純淨政策

**每個語言頁面應只包含該語言的內容。**

| 規則 | 說明 |
| --- | --- |
| **EN 頁面** | 不得包含 CJK 字元或對特定語言欄位的參照（例如 `_ja` 後綴） |
| **JA 頁面** | 不得將 EN 特定術語解釋為規範結構 |
| **例外** | 列於 `tooling/checks/lint_i18n.py` 中的 `MIXED_LANGUAGE_ALLOWLIST` |

此政策確保：
1. 讀者只看到他們選擇的語言
2. 新增新語言不需要更新現有頁面
3. CI 可以自動偵測違規

## 語言結構

AIMO 標準文件使用**基於資料夾的 i18n 結構**：

```
docs/
├── en/           # English（規範）
├── ja/           # Japanese（日本語）
├── es/           # Spanish（Español）
├── fr/           # French（Français）
├── de/           # German（Deutsch）
├── pt/           # Portuguese（Português）
├── it/           # Italian（Italiano）
├── zh/           # Simplified Chinese（简体中文）
├── zh-TW/        # Traditional Chinese（繁體中文）
└── ko/           # Korean（한국어）
```

- **英文是規範版本**：`docs/en/` 資料夾是文件內容的權威來源。
- **其他語言鏡像結構**：每個語言資料夾（`ja/` 等）維持與 `en/` 相同的檔案結構。
- **相同檔名**：所有語言使用 `.md` 副檔名（檔名中沒有語言後綴）。
- **回退到英文**：缺少的翻譯自動回退到英文內容。

## 分類法資料模型

分類法使用**語言中立的規範結構**搭配獨立的翻譯套件：

```
data/
└── taxonomy/
    ├── canonical.yaml           # 語言中立（代碼、狀態、生命週期）
    └── i18n/
        ├── en.yaml              # 英文標籤和定義
        ├── ja.yaml              # 日文標籤和定義
        └── {lang}.yaml          # 其他語言（空白範本）
```

### 規範結構（`canonical.yaml`）

包含語言中立的資料：

- 代碼識別碼（例如 `FS-001`、`UC-001`）
- 狀態（`active`、`deprecated`、`removed`）
- 生命週期中繼資料（`introduced_in`、`deprecated_in`、`removed_in`、`replaced_by`）
- 範圍說明和範例（英文，作為技術參考）

### 翻譯套件（`i18n/*.yaml`）

每個語言套件包含：

- 維度名稱（例如「功能範圍」）
- 代碼標籤（例如「終端使用者生產力」）
- 代碼定義

**回退**：如果翻譯缺失，系統使用英文。

## SSOT 原則

AIMO 對分類法資料使用 **SSOT 優先架構**：

| 資產類型 | SSOT 位置 | 說明 |
| --- | --- | --- |
| **分類法（結構）** | `data/taxonomy/canonical.yaml` | 語言中立結構（SSOT） |
| **分類法（i18n）** | `data/taxonomy/i18n/*.yaml` | 各語言翻譯（SSOT） |
| **覆蓋範圍對應** | `coverage_map/coverage_map.yaml` | 框架到證據的對應 |
| **結構描述** | `schemas/jsonschema/` | JSON 驗證結構描述 |

### 衍生檔案

以下檔案是從 SSOT **產生**的，不應手動編輯：

| 檔案 | 產生自 | 產生器 |
| --- | --- | --- |
| `artifacts/taxonomy/{version}/{lang}/taxonomy_dictionary.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_en.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_ja.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/code_system.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/dimensions_en_ja.md` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_dictionary.json` | canonical + i18n | `build_artifacts.py` |

### 語言代碼（BCP47）

AIMO 使用 BCP47 語言代碼：

| 代碼 | 語言 | 狀態 |
| --- | --- | --- |
| `en` | English | 規範（來源） |
| `ja` | Japanese（日本語） | 啟用 |
| `es` | Spanish（Español） | 啟用 |
| `fr` | French（Français） | 啟用 |
| `de` | German（Deutsch） | 啟用 |
| `pt` | Portuguese（Português） | 啟用 |
| `it` | Italian（Italiano） | 啟用 |
| `zh` | Simplified Chinese（简体中文） | 啟用 |
| `zh-TW` | Traditional Chinese（繁體中文） | 啟用 |
| `ko` | Korean（한국어） | 啟用 |

### 舊版 CSV 檔案（凍結）

`source_pack/03_taxonomy/legacy/` 中的舊版 EN/JA 混合 CSV 檔案：

- **凍結在 21 欄** — 不會新增新的語言欄位
- **為向後相容性而維護** — 現有整合可以繼續使用
- **CI 強制執行** — 新增 `label_es`、`definition_de` 等會導致建置失敗

對於新語言，請使用 `artifacts/taxonomy/{version}/{lang}/` 中的各語言人工產物。

## 翻譯新鮮度追蹤

AIMO 使用**翻譯新鮮度追蹤**系統來維護英文（來源）和翻譯內容之間的一致性。

### 運作方式

1. 每個翻譯檔案包含追蹤其翻譯自哪個英文來源版本的中繼資料
2. 當英文內容更新時，系統偵測過時的翻譯
3. CI 會對過時的翻譯發出警告但不會阻擋（翻譯可以落後）

### 翻譯中繼資料

翻譯檔案包含 frontmatter 中繼資料：

```yaml
---
# TRANSLATION METADATA - DO NOT REMOVE
source_file: en/standard/current/01-overview.md
source_hash: abc123def456
translation_date: 2026-02-02
translator: human|machine|hybrid
translation_status: current|outdated|needs_review
---
```

### 使用同步工具

```bash
# 檢查所有翻譯的新鮮度
python tooling/i18n/sync_translations.py --check

# 檢查特定語言
python tooling/i18n/sync_translations.py --check --lang ja

# 產生翻譯報告
python tooling/i18n/sync_translations.py --report

# 初始化新語言（複製 EN 作為基礎）
python tooling/i18n/sync_translations.py --init-lang es

# 完成翻譯後更新中繼資料
python tooling/i18n/sync_translations.py --update-meta docs/ja/index.md
```

如需詳細技術規格，請參閱 `tooling/i18n/TRANSLATION_SYNC_SPEC.md`。

## 更新工作流程

### 分類法更新（新 SSOT 優先工作流程）

1. 編輯 `data/taxonomy/` 中的 SSOT：
   - 結構變更 → `canonical.yaml`
   - 英文翻譯 → `i18n/en.yaml`
   - 日文翻譯 → `i18n/ja.yaml`
2. 執行驗證：`python tooling/checks/lint_taxonomy_ssot.py`
3. 重新產生所有衍生檔案：`python tooling/taxonomy/build_artifacts.py --version current --langs en ja`
4. 根據需要更新文件頁面
5. 一起提交所有變更

### 覆蓋範圍對應更新

1. 編輯 `coverage_map/coverage_map.yaml`（SSOT）
2. 更新對應的框架頁面表格（`docs/en/coverage-map/*.md`）
3. 更新日文翻譯（`docs/ja/coverage-map/*.md`）
4. 一起提交所有變更

### 文件更新

1. 編輯英文來源（`docs/en/...`）
2. 根據需要更新翻譯（或標記以便稍後更新）
3. 執行 `python tooling/i18n/sync_translations.py --check` 查看過時的翻譯
4. 執行 `python tooling/checks/lint_i18n.py` 驗證標題一致性
5. 執行 `mkdocs build --strict` 驗證建置
6. 一起提交所有變更

!!! note "翻譯優先順序"
    並非所有翻譯都需要立即更新。第 1 層（關鍵）頁面應優先處理：
    
    - `index.md`
    - `standard/current/*.md`
    - `governance/index.md`
    - `releases/`

## 新增新語言（5 步驟）

要新增新語言（例如西班牙文）：

### 步驟 1：產生分類法套件

```bash
python tooling/taxonomy/build_i18n_taxonomy.py --add-lang es --lang-name "Español"
```

建立 `data/taxonomy/i18n/es.yaml`，以英文參考作為註解。

### 步驟 2：建立文件資料夾

```bash
mkdir -p docs/es && cp -r docs/en/* docs/es/
```

### 步驟 3：更新 mkdocs.yml

```yaml
plugins:
  - i18n:
      languages:
        - locale: es
          name: Español
          build: true
```

### 步驟 4：翻譯

- 翻譯 `data/taxonomy/i18n/es.yaml`
- 翻譯 `docs/es/` 中的檔案

### 步驟 5：驗證

```bash
python tooling/checks/lint_i18n.py && mkdocs build --strict
```

!!! success "完成"
    新語言現在可在 `/dev/es/` 使用

## 檔案命名慣例

| 模式 | 範例 | 說明 |
| --- | --- | --- |
| `index.md` | `docs/en/governance/index.md` | 章節首頁 |
| `{topic}.md` | `docs/en/governance/trust-package.md` | 主題頁面 |
| `{NN}-{topic}.md` | `docs/en/standard/current/03-taxonomy.md` | 編號規格頁面 |

## 品質檢查

提交前執行這些檢查：

```bash
# i18n 結構、標題一致性和過時用語偵測
python tooling/checks/lint_i18n.py

# 結構描述和清單 lint
python tooling/checks/lint_schema.py
python tooling/checks/lint_manifest.py

# 分類法 SSOT lint
python tooling/checks/lint_taxonomy_ssot.py --required-langs en
python tooling/checks/lint_legacy_csv.py
python tooling/checks/lint_taxonomy_dictionary.py
python tooling/checks/lint_taxonomy_json.py

# 分類法人工產物是否最新
python tooling/taxonomy/build_artifacts.py --check

# 建置驗證
mkdocs build --strict
```

## 相關頁面

- [發布](../../releases/) — 可下載的套件
- [治理](../../governance/) — 專案治理
