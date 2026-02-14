---
description: AIMO Standard zu ISMS (ISO 27001/27002)-Zuordnung. Nachverfolgbarkeit zwischen AIMO-Taxonomie und Informationssicherheits-Managementsystem-Kontrollen.
---

# ISMS-Ansicht (ISO/IEC 27001/27002)-Zuordnung

> Nachverfolgbarkeits-Shortcuts: Taxonomie → Mindestanforderungen an Evidence → Validator → Human Oversight Protocol.

- [Taxonomie](../../standard/current/03-taxonomy/)
- [Mindestanforderungen an Evidence](../../artifacts/minimum-evidence/)
- [Log Schemas](../../artifacts/log-schemas/)
- [Validator](../../validator/)
- [Human Oversight Protocol](../../governance/human-oversight-protocol/)

Diese Seite ordnet ausgewählte ISO/IEC 27001/27002-Themen (Änderungsmanagement, Zugriffskontrolle, Protokollierung, Evidence-Integrität) AIMO Evidence und Artefakten zu. Sie dient nur der Erklärbarkeit; sie garantiert keine Konformität mit ISO/IEC 27001 oder 27002. Überprüfen Sie gegen die veröffentlichten Standards.


## Zuordnungstabelle

| Framework-Referenz / Thema | AIMO Evidence / Wo in AIMO | Evidence Bundle / Mindestanforderungen | Artefakte & Validierung | Hinweise |
| --- | --- | --- | --- | --- |
| A.5.24 – Informationssicherheit im Projektmanagement | [Scope](../../standard/current/02-scope/) | request, review | templates/ev/ | Informativ; gegen offiziellen Text prüfen. |
| A.5.29 – Informationssicherheit bei Störungen | [Mindestanforderungen](../../artifacts/minimum-evidence/) | exception, renewal | templates/ev/ev_template.md | Informativ; gegen offiziellen Text prüfen. |
| A.5.30 – IKT-Bereitschaft für Geschäftskontinuität | [Übersicht](../../standard/current/01-overview/) | Summary; integrity | — | Informativ; gegen offiziellen Text prüfen. |
| A.8.1 – Inventar von Assets | [Dictionary](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativ; gegen offiziellen Text prüfen. |
| A.8.2 – Informationsklassifizierung | [Taxonomie](../../standard/current/03-taxonomy/) | Dictionary; review | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativ; gegen offiziellen Text prüfen. |
| A.8.3 – Zugriffskontrolle | [Mindestanforderungen](../../artifacts/minimum-evidence/) | —; integrity | — | Informativ; gegen offiziellen Text prüfen. |
| A.8.15 – Protokollierung | [EV Template](../../standard/current/06-ev-template/) | EV, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informativ; gegen offiziellen Text prüfen. |
| A.8.16 – Überwachungsaktivitäten | [Mindestanforderungen](../../artifacts/minimum-evidence/) | EV, change_log; change_log, integrity | templates/ev/ | Informativ; gegen offiziellen Text prüfen. |
| A.8.32 – Änderungsmanagement | [Evidence Bundle](../../artifacts/evidence-bundle/) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | Informativ; gegen offiziellen Text prüfen. |
| A.8.33 – Testinformationen | [Validator](../../standard/current/07-validator/) | EV | validator/rules/, validator/src/; schema_validate_ev | Informativ; gegen offiziellen Text prüfen. |
