---
description: AIMO Standard zu NIST AI RMF-Zuordnung. Nachverfolgbarkeit zwischen AIMO-Taxonomiecodes und NIST AI Risk Management Framework-Funktionen.
---
<!-- aimo:translation_status=translated -->

# NIST AI RMF-Zuordnung

> Nachverfolgbarkeits-Shortcuts: Taxonomie → Mindestanforderungen an Evidence → Validator → Human Oversight Protocol.

- [Taxonomie](../../standard/current/03-taxonomy/)
- [Mindestanforderungen an Evidence](../../artifacts/minimum-evidence/)
- [Log Schemas](../../artifacts/log-schemas/)
- [Validator](../../validator/)
- [Human Oversight Protocol](../../governance/human-oversight-protocol/)

Diese Seite ordnet ausgewählte NIST AI Risk Management Framework (Govern, Map, Measure, Manage)-Themen AIMO Evidence und Artefakten zu. Sie dient nur der Erklärbarkeit; sie garantiert keine Konformität mit dem NIST AI RMF. Überprüfen Sie gegen die NIST-Publikation.


## Zuordnungstabelle

| Framework-Referenz / Thema | AIMO Evidence / Wo in AIMO | Evidence Bundle / Mindestanforderungen | Artefakte & Validierung | Hinweise |
| --- | --- | --- | --- | --- |
| Govern 1.1 – Richtlinien | [Scope](../../standard/current/02-scope/), [Taxonomie](../../standard/current/03-taxonomy/) | Dictionary, Summary, review; review | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativ; gegen NIST-Publikation prüfen. |
| Govern 1.2 – Rollen und Verantwortlichkeiten | [Mindestanforderungen](../../artifacts/minimum-evidence/) | request, review | templates/ev/ev_template.md | Informativ; gegen NIST-Publikation prüfen. |
| Govern 2.1 – Rechenschaftspflicht | [Evidence Bundle](../../artifacts/evidence-bundle/) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | Informativ; gegen NIST-Publikation prüfen. |
| Govern 3.1 – Risikomanagement | [Scope](../../standard/current/02-scope/) | request, review, exception | templates/ev/ | Informativ; gegen NIST-Publikation prüfen. |
| Govern 4.1 – Kultur | [Übersicht](../../standard/current/01-overview/) | Summary, review; review | — | Informativ; gegen NIST-Publikation prüfen. |
| Map 1.1 – Kontextzuordnung | [Scope](../../standard/current/02-scope/), [Dictionary](../../standard/current/05-dictionary/) | Dictionary, Summary; request | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativ; gegen NIST-Publikation prüfen. |
| Map 2.1 – Daten und Dokumentation | [EV Template](../../standard/current/06-ev-template/) | EV, Dictionary, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informativ; gegen NIST-Publikation prüfen. |
| Map 3.1 – Data Governance | [Dictionary](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativ; gegen NIST-Publikation prüfen. |
| Measure 1.1 – Leistung und Auswirkung | [EV Template](../../standard/current/06-ev-template/) | EV | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informativ; gegen NIST-Publikation prüfen. |
| Measure 2.1 – Überwachung | [Mindestanforderungen](../../artifacts/minimum-evidence/) | EV, change_log; change_log, integrity | templates/ev/ | Informativ; gegen NIST-Publikation prüfen. |
| Measure 3.1 – Test und Validierung | [Validator](../../standard/current/07-validator/) | EV | validator/rules/, validator/src/; schema_validate_ev | Informativ; gegen NIST-Publikation prüfen. |
| Manage 1.1 – Ressourcenzuweisung | [Übersicht](../../standard/current/01-overview/) | Summary, review; review | — | Informativ; gegen NIST-Publikation prüfen. |
| Manage 2.1 – Incidents und Reaktionen | [Mindestanforderungen](../../artifacts/minimum-evidence/) | exception, renewal, change_log | templates/ev/ev_template.md | Informativ; gegen NIST-Publikation prüfen. |
| Manage 3.1 – Änderungsmanagement | [Evidence Bundle](../../artifacts/evidence-bundle/) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | Informativ; gegen NIST-Publikation prüfen. |
| Manage 4.1 – Überprüfung und Aktualisierung | [Mindestanforderungen](../../artifacts/minimum-evidence/) | renewal, review; review, renewal | templates/ev/ | Informativ; gegen NIST-Publikation prüfen. |
| Manage 5.1 – Kommunikation | [Evidence Bundle](../../artifacts/evidence-bundle/) | Summary, change_log; change_log | templates/ev/ | Informativ; gegen NIST-Publikation prüfen. |
