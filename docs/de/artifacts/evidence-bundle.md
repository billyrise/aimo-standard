---
description: AIMO Evidence Bundle-Struktur. Auditpaketformat mit Inhaltsverzeichnis, Nachverfolgbarkeit und Artefakten für KI-Governance-Compliance und Prüferbereitstellung.
---

# Evidence Bundle

Ein **Evidence Bundle** ist ein Auditpaket: eine strukturierte Sammlung von Artefakten, die Erklärbarkeit und Nachverfolgbarkeit für KI-Governance unterstützt. Es ist keine Produktfunktion, sondern ein Lieferformat für Prüfer und Compliance.

## Bundle-Struktur und Benennung

- **Bundle-Stammbenennung**: Verwenden Sie ein konsistentes Muster wie `{org}_{system}_{zeitraum}_{version}` (z.B. `acme_ai-usage_2026-Q1_v1`).
- **Erforderliche Dateien**: mindestens ein Evidence (EV)-Satz, der am [EV-Template](../standard/current/06-ev-template.md) ausgerichtet ist, ein [Dictionary](../standard/current/05-dictionary.md), eine kurze **Zusammenfassung** (Executive Summary des Bundles) und ein **Änderungsprotokoll** (oder Verweis darauf) für Änderungen am Bundle oder dessen Inhalten.
- **Optionale Anhänge**: Protokolle, Prüfaufzeichnungen, Ausnahmegenehmigungen, Verlängerungsaufzeichnungen; halten Sie die Benennung konsistent und referenzierbar vom Haupt-EV/Dictionary.

## Inhaltsverzeichnis (TOC)

| Abschnitt | Artefakt | Erforderlich? | Zweck | Mindestfelder | Validierung |
| --- | --- | --- | --- | --- | --- |
| Evidence | EV-Datensätze (JSON/Array) | Ja | Aufzeichnung des Geschehens; Verknüpfung zu Antrag/Prüfung/Ausnahme/Verlängerung | id, timestamp, source, summary; optionale Lifecycle-Referenzen | [Validator](../validator/index.md), aimo-ev.schema.json |
| Dictionary | dictionary.json | Ja | Schlüssel/Labels/Beschreibungen für Codes und Dimensionen | entries (key, label, description) | aimo-dictionary.schema.json |
| Zusammenfassung | summary (Dokument oder Feld) | Ja | Einseitige Übersicht für Prüfer | Umfang, Zeitraum, Schlüsselentscheidungen, Ausnahmen | — |
| Änderungsprotokoll | change_log oder Verweis | Ja | Audit-Trail für Bundle-/Inhaltsänderungen | id, timestamp, actor, Änderungsbeschreibung, Referenzen | — |
| Antrag | Antragsdatensatz/-sätze | Falls zutreffend | Anwendung/Antrag zur Nutzung | id, timestamp, actor/role, Umfang, Begründung | — |
| Prüfung/Genehmigung | Prüfdatensatz/-sätze | Falls zutreffend | Prüfungs- und Genehmigungsergebnis | id, timestamp, actor/role, Entscheidung, Referenzen | — |
| Ausnahme | Ausnahmedatensatz/-sätze | Falls zutreffend | Ausnahme mit kompensierenden Kontrollen und Ablauf | id, timestamp, Umfang, Ablauf, kompensierende Kontrollen, Verlängerungsreferenz | — |
| Verlängerung | Verlängerungsdatensatz/-sätze | Falls zutreffend | Neubewertung und Verlängerung | id, timestamp, actor/role, Entscheidung, Referenzen zu vorheriger Ausnahme/EV | — |

## Nachverfolgbarkeit

- **Stabile IDs**: Jeder Datensatz (EV, Antrag, Prüfung, Ausnahme, Verlängerung, Änderungsprotokoll-Eintrag) MUSS einen stabilen, eindeutigen Identifikator haben.
- **Querverweise**: Verknüpfen Sie Antrag → Prüfung → Ausnahme (falls vorhanden) → Verlängerung und verknüpfen Sie EV-Elemente mit diesen über Referenzfelder (z.B. `request_id`, `review_id`, `exception_id`, `renewal_id`).
- **Verknüpfung**: Stellen Sie sicher, dass Prüfer eine Kette von einer KI-Nutzung (oder Ausnahme) zum Antrag, zur Genehmigung, zu jeder Ausnahme und deren kompensierenden Kontrollen und Ablauf sowie zur Verlängerung nachvollziehen können.

## Wie Prüfer dies nutzen

Prüfer nutzen das Evidence Bundle, um zu überprüfen, dass KI-Nutzung beantragt, geprüft und genehmigt wird; dass Ausnahmen zeitlich begrenzt sind und kompensierende Kontrollen sowie Verlängerungen haben; und dass Änderungen protokolliert werden. Das Inhaltsverzeichnis und die Nachverfolgbarkeitsregeln ermöglichen es ihnen, erforderliche Artefakte zu lokalisieren und IDs und Referenzen über Antrag, Prüfung, Ausnahme, Verlängerung und EV-Datensätze zu verfolgen. Die Zusammenfassung gibt einen schnellen Überblick; das Änderungsprotokoll unterstützt Änderungskontrolle und Rechenschaftspflicht.

Siehe [Mindestanforderungen an Evidence](minimum-evidence.md) für MUSS-Felder und Lifecycle-Gruppen.

## Betriebsanleitung

!!! info "Integrität und Zugriffskontrolle"
    Obwohl AIMO keine spezifischen Kontrollen vorschreibt, sollten Anwender dokumentieren:
    
    - **Zugriffsrollen**: Wer kann Evidence erstellen, lesen, aktualisieren oder löschen
    - **Aufbewahrungsrichtlinie**: Wie lange Evidence aufbewahrt wird und nach welchem Zeitplan
    - **Integritätsmechanismen**: Verwendete Hashing-, WORM-Speicher- oder digitale Signatur-Verfahren
    - **Audit-Trail**: Protokolle über Zugriff und Änderungen am Bundle
    
    Siehe [Mindestanforderungen an Evidence > Integrität & Zugriff](minimum-evidence.md#6-integrity-access) für detaillierte Anleitung.

## Audit-Reise

Von dieser Seite aus setzt sich die typische Audit-Reise fort:

1. **Weiter**: [Mindestanforderungen an Evidence](minimum-evidence.md) — MUSS-Checkliste nach Lifecycle
2. **Dann**: [Coverage Map](../coverage-map/index.md) — Zuordnung zu externen Frameworks
3. **Validieren**: [Validator](../validator/index.md) — Strukturprüfungen durchführen
4. **Download**: [Releases](../releases/index.md) — Release-Assets herunterladen und Prüfsummen verifizieren
