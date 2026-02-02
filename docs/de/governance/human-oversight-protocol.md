---
description: AIMO Human Oversight Protocol - Grenze zwischen automatisierter Validierung und menschlicher Überprüfung. Verantwortlichkeiten für maschinelle vs. menschliche Beurteilung in der KI-Governance.
---

# Human Oversight Protocol

Diese Seite definiert die Grenze zwischen dem, was automatische Validierung (Validator) prüfen kann, und dem, was menschliche Überprüfung (Human-in-the-Loop) erfordert. Sie klärt die Verantwortlichkeiten für maschinelle vs. menschliche Beurteilung in KI-Governance-Evidence-Prozessen.

## Zweck

Automatisierte Validierungstools können effizient strukturelle und syntaktische Korrektheit prüfen, können aber menschliche Beurteilung für kontextabhängige Entscheidungen nicht ersetzen. Dieses Protokoll:

- Klärt, was der Validator verifizieren kann und was nicht
- Definiert den Umfang der menschlichen Überprüfung, die für effektive Governance erforderlich ist
- Unterstützt Audit-Erklärungen durch Dokumentation des Human-Oversight-Prozesses
- Bietet einen Rahmen für Organisationen, die KI-Governance-Workflows implementieren

## Was automatische Validierung leisten kann (Validator-Umfang)

Der AIMO Validator und ähnliche automatisierte Tools können prüfen:

| Fähigkeit | Beschreibung |
| --- | --- |
| **Vollständigkeit erforderlicher Felder/Dokumente** | Überprüfen, dass alle Pflichtfelder in Manifesten, EV-Datensätzen und anderen Artefakten vorhanden sind |
| **Strukturelle Konsistenz** | Referenzen, IDs und Querverweise zwischen Artefakten validieren (z.B. request_id → review_id) |
| **Schema-Validierung** | Prüfen, dass JSON/YAML-Artefakte definierten Schemas entsprechen |
| **Code-Format-Validierung** | Verifizieren, dass Taxonomie-Codes erwarteten Mustern entsprechen (z.B. `UC-001`) |
| **Integritätsprüfungen** | Hash-Format und -Vorhandensein validieren (keine Neuberechnung gegen Inhalt) |
| **Dictionary-Validierung** | Bestätigen, dass Codes im Taxonomie-Dictionary existieren |

Siehe [Validator](../standard/current/07-validator.md) für detaillierte Validierungsregeln und Referenzimplementierung.

## Was menschliche Überprüfung erfordert (Human-in-the-Loop-Umfang)

Die folgenden Bereiche erfordern menschliche Beurteilung und können nicht automatisiert werden:

| Fähigkeit | Beschreibung |
| --- | --- |
| **Kontextabhängige Risikobeurteilung** | Bewertung von Geschäfts-, Ethik- und Betriebsrisiken basierend auf organisatorischem Kontext |
| **Ausnahmegenehmigungsbegründung** | Bewertung, ob eine Ausnahme gerechtfertigt ist und kompensierende Kontrollen angemessen sind |
| **Behebungsentscheidungen** | Priorisierung von Korrekturen, Ressourcenzuweisung und Festlegung von Zeitplänen |
| **Policy-Kompromisse** | Abwägung konkurrierender Anforderungen (z.B. Geschwindigkeit vs. Gründlichkeit, Kosten vs. Risiko) |
| **Restrisiko-Akzeptanz** | Entscheidung, ob verbleibende Risiken nach Kontrollen akzeptabel sind |
| **Bereichsübergreifende Auswirkungsbewertung** | Bewertung von Implikationen für Recht, HR, Betrieb und andere Funktionen |
| **Inhaltsgenauigkeitsprüfung** | Bestätigung, dass Evidence-Inhalte sachlich korrekt und vollständig sind |
| **Stakeholder-Kommunikation** | Erklärung von Entscheidungen gegenüber Prüfern, Aufsichtsbehörden und Führungskräften |

## Verantwortungsgrenze

| Aspekt | Validator (Maschine) | Menschlicher Reviewer |
| --- | --- | --- |
| **Struktur** | ✓ Kann verifizieren | Überprüfen bei Kennzeichnung |
| **Vollständigkeit** | ✓ Kann Felder verifizieren | Inhaltsangemessenheit prüfen |
| **Format** | ✓ Kann verifizieren | — |
| **Risikobeurteilung** | ✗ Kann nicht bewerten | ✓ Muss bewerten |
| **Ausnahmegenehmigung** | ✗ Kann nicht entscheiden | ✓ Muss entscheiden |
| **Behebungspriorität** | ✗ Kann nicht priorisieren | ✓ Muss priorisieren |
| **Rechtliche Interpretation** | ✗ Kann nicht interpretieren | ✓ Muss mit Rechtsberatung verifizieren |
| **Audit-Schlussfolgerung** | ✗ Kann nicht schlussfolgern | ✓ Verantwortung des Prüfers |

!!! note "Komplementäre Rollen"
    Validator und menschliche Überprüfung sind **komplementär**, keine Alternativen. Der Validator stellt strukturelle Konsistenz vor der menschlichen Überprüfung sicher; menschliche Überprüfung stellt kontextuelle Angemessenheit sicher.

## Evidence-Erwartungen

Organisationen, die Human Oversight implementieren, sollten dokumentieren:

| Evidence-Typ | Beschreibung |
| --- | --- |
| **Prüfungsdatensatz** | Wer hat wann überprüft und welche Entscheidung wurde getroffen |
| **Genehmigungsbegründung** | Warum die Entscheidung getroffen wurde (besonders bei Ausnahmen) |
| **Eskalationsdatensatz** | Wann und warum Probleme an höhere Autorität eskaliert wurden |
| **Behebungsplan** | Geplante Maßnahmen, Verantwortliche und Zeitpläne zur Problembehebung |
| **Abzeichnung** | Formelle Bestätigung, dass die Überprüfung abgeschlossen wurde |

Diese Datensätze sollten im Evidence Bundle gemäß den [Mindestanforderungen an Evidence](../artifacts/minimum-evidence.md) enthalten sein.

## Keine Überbeanspruchung

!!! warning "Wichtig"
    Dieses Protokoll definiert einen **Rahmen zur Dokumentation menschlicher Aufsicht**. Es:

    - Bietet keine Rechtsberatung oder regulatorische Interpretation
    - Garantiert keine Compliance mit Vorschriften oder Standards
    - Ersetzt keine qualifizierte menschliche Beurteilung durch automatisierte Entscheidungen
    - Schreibt keine spezifischen organisatorischen Prozesse vor

    Organisationen müssen diesen Rahmen an ihren spezifischen Kontext, ihr Risikoprofil und ihre regulatorischen Anforderungen anpassen.

## Verwandte Seiten

- [Validator](../standard/current/07-validator.md) — Automatisierte Validierungsregeln und Referenzimplementierung
- [Verantwortungsgrenze](responsibility-boundary.md) — Was AIMO bereitstellt vs. Anwenderverantwortlichkeiten
- [Mindestanforderungen an Evidence](../artifacts/minimum-evidence.md) — MUSS-Evidence-Checkliste
- [Trust Package](trust-package.md) — Prüfungsbereite Materialien-Hub
