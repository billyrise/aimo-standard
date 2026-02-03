---
description: AIMO Validator - Stellt sicher, dass Evidence Packs den AIMO Standard-Schemas entsprechen. Validierungsregeln, Fehlerbehandlung und Referenzimplementierung für Compliance-Prüfungen.
---

# Validator

Der AIMO Validator stellt sicher, dass Evidence Packs und zugehörige Artefakte den AIMO Standard-Schemas und -Anforderungen entsprechen.

Siehe auch: [Human Oversight Protocol](../../governance/human-oversight-protocol.md) — Verantwortungsgrenze für maschinelle vs. menschliche Überprüfung.

## Validator in der Praxis

Für einen 30-Sekunden-Schnellstart (Installation, Ausführung, Ausgabe interpretieren) siehe [Validator-Hub](../../validator/index.md).

## Validator MVP-Anforderungen

Der minimale viable Validator MUSS die folgenden Prüfungen durchführen:

### 1. Erforderliche-Feld-Validierung

Prüfen, dass alle Pflichtfelder vorhanden sind:

| Artefakt | Erforderliche Felder |
| --- | --- |
| Evidence Pack Manifest | pack_id, pack_version, taxonomy_version, created_date, last_updated, codes, evidence_files |
| Codes-Objekt | FS, UC, DT, CH, IM, RS, EV (OB optional) |
| Evidence-Datei-Eintrag | file_id (EP-01..EP-07), filename, title (ev_type / ev_codes optional) |

### 2. Dimensions-Code-Validierung

Prüfen, dass jede erforderliche Dimension mindestens einen Code hat:

| Dimension | Anforderung |
| --- | --- |
| FS (Funktionaler Scope) | Genau 1 Code |
| UC (Anwendungsfall-Klasse) | Mindestens 1 Code |
| DT (Datentyp) | Mindestens 1 Code |
| CH (Kanal) | Mindestens 1 Code |
| IM (Integrationsmodus) | Genau 1 Code |
| RS (Risikooberfläche) | Mindestens 1 Code |
| OB (Ergebnis / Nutzen) | Optional (0 oder mehr) |
| LG (Log-/Ereignistyp) | Mindestens 1 Code |

### 3. Dictionary-Existenzprüfung

Validieren, dass alle Codes im Taxonomie-Dictionary existieren:

- Taxonomie-Dictionary für die angegebene `taxonomy_version` laden
- Verifizieren, dass jeder Code im Manifest im Dictionary existiert
- Ungültige Codes mit ihrer Dimension und ihrem Wert melden

### 4. Code-Format-Validierung

Prüfen, dass alle Codes dem erwarteten Format entsprechen:

```regex
^(FS|UC|DT|CH|IM|RS|OB|LG)-\d{3}$
```

### 5. Schema-Validierung

Gegen JSON Schemas validieren:

| Schema | Zweck |
| --- | --- |
| `evidence_pack_manifest.schema.json` | Evidence Pack-Manifeste |
| `taxonomy_pack.schema.json` | Taxonomie-Pack-Definitionen |
| `changelog.schema.json` | Changelog-Einträge |

## Validierungsregeln

### Regel: Erforderliche Dimensionen

```yaml
rule_id: required_dimensions
description: Alle erforderlichen Dimensionen müssen mindestens einen Code haben
severity: error
check: |
  - FS: genau 1
  - UC: mindestens 1
  - DT: mindestens 1
  - CH: mindestens 1
  - IM: genau 1
  - RS: mindestens 1
  - LG: mindestens 1
```

### Regel: Gültige Codes

```yaml
rule_id: valid_codes
description: Alle Codes müssen im Taxonomie-Dictionary existieren
severity: error
check: |
  Für jeden Code in manifest.codes:
    - Code existiert im Dictionary für angegebene taxonomy_version
    - Code-Status ist 'active' (Warnung wenn 'deprecated')
```

### Regel: Code-Format

```yaml
rule_id: code_format
description: Alle Codes müssen dem Standard-Format entsprechen
severity: error
pattern: "^(FS|UC|DT|CH|IM|RS|OB|LG)-\\d{3}$"
```

### Regel: Versions-Format

```yaml
rule_id: version_format
description: Versionen müssen gültiges SemVer sein
severity: error
pattern: "^\\d+\\.\\d+\\.\\d+$"
fields:
  - pack_version
  - taxonomy_version
```

## Fehlerausgabe-Format

Validierungsfehler werden im folgenden Format gemeldet:

```
<pfad>: <schweregrad>: <nachricht>
```

**Beispiele:**

```
codes.FS: error: Erforderliche Dimension 'FS' hat keine Codes
codes.UC[0]: error: Code 'UC-999' existiert nicht im Dictionary v0.1.0
pack_version: error: Ungültiges Versionsformat 'v1.0' (erwartet SemVer)
codes.RS[1]: warning: Code 'RS-002' ist veraltet in v0.2.0
```

## Was der Validator NICHT prüft

Der Validator konzentriert sich auf strukturelle Konformität, nicht Inhaltsqualität:

| Aspekt | Grund |
| --- | --- |
| Inhaltsgenauigkeit | Validator prüft Struktur, nicht Bedeutung |
| Evidence-Vollständigkeit | Templates sind Anleitungen, keine erzwungenen Formate |
| Querverweisauflösung | Dateiexistenz wird nicht verifiziert |
| Zeitstempel-Gültigkeit | ISO-8601 wird nicht strikt validiert |
| ID-Eindeutigkeit | Derzeit nicht durchgesetzt |
| Integritäts-Hashes | Anwenderverantwortung |

## Referenzimplementierung

Eine Referenzimplementierung wird in Python bereitgestellt:

```
validator/src/validate.py
```

### Verwendung

```bash
python validator/src/validate.py <manifest.json>
```

### Beispielausgabe

```
Validating: evidence_pack_manifest.json
Taxonomy version: 0.1.0

Checking required dimensions...
  FS: OK (1 code)
  UC: OK (3 codes)
  DT: OK (1 code)
  CH: OK (1 code)
  IM: OK (1 code)
  RS: OK (3 codes)
  OB: OK (2 codes)
  LG: OK (7 codes)

Checking code validity...
  All codes valid.

Validation: PASSED
```

## Versionierungsrichtlinie

Validator-Regeln folgen SemVer:

- **MAJOR**: Breaking-Regeländerungen (neue erforderliche Prüfungen, die bestehende gültige Packs fehlschlagen lassen)
- **MINOR**: Neue optionale Prüfungen, Warnungen oder informative Nachrichten
- **PATCH**: Bug-Fixes, die Validierungsergebnisse nicht ändern

## Schema-Referenzen

| Schema | Speicherort |
| --- | --- |
| Evidence Pack Manifest | `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json` |
| Taxonomy Pack | `source_pack/03_taxonomy/schemas/taxonomy_pack.schema.json` |
| Changelog | `source_pack/03_taxonomy/schemas/changelog.schema.json` |

## Referenzen

- [Taxonomie](./03-taxonomy.md) - Dimensionsdefinitionen
- [Codes](./04-codes.md) - Code-Format
- [Dictionary](./05-dictionary.md) - Code-Dictionary
- [Validator-Regeln](../../validator/index.md) - Vollständige Regeldokumentation
