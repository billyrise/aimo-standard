# AIMO Standard Positioning (Authoring SSOT)

**Status**: Authoring input — not user-facing documentation  
**Canonical language**: English (EN)

This document defines the positioning, target audiences, value proposition, and non-goals of the AIMO Standard. It serves as the authoring source for user-facing documentation.

---

## 1. Target Audiences

| Audience | Primary need | AIMO value |
| --- | --- | --- |
| **Auditors** | Verify AI governance controls exist and are documented | Structured evidence format, traceability, validator checks |
| **Security / IT Security** | Ensure evidence integrity, access control, and auditability | Integrity guidance (hashing, WORM, access logs), RACI matrix |
| **IT Ops** | Obtain release assets, run validator, prepare submission packages | Releases page, validator tooling, checksum verification |
| **Legal / Procurement** | Understand scope, limitations, and non-certification nature | Responsibility Boundary, Non-overclaim statement, licensing |

---

## 2. Value Proposition

**Core value**: Explainability + Evidence Readiness

The AIMO Standard provides:

1. **Structured evidence format**: JSON schemas, templates, and taxonomy for AI governance evidence.
2. **Traceability framework**: Lifecycle-based evidence linking (request → review → exception → renewal).
3. **Explainability support**: Coverage mapping to external frameworks (ISO 42001, NIST AI RMF, EU AI Act, ISMS) for audit discussions.
4. **Validation tooling**: Reference validator and rules for structural consistency checks.
5. **Documentation**: Normative specification, examples, and guidance.

**Outcome**: Adopters can demonstrate to auditors that AI use is requested, reviewed, approved, and tracked with structured evidence.

---

## 3. Non-Goals & Responsibility Boundary

The AIMO Standard does **NOT** provide:

| Out-of-scope | Explanation |
| --- | --- |
| Legal advice | AIMO does not interpret laws or regulations. Consult qualified legal counsel. |
| Compliance certification | Using AIMO does not certify compliance with any regulation or framework. |
| Risk assessment | AIMO structures evidence but does not perform or validate AI risk assessments. |
| Technical controls | AIMO does not implement access control, encryption, or other security controls. |
| Audit execution | AIMO provides materials for auditors but does not conduct audits. |
| AI model evaluation | AIMO does not assess model performance, bias, or safety. |

### Canonical Non-Overclaim Statement

> **Important**: The AIMO Standard supports **explainability and evidence readiness**. It does **not** provide legal advice, guarantee compliance, or certify conformity to any regulation or framework. Adopters must verify claims against authoritative texts and obtain professional advice as appropriate.

**Source**: `docs/governance/responsibility-boundary.md` — This is the SSOT for the non-overclaim statement. All other references should point here.

### Assumptions

1. Adopters have governance processes (request, review, approval, exception workflows).
2. Adopters maintain evidence (creation, storage, retention).
3. Adopters verify against authoritative texts when using Coverage Map.
4. Tooling is optional; adopters may use their own validation.

### RACI Summary

| Activity | AIMO Standard | Adopter | Auditor |
| --- | :---: | :---: | :---: |
| Define evidence schema & templates | R/A | I | I |
| Create evidence records | — | R/A | I |
| Store & retain evidence | — | R/A | I |
| Run validator on bundle | C | R/A | C |
| Verify checksums | — | C | R/A |
| Issue audit conclusion | — | — | R/A |

**Legend**: R = Responsible, A = Accountable, C = Consulted, I = Informed

---

## 4. Audit Journey (5-Step Narrative)

The recommended audit journey for adopters and auditors:

| Step | Action | Target page | Outcome |
| --- | --- | --- | --- |
| 1 | **Understand Trust Package** | `governance/trust-package` | Overview of auditor-ready materials |
| 2 | **Review Evidence Bundle structure** | `artifacts/evidence-bundle` | Understand bundle TOC and traceability |
| 3 | **Check Minimum Evidence Requirements** | `artifacts/minimum-evidence` | MUST-level checklist by lifecycle |
| 4 | **Explore Coverage Map** | `coverage-map/methodology`, framework pages | See how AIMO maps to external frameworks |
| 5 | **Validate and Download** | `validator/index`, `releases/index` | Run structural checks, obtain release assets |

This journey is embedded in user-facing docs via "Audit journey" sections that link to the next step.

---

## 5. Translation Rules (EN → JA)

- **English is canonical**: All normative statements are authored in English first.
- **Japanese is derivative**: Japanese translations follow the same structure and heading levels.
- **Heading parity**: EN and JA files must have matching heading levels (enforced by `lint_i18n.py`).
- **Key terms**: See `99_style_guide.md` for glossary and translation conventions.

---

## Authoring Notes

- This file is authoring input; it is not published to users.
- User-facing content is in `docs/governance/trust-package.md` and `docs/governance/responsibility-boundary.md`.
- Any changes to positioning must update both this file and the user-facing docs.
