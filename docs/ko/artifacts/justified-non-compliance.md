---
description: Informative concept for Justified Non-Compliance (JNC). Not part of v0.1 or v0.1.1 normative specification.
---
<!-- aimo:translation_status=translated -->

# Justified Non-Compliance (JNC) — future extension

This page is **informative**. The AIMO Standard v0.1 and v0.1.1 do **not** define or require a mechanism to prove or declare "intentional non-compliance" with a requirement. The following describes a possible future extension for adopters who need to document and justify exceptions.

## Purpose

In practice, an organization may decide not to implement a specific control or evidence item (e.g. "Phase 1 does not include a model monitoring dashboard"). Auditors may ask: "Why is this not implemented, and what is the risk?" Today, that explanation lives outside the standard. A future **Justified Non-Compliance (JNC)** mechanism would allow such decisions to be recorded in a structured, auditable way within or alongside the Evidence Bundle.

## Possible schema (draft, not normative)

A future version might support an optional file such as `evidence/justified-non-compliance.json` with a structure along these lines:

```json
{
  "non_compliances": [
    {
      "aimo_requirement": "Model Monitoring Dashboard",
      "rationale": "Business justification",
      "risk_assessment": {
        "likelihood": "low",
        "impact": "medium",
        "mitigation": "Manual quarterly review by Data Science Lead"
      },
      "approver": {
        "name": "Jane Doe",
        "role": "CTO",
        "approval_date": "2026-01-15"
      },
      "review_schedule": "quarterly",
      "sunset_condition": "When model is used for regulated decisions"
    }
  ]
}
```

Such a structure would align with:

- ISO 42001 Clause 6.1 (addressing risks and opportunities)
- NIST AI RMF GOVERN-1.6 (exception management)

## Status

- **v0.1 / v0.1.1**: No JNC schema or requirement. Adopters may document exceptions outside the bundle.
- **v0.2 (planned)**: JNC may be introduced as an optional, informative mechanism; see [v0.2 roadmap](../../standard/current/10-roadmap-v0.2/).
