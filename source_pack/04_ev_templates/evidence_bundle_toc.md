# Evidence Bundle TOC (Authoring SSOT)

**Status**: Authoring input — not user-facing documentation  
**Canonical language**: English (EN)

This document defines the Table of Contents (TOC) structure for Evidence Bundles. It is extracted from `docs/artifacts/evidence-bundle.md`.

---

## TOC Structure

| Section | Artifact | Required? | Purpose | Minimum fields | Validation |
| --- | --- | --- | --- | --- | --- |
| **Evidence** | EV records (JSON/array) | **Yes** | Record of what happened; link to request/review/exception/renewal | id, timestamp, source, summary; optional lifecycle refs | `validator/src/validate.py`, `aimo-ev.schema.json` |
| **Dictionary** | dictionary.json | **Yes** | Keys/labels/descriptions for codes and dimensions | entries (key, label, description) | `aimo-dictionary.schema.json` |
| **Summary** | summary (doc or field) | **Yes** | One-page overview for auditors | scope, period, key decisions, exceptions | — |
| **Change log** | change_log or reference | **Yes** | Audit trail of bundle/content changes | id, timestamp, actor, change description, references | — |
| **Request** | request record(s) | If applicable | Application/request for use | id, timestamp, actor/role, scope, rationale | — |
| **Review/Approval** | review record(s) | If applicable | Review and approval outcome | id, timestamp, actor/role, decision, references | — |
| **Exception** | exception record(s) | If applicable | Exception with compensating controls and expiry | id, timestamp, scope, expiry, compensating controls, renewal ref | — |
| **Renewal** | renewal record(s) | If applicable | Re-evaluation and renewal | id, timestamp, actor/role, decision, references to prior exception/EV | — |

---

## Cross-Reference Rules

### Stable IDs

Every record (EV, request, review, exception, renewal, change log entry) **MUST** have a stable, unique identifier.

### Linkage Pattern

```
Request → Review → Exception (if any) → Renewal
    ↓         ↓           ↓               ↓
   EV ←──────────────────────────────────→ EV
```

### Reference Fields

| From | To | Reference field |
| --- | --- | --- |
| EV record | Request | `request_id` |
| EV record | Review | `review_id` |
| EV record | Exception | `exception_id` |
| EV record | Renewal | `renewal_id` |
| Review | Request | `references[]` containing request id |
| Exception | Request/Review | `references[]` |
| Renewal | Exception | `references[]` |
| Change log | Any affected artifact | `references[]` |

---

## Bundle Naming

**Recommended pattern**: `{org}_{system}_{period}_{version}`

Examples:
- `acme_ai-usage_2026-Q1_v1`
- `example-corp_ml-platform_2026-H1_v2`

---

## Auditor Verification Flow

1. **Locate Summary**: Get overview of bundle scope and period.
2. **Check TOC completeness**: Required sections present?
3. **Verify traceability**: IDs and cross-references resolve?
4. **Run validator**: Schema validation passes?
5. **Review Change Log**: Changes are documented?

---

## Schema Mapping

| TOC Section | Schema | Location |
| --- | --- | --- |
| Evidence | `aimo-ev.schema.json` | `schemas/jsonschema/` |
| Dictionary | `aimo-dictionary.schema.json` | `schemas/jsonschema/` |
| Root structure | `aimo-standard.schema.json` | `schemas/jsonschema/` |

---

## Authoring Notes

- This TOC is the authoring source for `docs/artifacts/evidence-bundle.md` TOC table.
- User-facing docs should link to this structure.
- Changes to TOC structure may require schema updates (MAJOR version bump).
