---
description: AIMO Standard to ISMS (ISO 27001/27002) mapping. Traceability between AIMO taxonomy and information security management system controls.
---

# ISMS view (ISO/IEC 27001/27002) mapping

> Traceability shortcuts: Taxonomy → Minimum Evidence → Validator → Human Oversight Protocol.

- [Taxonomy](../standard/current/03-taxonomy.md)
- [Minimum Evidence Requirements](../artifacts/minimum-evidence.md)
- [Log Schemas](../artifacts/log-schemas/index.md)
- [Validator](../validator/index.md)
- [Human Oversight Protocol](../governance/human-oversight-protocol.md)

This page maps selected ISO/IEC 27001/27002 themes (change management, access control, logging, evidence integrity) to AIMO evidence and artifacts. It is for explainability only; it does not guarantee conformity to ISO/IEC 27001 or 27002. Verify against the published standards.


## Mapping table

| Framework reference / topic | AIMO evidence / where in AIMO | Evidence Bundle / Minimum Evidence | Artifacts & validation | Notes |
| --- | --- | --- | --- | --- |
| A.5.24 – Information security in project management | [Scope](../standard/current/02-scope.md) | request, review | templates/ev/ | Informative; verify against official text. |
| A.5.29 – Information security during disruption | [Minimum Evidence](../artifacts/minimum-evidence.md) | exception, renewal | templates/ev/ev_template.md | Informative; verify against official text. |
| A.5.30 – ICT readiness for business continuity | [Overview](../standard/current/01-overview.md) | Summary; integrity | — | Informative; verify against official text. |
| A.8.1 – Inventory of assets | [Dictionary](../standard/current/05-dictionary.md) | Dictionary, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informative; verify against official text. |
| A.8.2 – Information classification | [Taxonomy](../standard/current/03-taxonomy.md) | Dictionary; review | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informative; verify against official text. |
| A.8.3 – Access control | [Minimum Evidence](../artifacts/minimum-evidence.md) | —; integrity | — | Informative; verify against official text. |
| A.8.15 – Logging | [EV Template](../standard/current/06-ev-template.md) | EV, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informative; verify against official text. |
| A.8.16 – Monitoring activities | [Minimum Evidence](../artifacts/minimum-evidence.md) | EV, change_log; change_log, integrity | templates/ev/ | Informative; verify against official text. |
| A.8.32 – Change management | [Evidence Bundle](../artifacts/evidence-bundle.md) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | Informative; verify against official text. |
| A.8.33 – Test information | [Validator](../standard/current/07-validator.md) | EV | validator/rules/, validator/src/; schema_validate_ev | Informative; verify against official text. |
