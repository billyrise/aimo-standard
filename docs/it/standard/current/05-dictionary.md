---
description: Dizionario AIMO - Lista autorevole di 91 codici della tassonomia in 8 dimensioni. Definizioni complete, etichette e informazioni sul ciclo di vita per la classificazione dell'IA.
---

# Dizionario

Il Dizionario AIMO è la lista autorevole di tutti i codici validi all'interno della tassonomia. Fornisce definizioni complete per ogni codice incluse etichette, descrizioni e informazioni sul ciclo di vita.

## Cos'è il Dizionario

Il dizionario fornisce un set completo e leggibile da macchina di tutti i codici della tassonomia AIMO. Contiene:

- Tutti i 91 codici in 8 dimensioni
- Etichette e definizioni (con traduzioni nei language pack)
- Metadati del ciclo di vita (stato, versione introdotto, deprecato, rimosso)
- Note sull'ambito ed esempi per l'uso dei codici

Il dizionario abilita:

1. **Template di Evidence**: I codici sono usati nei template EV per classificare i sistemi IA
2. **Validator**: Il validator controlla che tutti i codici esistano nel dizionario
3. **Coverage Map**: I codici abilitano la mappatura verso framework e normative esterne

!!! info "Single Source of Truth (SSOT)"
    La SSOT per il dizionario è:

    - **Struttura**: `data/taxonomy/canonical.yaml` (codici, stato, ciclo di vita)
    - **Traduzioni**: `data/taxonomy/i18n/*.yaml` (etichette, definizioni per lingua)

    I file CSV sono **artefatti generati** per la distribuzione. Vedere [Release](../../../releases/) per i download.

## Schema delle Colonne

Il dizionario canonico utilizza **18 colonne** (struttura neutrale rispetto alla lingua):

### Colonne di Identificazione (5)

| # | Colonna | Richiesta | Descrizione | Esempio |
| --- | --- | --- | --- | --- |
| 1 | `standard_id` | Sì | Identificatore dello standard | `AIMO-STD` |
| 2 | `standard_version` | Sì | Formato SemVer | `0.1.0` |
| 3 | `dimension_id` | Sì | ID dimensione a due lettere | `FS`, `UC`, `DT` |
| 4 | `dimension_name` | Sì | Nome della dimensione | `Functional Scope` |
| 5 | `code` | Sì | Codice completo | `UC-001` |

### Colonne di Etichetta e Definizione (4)

| # | Colonna | Richiesta | Descrizione | Esempio |
| --- | --- | --- | --- | --- |
| 6 | `label` | Sì | Etichetta del codice (max 50 caratteri) | `General Q&A` |
| 7 | `definition` | Sì | Definizione del codice (1-2 frasi) | `General question answering...` |
| 8 | `scope_notes` | No | Chiarimento sull'ambito d'uso | `Low to medium risk...` |
| 9 | `examples` | No | Esempi separati da pipe | `chatbot\|recommendation` |

!!! note "Traduzioni"
    Il modello dati canonico separa le traduzioni in language pack (`data/taxonomy/i18n/*.yaml`). Ogni language pack fornisce valori localizzati per `dimension_name`, `label` e `definition`. Vedere [Guida alla Localizzazione](../../../contributing/localization/) per i dettagli.

### Colonne del Ciclo di Vita (6)

| # | Colonna | Richiesta | Descrizione | Esempio |
| --- | --- | --- | --- | --- |
| 10 | `status` | Sì | `active`, `deprecated`, `removed` | `active` |
| 11 | `introduced_in` | Sì | Versione quando aggiunto | `0.1.0` |
| 12 | `deprecated_in` | No | Versione quando deprecato | `1.2.0` |
| 13 | `removed_in` | No | Versione quando rimosso | `2.0.0` |
| 14 | `replaced_by` | No | Codice di sostituzione | `UC-015` |
| 15 | `backward_compatible` | Sì | `true` o `false` | `true` |

### Colonne di Governance (3)

| # | Colonna | Richiesta | Descrizione | Esempio |
| --- | --- | --- | --- | --- |
| 16 | `references` | No | Riferimenti esterni | ISO/IEC 42001 |
| 17 | `owner` | No | Parte responsabile | `AIMO WG` |
| 18 | `last_reviewed_date` | No | Ultima revisione (YYYY-MM-DD) | `2026-01-19` |

## Voci Iniziali

La versione corrente del dizionario è **v0.1.0** e contiene:

| Dimensione | Nome | Codici Attivi | Deprecati | Totale |
| --- | --- | --- | --- | --- |
| FS | Functional Scope | 6 | 0 | 6 |
| UC | Use Case Class | 30 | 0 | 30 |
| DT | Data Type | 10 | 0 | 10 |
| CH | Channel | 8 | 0 | 8 |
| IM | Integration Mode | 7 | 0 | 7 |
| RS | Risk Surface | 8 | 0 | 8 |
| OB | Outcome / Benefit | 7 | 0 | 7 |
| LG | Log/Event Type | 15 | 0 | 15 |
| **Totale** | | **91** | **0** | **91** |

