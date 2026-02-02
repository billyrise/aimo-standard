---
description: AIMO Mindestanforderungen an Evidence. MUSS-Checkliste nach Lifecycle (Antrag, Prüfung, Genehmigung, Änderung, Verlängerung) für die KI-Governance-Evidence-Bereitschaft.
---

# Mindestanforderungen an Evidence

Diese Seite definiert die Mindestanforderungen an Evidence als MUSS-Checkliste, gruppiert nach Lifecycle. Sie unterstützt Erklärbarkeit und Evidence-Bereitschaft; sie bietet keine Rechtsberatung und garantiert keine Compliance.

## 1) Antrag

- **MUSS-Felder**: Identifikator, Zeitstempel, Akteur/Rolle, Umfang (was beantragt wird), Begründung (warum).
- **MUSS-Verknüpfungen**: Antrags-ID wird von Prüfung und von EV-Elementen referenziert, die die Nutzung aufzeichnen.
- **Was es beweist**: dass die Nutzung vor Genehmigung und Nutzung beantragt und eingegrenzt wurde.

## 2) Prüfung / Genehmigung

- **MUSS-Felder**: Identifikator, Zeitstempel, Akteur/Rolle, Entscheidung (genehmigt/abgelehnt/bedingt), Umfang, Begründung, Verweis auf Antrag.
- **MUSS-Verknüpfungen**: Prüfungs-ID wird von EV und von jeder folgenden Ausnahme oder Verlängerung referenziert.
- **Was es beweist**: dass eine definierte Prüfung und Genehmigung vor der Nutzung (oder Ausnahme) erfolgte.

## 3) Ausnahme

- **MUSS-Felder**: Identifikator, Zeitstempel, Umfang, Ablauf (oder Frist), kompensierende Kontrollen, Begründung, Verweis auf Prüfung/Antrag.
- **MUSS-Verknüpfungen**: Ausnahme → kompensierende Kontrollen; Ausnahme → Ablauf; Ausnahme → Verlängerung (wenn Neubewertung fällig ist).
- **Was es beweist**: dass Abweichungen zeitlich begrenzt sind, kompensierende Kontrollen haben und mit Verlängerung verknüpft sind.

## 4) Verlängerung / Neubewertung

- **MUSS-Felder**: Identifikator, Zeitstempel, Akteur/Rolle, Entscheidung (verlängert/widerrufen/bedingt), Verweise auf vorherige Ausnahme/Antrag/Prüfung/EV.
- **MUSS-Verknüpfungen**: Verlängerung referenziert die Ausnahme oder Genehmigung, die verlängert wird; EV-Elemente können Verlängerungs-ID referenzieren.
- **Was es beweist**: dass Ausnahmen und Genehmigungen auf definierter Basis neu bewertet und verlängert oder widerrufen werden.

## 5) Änderungsprotokoll

- **MUSS-Felder**: Identifikator, Zeitstempel, Akteur/Rolle, Änderungsbeschreibung, Referenzen (z.B. zu betroffenen EV, Antrag, Prüfung, Ausnahme, Verlängerung).
- **MUSS-Verknüpfungen**: Änderungsprotokoll-Einträge referenzieren die Artefakte, die sie modifizieren oder die die Änderung auslösen.
- **Was es beweist**: dass Änderungen am Bundle oder dessen Inhalten aufgezeichnet und nachverfolgbar sind.

## 6) Integrität & Zugriff

Evidence-Integrität und Zugriffskontrolle sind essentiell für die Audit-Vertrauenswürdigkeit. Obwohl AIMO keine spezifischen technischen Kontrollen vorschreibt, sollten Anwender dokumentieren, wie diese Erwartungen erfüllt werden.

### Anleitung zur Zugriffskontrolle

| Aspekt | Anleitung |
| --- | --- |
| **Rollenbasierter Zugriff** | Definieren Sie Rollen (z.B. Evidence-Ersteller, Prüfer, Auditor, Admin) und dokumentieren Sie, wer Evidence erstellen, lesen, aktualisieren oder löschen kann. |
| **Minimale Berechtigung** | Gewähren Sie minimalen notwendigen Zugriff; beschränken Sie Schreibzugriff auf autorisiertes Personal. |
| **Zugriffsprotokollierung** | Protokollieren Sie Zugriffsereignisse (wer, wann, was) für Audit-Trail-Zwecke. |
| **Funktionstrennung** | Trennen Sie, wo praktikabel, Evidence-Erstellung von Genehmigungsrollen. |

### Anleitung zur Aufbewahrung

| Aspekt | Anleitung |
| --- | --- |
| **Aufbewahrungsfrist** | Definieren und dokumentieren Sie Aufbewahrungsfristen basierend auf regulatorischen Anforderungen und Organisationsrichtlinien (z.B. 5-7 Jahre für Finanzaudits). |
| **Aufbewahrungsplan** | Führen Sie einen Plan, der zeigt, welches Evidence aufbewahrt wird, wie lange und wann es entsorgt werden kann. |
| **Legal Hold** | Unterstützen Sie Legal-Hold-Prozesse, die normale Aufbewahrung/Löschung für Rechtsstreitigkeiten oder Untersuchungen aussetzen. |

