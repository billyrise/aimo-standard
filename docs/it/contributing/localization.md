---
description: Guida alla localizzazione AIMO - struttura i18n, workflow di manutenzione e principi SSOT per la documentazione multilingue.
---

# Guida alla Localizzazione

Questa pagina documenta la struttura di localizzazione (i18n), il workflow di manutenzione e i principi SSOT (Single Source of Truth) per la documentazione dello Standard AIMO.

## Politica di Purezza Linguistica

**Ogni pagina linguistica dovrebbe contenere solo il contenuto di quella lingua.**

| Regola | Descrizione |
| --- | --- |
| **Pagine EN** | Non devono contenere caratteri CJK o riferimenti a colonne specifiche per lingua (es. suffissi `_ja`) |
| **Pagine JA** | Non devono spiegare terminologia specifica EN come se fosse la struttura canonica |
| **Eccezioni** | Elencate in `MIXED_LANGUAGE_ALLOWLIST` in `tooling/checks/lint_i18n.py` |

Questa politica assicura:
1. I lettori vedono solo la lingua selezionata
2. L'aggiunta di nuove lingue non richiede l'aggiornamento delle pagine esistenti
3. La CI può rilevare automaticamente le violazioni

## Struttura Linguistica

La documentazione dello Standard AIMO utilizza una **struttura i18n basata su cartelle**:

```
docs/
├── en/           # Inglese (canonico)
├── ja/           # Giapponese (日本語)
├── es/           # Spagnolo (Español)
├── fr/           # Francese (Français)
├── de/           # Tedesco (Deutsch)
├── pt/           # Portoghese (Português)
├── it/           # Italiano (Italiano)
├── zh/           # Cinese Semplificato (简体中文)
├── zh-TW/        # Cinese Tradizionale (繁體中文)
└── ko/           # Coreano (한국어)
```

- **L'inglese è canonico**: La cartella `docs/en/` è la fonte autorevole per il contenuto della documentazione.
- **Le altre lingue rispecchiano la struttura**: Ogni cartella linguistica (`ja/`, ecc.) mantiene la stessa struttura di file di `en/`.
- **Stessi nomi file**: Tutte le lingue usano l'estensione `.md` (nessun suffisso linguistico nei nomi file).
- **Fallback all'inglese**: Le traduzioni mancanti ricadono automaticamente sul contenuto inglese.

## Modello Dati della Tassonomia

La tassonomia utilizza una **struttura canonica neutrale rispetto alla lingua** con pack di traduzione separati:

```
data/
└── taxonomy/
    ├── canonical.yaml           # Neutrale rispetto alla lingua (codici, stato, ciclo di vita)
    └── i18n/
        ├── en.yaml              # Etichette e definizioni inglesi
        ├── ja.yaml              # Etichette e definizioni giapponesi
        └── {lang}.yaml          # Lingue aggiuntive (template vuoto)
```

### Struttura Canonica (`canonical.yaml`)

Contiene dati neutri rispetto alla lingua:

- Identificatori di codice (es. `FS-001`, `UC-001`)
- Stato (`active`, `deprecated`, `removed`)
- Metadati del ciclo di vita (`introduced_in`, `deprecated_in`, `removed_in`, `replaced_by`)
- Note sull'ambito ed esempi (in inglese, come riferimenti tecnici)

### Pack di Traduzione (`i18n/*.yaml`)

Ogni pack linguistico contiene:

- Nomi delle dimensioni (es. "Functional Scope")
- Etichette dei codici (es. "End-user Productivity")
- Definizioni dei codici

**Fallback**: Se manca una traduzione, il sistema usa l'inglese.

## Principio SSOT

AIMO utilizza un'**architettura SSOT-first** per i dati della tassonomia:

