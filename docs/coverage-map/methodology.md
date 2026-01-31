# Methodology

This page explains what the Coverage Map is and is not, how to use it in audit, and how it relates to the Evidence Bundle and Minimum Evidence Requirements.

## What the mapping is

- An **informative** mapping from external framework/regulation references (by topic) to AIMO evidence, Evidence Bundle TOC items, Minimum Evidence lifecycle groups, artifacts, and validator checks.
- A support tool for **explainability**: which AIMO evidence and artifacts can help demonstrate or explain alignment with a given external requirement (without claiming conformity).
- Single source of truth: `coverage_map/coverage_map.yaml` in the repository. Doc tables are derived from it; keep both in sync when updating.

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

## Update policy

- Mapping data is updated when AIMO evidence/artifacts or framework interpretations change.
- When updating, change `coverage_map/coverage_map.yaml` first, then refresh the tables in the framework-specific doc pages so they remain consistent with the SSOT.

## Relationship to Evidence Bundle and Minimum Evidence Requirements

- **[Evidence Bundle](../artifacts/evidence-bundle.md)**: Defines the bundle structure, TOC, and traceability. Coverage Map rows reference Evidence Bundle sections (e.g. EV, Dictionary, Summary, change_log, request, review, exception, renewal).
- **[Minimum Evidence Requirements](../artifacts/minimum-evidence.md)**: Defines MUST-level lifecycle groups (request, review, exception, renewal, change_log, integrity). Coverage Map rows reference these groups in `minimum_evidence_refs`.

Use the Coverage Map to see which Evidence Bundle items and Minimum Evidence groups support explainability for a given external requirement.
