---
description: AIMO Standard Changelog und Versionierungsrichtlinie. Dokumentiert Versionshistorie, Semantic-Versioning-Regeln und Migrationsanleitung zwischen Releases.
---

# Changelog

Dieser Abschnitt dokumentiert die Versionierungsrichtlinie und Änderungshistorie für den AIMO Standard.

## Versionierungsrichtlinie

AIMO Standard folgt [Semantic Versioning](https://semver.org/) (SemVer):

### Versionsformat: MAJOR.MINOR.PATCH

| Änderungstyp | Versionserhöhung | Beispiele |
| --- | --- | --- |
| **MAJOR** | X.0.0 | Breaking-Schema-Änderungen, Code-Entfernung, Pflichtfeld-Änderungen |
| **MINOR** | 0.X.0 | Neue Codes, neue optionale Felder, neue Dimensionen (optional) |
| **PATCH** | 0.0.X | Dokumentationskorrekturen, Definitionsklarstellungen, Validator-Bug-Fixes |

### Breaking vs. Kompatible Änderungen

**Breaking Changes (MAJOR):**

- Entfernung von Codes (nach Deprecation-Zeitraum)
- Änderungen an Pflichtfeldern in Schemas
- Strukturelle Änderungen, die bestehende Dokumente ungültig machen
- Änderungen an Code-Format-Mustern

**Rückwärtskompatible Änderungen (MINOR):**

- Hinzufügen neuer Codes zu bestehenden Dimensionen
- Hinzufügen neuer optionaler Felder zu Schemas
- Hinzufügen neuer optionaler Dimensionen
- Hinzufügen neuer Evidence-Templates

**Nicht-breaking Änderungen (PATCH):**

- Dokumentationskorrekturen
- Klarstellung bestehender Definitionen
- Übersetzungsverbesserungen
- Validator-Bug-Fixes

## Deprecation-Richtlinie

### Deprecation-Prozess

1. **Als veraltet markieren**: Code oder Feature wird mit `status: deprecated` und `deprecated_in: X.Y.Z` markiert
2. **Deprecation-Zeitraum**: Mindestens eine MINOR-Version muss vor Entfernung vergehen
3. **Ersatz bereitstellen**: Falls zutreffend, zeigt `replaced_by` den Ersatz an
4. **In MAJOR entfernen**: Entfernung erfolgt in der nächsten MAJOR-Version

### Beispiel-Lifecycle

```
v0.0.1: FS-007 eingeführt (status: active)
v0.1.0: FS-007 veraltet (status: deprecated, replaced_by: FS-008)
v0.2.0: FS-007 noch verfügbar mit Deprecation-Warnung
v1.0.0: FS-007 entfernt (status: removed)
```

### Veraltete Codes verwenden

- Veraltete Codes bleiben für Validierung gültig
- Validator SOLLTE Warnung für veraltete Codes ausgeben
- Neue Implementierungen SOLLTEN Ersatz-Codes verwenden
- Bestehende Dokumente KÖNNEN veraltete Codes bis zur Migration weiter verwenden

## Release-Artefakte

Jedes offizielle Release enthält:

| Artefakt | Beschreibung |
| --- | --- |
| Versionierter Site-Snapshot | `https://standard.aimoaas.com/0.0.1/` |
| PDF-Spezifikation | `trust_package.pdf` |
| Asset-Paket (ZIP) | Schemas, Templates, Dictionary |
| Prüfsummen | SHA-256-Hashes für Integrität |
| Changelog | Dieses Dokument |

## Änderungshistorie

### Unveröffentlicht (Namespace- und Normativ-Korrekturen)

**Zusammenfassung:** Behebung der EV-Code-Kollision, Klarstellung EV (Index) vs Evidence Pack (Payload), Härtung von /dev gegen Audit-Fehlzitierung. Evidence-Pack-Dokumenttypen: EP-01..EP-07; Taxonomy EV bleibt für Ereignistypen. Normative Beziehung EV↔Evidence Pack dokumentiert. Banner und Canonical für /dev.

### Version 0.0.1 (2026-02-02)

**Zusammenfassung:** Erstveröffentlichung des AIMO Standards mit 8-Dimensionen-Code-System, Evidence Pack-Templates und umfassender Governance-Dokumentation.

#### Hinzugefügt

**Code-System (8 Dimensionen)**

| Dimension | Hinzugefügte Codes | Beschreibung |
| --- | --- | --- |
| FS | FS-001 bis FS-006 | Funktionaler Scope |
| UC | UC-001 bis UC-010 | Anwendungsfall-Klasse |
| DT | DT-001 bis DT-008 | Datentyp |
| CH | CH-001 bis CH-006 | Kanal |
| IM | IM-001 bis IM-005 | Integrationsmodus |
| RS | RS-001 bis RS-005 | Risikooberfläche |
| OB | OB-001 bis OB-005 | Ergebnis / Nutzen |
| LG | LG-001 bis LG-015 | Log-/Registrierungstyp |

**Schemas**

- `taxonomy_pack.schema.json`: Taxonomie-Pack-Definition
- `changelog.schema.json`: Changelog-Einträge
- `evidence_pack_manifest.schema.json`: Evidence Pack-Manifeste
- `shadow-ai-discovery.schema.json`: Shadow AI-Erkennungs-Evidence
- `agent-activity.schema.json`: Agentenaktivitäts-Evidence

**Evidence Pack-Templates (MVP)**

- EV-01: Systemübersicht
- EV-02: Datenfluss
- EV-03: KI-Inventar
- EV-04: Risiko- & Auswirkungsbewertung
- EV-05: Kontrollen & Genehmigungen
- EV-06: Logging & Monitoring
- EV-07: Incident- & Ausnahme-Handling

**Dokumentation**

- Taxonomie-Dokumentation mit 8-Dimensionen-Definitionen
- Code-System-Format-Spezifikation
- Dictionary-CSV-Format-Spezifikation
- Versionierungs- und Änderungsrichtlinie
- Validator-MVP-Anforderungen
- Human Oversight Protocol
- Coverage Map (ISO 42001, NIST AI RMF, EU AI Act, ISMS)
- Trust Package

#### Rückwärtskompatibilität

Dies ist die Erstveröffentlichung; keine Rückwärtskompatibilitätsbedenken.

---

## Maschinenlesbarer Changelog

Ein maschinenlesbarer Changelog ist verfügbar:

- `changelog/changelog.json`

Diese Datei folgt dem `changelog.schema.json`-Schema und kann programmgesteuert geparst werden.

## Referenzen

- [Taxonomie](./03-taxonomy.md) - Dimensionsdefinitionen
- [Dictionary](./05-dictionary.md) - Code-Dictionary
- [Versionierungsrichtlinie](../../governance/index.md) - Versionierungsrichtlinie (siehe VERSIONING.md im Repository-Root)
