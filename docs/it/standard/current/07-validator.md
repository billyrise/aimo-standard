---
description: Validator AIMO - Assicura che gli Evidence Pack siano conformi agli schemi dello Standard AIMO. Regole di validazione, gestione degli errori e implementazione di riferimento per controlli di conformità.
---

# Validator

Il Validator AIMO assicura che gli Evidence Pack e gli artefatti correlati siano conformi agli schemi e ai requisiti dello Standard AIMO.

Vedere anche: [Protocollo di Supervisione Umana](../../governance/human-oversight-protocol.md) — confine di responsabilità per revisione macchina vs. umana.

## Validator in pratica

Per un quickstart di 30 secondi (installazione, esecuzione, interpretazione dell'output), vedere [Hub del Validator](../../validator/index.md).

## Requisiti MVP del Validator

Il validator minimo vitale DEVE eseguire i seguenti controlli:

### 1. Validazione dei Campi Richiesti

Controllare che tutti i campi obbligatori siano presenti:

| Artefatto | Campi Richiesti |
| --- | --- |
| Manifest Evidence Pack | pack_id, pack_version, taxonomy_version, created_date, last_updated, codes, evidence_files |
| Oggetto Codes | FS, UC, DT, CH, IM, RS, EV (OB opzionale) |
| Voce File Evidence | file_id, filename, ev_type, title |

### 2. Validazione Codici Dimensione

Controllare che ogni dimensione richiesta abbia almeno un codice:

| Dimensione | Requisito |
| --- | --- |
| FS (Functional Scope) | Esattamente 1 codice |
| UC (Use Case Class) | Almeno 1 codice |
| DT (Data Type) | Almeno 1 codice |
| CH (Channel) | Almeno 1 codice |
| IM (Integration Mode) | Esattamente 1 codice |
| RS (Risk Surface) | Almeno 1 codice |
| OB (Outcome / Benefit) | Opzionale (0 o più) |
| EV (Evidence Type) | Almeno 1 codice |

### 3. Controllo Esistenza nel Dizionario

Validare che tutti i codici esistano nel dizionario della tassonomia:

- Caricare il dizionario della tassonomia per la `taxonomy_version` specificata
- Verificare che ogni codice nel manifest esista nel dizionario
- Riportare codici non validi con la loro dimensione e valore

### 4. Validazione Formato Codice

Controllare che tutti i codici corrispondano al formato atteso:

```regex
^(FS|UC|DT|CH|IM|RS|OB|EV)-\d{3}$
```

### 5. Validazione Schema

Validare contro JSON Schemas:

| Schema | Scopo |
| --- | --- |
| `evidence_pack_manifest.schema.json` | Manifest Evidence Pack |
| `taxonomy_pack.schema.json` | Definizioni taxonomy pack |
| `changelog.schema.json` | Voci del changelog |

## Regole di Validazione

### Regola: Dimensioni Richieste

```yaml
rule_id: required_dimensions
description: Tutte le dimensioni richieste devono avere almeno un codice
severity: error
check: |
  - FS: esattamente 1
  - UC: almeno 1
  - DT: almeno 1
  - CH: almeno 1
  - IM: esattamente 1
  - RS: almeno 1
  - EV: almeno 1
```

### Regola: Codici Validi

```yaml
rule_id: valid_codes
description: Tutti i codici devono esistere nel dizionario della tassonomia
severity: error
check: |
  Per ogni codice in manifest.codes:
    - Il codice esiste nel dizionario per la taxonomy_version specificata
    - Lo stato del codice è 'active' (avviso se 'deprecated')
```

### Regola: Formato Codice

```yaml
rule_id: code_format
description: Tutti i codici devono corrispondere al formato standard
severity: error
pattern: "^(FS|UC|DT|CH|IM|RS|OB|EV)-\\d{3}$"
```

### Regola: Formato Versione

```yaml
rule_id: version_format
description: Le versioni devono essere SemVer validi
severity: error
pattern: "^\\d+\\.\\d+\\.\\d+$"
fields:
  - pack_version
  - taxonomy_version
```

## Formato Output Errori

Gli errori di validazione sono riportati nel seguente formato:

```
<path>: <severity>: <message>
```

**Esempi:**

```
codes.FS: error: La dimensione richiesta 'FS' non ha codici
codes.UC[0]: error: Il codice 'UC-999' non esiste nel dizionario v0.1.0
pack_version: error: Formato versione non valido 'v1.0' (atteso SemVer)
codes.RS[1]: warning: Il codice 'RS-002' è deprecato in v0.2.0
```

## Cosa il Validator NON Controlla

Il validator si concentra sulla conformità strutturale, non sulla qualità del contenuto:

| Aspetto | Motivo |
| --- | --- |
| Accuratezza del contenuto | Il validator controlla la struttura, non il significato |
| Completezza dell'evidence | I template sono guide, non formati imposti |
| Risoluzione dei riferimenti incrociati | L'esistenza dei file non è verificata |
| Validità timestamp | ISO-8601 non è strettamente validato |
| Unicità ID | Non attualmente imposta |
| Hash di integrità | Responsabilità dell'adottante |

## Implementazione di Riferimento

Un'implementazione di riferimento è fornita in Python:

```
validator/src/validate.py
```

### Utilizzo

```bash
python validator/src/validate.py <manifest.json>
```

### Esempio di Output

```
Validating: evidence_pack_manifest.json
Taxonomy version: 0.1.0

Checking required dimensions...
  FS: OK (1 codice)
  UC: OK (3 codici)
  DT: OK (1 codice)
  CH: OK (1 codice)
  IM: OK (1 codice)
  RS: OK (3 codici)
  OB: OK (2 codici)
  EV: OK (7 codici)

Checking code validity...
  Tutti i codici validi.

Validation: PASSED
```

## Politica di Versionamento

Le regole del validator seguono SemVer:

- **MAJOR**: Modifiche alle regole breaking (nuovi controlli richiesti che fanno fallire pack validi esistenti)
- **MINOR**: Nuovi controlli opzionali, avvisi o messaggi informativi
- **PATCH**: Bug fix che non cambiano i risultati della validazione

## Riferimenti Schema

| Schema | Posizione |
| --- | --- |
| Evidence Pack Manifest | `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json` |
| Taxonomy Pack | `source_pack/03_taxonomy/schemas/taxonomy_pack.schema.json` |
| Changelog | `source_pack/03_taxonomy/schemas/changelog.schema.json` |

## Riferimenti

- [Tassonomia](./03-taxonomy.md) - Definizioni delle dimensioni
- [Codici](./04-codes.md) - Formato dei codici
- [Dizionario](./05-dictionary.md) - Dizionario dei codici
- [Regole del Validator](../../validator/index.md) - Documentazione completa delle regole
