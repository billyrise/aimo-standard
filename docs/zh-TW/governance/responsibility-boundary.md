---
description: AIMO Responsibility Boundary - Defines what the standard provides vs. adopter responsibilities. Non-overclaim statement and scope limitations.
# TRANSLATION METADATA - DO NOT REMOVE
source_file: en/governance/responsibility-boundary.md
source_hash: ce129a53e8e41bbe
translation_date: 2026-02-02
translator: pending
translation_status: needs_translation
---

# Responsibility Boundary

This page defines what the AIMO Standard provides and does not provide, the assumptions it makes, and the responsibilities of adopters.

## What AIMO Standard provides

- **A structured evidence format**: schemas, templates, and taxonomy for AI governance evidence.
- **Traceability framework**: lifecycle-based evidence linking (request → review → exception → renewal).
- **Explainability support**: coverage mapping to external frameworks for audit discussions.
- **Validation tooling**: reference validator and rules for structural consistency checks.
- **Documentation**: normative specification, examples, and guidance.

## What AIMO Standard does NOT provide

| Out-of-scope | Explanation |
| --- | --- |
| **Legal advice** | AIMO does not interpret laws or regulations. Consult qualified legal counsel for regulatory compliance. |
| **Compliance certification** | Using AIMO does not certify compliance with any regulation or framework (ISO 42001, EU AI Act, NIST AI RMF, etc.). |
| **Risk assessment** | AIMO structures evidence but does not perform or validate AI risk assessments. |
| **Technical controls** | AIMO does not implement access control, encryption, or other security controls; it documents expectations. |
| **Audit execution** | AIMO provides materials for auditors but does not conduct audits. |
| **AI model evaluation** | AIMO does not assess model performance, bias, or safety. |

## Assumptions

The AIMO Standard assumes:

1. **Adopters have governance processes**: request, review, approval, and exception workflows exist.
2. **Adopters maintain evidence**: evidence is created, stored, and retained by the adopter's systems.
3. **Adopters verify against authoritative texts**: when using Coverage Map, adopters check the original framework or regulation.
4. **Tooling is optional**: the reference validator is a convenience; adopters may use their own validation.

## Adopter responsibilities

| Responsibility | Description |
| --- | --- |
| **Evidence creation** | Generate accurate, timely evidence records aligned with EV schema. |
| **Evidence storage & retention** | Store evidence securely with appropriate access controls and retention periods. |
| **Integrity & access control** | Implement controls (hashing, WORM, audit logs) to preserve evidence integrity. |
| **Legal verification** | Verify compliance claims against authoritative legal texts and obtain legal advice as needed. |
| **Continuous alignment** | Update evidence and mappings as AIMO Standard versions and external frameworks evolve. |
| **Audit preparation** | Package evidence bundles and run validation before submission to auditors. |

## RACI Matrix

The following RACI matrix clarifies responsibilities across AIMO Standard, Adopter, and Auditor roles.

| Activity | AIMO Standard | Adopter | Auditor |
| --- | :---: | :---: | :---: |
| **Define evidence schema & templates** | R/A | I | I |
| **Create evidence records** | — | R/A | I |
| **Store & retain evidence** | — | R/A | I |
| **Implement access controls** | — | R/A | I |
| **Implement integrity controls (hash, WORM)** | — | R/A | I |
| **Run validator on bundle** | C | R/A | C |
| **Package submission (zip, checksums)** | C | R/A | I |
| **Verify checksums (sha256)** | — | C | R/A |
| **Verify bundle structure (validator)** | — | C | R/A |
| **Interpret regulatory requirements** | — | R/A | C |
| **Issue audit conclusion** | — | — | R/A |
| **Provide legal advice** | — | — | — |

**Legend**: R = Responsible, A = Accountable, C = Consulted, I = Informed, — = Not applicable

!!! note "Key takeaway"
    AIMO Standard is responsible for **defining the format**. Adopters are responsible for **creating, storing, and validating evidence**. Auditors are responsible for **verifying submissions and issuing audit conclusions**.

!!! warning "Non-certification notice"
    AIMO Standard is informative; it does not certify compliance or provide legal advice. Audit conclusions and conformity assessments are the sole responsibility of qualified auditors and legal professionals.

## Non-overclaim statement

!!! warning "Important"
    The AIMO Standard supports **explainability and evidence readiness**. It does **not** provide legal advice, guarantee compliance, or certify conformity to any regulation or framework. Adopters must verify claims against authoritative texts and obtain professional advice as appropriate.

This statement applies to all AIMO Standard documentation, including Trust Package, Evidence Bundle, Minimum Evidence Requirements, Coverage Map, and Releases.

## Related pages

- [Trust Package](trust-package.md) — auditor-ready materials hub
- [Human Oversight Protocol](human-oversight-protocol.md) — machine vs. human review boundary
- [Minimum Evidence Requirements](../artifacts/minimum-evidence.md) — MUST-level lifecycle checklist
- [Coverage Map Methodology](../coverage-map/methodology.md) — what the mapping is and is not
