---
description: Shadow AI 發現日誌結構描述 - 用於記錄企業中未經核准 AI 使用的偵測、清查和補救的廠商中立格式。
---
<!-- aimo:translation_status=translated -->

# Shadow AI 發現日誌結構描述

## 用途

此結構描述定義了一種廠商中立的格式，用於記錄**未經核准 AI 使用（Shadow AI）**的偵測、清查和補救。它使組織能夠：

- 維護 Shadow AI 偵測事件的可稽核記錄
- 將來自各種來源（CASB、代理、IdP、EDR、SaaS 稽核日誌）的日誌標準化為一致的格式
- 支援合規性和稽核目的的證據提交

## 標準化原則

| 原則 | 說明 |
| --- | --- |
| **廠商中立** | 不依賴特定廠商日誌格式；適用於 Netskope、Zscaler、Microsoft Defender 等 |
| **最少必要欄位** | 只有必要欄位是 MUST；組織可省略選用欄位 |
| **可擴展** | `additionalProperties: true` 允許廠商特定或組織特定的擴展 |
| **隱私意識** | 欄位設計為參照（而非嵌入）敏感內容 |

## 必要欄位（MUST）

| 欄位 | 類型 | 說明 | 範例 |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | 事件的時間戳記 | `2026-01-15T09:30:00Z` |
| `actor_id` | string | 使用者或服務識別碼 | `user@example.com` |
| `actor_type` | string | 行為者類型 | `user` 或 `service` |
| `source_system` | string | 偵測到事件的系統 | `proxy`、`casb`、`idp`、`edr`、`saas_audit` |
| `ai_service` | string | 存取的 AI 產品或網域 | `chat.openai.com`、`claude.ai` |
| `action` | string | 執行的動作 | `chat`、`upload`、`download`、`tool_execute`、`api_call` |
| `data_classification` | string | 資料分類等級 | `public`、`internal`、`confidential`、`restricted` |
| `decision` | string | 套用的政策決策 | `allow`、`block`、`needs_review`、`unknown` |
| `evidence_ref` | string | 相關證據的參照 | `sha256:abc123...` 或 `urn:evidence:...` |
| `record_id` | string | 此記錄的唯一識別碼 | `evt-20260115-001` |

## 選用欄位（SHOULD/MAY）

| 欄位 | 類型 | 說明 |
| --- | --- | --- |
| `session_id` | string | 工作階段識別碼 |
| `device_id` | string | 裝置識別碼 |
| `ip` | string | IP 位址 |
| `user_agent` | string | 使用者代理字串 |
| `department` | string | 組織部門 |
| `project_id` | string | 專案識別碼 |
| `prompt_category` | string | 提示/查詢的類別 |
| `model_family` | string | AI 模型系列（例如 GPT-4、Claude） |
| `destination` | string | 目標 URL 或端點 |
| `policy_id` | string | 觸發決策的政策 |
| `remediation_ticket` | string | 補救工單參照 |

## 隱私/安全注意事項

!!! warning "資料處理"
    - **請勿嵌入** PII、憑證或提示內容到日誌欄位中。
    - 使用 `evidence_ref` 參照單獨儲存的敏感內容。
    - 對日誌儲存套用適當的存取控制。
    - 考慮與[最低證據要求](../../minimum-evidence/)一致的資料保留政策。

## JSON Schema

下載：[shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json)

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

## 相關頁面

- [日誌結構描述索引](../)
- [代理活動日誌](../agent-activity/)
- [最低證據要求](../../minimum-evidence/)
- [分類法：IM-007 Shadow/未受管理](../../../standard/current/03-taxonomy/)
