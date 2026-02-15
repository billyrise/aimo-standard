---
description: AIMO Log Schemas - Vendor-neutral log formats for AI evidence. Includes Shadow AI discovery and agent activity monitoring schemas.
---
<!-- aimo:translation_status=source -->

# Log Schemas

## What this is

This section defines **normalized log formats** for evidence that can be included in an Evidence Bundle. These schemas provide a vendor-neutral structure for logs related to AI usage monitoring and agentic operations.

## When to use

- **Shadow AI visibility**: Documenting detection, inventory, and remediation of unapproved AI usage.
- **Agentic operation audits**: Explaining autonomous agent privilege exercise, tool execution, and recursive operations.
- **Incident reproducibility**: Providing structured evidence for incident investigation and root cause analysis.

## What it is NOT

!!! warning "Important"
    These schemas define **log formats for evidence submission**. They do NOT:

    - Automatically collect logs from your systems
    - Provide log aggregation or monitoring tools
    - Guarantee compliance with any regulation or standard
    - Replace vendor-specific logging implementations

    Organizations must implement their own log collection pipelines and normalize logs to these schemas for evidence submission.

## Schemas

| Schema | Purpose | Download |
| --- | --- | --- |
| [Shadow AI Discovery Log](shadow-ai-discovery/) | Unapproved AI usage detection and inventory | [shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json) |
| [Agent Activity Log](agent-activity/) | Agentic AI privilege exercise and tool execution | [agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json) |

## Related pages

- [Minimum Evidence Requirements](../minimum-evidence/) — MUST-level evidence checklist
- [Evidence Bundle](../evidence-bundle/) — Bundle structure and TOC
- [Taxonomy](../../standard/current/03-taxonomy/) — Classification codes (including UC-010 Agentic Automation, IM-007 Shadow/Unmanaged)
