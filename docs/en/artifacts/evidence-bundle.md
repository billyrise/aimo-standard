---
description: AIMO Evidence Bundle structure. Audit package format with TOC, traceability, and artifacts for AI governance compliance and auditor delivery.
---

# Evidence Bundle

An **Evidence Bundle** is an audit package: a structured set of artifacts that supports explainability and traceability for AI governance. It is not a product feature but a deliverable format for auditors and compliance.

## Bundle structure and naming

- **Bundle root naming**: use a consistent pattern such as `{org}_{system}_{period}_{version}` (e.g. `acme_ai-usage_2026-Q1_v1`).
- **Required files**: at least one Evidence (EV) set aligned with the [Evidence Pack Template (EP)](../standard/current/06-ev-template.md), a [Dictionary](../standard/current/05-dictionary.md), a short **Summary** (executive summary of the bundle), and a **Change Log** (or reference to it) for changes to the bundle or its contents.
- **Optional attachments**: logs, review records, exception approvals, renewal records; keep naming consistent and referrable from the main EV/Dictionary.

## Table of contents (TOC)

| Section | Artifact | Required? | Purpose | Minimum fields | Validation |
| --- | --- | --- | --- | --- | --- |
| Evidence | EV records (JSON/array) | Yes | Record of what happened; link to request/review/exception/renewal | id, timestamp, source, summary; optional lifecycle refs | [Validator](../validator/index.md), aimo-ev.schema.json |
| Dictionary | dictionary.json | Yes | Keys/labels/descriptions for codes and dimensions | entries (key, label, description) | aimo-dictionary.schema.json |
| Summary | summary (doc or field) | Yes | One-page overview for auditors | scope, period, key decisions, exceptions | — |
| Change log | change_log or reference | Yes | Audit trail of bundle/content changes | id, timestamp, actor, change description, references | — |
| Request | request record(s) | If applicable | Application/request for use | id, timestamp, actor/role, scope, rationale | — |
| Review/Approval | review record(s) | If applicable | Review and approval outcome | id, timestamp, actor/role, decision, references | — |
| Exception | exception record(s) | If applicable | Exception with compensating controls and expiry | id, timestamp, scope, expiry, compensating controls, renewal ref | — |
| Renewal | renewal record(s) | If applicable | Re-evaluation and renewal | id, timestamp, actor/role, decision, references to prior exception/EV | — |

## Normative relationship: EV records (index) and Evidence Pack (payload)

To avoid double-build and audit ambiguity, the following is **normative**:

1. **EV records (JSON)** are the **index/ledger**: machine-verifiable traceability. They record what happened (request, review, exception, renewal, change) and MUST carry stable IDs and cross-references.
2. **Evidence Pack files** (EP-01..EP-07 documents and manifest) are the **payload**: the human- and tool-readable evidence that the index points to.
3. **Linkage**: EV records SHOULD reference payload via `evidence_file_ids` (e.g. EP-01, EP-02) and/or cryptographic hashes. The [Validator](../validator/index.md) checks referential integrity when these references are present (e.g. every referenced file_id exists in the Evidence Pack manifest and optional hash matches).
4. **Minimum submission set** for audit: **EV JSON** (root/records) + **Dictionary** + **Summary** + **Change Log** + **Evidence Pack** (manifest + files, e.g. as a zip). All of these together form the conformance surface.

Implementers maintain a single source of truth: the EV index references the pack; the pack does not redefine the meaning of taxonomy EV codes (Request Record, Review/Approval, etc.). See [Evidence Pack Template](../standard/current/06-ev-template.md) for EP-01..EP-07 document types.

## Traceability

- **Stable IDs**: every record (EV, request, review, exception, renewal, change log entry) MUST have a stable, unique identifier.
- **Cross-references**: link Request → Review → Exception (if any) → Renewal and link EV items to these via reference fields (e.g. `request_id`, `review_id`, `exception_id`, `renewal_id`).
- **Linkage**: ensure auditors can follow a chain from an AI use (or exception) to the request, approval, any exception and its compensating controls and expiry, and renewal.

## How auditors use this

Auditors use the Evidence Bundle to verify that AI use is requested, reviewed, and approved; that exceptions are time-bound and have compensating controls and renewal; and that changes are logged. The TOC and traceability rules let them locate required artifacts and follow IDs and references across request, review, exception, renewal, and EV records. The Summary gives a quick overview; the Change Log supports change control and accountability.

See [Minimum Evidence Requirements](minimum-evidence.md) for MUST-level fields and lifecycle groups.

## Operational guidance

!!! info "Integrity and access control"
    While AIMO does not prescribe specific controls, adopters should document:
    
    - **Access roles**: who can create, read, update, or delete evidence
    - **Retention policy**: how long evidence is retained and under what schedule
    - **Integrity mechanisms**: hashing, WORM storage, or digital signatures used
    - **Audit trail**: logs of access and changes to the bundle
    
    See [Minimum Evidence Requirements > Integrity & Access](minimum-evidence.md#6-integrity-access) for detailed guidance.

## Audit journey

From this page, the typical audit journey continues:

1. **Next**: [Minimum Evidence Requirements](minimum-evidence.md) — MUST-level checklist by lifecycle
2. **Then**: [Coverage Map](../coverage-map/index.md) — mapping to external frameworks
3. **Validate**: [Validator](../validator/index.md) — run structural checks
4. **Download**: [Releases](../releases/index.md) — get release assets and verify checksums
