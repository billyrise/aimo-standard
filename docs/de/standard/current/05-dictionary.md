---
description: AIMO Dictionary - Maßgebliche Liste von 91 Taxonomie-Codes über 8 Dimensionen. Vollständige Definitionen, Labels und Lifecycle-Informationen für KI-Klassifizierung.
---
<!-- aimo:translation_status=translated -->

# Dictionary

Das AIMO Dictionary ist die maßgebliche Liste aller gültigen Codes innerhalb der Taxonomie. Es bietet vollständige Definitionen für jeden Code einschließlich Labels, Beschreibungen und Lifecycle-Informationen.

## Was ist das Dictionary

Das Dictionary bietet einen vollständigen, maschinenlesbaren Satz aller AIMO Taxonomie-Codes. Es enthält:

- Alle 91 Codes über 8 Dimensionen
- Labels und Definitionen (mit Übersetzungen in Sprachpaketen)
- Lifecycle-Metadaten (Status, eingeführte Version, veraltet, entfernt)
- Geltungsbereich-Hinweise und Beispiele für Code-Nutzung

Das Dictionary ermöglicht:

1. **Evidence-Templates**: Codes werden in EV-Templates verwendet, um KI-Systeme zu klassifizieren
2. **Validator**: Der Validator prüft, dass alle Codes im Dictionary existieren
3. **Coverage Map**: Codes ermöglichen Zuordnung zu externen Frameworks und Vorschriften

!!! info "Single Source of Truth (SSOT)"
    Das SSOT für das Dictionary ist:

    - **Struktur**: `data/taxonomy/canonical.yaml` (Codes, Status, Lifecycle)
    - **Übersetzungen**: `data/taxonomy/i18n/*.yaml` (Labels, Definitionen pro Sprache)

    CSV-Dateien sind **generierte Artefakte** zur Distribution. Siehe [Releases](../../../releases/) für Downloads.

## Spalten-Schema

Das kanonische Dictionary verwendet **18 Spalten** (sprachneutrale Struktur):

### Identifikationsspalten (5)

| # | Spalte | Erforderlich | Beschreibung | Beispiel |
| --- | --- | --- | --- | --- |
| 1 | `standard_id` | Ja | Standard-Identifikator | `AIMO-STD` |
| 2 | `standard_version` | Ja | SemVer-Format | `0.1.0` |
| 3 | `dimension_id` | Ja | Zwei-Buchstaben-Dimensions-ID | `FS`, `UC`, `DT` |
| 4 | `dimension_name` | Ja | Dimensionsname | `Functional Scope` |
| 5 | `code` | Ja | Vollständiger Code | `UC-001` |

### Label- und Definitionsspalten (4)

| # | Spalte | Erforderlich | Beschreibung | Beispiel |
| --- | --- | --- | --- | --- |
| 6 | `label` | Ja | Code-Label (max 50 Zeichen) | `General Q&A` |
| 7 | `definition` | Ja | Code-Definition (1-2 Sätze) | `General question answering...` |
| 8 | `scope_notes` | Nein | Geltungsbereich-Klarstellung | `Low to medium risk...` |
| 9 | `examples` | Nein | Pipe-getrennte Beispiele | `chatbot\|recommendation` |

!!! note "Übersetzungen"
    Das kanonische Datenmodell trennt Übersetzungen in Sprachpakete (`data/taxonomy/i18n/*.yaml`). Jedes Sprachpaket bietet lokalisierte `dimension_name`, `label` und `definition`-Werte. Siehe [Lokalisierungsleitfaden](../../../contributing/localization/) für Details.

### Lifecycle-Spalten (6)

| # | Spalte | Erforderlich | Beschreibung | Beispiel |
| --- | --- | --- | --- | --- |
| 10 | `status` | Ja | `active`, `deprecated`, `removed` | `active` |
| 11 | `introduced_in` | Ja | Version, als hinzugefügt | `0.1.0` |
| 12 | `deprecated_in` | Nein | Version, als veraltet | `1.2.0` |
| 13 | `removed_in` | Nein | Version, als entfernt | `2.0.0` |
| 14 | `replaced_by` | Nein | Ersetzungscode | `UC-015` |
| 15 | `backward_compatible` | Ja | `true` oder `false` | `true` |

### Governance-Spalten (3)

| # | Spalte | Erforderlich | Beschreibung | Beispiel |
| --- | --- | --- | --- | --- |
| 16 | `references` | Nein | Externe Referenzen | ISO/IEC 42001 |
| 17 | `owner` | Nein | Verantwortliche Partei | `AIMO WG` |
| 18 | `last_reviewed_date` | Nein | Letzte Überprüfung (JJJJ-MM-TT) | `2026-01-19` |

## Initiale Einträge

Die aktuelle Dictionary-Version ist **v0.1.0** und enthält:

| Dimension | Name | Aktive Codes | Veraltet | Gesamt |
| --- | --- | --- | --- | --- |
| FS | Funktionaler Scope | 6 | 0 | 6 |
| UC | Anwendungsfall-Klasse | 30 | 0 | 30 |
| DT | Datentyp | 10 | 0 | 10 |
| CH | Kanal | 8 | 0 | 8 |
| IM | Integrationsmodus | 7 | 0 | 7 |
| RS | Risikooberfläche | 8 | 0 | 8 |
| OB | Ergebnis / Nutzen | 7 | 0 | 7 |
| LG | Log/Event-Typ | 15 | 0 | 15 |
| **Gesamt** | | **91** | **0** | **91** |

