---
description: AIMO minimum evidence requirements. MUST-level checklist by lifecycle (request, review, approval, change, renewal) for AI governance evidence readiness.
---

# Minimum Evidence Requirements

This page is the **Minimum Evidence Requirements** checklist for auditors and implementers. It defines the minimum evidence requirements as a MUST-level checklist, grouped by lifecycle. It supports explainability and evidence readiness; it does not provide legal advice or guarantee compliance.

Use this page together with [Evidence Bundle](../evidence-bundle/) and the [Validator](../../standard/current/07-validator/) when preparing or reviewing submissions.

## 1) Request

- **MUST fields**: identifier, timestamp(s), actor/role, scope (what is requested), rationale (why).
- **MUST linkages**: request id referenced by review and by EV items that record the use.
- **What it proves**: that use was requested and scoped before approval and use.

## 2) Review / Approval

- **MUST fields**: identifier, timestamp(s), actor/role, decision (approved/rejected/conditional), scope, rationale, reference to request.
- **MUST linkages**: review id referenced by EV and by any exception or renewal that follows.
- **What it proves**: that a defined review and approval occurred before use (or exception).

## 3) Exception

- **MUST fields**: identifier, timestamp(s), scope, expiry (or deadline), compensating controls, rationale, reference to review/request.
- **MUST linkages**: exception → compensating controls; exception → expiry; exception → renewal (when re-evaluation is due).
- **What it proves**: that deviations are time-bound, have compensating controls, and are linked to renewal.

## 4) Renewal / Re-evaluation

- **MUST fields**: identifier, timestamp(s), actor/role, decision (renewed/revoked/conditional), references to prior exception/request/review/EV.
- **MUST linkages**: renewal references the exception or approval being renewed; EV items can reference renewal id.
- **What it proves**: that exceptions and approvals are re-evaluated and renewed or revoked on a defined basis.

## 5) Change Log

- **MUST fields**: identifier, timestamp, actor/role, change description, references (e.g. to EV, request, review, exception, renewal affected).
- **MUST linkages**: change log entries reference the artifacts they modify or that trigger the change.
- **What it proves**: that changes to the bundle or its contents are recorded and traceable.

## 6) Integrity & Access

Evidence integrity and access control are essential for audit reliance. While AIMO does not prescribe specific technical controls, adopters should document how these expectations are met.

### Access control guidance

| Aspect | Guidance |
| --- | --- |
| **Role-based access** | Define roles (e.g., evidence creator, reviewer, auditor, admin) and document who can create, read, update, or delete evidence. |
| **Least privilege** | Grant minimum necessary access; restrict write access to authorized personnel. |
| **Access logging** | Log access events (who, when, what) for audit trail purposes. |
| **Separation of duties** | Where practical, separate evidence creation from approval roles. |

### Retention guidance

| Aspect | Guidance |
| --- | --- |
| **Retention period** | Define and document retention periods based on regulatory requirements and organizational policy (e.g., 5-7 years for financial audits). |
| **Retention schedule** | Maintain a schedule showing what evidence is retained, for how long, and when it can be disposed. |
| **Legal hold** | Support legal hold processes that suspend normal retention/deletion for litigation or investigation. |

### Immutability options

| Option | Description |
| --- | --- |
| **Cryptographic hashing** | Generate SHA-256 (or stronger) hashes for evidence files; store hashes separately for verification. |
| **WORM storage** | Use Write-Once-Read-Many storage for evidence archives to prevent modification. |
| **Append-only logs** | Use append-only audit logs for change tracking. |
| **Digital signatures** | Sign evidence bundles to prove authorship and detect tampering. |

### Audit trail expectations

| Element | What to document |
| --- | --- |
| **Change log** | Record who changed what, when, and why (see Change Log lifecycle group). |
| **Access log** | Record who accessed evidence, when, and for what purpose. |
| **System logs** | Retain relevant system logs (authentication, authorization) that support evidence integrity claims. |
| **Verification records** | Document periodic integrity verification (hash checks, audit reviews). |

### What it proves

- **Evidence is preserved**: integrity mechanisms (hashing, WORM, signatures) demonstrate that evidence has not been tampered with.
- **Access is controlled**: access logs and role definitions show who had access and that least privilege was applied.
- **Audit reliance is supported**: together, these elements give auditors confidence in the reliability of evidence.

### Recommended operational profiles

Choose a profile based on your risk tolerance and regulatory requirements. These are recommendations, not mandates.

| Aspect | Lightweight | Standard | Strict |
| --- | --- | --- | --- |
| **Use case** | Internal pilots, low-risk AI | Production systems, moderate risk | Regulated industries, high-risk AI |
| **Retention period** | 1-2 years | 5-7 years | 7-10+ years or regulatory minimum |
| **Immutability** | SHA-256 hashes | SHA-256 + append-only logs | WORM storage + digital signatures |
| **Access control** | Role-based (basic) | Role-based + access logging | Separation of duties + full audit trail |
| **Audit trail** | Change log only | Change log + access log | Full system logs + periodic verification |
| **Verification frequency** | On-demand | Quarterly | Monthly or continuous |
| **Validator usage** | Optional | Required before submission | Required + automated CI checks |

!!! note "Retention periods are examples"
    Retention periods shown are illustrative. Organizations must determine retention based on applicable laws, contracts, industry requirements, and internal policies.

!!! tip "How to choose"
    - **Lightweight**: Suitable for experimentation, internal tools, or low-stakes applications where formal audits are unlikely.
    - **Standard**: Recommended for most production deployments where audits may occur but are not continuous.
    - **Strict**: Required for regulated industries (finance, healthcare, government) or AI systems with significant risk impact.

## Important note

This minimum set supports explainability and evidence readiness; it does not itself provide legal advice or guarantee compliance.

See [Evidence Bundle](../evidence-bundle/) for bundle structure and TOC; see [EV Template](../../standard/current/06-ev-template/) and schemas for field-level alignment.

See also: [Log Schemas](../log-schemas/) — normalized log formats for Shadow AI discovery and agent activity evidence.
