---
description: Formato e convenzioni di denominazione del Code System AIMO. Definisce la struttura dei codici (XX-NNN), stati del ciclo di vita, versionamento e politiche di deprecazione per i codici della tassonomia.
---

# Codici

Questa pagina definisce il formato del Code System AIMO, le convenzioni di denominazione e la gestione del ciclo di vita.

## Formato dei Codici

Tutti i codici AIMO seguono il formato: **`<PREFIX>-<TOKEN>`**

| Componente | Descrizione | Formato | Esempio |
| --- | --- | --- | --- |
| `<PREFIX>` | Identificatore della dimensione | 2 lettere maiuscole | FS, UC, DT |
| `-` | Separatore | Trattino | - |
| `<TOKEN>` | Token univoco all'interno della dimensione | 3 cifre (zero-padded) | 001, 002, 003 |

### Esempi

- `FS-001` - Functional Scope: End-user Productivity
- `UC-005` - Use Case Class: Code Generation
- `DT-004` - Data Type: Personal Data
- `CH-003` - Channel: IDE Plugin
- `IM-002` - Integration Mode: SaaS Integrated
- `RS-001` - Risk Surface: Data Leakage
- `OB-001` - Outcome/Benefit: Efficiency
- `LG-001` - Log/Event Type: Request Record

## Namespace

La tassonomia AIMO utilizza 8 namespace dimensionali:

| ID | Nome | Prefisso | Conteggio Codici |
| --- | --- | --- | --- |
| **FS** | Functional Scope | `FS-` | 6 |
| **UC** | Use Case Class | `UC-` | 30 |
| **DT** | Data Type | `DT-` | 10 |
| **CH** | Channel | `CH-` | 8 |
| **IM** | Integration Mode | `IM-` | 7 |
| **RS** | Risk Surface | `RS-` | 8 |
| **OB** | Outcome / Benefit | `OB-` | 7 |
| **LG** | Log/Event Type | `LG-` | 15 |

**Totale: 91 codici in 8 dimensioni**

### Regole del Namespace

1. **Il prefisso è fisso**: Il prefisso a due lettere della dimensione (FS, UC, ecc.) è permanente e non cambierà mai.
2. **Zero-padding**: I token sono sempre 3 cifre, zero-padded (es. `001` non `1`).
3. **Assegnazione sequenziale**: Nuovi codici sono assegnati al prossimo numero disponibile all'interno di una dimensione.
4. **Nessun riutilizzo**: I codici rimossi non vengono mai riassegnati a significati diversi.

## Regole di Stabilità

La stabilità dei codici è un principio critico per la tracciabilità dell'audit.

### Immutabilità dell'ID

- **Gli ID dei codici sono immutabili** — una volta assegnato, un ID codice non cambia mai significato
- Un codice come `UC-001` significherà sempre "General Q&A" per il suo intero ciclo di vita
- Se il significato deve cambiare, viene creato un nuovo codice

### Politica di Non Riutilizzo

- I codici deprecati o rimossi non vengono **mai riassegnati** a significati diversi
- Questo assicura che l'evidence storica rimanga valida e tracciabile
- Esempio: Se `UC-010` viene deprecato, un nuovo caso d'uso ottiene `UC-031` (non `UC-010`)

### Deprecazione Prima della Rimozione

