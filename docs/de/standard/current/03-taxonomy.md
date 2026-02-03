---
description: AIMO Taxonomie - 8-Dimensionen-Klassifizierungssystem mit 91 Codes zur Kategorisierung von KI-Systemen. Umfasst funktionalen Scope, Anwendungsfälle, Datentypen, Kanäle, Integration, Risiken, Ergebnisse und Evidence.
---

# Taxonomie

Die AIMO Taxonomie bietet ein strukturiertes Klassifizierungssystem zur Kategorisierung von KI-Systemen, deren Nutzung und zugehörigen Governance-Anforderungen. Sie besteht aus **8 Dimensionen** mit **91 Codes**, die eine konsistente Klassifizierung und Evidence-Verwaltung in Organisationen ermöglichen.

## Zweck

Die Taxonomie dient drei Hauptzwecken aus Audit-Perspektive:

1. **Erklärbarkeit**: Bietet ein gemeinsames Vokabular zur Beschreibung von KI-Anwendungsfällen in der Organisation und unterstützt klare Kommunikation mit Prüfern und Stakeholdern.

2. **Evidence-Bereitschaft**: Ermöglicht systematische Dokumentation von KI-Systemen mit standardisierter Klassifizierung, was Evidence-Sammlung und -Überprüfung effizienter macht.

3. **Vergleichbarkeit**: Ermöglicht es Organisationen, KI-Anwendungsfälle über verschiedene Kontexte hinweg mit konsistenter Terminologie zu vergleichen.

## Was sie nicht ist (Keine Überbeanspruchung)

!!! warning "Wichtig"
    Der AIMO Standard unterstützt **Erklärbarkeit und Evidence-Bereitschaft**. Er bietet **keine** Rechtsberatung, garantiert keine Compliance und zertifiziert keine Konformität mit Vorschriften oder Frameworks. Siehe [Verantwortungsgrenze](../../governance/responsibility-boundary.md) für Details.

Die Taxonomie ist nur ein Klassifizierungssystem. Sie:

- Garantiert keine Compliance mit Gesetzen oder Vorschriften
- Ersetzt keine professionelle Rechts-, Sicherheits- oder Compliance-Beratung
- Zertifiziert keine Konformität mit externen Frameworks (ISO, NIST, EU AI Act, etc.)
- Bietet keine Risikobewertungen oder Kontrollempfehlungen

## Beispiele für KI-/agentenspezifische Risiken (warum ein KI-spezifischer Standard benötigt wird)

Traditionelle Sicherheitskontrollen (z.B. ISMS) allein erfassen oft keine LLM-/agentenspezifischen Fehlermodi und autonomen Agentenabweichungen (z.B. unbeabsichtigte Tool-Ausführung, rekursive Schleifen) auf eine **audit-erklärbare** Weise.
AIMO Taxonomie bietet eine gemeinsame Sprache, um diese KI-spezifischen Risiken zu klassifizieren und sie mit Evidence-Anforderungen und Behebungs-Workflows zu verbinden.

(Referenzbeispiele zur Differenzierung. Die folgenden Codes sind illustrative Platzhalter; das offizielle Code-System folgt den Standard-Definitionen.)
- AG-01 Runaway Loop / Rekursion
- AG-02 Nicht autorisierte Tool-Nutzung (Confused-Deputy-artiger Missbrauch)
- AG-03 Berechtigungsgrenze-Drift

## Dimensionen-Übersicht

AIMO verwendet 8 Dimensionen zur Klassifizierung von KI-Anwendungsfällen. Jede Dimension hat ein eindeutiges 2-Buchstaben-Präfix.

| ID | Name | Code-Anzahl | Beschreibung |
| --- | --- | --- | --- |
| **FS** | Funktionaler Scope | 6 | Welche Geschäftsfunktion wird unterstützt |
| **UC** | Anwendungsfall-Klasse | 30 | Welche Art von Aufgabe wird ausgeführt |
| **DT** | Datentyp | 10 | Welche Datenklassifizierungen sind beteiligt |
| **CH** | Kanal | 8 | Wie Benutzer auf die KI zugreifen |
| **IM** | Integrationsmodus | 7 | Wie KI mit Unternehmenssystemen verbunden ist |
| **RS** | Risikooberfläche | 8 | Welche Risiken sind verbunden |
| **OB** | Ergebnis / Nutzen | 7 | Welcher Nutzen wird erwartet |
| **LG** | Log-/Registrierungstyp | 15 | Welches Log/Registrierung erforderlich ist |

