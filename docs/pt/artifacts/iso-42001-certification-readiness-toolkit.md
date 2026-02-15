---
description: ISO/IEC 42001 certification readiness toolkit. Fastest path to audit-ready evidence aligned to ISO 42001 using AIMO artifacts. Supports readiness only; does not confer certification.
---
<!-- aimo:translation_status=translated -->

# ISO/IEC 42001 Certification Readiness Toolkit

This page is a **practical, adoption-oriented** guide to producing **audit-ready evidence** aligned to ISO/IEC 42001 using AIMO artifacts. It **supports readiness**; it does **not** confer certification. Certification decisions remain with **accredited certification bodies**.

## Goal

Produce a structured, validator-checked Evidence Bundle that supports ISO/IEC 42001–type controls (context, leadership, planning, support, operation, performance evaluation, improvement) so that auditors can efficiently locate and verify evidence.

## 5-step workflow

| Step | Action |
| --- | --- |
| **1. Establish scope and AI inventory** | Define scope (scope_ref); classify AI systems using the [taxonomy](../../standard/current/03-taxonomy/) and [dictionary](../../standard/current/05-dictionary/). |
| **2. Set management-system artifacts** | Create or reference policies, roles, and PDCA-aligned artifacts. Use [AIMO-MS / AIMO-Controls](../../conformance/) as a structure; reference [Evidence Pack Template](../../standard/current/06-ev-template/) (EP-01..EP-07). |
| **3. Produce Evidence Bundle + minimum evidence** | Build manifest, object_index, payload_index, hash_chain, signing per [Evidence Bundle structure](../../standard/current/09-evidence-bundle-structure/). Include request, review, exception, renewal, change_log per [Minimum Evidence Requirements](minimum-evidence.md). |
| **4. Run validator + checksums + change control** | Run `python validator/src/validate.py <bundle_path> --validate-profiles`. Record validator version and output. Generate SHA-256 checksums; maintain change log entries that reference impacted objects. |
| **5. Prepare audit pack** | Package the bundle (zip or equivalent); provide checksums. Optionally attach [audit report output](../../standard/current/07-validator/) (audit-json / audit-html). Use versioned URLs (e.g. `/0.1.2/`) when citing the standard. For Audit-Ready level, add [Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index) and [External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) section. |

## Checklist: ISO 42001 clause family → AIMO artifacts → evidence outputs

| ISO 42001 clause family | AIMO artifacts | Evidence outputs |
| --- | --- | --- |
| Context (4.1) | Summary, Dictionary, scope_ref | manifest scope_ref; Summary; Dictionary |
| Leadership / Policy (5.x) | Summary, review, dictionary | Review records; policy references |
| Planning (6.x) | request, review, exception, EV, Dictionary | Request/approval; risk/objectives in EV or Dictionary |
| Support (7.x) | Summary, review, EV, change_log | Documentation; competence/awareness evidence |
| Operation (8.x) | EV, request, review, exception | Operational controls; applicability |
| Performance evaluation (9.x) | EV, change_log, review, renewal | Monitoring; internal audit; management review |
| Improvement (10.x) | exception, renewal, change_log | Corrective action; continual improvement |

See [Coverage Map — ISO/IEC 42001](../../coverage-map/iso-42001/) and [ISO/IEC 42006](https://www.iso.org/standard/42006) for audit-body expectations.

## Safe language

- **Use:** "We use AIMO artifacts to support ISO/IEC 42001 readiness; certification decisions remain with accredited certification bodies."
- **Do not use:** "ISO 42001 certified by AIMO" or "AIMO certifies compliance."

## Related

- [Conformance](../../conformance/) — Levels (Foundation, Operational, Audit-Ready) and claim language
- [Trust Package](../../governance/trust-package/) — Auditor-ready materials
- [Responsibility Boundary](../../governance/responsibility-boundary/) — What AIMO does and does not provide
