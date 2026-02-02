---
description: AIMO Human Oversight Protocol - Boundary between automated validation and human review. Machine vs. human judgment responsibilities in AI governance.
---

# Human Oversight Protocol

This page defines the boundary between what automated validation (Validator) can check and what requires human review (Human-in-the-Loop). It clarifies the responsibilities for machine vs. human judgment in AI governance evidence processes.

## Purpose

Automated validation tools can efficiently check structural and syntactic correctness, but cannot replace human judgment for context-dependent decisions. This protocol:

- Clarifies what the Validator can and cannot verify
- Defines the scope of human review required for effective governance
- Supports audit explanations by documenting the human oversight process
- Provides a framework for organizations implementing AI governance workflows

## What automated validation can do (Validator scope)

The AIMO Validator and similar automated tools can check:

| Capability | Description |
| --- | --- |
| **Completeness of required fields/documents** | Verify that all mandatory fields are present in manifests, EV records, and other artifacts |
| **Structural consistency** | Validate references, IDs, and cross-links between artifacts (e.g., request_id → review_id) |
| **Schema validation** | Check that JSON/YAML artifacts conform to defined schemas |
| **Code format validation** | Verify that taxonomy codes match expected patterns (e.g., `UC-001`) |
| **Integrity checks** | Validate hash format and presence (not recomputation against content) |
| **Dictionary validation** | Confirm that codes exist in the taxonomy dictionary |

See [Validator](../standard/current/07-validator.md) for detailed validation rules and reference implementation.

## What requires human review (Human-in-the-Loop scope)

The following areas require human judgment and cannot be automated:

| Capability | Description |
| --- | --- |
| **Context-dependent risk judgment** | Assessing business, ethical, and operational risks based on organizational context |
| **Exception approval rationale** | Evaluating whether an exception is justified and compensating controls are adequate |
| **Remediation decision-making** | Prioritizing fixes, allocating resources, and determining timelines |
| **Policy trade-offs** | Balancing competing requirements (e.g., speed vs. thoroughness, cost vs. risk) |
| **Residual risk acceptance** | Deciding whether remaining risks are acceptable after controls |
| **Cross-domain impact assessment** | Evaluating implications for legal, HR, operations, and other functions |
| **Content accuracy verification** | Confirming that evidence content is factually correct and complete |
| **Stakeholder communication** | Explaining decisions to auditors, regulators, and leadership |

## Responsibility boundary

| Aspect | Validator (Machine) | Human Reviewer |
| --- | --- | --- |
| **Structure** | ✓ Can verify | Review if flagged |
| **Completeness** | ✓ Can verify fields | Verify content adequacy |
| **Format** | ✓ Can verify | — |
| **Risk judgment** | ✗ Cannot assess | ✓ Must assess |
| **Exception approval** | ✗ Cannot decide | ✓ Must decide |
| **Remediation priority** | ✗ Cannot prioritize | ✓ Must prioritize |
| **Legal interpretation** | ✗ Cannot interpret | ✓ Must verify with counsel |
| **Audit conclusion** | ✗ Cannot conclude | ✓ Auditor responsibility |

!!! note "Complementary roles"
    Validator and human review are **complementary**, not alternatives. Validator ensures structural consistency before human review; human review ensures contextual appropriateness.

## Evidence expectations

Organizations implementing human oversight should document:

| Evidence Type | Description |
| --- | --- |
| **Review record** | Who reviewed, when, and what decision was made |
| **Approval rationale** | Why the decision was made (especially for exceptions) |
| **Escalation record** | When and why issues were escalated to higher authority |
| **Remediation plan** | Planned actions, owners, and timelines for addressing issues |
| **Sign-off** | Formal attestation that review was completed |

These records should be included in the Evidence Bundle per [Minimum Evidence Requirements](../artifacts/minimum-evidence.md).

## Non-overclaim

!!! warning "Important"
    This protocol defines a **framework for documenting human oversight**. It does **not**:

    - Provide legal advice or regulatory interpretation
    - Guarantee compliance with any regulation or standard
    - Replace qualified human judgment with automated decisions
    - Prescribe specific organizational processes

    Organizations must adapt this framework to their specific context, risk profile, and regulatory requirements.

## Related pages

- [Validator](../standard/current/07-validator.md) — automated validation rules and reference implementation
- [Responsibility Boundary](responsibility-boundary.md) — what AIMO provides vs. adopter responsibilities
- [Minimum Evidence Requirements](../artifacts/minimum-evidence.md) — MUST-level evidence checklist
- [Trust Package](trust-package.md) — auditor-ready materials hub