**Gesamt: 91 Codes über 8 Dimensionen**（**EV-** reserviert für Evidence-Artefakt-IDs; Taxonomie-Dimension Log/Registrierung: **LG-**.)

### Nutzungsregeln

| Dimension | Auswahl | Audit-Implikation |
| --- | --- | --- |
| FS, IM | Genau 1 | Primäre Klassifizierung für Verantwortungszuweisung |
| UC, DT, CH, RS, LG | 1 oder mehr | Vollständige Aufzählung für Risikoabdeckung erforderlich |
| OB | 0 oder mehr | Optional; dokumentiert erwarteten Geschäftswert |

## Dimensionsdefinitionen

### FS: Funktionaler Scope

Kategorisiert KI-Nutzung nach der unterstützten Geschäftsfunktion. **Wählen Sie genau eine.**

| Code | Label | Definition |
| --- | --- | --- |
| FS-001 | Endbenutzer-Produktivität | KI zur Verbesserung der Produktivität interner Endbenutzer (Schreiben, Suche, Zusammenfassung, Besprechungsnotizen). |
| FS-002 | Kundenbezogene Funktionen | KI eingebettet in Produkt-/Servicefunktionen für Kunden. |
| FS-003 | Entwickler-Tooling | KI zur Unterstützung von Softwareentwicklung und Engineering-Aufgaben. |
| FS-004 | IT-Betrieb | KI für IT-Betrieb und Systemadministration (Monitoring, Incident-Handling). |
| FS-005 | Sicherheitsbetrieb | KI für Sicherheitsüberwachung/-reaktion (SOC, Erkennung, Triage). |
| FS-006 | Governance & Compliance | KI zur Unterstützung von Governance-/Compliance-Aktivitäten (Policy, Audit-Evidence). |

### UC: Anwendungsfall-Klasse

Kategorisiert KI-Nutzung nach Art der Aufgabe oder Interaktion. **Wählen Sie eine oder mehrere.** Vollständige Liste enthält 30 Codes; repräsentative Beispiele unten.

| Code | Label | Definition |
| --- | --- | --- |
| UC-001 | Allgemeine F&A | Allgemeine Fragebeantwortung und konversationelle Nutzung. |
| UC-002 | Zusammenfassung | Zusammenfassung von Dokumenten, Besprechungen oder Nachrichten. |
| UC-003 | Übersetzung | Übersetzung zwischen Sprachen. |
| UC-004 | Inhaltsentwurf | Generierung von Entwürfen für E-Mails, Dokumente oder Berichte. |
| UC-005 | Code-Generierung | Generierung von Code oder Skripten. |
| UC-006 | Code-Review | Überprüfung von Code auf Probleme und Verbesserungen. |
| UC-009 | Search/RAG | RAG-basiertes Retrieval und Fragebeantwortung. |
| UC-010 | Agentic Automation | Autonome oder semi-autonome Agenten, die Aktionen ausführen. |

Siehe [Dictionary](./05-dictionary.md) für die vollständige Liste von 30 UC-Codes.

### DT: Datentyp

Kategorisiert die Sensitivität und Klassifizierung der beteiligten Daten. **Wählen Sie eine oder mehrere.**

| Code | Label | Definition |
| --- | --- | --- |
| DT-001 | Öffentlich | Daten, die öffentlich verfügbar und zur öffentlichen Offenlegung bestimmt sind. |
| DT-002 | Intern | Nicht-öffentliche interne Geschäftsdaten. |
| DT-003 | Vertraulich | Hochsensitive interne Daten, die eingeschränkten Zugriff erfordern. |
| DT-004 | Personenbezogene Daten | Personenbezogene Daten wie durch anwendbare Datenschutzgesetze definiert. |
| DT-005 | Sensible personenbezogene Daten | Besondere Kategorie/sensible personenbezogene Daten. |
| DT-006 | Anmeldeinformationen | Authentifizierungsgeheimnisse und Anmeldeinformationen. |
| DT-007 | Quellcode | Quellcode und zugehörige Artefakte. |
| DT-008 | Kundendaten | Von Kunden bereitgestellte oder kundenbezogene Daten. |
| DT-009 | Betriebsprotokolle | Betriebs- oder Systemprotokolle für Monitoring und Troubleshooting. |
| DT-010 | Sicherheitstelemetrie | Sicherheitstelemetrie wie Alerts und Erkennungen. |

