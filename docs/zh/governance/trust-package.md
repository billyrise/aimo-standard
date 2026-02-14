---
description: AIMO 信任包 - 审计师就绪材料包。审计师、法律和IT安全评估AI治理采用就绪性所需的最低文档。
---

# 信任包（保证包）

本页汇集了审计师、法律和IT安全评估采用就绪性所需的最低材料。
它只是一个中心；详细的证据目录和覆盖表在各自的部分中维护。

## 下载

**[下载信任包 PDF（最新发布）](https://github.com/billyrise/aimo-standard/releases/latest)**

信任包 PDF 将审计师就绪材料整合到单个文档中。每个 GitHub 发布包括：

- `trust_package.pdf` — 英文信任包
- `trust_package.ja.pdf` — 日文信任包
- `aimo-standard-artifacts.zip` — 模式、模板、示例、验证器规则
- `SHA256SUMS.txt` — 用于验证的校验和

## 您获得什么

- **符合性**：如何声明合规以及级别的含义 — [符合性](../conformance/index.md)
- **覆盖映射**：与外部标准的映射 — [覆盖映射索引](../coverage-map/index.md)、[覆盖映射方法论](../coverage-map/methodology.md)
- **标准**：规范性要求和定义 — [标准（当前版本）](../standard/current/index.md)
- **分类法**：AI治理的8维分类系统 — [分类法](../standard/current/03-taxonomy.md)、[代码](../standard/current/04-codes.md)、[字典](../standard/current/05-dictionary.md)
- **证据包**：结构、目录、可追溯性 — [证据包](../artifacts/evidence-bundle.md)
- **最低证据要求**：按生命周期的 MUST 级别清单 — [最低证据要求](../artifacts/minimum-evidence.md)
- **验证器**：规则和参考检查 — [验证器](../validator/index.md)
- **示例**：审计就绪的示例包 — [示例](../examples/index.md)
- **发布**：变更历史和分发 — [发布](../../releases/)
- **治理**：政策、安全、许可 — [治理](../governance/index.md)

## 审计就绪的最小集

| 项目 | 在哪里找到 | 结果/证明什么 |
| --- | --- | --- |
| 符合性级别 | [符合性](../conformance/index.md) | 如何声明合规以及所需证据的范围 |
| 覆盖映射 | [覆盖映射索引](../coverage-map/index.md)、[覆盖映射方法论](../coverage-map/methodology.md) | 针对外部法规和标准的可解释性 |
| 分类法与字典 | [分类法](../standard/current/03-taxonomy.md)、[代码](../standard/current/04-codes.md)、[字典](../standard/current/05-dictionary.md) | AI系统的分类系统（8个维度、91个代码） |
| 证据工件 | [证据包](../artifacts/evidence-bundle.md)、[最低证据](../artifacts/minimum-evidence.md)、[EV 模板](../standard/current/06-ev-template.md) | 支持可追溯性必须存在的数据 |
| 验证器检查 | [验证器](../validator/index.md) | 如何验证内部一致性和完整性 |
| 示例包 | [示例](../examples/index.md) | 实践中审计就绪包的样子 |
| 变更控制 | [发布](../../releases/)、[治理](../governance/index.md) | 如何管理和传达更新 |
| 安全/许可证/商标 | [治理](../governance/index.md) | 采用决策的法律和安全态势 |

## 如何引用

使用仓库 README 获取引用指南和背景；治理链接到权威政策。
请参阅 [README.md](https://github.com/billyrise/aimo-standard/blob/main/README.md) 和 [治理](../governance/index.md)。

## 工件 zip 内容

`aimo-standard-artifacts.zip` 包括：

- **分类法（SSOT）**：`source_pack/03_taxonomy/` — 字典 CSV（91个代码）、YAML、代码系统
- **JSON 模式**：`schemas/jsonschema/` — 机器可读验证模式
- **模板**：`templates/ev/` — 证据记录模板（JSON + Markdown）
- **示例**：`examples/` — 用于快速采用的最小示例包
- **覆盖映射**：`coverage_map/coverage_map.yaml` — 与外部标准的映射
- **验证器规则**：`validator/rules/` — 验证规则定义
- **治理文档**：`VERSIONING.md`、`GOVERNANCE.md`、`SECURITY.md`、`LICENSE.txt` 等

## 责任边界

AIMO 标准提供结构化的证据格式和可解释性框架。它**不**提供法律建议、合规认证、风险评估或审计执行。

有关完整的范围定义、假设和采用者责任，请参阅 [责任边界](responsibility-boundary.md)。

## 如何准备提交包

按照以下步骤准备审计就绪的提交：

1. **生成证据包**：按照 [证据包](../artifacts/evidence-bundle.md) 和 [最低证据要求](../artifacts/minimum-evidence.md) 创建 EV 记录、字典、摘要和变更日志。
2. **运行验证器**：执行 `python validator/src/validate.py bundle/root.json` 检查结构一致性。在继续之前修复任何错误。
3. **创建校验和**：为所有提交文件生成 SHA-256 校验和：

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
4. **打包工件**：创建证据包的 zip 存档：
   ```bash
   zip -r evidence_bundle.zip bundle_directory/
   ```
5. **引用发布版本**：记录您的包对齐的 AIMO 标准版本（例如 `v1.0.0`）。
6. **交付**：将 zip、校验和和版本引用提供给您的审计师或合规职能部门。

有关发布资产和验证，请参阅 [发布](../../releases/)。

## 不过度声明声明

!!! warning "重要提示"
    AIMO 标准支持**可解释性和证据就绪**。它**不**提供法律建议、保证合规或认证符合任何法规或框架。采用者必须根据权威文本验证声明，并在适当时获取专业建议。

有关范围、假设和采用者责任的详情，请参阅 [责任边界](responsibility-boundary.md)。

## 审计师：验证程序

收到证据提交时，审计师应使用以下步骤验证完整性和结构：

!!! success "构建来源可用"
    所有发布资产包括加密签名的构建证明。请参阅 [验证程序](../standard/versions/index.md#4-verify-build-provenance-attestation) 了解证明验证步骤。

### 步骤 1：验证校验和（SHA-256）

=== "Linux"

    ```bash
    # 下载或接收随提交的 SHA256SUMS.txt
    # 验证所有文件与其记录的校验和匹配
    sha256sum -c SHA256SUMS.txt

    # 或手动验证单个文件：
    sha256sum evidence_bundle.zip
    # 将输出与 SHA256SUMS.txt 中的值进行比较
    ```

=== "macOS"

    ```bash
    # 验证所有文件与其记录的校验和匹配
    shasum -a 256 -c SHA256SUMS.txt

    # 或手动验证单个文件：
    shasum -a 256 evidence_bundle.zip
    # 将输出与 SHA256SUMS.txt 中的值进行比较
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 验证单个文件
    Get-FileHash .\evidence_bundle.zip -Algorithm SHA256

    # 将 Hash 输出与 SHA256SUMS.txt 进行比较
    Get-Content .\SHA256SUMS.txt
    ```

如果任何校验和失败，应拒绝或重新请求提交。

### 步骤 2：验证包结构（验证器）

**前提条件**（一次性设置）：

```bash
# 克隆官方 AIMO 标准发布
git clone https://github.com/billyrise/aimo-standard.git
cd aimo-standard

# 重要：使用提交中声明的确切版本
# 将 VERSION 替换为提交者声明的版本（例如 v0.0.1）
VERSION=v0.0.1  # ← 匹配提交中的版本
git checkout "$VERSION"

# 设置 Python 环境
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

!!! warning "版本匹配"
    始终使用提交中声明的确切 AIMO 标准版本。使用不同版本可能会由于版本之间的模式或规则更改导致验证不匹配。

**运行验证**：

```bash
# 解压提交的包
unzip evidence_bundle.zip -d bundle/

# 对包的 root.json 运行验证器
python validator/src/validate.py bundle/root.json

# 预期输出："validation OK" 或错误列表
```

**示例**（使用内置样本）：

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

验证器检查：

- 必需文件存在（EV 记录、字典）
- JSON 文件符合模式
- 交叉引用（request_id、review_id 等）有效
- 时间戳存在且格式正确

### 步骤 3：验证版本对齐

检查提交是否引用了官方 AIMO 标准发布：

1. 确认声明的版本（例如 `v0.0.1`）存在于 [GitHub Releases](https://github.com/billyrise/aimo-standard/releases)
2. 将提交的模式与发布工件进行比较
3. 记录与官方发布的任何偏差

### 检查要点

| 检查 | 通过标准 | 失败操作 |
| --- | --- | --- |
| 校验和匹配 | 所有 `sha256sum -c` 检查通过 | 拒绝或重新请求 |
| 验证器通过 | `validate.py` 无错误 | 在接受前请求修复 |
| 版本存在 | 发布标签存在于 GitHub | 澄清版本对齐 |
| 必需字段存在 | EV 记录有 id、timestamp、source、summary | 请求完成 |
| 可追溯性完整 | 交叉引用正确解析 | 请求链接修复 |

!!! info "审计师独立性"
    审计师应直接从官方 AIMO 标准发布获取验证器和模式，而不是从提交方获取，以确保验证独立性。

## 审计旅程

从此页面，推荐的审计旅程是：

1. **分类系统**：[分类法](../standard/current/03-taxonomy.md) + [字典](../standard/current/05-dictionary.md) — 理解8维代码系统
2. **证据结构**：[证据包](../artifacts/evidence-bundle.md) — 理解包目录和可追溯性
3. **必需证据**：[最低证据要求](../artifacts/minimum-evidence.md) — 按生命周期的 MUST 级别清单
4. **框架对齐**：[覆盖映射](../coverage-map/index.md) + [方法论](../coverage-map/methodology.md) — 了解 AIMO 如何映射到外部框架
5. **验证**：[验证器](../validator/index.md) — 运行结构一致性检查
6. **下载**：[发布](../../releases/) — 获取发布资产并验证校验和
