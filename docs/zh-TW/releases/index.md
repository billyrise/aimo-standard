---
description: AIMO 標準發布 - 下載版本化 PDF、人工產物和校驗和。變更日誌、遷移指南和建置來源證明。
---

# 發布

本節是版本化發布、變更日誌、遷移和發布人工產物的中心。

## 下載最新發布

**[GitHub Releases](https://github.com/billyrise/aimo-standard/releases/latest)** — 此為「latest」發布的單一事實來源。網站路徑 `/latest/` 會重新導向至同一版本。

## 驗證程序（永久網頁）

完整的**驗證程序**（下載資產、校驗和驗證、建置來源證明）以永久網頁形式提供，不限於 PDF：

- **[Standard → 版本 → 驗證程序](../standard/versions/index.md)** — 分步校驗和驗證（Linux/macOS/Windows）及來源證明。

當需要驗證發布資產或在稽核交付物中記錄驗證步驟時，請使用本頁。

## 發布資產

每個官方發布（`vX.Y.Z` 標籤）包含：

| 資產 | 說明 |
| --- | --- |
| `trust_package.pdf` | 英文信任套件 — 稽核員就緒保證材料 |
| `trust_package.ja.pdf` | 日文信任套件 |
| `aimo-standard-artifacts.zip` | 結構描述、範本、範例、驗證器規則 |
| `SHA256SUMS.txt` | 所有資產的 SHA-256 校驗和 |

### 驗證下載

下載後，使用校驗和驗證檔案完整性：

=== "Linux"

    ```bash
    # 下載校驗和檔案
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # 驗證特定檔案
    sha256sum -c SHA256SUMS.txt --ignore-missing

    # 或手動驗證：
    sha256sum trust_package.pdf
    # 將輸出與 SHA256SUMS.txt 比較
    ```

=== "macOS"

    ```bash
    # 下載校驗和檔案
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # 驗證特定檔案
    shasum -a 256 -c SHA256SUMS.txt

    # 或手動驗證：
    shasum -a 256 trust_package.pdf
    # 將輸出與 SHA256SUMS.txt 比較
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 下載校驗和檔案
    Invoke-WebRequest -Uri "https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt" -OutFile SHA256SUMS.txt

    # 驗證特定檔案
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # 將 Hash 輸出與 SHA256SUMS.txt 比較
    Get-Content .\SHA256SUMS.txt
    ```

## 人工產物 Zip 內容

`aimo-standard-artifacts.zip` 包含：

- `schemas/jsonschema/*` — 驗證用的 JSON Schema
- `templates/ev/*` — 證據範本（JSON + Markdown）
- `examples/*` — 樣本證據包
- `coverage_map/coverage_map.yaml` — 外部標準對應
- `validator/rules/*` — 驗證規則定義
- `VERSIONING.md`、`GOVERNANCE.md`、`SECURITY.md` 等。

## 資源

- **版本歷史表**：[標準 > 版本](../standard/versions/index.md) — 版本表，包含所有發布資產的直接連結（PDF、ZIP、SHA256）
- **變更日誌（規格）**：[標準 > 當前 > 變更日誌](../standard/current/08-changelog.md) — 規範性和非規範性變更歷史。
- **發布流程**：標記 `vX.Y.Z`、CI 建置、`dist/` 下的 PDF、校驗和、GitHub Release 資產。請參閱儲存庫中的 [GOVERNANCE.md](https://github.com/billyrise/aimo-standard/blob/main/GOVERNANCE.md) 和 [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)。
- **遷移指南**：[MIGRATION.md](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) — 破壞性變更的升級路徑。

如需治理和版本政策，請參閱[治理](../governance/index.md)。

## 準備您的提交套件

準備稽核提交的證據時：

1. **建立您的證據包**：按照[證據包](../artifacts/evidence-bundle.md)和[最低證據要求](../artifacts/minimum-evidence.md)建立 EV 記錄、字典、摘要和變更日誌。
2. **執行驗證器**：執行 `python validator/src/validate.py bundle/root.json` 檢查結構一致性。在繼續之前修復所有錯誤。
3. **產生校驗和**：建立 SHA-256 校驗和以供驗證：

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
4. **打包**：建立套件目錄的 zip 壓縮檔。
5. **記錄版本對齊**：記錄您的證據對齊的 AIMO 標準發布（例如 `v1.0.0`）。
6. **交付**：將套件、校驗和和版本參照提供給您的稽核員。

如需完整的準備指南，請參閱[信任套件](../governance/trust-package.md)。

## 稽核員：驗證程序

收到證據提交的稽核員應驗證完整性和結構：

1. **驗證校驗和**：執行校驗和驗證（Linux：`sha256sum -c`、macOS：`shasum -a 256 -c`、Windows：`Get-FileHash`）以確認檔案完整性
2. **執行驗證器**：執行 `python validator/src/validate.py bundle/root.json` 檢查結構
3. **確認版本**：驗證聲明的 AIMO 標準版本存在於 [GitHub Releases](https://github.com/billyrise/aimo-standard/releases)

!!! tip "獨立取得工具"
    稽核員應直接從官方 AIMO 標準發布下載驗證器和結構描述，而非從提交方取得。

如需完整的驗證程序（校驗和、證明、分步），請參閱 **[Standard → 版本 → 驗證程序](../standard/versions/index.md)**。另見 [信任套件](../governance/trust-package.md) 取得稽核就緒材料。

## 不過度聲明聲明

!!! warning "重要"
    AIMO 標準支援**可解釋性和證據就緒**。它**不**提供法律建議、保證合規性或認證符合任何法規或框架。採用者必須對照權威文本驗證聲明並視情況取得專業建議。

請參閱[責任邊界](../governance/responsibility-boundary.md)了解範圍、假設和採用者責任。
