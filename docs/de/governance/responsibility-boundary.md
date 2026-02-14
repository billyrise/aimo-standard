---
description: AIMO Verantwortungsgrenze - Definiert, was der Standard bereitstellt vs. Anwenderverantwortlichkeiten. Keine-Überbeanspruchung-Erklärung und Umfangsbeschränkungen.
---

# Verantwortungsgrenze

Diese Seite definiert, was der AIMO Standard bereitstellt und nicht bereitstellt, welche Annahmen er macht und welche Verantwortlichkeiten die Anwender haben.

## Was der AIMO Standard bereitstellt

- **Ein strukturiertes Evidence-Format**: Schemas, Templates und Taxonomie für KI-Governance-Evidence.
- **Nachverfolgbarkeitsrahmen**: Lifecycle-basierte Evidence-Verknüpfung (request → review → exception → renewal).
- **Erklärbarkeitsunterstützung**: Coverage Mapping zu externen Frameworks für Audit-Diskussionen.
- **Validierungstools**: Referenz-Validator und Regeln für strukturelle Konsistenzprüfungen.
- **Dokumentation**: Normative Spezifikation, Beispiele und Anleitungen.

## Was der AIMO Standard NICHT bereitstellt

| Außerhalb des Umfangs | Erklärung |
| --- | --- |
| **Rechtsberatung** | AIMO interpretiert keine Gesetze oder Vorschriften. Konsultieren Sie qualifizierte Rechtsberater für regulatorische Compliance. |
| **Compliance-Zertifizierung** | Die Verwendung von AIMO zertifiziert keine Compliance mit Vorschriften oder Frameworks (ISO 42001, EU AI Act, NIST AI RMF, etc.). |
| **Risikobewertung** | AIMO strukturiert Evidence, führt aber keine KI-Risikobewertungen durch oder validiert sie. |
| **Technische Kontrollen** | AIMO implementiert keine Zugriffskontrolle, Verschlüsselung oder andere Sicherheitskontrollen; es dokumentiert Erwartungen. |
| **Audit-Durchführung** | AIMO stellt Materialien für Prüfer bereit, führt aber keine Audits durch. |
| **KI-Modell-Evaluation** | AIMO bewertet keine Modellleistung, Verzerrung oder Sicherheit. |

## Annahmen

Der AIMO Standard nimmt an:

1. **Anwender haben Governance-Prozesse**: Antrags-, Prüfungs-, Genehmigungs- und Ausnahme-Workflows existieren.
2. **Anwender pflegen Evidence**: Evidence wird von den Systemen des Anwenders erstellt, gespeichert und aufbewahrt.
3. **Anwender verifizieren gegen maßgebliche Texte**: Bei Verwendung der Coverage Map prüfen Anwender das Original-Framework oder die Vorschrift.
4. **Tooling ist optional**: Der Referenz-Validator ist eine Hilfe; Anwender können ihre eigene Validierung verwenden.

## Anwenderverantwortlichkeiten

| Verantwortlichkeit | Beschreibung |
| --- | --- |
| **Evidence-Erstellung** | Genaue, zeitnahe Evidence-Datensätze erstellen, die am EV-Schema ausgerichtet sind. |
| **Evidence-Speicherung & -Aufbewahrung** | Evidence sicher mit entsprechenden Zugriffskontrollen und Aufbewahrungsfristen speichern. |
| **Integrität & Zugriffskontrolle** | Kontrollen (Hashing, WORM, Audit-Logs) implementieren, um Evidence-Integrität zu bewahren. |
| **Rechtliche Verifizierung** | Compliance-Ansprüche gegen maßgebliche Rechtstexte verifizieren und bei Bedarf Rechtsberatung einholen. |
| **Kontinuierliche Ausrichtung** | Evidence und Zuordnungen aktualisieren, wenn sich AIMO Standard-Versionen und externe Frameworks weiterentwickeln. |
| **Audit-Vorbereitung** | Evidence Bundles verpacken und Validierung vor Einreichung an Prüfer ausführen. |

## RACI-Matrix

Die folgende RACI-Matrix klärt die Verantwortlichkeiten zwischen AIMO Standard, Anwender und Prüfer.

| Aktivität | AIMO Standard | Anwender | Prüfer |
| --- | :---: | :---: | :---: |
| **Evidence-Schema & -Templates definieren** | R/A | I | I |
| **Evidence-Datensätze erstellen** | — | R/A | I |
| **Evidence speichern & aufbewahren** | — | R/A | I |
| **Zugriffskontrollen implementieren** | — | R/A | I |
| **Integritätskontrollen implementieren (Hash, WORM)** | — | R/A | I |
| **Validator auf Bundle ausführen** | C | R/A | C |
| **Einreichungspaket erstellen (zip, Prüfsummen)** | C | R/A | I |
| **Prüfsummen verifizieren (sha256)** | — | C | R/A |
| **Bundle-Struktur verifizieren (Validator)** | — | C | R/A |
| **Regulatorische Anforderungen interpretieren** | — | R/A | C |
| **Audit-Schlussfolgerung ausstellen** | — | — | R/A |
| **Rechtsberatung bereitstellen** | — | — | — |

**Legende**: R = Verantwortlich, A = Rechenschaftspflichtig, C = Konsultiert, I = Informiert, — = Nicht zutreffend

!!! note "Kernaussage"
    Der AIMO Standard ist verantwortlich für die **Definition des Formats**. Anwender sind verantwortlich für die **Erstellung, Speicherung und Validierung von Evidence**. Prüfer sind verantwortlich für die **Verifizierung von Einreichungen und das Ausstellen von Audit-Schlussfolgerungen**.

!!! warning "Keine-Zertifizierung-Hinweis"
    Der AIMO Standard ist informativ; er zertifiziert keine Compliance und bietet keine Rechtsberatung. Audit-Schlussfolgerungen und Konformitätsbewertungen liegen in der alleinigen Verantwortung qualifizierter Prüfer und Rechtsexperten.

## Keine-Überbeanspruchung-Erklärung

!!! warning "Wichtig"
    Der AIMO Standard unterstützt **Erklärbarkeit und Evidence-Bereitschaft**. Er bietet **keine** Rechtsberatung, garantiert keine Compliance und zertifiziert keine Konformität mit Vorschriften oder Frameworks. Anwender müssen Ansprüche gegen maßgebliche Texte verifizieren und bei Bedarf professionelle Beratung einholen.

Diese Erklärung gilt für alle AIMO Standard-Dokumentation, einschließlich Trust Package, Evidence Bundle, Mindestanforderungen an Evidence, Coverage Map und Releases.

## Verwandte Seiten

- [Trust Package](../trust-package/) — Prüfungsbereite Materialien-Hub
- [Human Oversight Protocol](../human-oversight-protocol/) — Grenze zwischen maschineller und menschlicher Überprüfung
- [Mindestanforderungen an Evidence](../../artifacts/minimum-evidence/) — MUSS-Lifecycle-Checkliste
- [Coverage Map Methodologie](../../coverage-map/methodology/) — Was die Zuordnung ist und nicht ist