!!! note "Vollständige Code-Listen"
    Die vollständige Liste von 91 Codes ist in den generierten CSV-Artefakten verfügbar. Diese Dokumentationsseite bietet Spaltendefinitionen und Nutzungsanleitungen. Für detaillierte Code-Definitionen:

    - **Download**: Siehe [Releases](../../../releases/) für Pro-Sprache-CSV-Dateien
    - **Pro-Sprache-CSV**: `artifacts/taxonomy/current/{lang}/taxonomy_dictionary.csv`
    - **Legacy EN/JA gemischte CSV**: `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` (eingefroren, nur für Rückwärtskompatibilität)

## Update-Richtlinie

### Neue Codes hinzufügen

1. Die nächste verfügbare Nummer innerhalb der Dimension zuweisen (z.B. `UC-031` nach `UC-030`)
2. `status` auf `active` setzen
3. `introduced_in` auf die aktuelle Version setzen
4. `backward_compatible` auf `true` setzen
5. Label und Definition bereitstellen (Übersetzungen zu Sprachpaketen hinzufügen)

### Bestehende Codes modifizieren

| Änderungstyp | Erlaubt | Versionsauswirkung |
| --- | --- | --- |
| Definitionsklarstellung | Ja | PATCH |
| Geltungsbereich-Hinweise-Update | Ja | PATCH |
| Label-Änderung (Bedeutung erhalten) | Ja | MINOR |
| Bedeutungsänderung | Nein | Neuen Code erstellen |

### Codes veralten

1. `status` auf `deprecated` setzen
2. `deprecated_in` auf aktuelle Version setzen
3. `replaced_by` auf den neuen Code setzen (falls zutreffend)
4. Code bleibt für Rückwärtskompatibilität funktional
5. Grund in scope_notes dokumentieren

### Codes entfernen

1. Zuerst für mindestens eine MINOR-Version veralten
2. `status` auf `removed` setzen
3. `removed_in` auf aktuelle MAJOR-Version setzen
4. Code ist nicht mehr für neues Evidence gültig

### Kompatibilitätsrichtlinie

| Aktion | Versionsauswirkung | Rückwärtskompatibel |
| --- | --- | --- |
| Neuen Code hinzufügen | MINOR | Ja |
| Code veralten | MINOR | Ja |
| Definition klären | PATCH | Ja |
| Code entfernen | MAJOR | Nein |
| Code-Bedeutung ändern | Nicht erlaubt | - |

## Verwendung

### In Evidence-Templates

Jedes EV-Template enthält eine 8-Dimensionen-Codes-Tabelle:

```markdown
## AIMO Codes (8 Dimensionen)

| Dimension | Code(s) | Label |
| --- | --- | --- |
| **FS** | `FS-001` | Endbenutzer-Produktivität |
| **UC** | `UC-001`, `UC-002` | Allgemeine F&A, Zusammenfassung |
| **DT** | `DT-002`, `DT-004` | Intern, Personenbezogene Daten |
| **CH** | `CH-001` | Web-UI |
| **IM** | `IM-002` | SaaS-integriert |
| **RS** | `RS-001`, `RS-003` | Datenleck, Compliance-Verstoß |
| **OB** | `OB-001` | Effizienz |
| **LG** | `LG-001`, `LG-002` | Antragsdatensatz, Prüfungs-/Genehmigungsdatensatz |
```

### Im Validator

Der Validator prüft:

1. Alle in Evidence referenzierten Codes existieren im Dictionary
2. Code-Format entspricht dem erwarteten Muster (`PRÄFIX-###`)
3. Veraltete Codes lösen Warnungen aus
4. Entfernte Codes werden abgelehnt

### Erweiterungsrichtlinien

Organisationen KÖNNEN das Dictionary mit benutzerdefinierten Codes erweitern:

**Erweiterungs-Präfix:**

```
X-<ORG>-<DIM>-<TOKEN>
```

Beispiel: `X-ACME-UC-901` für ACMEs benutzerdefinierten Anwendungsfall-Code.

**Erweiterungsregeln:**

1. Benutzerdefinierte Codes DÜRFEN NICHT mit Standard-Codes kollidieren
2. Benutzerdefinierte Codes SOLLTEN in einem lokalen Erweiterungs-Dictionary dokumentiert werden
3. Beim Austausch von Evidence mit externen Parteien nur Standard-Codes verwenden

## Downloads

Siehe [Releases](../../../releases/) für herunterladbare Pakete mit Dictionary und zugehörigen Dateien.

## Verwandte Seiten

- [Taxonomie](../03-taxonomy/) - Dimensionsdefinitionen und Code-Tabellen
- [Codes](../04-codes/) - Code-Format, Benennung und Lifecycle
- [Evidence-Templates](../06-ev-template/) - Wie Codes in Templates verwendet werden
- [Validator](../07-validator/) - Code-Validierungsregeln
- [Changelog](../08-changelog/) - Versionshistorie
