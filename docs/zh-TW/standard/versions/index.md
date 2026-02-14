---
description: AIMO 標準版本歷史。包含稽核員就緒 PDF、機器可讀人工產物、校驗和和建置來源證明的官方凍結發布。
---

# 版本

官方發布是與稽核員就緒 PDF 和機器可讀人工產物一起發布的凍結快照。

## 最新發布

!!! success "當前版本"
    **v0.0.2** (2026-02-02) — [檢視文件](../current/) | [GitHub Release](https://github.com/billyrise/aimo-standard/releases/tag/v0.0.2)

## 版本歷史

| 版本 | 日期 | 發布說明 | PDF (EN) | PDF (JA) | 人工產物 | 校驗和 |
| :------ | :--- | :------------ | :------- | :------- | :-------- | :-------- |
| **v0.0.2** | 2026-02-02 | [變更日誌](../current/08-changelog/) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/SHA256SUMS.txt) |
| **v0.0.1** | 2026-02-02 | [變更日誌](../current/08-changelog/) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/SHA256SUMS.txt) |

!!! note "資料來源"
    此版本表與 [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) 同步。每個發布標籤（`vX.Y.Z`）對應一個凍結的規格快照。

##「latest」的單一事實來源（SSOT）

**「latest」的權威定義**是 [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) 的 **latest** 標籤（`releases/latest`）。網站路徑 `/latest/` 一律重新導向至該發布。沒有獨立的「網站 latest」——發布工作流程會部署帶標籤的版本並在一步中將其設為 `latest` 別名。

| 來源 | 角色 |
|--------|------|
| **GitHub Release 的 latest 標籤** | SSOT —「目前發布」的唯一定義 |
| **版本表**（本頁） | 透過發布工作流程與發布同步；部署前必須與標籤一致 |
| **Changelog** | 規範性變更歷史；發布說明會引用 |
| **網站 `/latest/`** | 重新導向至與 GitHub Release latest 相同的版本 |

