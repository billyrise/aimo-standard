---
description: 代理活動日誌格式 - 用於企業中代理式 AI 權限執行、工具執行和遞迴操作監控的廠商中立結構描述。
---
<!-- aimo:translation_status=translated -->

# 代理活動日誌格式

## 用途

此結構描述定義了一種廠商中立的格式，用於記錄**代理式 AI 權限執行、工具執行和遞迴操作**的日誌。它使組織能夠：

- 維護自主代理行為的可稽核記錄
- 追蹤「誰以什麼權限做了什麼」以用於合規性和事件調查
- 在稽核情境中支援代理式 AI 操作的可解釋性

## 事件模型

此結構描述支援四種事件類型，捕捉代理式操作生命週期：

| 事件類型 | 說明 |
| --- | --- |
| `agent_run` | 代理執行工作階段的開始或完成 |
| `tool_call` | 代理呼叫工具或外部動作 |
| `tool_result` | 工具呼叫返回的結果 |
| `escalation` | 代理請求人工介入或提升權限 |

## 必要欄位（MUST）

| 欄位 | 類型 | 說明 | 範例 |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | 事件的時間戳記 | `2026-01-15T09:30:00Z` |
| `agent_id` | string | 代理的識別碼 | `agent-coding-assistant-v2` |
| `agent_version` | string | 代理的版本 | `2.1.0` |
| `run_id` | string | 此次執行/工作階段的唯一識別碼 | `run-20260115-abc123` |
| `event_type` | string | 事件類型 | `agent_run`、`tool_call`、`tool_result`、`escalation` |
| `actor_id` | string | 發起的使用者或服務 | `user@example.com` |
| `tool_name` | string | 呼叫的工具名稱 | `file_write`、`api_call`、`shell_exec` |
| `tool_action` | string | 工具執行的動作 | `create`、`read`、`update`、`delete`、`execute` |
| `tool_target` | string | 動作的目標 | `/path/to/file`、`https://api.example.com` |
| `auth_context` | string | 權限/角色摘要 | `role:developer, scope:project-x` |
| `input_ref` | string | 輸入的雜湊或 URI（非內容本身） | `sha256:def456...` |
| `output_ref` | string | 輸出的雜湊或 URI（非內容本身） | `sha256:ghi789...` |
| `decision` | string | 套用的政策決策 | `allow`、`block`、`needs_review`、`unknown` |
| `evidence_ref` | string | 相關證據的參照 | `urn:evidence:...` |

## 選用欄位（SHOULD/MAY）

| 欄位 | 類型 | 說明 |
| --- | --- | --- |
| `recursion_depth` | number | 巢狀代理呼叫的目前遞迴深度 |
| `retry_count` | number | 此動作的重試次數 |
| `policy_id` | string | 觸發決策的政策 |
| `prompt_template_id` | string | 提示範本識別碼 |
| `model` | string | 此動作使用的模型 |
| `latency_ms` | number | 延遲時間（毫秒） |
| `cost_estimate` | number | 此動作的估計成本 |
| `error_code` | string | 動作失敗時的錯誤碼 |

## 安全注意事項

!!! warning "代理式風險假設"
    記錄代理式 AI 活動時，請假設以下風險：

    - **提示注入**：惡意輸入可能嘗試操縱代理行為
    - **過度權限**：代理可能擁有超出特定任務所需的更廣泛權限
    - **遞迴迴圈**：代理可能進入非預期的遞迴執行模式
    - **混淆代理人**：代理可能被欺騙而代表未授權方行動

    此結構描述旨在捕捉「誰以什麼權限做了什麼」以支援事後事件分析和稽核說明。它不能防止這些風險；組織必須實施適當的防護措施。

!!! warning "資料處理"
    - **請勿嵌入**機密、憑證或敏感內容到 `input_ref` 或 `output_ref`。
    - 使用雜湊參照或安全 URI 指向單獨儲存的內容。
    - 套用適當的存取控制和保留政策。

## JSON Schema

下載：[agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json)

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

## 相關頁面

- [日誌結構描述索引](../)
- [Shadow AI 發現日誌](../shadow-ai-discovery/)
- [最低證據要求](../../minimum-evidence/)
- [分類法：UC-010 代理式自動化](../../../standard/current/03-taxonomy/)
