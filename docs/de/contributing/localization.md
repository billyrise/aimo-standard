---
description: AIMO Lokalisierungsleitfaden - i18n-Struktur, Wartungsworkflow und SSOT-Prinzipien für mehrsprachige Dokumentation.
---

# Lokalisierungsleitfaden

Diese Seite dokumentiert die Lokalisierungs-(i18n-)Struktur, den Wartungsworkflow und die SSOT-(Single Source of Truth-)Prinzipien für die AIMO Standard-Dokumentation.

## Sprachreinhaltungsrichtlinie

**Jede Sprachseite sollte nur Inhalte in dieser Sprache enthalten.**

| Regel | Beschreibung |
| --- | --- |
| **EN-Seiten** | Dürfen keine CJK-Zeichen oder Verweise auf sprachspezifische Spalten (z.B. `_ja`-Suffixe) enthalten |
| **JA-Seiten** | Dürfen EN-spezifische Terminologie nicht so erklären, als wäre sie die kanonische Struktur |
| **Ausnahmen** | Aufgelistet in `MIXED_LANGUAGE_ALLOWLIST` in `tooling/checks/lint_i18n.py` |

Diese Richtlinie stellt sicher:
1. Leser sehen nur ihre ausgewählte Sprache
2. Das Hinzufügen neuer Sprachen erfordert keine Aktualisierung bestehender Seiten
3. CI kann Verstöße automatisch erkennen

## Sprachstruktur

Die AIMO Standard-Dokumentation verwendet eine **ordnerbasierte i18n-Struktur**:

```
docs/
├── en/           # Englisch (kanonisch)
├── ja/           # Japanisch (日本語)
├── es/           # Spanisch (Español)
├── fr/           # Französisch (Français)
├── de/           # Deutsch (Deutsch)
├── pt/           # Portugiesisch (Português)
├── it/           # Italienisch (Italiano)
├── zh/           # Vereinfachtes Chinesisch (简体中文)
├── zh-TW/        # Traditionelles Chinesisch (繁體中文)
└── ko/           # Koreanisch (한국어)
```

- **Englisch ist kanonisch**: Der Ordner `docs/en/` ist die autoritative Quelle für Dokumentationsinhalte.
- **Andere Sprachen spiegeln die Struktur**: Jeder Sprachordner (`ja/`, etc.) behält die gleiche Dateistruktur wie `en/` bei.
- **Gleiche Dateinamen**: Alle Sprachen verwenden die Erweiterung `.md` (kein Sprachsuffix in Dateinamen).
- **Fallback auf Englisch**: Fehlende Übersetzungen fallen automatisch auf englische Inhalte zurück.

## Taxonomie-Datenmodell

Die Taxonomie verwendet eine **sprachneutrale kanonische Struktur** mit separaten Übersetzungspaketen:

```
data/
└── taxonomy/
    ├── canonical.yaml           # Sprachneutral (Codes, Status, Lifecycle)
    └── i18n/
        ├── en.yaml              # Englische Labels und Definitionen
        ├── ja.yaml              # Japanische Labels und Definitionen
        └── {lang}.yaml          # Zusätzliche Sprachen (leere Vorlage)
```

### Kanonische Struktur (`canonical.yaml`)

Enthält sprachneutrale Daten:

- Code-Identifikatoren (z.B. `FS-001`, `UC-001`)
- Status (`active`, `deprecated`, `removed`)
- Lifecycle-Metadaten (`introduced_in`, `deprecated_in`, `removed_in`, `replaced_by`)
- Geltungsbereich-Hinweise und Beispiele (auf Englisch, als technische Referenzen)

### Übersetzungspakete (`i18n/*.yaml`)

Jedes Sprachpaket enthält:

- Dimensionsnamen (z.B. "Functional Scope")
- Code-Labels (z.B. "End-user Productivity")
- Code-Definitionen

**Fallback**: Wenn eine Übersetzung fehlt, verwendet das System Englisch.

## SSOT-Prinzip

AIMO verwendet eine **SSOT-first-Architektur** für Taxonomiedaten:

