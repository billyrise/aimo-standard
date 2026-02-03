---
description: AIMO Code-System Format und Namenskonventionen. Definiert Code-Struktur (XX-NNN), Lifecycle-Zustände, Versionierung und Deprecation-Richtlinien für Taxonomie-Codes.
---

# Codes

Diese Seite definiert das AIMO Code-System Format, Namenskonventionen und Lifecycle-Management.

## Code-Format

Alle AIMO-Codes folgen dem Format: **`<PRÄFIX>-<TOKEN>`**

| Komponente | Beschreibung | Format | Beispiel |
| --- | --- | --- | --- |
| `<PRÄFIX>` | Dimensions-Identifikator | 2 Großbuchstaben | FS, UC, DT |
| `-` | Trennzeichen | Bindestrich | - |
| `<TOKEN>` | Eindeutiges Token innerhalb der Dimension | 3 Ziffern (nullgefüllt) | 001, 002, 003 |

### Beispiele

- `FS-001` - Funktionaler Scope: Endbenutzer-Produktivität
- `UC-005` - Anwendungsfall-Klasse: Code-Generierung
- `DT-004` - Datentyp: Personenbezogene Daten
- `CH-003` - Kanal: IDE-Plugin
- `IM-002` - Integrationsmodus: SaaS-integriert
- `RS-001` - Risikooberfläche: Datenleck
- `OB-001` - Ergebnis/Nutzen: Effizienz
- `LG-001` - Log-/Registrierungstyp: Antragsdatensatz

## Namensräume

Die AIMO Taxonomie verwendet 8 Dimensions-Namensräume:

| ID | Name | Präfix | Code-Anzahl |
| --- | --- | --- | --- |
| **FS** | Funktionaler Scope | `FS-` | 6 |
| **UC** | Anwendungsfall-Klasse | `UC-` | 30 |
| **DT** | Datentyp | `DT-` | 10 |
| **CH** | Kanal | `CH-` | 8 |
| **IM** | Integrationsmodus | `IM-` | 7 |
| **RS** | Risikooberfläche | `RS-` | 8 |
| **OB** | Ergebnis / Nutzen | `OB-` | 7 |
| **LG** | Log/Event-Typ | `LG-` | 15 |

**Gesamt: 91 Codes über 8 Dimensionen**

### Namensraum-Regeln

1. **Präfix ist fest**: Das zwei-Buchstaben-Dimensions-Präfix (FS, UC, etc.) ist permanent und wird sich nie ändern.
2. **Nullfüllung**: Tokens sind immer 3 Ziffern, nullgefüllt (z.B. `001` nicht `1`).
3. **Sequenzielle Zuweisung**: Neue Codes erhalten die nächste verfügbare Nummer innerhalb einer Dimension.
4. **Keine Wiederverwendung**: Entfernte Codes werden nie für andere Bedeutungen neu zugewiesen.

## Stabilitätsregeln

Code-Stabilität ist ein kritisches Prinzip für Audit-Nachverfolgbarkeit.

### ID-Unveränderlichkeit

- **Code-IDs sind unveränderlich** — einmal zugewiesen, ändert eine Code-ID nie ihre Bedeutung
- Ein Code wie `UC-001` wird immer "Allgemeine F&A" für seinen gesamten Lifecycle bedeuten
- Wenn die Bedeutung geändert werden muss, wird stattdessen ein neuer Code erstellt

### Keine-Wiederverwendung-Richtlinie

- Veraltete oder entfernte Codes werden **nie** für andere Bedeutungen neu zugewiesen
- Dies stellt sicher, dass historisches Evidence gültig und nachverfolgbar bleibt
- Beispiel: Wenn `UC-010` veraltet ist, erhält ein neuer Anwendungsfall `UC-031` (nicht `UC-010`)

### Deprecation vor Entfernung

