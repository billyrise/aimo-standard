---
description: AIMO Standard zu EU-KI-Verordnung-Zuordnung. Nachverfolgbarkeit zwischen AIMO-Taxonomiecodes und EU-KI-Verordnung-Risikokategorien und -anforderungen.
---
<!-- aimo:translation_status=translated -->

# EU-KI-Verordnung-Zuordnung

> Nachverfolgbarkeit: Taxonomie → Mindestanforderungen an Evidence → Validator → Human Oversight Protocol.

- [Taxonomie](../../standard/current/03-taxonomy/)
- [Mindestanforderungen an Evidence](../../artifacts/minimum-evidence/)
- [Log Schemas](../../artifacts/log-schemas/)
- [Validator](../../validator/)
- [Human Oversight Protocol](../../governance/human-oversight-protocol/)

Diese Seite ordnet ausgewählte Themen der EU-KI-Verordnung (Dokumentation, Aufzeichnung, Risikomanagement, menschliche Aufsicht, Transparenz) AIMO-Evidenz und -Artefakten zu. Sie ist nur auf hoher Ebene; sie **stellt keine Rechtsberatung dar** und garantiert keine Konformität. Gegen den offiziellen Rechtstext prüfen.

**Referenz:** Verordnung (EU) 2024/1689 (KI-Verordnung). Alle nachfolgenden Artikelnummern beziehen sich auf diese Verordnung.

## Zuordnungstabelle

