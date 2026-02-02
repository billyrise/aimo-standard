---
description: AIMO 证据包模板和使用指南。用于记录AI治理证据的结构，包括索引管理和审计就绪格式。
---

# Evidence Pack 模板（EP）

本节定义证据包模板及其使用。证据包是一组文档的集合，用于展示AI系统的治理和合规。

## 命名空间：Evidence Pack 文档类型（EP）与 Taxonomy Evidence Type（EV）

> **重要**：**EP-01..EP-07** 表示*文档类型*（证据包文件类型）。**EV-001、EV-002、…** 在[分类法](./03-taxonomy.md)中表示*事件/证据类型*（请求记录、审查/批准记录等）。请勿混用代码：EP 用于包结构，EV 用于生命周期证据分类。

## 关键原则：索引和差异管理

重要的不仅是单个提交的内容，而是证据项之间的**索引**和**差异管理**。

证据包作为将AI系统链接到其治理工件的索引。其价值在于：

1. **可追溯性**：跨时间链接决策、批准和变更
2. **可审计性**：使审计师能够导航证据结构
3. **可维护性**：跟踪什么变了、何时变的、为什么变

## MVP 证据集（EP-01 到 EP-07）

以下七种 **Evidence Pack 文档类型**（EP）构成展示AI治理的**最小可行集**。每种为文档模板；分类法 **EV** 代码（请求记录、审查/批准等）在包内及 `codes.EV` 中用于对*事件*证据进行分类。

| ID | 文档类型 | 目的 |
| --- | --- | --- |
| EP-01 | 系统概述 | 记录AI系统及其目的 |
| EP-02 | 数据流 | 映射系统中的数据移动 |
| EP-03 | 清单 | 维护AI资产目录 |
| EP-04 | 风险与影响评估 | 评估和记录风险 |
| EP-05 | 控制与批准 | 记录控制和批准记录 |
| EP-06 | 日志与监控 | 定义日志和监控设置 |
| EP-07 | 事件与例外 | 跟踪事件和例外 |

## 证据包清单

每个证据包必须包含一个清单文件，包含：

### 必需元数据

| 字段 | 描述 | 必需 |
| --- | --- | --- |
| `pack_id` | 唯一标识符（例如 EP-EXAMPLE-001） | 是 |
| `pack_version` | 包的 SemVer 版本 | 是 |
| `taxonomy_version` | 使用的 AIMO 分类法版本 | 是 |
| `created_date` | 包创建日期 | 是 |
| `last_updated` | 最后更新日期 | 是 |
| `owner` | 负责方 | 是 |

### AIMO 代码（8个维度）

每个证据包必须包含所有8个维度的代码。**EV** 维度列出适用于本包的*分类法*证据类型（如请求记录、审查/批准），而非文档类型代码。文档类型由 `evidence_files[].file_id`（EP-01..EP-07）给出。

```json
{
  "codes": {
    "FS": ["FS-001"],
    "UC": ["UC-001", "UC-002"],
    "DT": ["DT-002"],
    "CH": ["CH-001"],
    "IM": ["IM-001"],
    "RS": ["RS-001", "RS-003"],
    "OB": ["OB-001"],
    "EV": ["EV-001", "EV-002", "EV-008", "EV-009"]
  }
}
```

### 证据文件列表

每条记录通过 **file_id**（EP-01..EP-07）标识包内文档。可选 **ev_codes** 可列出该文档支持的分类法 EV 代码（EV-xxx）。

```json
{
  "evidence_files": [
    {
      "file_id": "EP-01",
      "filename": "EP-01_system_overview.md",
      "title": "System Overview",
      "required": true
    }
  ]
}
```

## 模板结构

每个证据模板包括：

1. **必需元数据块** - pack_id、版本、taxonomy_version、日期、owner
2. **AIMO 代码表** - 所有8个维度及适用代码
3. **内容部分** - 领域特定的文档部分
4. **参考** - 相关证据的链接
5. **修订历史** - 变更跟踪

### 模板头部示例

```markdown
# EP-01: 系统概述

---

## 必需元数据

| 字段 | 值 |
| --- | --- |
| **pack_id** | `EP-EXAMPLE-001` |
| **pack_version** | `0.1.0` |
| **taxonomy_version** | `0.1.0` |
| **created_date** | `2026-01-31` |
| **last_updated** | `2026-01-31` |
| **owner** | `AI Governance Team` |

---

## AIMO 代码（8个维度）

| 维度 | 代码 | 标签 |
| --- | --- | --- |
| **FS** | `FS-001` | 最终用户生产力 |
| **UC** | `UC-001` | 通用问答 |
| **DT** | `DT-002` | 内部 |
| **CH** | `CH-001` | Web UI |
| **IM** | `IM-001` | 独立 |
| **RS** | `RS-001` | 数据泄露 |
| **OB** | `OB-001` | 效率 |
| **EV** | `EV-001`, `EV-002` | 请求记录、审查/批准记录 |
```

## 下载

### 模板

证据包模板在仓库中提供。清单中请使用 **file_id** EP-01..EP-07；文件名可为 EP-01_... 或兼容的 EV-01_...。

- `source_pack/04_evidence_pack/templates/EV-01_system_overview.md` → file_id **EP-01**
- `source_pack/04_evidence_pack/templates/EV-02_data_flow.md` → file_id **EP-02**
- `source_pack/04_evidence_pack/templates/EV-03_inventory.md` → file_id **EP-03**
- `source_pack/04_evidence_pack/templates/EV-04_risk_impact.md` → file_id **EP-04**
- `source_pack/04_evidence_pack/templates/EV-05_controls_approvals.md` → file_id **EP-05**
- `source_pack/04_evidence_pack/templates/EV-06_logging_monitoring.md` → file_id **EP-06**
- `source_pack/04_evidence_pack/templates/EV-07_incident_exception.md` → file_id **EP-07**

### 模式和示例

- 模式：`source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json`
- 示例：`source_pack/04_evidence_pack/examples/evidence_pack_manifest.example.json`

请参阅 [发布](../../releases/index.md) 获取可下载的包。

## 分发模式

> **注意**：主要分发目标是**审计公司和系统集成商**（模板分发者），而非个别企业。

模板设计为：

1. 被审计师和顾问作为标准工件采用
2. 分发给企业，保留来源归属
3. 与 AIMO 标准一起版本化

企业通过其审计师、顾问或内部治理团队接收模板，这些团队维护与标准版本的链接。

## 参考

- [分类法](./03-taxonomy.md) - 维度定义
- [代码](./04-codes.md) - 代码格式
- [验证器](./07-validator.md) - 验证规则
- [证据包](../../artifacts/evidence-bundle.md) - 包结构
