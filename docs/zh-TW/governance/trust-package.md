---
description: AIMO 信任套件 - 稽核員就緒材料包。稽核員、法務和 IT 安全評估 AI 治理採用就緒性所需的最低文件。
---

# 信任套件（保證套件）

本頁彙整稽核員、法務和 IT 安全評估採用就緒性所需的最低材料。
它僅是一個中心；詳細的證據目錄和覆蓋範圍表在各自的章節中維護。

## 下載

**[下載信任套件 PDF（最新發布）](https://github.com/billyrise/aimo-standard/releases/latest)**

信任套件 PDF 將稽核員就緒材料整合成單一文件。每個 GitHub Release 包含：

- `trust_package.pdf` — 英文信任套件
- `trust_package.ja.pdf` — 日文信任套件
- `aimo-standard-artifacts.zip` — 結構描述、範本、範例、驗證器規則
- `SHA256SUMS.txt` — 驗證用的校驗和

## 您獲得的內容

- **符合性**：如何聲明合規以及各等級的意義 — [符合性](../conformance/index.md)
- **覆蓋範圍對應**：與外部標準的對應 — [覆蓋範圍對應索引](../coverage-map/index.md)、[覆蓋範圍對應方法論](../coverage-map/methodology.md)
- **標準**：規範性要求和定義 — [標準（當前）](../standard/current/index.md)
- **分類法**：AI 治理的 8 維度分類系統 — [分類法](../standard/current/03-taxonomy.md)、[代碼](../standard/current/04-codes.md)、[字典](../standard/current/05-dictionary.md)
- **證據包**：結構、目錄、可追溯性 — [證據包](../artifacts/evidence-bundle.md)
- **最低證據要求**：按生命週期的必要層級檢查清單 — [最低證據要求](../artifacts/minimum-evidence.md)
- **驗證器**：規則和參考檢查 — [驗證器](../validator/index.md)
- **範例**：稽核就緒的樣本套件 — [範例](../examples/index.md)
- **發布**：變更歷史和發布 — [發布](../../releases/)
- **治理**：政策、安全、授權 — [治理](../governance/index.md)

## 稽核就緒的最低要求集

| 項目 | 在哪裡找到 | 結果 / 證明什麼 |
| --- | --- | --- |
| 符合性等級 | [符合性](../conformance/index.md) | 如何聲明合規以及所需證據的範圍 |
| 覆蓋範圍對應 | [覆蓋範圍對應索引](../coverage-map/index.md)、[覆蓋範圍對應方法論](../coverage-map/methodology.md) | 對外部法規和標準的可解釋性 |
| 分類法與字典 | [分類法](../standard/current/03-taxonomy.md)、[代碼](../standard/current/04-codes.md)、[字典](../standard/current/05-dictionary.md) | AI 系統的分類系統（8 維度、91 個代碼） |
| 證據人工產物 | [證據包](../artifacts/evidence-bundle.md)、[最低證據](../artifacts/minimum-evidence.md)、[EV 範本](../standard/current/06-ev-template.md) | 支援可追溯性必須存在的資料 |
| 驗證器檢查 | [驗證器](../validator/index.md) | 如何驗證內部一致性和完整性 |
| 範例套件 | [範例](../examples/index.md) | 稽核就緒套件在實務中的樣子 |
| 變更控制 | [發布](../../releases/)、[治理](../governance/index.md) | 更新如何管理和溝通 |
| 安全 / 授權 / 商標 | [治理](../governance/index.md) | 採用決策的法律和安全態勢 |

## 如何引用

使用儲存庫 README 獲取引用指引和背景；治理連結到權威政策。
請參閱 [README.md](https://github.com/billyrise/aimo-standard/blob/main/README.md) 和[治理](../governance/index.md)。

## 人工產物 zip 內容

`aimo-standard-artifacts.zip` 包含：

- **分類法（SSOT）**：`source_pack/03_taxonomy/` — 字典 CSV（91 個代碼）、YAML、代碼系統
- **JSON 結構描述**：`schemas/jsonschema/` — 機器可讀驗證結構描述
- **範本**：`templates/ev/` — 證據記錄範本（JSON + Markdown）
- **範例**：`examples/` — 快速採用的最小樣本套件
- **覆蓋範圍對應**：`coverage_map/coverage_map.yaml` — 與外部標準的對應
- **驗證器規則**：`validator/rules/` — 驗證規則定義
- **治理文件**：`VERSIONING.md`、`GOVERNANCE.md`、`SECURITY.md`、`LICENSE.txt` 等。

## 責任邊界

AIMO 標準提供結構化證據格式和可解釋性框架。它**不**提供法律建議、合規認證、風險評估或稽核執行。

如需完整的範圍定義、假設和採用者責任，請參閱[責任邊界](responsibility-boundary.md)。

## 如何準備提交套件

按照以下步驟準備稽核就緒的提交：

1. **產生證據包**：根據[證據包](../artifacts/evidence-bundle.md)和[最低證據要求](../artifacts/minimum-evidence.md)建立 EV 記錄、字典、摘要和變更日誌。
2. **執行驗證器**：執行 `python validator/src/validate.py bundle/root.json` 檢查結構一致性。在繼續之前修復任何錯誤。
3. **建立校驗和**：為所有提交檔案產生 SHA-256 校驗和：

    === "Linux"

        ```bash
        sha256sum *.json *.pdf > SHA256SUMS.txt
        ```

    === "macOS"

        ```bash
        shasum -a 256 *.json *.pdf > SHA256SUMS.txt
        ```

    === "Windows (PowerShell)"

        ```powershell
        Get-ChildItem *.json, *.pdf | ForEach-Object {
            $hash = (Get-FileHash $_.FullName -Algorithm SHA256).Hash.ToLower()
            "$hash  $($_.Name)"
        } | Out-File SHA256SUMS.txt -Encoding UTF8
        ```
4. **打包人工產物**：建立證據包的 zip 壓縮檔：
   ```bash
   zip -r evidence_bundle.zip bundle_directory/
   ```
5. **參照發布版本**：記錄您的套件對齊的 AIMO 標準版本（例如 `v1.0.0`）。
6. **交付**：將 zip、校驗和和版本參照提供給您的稽核員或合規功能。

如需發布資產和驗證，請參閱[發布](../../releases/)。

## 不過度聲明聲明

!!! warning "重要"
    AIMO 標準支援**可解釋性和證據就緒**。它**不**提供法律建議、保證合規性或認證符合任何法規或框架。採用者必須對照權威文本驗證聲明並視情況取得專業建議。

請參閱[責任邊界](responsibility-boundary.md)了解範圍、假設和採用者責任的詳細資訊。

## 稽核員：驗證程序

收到證據提交時，稽核員應使用以下步驟驗證完整性和結構：

!!! success "建置來源可用"
    所有發布資產包含密碼學簽名的建置證明。請參閱[驗證程序](../standard/versions/index.md#4-verify-build-provenance-attestation)了解證明驗證步驟。

### 步驟 1：驗證校驗和（SHA-256）

=== "Linux"

    ```bash
    # 下載或接收提交附帶的 SHA256SUMS.txt
    # 驗證所有檔案符合其記錄的校驗和
    sha256sum -c SHA256SUMS.txt

    # 或手動驗證個別檔案：
    sha256sum evidence_bundle.zip
    # 將輸出與 SHA256SUMS.txt 中的值比較
    ```

=== "macOS"

    ```bash
    # 驗證所有檔案符合其記錄的校驗和
    shasum -a 256 -c SHA256SUMS.txt

    # 或手動驗證個別檔案：
    shasum -a 256 evidence_bundle.zip
    # 將輸出與 SHA256SUMS.txt 中的值比較
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 驗證個別檔案
    Get-FileHash .\evidence_bundle.zip -Algorithm SHA256

    # 將 Hash 輸出與 SHA256SUMS.txt 比較
    Get-Content .\SHA256SUMS.txt
    ```

如果任何校驗和失敗，應拒絕或重新請求提交。

### 步驟 2：驗證套件結構（驗證器）

**先決條件**（一次性設定）：

```bash
# 複製官方 AIMO 標準發布
git clone https://github.com/billyrise/aimo-standard.git
cd aimo-standard

# 重要：使用提交中聲明的確切版本
# 將 VERSION 替換為提交者聲明的版本（例如 v0.0.1）
VERSION=v0.0.1  # ← 符合提交中的版本
git checkout "$VERSION"

# 設定 Python 環境
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

!!! warning "版本符合"
    始終使用提交中聲明的確切 AIMO 標準版本。使用不同版本可能會因版本之間的結構描述或規則變更而導致驗證不符。

**執行驗證**：

```bash
# 解壓提交的套件
unzip evidence_bundle.zip -d bundle/

# 對套件的 root.json 執行驗證器
python validator/src/validate.py bundle/root.json

# 預期輸出：「validation OK」或錯誤清單
```

**範例**（使用內建樣本）：

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

驗證器檢查：

- 必要檔案存在（EV 記錄、字典）
- JSON 檔案符合結構描述
- 交叉參照（request_id、review_id 等）有效
- 時間戳記存在且格式正確

### 步驟 3：驗證版本對齊

檢查提交是否參照官方 AIMO 標準發布：

1. 確認聲明的版本（例如 `v0.0.1`）存在於 [GitHub Releases](https://github.com/billyrise/aimo-standard/releases)
2. 將提交的結構描述與發布人工產物比較
3. 記錄與官方發布的任何偏差

### 要檢查的內容

| 檢查 | 通過標準 | 失敗動作 |
| --- | --- | --- |
| 校驗和符合 | 所有 `sha256sum -c` 檢查通過 | 拒絕或重新請求 |
| 驗證器通過 | `validate.py` 無錯誤 | 接受前請求修復 |
| 版本存在 | 發布標籤存在於 GitHub | 澄清版本對齊 |
| 必要欄位存在 | EV 記錄有 id、timestamp、source、summary | 請求完成 |
| 可追溯性完整 | 交叉參照正確解析 | 請求連結修復 |

!!! info "稽核員獨立性"
    稽核員應直接從官方 AIMO 標準發布取得驗證器和結構描述，而非從提交方取得，以確保驗證獨立性。

## 稽核旅程

從本頁面開始，建議的稽核旅程是：

1. **分類系統**：[分類法](../standard/current/03-taxonomy.md) + [字典](../standard/current/05-dictionary.md) — 了解 8 維度代碼系統
2. **證據結構**：[證據包](../artifacts/evidence-bundle.md) — 了解套件目錄和可追溯性
3. **必要證據**：[最低證據要求](../artifacts/minimum-evidence.md) — 按生命週期的必要層級檢查清單
4. **框架對齊**：[覆蓋範圍對應](../coverage-map/index.md) + [方法論](../coverage-map/methodology.md) — 查看 AIMO 如何對應到外部框架
5. **驗證**：[驗證器](../validator/index.md) — 執行結構一致性檢查
6. **下載**：[發布](../../releases/) — 取得發布資產並驗證校驗和