發布流程詳情請見 [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) 與 [release 工作流程](https://github.com/billyrise/aimo-standard/blob/main/.github/workflows/release.yml)。版本表與 Changelog 會作為發布準備的一部分更新，以始終與已部署版本一致。

## 法律與商標聲明

**English notice (key facts):** Only AIMOaaS has been filed for trademark registration by RISEby Inc. (pending). "AIMO" is a registered trademark owned by third parties; RISEby Inc. does not claim ownership. For full trademark status and usage, see [Governance → 商標](../../governance/trademarks/) and [TRADEMARKS.md](https://github.com/billyrise/aimo-standard/blob/main/TRADEMARKS.md).

## 給稽核員：正規 URL 與版本固定

在稽核報告中引用特定版本並確保可重現性時：

1. **正規 URL**：使用該版本的固定文件 URL，例如 `https://standard.aimoaas.com/0.0.3/`（將 `0.0.3` 替換為您使用的版本）。
2. **版本固定**：記錄 [GitHub Release](https://github.com/billyrise/aimo-standard/releases) 頁面的**發布標籤**（例如 `v0.0.3`）及可選的**提交雜湊**。如此可獨立驗證規格快照與發布資產（PDF、ZIP、校驗和）一致。
3. **證據對齊**：在提交中說明您的 evidence bundle 所依據的 AIMO Standard 版本（例如 `v0.0.3`），並從同一發布取得驗證器與結構描述。

## 版本層

AIMO Standard 使用三種版本概念。目前發布中它們一致；未來發布可能獨立進行版本管理。

| 層 | 說明 | 出現位置 |
|------|-------------|--------------|
| **Standard 版本**（網站/發布） | 發布標籤與文件快照（例如 `v0.0.3`）。 | 版本表、GitHub Releases、`/X.Y.Z/` URL。 |
| **Taxonomy 結構描述版本** | 代碼體系與 taxonomy/結構描述定義的版本。 | 清單中的 `taxonomy_version`；結構描述的 `$id` 或文件。 |
| **Dictionary 內容版本** | 字典條目（代碼與定義）的版本。 | 字典中繼資料；0.0.x 中與 taxonomy 相同。 |

引用「AIMO Standard vX.Y.Z」時，**Standard 版本**定義規範快照。Validator 與 Minimum Evidence Requirements 指該發布的產物與結構描述。

## 驗證程序

稽核員和實作者應使用 SHA-256 校驗和驗證下載完整性：

### 1. 下載發布資產

=== "Linux / macOS"

    ```bash
    # 下載特定版本的所有資產
    VERSION=v0.0.1
    BASE_URL="https://github.com/billyrise/aimo-standard/releases/download/${VERSION}"

    curl -LO "${BASE_URL}/trust_package.pdf"
    curl -LO "${BASE_URL}/trust_package.ja.pdf"
    curl -LO "${BASE_URL}/aimo-standard-artifacts.zip"
    curl -LO "${BASE_URL}/SHA256SUMS.txt"
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 下載特定版本的所有資產
    $VERSION = "v0.0.1"
    $BASE_URL = "https://github.com/billyrise/aimo-standard/releases/download/$VERSION"

    Invoke-WebRequest -Uri "$BASE_URL/trust_package.pdf" -OutFile trust_package.pdf
    Invoke-WebRequest -Uri "$BASE_URL/trust_package.ja.pdf" -OutFile trust_package.ja.pdf
    Invoke-WebRequest -Uri "$BASE_URL/aimo-standard-artifacts.zip" -OutFile aimo-standard-artifacts.zip
    Invoke-WebRequest -Uri "$BASE_URL/SHA256SUMS.txt" -OutFile SHA256SUMS.txt
    ```

### 2. 驗證校驗和

=== "Linux"

    ```bash
    # 驗證所有下載的檔案是否符合校驗和
    sha256sum -c SHA256SUMS.txt

    # 預期輸出（所有都應顯示「OK」）：
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "macOS"

    ```bash
    # 驗證所有下載的檔案是否符合校驗和
    shasum -a 256 -c SHA256SUMS.txt

    # 預期輸出（所有都應顯示「OK」）：
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 驗證每個檔案
    Get-FileHash .\trust_package.pdf -Algorithm SHA256
    Get-FileHash .\trust_package.ja.pdf -Algorithm SHA256
    Get-FileHash .\aimo-standard-artifacts.zip -Algorithm SHA256

    # 將 Hash 輸出與 SHA256SUMS.txt 比較
    Get-Content .\SHA256SUMS.txt
    ```

### 3. 手動驗證（替代方案）

=== "Linux"

    ```bash
    # 計算特定檔案的雜湊
    sha256sum trust_package.pdf

    # 與 SHA256SUMS.txt 比較輸出
    cat SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # 計算特定檔案的雜湊
    shasum -a 256 trust_package.pdf

    # 與 SHA256SUMS.txt 比較輸出
    cat SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 計算特定檔案的雜湊
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # 檢視校驗和檔案
    Get-Content .\SHA256SUMS.txt
    ```

!!! tip "給稽核員"
    始終直接從官方 GitHub Release 取得校驗和檔案，而非從提交方取得。這確保獨立驗證。

### 4. 驗證建置來源（證明）

所有發布資產包含由 GitHub Actions 產生的密碼學簽名建置來源證明。這讓您可以驗證資產是在官方儲存庫中建置的，沒有被竄改。

**先決條件**：安裝 [GitHub CLI](https://cli.github.com/)（`gh`）

```bash
# 使用 GitHub CLI 下載發布資產
VERSION=v0.0.1
gh release download "$VERSION" --repo billyrise/aimo-standard

# 驗證每個資產的證明
gh attestation verify trust_package.pdf --repo billyrise/aimo-standard
gh attestation verify trust_package.ja.pdf --repo billyrise/aimo-standard
gh attestation verify aimo-standard-artifacts.zip --repo billyrise/aimo-standard
gh attestation verify SHA256SUMS.txt --repo billyrise/aimo-standard
```

**預期輸出**（成功）：

```
Loaded digest sha256:abc123... for file trust_package.pdf
Loaded 1 attestation from GitHub API
✓ Verification succeeded!
```

**離線驗證**（隔離環境）：

```bash
# 首先，下載受信任的根（需要一次網路存取）
gh attestation trusted-root > trusted-root.jsonl

# 然後離線驗證
gh attestation verify trust_package.pdf \
  --repo billyrise/aimo-standard \
  --custom-trusted-root trusted-root.jsonl
```

!!! info "證明證明什麼"
    建置來源證明密碼學證明發布資產：

    1. 由 GitHub Actions 建置（非開發者的本機電腦）
    2. 從官方 `billyrise/aimo-standard` 儲存庫建置
    3. 從與發布標籤關聯的確切 commit 建置
    4. 在建置完成後未被修改

## 相容性

AIMO 標準遵循[語意化版本控制](https://semver.org/)（SemVer）：

| 變更類型 | 版本提升 | 影響 |
| :---------- | :----------- | :----- |
| **MAJOR** | X.0.0 | 破壞性變更 — 需要遷移 |
| **MINOR** | 0.X.0 | 向後相容的新增 |
| **PATCH** | 0.0.X | 修復和澄清 |

如需完整的版本政策，請參閱 [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)。

## 遷移

在具有破壞性變更的版本之間升級時：

1. 檢查[變更日誌](../current/08-changelog/)了解破壞性變更
2. 查閱[遷移指南](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md)了解特定的升級路徑
3. 更新您的證據包以符合新的結構描述要求
4. 重新執行驗證器以驗證符合性

!!! warning "破壞性變更"
    MAJOR 版本更新可能需要變更現有的證據包。升級前務必查閱遷移指南。

## 版本化文件快照

每個發布建立一個凍結的文件快照，可在以下位置存取：

- 生產環境：`https://standard.aimoaas.com/{version}/`（例如 `/0.0.1/`）
- GitHub Pages：`https://billyrise.github.io/aimo-standard/{version}/`

### URL 類型及其含義

| URL 模式 | 說明 | 用於稽核引用？ |
|-------------|-------------|---------------------|
| `/X.Y.Z/`（例如 `/0.0.1/`） | **凍結發布** — 不可變快照 | **是**（首選） |
| `/latest/` | **別名** — 重新導向到最新發布 | 是（解析到 `/X.Y.Z/`） |
| `/dev/` | **預覽** — 未發布的主分支內容 | **否**（不用於引用） |

!!! warning "理解 `/latest/` 與 `/dev/`"
    - **`/latest/`** 是指向最新**已發布**版本的別名（重新導向）。它可以安全地用於引用，因為它解析到凍結的快照。
    - **`/dev/`** 反映當前的 `main` 分支，可能包含**未發布的變更**。絕不要在稽核報告中引用 `/dev/`。

### 常見問題

??? question "為什麼 `/latest/` 不是版本號？"
    `/latest/` 是一個便利別名，始終重新導向到最新的穩定發布（例如 `/0.0.1/`）。這讓使用者可以收藏單一 URL，同時自動取得當前版本。對於需要不可變性的正式稽核，請改用明確的版本 URL。

??? question "稽核員應引用哪個 URL？"
    - **正式稽核（需要不可變性）**：使用 `/X.Y.Z/`（例如 `https://standard.aimoaas.com/0.0.1/standard/current/`）
    - **一般參照**：`/latest/` 可接受，因為它重新導向到當前發布
    - **絕不引用**：`/dev/`（未發布，可能變更）

??? question "如果 `/latest/` 顯示與預期不同的內容怎麼辦？"
    這可能是部署錯誤。如果您懷疑 `/latest/` 與最新的 [GitHub Release](https://github.com/billyrise/aimo-standard/releases) 不同，請[報告問題](https://github.com/billyrise/aimo-standard/issues)。`/latest/` 別名應始終重新導向到最新的標記發布。

## 資源

- **[發布中心](../../../releases/)** — 提交準備、稽核員驗證、不過度聲明聲明
- **[信任套件](../../governance/trust-package/)** — 稽核員就緒保證材料
- **[變更日誌（詳細）](../current/08-changelog/)** — 包含棄用追蹤的完整變更歷史
- **[VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)** — 完整版本政策