### Unveränderlichkeitsoptionen

| Option | Beschreibung |
| --- | --- |
| **Kryptographisches Hashing** | Generieren Sie SHA-256 (oder stärkere) Hashes für Evidence-Dateien; speichern Sie Hashes separat zur Verifizierung. |
| **WORM-Speicher** | Verwenden Sie Write-Once-Read-Many-Speicher für Evidence-Archive, um Modifikation zu verhindern. |
| **Append-Only-Logs** | Verwenden Sie Append-Only-Audit-Logs für Änderungsverfolgung. |
| **Digitale Signaturen** | Signieren Sie Evidence Bundles, um Urheberschaft nachzuweisen und Manipulation zu erkennen. |

### Erwartungen an den Audit-Trail

| Element | Was zu dokumentieren ist |
| --- | --- |
| **Änderungsprotokoll** | Aufzeichnen, wer was wann und warum geändert hat (siehe Änderungsprotokoll-Lifecycle-Gruppe). |
| **Zugriffsprotokoll** | Aufzeichnen, wer wann und zu welchem Zweck auf Evidence zugegriffen hat. |
| **Systemprotokolle** | Relevante Systemprotokolle aufbewahren (Authentifizierung, Autorisierung), die Evidence-Integritätsaussagen unterstützen. |
| **Verifizierungsaufzeichnungen** | Periodische Integritätsverifizierung dokumentieren (Hash-Prüfungen, Audit-Reviews). |

### Was es beweist

- **Evidence wird aufbewahrt**: Integritätsmechanismen (Hashing, WORM, Signaturen) zeigen, dass Evidence nicht manipuliert wurde.
- **Zugriff wird kontrolliert**: Zugriffsprotokolle und Rollendefinitionen zeigen, wer Zugriff hatte und dass minimale Berechtigung angewendet wurde.
- **Audit-Vertrauenswürdigkeit wird unterstützt**: Zusammen geben diese Elemente Prüfern Vertrauen in die Zuverlässigkeit des Evidence.

### Empfohlene Betriebsprofile

Wählen Sie ein Profil basierend auf Ihrer Risikotoleranz und regulatorischen Anforderungen. Dies sind Empfehlungen, keine Vorschriften.

| Aspekt | Leichtgewichtig | Standard | Streng |
| --- | --- | --- | --- |
| **Anwendungsfall** | Interne Piloten, risikoarme KI | Produktionssysteme, moderates Risiko | Regulierte Branchen, hochriskante KI |
| **Aufbewahrungsfrist** | 1-2 Jahre | 5-7 Jahre | 7-10+ Jahre oder regulatorisches Minimum |
| **Unveränderlichkeit** | SHA-256-Hashes | SHA-256 + Append-Only-Logs | WORM-Speicher + digitale Signaturen |
| **Zugriffskontrolle** | Rollenbasiert (einfach) | Rollenbasiert + Zugriffsprotokollierung | Funktionstrennung + vollständiger Audit-Trail |
| **Audit-Trail** | Nur Änderungsprotokoll | Änderungsprotokoll + Zugriffsprotokoll | Vollständige Systemprotokolle + periodische Verifizierung |
| **Verifizierungshäufigkeit** | Bei Bedarf | Vierteljährlich | Monatlich oder kontinuierlich |
| **Validator-Nutzung** | Optional | Erforderlich vor Einreichung | Erforderlich + automatisierte CI-Prüfungen |

!!! note "Aufbewahrungsfristen sind Beispiele"
    Die gezeigten Aufbewahrungsfristen sind illustrativ. Organisationen müssen die Aufbewahrung basierend auf geltenden Gesetzen, Verträgen, Branchenanforderungen und internen Richtlinien bestimmen.

!!! tip "Wie Sie wählen"
    - **Leichtgewichtig**: Geeignet für Experimente, interne Tools oder Anwendungen mit geringem Risiko, bei denen formelle Audits unwahrscheinlich sind.
    - **Standard**: Empfohlen für die meisten Produktionsbereitstellungen, bei denen Audits auftreten können, aber nicht kontinuierlich sind.
    - **Streng**: Erforderlich für regulierte Branchen (Finanzen, Gesundheitswesen, Behörden) oder KI-Systeme mit signifikanter Risikoauswirkung.

## Wichtiger Hinweis

Diese Mindestanforderungen unterstützen Erklärbarkeit und Evidence-Bereitschaft; sie bieten selbst keine Rechtsberatung und garantieren keine Compliance.

Siehe [Evidence Bundle](evidence-bundle.md) für Bundle-Struktur und TOC; siehe [EV-Template](../standard/current/06-ev-template.md) und Schemas für Feldebenen-Ausrichtung.

Siehe auch: [Log Schemas](log-schemas/index.md) — normalisierte Log-Formate für Shadow AI-Erkennung und Agentenaktivitäts-Evidence.