| Tipo di Asset | Posizione SSOT | Descrizione |
| --- | --- | --- |
| **Tassonomia (struttura)** | `data/taxonomy/canonical.yaml` | Struttura neutrale rispetto alla lingua (SSOT) |
| **Tassonomia (i18n)** | `data/taxonomy/i18n/*.yaml` | Traduzioni per lingua (SSOT) |
| **Mappa di Copertura** | `coverage_map/coverage_map.yaml` | Mappatura framework-evidence |
| **Schemi** | `schemas/jsonschema/` | Schemi di validazione JSON |

### File Derivati

I seguenti file sono **generati** dalla SSOT e NON dovrebbero essere modificati manualmente:

| File | Generato Da | Generatore |
| --- | --- | --- |
| `artifacts/taxonomy/{version}/{lang}/taxonomy_dictionary.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_en.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_ja.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/code_system.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/dimensions_en_ja.md` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_dictionary.json` | canonical + i18n | `build_artifacts.py` |

### Codici Linguistici (BCP47)

AIMO utilizza codici linguistici BCP47:

| Codice | Lingua | Stato |
| --- | --- | --- |
| `en` | Inglese | Canonico (fonte) |
| `ja` | Giapponese (日本語) | Attivo |
| `es` | Spagnolo (Español) | Attivo |
| `fr` | Francese (Français) | Attivo |
| `de` | Tedesco (Deutsch) | Attivo |
| `pt` | Portoghese (Português) | Attivo |
| `it` | Italiano (Italiano) | Attivo |
| `zh` | Cinese Semplificato (简体中文) | Attivo |
| `zh-TW` | Cinese Tradizionale (繁體中文) | Attivo |
| `ko` | Coreano (한국어) | Attivo |

### File CSV Legacy (Congelati)

I file CSV legacy misti EN/JA in `source_pack/03_taxonomy/legacy/` sono:

- **Congelati a 21 colonne** — non verranno aggiunte nuove colonne linguistiche
- **Mantenuti per retrocompatibilità** — le integrazioni esistenti possono continuare a usarli
- **Applicati dalla CI** — aggiungere `label_es`, `definition_de`, ecc. farà fallire il build

Per nuove lingue, usare gli artefatti per lingua in `artifacts/taxonomy/{version}/{lang}/`.

## Tracciamento della Freschezza delle Traduzioni

AIMO utilizza un sistema di **Tracciamento della Freschezza delle Traduzioni** per mantenere la coerenza tra il contenuto inglese (fonte) e quello tradotto.

### Come Funziona

1. Ogni file tradotto contiene metadati che tracciano da quale versione della fonte inglese è stato tradotto
2. Quando il contenuto inglese viene aggiornato, il sistema rileva le traduzioni obsolete
3. La CI avvisa delle traduzioni obsolete ma non blocca (le traduzioni possono essere in ritardo)

### Metadati di Traduzione

I file tradotti includono metadati nel frontmatter:

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

### Utilizzo dello Strumento di Sincronizzazione

```bash
# Controllare la freschezza di tutte le traduzioni
python tooling/i18n/sync_translations.py --check

# Controllare una lingua specifica
python tooling/i18n/sync_translations.py --check --lang ja

# Generare un report delle traduzioni
python tooling/i18n/sync_translations.py --report

# Inizializzare una nuova lingua (copiare EN come base)
python tooling/i18n/sync_translations.py --init-lang es

