---
description: AIMO 本地化指南 - 多语言文档的国际化结构、维护工作流程和单一事实来源原则。
---

# 本地化指南

本页记录了 AIMO 标准文档的本地化（i18n）结构、维护工作流程和 SSOT（单一事实来源）原则。

## 语言纯净策略

**每个语言页面应仅包含该语言的内容。**

| 规则 | 描述 |
| --- | --- |
| **EN 页面** | 不得包含 CJK 字符或语言特定列的引用（如 `_ja` 后缀） |
| **JA 页面** | 不得将 EN 特定术语解释为规范结构 |
| **例外** | 列在 `tooling/checks/lint_i18n.py` 的 `MIXED_LANGUAGE_ALLOWLIST` 中 |

此策略确保：
1. 读者只看到所选语言的内容
2. 添加新语言不需要更新现有页面
3. CI 可以自动检测违规

## 语言结构

AIMO 标准文档使用**基于文件夹的国际化结构**：

```
docs/
├── en/           # 英语（规范）
├── ja/           # 日语（日本語）
├── es/           # 西班牙语（Español）
├── fr/           # 法语（Français）
├── de/           # 德语（Deutsch）
├── pt/           # 葡萄牙语（Português）
├── it/           # 意大利语（Italiano）
├── zh/           # 简体中文（简体中文）
├── zh-TW/        # 繁体中文（繁體中文）
└── ko/           # 韩语（한국어）
```

- **英语是规范的**：`docs/en/` 文件夹是文档内容的权威来源。
- **其他语言镜像结构**：每个语言文件夹（`ja/` 等）与 `en/` 保持相同的文件结构。
- **相同的文件名**：所有语言使用 `.md` 扩展名（文件名中没有语言后缀）。
- **回退到英语**：缺失的翻译会自动回退到英语内容。

## 分类法数据模型

分类法使用**语言中立的规范结构**和单独的翻译包：

```
data/
└── taxonomy/
    ├── canonical.yaml           # 语言中立（代码、状态、生命周期）
    └── i18n/
        ├── en.yaml              # 英语标签和定义
        ├── ja.yaml              # 日语标签和定义
        └── {lang}.yaml          # 其他语言（空模板）
```

### 规范结构（`canonical.yaml`）

包含语言中立的数据：

- 代码标识符（例如 `FS-001`、`UC-001`）
- 状态（`active`、`deprecated`、`removed`）
- 生命周期元数据（`introduced_in`、`deprecated_in`、`removed_in`、`replaced_by`）
- 范围说明和示例（英语，作为技术参考）

### 翻译包（`i18n/*.yaml`）

每个语言包包含：

- 维度名称（例如"功能范围"）
- 代码标签（例如"最终用户生产力"）
- 代码定义

**回退**：如果缺少翻译，系统使用英语。

## SSOT 原则

AIMO 对分类法数据使用 **SSOT 优先架构**：

| 资产类型 | SSOT 位置 | 描述 |
| --- | --- | --- |
| **分类法（结构）** | `data/taxonomy/canonical.yaml` | 语言中立结构（SSOT） |
| **分类法（i18n）** | `data/taxonomy/i18n/*.yaml` | 每种语言的翻译（SSOT） |
| **覆盖映射** | `coverage_map/coverage_map.yaml` | 框架到证据的映射 |
| **模式** | `schemas/jsonschema/` | JSON 验证模式 |

### 派生文件

以下文件是从 SSOT **生成**的，不应手动编辑：

| 文件 | 生成自 | 生成器 |
| --- | --- | --- |
| `artifacts/taxonomy/{version}/{lang}/taxonomy_dictionary.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_en.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_ja.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/code_system.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/dimensions_en_ja.md` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_dictionary.json` | canonical + i18n | `build_artifacts.py` |

### 语言代码（BCP47）

AIMO 使用 BCP47 语言代码：

| 代码 | 语言 | 状态 |
| --- | --- | --- |
| `en` | 英语 | 规范（源） |
| `ja` | 日语（日本語） | 活跃 |
| `es` | 西班牙语（Español） | 活跃 |
| `fr` | 法语（Français） | 活跃 |
| `de` | 德语（Deutsch） | 活跃 |
| `pt` | 葡萄牙语（Português） | 活跃 |
| `it` | 意大利语（Italiano） | 活跃 |
| `zh` | 简体中文（简体中文） | 活跃 |
| `zh-TW` | 繁体中文（繁體中文） | 活跃 |
| `ko` | 韩语（한국어） | 活跃 |

### 旧版 CSV 文件（已冻结）

`source_pack/03_taxonomy/legacy/` 中的旧版 EN/JA 混合 CSV 文件：

- **冻结在 21 列** — 不会添加新的语言列
- **为向后兼容而维护** — 现有集成可以继续使用它们
- **CI 强制执行** — 添加 `label_es`、`definition_de` 等会导致构建失败

对于新语言，请使用 `artifacts/taxonomy/{version}/{lang}/` 中的每种语言工件。

## 翻译新鲜度跟踪

AIMO 使用**翻译新鲜度跟踪**系统来维护英语（源）和翻译内容之间的一致性。

### 工作原理

1. 每个翻译文件包含跟踪它是从哪个版本的英语源翻译的元数据
2. 当英语内容更新时，系统检测过时的翻译
3. CI 对过时的翻译发出警告但不阻止（翻译可以滞后）

### 翻译元数据

翻译文件包含前言元数据：

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
# 检查所有翻译的新鲜度
python tooling/i18n/sync_translations.py --check

# 检查特定语言
python tooling/i18n/sync_translations.py --check --lang ja

# 生成翻译报告
python tooling/i18n/sync_translations.py --report

# 初始化新语言（复制 EN 作为基础）
python tooling/i18n/sync_translations.py --init-lang es

# 完成翻译后更新元数据
python tooling/i18n/sync_translations.py --update-meta docs/ja/index.md
```

