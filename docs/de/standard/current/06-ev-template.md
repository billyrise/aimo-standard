---
description: AIMO Evidence Pack-Templates und Nutzungsleitfaden. Struktur zur Dokumentation von KI-Governance-Evidence mit Index-Management und prüfungsbereiter Formatierung.
---

# EV-Template

Dieser Abschnitt definiert die Evidence Pack-Templates und deren Verwendung. Ein Evidence Pack ist eine Sammlung von Dokumentation, die Governance und Compliance für ein KI-System nachweist.

## Grundprinzip: Index- und Diff-Management

> **Wichtig**: Was zählt, ist nicht der Inhalt einzelner Einreichungen, sondern das **Index**- und **Diff-Management** über Evidence-Elemente hinweg.

Ein Evidence Pack dient als Index, der KI-Systeme mit ihren Governance-Artefakten verknüpft. Der Wert liegt in:

1. **Nachverfolgbarkeit**: Verknüpfung von Entscheidungen, Genehmigungen und Änderungen über die Zeit
2. **Auditierbarkeit**: Ermöglichung für Prüfer, durch die Evidence-Struktur zu navigieren
3. **Wartbarkeit**: Verfolgung, was sich wann und warum geändert hat

## MVP Evidence Set (EV-01 bis EV-07)

Die folgenden sieben Evidence-Typen bilden das **minimale viable Set** zum Nachweis von KI-Governance:

| ID | Evidence-Typ | Code | Zweck |
| --- | --- | --- | --- |
| EV-01 | Systemübersicht | EV-001 | KI-System und seinen Zweck dokumentieren |
| EV-02 | Datenfluss | EV-002 | Datenbewegung durch das System abbilden |
| EV-03 | Inventar | EV-003 | Katalog von KI-Assets pflegen |
| EV-04 | Risiko- & Auswirkungsbewertung | EV-004 | Risiken bewerten und dokumentieren |
| EV-05 | Kontrollen & Genehmigungen | EV-005 | Kontrollen und Genehmigungsdatensätze dokumentieren |
| EV-06 | Logging & Monitoring | EV-006 | Logging- und Monitoring-Setup definieren |
| EV-07 | Incident & Ausnahme | EV-007 | Incidents und Ausnahmen verfolgen |

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

Jedes Evidence Pack MUSS Codes aus allen 8 Dimensionen enthalten:

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
    "EV": ["EV-001", "EV-002", "EV-003", "EV-004", "EV-005", "EV-006", "EV-007"]
  }
}
```

### Evidence-Dateiliste

```json
{
  "evidence_files": [
    {
      "file_id": "EV-01",
      "filename": "EV-01_system_overview.md",
      "ev_type": "EV-001",
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
# EV-01: Systemübersicht

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
| **EV** | `EV-001` | Systemübersicht |
```

## Downloads

### Templates

Evidence Pack-Templates sind verfügbar in:

- `source_pack/04_evidence_pack/templates/EV-01_system_overview.md`
- `source_pack/04_evidence_pack/templates/EV-02_data_flow.md`
- `source_pack/04_evidence_pack/templates/EV-03_inventory.md`
- `source_pack/04_evidence_pack/templates/EV-04_risk_impact.md`
- `source_pack/04_evidence_pack/templates/EV-05_controls_approvals.md`
- `source_pack/04_evidence_pack/templates/EV-06_logging_monitoring.md`
- `source_pack/04_evidence_pack/templates/EV-07_incident_exception.md`

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
