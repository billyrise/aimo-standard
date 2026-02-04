---
description: AIMO 标准版本历史。带有审计师就绪 PDF、机器可读工件、校验和和构建来源证明的官方冻结版本。
---

# 版本

官方发布是带有审计师就绪 PDF 和机器可读工件的冻结快照。

## 最新版本

!!! success "当前版本"
    **v0.0.2**（2026-02-02）— [查看文档](../current/index.md) | [GitHub Release](https://github.com/billyrise/aimo-standard/releases/tag/v0.0.2)

## 版本历史

| 版本 | 日期 | 发布说明 | PDF（EN） | PDF（JA） | 工件 | 校验和 |
| :------ | :--- | :------------ | :------- | :------- | :-------- | :-------- |
| **v0.0.2** | 2026-02-02 | [变更日志](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/SHA256SUMS.txt) |
| **v0.0.1** | 2026-02-02 | [变更日志](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/SHA256SUMS.txt) |

!!! note "数据来源"
    此版本表与 [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) 同步。每个发布标签（`vX.Y.Z`）对应规范的冻结快照。

## “latest”的单一事实来源（SSOT）

**“latest”的权威定义**是 [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) 的 **latest** 标签（`releases/latest`）。站点路径 `/latest/` 始终重定向到该发布。不存在单独的“站点 latest”——发布工作流会部署带标签的版本并在一步中将其设为 `latest` 别名。

| 来源 | 角色 |
|--------|------|
| **GitHub Release 的 latest 标签** | SSOT — “当前发布”的唯一定义 |
| **版本表**（本页） | 通过发布工作流与发布同步；部署前必须与标签一致 |
| **Changelog** | 规范性变更历史；发布说明引用它 |
| **站点 `/latest/`** | 重定向到与 GitHub Release latest 相同的版本 |

发布流程详情见 [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) 和 [release 工作流](https://github.com/billyrise/aimo-standard/blob/main/.github/workflows/release.yml)。版本表和 Changelog 作为发布准备的一部分进行更新，以始终与已部署版本一致。

## 法律与商标声明

**English notice (key facts):** Only AIMOaaS has been filed for trademark registration by RISEby Inc. (pending). "AIMO" is a registered trademark owned by third parties; RISEby Inc. does not claim ownership. For full trademark status and usage, see [Governance → 商标](../../governance/trademarks.md) and [TRADEMARKS.md](https://github.com/billyrise/aimo-standard/blob/main/TRADEMARKS.md).

## 面向审计师：规范 URL 与版本固定

在审计报告中引用特定版本并确保可重复性时：

1. **规范 URL**：使用该版本的固定文档 URL，例如 `https://standard.aimoaas.com/0.0.3/`（将 `0.0.3` 替换为您使用的版本）。
2. **版本固定**：记录 [GitHub Release](https://github.com/billyrise/aimo-standard/releases) 页面的**发布标签**（例如 `v0.0.3`）及可选的**提交哈希**。这样可独立验证规范快照与发布资产（PDF、ZIP、校验和）一致。
3. **证据对齐**：在提交中说明您的 evidence bundle 所依据的 AIMO Standard 版本（例如 `v0.0.3`），并从同一发布获取验证器和模式。

## 版本层

AIMO Standard 使用三个版本概念。当前发布中它们一致；未来发布可能独立进行版本管理。

| 层 | 说明 | 出现位置 |
|------|-------------|--------------|
| **Standard 版本**（站点/发布） | 发布标签和文档快照（例如 `v0.0.3`）。 | 版本表、GitHub Releases、`/X.Y.Z/` URL。 |
| **Taxonomy 模式版本** | 代码体系与 taxonomy/模式定义的版本。 | 清单中的 `taxonomy_version`；模式的 `$id` 或文档。 |
| **Dictionary 内容版本** | 字典条目（代码与定义）的版本。 | 字典元数据；0.0.x 中与 taxonomy 相同。 |

引用“AIMO Standard vX.Y.Z”时，**Standard 版本**定义规范快照。Validator 和 Minimum Evidence Requirements 指该发布的工件和模式。

## 验证程序

审计师和实施者应使用 SHA-256 校验和验证下载完整性：

### 1. 下载发布资产

=== "Linux / macOS"

    ```bash
    # 下载特定版本的所有资产
    VERSION=v0.0.1
    BASE_URL="https://github.com/billyrise/aimo-standard/releases/download/${VERSION}"

    curl -LO "${BASE_URL}/trust_package.pdf"
    curl -LO "${BASE_URL}/trust_package.ja.pdf"
    curl -LO "${BASE_URL}/aimo-standard-artifacts.zip"
    curl -LO "${BASE_URL}/SHA256SUMS.txt"
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 下载特定版本的所有资产
    $VERSION = "v0.0.1"
    $BASE_URL = "https://github.com/billyrise/aimo-standard/releases/download/$VERSION"

    Invoke-WebRequest -Uri "$BASE_URL/trust_package.pdf" -OutFile trust_package.pdf
    Invoke-WebRequest -Uri "$BASE_URL/trust_package.ja.pdf" -OutFile trust_package.ja.pdf
    Invoke-WebRequest -Uri "$BASE_URL/aimo-standard-artifacts.zip" -OutFile aimo-standard-artifacts.zip
    Invoke-WebRequest -Uri "$BASE_URL/SHA256SUMS.txt" -OutFile SHA256SUMS.txt
    ```

### 2. 验证校验和

=== "Linux"

    ```bash
    # 验证所有下载的文件与校验和
    sha256sum -c SHA256SUMS.txt

    # 预期输出（所有应显示"OK"）：
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "macOS"

    ```bash
    # 验证所有下载的文件与校验和
    shasum -a 256 -c SHA256SUMS.txt

    # 预期输出（所有应显示"OK"）：
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 验证每个文件
    Get-FileHash .\trust_package.pdf -Algorithm SHA256
    Get-FileHash .\trust_package.ja.pdf -Algorithm SHA256
    Get-FileHash .\aimo-standard-artifacts.zip -Algorithm SHA256

    # 将 Hash 输出与 SHA256SUMS.txt 进行比较
    Get-Content .\SHA256SUMS.txt
    ```

### 3. 手动验证（替代方法）

=== "Linux"

    ```bash
    # 计算特定文件的哈希
    sha256sum trust_package.pdf

    # 与 SHA256SUMS.txt 比较输出
    cat SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # 计算特定文件的哈希
    shasum -a 256 trust_package.pdf

    # 与 SHA256SUMS.txt 比较输出
    cat SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 计算特定文件的哈希
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # 查看校验和文件
    Get-Content .\SHA256SUMS.txt
    ```

!!! tip "审计师提示"
    始终直接从官方 GitHub Release 获取校验和文件，而不是从提交方获取。这确保独立验证。

### 4. 验证构建来源（证明）

所有发布资产包括由 GitHub Actions 生成的加密签名构建来源证明。这允许您验证资产是在官方仓库中构建的，没有被篡改。

**前提条件**：安装 [GitHub CLI](https://cli.github.com/)（`gh`）

```bash
# 使用 GitHub CLI 下载发布资产
VERSION=v0.0.1
gh release download "$VERSION" --repo billyrise/aimo-standard

# 验证每个资产的证明
gh attestation verify trust_package.pdf --repo billyrise/aimo-standard
gh attestation verify trust_package.ja.pdf --repo billyrise/aimo-standard
gh attestation verify aimo-standard-artifacts.zip --repo billyrise/aimo-standard
gh attestation verify SHA256SUMS.txt --repo billyrise/aimo-standard
```

**预期输出**（成功）：

```
Loaded digest sha256:abc123... for file trust_package.pdf
Loaded 1 attestation from GitHub API
✓ Verification succeeded!
```

**离线验证**（隔离环境）：

```bash
# 首先，下载可信根（需要一次网络）
gh attestation trusted-root > trusted-root.jsonl

# 然后离线验证
gh attestation verify trust_package.pdf \
  --repo billyrise/aimo-standard \
  --custom-trusted-root trusted-root.jsonl
```

!!! info "证明证明什么"
    构建来源证明加密证明发布资产：

    1. 由 GitHub Actions 构建（而非开发者的本地机器）
    2. 从官方 `billyrise/aimo-standard` 仓库构建
    3. 从与发布标签关联的确切提交构建
    4. 构建完成后未被修改

## 兼容性

AIMO 标准遵循 [语义版本控制](https://semver.org/)（SemVer）：

| 变更类型 | 版本升级 | 影响 |
| :---------- | :----------- | :----- |
| **MAJOR** | X.0.0 | 破坏性变更 — 需要迁移 |
| **MINOR** | 0.X.0 | 向后兼容的添加 |
| **PATCH** | 0.0.X | 修复和澄清 |

有关完整的版本控制政策，请参阅 [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)。

## 迁移

在版本之间升级时有破坏性变更：

1. 查看 [变更日志](../current/08-changelog.md) 了解破坏性变更
2. 查看 [迁移指南](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) 了解特定升级路径
3. 更新您的证据包以符合新的模式要求
4. 重新运行验证器以验证合规

!!! warning "破坏性变更"
    MAJOR 版本更新可能需要更改现有的证据包。在升级前始终查看迁移指南。

## 版本化文档快照

每个发布创建一个冻结的文档快照，可在以下位置访问：

- 生产：`https://standard.aimoaas.com/{version}/`（例如 `/0.0.1/`）
- GitHub Pages：`https://billyrise.github.io/aimo-standard/{version}/`

### URL 类型及其含义

| URL 模式 | 描述 | 用于审计引用？ |
|-------------|-------------|---------------------|
| `/X.Y.Z/`（例如 `/0.0.1/`） | **冻结版本** — 不可变快照 | **是**（首选） |
| `/latest/` | **别名** — 重定向到最新版本 | 是（解析到 `/X.Y.Z/`） |
| `/dev/` | **预览** — 未发布的主分支内容 | **否**（不用于引用） |

!!! warning "理解 `/latest/` 与 `/dev/`"
    - **`/latest/`** 是指向最新**发布**版本的别名（重定向）。它可以安全地用于引用，因为它解析到冻结快照。
    - **`/dev/`** 反映当前 `main` 分支，可能包含**未发布的更改**。永远不要在审计报告中引用 `/dev/`。

### 常见问题

??? question "为什么 `/latest/` 不是版本号？"
    `/latest/` 是一个方便的别名，始终重定向到最新的稳定版本（例如 `/0.0.1/`）。这允许用户收藏单个 URL，同时自动获取当前版本。对于需要不可变性的正式审计，改为引用显式版本 URL。

??? question "审计师应该引用哪个 URL？"
    - **正式审计（需要不可变性）**：使用 `/X.Y.Z/`（例如 `https://standard.aimoaas.com/0.0.1/standard/current/`）
    - **一般参考**：`/latest/` 可以接受，因为它重定向到当前版本
    - **永远不要引用**：`/dev/`（未发布，可能更改）

??? question "如果 `/latest/` 显示的内容与预期不同怎么办？"
    这将是部署错误。如果您怀疑 `/latest/` 与最新的 [GitHub Release](https://github.com/billyrise/aimo-standard/releases) 不同，请 [报告问题](https://github.com/billyrise/aimo-standard/issues)。`/latest/` 别名应始终重定向到最新的标记版本。

## 资源

- **[发布中心](../../releases/index.md)** — 提交准备、审计师验证、不过度声明声明
- **[信任包](../../governance/trust-package.md)** — 审计师就绪的保证材料
- **[变更日志（详细）](../current/08-changelog.md)** — 带弃用跟踪的完整变更历史
- **[VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)** — 完整版本控制政策