| Asset-Typ | SSOT-Speicherort | Beschreibung |
| --- | --- | --- |
| **Taxonomie (Struktur)** | `data/taxonomy/canonical.yaml` | Sprachneutrale Struktur (SSOT) |
| **Taxonomie (i18n)** | `data/taxonomy/i18n/*.yaml` | Pro-Sprache-Übersetzungen (SSOT) |
| **Coverage Map** | `coverage_map/coverage_map.yaml` | Framework-zu-Evidence-Zuordnung |
| **Schemas** | `schemas/jsonschema/` | JSON-Validierungsschemas |

### Abgeleitete Dateien

Die folgenden Dateien werden aus dem SSOT **generiert** und sollten NICHT manuell bearbeitet werden:

| Datei | Generiert aus | Generator |
| --- | --- | --- |
| `artifacts/taxonomy/{version}/{lang}/taxonomy_dictionary.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_en.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_ja.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/code_system.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/dimensions_en_ja.md` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_dictionary.json` | canonical + i18n | `build_artifacts.py` |

### Sprachcodes (BCP47)

AIMO verwendet BCP47-Sprachcodes:

| Code | Sprache | Status |
| --- | --- | --- |
| `en` | Englisch | Kanonisch (Quelle) |
| `ja` | Japanisch (日本語) | Aktiv |
| `es` | Spanisch (Español) | Aktiv |
| `fr` | Französisch (Français) | Aktiv |
| `de` | Deutsch (Deutsch) | Aktiv |
| `pt` | Portugiesisch (Português) | Aktiv |
| `it` | Italienisch (Italiano) | Aktiv |
| `zh` | Vereinfachtes Chinesisch (简体中文) | Aktiv |
| `zh-TW` | Traditionelles Chinesisch (繁體中文) | Aktiv |
| `ko` | Koreanisch (한국어) | Aktiv |

### Legacy-CSV-Dateien (Eingefroren)

Die Legacy-EN/JA-gemischten CSV-Dateien in `source_pack/03_taxonomy/legacy/` sind:

- **Eingefroren auf 21 Spalten** — keine neuen Sprachspalten werden hinzugefügt
- **Für Rückwärtskompatibilität gepflegt** — bestehende Integrationen können sie weiterhin verwenden
- **CI-durchgesetzt** — das Hinzufügen von `label_es`, `definition_de`, etc. lässt den Build fehlschlagen

Für neue Sprachen verwenden Sie die Pro-Sprache-Artefakte in `artifacts/taxonomy/{version}/{lang}/`.

## Übersetzungsaktualitäts-Tracking

AIMO verwendet ein **Übersetzungsaktualitäts-Tracking**-System, um die Konsistenz zwischen englischen (Quell-) und übersetzten Inhalten zu wahren.

### Wie es funktioniert

1. Jede übersetzte Datei enthält Metadaten, die verfolgen, von welcher Version der englischen Quelle sie übersetzt wurde
2. Wenn englische Inhalte aktualisiert werden, erkennt das System veraltete Übersetzungen
3. CI warnt vor veralteten Übersetzungen, blockiert aber nicht (Übersetzungen können hinterherhinken)

### Übersetzungsmetadaten

Übersetzte Dateien enthalten Frontmatter-Metadaten:

```yaml
---
# TRANSLATION METADATA - DO NOT REMOVE
source_file: en/standard/current/01-overview.md
source_hash: abc123def456
translation_date: 2026-02-02
translator: human|machine|hybrid
translation_status: current|outdated|needs_review
---
```

### Verwendung des Sync-Tools

```bash
# Alle Übersetzungen auf Aktualität prüfen
python tooling/i18n/sync_translations.py --check

# Bestimmte Sprache prüfen
python tooling/i18n/sync_translations.py --check --lang ja

# Übersetzungsbericht generieren
python tooling/i18n/sync_translations.py --report

# Neue Sprache initialisieren (EN als Basis kopieren)
python tooling/i18n/sync_translations.py --init-lang es