!!! note "Liste Complete dei Codici"
    La lista completa dei 91 codici è disponibile negli artefatti CSV generati. Questa pagina di documentazione fornisce definizioni delle colonne e guida all'uso. Per definizioni dettagliate dei codici:

    - **Download**: Vedere [Release](../../../releases/) per i file CSV per lingua
    - **CSV per lingua**: `artifacts/taxonomy/current/{lang}/taxonomy_dictionary.csv`
    - **CSV legacy EN/JA misto**: `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` (congelato, solo per retrocompatibilità)

## Politica di Aggiornamento

### Aggiungere Nuovi Codici

1. Assegnare il prossimo numero disponibile all'interno della dimensione (es. `UC-031` dopo `UC-030`)
2. Impostare `status` su `active`
3. Impostare `introduced_in` sulla versione corrente
4. Impostare `backward_compatible` su `true`
5. Fornire etichetta e definizione (aggiungere traduzioni ai language pack)

### Modificare Codici Esistenti

| Tipo di Modifica | Permessa | Impatto sulla Versione |
| --- | --- | --- |
| Chiarimento della definizione | Sì | PATCH |
| Aggiornamento delle scope notes | Sì | PATCH |
| Cambio dell'etichetta (significato preservato) | Sì | MINOR |
| Cambio del significato | No | Creare nuovo codice invece |

### Deprecare Codici

1. Impostare `status` su `deprecated`
2. Impostare `deprecated_in` sulla versione corrente
3. Impostare `replaced_by` sul nuovo codice (se applicabile)
4. Il codice rimane funzionale per la retrocompatibilità
5. Documentare il motivo nelle scope_notes

### Rimuovere Codici

1. Deprecare per almeno una versione MINOR prima
2. Impostare `status` su `removed`
3. Impostare `removed_in` sulla versione MAJOR corrente
4. Il codice non è più valido per nuova evidence

### Politica di Compatibilità

| Azione | Impatto sulla Versione | Retrocompatibile |
| --- | --- | --- |
| Aggiungere nuovo codice | MINOR | Sì |
| Deprecare codice | MINOR | Sì |
| Chiarire definizione | PATCH | Sì |
| Rimuovere codice | MAJOR | No |
| Cambiare significato del codice | Non permesso | - |

## Come Usare

### Nei Template di Evidence

Ogni template EV include una tabella di codici a 8 dimensioni:

```markdown
## Codici AIMO (8 Dimensioni)

| Dimensione | Codice/i | Etichetta |
| --- | --- | --- |
| **FS** | `FS-001` | End-user Productivity |
| **UC** | `UC-001`, `UC-002` | General Q&A, Summarization |
| **DT** | `DT-002`, `DT-004` | Internal, Personal Data |
| **CH** | `CH-001` | Web UI |
| **IM** | `IM-002` | SaaS Integrated |
| **RS** | `RS-001`, `RS-003` | Data Leakage, Compliance Breach |
| **OB** | `OB-001` | Efficiency |
| **LG** | `LG-001`, `LG-002` | Request Record, Review/Approval Record |
```

### Nel Validator

Il validator controlla:

1. Tutti i codici referenziati nell'evidence esistono nel dizionario
2. Il formato del codice corrisponde al pattern atteso (`PREFIX-###`)
3. I codici deprecati attivano avvisi
4. I codici rimossi sono rifiutati

### Linee Guida per le Estensioni

Le organizzazioni POSSONO estendere il dizionario con codici personalizzati:

**Prefisso di Estensione:**

```
X-<ORG>-<DIM>-<TOKEN>
```

Esempio: `X-ACME-UC-901` per un codice di caso d'uso personalizzato di ACME Corporation.

**Regole di Estensione:**

1. I codici personalizzati NON DEVONO entrare in conflitto con i codici standard
2. I codici personalizzati DOVREBBERO essere documentati in un dizionario di estensione locale
3. Quando si scambia evidence con parti esterne, usare solo codici standard

## Download

Vedere [Release](../../../releases/) per pacchetti scaricabili contenenti il dizionario e file correlati.

## Pagine Correlate

- [Tassonomia](../03-taxonomy/) - Definizioni delle dimensioni e tabelle dei codici
- [Codici](../04-codes/) - Formato, denominazione e ciclo di vita dei codici
- [Template di Evidence](../06-ev-template/) - Come i codici sono usati nei template
- [Validator](../07-validator/) - Regole di validazione dei codici
- [Changelog](../08-changelog/) - Cronologia delle versioni