| Rahmenreferenz / Thema | AIMO-Evidenz / wo in AIMO | Evidence Bundle / Mindestanforderungen | Artefakte & Validierung | Hinweise |
| --- | --- | --- | --- | --- |
| Art. 4 – KI-Kompetenz | [Umfang](../../standard/current/02-scope/) | Summary, EV; review | templates/ev/ | Querschnitt; Evidenz organisatorischer Fähigkeit/Schulung (Überblick). Keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Art. 9 – Risikomanagementsystem | [Umfang](../../standard/current/02-scope/) | request, review, exception, renewal | templates/ev/ | Hochrisiko-KI-Systeme (Titel III). Keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Art. 10 – Daten und Datengovernance | [Wörterbuch](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/; schema_validate_dictionary | Keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Art. 11 – Technische Dokumentation (Hochrisiko) | [EV-Vorlage](../../standard/current/06-ev-template/), [Evidence Bundle](../../artifacts/evidence-bundle/) | EV, Dictionary, Summary; request, review | schemas/jsonschema/, templates/ev/; **Anhang IV**: [Beispiele > EU-Anhang-IV-Beispiel](../../examples/) (`examples/evidence_bundle_v01_annex_iv_sample/`); Profil: `coverage_map/profiles/eu_ai_act_annex_iv.json`. Beispielbündel normenkonform (signatures/, hashes/, Payload mit anhang-IV-orientierter technischer Dokumentation). Siehe Beispiele (weitere Beispielinhalte in künftiger Version). | Nur Überblick; keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Art. 12 – Aufzeichnung | [Evidence Bundle](../../artifacts/evidence-bundle/), [Mindestanforderungen an Evidence](../../artifacts/minimum-evidence/) | EV, change_log, request, review | examples/evidence_bundle_minimal/; schema_validate_ev | Keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Art. 13 – Transparenz und Informationsbereitstellung an Betreiber/Nutzer | [Umfang](../../standard/current/02-scope/) | Summary, EV; review | templates/ev/ | Hochrisiko-Kontext. Keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Art. 14 – Menschliche Aufsicht | [Mindestanforderungen an Evidence](../../artifacts/minimum-evidence/) | review, exception | templates/ev/ev_template.md | Keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Art. 15 – Genauigkeit, Robustheit, Cybersicherheit | [Mindestanforderungen an Evidence](../../artifacts/minimum-evidence/) | EV (Evidenzcodes / Risikocodes, Überblick) | templates/ev/ | Nur Überblick-Zuordnung. Keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Art. 17 – Qualitätsmanagementsystem | [Umfang](../../standard/current/02-scope/) | Summary, review (Organisationsprozess) | templates/ev/ | Unterscheidet sich von Art. 9 (Risikomanagementsystem). Keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Transparenzpflichten (anwendungsabhängig) | [Umfang](../../standard/current/02-scope/), [Mindestanforderungen an Evidence](../../artifacts/minimum-evidence/) | Summary, EV; review | templates/ev/ | Anwendbare Bestimmungen hängen vom Anwendungsfall ab (z. B. begrenztes Risiko, Betreiberpflichten). Keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| GPAI-Modellpflichten | [EV-Vorlage](../../standard/current/06-ev-template/), [Evidence Bundle](../../artifacts/evidence-bundle/) | EV-Vorlage, Evidence Bundle (Evidenzstrukturierungsrahmen) | schemas/jsonschema/; schema_validate_ev | AIMO stellt einen Rahmen zur Evidenzorganisation bereit; die tatsächlichen Pflichten sind in der Verordnung definiert. Keine Rechtsberatung. Gegen offiziellen Text prüfen. |
| Erwägungsgründe – Rechenschaftspflicht | [Evidence Bundle](../../artifacts/evidence-bundle/) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | Keine Rechtsberatung. Gegen offiziellen Text prüfen. |

## Geltungsbeginn / Anwendbarkeit (Überblick)

Das Folgende orientiert sich am **offiziellen EU-Zeitplan** (KI-Verordnung-Service-Desk / Kommission). Es ist **keine Rechtsberatung** und garantiert keine Richtigkeit. Immer mit dem **offiziellen Rechtstext** und den zuständigen Behörden bestätigen.

| Phase | Datum | Was gilt (Überblick) |
| --- | --- | --- |
| Inkrafttreten | August 2024 | Verordnung in Kraft; die meisten materiellen Pflichten noch nicht anwendbar. |
| Allgemeine Bestimmungen & Verbote | 02.02.2025 | Verbotene Praktiken (inakzeptables Risiko); bestimmte KI-Kompetenz-bezogene Bestimmungen. |
| GPAI-Regeln & Governance | 02.08.2025 | Regeln zu benannten Stellen, GPAI, Governance, Vertraulichkeit, Sanktionen; Verhaltenskodizes. |
| Mehrheitsregeln + Anhang III Hochrisiko + Art. 50 Transparenz | 02.08.2026 | Vollständige Anwendung für Hochrisiko-KI-Systeme (Anhang III), Art. 50 Transparenzpflichten. |
| Hochrisiko in regulierten Produkten | 02.08.2027 | Hochrisiko-KI-Systeme eingebettet in unter EU-Produktrecht fallende Produkte. |

## Harmonisierte Normen und Konformitätsvermutung (Art. 40)

Wenn **harmonisierte Normen** im EU-Amtsblatt unter der KI-Verordnung veröffentlicht werden, kann deren Einhaltung eine **Konformitätsvermutung** für die entsprechenden Anforderungen begründen. Die genaue Liste und die Daten hängen von der Normungsarbeit und der Veröffentlichung im Amtsblatt ab. AIMO-Zuordnungen sind informativ und begründen keine Konformitätsvermutung. Für den aktuellen Stand siehe die [KI-Verordnung-Standardisierung](https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation) der Kommission und **Referenzen** unten.

## 2026-Leitlinien des KI-Büros (Umsetzungsdetail)

Die Europäische Kommission hat angekündigt, dass das **KI-Büro** 2026 **praktische Leitlinien** erarbeiten wird, u. a. zu:

- Hochrisiko-Klassifizierung
- Art. 50 (Transparenz) Umsetzung
- Meldung von Vorfällen
- QMS-bezogene Elemente

Diese Leitlinien sind **Aktualisierungsauslöser** für AIMO-Profile und Coverage-Zuordnungen: Nach ihrer Veröffentlichung sollten Adoptierende Evidenz und Zuordnungen an die neueste offizielle Leitlinie anpassen. AIMO interpretiert oder garantiert keine Konformität mit diesen Leitlinien.

!!! warning "Keine Rechtsberatung"
    Diese Seite dient nur der Erläuterung. Sie müssen Anwendbarkeit und Daten anhand der offiziellen Verordnung sowie ggf. Durchführungs- oder Änderungsrechtsakten prüfen. AIMO erteilt keine Rechtsberatung und garantiert keine Konformität.

!!! note "Rechtlicher Hinweis / Informative Zuordnung"
    Diese Seite ist **nur informativ**. Die rechtliche Auslegung sollte auf der offiziellen Verordnung (EUR-Lex) und den Veröffentlichungen der Europäischen Kommission beruhen. AIMO erteilt keine Rechtsberatung und garantiert keine Konformität.

## Referenzen

**Primärquellen**

- [Verordnung (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689) (EUR-Lex) — KI-Verordnung (Rechtstext)
- [Zeitplan für die Umsetzung der KI-Verordnung](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act) — KI-Verordnung-Service-Desk der Europäischen Kommission (Umsetzungszeitplan)
- [Standardisierung der KI-Verordnung](https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation) — Digitale Strategie der Europäischen Kommission (harmonisierte Normen, Konformitätsvermutung)

**Sonstige**

- Europäische Kommission / KI-Büro — Leitlinien und Zeitplan (siehe KI-Verordnung-Service-Desk und Kommissionsnachrichten für aktuelle URLs)
- [EPRS — EU-KI-Verordnung-Umsetzung](https://www.europarl.europa.eu/thinktank/) — Parlaments-Briefing (informativ)
