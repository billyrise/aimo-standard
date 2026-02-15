---
description: AIMO Mindestanforderungen an Evidence. MUST-Checkliste nach Lebenszyklus (Antrag, Prüfung, Genehmigung, Änderung, Verlängerung) für die Evidence-Bereitschaft in der KI-Governance.
---
<!-- aimo:translation_status=translated -->

# Mindestanforderungen an Evidence (Minimum Evidence Requirements)

Diese Seite ist die **Mindestanforderungen an Evidence**-Checkliste für Prüfer und Implementierer. Sie definiert die Mindestanforderungen als MUST-Checkliste, gruppiert nach Lebenszyklus. Sie unterstützt Erklärbarkeit und Evidence-Bereitschaft; sie bietet keine Rechtsberatung und garantiert keine Compliance.

Nutzen Sie diese Seite zusammen mit [Evidence Bundle](../evidence-bundle/) und dem [Validator](../../standard/current/07-validator/) bei der Vorbereitung oder Prüfung von Einreichungen.

## 1) Antrag (Request)

- **MUST-Felder**: Bezeichner, Zeitstempel, Akteur/Rolle, Umfang (was beantragt wird), Begründung (rationale).
- **MUST-Verknüpfungen**: Antrags-ID wird von der Prüfung und von EV-Einträgen, die die Nutzung erfassen, referenziert.
- **Was es belegt**: dass die Nutzung vor Genehmigung und Einsatz beantragt und abgegrenzt wurde.

## 2) Prüfung / Genehmigung (Review / Approval)

- **MUST-Felder**: Bezeichner, Zeitstempel, Akteur/Rolle, Entscheidung (genehmigt/abgelehnt/bedingt), Umfang, Begründung, Referenz auf Antrag.
- **MUST-Verknüpfungen**: Prüfungs-ID wird von EV und von nachfolgenden Ausnahmen oder Verlängerungen referenziert.
- **Was es belegt**: dass vor Nutzung (oder Ausnahme) eine definierte Prüfung und Genehmigung erfolgte.

## 3) Ausnahme (Exception)

- **MUST-Felder**: Bezeichner, Zeitstempel, Umfang, Ablauf (oder Frist), kompensierende Kontrollen, Begründung, Referenz auf Prüfung/Antrag.
- **MUST-Verknüpfungen**: Ausnahme → kompensierende Kontrollen; Ausnahme → Ablauf; Ausnahme → Verlängerung (bei fälliger Neubewertung).
- **Was es belegt**: dass Abweichungen befristet sind, kompensierende Kontrollen haben und mit Verlängerung verknüpft sind.

## 4) Verlängerung / Neubewertung (Renewal / Re-evaluation)

- **MUST-Felder**: Bezeichner, Zeitstempel, Akteur/Rolle, Entscheidung (verlängert/widerrufen/bedingt), Referenzen auf vorherige Ausnahme/Antrag/Prüfung/EV.
- **MUST-Verknüpfungen**: Verlängerung referenziert die verlängerte Ausnahme oder Genehmigung; EV-Einträge können Verlängerungs-ID referenzieren.
- **Was es belegt**: dass Ausnahmen und Genehmigungen nach definierten Kriterien neu bewertet und verlängert oder widerrufen werden.

## 5) Änderungsprotokoll (Change Log)

- **MUST-Felder**: Bezeichner, Zeitstempel, Akteur/Rolle, Änderungsbeschreibung, Referenzen (z. B. auf betroffene EV, Antrag, Prüfung, Ausnahme, Verlängerung).
- **MUST-Verknüpfungen**: Änderungsprotokolleinträge referenzieren die geänderten oder auslösenden Artefakte.
- **Was es belegt**: dass Änderungen am Bundle oder dessen Inhalten erfasst und nachverfolgbar sind.

## 6) Integrität & Zugriff (Integrity & Access)

Evidence-Integrität und Zugriffskontrolle sind für die Prüfungsvertrauenswürdigkeit wesentlich. AIMO schreibt keine konkreten technischen Kontrollen vor; Adoptierer sollen dokumentieren, wie diese Erwartungen erfüllt werden.

### Zugriffskontroll-Leitfaden

