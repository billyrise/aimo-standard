---
description: Template e guida all'uso dell'Evidence Pack AIMO. Struttura per documentare l'evidence di governance dell'IA con gestione dell'indice e formattazione pronta per l'audit.
---

# Template EV

Questa sezione definisce i template dell'Evidence Pack e il loro utilizzo. Un Evidence Pack è una raccolta di documentazione che dimostra governance e conformità per un sistema IA.

## Principio Chiave: Gestione dell'Indice e delle Differenze

> **Importante**: Ciò che conta non è il contenuto delle singole submission, ma la **gestione dell'indice** e delle **differenze** tra gli elementi di evidence.

Un Evidence Pack serve come indice che collega i sistemi IA ai loro artefatti di governance. Il valore sta in:

1. **Tracciabilità**: Collegare decisioni, approvazioni e modifiche nel tempo
2. **Verificabilità**: Abilitare gli auditor a navigare la struttura dell'evidence
3. **Manutenibilità**: Tracciare cosa è cambiato, quando e perché

## Set di Evidence MVP (EV-01 a EV-07)

I seguenti sette tipi di evidence formano il **set minimo vitale** per dimostrare la governance dell'IA:

| ID | Tipo di Evidence | Codice | Scopo |
| --- | --- | --- | --- |
| EV-01 | Panoramica del Sistema | EV-001 | Documentare il sistema IA e il suo scopo |
| EV-02 | Flusso dei Dati | EV-002 | Mappare il movimento dei dati attraverso il sistema |
| EV-03 | Inventario | EV-003 | Mantenere il catalogo degli asset IA |
| EV-04 | Valutazione Rischi & Impatto | EV-004 | Valutare e documentare i rischi |
| EV-05 | Controlli & Approvazioni | EV-005 | Documentare controlli e record di approvazione |
| EV-06 | Logging & Monitoraggio | EV-006 | Definire la configurazione di logging e monitoraggio |
| EV-07 | Incidenti & Eccezioni | EV-007 | Tracciare incidenti ed eccezioni |

## Manifest dell'Evidence Pack

Ogni Evidence Pack DEVE includere un file manifest contenente:

### Metadati Obbligatori

| Campo | Descrizione | Richiesto |
| --- | --- | --- |
| `pack_id` | Identificatore univoco (es. EP-EXAMPLE-001) | Sì |
| `pack_version` | Versione SemVer del pack | Sì |
| `taxonomy_version` | Versione della tassonomia AIMO usata | Sì |
| `created_date` | Data di creazione del pack | Sì |
| `last_updated` | Data dell'ultimo aggiornamento | Sì |
| `owner` | Parte responsabile | Sì |

### Codici AIMO (8 Dimensioni)

Ogni Evidence Pack DEVE includere codici da tutte le 8 dimensioni:

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

### Lista dei File di Evidence

```json
{
  "evidence_files": [
    {
      "file_id": "EV-01",
      "filename": "EV-01_system_overview.md",
      "ev_type": "EV-001",
      "title": "System Overview",
      "required": true
    }
  ]
}
```

## Struttura del Template

Ogni template di evidence include:

1. **Blocco di Metadati Obbligatori** - pack_id, versione, taxonomy_version, date, owner
2. **Tabella Codici AIMO** - Tutte le 8 dimensioni con codici applicabili
3. **Sezioni di Contenuto** - Sezioni di documentazione specifiche per dominio
4. **Riferimenti** - Link a evidence correlata
5. **Cronologia delle Revisioni** - Tracciamento delle modifiche

### Esempio di Header del Template

```markdown
# EV-01: Panoramica del Sistema

---

## Metadati Obbligatori

| Campo | Valore |
| --- | --- |
| **pack_id** | `EP-EXAMPLE-001` |
| **pack_version** | `0.1.0` |
| **taxonomy_version** | `0.1.0` |
| **created_date** | `2026-01-31` |
| **last_updated** | `2026-01-31` |
| **owner** | `AI Governance Team` |

---

## Codici AIMO (8 Dimensioni)

| Dimensione | Codice/i | Etichetta |
| --- | --- | --- |
| **FS** | `FS-001` | End-user Productivity |
| **UC** | `UC-001` | General Q&A |
| **DT** | `DT-002` | Internal |
| **CH** | `CH-001` | Web UI |
| **IM** | `IM-001` | Standalone |
| **RS** | `RS-001` | Data Leakage |
| **OB** | `OB-001` | Efficiency |
| **EV** | `EV-001` | System Overview |
```

## Download

### Template

I template dell'Evidence Pack sono disponibili in:

- `source_pack/04_evidence_pack/templates/EV-01_system_overview.md`
- `source_pack/04_evidence_pack/templates/EV-02_data_flow.md`
- `source_pack/04_evidence_pack/templates/EV-03_inventory.md`
- `source_pack/04_evidence_pack/templates/EV-04_risk_impact.md`
- `source_pack/04_evidence_pack/templates/EV-05_controls_approvals.md`
- `source_pack/04_evidence_pack/templates/EV-06_logging_monitoring.md`
- `source_pack/04_evidence_pack/templates/EV-07_incident_exception.md`

### Schemi ed Esempi

- Schema: `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json`
- Esempio: `source_pack/04_evidence_pack/examples/evidence_pack_manifest.example.json`

Vedere [Release](../../releases/index.md) per pacchetti scaricabili.

## Modello di Distribuzione

> **Nota**: I target di distribuzione primari sono **società di audit e system integrator** (distributori di template), non singole aziende.

I template sono progettati per essere:

1. Adottati da auditor e consulenti come artefatti standard
2. Distribuiti alle aziende con attribuzione della fonte preservata
3. Versionati insieme allo Standard AIMO

Le aziende ricevono i template tramite i loro auditor, consulenti o team di governance interni che mantengono il collegamento alla versione dello standard.

## Riferimenti

- [Tassonomia](./03-taxonomy.md) - Definizioni delle dimensioni
- [Codici](./04-codes.md) - Formato dei codici
- [Validator](./07-validator.md) - Regole di validazione
- [Evidence Bundle](../../artifacts/evidence-bundle.md) - Struttura del bundle
