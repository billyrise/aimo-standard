# Sample Inputs (Authoring SSOT)

**Status**: Placeholder directory for sample input files  
**Canonical language**: English (EN)

This directory is intended to contain sample input files for creating evidence bundles.

---

## Purpose

Sample inputs demonstrate:
- Raw governance records before bundling
- Different input formats (JSON, CSV, etc.)
- Various lifecycle scenarios (request-only, full lifecycle, exception cases)

---

## What Belongs Here

| File type | Description | Anonymization |
| --- | --- | --- |
| Request records | Sample AI use requests | Remove real names, systems, dates |
| Review records | Sample review/approval records | Remove real names, decisions |
| Exception records | Sample exception scenarios | Remove sensitive business context |
| Log extracts | Sanitized log entries | Remove PII, IP addresses, credentials |

---

## Anonymization Requirements

Before adding sample inputs:

1. **Remove PII**: No real names, email addresses, employee IDs.
2. **Remove sensitive data**: No credentials, API keys, internal system names.
3. **Generalize dates**: Use fictional dates (e.g., `2026-01-01`).
4. **Generalize organizations**: Use placeholder names (e.g., `acme`, `example-corp`).
5. **Review for business sensitivity**: No real business decisions, financials, or strategies.

---

## Current Status

This directory is a placeholder. Sample inputs will be added as authoritative examples are developed.

**TBD**: Add sample input files following anonymization requirements.

---

## Authoring Notes

- All sample inputs must be fictional or fully anonymized.
- Inputs should demonstrate realistic but non-sensitive scenarios.
- Link to corresponding outputs in `sample_outputs/`.
