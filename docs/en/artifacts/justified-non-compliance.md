---
description: Justified Non-Compliance (JNC) — optional payload in v0.1.2. Not legal advice; does not constitute assurance.
---

# Justified Non-Compliance (JNC) — optional (v0.1.2)

This page is **informative**. The AIMO Standard **does not** require a Justified Non-Compliance (JNC) payload. As of **v0.1.2**, JNC is introduced as an **optional** mechanism: if an adopter submits a JNC payload within an Evidence Bundle, it **must** conform to the schema and is machine-validated. JNC is **not mandatory** in v0.1.2.

**Disclaimer:** This mechanism is for documentation and audit support only. It is **not legal advice** and does **not** constitute assurance or a guarantee of compliance with any regulation.

## Purpose

In practice, an organization may decide not to implement a specific control or evidence item (e.g. "Phase 1 does not include a model monitoring dashboard"). Auditors may ask: "Why is this not implemented, and what is the risk?" A **Justified Non-Compliance (JNC)** payload allows such decisions to be recorded in a structured, auditable way within the Evidence Bundle, alongside other payloads.

## v0.1.2 optional payload

- **Not required:** Bundles without JNC are valid. Validators do not require a JNC payload.
- **If present:** The JNC file must be listed in the bundle `manifest.json` `payload_index` and must conform to the JNC schema. The validator will run schema validation when it detects a JNC payload.

### Recommended placement

| Item | Recommendation |
|------|----------------|
| Path in bundle | `payloads/jnc.json` |
| `logical_id` in payload_index | `JNC`, `jnc`, or `JUSTIFIED_NON_COMPLIANCE` (validator accepts any of these, case-insensitive) |
| MIME | `application/json` |

### Schema

The normative schema for the JNC payload is:

- **Schema file:** [schemas/jsonschema/aimo-jnc.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/aimo-jnc.schema.json)

It defines a `version` (e.g. `0.1.2`) and a `non_compliances` array. Each entry includes:

- `id`, `aimo_item_ref`, `title`, `rationale`
- `risk_assessment`: `likelihood`, `impact` (enum: low/medium/high), `mitigation`
- `approver`: `name`, `role`, `approval_date` (YYYY-MM-DD)
- `review_schedule`: `quarterly` | `monthly` | `annually` | `ad-hoc`
- Optional: `sunset_condition`, `references`

See the schema and [examples/justified_non_compliance.json](https://github.com/billyrise/aimo-standard/blob/main/examples/justified_non_compliance.json) for a minimal valid example.

## Alignment

A JNC structure aligns with:

- ISO 42001 Clause 6.1 (addressing risks and opportunities)
- NIST AI RMF GOVERN-1.6 (exception management)

## Status

- **v0.1 / v0.1.1**: No JNC schema or requirement. Adopters may document exceptions outside the bundle.
- **v0.1.2**: JNC is **optional**. If present in the Evidence Bundle, it is schema-validated. Not required for bundle validity.
- **v0.2 (planned)**: Further evolution may be described in the [v0.2 roadmap](../standard/current/10-roadmap-v0.2.md).