### CH: Kanal

Kategorisiert, wie Benutzer auf die KI zugreifen oder mit ihr interagieren. **Wählen Sie eine oder mehrere.**

| Code | Label | Definition |
| --- | --- | --- |
| CH-001 | Web-UI | Nutzung über eine Web-Benutzeroberfläche. |
| CH-002 | API | Nutzung über programmatische API-Integration. |
| CH-003 | IDE-Plugin | Nutzung über IDE/Editor-Plugin. |
| CH-004 | ChatOps | Nutzung über Chat-Plattform-Integrationen (Slack/Teams). |
| CH-005 | Desktop-App | Nutzung über native Desktop-Anwendung. |
| CH-006 | Mobile-App | Nutzung über native mobile Anwendung. |
| CH-007 | E-Mail | Nutzung über E-Mail-Schnittstelle oder E-Mail-basierte Automatisierung. |
| CH-008 | Kommandozeile | Nutzung über Kommandozeilen-Schnittstelle. |

### IM: Integrationsmodus

Kategorisiert, wie KI in Unternehmenssysteme integriert ist. **Wählen Sie genau eine.**

| Code | Label | Definition |
| --- | --- | --- |
| IM-001 | Standalone | Standalone-Nutzung ohne Integration in Unternehmenssysteme. |
| IM-002 | SaaS-integriert | SaaS-Anwendung integriert KI-Funktionen. |
| IM-003 | Enterprise-App-eingebettet | KI eingebettet in interne Unternehmensanwendungen. |
| IM-004 | RPA/Workflow | KI aufgerufen innerhalb von Workflow-Automatisierung oder RPA. |
| IM-005 | On-prem / Privat | KI gehostet in privater/On-prem-Umgebung. |
| IM-006 | Managed Service | Nutzung über Managed Service mit Enterprise-Kontrollen. |
| IM-007 | Shadow / Unmanaged | Nutzung außerhalb genehmigter Governance-Kontrollen. |

### RS: Risikooberfläche

Kategorisiert die mit der KI-Nutzung verbundenen Risikotypen. **Wählen Sie eine oder mehrere.**

| Code | Label | Definition |
| --- | --- | --- |
| RS-001 | Datenleck | Risiko unbeabsichtigter Datenoffenlegung. |
| RS-002 | Sicherheitsmissbrauch | Risiko, dass das System für bösartige Zwecke missbraucht wird. |
| RS-003 | Compliance-Verstoß | Risiko der Verletzung von Gesetzen/Vorschriften/Richtlinien. |
| RS-004 | IP-Verletzung | Risiko der Verletzung von Urheberrecht/Patent/Geschäftsgeheimnissen. |
| RS-005 | Modell-Missbrauch | Risiko durch unangemessene Modellnutzung oder Überabhängigkeit. |
| RS-006 | Bias/Fairness | Risiko unfairer oder verzerrter Ergebnisse. |
| RS-007 | Sicherheit | Risiko schädlicher Inhalte oder unsicherer Empfehlungen. |
| RS-008 | Drittanbieter-Risiko | Anbieter-, Subunternehmer- und Modellanbieter-Risiken. |

### OB: Ergebnis / Nutzen

Kategorisiert die erwarteten Ergebnisse oder Vorteile der KI-Nutzung. **Optional; wählen Sie null oder mehr.**

| Code | Label | Definition |
| --- | --- | --- |
| OB-001 | Effizienz | Verbessert Zeit-/Kosteneffizienz. |
| OB-002 | Qualität | Verbessert Qualität/Genauigkeit der Ausgaben. |
| OB-003 | Umsatz | Trägt zum Umsatzwachstum bei. |
| OB-004 | Risikoreduktion | Reduziert Betriebs-/Sicherheits-/Compliance-Risiko. |
| OB-005 | Innovation | Ermöglicht neue Fähigkeiten oder Innovationen. |
| OB-006 | Kundenzufriedenheit | Verbessert Kundenzufriedenheit. |
| OB-007 | Mitarbeitererfahrung | Verbessert Mitarbeitererfahrung. |

