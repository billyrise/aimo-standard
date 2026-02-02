---
description: Struttura dell'Evidence Bundle AIMO. Formato pacchetto di audit con indice, tracciabilità e artefatti per la conformità alla governance dell'IA e la consegna agli auditor.
---

# Evidence Bundle

Un **Evidence Bundle** è un pacchetto di audit: un insieme strutturato di artefatti che supporta la spiegabilità e la tracciabilità per la governance dell'IA. Non è una funzionalità di prodotto ma un formato consegnabile per auditor e conformità.

## Struttura e denominazione del bundle

- **Denominazione radice del bundle**: utilizzare un pattern coerente come `{org}_{system}_{period}_{version}` (es. `acme_ai-usage_2026-Q1_v1`).
- **File obbligatori**: almeno un set di Evidence (EV) allineato con il [Template EV](../standard/current/06-ev-template.md), un [Dizionario](../standard/current/05-dictionary.md), un breve **Riepilogo** (sintesi esecutiva del bundle) e un **Change Log** (o riferimento ad esso) per le modifiche al bundle o ai suoi contenuti.
- **Allegati opzionali**: log, record di revisione, approvazioni di eccezioni, record di rinnovo; mantenere una denominazione coerente e referenziabile dall'EV/Dizionario principale.

## Indice dei contenuti (TOC)

| Sezione | Artefatto | Obbligatorio? | Scopo | Campi minimi | Validazione |
| --- | --- | --- | --- | --- | --- |
| Evidence | Record EV (JSON/array) | Sì | Registro di quanto accaduto; collegamento a richiesta/revisione/eccezione/rinnovo | id, timestamp, source, summary; ref ciclo di vita opzionali | [Validator](../validator/index.md), aimo-ev.schema.json |
| Dizionario | dictionary.json | Sì | Chiavi/etichette/descrizioni per codici e dimensioni | entries (key, label, description) | aimo-dictionary.schema.json |
| Riepilogo | summary (doc o campo) | Sì | Panoramica di una pagina per gli auditor | scope, period, key decisions, exceptions | — |
| Change log | change_log o riferimento | Sì | Traccia di audit delle modifiche al bundle/contenuto | id, timestamp, actor, change description, references | — |
| Richiesta | record di richiesta | Se applicabile | Applicazione/richiesta di utilizzo | id, timestamp, actor/role, scope, rationale | — |
| Revisione/Approvazione | record di revisione | Se applicabile | Esito della revisione e approvazione | id, timestamp, actor/role, decision, references | — |
| Eccezione | record di eccezione | Se applicabile | Eccezione con controlli compensativi e scadenza | id, timestamp, scope, expiry, compensating controls, renewal ref | — |
| Rinnovo | record di rinnovo | Se applicabile | Rivalutazione e rinnovo | id, timestamp, actor/role, decision, references to prior exception/EV | — |

## Tracciabilità

- **ID stabili**: ogni record (EV, richiesta, revisione, eccezione, rinnovo, voce del change log) DEVE avere un identificatore stabile e univoco.
- **Riferimenti incrociati**: collegare Richiesta → Revisione → Eccezione (se presente) → Rinnovo e collegare gli elementi EV a questi tramite campi di riferimento (es. `request_id`, `review_id`, `exception_id`, `renewal_id`).
- **Collegamento**: assicurarsi che gli auditor possano seguire una catena dall'uso dell'IA (o eccezione) alla richiesta, approvazione, eventuale eccezione e suoi controlli compensativi e scadenza, e rinnovo.

## Come lo utilizzano gli auditor

Gli auditor utilizzano l'Evidence Bundle per verificare che l'uso dell'IA sia richiesto, revisionato e approvato; che le eccezioni siano temporalmente limitate e abbiano controlli compensativi e rinnovo; e che le modifiche siano registrate. Il TOC e le regole di tracciabilità permettono loro di localizzare gli artefatti richiesti e seguire ID e riferimenti attraverso richiesta, revisione, eccezione, rinnovo e record EV. Il Riepilogo fornisce una panoramica rapida; il Change Log supporta il controllo delle modifiche e la responsabilità.

Vedere [Requisiti Minimi di Evidence](minimum-evidence.md) per i campi MUST-level e i gruppi del ciclo di vita.

## Guida operativa

!!! info "Integrità e controllo degli accessi"
    Sebbene AIMO non prescriva controlli specifici, gli adottanti dovrebbero documentare:
    
    - **Ruoli di accesso**: chi può creare, leggere, aggiornare o eliminare evidence
    - **Politica di conservazione**: quanto tempo viene conservata l'evidence e secondo quale programma
    - **Meccanismi di integrità**: hashing, storage WORM o firme digitali utilizzati
    - **Traccia di audit**: log degli accessi e delle modifiche al bundle
    
    Vedere [Requisiti Minimi di Evidence > Integrità & Accesso](minimum-evidence.md#6-integrity-access) per una guida dettagliata.

## Percorso di audit

Da questa pagina, il tipico percorso di audit prosegue:

1. **Prossimo**: [Requisiti Minimi di Evidence](minimum-evidence.md) — Checklist MUST-level per ciclo di vita
2. **Poi**: [Mappa di Copertura](../coverage-map/index.md) — Mappatura ai framework esterni
3. **Validazione**: [Validator](../validator/index.md) — Eseguire controlli strutturali
4. **Download**: [Release](../releases/index.md) — Ottenere gli asset di release e verificare i checksum