- I codici devono essere marcati come `deprecated` per almeno una versione MINOR prima della rimozione
- La rimozione avviene solo in incrementi di versione MAJOR
- Vedere la sezione [Ciclo di Vita](#ciclo-di-vita) per i dettagli

## Uso

### Dimensioni Richieste

Per ogni sistema IA o caso d'uso, DEVI specificare almeno un codice da ogni dimensione richiesta:

| Dimensione | Selezione | Note |
| --- | --- | --- |
| FS | Esattamente 1 | Funzione aziendale primaria |
| UC | 1 o più | Tipi di attività eseguite |
| DT | 1 o più | Classificazioni dei dati |
| CH | 1 o più | Canali di accesso |
| IM | Esattamente 1 | Modalità di integrazione |
| RS | 1 o più | Categorie di rischio |
| LG | 1 o più | Tipi di log/evento |

### Dimensioni Opzionali

| Dimensione | Selezione | Note |
| --- | --- | --- |
| OB | 0 o più | Benefici attesi (opzionale) |

### Composizione dei Codici

Quando si documenta un sistema IA, i codici da più dimensioni vengono combinati. La **priorità di composizione** determina l'ordine quando si elencano i codici:

1. FS (Functional Scope)
2. UC (Use Case Class)
3. DT (Data Type)
4. CH (Channel)
5. IM (Integration Mode)
6. RS (Risk Surface)
7. OB (Outcome / Benefit)
8. LG (Log/Event Type)

**Esempio di composizione:**

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

## Ciclo di Vita

### Valori di Stato

| Stato | Descrizione | Comportamento del Validator |
| --- | --- | --- |
| `active` | Attualmente valido e in uso | Accettato |
| `deprecated` | Ancora valido ma programmato per la rimozione | Accettato con avviso |
| `removed` | Non più valido; non usare | Rifiutato |

### Campi di Metadati del Ciclo di Vita

Il dizionario traccia il ciclo di vita con questi campi:

| Campo | Richiesto | Descrizione | Esempio |
| --- | --- | --- | --- |
| `status` | Sì | Stato corrente | `active` |
| `introduced_in` | Sì | Versione quando il codice è stato aggiunto | `0.1.0` |
| `deprecated_in` | No | Versione quando marcato deprecato | `1.2.0` |
| `removed_in` | No | Versione quando rimosso | `2.0.0` |
| `replaced_by` | No | Codice/i di sostituzione | `UC-015` |
| `backward_compatible` | Sì | Se la modifica rompe l'uso esistente | `true` |

### Regole di Deprecazione

1. I codici DEVONO essere marcati `deprecated` per almeno una versione MINOR prima della rimozione
2. I codici deprecati includono la versione `deprecated_in` e `replaced_by` se applicabile
3. La rimozione avviene solo in incrementi di versione MAJOR
4. I codici deprecati rimangono validi per la retrocompatibilità durante il periodo di deprecazione

**Esempio di timeline:**

| Versione | Stato | Azione |
| --- | --- | --- |
| 0.1.0 | `active` | Codice `UC-010` introdotto |
| 1.2.0 | `deprecated` | Marcato deprecato, `replaced_by: UC-031` |
| 2.0.0 | `removed` | Non più accettato dal validator |

### Versionamento

Le modifiche ai codici seguono [Semantic Versioning](./08-changelog.md):

- **MAJOR**: Rimozione di codici o modifiche breaking
- **MINOR**: Nuovi codici aggiunti, codici deprecati
- **PATCH**: Solo chiarimenti alle definizioni (nessuna modifica strutturale)

### Retrocompatibilità

Il campo `backward_compatible` indica se una modifica rompe l'uso esistente:

| Valore | Significato |
| --- | --- |
| `true` | L'evidence esistente che usa questo codice rimane valida |
| `false` | L'evidence esistente potrebbe necessitare aggiornamenti (modifica versione MAJOR) |

## Validazione

Il validator controlla:

1. Tutte le dimensioni richieste hanno almeno un codice
2. Le dimensioni a selezione singola hanno esattamente un codice
3. Tutti i codici esistono nel dizionario della tassonomia corrente
4. Il formato del codice corrisponde al pattern `<PREFIX>-<TOKEN>` (es. `UC-001`)
5. I codici deprecati sono segnalati con avvisi

Vedere [Validator](./07-validator.md) per i dettagli dell'implementazione.

## Riferimento SSOT

!!! info "Fonte di Verità"
    La definizione autorevole è `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv`. Questa pagina è esplicativa. Vedere [Guida alla Localizzazione](../../contributing/localization.md) per i workflow di aggiornamento.

## Pagine Correlate

- [Tassonomia](./03-taxonomy.md) - Definizioni complete delle dimensioni
- [Dizionario](./05-dictionary.md) - Liste complete dei codici e definizioni delle colonne
- [Validator](./07-validator.md) - Regole di validazione
- [Changelog](./08-changelog.md) - Cronologia delle versioni
