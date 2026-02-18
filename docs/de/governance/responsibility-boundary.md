---
description: AIMO Verantwortungsgrenze — Definiert, was die Norm bietet vs. Verantwortung der Anwender. Keine Überbeanspruchung und Umfangsgrenzen.
---
<!-- aimo:translation_status=translated -->

# Verantwortungsgrenze（Responsibility Boundary）

Diese Seite definiert, was der AIMO Standard bietet und nicht bietet, welche Annahmen er trifft und die Verantwortlichkeiten der Anwender.

## Beweis vs. Assurance (Proof vs assurance boundary)

| Grenze | Was AIMO bietet | Wer entscheidet |
| --- | --- | --- |
| **Beweis (Evidenz)** | Evidence-Bundle-Struktur, Validatoren, Schemas, Vorlagen, Coverage-Zuordnungen (informativ). AIMO erstellt **Evidenzpakete** und **Validatoren**, die die Strukturkonformität prüfen. | Der Adoptierende erstellt die Evidenz; AIMO definiert Format und Regeln. |
| **Assurance / Konformität / Zertifizierung** | AIMO **erteilt keine** Zertifizierungen, Prüfungsmeinungen oder Konformitätsentscheidungen. | **Extern:** Kunde, Prüfer oder **akkreditierte Zertifizierungsstelle** entscheiden über Konformität und Zertifizierung. |

Konformität und Anspruchssprache sind in [Konformität](../../conformance/) und dem [ISO-42001-Zertifizierungsbereitschafts-Toolkit](../../artifacts/iso-42001-certification-readiness-toolkit/) vereinheitlicht. AIMO unterstützt **Evidenzbereitschaft** und **Audit-Übergabe**; es zertifiziert nicht und garantiert keine Konformität.

## Was der AIMO Standard bietet

- **Ein strukturiertes Evidenzformat**: Schemas, Vorlagen und Taxonomie für AI-Governance-Evidenz.
- **Rahmen für Nachverfolgbarkeit**: lebenszyklusbasierte Evidenzverknüpfung (Antrag → Prüfung → Ausnahme → Erneuerung).
- **Unterstützung der Erklärbarkeit**: Coverage Map zu externen Rahmenwerken für Audit-Diskussionen.
- **Validierungswerkzeuge**: Referenz-Validator und Regeln für Strukturkonsistenzprüfungen.
- **Dokumentation**: normative Spezifikation, Beispiele und Anleitungen.

## Was der AIMO Standard nicht bietet

| Außerhalb des Umfangs | Erklärung |
| --- | --- |
| **Rechtsberatung** | AIMO interpretiert keine Gesetze oder Vorschriften. Konsultieren Sie qualifizierte Rechtsberatung für regulatorische Konformität. |
| **Konformitätszertifizierung** | Die Nutzung von AIMO zertifiziert nicht die Konformität mit Vorschriften oder Rahmenwerken (ISO 42001, EU AI Act, NIST AI RMF usw.). |
| **„ISO-zertifiziert durch AIMO“** | AIMO erteilt keine Zertifikate. Die Zertifizierung erfolgt durch akkreditierte Zertifizierungsstellen. |
| **„EU AI Act-konform wegen AIMO“** | AIMO strukturiert Evidenz; es garantiert oder zertifiziert keine regulatorische Konformität. |
| **Risikobewertung** | AIMO strukturiert Evidenz, führt aber keine AI-Risikobewertungen durch oder validiert sie. |
| **Technische Kontrollen** | AIMO implementiert keine Zugriffskontrolle, Verschlüsselung oder andere Sicherheitskontrollen; es dokumentiert Erwartungen. |
| **Audit-Durchführung** | AIMO stellt Materialien für Prüfer bereit, führt aber keine Audits durch. |
| **AI-Modellbewertung** | AIMO bewertet nicht Modellleistung, Bias oder Sicherheit. |

## Annahmen

Der AIMO Standard geht davon aus:

1. **Anwender haben Governance-Prozesse**: Antrags-, Prüf-, Genehmigungs- und Ausnahme-Workflows existieren.
2. **Anwender pflegen Evidenz**: Evidenz wird von den Systemen des Anwenders erstellt, gespeichert und aufbewahrt.
3. **Anwender prüfen anhand maßgeblicher Texte**: Bei Nutzung der Coverage Map prüfen Anwender das ursprüngliche Rahmenwerk oder die Vorschrift.
4. **Werkzeuge sind optional**: Der Referenz-Validator ist ein Hilfsmittel; Anwender können eigene Validierung nutzen.

## Verantwortlichkeiten der Anwender

