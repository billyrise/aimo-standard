---
description: Agent Activity Log Format - Vendor-neutral schema for agentic AI privilege exercise, tool execution, and recursive operation monitoring in enterprises.
---
<!-- aimo:translation_status=source -->

# Agent Activity Log Format

## Purpose

This schema defines a vendor-neutral format for logs that document **agentic AI privilege exercise, tool execution, and recursive operations**. It enables organizations to:

- Maintain an auditable record of autonomous agent actions
- Track "who did what with what authority" for compliance and incident investigation
- Support explainability for agentic AI operations in audit contexts

## Event model

The schema supports four event types that capture the agentic operation lifecycle:

| Event Type | Description |
| --- | --- |
| `agent_run` | Start or completion of an agent execution session |
| `tool_call` | Agent invoking a tool or external action |
| `tool_result` | Result returned from a tool invocation |
| `escalation` | Agent requesting human intervention or elevated privileges |

## Required fields (MUST)

| Field | Type | Description | Example |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | Timestamp of the event | `2026-01-15T09:30:00Z` |
| `agent_id` | string | Identifier of the agent | `agent-coding-assistant-v2` |
| `agent_version` | string | Version of the agent | `2.1.0` |
| `run_id` | string | Unique identifier for this run/session | `run-20260115-abc123` |
| `event_type` | string | Type of event | `agent_run`, `tool_call`, `tool_result`, `escalation` |
| `actor_id` | string | Initiating user or service | `user@example.com` |
| `tool_name` | string | Name of the tool invoked | `file_write`, `api_call`, `shell_exec` |
| `tool_action` | string | Action performed by the tool | `create`, `read`, `update`, `delete`, `execute` |
| `tool_target` | string | Target of the action | `/path/to/file`, `https://api.example.com` |
| `auth_context` | string | Permission/role summary | `role:developer, scope:project-x` |
| `input_ref` | string | Hash or URI to input (not the content itself) | `sha256:def456...` |
| `output_ref` | string | Hash or URI to output (not the content itself) | `sha256:ghi789...` |
| `decision` | string | Policy decision applied | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | Reference to related evidence | `urn:evidence:...` |

## Optional fields (SHOULD/MAY)

| Field | Type | Description |
| --- | --- | --- |
| `recursion_depth` | number | Current recursion depth for nested agent calls |
| `retry_count` | number | Number of retries for this action |
| `policy_id` | string | Policy that triggered the decision |
| `prompt_template_id` | string | Prompt template identifier |
| `model` | string | Model used for this action |
| `latency_ms` | number | Latency in milliseconds |
| `cost_estimate` | number | Estimated cost of this action |
| `error_code` | string | Error code if the action failed |

## Safety notes

!!! warning "Agentic risk assumptions"
    When logging agentic AI activity, assume the following risks:

    - **Prompt injection**: Malicious inputs may attempt to manipulate agent behavior
    - **Over-privilege**: Agents may have broader permissions than intended for a specific task
    - **Recursive loops**: Agents may enter unintended recursive execution patterns
    - **Confused deputy**: Agents may be tricked into acting on behalf of unauthorized parties

    The schema is designed to capture "who did what with what authority" to support post-incident analysis and audit explanations. It does not prevent these risks; organizations must implement appropriate guardrails.

!!! warning "Data handling"
    - **Do not embed** secrets, credentials, or sensitive content in `input_ref` or `output_ref`.
    - Use hash references or secure URIs to separately stored content.
    - Apply appropriate access controls and retention policies.

## JSON Schema

Download: [agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json)

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

## Related pages

- [Log Schemas index](../)
- [Shadow AI Discovery Log](../shadow-ai-discovery/)
- [Minimum Evidence Requirements](../../minimum-evidence/)
- [Taxonomy: UC-010 Agentic Automation](../../../standard/current/03-taxonomy/)
