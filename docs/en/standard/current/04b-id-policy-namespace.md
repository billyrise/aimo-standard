---
description: AIMO v0.1 ID Policy and namespace separation - EV for Evidence (artifacts) only, LG for Log/Event Type (taxonomy). Prevents ID collisions.
---

# ID Policy / Namespace (v0.1)

This page defines the **normative** ID policy for AIMO Standard v0.1 to avoid collisions between taxonomy codes and evidence artifact identifiers.

## Namespace Separation

| Prefix | Use | Scope | Example |
|--------|-----|--------|---------|
| **EV-** | **Evidence (artifact) ID only** | Unique identifier for an evidence *object* (record, document, bundle item) | `EV-20260115-001`, `EV-20260131-002` |
| **LG-** | **Log/Event Type (Taxonomy)** | Taxonomy dimension for *classifying* log/event/record types (request record, access log, etc.) | `LG-001`, `LG-002`, … `LG-015` |

- **EV** is reserved for **Evidence artifact IDs** (e.g. in `evidence[].id`, `references[]`). Do **not** use EV as a taxonomy dimension or as taxonomy codes in `evidence[].codes`.
- **LG** is the **Log/Event Type** taxonomy dimension. Use **only** `LG-xxx` codes (e.g. `LG-001`, `LG-007`) in taxonomy fields such as `evidence[].codes.LG`, Evidence Pack manifest `codes.LG`, and dictionary entries for log/event classification.

## Rationale

Previously, the taxonomy used **EV-001** … **EV-015** for "Evidence Type" (request record, access log, etc.). This collided with the use of **EV-** for **Evidence artifact IDs** (e.g. `evidence[].id`). To remove ambiguity:

- **Taxonomy (log/event classification)** → **LG-** (Log/Event Type): `LG-001` … `LG-015`.
- **Evidence (artifact identifier)** → **EV-** only: e.g. `EV-YYYYMMDD-NNN` or similar stable IDs.

Validators **must** reject:

- Use of **EV** as a taxonomy dimension in `evidence[].codes` (e.g. `"EV": ["EV-001"]`). Use **LG** and `LG-xxx` instead.
- Use of taxonomy codes **EV-001** … **EV-999** in any taxonomy/codes field; only **LG-xxx** are allowed for the log/event dimension.

## v0.1 prefix inventory

| Prefix | v0.1 status | Use |
|--------|-------------|-----|
| **EV-** | In use | Evidence artifact ID only (e.g. `evidence[].id`) |
| **LG-** | In use | Log/Event Type taxonomy dimension (`evidence[].codes.LG`) |
| **SC-** | In use | Scope (e.g. scope identifier) |
| **RQ-**, **CT-**, **CL-**, **TP-**, **FD-**, **RM-**, **AP-**, **CH-**, **PR-** | Reserved | Requirement, Control, Claim, Test Plan, Finding, Remediation, Approval, Change, Profile — for future use; not yet normative in v0.1 |

## References

- [Taxonomy](../03-taxonomy/) — dimension **LG: Log/Event Type**
- [Evidence Pack Template](../06-ev-template/) — `codes.LG` and `ev_codes` / `ev_type` use **LG-xxx**
- [Validator](../07-validator/) — namespace and collision checks
