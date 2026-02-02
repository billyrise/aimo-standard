---
description: AIMO 证据包模板和使用指南。用于记录AI治理证据的结构，包括索引管理和审计就绪格式。
---

# EV 模板

本节定义证据包模板及其使用。证据包是一组文档的集合，用于展示AI系统的治理和合规。

## 关键原则：索引和差异管理

> **重要**：重要的不是单个提交的内容，而是证据项之间的**索引**和**差异管理**。

证据包作为将AI系统链接到其治理工件的索引。其价值在于：

1. **可追溯性**：跨时间链接决策、批准和变更
2. **可审计性**：使审计师能够导航证据结构
3. **可维护性**：跟踪什么变了、何时变的、为什么变

## MVP 证据集（EV-01 到 EV-07）

以下七种证据类型构成展示AI治理的**最小可行集**：

| ID | 证据类型 | 代码 | 目的 |
| --- | --- | --- | --- |
| EV-01 | 系统概述 | EV-001 | 记录AI系统及其目的 |
| EV-02 | 数据流 | EV-002 | 映射系统中的数据移动 |
| EV-03 | 清单 | EV-003 | 维护AI资产目录 |
| EV-04 | 风险与影响评估 | EV-004 | 评估和记录风险 |
| EV-05 | 控制与批准 | EV-005 | 记录控制和批准记录 |
| EV-06 | 日志与监控 | EV-006 | 定义日志和监控设置 |
| EV-07 | 事件与例外 | EV-007 | 跟踪事件和例外 |

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

每个证据包必须包含所有8个维度的代码：

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
    "EV": ["EV-001", "EV-002", "EV-003", "EV-004", "EV-005", "EV-006", "EV-007"]
  }
}
```

### 证据文件列表

```json
{
  "evidence_files": [
    {
      "file_id": "EV-01",
      "filename": "EV-01_system_overview.md",
      "ev_type": "EV-001",
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
# EV-01: 系统概述

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
| **EV** | `EV-001` | 系统概述 |
```

## 下载

### 模板

证据包模板可在以下位置获取：

- `source_pack/04_evidence_pack/templates/EV-01_system_overview.md`
- `source_pack/04_evidence_pack/templates/EV-02_data_flow.md`
- `source_pack/04_evidence_pack/templates/EV-03_inventory.md`
- `source_pack/04_evidence_pack/templates/EV-04_risk_impact.md`
- `source_pack/04_evidence_pack/templates/EV-05_controls_approvals.md`
- `source_pack/04_evidence_pack/templates/EV-06_logging_monitoring.md`
- `source_pack/04_evidence_pack/templates/EV-07_incident_exception.md`

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