有关详细技术规范，请参阅 `tooling/i18n/TRANSLATION_SYNC_SPEC.md`。

## 更新工作流程

### 分类法更新（新的 SSOT 优先工作流程）

1. 编辑 `data/taxonomy/` 中的 SSOT：
   - 结构变更 → `canonical.yaml`
   - 英语翻译 → `i18n/en.yaml`
   - 日语翻译 → `i18n/ja.yaml`
2. 运行验证：`python tooling/checks/lint_taxonomy_ssot.py`
3. 重新生成所有派生文件：`python tooling/taxonomy/build_artifacts.py --version current --langs en ja`
4. 根据需要更新文档页面
5. 一起提交所有变更

### 覆盖映射更新

1. 编辑 `coverage_map/coverage_map.yaml`（SSOT）
2. 更新相应的框架页面表格（`docs/en/coverage-map/*.md`）
3. 更新日语翻译（`docs/ja/coverage-map/*.md`）
4. 一起提交所有变更

### 文档更新

1. 编辑英语源（`docs/en/...`）
2. 根据需要更新翻译（或标记为稍后更新）
3. 运行 `python tooling/i18n/sync_translations.py --check` 查看过时的翻译
4. 运行 `python tooling/checks/lint_i18n.py` 验证标题一致性
5. 运行 `mkdocs build --strict` 验证构建
6. 一起提交所有变更

!!! note "翻译优先级"
    并非所有翻译都需要立即更新。一级（关键）页面应优先处理：
    
    - `index.md`
    - `standard/current/*.md`
    - `governance/index.md`
    - `releases/`

## 添加新语言（5 步）

要添加新语言（例如西班牙语）：

### 步骤 1：生成分类法包

```bash
python tooling/taxonomy/build_i18n_taxonomy.py --add-lang es --lang-name "Español"
```

创建 `data/taxonomy/i18n/es.yaml`，并以英语引用作为注释。

### 步骤 2：创建文档文件夹

```bash
mkdir -p docs/es && cp -r docs/en/* docs/es/
```

### 步骤 3：更新 mkdocs.yml

```yaml
plugins:
  - i18n:
      languages:
        - locale: es
          name: Español
          build: true
```

### 步骤 4：翻译

- 翻译 `data/taxonomy/i18n/es.yaml`
- 翻译 `docs/es/` 中的文件

### 步骤 5：验证

```bash
python tooling/checks/lint_i18n.py && mkdocs build --strict
```

!!! success "完成"
    新语言现在可在 `/dev/es/` 访问

## 文件命名约定

| 模式 | 示例 | 描述 |
| --- | --- | --- |
| `index.md` | `docs/en/governance/index.md` | 章节首页 |
| `{topic}.md` | `docs/en/governance/trust-package.md` | 主题页面 |
| `{NN}-{topic}.md` | `docs/en/standard/current/03-taxonomy.md` | 编号规范页面 |

## 质量检查

提交前运行这些检查：

```bash
# i18n 结构、标题一致性和废弃短语检测
python tooling/checks/lint_i18n.py

# 模式和清单检查
python tooling/checks/lint_schema.py
python tooling/checks/lint_manifest.py

# 分类法 SSOT 检查
python tooling/checks/lint_taxonomy_ssot.py --required-langs en
python tooling/checks/lint_legacy_csv.py
python tooling/checks/lint_taxonomy_dictionary.py
python tooling/checks/lint_taxonomy_json.py

# 分类法工件是否最新
python tooling/taxonomy/build_artifacts.py --check

# 构建验证
mkdocs build --strict
```

## 相关页面

- [发布](../../releases/) — 可下载的包
- [治理](../../governance/) — 项目治理
