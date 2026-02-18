---
description: AIMO Standard conformance levels. How organizations claim compliance, evidence requirements, and what each conformance level means for AI governance.
---
<!-- aimo:translation_status=source -->

# Conformance

!!! warning "Important: No certification, no assurance, no legal compliance claim"
    AIMO Standard defines an **evidence packaging and validation format**. It does not certify compliance with laws or standards.
    Audit and assurance opinions remain the responsibility of independent auditors and the adopting organization.
    **Appropriate claim:** "An Evidence Bundle was produced according to AIMO Standard v0.1.2 and structurally validated by the AIMO Validator."
    <!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
    **Inappropriate claim:** "EU AI Act compliant", "ISO 42001 certified", "government approved".
    <!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

AIMO Standard positions as an **assurance / audit handoff / continuous evidence layer**: it provides evidence packaging, validators, and traceability so that adopters and auditors can work with structured evidence. AIMO is **not** a certifier; certification and compliance decisions are made by accredited certification bodies, auditors, and the adopting organization.

These tiers are **internal evidence maturity levels** for packaging and traceability. They are **not** a certification, **not** an assurance opinion, and **not** legal or regulatory compliance.

## Compatibility claims (ISO/NIST/EU)

The following **informative mappings** link AIMO evidence and artifacts to external frameworks. They support explainability and audit handoff; they do **not** confer certification or guarantee compliance. Verify against the authoritative framework texts.

- [Coverage Map — ISO/IEC 42001](../coverage-map/iso-42001/) — mapping to ISO/IEC 42001 (AI management system)
- [Coverage Map — NIST AI RMF](../coverage-map/nist-ai-rmf/) — mapping to NIST AI Risk Management Framework
- [Coverage Map — EU AI Act](../coverage-map/eu-ai-act/) — mapping to EU AI Act themes (high-level; not legal advice)

Primary sources and claim language are documented on each coverage map page and in [Responsibility Boundary](../governance/responsibility-boundary/).

## Non-claims (what AIMO does NOT claim)

- AIMO does **not** certify conformity to ISO/IEC 42001, NIST AI RMF, EU AI Act, or any other framework.
- AIMO does **not** guarantee regulatory or legal compliance.
- AIMO does **not** provide assurance opinions or legal advice.
- AIMO does **not** decide whether an organization meets external requirements; that is the responsibility of adopters, auditors, and certification bodies.

AIMO **does** provide: structured evidence format, validator, coverage mappings (informative), and materials to support audit handoff. See [Responsibility Boundary](../governance/responsibility-boundary/) for the full scope.

!!! note "Tier name alias"
    The top tier was previously referred to as "Gold" in informal discussions; the **official tier name is Audit-Ready**.

## AIMO Conformity Framework (AIMO-MS / AIMO-Controls / AIMO-Audit)

| Component | Description | Evidence expectations |
| --- | --- | --- |
| **AIMO-MS** | Management-system–oriented structure: policies, roles, PDCA-aligned artifacts that can support ISO/IEC 42001–type controls. | Request, review, exception, renewal, change log; Summary and Dictionary. |
| **AIMO-Controls** | Lifecycle and integrity controls: request→review→exception→renewal, hashing, signing (per [Evidence Bundle structure](../../standard/current/09-evidence-bundle-structure/)). | Object_index, payload_index, hash_chain, signing; lifecycle records. |
| **AIMO-Audit** | Readiness for audit handoff: validator pass, checksums, optional attestation and audit handoff index. | Validator output, bundle_id, producer identity, optional signature metadata and handoff index. |

Evidence expectations are described in [Minimum Evidence Requirements](../artifacts/minimum-evidence/) and [Evidence Bundle](../artifacts/evidence-bundle/).

## Conformity Levels (AIMO-only)

### Level 1 — Foundation

**Purpose:** Traceable baseline. Minimum set to make the bundle identifiable, integrity-verifiable, and validator-checked.

| Item | Requirement |
| --- | --- |
| **Required artifacts** | [Evidence Bundle](../artifacts/evidence-bundle/) structure (manifest.json, objects/, payload_index per spec); [Validator](../validator/) pass; link to [Minimum Evidence](../artifacts/minimum-evidence/). |
| **Typical audit questions** | What is in scope? Who produced the bundle? Can hashes be verified? |
| **Typical gaps** | Missing manifest metadata (bundle_id, created_at, producer); validator not run or not attached. |

### Level 2 — Operational

**Purpose:** Operational control evidence. Builds on Foundation with lifecycle trail and monitoring.

