---
description: AIMO 标准发布 - 下载版本化的PDF、工件和校验和。变更日志、迁移指南和构建来源证明。
---

# 发布

本节是版本化发布、变更日志、迁移和分发工件的中心。

## 下载最新发布

**[GitHub Releases](https://github.com/billyrise/aimo-standard/releases/latest)** — 此为“latest”发布的单一事实来源。站点路径 `/latest/` 会重定向到同一版本。

## 验证程序（永久网页）

完整的**验证程序**（下载资产、校验和验证、构建来源证明）以永久网页形式提供，不仅限于 PDF：

- **[Standard → 版本 → 验证程序](../standard/versions/)** — 分步校验和验证（Linux/macOS/Windows）及来源证明。

在需要验证发布资产或在审计交付物中记录验证步骤时，请使用本页。

## 发布资产

每个官方发布（`vX.Y.Z` 标签）包括：

| 资产 | 描述 |
| --- | --- |
| `trust_package.pdf` | 英文信任包 — 审计师就绪的保证材料 |
| `trust_package.ja.pdf` | 日文信任包 |
| `aimo-standard-artifacts.zip` | 模式、模板、示例、验证器规则 |
| `SHA256SUMS.txt` | 所有资产的 SHA-256 校验和 |

### 验证下载

下载后，使用校验和验证文件完整性：

=== "Linux"

    ```bash
    # 下载校验和文件
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # 验证特定文件
    sha256sum -c SHA256SUMS.txt --ignore-missing

    # 或手动验证：
    sha256sum trust_package.pdf
    # 将输出与 SHA256SUMS.txt 进行比较
    ```

=== "macOS"

    ```bash
    # 下载校验和文件
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # 验证特定文件
    shasum -a 256 -c SHA256SUMS.txt

    # 或手动验证：
    shasum -a 256 trust_package.pdf
    # 将输出与 SHA256SUMS.txt 进行比较
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 下载校验和文件
    Invoke-WebRequest -Uri "https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt" -OutFile SHA256SUMS.txt

    # 验证特定文件
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # 将 Hash 输出与 SHA256SUMS.txt 进行比较
    Get-Content .\SHA256SUMS.txt
    ```

## 工件 Zip 内容

`aimo-standard-artifacts.zip` 包含：

- `schemas/jsonschema/*` — 用于验证的 JSON Schema
- `templates/ev/*` — 证据模板（JSON + Markdown）
- `examples/*` — 示例证据包
- `coverage_map/coverage_map.yaml` — 外部标准映射
- `validator/rules/*` — 验证规则定义
- `VERSIONING.md`、`GOVERNANCE.md`、`SECURITY.md` 等

## 资源

- **版本历史表**：[标准 > 版本](../standard/versions/) — 带有所有发布资产（PDF、ZIP、SHA256）直接链接的版本表
- **变更日志（规范）**：[标准 > 当前 > 变更日志](../standard/current/08-changelog/) — 规范性和非规范性变更历史。
- **发布流程**：标记 `vX.Y.Z`、CI 构建、`dist/` 下的 PDF、校验和、GitHub Release 资产。参见仓库中的 [GOVERNANCE.md](https://github.com/billyrise/aimo-standard/blob/main/GOVERNANCE.md) 和 [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)。
- **迁移指南**：[MIGRATION.md](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) — 破坏性变更的升级路径。

有关治理和版本管理政策，请参阅 [治理](../governance/)。

## 准备您的提交包

准备审计提交的证据时：

1. **创建您的证据包**：按照 [证据包](../artifacts/evidence-bundle/) 和 [最低证据要求](../artifacts/minimum-evidence/) 创建 EV 记录、字典、摘要和变更日志。
2. **运行验证器**：执行 `python validator/src/validate.py bundle/root.json` 检查结构一致性。在继续之前修复所有错误。
3. **生成校验和**：创建 SHA-256 校验和用于验证：

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
4. **打包**：创建您的包目录的 zip 存档。
5. **记录版本对齐**：记录您的证据对齐的 AIMO 标准发布版本（例如 `v1.0.0`）。
6. **交付**：将包、校验和和版本引用提供给您的审计师。

有关完整的准备指南，请参阅 [信任包](../governance/trust-package/)。

## 审计师：验证程序

收到证据提交的审计师应验证完整性和结构：

1. **验证校验和**：运行校验和验证（Linux：`sha256sum -c`、macOS：`shasum -a 256 -c`、Windows：`Get-FileHash`）以确认文件完整性
2. **运行验证器**：执行 `python validator/src/validate.py bundle/root.json` 检查结构
3. **确认版本**：验证声明的 AIMO 标准版本存在于 [GitHub Releases](https://github.com/billyrise/aimo-standard/releases)

!!! tip "独立获取工具"
    审计师应直接从官方 AIMO 标准发布下载验证器和模式，而不是从提交方获取。

有关完整的验证程序（校验和、证明、分步），请参阅 **[Standard → 版本 → 验证程序](../standard/versions/)**。另见 [信任包](../governance/trust-package/) 获取审计就绪材料。

## 不过度声明声明

!!! warning "重要提示"
    AIMO 标准支持**可解释性和证据就绪**。它**不**提供法律建议、保证合规或认证符合任何法规或框架。采用者必须根据权威文本验证声明，并在适当时获取专业建议。

有关范围、假设和采用者责任，请参阅 [责任边界](../governance/responsibility-boundary/)。
