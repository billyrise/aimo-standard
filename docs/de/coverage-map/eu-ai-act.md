---
description: AIMO Standard zu EU AI Act-Zuordnung. Nachverfolgbarkeit zwischen AIMO-Taxonomiecodes und EU AI Act-Risikokategorien und -Anforderungen.
---

# EU AI Act-Zuordnung

> Nachverfolgbarkeits-Shortcuts: Taxonomie → Mindestanforderungen an Evidence → Validator → Human Oversight Protocol.

- [Taxonomie](../standard/current/03-taxonomy.md)
- [Mindestanforderungen an Evidence](../artifacts/minimum-evidence.md)
- [Log Schemas](../artifacts/log-schemas/index.md)
- [Validator](../validator/index.md)
- [Human Oversight Protocol](../governance/human-oversight-protocol.md)

Diese Seite ordnet ausgewählte EU AI Act-Themen (Dokumentation, Aufzeichnungspflichten, Risikomanagement, menschliche Aufsicht, Transparenz) AIMO Evidence und Artefakten zu. Sie ist nur übergeordnet und stellt **keine** Rechtsberatung dar und garantiert keine Konformität. Überprüfen Sie gegen den offiziellen Gesetzestext.


## Zuordnungstabelle

| Framework-Referenz / Thema | AIMO Evidence / Wo in AIMO | Evidence Bundle / Mindestanforderungen | Artefakte & Validierung | Hinweise |
| --- | --- | --- | --- | --- |
| Art 9 – Risikomanagement (Pflichten) | [Scope](../standard/current/02-scope.md) | request, review, exception | templates/ev/ | Nur übergeordnet; keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Art 10 – Data Governance | [Dictionary](../standard/current/05-dictionary.md) | Dictionary, EV | schemas/jsonschema/; schema_validate_dictionary | Nur übergeordnet; keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Art 11 – Dokumentation (Hochrisiko) | [EV Template](../standard/current/06-ev-template.md), [Evidence Bundle](../artifacts/evidence-bundle.md) | EV, Dictionary, Summary; request, review | schemas/jsonschema/, templates/ev/; schema_validate_ev | Nur übergeordnet; keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Art 12 – Aufzeichnungspflichten | [Evidence Bundle](../artifacts/evidence-bundle.md), [Mindestanforderungen](../artifacts/minimum-evidence.md) | EV, change_log, request, review | examples/evidence_bundle_minimal/; schema_validate_ev | Nur übergeordnet; keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Art 13 – Transparenz (Benutzerinformation) | [Scope](../standard/current/02-scope.md) | Summary, EV; review | templates/ev/ | Nur übergeordnet; keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Art 14 – Menschliche Aufsicht | [Mindestanforderungen](../artifacts/minimum-evidence.md) | review, exception; review, exception | templates/ev/ev_template.md | Nur übergeordnet; keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Art 17 – Risikomanagement (Hochrisiko) | [Scope](../standard/current/02-scope.md) | request, review, exception, renewal | templates/ev/ | Nur übergeordnet; keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Art 26 – Transparenz (begrenztes Risiko) | [Scope](../standard/current/02-scope.md) | Summary, EV; review | templates/ev/ | Nur übergeordnet; keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Art 29 – Dokumentation (Allzweck-KI) | [EV Template](../standard/current/06-ev-template.md) | EV, Dictionary, Summary; request, review | schemas/jsonschema/; schema_validate_ev | Nur übergeordnet; keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Art 52 – Transparenz (Bereitsteller) | [Mindestanforderungen](../artifacts/minimum-evidence.md) | EV, Summary; review | templates/ev/ | Nur übergeordnet; keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Erwägungsgründe – Rechenschaftspflicht | [Evidence Bundle](../artifacts/evidence-bundle.md) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | Nur übergeordnet; keine Rechtsberatung. Gegen offiziellen Text prüfen. |