# Metadaten nach Abschluss der Übersetzung aktualisieren
python tooling/i18n/sync_translations.py --update-meta docs/ja/index.md
```

Für detaillierte technische Spezifikation siehe `tooling/i18n/TRANSLATION_SYNC_SPEC.md`.

## Update-Workflows

### Taxonomie-Updates (Neuer SSOT-First-Workflow)

1. Bearbeiten Sie das SSOT in `data/taxonomy/`:
   - Strukturänderungen → `canonical.yaml`
   - Englische Übersetzungen → `i18n/en.yaml`
   - Japanische Übersetzungen → `i18n/ja.yaml`
2. Validierung ausführen: `python tooling/checks/lint_taxonomy_ssot.py`
3. Alle abgeleiteten Dateien regenerieren: `python tooling/taxonomy/build_artifacts.py --version current --langs en ja`
4. Dokumentationsseiten nach Bedarf aktualisieren
5. Alle Änderungen zusammen committen

### Coverage Map-Updates

1. Bearbeiten Sie `coverage_map/coverage_map.yaml` (das SSOT)
2. Aktualisieren Sie die entsprechenden Framework-Seitentabellen (`docs/en/coverage-map/*.md`)
3. Aktualisieren Sie japanische Übersetzungen (`docs/ja/coverage-map/*.md`)
4. Alle Änderungen zusammen committen

### Dokumentations-Updates

1. Bearbeiten Sie die englische Quelle (`docs/en/...`)
2. Aktualisieren Sie Übersetzungen nach Bedarf (oder markieren Sie sie für spätere Aktualisierung)
3. Führen Sie `python tooling/i18n/sync_translations.py --check` aus, um veraltete Übersetzungen zu sehen
4. Führen Sie `python tooling/checks/lint_i18n.py` aus, um Überschriftenkonsistenz zu überprüfen
5. Führen Sie `mkdocs build --strict` aus, um den Build zu überprüfen
6. Alle Änderungen zusammen committen

!!! note "Übersetzungspriorität"
    Nicht alle Übersetzungen müssen sofort aktualisiert werden. Tier 1 (kritische) Seiten sollten priorisiert werden:
    
    - `index.md`
    - `standard/current/*.md`
    - `governance/index.md`
    - `releases/index.md`

## Hinzufügen einer neuen Sprache (5 Schritte)

Um eine neue Sprache hinzuzufügen (z.B. Spanisch):

### Schritt 1: Taxonomiepaket generieren

```bash
python tooling/taxonomy/build_i18n_taxonomy.py --add-lang es --lang-name "Español"
```

Erstellt `data/taxonomy/i18n/es.yaml` mit englischen Referenzen als Kommentare.

### Schritt 2: Docs-Ordner erstellen

```bash
mkdir -p docs/es && cp -r docs/en/* docs/es/
```

### Schritt 3: mkdocs.yml aktualisieren

```yaml
plugins:
  - i18n:
      languages:
        - locale: es
          name: Español
          build: true
```

### Schritt 4: Übersetzen

- Übersetzen Sie `data/taxonomy/i18n/es.yaml`
- Übersetzen Sie Dateien in `docs/es/`

### Schritt 5: Überprüfen

```bash
python tooling/checks/lint_i18n.py && mkdocs build --strict
```

!!! success "Fertig"
    Neue Sprache ist jetzt verfügbar unter `/dev/es/`

## Dateibenennungskonventionen

| Muster | Beispiel | Beschreibung |
| --- | --- | --- |
| `index.md` | `docs/en/governance/index.md` | Abschnitts-Landingpage |
| `{topic}.md` | `docs/en/governance/trust-package.md` | Themenseite |
| `{NN}-{topic}.md` | `docs/en/standard/current/03-taxonomy.md` | Nummerierte Spezifikationsseite |

## Qualitätsprüfungen

Führen Sie diese Prüfungen vor dem Committen aus:

```bash
# i18n-Struktur, Überschriftenkonsistenz und veraltete Phrasenerkennung
python tooling/checks/lint_i18n.py

# Schema- und Manifest-Lints
python tooling/checks/lint_schema.py
python tooling/checks/lint_manifest.py

# Taxonomie-SSOT-Lints
python tooling/checks/lint_taxonomy_ssot.py --required-langs en
python tooling/checks/lint_legacy_csv.py
python tooling/checks/lint_taxonomy_dictionary.py
python tooling/checks/lint_taxonomy_json.py

# Taxonomie-Artefakte aktuell
python tooling/taxonomy/build_artifacts.py --check

# Build-Verifizierung
mkdocs build --strict
```

## Verwandte Seiten

- [Releases](../releases/index.md) — Herunterladbare Pakete
- [Governance](../governance/index.md) — Projekt-Governance
