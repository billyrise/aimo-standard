# Minimum Evidence Requirements

This page defines the minimum evidence requirements as a MUST-level checklist, grouped by lifecycle. It supports explainability and evidence readiness; it does not provide legal advice or guarantee compliance.

## 1) Request (申請)

- **MUST fields**: identifier, timestamp(s), actor/role, scope (what is requested), rationale (why).
- **MUST linkages**: request id referenced by review and by EV items that record the use.
- **What it proves**: that use was requested and scoped before approval and use.

## 2) Review / Approval (審査/承認)

- **MUST fields**: identifier, timestamp(s), actor/role, decision (approved/rejected/conditional), scope, rationale, reference to request.
- **MUST linkages**: review id referenced by EV and by any exception or renewal that follows.
- **What it proves**: that a defined review and approval occurred before use (or exception).

## 3) Exception (例外)

- **MUST fields**: identifier, timestamp(s), scope, expiry (or deadline), compensating controls, rationale, reference to review/request.
- **MUST linkages**: exception → compensating controls; exception → expiry; exception → renewal (when re-evaluation is due).
- **What it proves**: that deviations are time-bound, have compensating controls, and are linked to renewal.

## 4) Renewal / Re-evaluation (更新/再評価)

- **MUST fields**: identifier, timestamp(s), actor/role, decision (renewed/revoked/conditional), references to prior exception/request/review/EV.
- **MUST linkages**: renewal references the exception or approval being renewed; EV items can reference renewal id.
- **What it proves**: that exceptions and approvals are re-evaluated and renewed or revoked on a defined basis.

## 5) Change Log (変更管理)

- **MUST fields**: identifier, timestamp, actor/role, change description, references (e.g. to EV, request, review, exception, renewal affected).
- **MUST linkages**: change log entries reference the artifacts they modify or that trigger the change.
- **What it proves**: that changes to the bundle or its contents are recorded and traceable.

## 6) Integrity & Access (完全性/アクセス制御)

- **Implementation**: recommended (e.g. access control, hashing, WORM, audit logs). Requirements are stated from the perspective of explainability: who had access, how integrity was preserved.
- **What it proves**: that evidence is preserved and access is controlled to support audit reliance.

## Important note

This minimum set supports explainability and evidence readiness; it does not itself provide legal advice or guarantee compliance.

See [Evidence Bundle](evidence-bundle.md) for bundle structure and TOC; see [EV Template](../standard/current/06-ev-template.md) and schemas for field-level alignment.
