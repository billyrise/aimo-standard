---
description: AIMO 日志模式 - 用于AI证据的厂商中立日志格式。包括影子AI发现和代理活动监控模式。
---

# 日志模式

## 这是什么

本节定义了可包含在证据包中的证据的**标准化日志格式**。这些模式为与AI使用监控和代理式操作相关的日志提供厂商中立的结构。

## 何时使用

- **影子AI可见性**：记录未经批准的AI使用的检测、清点和整改。
- **代理式操作审计**：解释自主代理的权限行使、工具执行和递归操作。
- **事件可重现性**：为事件调查和根因分析提供结构化证据。

## 这不是什么

!!! warning "重要提示"
    这些模式定义的是**用于证据提交的日志格式**。它们不会：

    - 自动从您的系统收集日志
    - 提供日志聚合或监控工具
    - 保证符合任何法规或标准
    - 替代厂商特定的日志实现

    组织必须实施自己的日志收集管道，并将日志标准化为这些模式以进行证据提交。

## 模式

| 模式 | 用途 | 下载 |
| --- | --- | --- |
| [影子AI发现日志](shadow-ai-discovery/) | 未经批准的AI使用检测和清点 | [shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json) |
| [代理活动日志](agent-activity/) | 代理式AI权限行使和工具执行 | [agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json) |

## 相关页面

- [最低证据要求](../minimum-evidence/) — MUST 级别证据清单
- [证据包](../evidence-bundle/) — 包结构和目录
- [分类法](../../standard/current/03-taxonomy/) — 分类代码（包括 UC-010 代理式自动化、IM-007 影子/非托管）