# Aggiornare i metadati dopo aver completato la traduzione
python tooling/i18n/sync_translations.py --update-meta docs/ja/index.md
```

Per specifiche tecniche dettagliate, vedere `tooling/i18n/TRANSLATION_SYNC_SPEC.md`.

## Workflow di Aggiornamento

### Aggiornamenti della Tassonomia (Nuovo Workflow SSOT-First)

1. Modificare la SSOT in `data/taxonomy/`:
   - Modifiche strutturali → `canonical.yaml`
   - Traduzioni inglesi → `i18n/en.yaml`
   - Traduzioni giapponesi → `i18n/ja.yaml`
2. Eseguire la validazione: `python tooling/checks/lint_taxonomy_ssot.py`
3. Rigenerare tutti i file derivati: `python tooling/taxonomy/build_artifacts.py --version current --langs en ja`
4. Aggiornare le pagine di documentazione se necessario
5. Committare tutte le modifiche insieme

### Aggiornamenti della Mappa di Copertura

1. Modificare `coverage_map/coverage_map.yaml` (la SSOT)
2. Aggiornare le tabelle delle pagine framework corrispondenti (`docs/en/coverage-map/*.md`)
3. Aggiornare le traduzioni giapponesi (`docs/ja/coverage-map/*.md`)
4. Committare tutte le modifiche insieme

### Aggiornamenti della Documentazione

1. Modificare la fonte inglese (`docs/en/...`)
2. Aggiornare le traduzioni se necessario (o segnarle per aggiornamento successivo)
3. Eseguire `python tooling/i18n/sync_translations.py --check` per vedere le traduzioni obsolete
4. Eseguire `python tooling/checks/lint_i18n.py` per verificare la coerenza degli heading
5. Eseguire `mkdocs build --strict` per verificare il build
6. Committare tutte le modifiche insieme

!!! note "Priorità delle Traduzioni"
    Non tutte le traduzioni devono essere aggiornate immediatamente. Le pagine di Livello 1 (critiche) dovrebbero avere la priorità:
    
    - `index.md`
    - `standard/current/*.md`
    - `governance/index.md`
    - `releases/`

## Aggiungere una Nuova Lingua (5 Passaggi)

Per aggiungere una nuova lingua (es. Spagnolo):

### Passaggio 1: Generare il Pack della Tassonomia

```bash
python tooling/taxonomy/build_i18n_taxonomy.py --add-lang es --lang-name "Español"
```

Crea `data/taxonomy/i18n/es.yaml` con riferimenti inglesi come commenti.

### Passaggio 2: Creare la Cartella Docs

```bash
mkdir -p docs/es && cp -r docs/en/* docs/es/
```

### Passaggio 3: Aggiornare mkdocs.yml

```yaml
plugins:
  - i18n:
      languages:
        - locale: es
          name: Español
          build: true
```

### Passaggio 4: Tradurre

- Tradurre `data/taxonomy/i18n/es.yaml`
- Tradurre i file in `docs/es/`

### Passaggio 5: Verificare

```bash
python tooling/checks/lint_i18n.py && mkdocs build --strict
```

!!! success "Fatto"
    La nuova lingua è ora disponibile su `/dev/es/`

## Convenzioni di Denominazione dei File

| Pattern | Esempio | Descrizione |
| --- | --- | --- |
| `index.md` | `docs/en/governance/index.md` | Pagina di atterraggio della sezione |
| `{topic}.md` | `docs/en/governance/trust-package.md` | Pagina dell'argomento |
| `{NN}-{topic}.md` | `docs/en/standard/current/03-taxonomy.md` | Pagina di specifica numerata |

## Controlli di Qualità

Eseguire questi controlli prima di committare:

```bash
# struttura i18n, coerenza heading e rilevamento frasi deprecate
python tooling/checks/lint_i18n.py

# Lint di schema e manifest
python tooling/checks/lint_schema.py
python tooling/checks/lint_manifest.py

# Lint SSOT della tassonomia
python tooling/checks/lint_taxonomy_ssot.py --required-langs en
python tooling/checks/lint_legacy_csv.py
python tooling/checks/lint_taxonomy_dictionary.py
python tooling/checks/lint_taxonomy_json.py

# Artefatti della tassonomia aggiornati
python tooling/taxonomy/build_artifacts.py --check

# Verifica del build
mkdocs build --strict
```

## Pagine Correlate

- [Release](../../releases/) — Pacchetti scaricabili
- [Governance](../../governance/) — Governance del progetto
