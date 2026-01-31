# Conformance (Authoring SSOT)

**Status**: Authoring input — not user-facing documentation  
**Canonical language**: English (EN)

This document defines conformance levels, MUST/SHOULD definitions, and how-to-claim guidance. It serves as the authoring source for `docs/conformance/index.md`.

---

## 1. MUST / SHOULD Definitions

Following RFC 2119 conventions as used in the AIMO Standard:

| Keyword | Meaning |
| --- | --- |
| **MUST** / **SHALL** | Absolute requirement. Implementations must satisfy this to claim conformance. |
| **MUST NOT** / **SHALL NOT** | Absolute prohibition. Implementations must not include this behavior. |
| **SHOULD** / **RECOMMENDED** | Best practice. Implementations should satisfy this unless there is a valid reason not to. |
| **SHOULD NOT** / **NOT RECOMMENDED** | Best practice to avoid. Implementations should not do this unless there is a valid reason. |
| **MAY** / **OPTIONAL** | Truly optional. Implementations may include or exclude at their discretion. |

### Japanese Mapping

| EN | JA |
| --- | --- |
| MUST | 必須 (hissu) / しなければならない |
| SHOULD | 推奨 (suishou) / すべきである |
| MAY | 任意 (nin'i) / してもよい |

---

## 2. Conformance Levels

**Current status**: Conformance levels are defined at a high level. Detailed criteria will be expanded in a future change unit.

### Level Overview

| Level | Scope | Evidence requirements |
| --- | --- | --- |
| **Structural** | Bundle structure and schema validation pass | Validator checks pass; required fields present |
| **Traceability** | Lifecycle linkages are complete | Request → Review → Exception → Renewal chain is intact |
| **Full** | All MUST requirements satisfied | All lifecycle groups, integrity/access documented |

### Normative Source

Conformance requirements are defined in:
- `docs/standard/current/` — normative specification
- `docs/conformance/index.md` — user-facing conformance hub

---

## 3. How to Claim Conformance (Authoring Viewpoint)

Adopters claim conformance by satisfying the checklist below. This checklist is the authoring source for user-facing guidance.

### Pre-submission Checklist

| # | Check | Reference | Status |
| --- | --- | --- | --- |
| 1 | **Evidence Bundle exists** | `artifacts/evidence-bundle` | ☐ |
| 2 | **Required files present**: EV records, Dictionary, Summary, Change Log | `artifacts/evidence-bundle` (TOC) | ☐ |
| 3 | **MUST fields populated** per lifecycle group | `artifacts/minimum-evidence` | ☐ |
| 4 | **Validator passes** (no errors) | `validator/index` | ☐ |
| 5 | **Traceability intact**: IDs and cross-references resolve | `artifacts/evidence-bundle` (Traceability) | ☐ |
| 6 | **Checksums generated** (SHA-256) | `releases/index` | ☐ |
| 7 | **Version alignment documented** | Release tag reference | ☐ |

### Lifecycle Groups (MUST fields)

Reference: `docs/artifacts/minimum-evidence.md`

| Lifecycle | MUST fields |
| --- | --- |
| **Request** | id, timestamp, actor/role, scope, rationale |
| **Review/Approval** | id, timestamp, actor/role, decision, scope, rationale, request reference |
| **Exception** | id, timestamp, scope, expiry, compensating controls, rationale, review/request reference |
| **Renewal** | id, timestamp, actor/role, decision, references to prior exception/request/review |
| **Change Log** | id, timestamp, actor, change description, references |
| **Integrity/Access** | Documented access control, retention policy, integrity mechanisms, audit trail |

---

## 4. Validator Usage

The reference validator (`validator/src/validate.py`) checks:

1. Schema validation against `aimo-standard.schema.json` (root)
2. Schema validation against `aimo-dictionary.schema.json` (dictionary)
3. Schema validation against `aimo-ev.schema.json` (each EV record)

### Usage

```bash
python validator/src/validate.py path/to/root.json
# Expected output: "OK" or error messages
```

### What validator does NOT check

- Content accuracy (validator checks structure, not meaning)
- Traceability linkages (cross-reference resolution is not yet implemented)
- Integrity controls (adopter responsibility)

---

## 5. Translation Rules

- MUST/SHOULD keywords should be preserved in English or translated consistently.
- Japanese translations must match heading structure.

---

## Authoring Notes

- This file is authoring input; user-facing content is in `docs/conformance/index.md`.
- Conformance levels are intentionally minimal in v0.1; expansion is planned for future CUs.
- Any mismatch between this file and published docs should be logged in `00_manifest.md` Gap Log.
