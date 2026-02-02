---
description: Coverage Map methodology - How AIMO maps to external frameworks. Usage in audits, relationship to Evidence Bundle, and traceability approach.
---

# Methodology

> Note: This methodology supports traceability and evidence readiness. It does not guarantee compliance with any specific regulation/standard.

This page explains what the Coverage Map is and is not, how to use it in audit, and how it relates to the Evidence Bundle and Minimum Evidence Requirements.

## What the mapping is

- An **informative** mapping from external framework/regulation references (by topic) to AIMO evidence, Evidence Bundle TOC items, Minimum Evidence lifecycle groups, artifacts, and validator checks.
- A support tool for **explainability**: which AIMO evidence and artifacts can help demonstrate or explain alignment with a given external requirement (without claiming conformity).

## What the mapping is not

- **Not** a guarantee of compliance with any framework or regulation.
- **Not** legal advice or a substitute for verification against authoritative texts.
- **Not** exhaustive; it is a practical subset for audit-readiness and explainability.

## How to use it in audit

Use the flow: **requirement → evidence → artifact → validation**.

1. **Requirement**: Identify the external framework reference and topic (e.g. ISO 42001 documentation, EU AI Act record-keeping).
2. **Evidence**: See which AIMO Evidence Bundle items and Minimum Evidence lifecycle groups (request, review, exception, renewal, change_log, integrity) support explainability for that requirement.
3. **Artifact**: Locate the artifacts (schemas, templates, examples) that implement or illustrate that evidence.
4. **Validation**: Use the validator and schema checks referenced to verify structural consistency.

Readers must verify against the authoritative text of each framework or regulation.

## Relationship to Evidence Bundle and Minimum Evidence Requirements

- **[Evidence Bundle](../artifacts/evidence-bundle.md)**: Defines the bundle structure, TOC, and traceability. Coverage Map rows reference Evidence Bundle sections (e.g. EV, Dictionary, Summary, change_log, request, review, exception, renewal).
- **[Minimum Evidence Requirements](../artifacts/minimum-evidence.md)**: Defines MUST-level lifecycle groups (request, review, exception, renewal, change_log, integrity). Coverage Map rows reference these groups in `minimum_evidence_refs`.

Use the Coverage Map to see which Evidence Bundle items and Minimum Evidence groups support explainability for a given external requirement.

## Non-overclaim statement

!!! warning "Important"
    The AIMO Standard supports **explainability and evidence readiness**. It does **not** provide legal advice, guarantee compliance, or certify conformity to any regulation or framework. Adopters must verify claims against authoritative texts and obtain professional advice as appropriate.

See [Responsibility Boundary](../governance/responsibility-boundary.md) for scope, assumptions, and adopter responsibilities.

## Audit journey

From this page, continue to:

1. **Framework mappings**: [ISO 42001](iso-42001.md), [NIST AI RMF](nist-ai-rmf.md), [EU AI Act](eu-ai-act.md), [ISMS](isms.md)
2. **Validate**: [Validator](../validator/index.md) — run structural checks
3. **Download**: [Releases](../releases/index.md) — get release assets