| Aspekt | Leitfaden |
| --- | --- |
| **Rollenbasierter Zugriff** | Rollen definieren (z. B. Evidence-Ersteller, Prüfer, Auditor, Admin) und dokumentieren, wer Evidence erstellen, lesen, aktualisieren oder löschen darf. |
| **Mindestberechtigung** | Nur den notwendigen Mindestzugriff gewähren; Schreibzugriff auf autorisiertes Personal beschränken. |
| **Zugriffsprotokollierung** | Zugriffsereignisse (wer, wann, was) für die Prüfungsnachverfolgung protokollieren. |
| **Funktionentrennung** | Wo praktikabel, Evidence-Erstellung von Genehmigungsrollen trennen. |

### Aufbewahrungs-Leitfaden

| Aspekt | Leitfaden |
| --- | --- |
| **Aufbewahrungsfrist** | Aufbewahrungsfristen anhand regulatorischer Anforderungen und Organisationsrichtlinie definieren und dokumentieren (z. B. 5–7 Jahre für Finanzprüfungen). |
| **Aufbewahrungsplan** | Einen Plan führen, der zeigt, welche Evidence wie lange aufbewahrt wird und wann sie vernichtet werden kann. |
| **Legal Hold** | Prozesse für Legal Hold unterstützen, die normale Aufbewahrung/Löschung bei Rechtsstreit oder Untersuchung aussetzen. |

### Unveränderbarkeits-Optionen

| Option | Beschreibung |
| --- | --- |
| **Kryptografische Hashbildung** | SHA-256- (oder stärkere) Hashes für Evidence-Dateien erzeugen; Hashes getrennt zur Verifikation speichern. |
| **WORM-Speicher** | Write-Once-Read-Many-Speicher für Evidence-Archive zur Änderungsverhinderung nutzen. |
| **Nur-Anhängen-Protokolle** | Nur-Anhängen-Audit-Protokolle für Änderungsverfolgung nutzen. |
| **Digitale Signaturen** | Evidence-Bundles signieren, um Urheberschaft zu belegen und Manipulation zu erkennen. |

### Erwartungen an die Prüfungsnachverfolgung

| Element | Was dokumentieren |
| --- | --- |
| **Änderungsprotokoll** | Wer was wann und warum geändert hat (siehe Change-Log-Lebenszyklusgruppe). |
| **Zugriffsprotokoll** | Wer wann zu welchem Zweck auf Evidence zugegriffen hat. |
| **Systemprotokolle** | Relevante Systemprotokolle (Authentifizierung, Autorisierung) aufbewahren, die Evidence-Integritätsaussagen stützen. |
| **Verifikationsaufzeichnungen** | Periodische Integritätsverifikation (Hash-Prüfungen, Prüfungsreviews) dokumentieren. |

### Was es belegt

- **Evidence ist bewahrt**: Integritätsmechanismen (Hashing, WORM, Signaturen) zeigen, dass Evidence nicht verändert wurde.
- **Zugriff ist kontrolliert**: Zugriffsprotokolle und Rollendefinitionen zeigen, wer Zugang hatte und dass Mindestberechtigung angewendet wurde.
- **Prüfungsvertrauen wird gestützt**: Gemeinsam geben diese Elemente Prüfern Vertrauen in die Zuverlässigkeit der Evidence.

### Empfohlene Betriebsprofile

Wählen Sie ein Profil nach Risikotoleranz und regulatorischen Anforderungen. Es sind Empfehlungen, keine Vorgaben.

| Aspekt | Leicht | Standard | Streng |
| --- | --- | --- | --- |
| **Anwendungsfall** | Interne Piloten, geringes KI-Risiko | Produktionssysteme, mäßiges Risiko | Regulierte Branchen, hohes KI-Risiko |
| **Aufbewahrungsfrist** | 1–2 Jahre | 5–7 Jahre | 7–10+ Jahre oder regulatorisches Minimum |
| **Unveränderbarkeit** | SHA-256-Hashes | SHA-256 + Nur-Anhängen-Protokolle | WORM-Speicher + digitale Signaturen |
| **Zugriffskontrolle** | Rollenbasiert (Basis) | Rollenbasiert + Zugriffsprotokollierung | Funktionentrennung + vollständige Prüfungsnachverfolgung |
| **Prüfungsnachverfolgung** | Nur Änderungsprotokoll | Änderungsprotokoll + Zugriffsprotokoll | Vollständige Systemprotokolle + periodische Verifikation |
| **Verifikationshäufigkeit** | Bei Bedarf | Vierteljährlich | Monatlich oder kontinuierlich |
| **Validator-Nutzung** | Optional | Vor Einreichung erforderlich | Erforderlich + automatisierte CI-Checks |