- Codes müssen für mindestens eine MINOR-Version als `deprecated` markiert werden, bevor sie entfernt werden
- Entfernung erfolgt nur bei MAJOR-Versionserhöhungen
- Siehe Abschnitt [Lifecycle](#lifecycle) für Details

## Verwendung

### Erforderliche Dimensionen

Für jedes KI-System oder jeden Anwendungsfall MÜSSEN Sie mindestens einen Code aus jeder erforderlichen Dimension angeben:

| Dimension | Auswahl | Hinweise |
| --- | --- | --- |
| FS | Genau 1 | Primäre Geschäftsfunktion |
| UC | 1 oder mehr | Ausgeführte Aufgabentypen |
| DT | 1 oder mehr | Datenklassifizierungen |
| CH | 1 oder mehr | Zugriffskanäle |
| IM | Genau 1 | Integrationsmodus |
| RS | 1 oder mehr | Risikokategorien |
| LG | 1 oder mehr | Log/Event-Typen |

### Optionale Dimensionen

| Dimension | Auswahl | Hinweise |
| --- | --- | --- |
| OB | 0 oder mehr | Erwartete Vorteile (optional) |

### Code-Komposition

Bei der Dokumentation eines KI-Systems werden Codes aus mehreren Dimensionen kombiniert. Die **Kompositionspriorität** bestimmt die Reihenfolge bei der Auflistung von Codes:

1. FS (Funktionaler Scope)
2. UC (Anwendungsfall-Klasse)
3. DT (Datentyp)
4. CH (Kanal)
5. IM (Integrationsmodus)
6. RS (Risikooberfläche)
7. OB (Ergebnis / Nutzen)
8. EV (Evidence-Typ)

**Beispielkomposition:**

```
FS: FS-001
UC: UC-001, UC-002
DT: DT-002, DT-004
CH: CH-001
IM: IM-002
RS: RS-001, RS-003
OB: OB-001
LG: LG-001, LG-002
```

## Lifecycle

### Statuswerte

| Status | Beschreibung | Validator-Verhalten |
| --- | --- | --- |
| `active` | Derzeit gültig und in Verwendung | Akzeptiert |
| `deprecated` | Noch gültig, aber zur Entfernung vorgesehen | Akzeptiert mit Warnung |
| `removed` | Nicht mehr gültig; nicht verwenden | Abgelehnt |

### Lifecycle-Metadatenfelder

Das Dictionary verfolgt den Lifecycle mit diesen Feldern:

| Feld | Erforderlich | Beschreibung | Beispiel |
| --- | --- | --- | --- |
| `status` | Ja | Aktueller Status | `active` |
| `introduced_in` | Ja | Version, als Code hinzugefügt wurde | `0.1.0` |
| `deprecated_in` | Nein | Version, als als veraltet markiert | `1.2.0` |
| `removed_in` | Nein | Version, als entfernt | `2.0.0` |
| `replaced_by` | Nein | Ersetzungscode(s) | `UC-015` |
| `backward_compatible` | Ja | Ob Änderung bestehende Nutzung bricht | `true` |

### Deprecation-Regeln

1. Codes MÜSSEN für mindestens eine MINOR-Version als `deprecated` markiert werden, bevor sie entfernt werden
2. Veraltete Codes enthalten `deprecated_in`-Version und `replaced_by`, falls zutreffend
3. Entfernung erfolgt nur bei MAJOR-Versionserhöhungen
4. Veraltete Codes bleiben während des Deprecation-Zeitraums für Rückwärtskompatibilität gültig

**Beispielzeitlinie:**

| Version | Status | Aktion |
| --- | --- | --- |
| 0.1.0 | `active` | Code `UC-010` eingeführt |
| 1.2.0 | `deprecated` | Als veraltet markiert, `replaced_by: UC-031` |
| 2.0.0 | `removed` | Nicht mehr vom Validator akzeptiert |

### Versionierung

Code-Änderungen folgen [Semantic Versioning](./08-changelog.md):

- **MAJOR**: Code-Entfernung oder Breaking Changes
- **MINOR**: Neue Codes hinzugefügt, Codes veraltet
- **PATCH**: Nur Definitionsklarstellungen (keine strukturellen Änderungen)

### Rückwärtskompatibilität

Das `backward_compatible`-Feld zeigt an, ob eine Änderung bestehende Nutzung bricht:

| Wert | Bedeutung |
| --- | --- |
| `true` | Bestehendes Evidence mit diesem Code bleibt gültig |
| `false` | Bestehendes Evidence benötigt möglicherweise Updates (MAJOR-Versionsänderung) |

## Validierung

Der Validator prüft:

1. Alle erforderlichen Dimensionen haben mindestens einen Code
2. Einzel-Auswahl-Dimensionen haben genau einen Code
3. Alle Codes existieren im aktuellen Taxonomie-Dictionary
4. Code-Format entspricht dem Muster `<PRÄFIX>-<TOKEN>` (z.B. `UC-001`)
5. Veraltete Codes werden mit Warnungen gekennzeichnet

Siehe [Validator](./07-validator.md) für Implementierungsdetails.

## SSOT-Referenz

!!! info "Quelle der Wahrheit"
    Die maßgebliche Definition ist `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv`. Diese Seite ist erklärend. Siehe [Lokalisierungsleitfaden](../../contributing/localization.md) für Update-Workflows.

## Verwandte Seiten

- [Taxonomie](./03-taxonomy.md) - Vollständige Dimensionsdefinitionen
- [Dictionary](./05-dictionary.md) - Vollständige Code-Listen und Spaltendefinitionen
- [Validator](./07-validator.md) - Validierungsregeln
- [Changelog](./08-changelog.md) - Versionshistorie
