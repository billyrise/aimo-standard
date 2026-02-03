---
description: AIMO Evidence Pack-Templates und Nutzungsleitfaden. Struktur zur Dokumentation von KI-Governance-Evidence mit Index-Management und prüfungsbereiter Formatierung.
---

# Evidence Pack Template (EP)

Dieser Abschnitt definiert die Evidence Pack-Templates und deren Verwendung. Ein Evidence Pack ist eine Sammlung von Dokumentation, die Governance und Compliance für ein KI-System nachweist.

## Namensraum: Evidence Pack-Dokumenttypen (EP) vs Taxonomy Evidence Type (EV)

> **Wichtig**: **EP-01..EP-07** bezeichnen *Dokumenttypen* (Evidence Pack-Dateitypen). **LG-001, LG-002, …** in der [Taxonomie](./03-taxonomy.md) bezeichnen *Log-/Registrierungstypen* (Antragsdatensatz, Prüf-/Genehmigungsdatensatz usw.). **EV-** reserviert für Evidence-Artefakt-IDs. EP für Pack-Struktur, LG für Lebenszyklus-Evidenzklassifikation.

## Grundprinzip: Index- und Diff-Management

Was zählt, ist nicht nur der Inhalt einzelner Einreichungen, sondern das **Index**- und **Diff-Management** über Evidence-Elemente hinweg.

Ein Evidence Pack dient als Index, der KI-Systeme mit ihren Governance-Artefakten verknüpft. Der Wert liegt in:

1. **Nachverfolgbarkeit**: Verknüpfung von Entscheidungen, Genehmigungen und Änderungen über die Zeit
2. **Auditierbarkeit**: Ermöglichung für Prüfer, durch die Evidence-Struktur zu navigieren
3. **Wartbarkeit**: Verfolgung, was sich wann und warum geändert hat

## MVP Evidence Set (EP-01 bis EP-07)

Die folgenden sieben **Evidence Pack-Dokumenttypen** (EP) bilden das **minimale viable Set** zum Nachweis von KI-Governance. Jeder ist ein Dokumenten-Template; Taxonomy-**LG**-Codes (Antragsdatensatz, Prüf/Genehmigung usw.) werden an anderer Stelle im Bundle und in `codes.LG` zur Klassifikation von *Log-/Registrierung*-Evidenz verwendet.

| ID | Dokumenttyp | Zweck |
| --- | --- | --- |
| EP-01 | Systemübersicht | KI-System und seinen Zweck dokumentieren |
| EP-02 | Datenfluss | Datenbewegung durch das System abbilden |
| EP-03 | Inventar | Katalog von KI-Assets pflegen |
| EP-04 | Risiko- & Auswirkungsbewertung | Risiken bewerten und dokumentieren |
| EP-05 | Kontrollen & Genehmigungen | Kontrollen und Genehmigungsdatensätze dokumentieren |
| EP-06 | Logging & Monitoring | Logging- und Monitoring-Setup definieren |
| EP-07 | Incident & Ausnahme | Incidents und Ausnahmen verfolgen |

## Evidence Pack Manifest

Jedes Evidence Pack MUSS eine Manifest-Datei enthalten mit:

### Obligatorische Metadaten

| Feld | Beschreibung | Erforderlich |
| --- | --- | --- |
| `pack_id` | Eindeutiger Identifikator (z.B. EP-EXAMPLE-001) | Ja |
| `pack_version` | SemVer-Version des Packs | Ja |
| `taxonomy_version` | Version der verwendeten AIMO Taxonomie | Ja |
| `created_date` | Pack-Erstellungsdatum | Ja |
| `last_updated` | Letztes Update-Datum | Ja |
| `owner` | Verantwortliche Partei | Ja |

### AIMO Codes (8 Dimensionen)

Jedes Evidence Pack MUSS Codes aus allen 8 Dimensionen enthalten. Die Dimension **LG** listet *Taxonomy*-Log-/Registrierungstypen (z. B. Antragsdatensatz, Prüf/Genehmigung), die auf dieses Pack zutreffen—nicht Dokumenttyp-Codes. Der Dokumenttyp wird durch `evidence_files[].file_id` (EP-01..EP-07) angegeben.

```json
{
  "codes": {
    "FS": ["FS-001"],
    "UC": ["UC-001", "UC-002"],
    "DT": ["DT-002"],
    "CH": ["CH-001"],
    "IM": ["IM-001"],
    "RS": ["RS-001", "RS-003"],
    "OB": ["OB-001"],
    "LG": ["LG-001", "LG-002", "LG-008", "LG-009"]
  }
}
```