!!! note "Aufbewahrungsfristen sind Beispiele"
    Die angegebenen Aufbewahrungsfristen sind veranschaulichend. Organisationen müssen die Aufbewahrung anhand geltender Gesetze, Verträge, Branchenanforderungen und interner Richtlinien festlegen.

!!! tip "Auswahl"
    - **Leicht**: Geeignet für Experimente, interne Tools oder Anwendungen mit geringem Risiko, bei denen formale Prüfungen unwahrscheinlich sind.
    - **Standard**: Empfohlen für die meisten Produktionseinsätze, bei denen Prüfungen vorkommen können, aber nicht durchgehend.
    - **Streng**: Erforderlich für regulierte Branchen (Finanzen, Gesundheitswesen, Behörden) oder KI-Systeme mit erheblichem Risikoauswirkung.

## Wichtiger Hinweis

Dieser Mindestsatz unterstützt Erklärbarkeit und Evidence-Bereitschaft; er bietet selbst keine Rechtsberatung und garantiert keine Compliance.

Siehe [Evidence Bundle](../evidence-bundle/) für Bundle-Struktur und TOC; siehe [EV Template](../../standard/current/06-ev-template/) und Schemas für die Ausrichtung auf Feldebene.

Siehe auch: [Log Schemas](../log-schemas/) — normalisierte Logformate für Shadow-AI-Erkennung und Evidence zu Agentenaktivität.

## Regulatorische Overlays (informativ)

Die folgenden **Overlays** beschreiben zusätzliche Evidence, die in bestimmten regulatorischen oder Beschaffungskontexten oft erwartet wird. Sie sind **informativ**; hängen Sie offizielle Vorlagen/Checklisten unverändert im [Abschnitt External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) des EV Template an und referenzieren Sie sie im Manifest per logical_id.

| Overlay | Zusätzlich typisch erwartete Artefakte | Anhängen in | Profil (optional) |
| --- | --- | --- | --- |
| **EU-Hochrisiko** | Risikomanagement, technische Dokumentation (Annex IV), Protokollierung, menschliche Aufsicht, Transparenz (Art 50), Meldewesen zu Vorfällen | payload_index; Evidence Bundle + Annex-IV-Profil | `eu_ai_act_annex_iv.json`, `eu_ai_act_high_risk.json` |
| **EU GPAI CoP** | Model Documentation Form (Transparenz, Urheberrecht, Sicherheit) | External Forms; logical_id z. B. GPAI_MODEL_DOC_FORM | `eu_gp_ai_cop.json` |
| **NIST GenAI** | GenAI-Profil-Artefakte (Modellanpassung, Bewertung, Überwachung) | payload_index; change_log; External Forms / GenAI-Aufzeichnungen | `nist_ai_600_1_genai.json` |
| **UK ATRS / Beschaffung** | ATRS-Transparenzaufzeichnung; Verantwortlicher; Beschaffungsbewertungsnotizen | External Forms; Summary, review | `uk_atrs_procurement.json` |
| **JP-Beschaffung** | Checkliste staatliche GenAI-Beschaffung; Checkliste AI Business Guidelines | External Forms; logical_id z. B. JP_PROCUREMENT_CHECKLIST | `jp_gov_genai_procurement.json` |

Profil-Dateinamen folgen dem Muster `coverage_map/profiles/<target>_<purpose>.json`; jede enthält `target_version`. Siehe [Coverage Map — Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/) für UK und Japan; [EU AI Act](../../coverage-map/eu-ai-act/) und [NIST AI RMF](../../coverage-map/nist-ai-rmf/) für EU und NIST.
