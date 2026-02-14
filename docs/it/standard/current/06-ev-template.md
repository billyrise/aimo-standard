---
description: Template e guida all'uso dell'Evidence Pack AIMO. Struttura per documentare l'evidence di governance dell'IA con gestione dell'indice e formattazione pronta per l'audit.
---

# Template Evidence Pack (EP)

Questa sezione definisce i template dell'Evidence Pack e il loro utilizzo. Un Evidence Pack è una raccolta di documentazione che dimostra governance e conformità per un sistema IA.

## Namespace: tipi di documento Evidence Pack (EP) vs Taxonomy Log/Event Type (LG)

> **Importante**: **EP-01..EP-07** identificano i *tipi di documento* (tipi di file Evidence Pack). **LG-001, LG-002, …** nella [Tassonomia](./03-taxonomy.md) identificano i *tipi di log/registro* (Request Record, Review/Approval Record, ecc.). **EV-** riservato per ID artefatti Evidence. Usare EP per la struttura del pack e LG per la classificazione dell'evidence del ciclo di vita.

## Principio Chiave: Gestione dell'Indice e delle Differenze

Ciò che conta non è solo il contenuto delle singole submission, ma la **gestione dell'indice** e delle **differenze** tra gli elementi di evidence.

Un Evidence Pack serve come indice che collega i sistemi IA ai loro artefatti di governance. Il valore sta in:

1. **Tracciabilità**: Collegare decisioni, approvazioni e modifiche nel tempo
2. **Verificabilità**: Abilitare gli auditor a navigare la struttura dell'evidence
3. **Manutenibilità**: Tracciare cosa è cambiato, quando e perché

## Set di Evidence MVP (EP-01 a EP-07)

I seguenti sette **tipi di documento Evidence Pack** (EP) formano il **set minimo vitale** per dimostrare la governance dell'IA. Ciascuno è un template di documento; i codici **LG** della tassonomia (Request Record, Review/Approval, ecc.) sono usati altrove nel bundle e in `codes.LG` per classificare l'evidence di *log/registro*.

| ID | Tipo di documento | Scopo |
| --- | --- | --- |
| EP-01 | Panoramica del Sistema | Documentare il sistema IA e il suo scopo |
| EP-02 | Flusso dei Dati | Mappare il movimento dei dati attraverso il sistema |
| EP-03 | Inventario | Mantenere il catalogo degli asset IA |
| EP-04 | Valutazione Rischi & Impatto | Valutare e documentare i rischi |
| EP-05 | Controlli & Approvazioni | Documentare controlli e record di approvazione |
| EP-06 | Logging & Monitoraggio | Definire la configurazione di logging e monitoraggio |
| EP-07 | Incidenti & Eccezioni | Tracciare incidenti ed eccezioni |

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

Ogni Evidence Pack DEVE includere codici da tutte le 8 dimensioni. La dimensione **LG** elenca i tipi di log/registro *tassonomia* (es. Request Record, Review/Approval) applicabili a questo pack—non i codici di tipo di documento. Il tipo di documento è dato da `evidence_files[].file_id` (EP-01..EP-07).

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

### Lista dei File di Evidence

Ogni voce identifica un documento nel pack tramite **file_id** (EP-01..EP-07). Opzionalmente **ev_codes** può elencare i codici LG di tassonomia (LG-xxx) supportati dal documento.

```json
{
  "evidence_files": [
    {
      "file_id": "EP-01",
      "filename": "EP-01_system_overview.md",
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
# EP-01: Panoramica del Sistema

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
| **LG** | `LG-001`, `LG-002` | Request Record, Review/Approval Record |
```

## Download

### Template

I template dell'Evidence Pack sono disponibili nel repository. Usare **file_id** EP-01..EP-07 nel manifest; i nomi file possono essere EP-01_... o legacy EV-01_... per compatibilità.

- `source_pack/04_evidence_pack/templates/EV-01_system_overview.md` → file_id **EP-01**
- `source_pack/04_evidence_pack/templates/EV-02_data_flow.md` → file_id **EP-02**
- `source_pack/04_evidence_pack/templates/EV-03_inventory.md` → file_id **EP-03**
- `source_pack/04_evidence_pack/templates/EV-04_risk_impact.md` → file_id **EP-04**
- `source_pack/04_evidence_pack/templates/EV-05_controls_approvals.md` → file_id **EP-05**
- `source_pack/04_evidence_pack/templates/EV-06_logging_monitoring.md` → file_id **EP-06**
- `source_pack/04_evidence_pack/templates/EV-07_incident_exception.md` → file_id **EP-07**

### Schemi ed Esempi

- Schema: `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json`
- Esempio: `source_pack/04_evidence_pack/examples/evidence_pack_manifest.example.json`

Vedere [Release](../../../releases/) per pacchetti scaricabili.

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