### Evidence-Dateiliste

Jeder Eintrag identifiziert ein Dokument im Pack durch **file_id** (EP-01..EP-07). Optional kann **ev_codes** Taxonomy-LG-Codes (LG-xxx) auflisten, die das Dokument unterstützt.

```json
{
  "evidence_files": [
    {
      "file_id": "EP-01",
      "filename": "EP-01_system_overview.md",
      "title": "Systemübersicht",
      "required": true
    }
  ]
}
```

## Template-Struktur

Jedes Evidence-Template enthält:

1. **Obligatorischer Metadatenblock** - pack_id, version, taxonomy_version, Daten, owner
2. **AIMO Codes-Tabelle** - Alle 8 Dimensionen mit anwendbaren Codes
3. **Inhaltsabschnitte** - Domänenspezifische Dokumentationsabschnitte
4. **Referenzen** - Links zu verwandtem Evidence
5. **Revisionshistorie** - Änderungsverfolgung

### Template-Header-Beispiel

```markdown
# EP-01: Systemübersicht

---

## Obligatorische Metadaten

| Feld | Wert |
| --- | --- |
| **pack_id** | `EP-EXAMPLE-001` |
| **pack_version** | `0.1.0` |
| **taxonomy_version** | `0.1.0` |
| **created_date** | `2026-01-31` |
| **last_updated** | `2026-01-31` |
| **owner** | `AI Governance Team` |

---

## AIMO Codes (8 Dimensionen)

| Dimension | Code(s) | Label |
| --- | --- | --- |
| **FS** | `FS-001` | Endbenutzer-Produktivität |
| **UC** | `UC-001` | Allgemeine F&A |
| **DT** | `DT-002` | Intern |
| **CH** | `CH-001` | Web-UI |
| **IM** | `IM-001` | Standalone |
| **RS** | `RS-001` | Datenleck |
| **OB** | `OB-001` | Effizienz |
| **LG** | `LG-001`, `LG-002` | Antragsdatensatz, Prüf-/Genehmigungsdatensatz |
```

## Downloads

### Templates

Evidence Pack-Templates sind im Repository verfügbar. Verwenden Sie **file_id** EP-01..EP-07 im Manifest; Dateinamen können EP-01_... oder legacy EV-01_... zur Abwärtskompatibilität sein.

- `source_pack/04_evidence_pack/templates/EV-01_system_overview.md` → file_id **EP-01**
- `source_pack/04_evidence_pack/templates/EV-02_data_flow.md` → file_id **EP-02**
- `source_pack/04_evidence_pack/templates/EV-03_inventory.md` → file_id **EP-03**
- `source_pack/04_evidence_pack/templates/EV-04_risk_impact.md` → file_id **EP-04**
- `source_pack/04_evidence_pack/templates/EV-05_controls_approvals.md` → file_id **EP-05**
- `source_pack/04_evidence_pack/templates/EV-06_logging_monitoring.md` → file_id **EP-06**
- `source_pack/04_evidence_pack/templates/EV-07_incident_exception.md` → file_id **EP-07**

### Schemas und Beispiele

- Schema: `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json`
- Beispiel: `source_pack/04_evidence_pack/examples/evidence_pack_manifest.example.json`

Siehe [Releases](../../releases/index.md) für herunterladbare Pakete.

## Distributionsmodell

> **Hinweis**: Die primären Distributionsziele sind **Wirtschaftsprüfungsgesellschaften und Systemintegratoren** (Template-Distributoren), nicht einzelne Unternehmen.

Die Templates sind darauf ausgelegt:

1. Von Prüfern und Beratern als Standard-Artefakte übernommen zu werden
2. An Unternehmen mit beibehaltener Quellenangabe verteilt zu werden
3. Neben dem AIMO Standard versioniert zu werden

Unternehmen erhalten Templates über ihre Prüfer, Berater oder internen Governance-Teams, die die Verknüpfung zur Standard-Version pflegen.

## Referenzen

- [Taxonomie](./03-taxonomy.md) - Dimensionsdefinitionen
- [Codes](./04-codes.md) - Code-Format
- [Validator](./07-validator.md) - Validierungsregeln
- [Evidence Bundle](../../artifacts/evidence-bundle.md) - Bundle-Struktur