| Item | Requirement |
| --- | --- |
| **Required artifacts** | All Foundation MUST items; lifecycle control trail (request/approval, review, exception or “no exceptions”, renewal schedule); at least one monitoring artifact (incident log or periodic check or human oversight sampling); change log with integrity linkage; proof vs assurance boundary statement. |
| **Typical audit questions** | Who approved use? How are exceptions tracked? When was the last review? |
| **Typical gaps** | Review/approval not linked to request; no monitoring artifact; change log not referencing impacted objects. |

### Level 3 — Audit-Ready

**Purpose:** Audit handoff quality. Full attestation, reproducibility, and external-form slotting.

| Item | Requirement |
| --- | --- |
| **Required artifacts** | All Operational MUST items; at least one digital signature covering manifest (signer identity + algorithm); TSA or “no TSA” statement; reproducibility packet (exact validator command, expected outputs, environment metadata); External Forms section with official templates/checklists attached as-is and cross-referenced; bounded completeness statement; one-page audit handoff index (artifact → hash → producer → date). |
| **Typical audit questions** | How can an auditor re-run validation? Where are external checklists and how do they map to the bundle? |
| **Typical gaps** | Signature present but signer/algorithm not documented; no handoff index; external forms not hashed or not referenced in manifest. |

## Minimum Evidence by Level (summary)

| Level | MUST (summary) |
| --- | --- |
| **Foundation** | Bundle structure (manifest, object_index, payload_index); sha256 for referenced objects; bundle_id, created_at, producer; validator run + version; evidence dictionary baseline (system name, owner, purpose, data categories, lifecycle stage); access & retention statement (who, duration, storage type, tamper-evidence). SHOULD: minimal change log entry. |
| **Operational** | All Foundation MUST; lifecycle trail (request/approval, review, exception or “none”, renewal + last renewal); ≥1 monitoring artifact; change log entries reference impacted objects; explicit proof vs assurance boundary statement. |
| **Audit-Ready** | All Operational MUST; ≥1 signature over manifest (signer identity + algorithm); TSA or “no TSA”; reproducibility packet; External Forms listed and cross-referenced; bounded completeness statement; audit handoff index. |

Signature **presence** (at least one signature targeting the manifest) is required by the normative [Evidence Bundle structure](../../standard/current/09-evidence-bundle-structure/) for all bundles. **Audit-Ready** adds stricter **cryptographic attestation** (signer identity, algorithm, TSA statement, re-validation instructions) so a third party can re-perform checks.

## ISO/IEC 42001 Mapping (informative)

The following table shows how AIMO artifacts **support evidence for** typical ISO/IEC 42001 clause families. This is informative only; it does not imply certification or compliance.

| ISO/IEC 42001 clause family | AIMO artifacts that support evidence |
| --- | --- |
| Context of the organization | Summary, Dictionary, scope_ref |
| Leadership / Policy | Summary, review, dictionary |
| Planning (risks, objectives) | request, review, exception, EV, Dictionary |
| Support (resources, competence, documentation) | Summary, review, EV, change_log |
| Operation | EV, request, review, exception; operational controls |
| Performance evaluation (monitoring, internal audit, management review) | EV, change_log, review, renewal |
| Improvement | exception, renewal, change_log |

See [Coverage Map — ISO/IEC 42001](../coverage-map/iso-42001/) and [ISO 42001 Certification Readiness Toolkit](../artifacts/iso-42001-certification-readiness-toolkit/) for more detail.

## Claim language templates (anti-overclaim)

Use only claims that accurately describe what was done. Certification and legal compliance remain the responsibility of adopters and accredited bodies.

**Acceptable (examples)**

- "We are AIMO Conformant (Level 2) against AIMO Standard v0.1.2; this does not imply ISO certification or legal compliance."
- "We use AIMO artifacts to support ISO/IEC 42001 readiness; certification decisions remain with accredited certification bodies."
- "An Evidence Bundle was produced according to AIMO Standard v0.1.2 and structurally validated by the AIMO Validator."

<!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
**Unacceptable (examples)**

- "EU AI Act compliant" (AIMO does not certify regulatory compliance.)
- "ISO 42001 certified" (Certification is issued by accredited certification bodies, not AIMO.)
- "Government approved" (AIMO is not a government approval scheme.)
<!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

## Related pages

- [Trust Package](../governance/trust-package/) — Consolidated entry point for auditors
- [Responsibility Boundary](../governance/responsibility-boundary/) — What AIMO does and does not provide
- [Standard (Current)](../standard/current/) — Normative requirements
- [Artifacts](../artifacts/) — Evidence structure and Minimum Evidence
- [Validator](../validator/) — Structural validation
