---
description: 影子AI发现日志模式 - 用于记录企业中未经批准的AI使用的检测、清点和整改的厂商中立格式。
---

# 影子AI发现日志模式

## 用途

此模式定义了一种厂商中立的日志格式，用于记录**未经批准的AI使用（影子AI）**的检测、清点和整改。它使组织能够：

- 维护影子AI检测事件的可审计记录
- 将来自各种来源（CASB、代理、IdP、EDR、SaaS审计日志）的日志标准化为一致的格式
- 支持合规和审计目的的证据提交

## 标准化原则

| 原则 | 描述 |
| --- | --- |
| **厂商中立** | 不依赖特定厂商的日志格式；适用于 Netskope、Zscaler、Microsoft Defender 等 |
| **最小必需字段** | 只有必要字段是 MUST；组织可以省略可选字段 |
| **可扩展** | `additionalProperties: true` 允许厂商特定或组织特定的扩展 |
| **隐私意识** | 字段设计为引用（而非嵌入）敏感内容 |

## 必需字段（MUST）

| 字段 | 类型 | 描述 | 示例 |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | 事件时间戳 | `2026-01-15T09:30:00Z` |
| `actor_id` | string | 用户或服务标识符 | `user@example.com` |
| `actor_type` | string | 行为者类型 | `user` 或 `service` |
| `source_system` | string | 检测事件的系统 | `proxy`, `casb`, `idp`, `edr`, `saas_audit` |
| `ai_service` | string | 访问的AI产品或域名 | `chat.openai.com`, `claude.ai` |
| `action` | string | 执行的操作 | `chat`, `upload`, `download`, `tool_execute`, `api_call` |
| `data_classification` | string | 数据分类级别 | `public`, `internal`, `confidential`, `restricted` |
| `decision` | string | 应用的策略决策 | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | 相关证据的引用 | `sha256:abc123...` 或 `urn:evidence:...` |
| `record_id` | string | 此记录的唯一标识符 | `evt-20260115-001` |

## 可选字段（SHOULD/MAY）

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `session_id` | string | 会话标识符 |
| `device_id` | string | 设备标识符 |
| `ip` | string | IP地址 |
| `user_agent` | string | 用户代理字符串 |
| `department` | string | 组织部门 |
| `project_id` | string | 项目标识符 |
| `prompt_category` | string | 提示词/查询的类别 |
| `model_family` | string | AI模型系列（例如 GPT-4、Claude） |
| `destination` | string | 目标URL或端点 |
| `policy_id` | string | 触发决策的策略 |
| `remediation_ticket` | string | 整改工单引用 |

## 隐私/安全注意事项

!!! warning "数据处理"
    - **不要直接在日志字段中嵌入** PII、凭证或提示词内容。
    - 使用 `evidence_ref` 引用单独存储的敏感内容。
    - 对日志存储应用适当的访问控制。
    - 考虑与 [最低证据要求](../minimum-evidence.md) 对齐的数据保留策略。

## JSON Schema

下载：[shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "event_time", "actor_id", "actor_type", "source_system",
    "ai_service", "action", "data_classification", "decision",
    "evidence_ref", "record_id"
  ],
  "properties": {
    "event_time": { "type": "string", "format": "date-time" },
    "actor_id": { "type": "string", "minLength": 1 },
    "actor_type": { "type": "string", "enum": ["user", "service"] },
    "source_system": { "type": "string", "minLength": 1 },
    "ai_service": { "type": "string", "minLength": 1 },
    "action": { "type": "string", "minLength": 1 },
    "data_classification": { "type": "string", "minLength": 1 },
    "decision": { "type": "string", "enum": ["allow", "block", "needs_review", "unknown"] },
    "evidence_ref": { "type": "string", "minLength": 1 },
    "record_id": { "type": "string", "minLength": 1 }
  },
  "additionalProperties": true
}
```

## 相关页面

- [日志模式索引](index.md)
- [代理活动日志](agent-activity.md)
- [最低证据要求](../minimum-evidence.md)
- [分类法：IM-007 影子/非托管](../../standard/current/03-taxonomy.md)