### LG: Log-/Registrierungstyp

Kategorisiert die erforderlichen oder gesammelten Log-/Registrierungstypen. **Wählen Sie eine oder mehrere.**（EV- reserviert für Evidence-Artefakt-IDs.)

| Code | Label | Definition |
| --- | --- | --- |
| LG-001 | Antragsdatensatz | Evidence, dass eine KI-Nutzung/ein Service beantragt und beschrieben wurde. |
| LG-002 | Prüfungs-/Genehmigungsdatensatz | Evidence, dass eine Prüfung/Genehmigung durchgeführt wurde. |
| LG-003 | Ausnahmedatensatz | Evidence, dass eine Ausnahme gewährt und verfolgt wurde. |
| LG-004 | Verlängerungs-/Neubewertungsdatensatz | Evidence, dass Verlängerung oder Neubewertung erfolgte. |
| LG-005 | Änderungsprotokolleintrag | Evidence von Änderungen und deren Genehmigungen. |
| LG-006 | Integritätsnachweis | Evidence der Integrität (Hash, Signatur, WORM). |
| LG-007 | Zugriffsprotokoll | Evidence von Zugriffskontrolle und Zugriffshistorie. |
| LG-008 | Modell-/Service-Inventar | Inventardatensatz der verwendeten Modelle/Services. |
| LG-009 | Risikobewertung | Dokumentierte Risikobewertung für die Nutzung/den Service. |
| LG-010 | Kontrollzuordnung | Kontrollzuordnungs-Evidence zu externen Frameworks. |
| LG-011 | Schulung/Anleitung | Evidence von Schulung oder Anleitung für Benutzer. |
| LG-012 | Monitoring-Evidence | Evidence von Monitoring und laufender Aufsicht. |
| LG-013 | Incident-Datensatz | Evidence von Incident-Handling im Zusammenhang mit KI-Nutzung. |
| LG-014 | Drittanbieter-Bewertung | Evidence von Anbieter- oder Drittanbieter-Bewertung. |
| LG-015 | Attestierung/Abzeichnung | Formelle Attestierung oder Abzeichnungsdatensatz. |

## Verwendung

### Beziehung zu Evidence

Jedes Evidence-Dokument referenziert Codes aus mehreren Dimensionen, um das dokumentierte KI-System oder den Anwendungsfall zu klassifizieren. Die 8-Dimensionen-Klassifizierung ermöglicht:

- **Konsistente Kategorisierung** in der gesamten Organisation
- **Risikobasierte Filterung** nach Dimensionswerten
- **Framework-Zuordnung** über Coverage Map

### Referenzierung des Dictionary

Für vollständige Code-Definitionen einschließlich Geltungsbereich-Hinweisen und Beispielen siehe [Dictionary](./05-dictionary.md).

### Beispielklassifizierung

```
FS: FS-001 (Endbenutzer-Produktivität)
UC: UC-001 (Allgemeine F&A), UC-002 (Zusammenfassung)
DT: DT-002 (Intern), DT-004 (Personenbezogene Daten)
CH: CH-001 (Web-UI)
IM: IM-002 (SaaS-integriert)
RS: RS-001 (Datenleck), RS-003 (Compliance-Verstoß)
OB: OB-001 (Effizienz)
LG: LG-001 (Antragsdatensatz), LG-002 (Prüfungs-/Genehmigungsdatensatz)
```

## SSOT-Referenz

!!! info "Quelle der Wahrheit"
    Die maßgebliche Definition ist `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv`. Diese Seite ist erklärend. Siehe [Lokalisierungsleitfaden](../../contributing/localization.md) für Update-Workflows.

## Verwandte Seiten

- [Codes](./04-codes.md) - Code-Format, Namenskonventionen und Lifecycle
- [Dictionary](./05-dictionary.md) - Vollständige Code-Listen und Spaltendefinitionen
- [Evidence-Templates](./06-ev-template.md) - Wie Codes in Evidence verwendet werden
- [Verantwortungsgrenze](../../governance/responsibility-boundary.md) - Keine-Überbeanspruchung-Erklärung
