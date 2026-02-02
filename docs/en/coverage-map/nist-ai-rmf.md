---
description: AIMO Standard to NIST AI RMF mapping. Traceability between AIMO taxonomy codes and NIST AI Risk Management Framework functions.
---

# NIST AI RMF mapping

> Traceability shortcuts: Taxonomy → Minimum Evidence → Validator → Human Oversight Protocol.

- [Taxonomy](../standard/current/03-taxonomy.md)
- [Minimum Evidence Requirements](../artifacts/minimum-evidence.md)
- [Log Schemas](../artifacts/log-schemas/index.md)
- [Validator](../validator/index.md)
- [Human Oversight Protocol](../governance/human-oversight-protocol.md)

This page maps selected NIST AI Risk Management Framework (Govern, Map, Measure, Manage) themes to AIMO evidence and artifacts. It is for explainability only; it does not guarantee conformity to the NIST AI RMF. Verify against the NIST publication.


## Mapping table

| Framework reference / topic | AIMO evidence / where in AIMO | Evidence Bundle / Minimum Evidence | Artifacts & validation | Notes |
| --- | --- | --- | --- | --- |
| Govern 1.1 – Policies | [Scope](../standard/current/02-scope.md), [Taxonomy](../standard/current/03-taxonomy.md) | Dictionary, Summary, review; review | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informative; verify against NIST publication. |
| Govern 1.2 – Roles and responsibilities | [Minimum Evidence](../artifacts/minimum-evidence.md) | request, review | templates/ev/ev_template.md | Informative; verify against NIST publication. |
| Govern 2.1 – Accountability | [Evidence Bundle](../artifacts/evidence-bundle.md) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | Informative; verify against NIST publication. |
| Govern 3.1 – Risk management | [Scope](../standard/current/02-scope.md) | request, review, exception | templates/ev/ | Informative; verify against NIST publication. |
| Govern 4.1 – Culture | [Overview](../standard/current/01-overview.md) | Summary, review; review | — | Informative; verify against NIST publication. |
| Map 1.1 – Context mapping | [Scope](../standard/current/02-scope.md), [Dictionary](../standard/current/05-dictionary.md) | Dictionary, Summary; request | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informative; verify against NIST publication. |
| Map 2.1 – Data and documentation | [EV Template](../standard/current/06-ev-template.md) | EV, Dictionary, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informative; verify against NIST publication. |
| Map 3.1 – Data governance | [Dictionary](../standard/current/05-dictionary.md) | Dictionary, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informative; verify against NIST publication. |
| Measure 1.1 – Performance and impact | [EV Template](../standard/current/06-ev-template.md) | EV | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informative; verify against NIST publication. |
| Measure 2.1 – Monitoring | [Minimum Evidence](../artifacts/minimum-evidence.md) | EV, change_log; change_log, integrity | templates/ev/ | Informative; verify against NIST publication. |
| Measure 3.1 – Testing and validation | [Validator](../standard/current/07-validator.md) | EV | validator/rules/, validator/src/; schema_validate_ev | Informative; verify against NIST publication. |
| Manage 1.1 – Allocation of resources | [Overview](../standard/current/01-overview.md) | Summary, review; review | — | Informative; verify against NIST publication. |
| Manage 2.1 – Incidents and responses | [Minimum Evidence](../artifacts/minimum-evidence.md) | exception, renewal, change_log | templates/ev/ev_template.md | Informative; verify against NIST publication. |
| Manage 3.1 – Change management | [Evidence Bundle](../artifacts/evidence-bundle.md) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | Informative; verify against NIST publication. |
| Manage 4.1 – Review and update | [Minimum Evidence](../artifacts/minimum-evidence.md) | renewal, review; review, renewal | templates/ev/ | Informative; verify against NIST publication. |
| Manage 5.1 – Communication | [Evidence Bundle](../artifacts/evidence-bundle.md) | Summary, change_log; change_log | templates/ev/ | Informative; verify against NIST publication. |
