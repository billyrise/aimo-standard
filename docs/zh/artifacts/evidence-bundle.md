---
description: AIMO 证据包结构。包含目录、可追溯性和工件的审计包格式，用于AI治理合规和审计交付。
---

# 证据包

**证据包**是一个审计包：一组结构化的工件，支持AI治理的可解释性和可追溯性。它不是产品功能，而是面向审计师和合规的交付格式。

## 包结构和命名

- **包根目录命名**：使用一致的命名模式，如 `{org}_{system}_{period}_{version}`（例如 `acme_ai-usage_2026-Q1_v1`）。
- **必需文件**：至少一个与 [Evidence Pack 模板（EP）](../standard/current/06-ev-template.md) 对齐的证据（EV）集、一个 [字典](../standard/current/05-dictionary.md)、一个简短的 **摘要**（包的执行摘要）以及一个 **变更日志**（或其引用），用于记录包或其内容的变更。
- **可选附件**：日志、审查记录、例外批准、续期记录；保持命名一致，并可从主 EV/字典中引用。

## 目录（TOC）

| 部分 | 工件 | 是否必需？ | 用途 | 最小字段 | 验证 |
| --- | --- | --- | --- | --- | --- |
| 证据 | EV 记录（JSON/数组） | 是 | 记录发生的事情；链接到请求/审查/例外/续期 | id, timestamp, source, summary; 可选生命周期引用 | [验证器](../validator/index.md), aimo-ev.schema.json |
| 字典 | dictionary.json | 是 | 代码和维度的键/标签/描述 | entries (key, label, description) | aimo-dictionary.schema.json |
| 摘要 | summary（文档或字段） | 是 | 面向审计师的一页概览 | scope, period, key decisions, exceptions | — |
| 变更日志 | change_log 或引用 | 是 | 包/内容变更的审计跟踪 | id, timestamp, actor, change description, references | — |
| 请求 | request 记录 | 如适用 | 使用申请/请求 | id, timestamp, actor/role, scope, rationale | — |
| 审查/批准 | review 记录 | 如适用 | 审查和批准结果 | id, timestamp, actor/role, decision, references | — |
| 例外 | exception 记录 | 如适用 | 带补偿控制和到期日的例外 | id, timestamp, scope, expiry, compensating controls, renewal ref | — |
| 续期 | renewal 记录 | 如适用 | 重新评估和续期 | id, timestamp, actor/role, decision, references to prior exception/EV | — |

## 规范关系：EV 记录（索引）与 Evidence Pack（payload）

为避免双重构建与审计歧义，以下为**规范**：(1) EV 记录（JSON）为**索引/台账**（可机器验证的可追溯性）。(2) Evidence Pack 文件（EP-01..EP-07 及清单）为 **payload**。(3) EV 记录应通过 `evidence_file_ids`（如 EP-01）和/或哈希引用 payload；[Validator](../validator/index.md) 检查引用完整性。(4) **最小提交集**：EV JSON + Dictionary + Summary + Change Log + Evidence Pack（zip）。参见 [Evidence Pack 模板](../standard/current/06-ev-template.md) 了解 EP-01..EP-07 文档类型。

## 可追溯性

- **稳定ID**：每条记录（EV、请求、审查、例外、续期、变更日志条目）必须具有稳定、唯一的标识符。
- **交叉引用**：将 请求 → 审查 → 例外（如有）→ 续期 链接起来，并通过引用字段（如 `request_id`、`review_id`、`exception_id`、`renewal_id`）将 EV 条目链接到这些记录。
- **链接**：确保审计师可以从AI使用（或例外）追溯到请求、批准、任何例外及其补偿控制和到期日，以及续期。

## 审计师如何使用

审计师使用证据包来验证AI使用是经过请求、审查和批准的；例外是有时限的，并有补偿控制和续期；变更已记录。目录和可追溯性规则让他们能够定位所需工件，并跨请求、审查、例外、续期和 EV 记录追踪ID和引用。摘要提供快速概览；变更日志支持变更控制和问责。

请参阅 [最低证据要求](minimum-evidence.md) 了解 MUST 级别字段和生命周期组。

## 操作指南

!!! info "完整性和访问控制"
    虽然 AIMO 不规定具体控制措施，但采用者应记录：
    
    - **访问角色**：谁可以创建、读取、更新或删除证据
    - **保留策略**：证据保留多长时间以及按什么计划
    - **完整性机制**：使用的哈希、WORM 存储或数字签名
    - **审计跟踪**：对包的访问和变更日志
    
    请参阅 [最低证据要求 > 完整性与访问](minimum-evidence.md#6-integrity-access) 获取详细指南。

## 审计旅程

从此页面开始，典型的审计旅程继续：

1. **下一步**：[最低证据要求](minimum-evidence.md) — 按生命周期的 MUST 级别清单
2. **然后**：[覆盖映射](../coverage-map/index.md) — 与外部框架的映射
3. **验证**：[验证器](../validator/index.md) — 运行结构检查
4. **下载**：[发布](../releases/index.md) — 获取发布资产并验证校验和
