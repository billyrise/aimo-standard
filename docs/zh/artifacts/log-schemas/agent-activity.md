---
description: 代理活动日志格式 - 用于企业中代理式AI权限行使、工具执行和递归操作监控的厂商中立模式。
---
<!-- aimo:translation_status=translated -->

# 代理活动日志格式

## 用途

此模式定义了一种厂商中立的日志格式，用于记录**代理式AI权限行使、工具执行和递归操作**。它使组织能够：

- 维护自主代理操作的可审计记录
- 追踪"谁用什么权限做了什么"以支持合规和事件调查
- 支持审计场景中代理式AI操作的可解释性

## 事件模型

该模式支持四种事件类型，捕获代理式操作的生命周期：

| 事件类型 | 描述 |
| --- | --- |
| `agent_run` | 代理执行会话的开始或完成 |
| `tool_call` | 代理调用工具或外部操作 |
| `tool_result` | 工具调用返回的结果 |
| `escalation` | 代理请求人工干预或提升权限 |

## 必需字段（MUST）

| 字段 | 类型 | 描述 | 示例 |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | 事件时间戳 | `2026-01-15T09:30:00Z` |
| `agent_id` | string | 代理标识符 | `agent-coding-assistant-v2` |
| `agent_version` | string | 代理版本 | `2.1.0` |
| `run_id` | string | 此次运行/会话的唯一标识符 | `run-20260115-abc123` |
| `event_type` | string | 事件类型 | `agent_run`, `tool_call`, `tool_result`, `escalation` |
| `actor_id` | string | 发起的用户或服务 | `user@example.com` |
| `tool_name` | string | 调用的工具名称 | `file_write`, `api_call`, `shell_exec` |
| `tool_action` | string | 工具执行的操作 | `create`, `read`, `update`, `delete`, `execute` |
| `tool_target` | string | 操作的目标 | `/path/to/file`, `https://api.example.com` |
| `auth_context` | string | 权限/角色摘要 | `role:developer, scope:project-x` |
| `input_ref` | string | 输入的哈希或URI（非内容本身） | `sha256:def456...` |
| `output_ref` | string | 输出的哈希或URI（非内容本身） | `sha256:ghi789...` |
| `decision` | string | 应用的策略决策 | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | 相关证据的引用 | `urn:evidence:...` |

## 可选字段（SHOULD/MAY）

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `recursion_depth` | number | 嵌套代理调用的当前递归深度 |
| `retry_count` | number | 此操作的重试次数 |
| `policy_id` | string | 触发决策的策略 |
| `prompt_template_id` | string | 提示词模板标识符 |
| `model` | string | 此操作使用的模型 |
| `latency_ms` | number | 延迟（毫秒） |
| `cost_estimate` | number | 此操作的估计成本 |
| `error_code` | string | 操作失败时的错误代码 |

## 安全注意事项

!!! warning "代理式风险假设"
    在记录代理式AI活动时，假设存在以下风险：

    - **提示词注入**：恶意输入可能试图操纵代理行为
    - **过度授权**：代理可能拥有比特定任务所需更广泛的权限
    - **递归循环**：代理可能进入意外的递归执行模式
    - **混淆代理**：代理可能被欺骗代表未授权方采取行动

    该模式旨在捕获"谁用什么权限做了什么"，以支持事后分析和审计解释。它不能防止这些风险；组织必须实施适当的防护措施。

!!! warning "数据处理"
    - **不要在** `input_ref` 或 `output_ref` 中嵌入密钥、凭证或敏感内容。
    - 使用哈希引用或安全URI指向单独存储的内容。
    - 应用适当的访问控制和保留策略。

## JSON Schema

下载：[agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "event_time", "agent_id", "agent_version", "run_id", "event_type",
    "actor_id", "tool_name", "tool_action", "tool_target", "auth_context",
    "input_ref", "output_ref", "decision", "evidence_ref"
  ],
  "properties": {
    "event_time": { "type": "string", "format": "date-time" },
    "agent_id": { "type": "string", "minLength": 1 },
    "agent_version": { "type": "string", "minLength": 1 },
    "run_id": { "type": "string", "minLength": 1 },
    "event_type": { "type": "string", "enum": ["agent_run", "tool_call", "tool_result", "escalation"] },
    "actor_id": { "type": "string", "minLength": 1 },
    "tool_name": { "type": "string", "minLength": 1 },
    "tool_action": { "type": "string", "minLength": 1 },
    "tool_target": { "type": "string", "minLength": 1 },
    "auth_context": { "type": "string", "minLength": 1 },
    "input_ref": { "type": "string", "minLength": 1 },
    "output_ref": { "type": "string", "minLength": 1 },
    "decision": { "type": "string", "enum": ["allow", "block", "needs_review", "unknown"] },
    "evidence_ref": { "type": "string", "minLength": 1 }
  },
  "additionalProperties": true
}
```

## 相关页面

- [日志模式索引](../)
- [影子AI发现日志](../shadow-ai-discovery/)
- [最低证据要求](../../minimum-evidence/)
- [分类法：UC-010 代理式自动化](../../../standard/current/03-taxonomy/)