| Verantwortung | Beschreibung |
| --- | --- |
| **Evidenzerstellung** | Genauere, zeitnahe Evidenzaufzeichnungen gemäß EV-Schema erstellen. |
| **Evidenzspeicherung & -aufbewahrung** | Evidenz sicher mit geeigneten Zugriffskontrollen und Aufbewahrungsfristen speichern. |
| **Integrität & Zugriffskontrolle** | Kontrollen (Hashing, WORM, Audit-Logs) zur Wahrung der Evidenzintegrität implementieren. |
| **Rechtliche Prüfung** | Konformitätsbehauptungen anhand maßgeblicher Rechtstexte prüfen und bei Bedarf Rechtsberatung einholen. |
| **Kontinuierliche Ausrichtung** | Evidenz und Zuordnungen bei Änderung von AIMO-Standard-Versionen und externen Rahmenwerken aktualisieren. |
| **Audit-Vorbereitung** | Evidence Bundles packen und Validierung vor Einreichung bei Prüfern ausführen. |

## RACI-Matrix

Die folgende RACI-Matrix klärt Verantwortlichkeiten zwischen AIMO Standard, Anwender und Prüfer.

| Aktivität | AIMO Standard | Anwender | Prüfer |
| --- | :---: | :---: | :---: |
| **Evidenz-Schema & Vorlagen definieren** | R/A | I | I |
| **Evidenzaufzeichnungen erstellen** | — | R/A | I |
| **Evidenz speichern & aufbewahren** | — | R/A | I |
| **Zugriffskontrollen implementieren** | — | R/A | I |
| **Integritätskontrollen (Hash, WORM) implementieren** | — | R/A | I |
| **Validator für Bundle ausführen** | C | R/A | C |
| **Einreichung packen (zip, Prüfsummen)** | C | R/A | I |
| **Prüfsummen (sha256) verifizieren** | — | C | R/A |
| **Bundle-Struktur verifizieren (Validator)** | — | C | R/A |
| **Regulatorische Anforderungen auslegen** | — | R/A | C |
| **Audit-Schlussfolgerung erteilen** | — | — | R/A |
| **Rechtsberatung erteilen** | — | — | — |

**Legende**: R = Verantwortlich, A = Rechenschaftspflichtig, C = Zu konsultieren, I = Zu informieren, — = Nicht anwendbar

!!! note "Kernaussage"
    Der AIMO Standard ist für **die Definition des Formats** verantwortlich. Anwender sind für **Erstellung, Speicherung und Validierung von Evidenz** verantwortlich. Prüfer sind für **Verifizierung von Einreichungen und Erteilung von Audit-Schlussfolgerungen** verantwortlich.

!!! warning "Hinweis zur Nicht-Zertifizierung"
    Der AIMO Standard ist informativ; er zertifiziert keine Konformität und erteilt keine Rechtsberatung. Audit-Schlussfolgerungen und Konformitätsbewertungen liegen in der alleinigen Verantwortung qualifizierter Prüfer und Rechtsberater.

## Aussagenrichtlinie

| Akzeptabel | Inakzeptabel |
| --- | --- |
| „Ein Evidence Bundle wurde gemäß AIMO Standard v0.1.2 erstellt und vom AIMO Validator strukturell validiert.“ | „EU AI Act-konform“, „ISO 42001 zertifiziert“, „staatlich genehmigt“ usw. |
| „Wir nutzen AIMO-Artefakte zur ISO/IEC 42001-Vorbereitung; Zertifizierungsentscheidungen obliegen akkreditierten Zertifizierungsstellen.“ | Behauptung, AIMO zertifiziere Konformität oder erteile Rechtsberatung. |

## Keine Überbeanspruchung

!!! warning "Wichtig"
    Der AIMO Standard unterstützt **Erklärbarkeit und Evidenzbereitschaft**. Er **stellt keine** Rechtsberatung bereit, **garantiert keine** Konformität und **zertifiziert keine** Konformität mit Vorschriften oder Rahmenwerken. Anwender müssen Aussagen anhand maßgeblicher Texte prüfen und bei Bedarf fachliche Beratung einholen.

Diese Aussage gilt für die gesamte AIMO-Standard-Dokumentation, einschließlich Trust Package, Evidence Bundle, Minimum Evidence Requirements, Coverage Map und Releases.

## Verwandte Seiten

- [Trust Package](../trust-package/) — zentrale Stelle für prüferfertige Materialien
- [Human Oversight Protocol](../human-oversight-protocol/) — Grenze maschinelle vs. menschliche Prüfung
- [Minimum Evidence Requirements](../../artifacts/minimum-evidence/) — MUST-Checkliste nach Lebenszyklus
- [Coverage Map Methodology](../../coverage-map/methodology/) — was die Zuordnung ist und nicht ist
