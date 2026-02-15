---
description: Requisiti minimi di evidence AIMO. Lista di controllo MUST per ciclo di vita (richiesta, revisione, approvazione, modifica, rinnovo) per la prontezza dell'evidence nella governance dell'IA.
---
<!-- aimo:translation_status=translated -->

# Requisiti minimi di evidence (Minimum Evidence Requirements)

Questa pagina è la lista di controllo dei **Requisiti minimi di evidence** per auditor e implementatori. Definisce i requisiti minimi come lista MUST, raggruppati per ciclo di vita. Supporta la spiegabilità e la prontezza dell'evidence; non costituisce parere legale né garantisce conformità.

Utilizzare questa pagina insieme a [Evidence Bundle](../evidence-bundle/) e al [Validator](../../standard/current/07-validator/) nella preparazione o revisione delle submission.

## 1) Richiesta (Request)

- **Campi MUST**: identificatore, timestamp, attore/ruolo, ambito (cosa è richiesto), rationale.
- **Collegamenti MUST**: l'id della richiesta è referenziato dalla revisione e dagli elementi EV che registrano l'uso.
- **Cosa dimostra**: che l'uso è stato richiesto e delimitato prima dell'approvazione e dell'uso.

## 2) Revisione / Approvazione (Review / Approval)

- **Campi MUST**: identificatore, timestamp, attore/ruolo, decisione (approvato/rifiutato/condizionato), ambito, rationale, riferimento alla richiesta.
- **Collegamenti MUST**: l'id della revisione è referenziato dall'EV e da eventuali eccezioni o rinnovi successivi.
- **Cosa dimostra**: che una revisione e approvazione definite sono avvenute prima dell'uso (o eccezione).

## 3) Eccezione (Exception)

- **Campi MUST**: identificatore, timestamp, ambito, scadenza (o termine), controlli compensativi, rationale, riferimento a revisione/richiesta.
- **Collegamenti MUST**: eccezione → controlli compensativi; eccezione → scadenza; eccezione → rinnovo (quando è dovuta la rivalutazione).
- **Cosa dimostra**: che le deviazioni sono limitate nel tempo, hanno controlli compensativi e sono collegate al rinnovo.

## 4) Rinnovo / Rivalutazione (Renewal / Re-evaluation)

- **Campi MUST**: identificatore, timestamp, attore/ruolo, decisione (rinnovato/revocato/condizionato), riferimenti a eccezione/richiesta/revisione/EV precedenti.
- **Collegamenti MUST**: il rinnovo referenzia l'eccezione o l'approvazione rinnovata; gli elementi EV possono referenziare l'id di rinnovo.
- **Cosa dimostra**: che eccezioni e approvazioni sono rivalutate e rinnovate o revocate secondo criteri definiti.

## 5) Registro delle modifiche (Change Log)

- **Campi MUST**: identificatore, timestamp, attore/ruolo, descrizione della modifica, riferimenti (es. a EV, richiesta, revisione, eccezione, rinnovo interessati).
- **Collegamenti MUST**: le voci del registro delle modifiche referenziano gli artefatti che modificano o che innescano la modifica.
- **Cosa dimostra**: che le modifiche al bundle o al suo contenuto sono registrate e tracciabili.

## 6) Integrità e accesso (Integrity & Access)

L'integrità dell'evidence e il controllo degli accessi sono essenziali per la fiducia nell'audit. AIMO non prescrive controlli tecnici specifici; gli adoptanti devono documentare come queste aspettative sono soddisfatte.

### Guida al controllo degli accessi

| Aspetto | Guida |
| --- | --- |
| **Accesso basato sui ruoli** | Definire ruoli (es. creatore evidence, revisore, auditor, admin) e documentare chi può creare, leggere, aggiornare o eliminare evidence. |
| **Privilegio minimo** | Concedere l'accesso minimo necessario; limitare la scrittura al personale autorizzato. |
| **Registrazione degli accessi** | Registrare gli eventi di accesso (chi, quando, cosa) per la tracciabilità dell'audit. |
| **Separazione delle funzioni** | Quando pratico, separare la creazione dell'evidence dai ruoli di approvazione. |

### Guida alla conservazione

| Aspetto | Guida |
| --- | --- |
| **Periodo di conservazione** | Definire e documentare i periodi in base ai requisiti normativi e alla politica organizzativa (es. 5–7 anni per audit finanziari). |
| **Piano di conservazione** | Mantenere un piano che mostri quali evidence sono conservate, per quanto tempo e quando possono essere eliminate. |
| **Legal hold** | Supportare processi di legal hold che sospendono la conservazione/eliminazione normale in caso di contenzioso o indagine. |

### Opzioni di immutabilità

| Opzione | Descrizione |
| --- | --- |
| **Hash crittografico** | Generare hash SHA-256 (o superiori) per i file di evidence; conservare gli hash separatamente per verifica. |
| **Storage WORM** | Utilizzare storage a scrittura singola e lettura multipla (WORM) per gli archivi di evidence per evitare modifiche. |
| **Log solo append** | Utilizzare log di audit solo append per il tracciamento delle modifiche. |
| **Firme digitali** | Firmare i bundle di evidence per provare la paternità e rilevare manomissioni. |

### Aspettative sulla tracciabilità dell'audit

| Elemento | Cosa documentare |
| --- | --- |
| **Registro delle modifiche** | Registrare chi ha modificato cosa, quando e perché (vedere il gruppo del ciclo di vita Change Log). |
| **Registro degli accessi** | Registrare chi ha acceduto all'evidence, quando e per quale scopo. |
| **Log di sistema** | Conservare i log di sistema rilevanti (autenticazione, autorizzazione) che supportano le affermazioni di integrità. |
| **Registri di verifica** | Documentare la verifica periodica dell'integrità (controlli hash, revisioni audit). |

### Cosa dimostra

- **L'evidence è preservata**: i meccanismi di integrità (hashing, WORM, firme) dimostrano che l'evidence non è stata manomessa.
- **L'accesso è controllato**: i registri degli accessi e le definizioni dei ruoli mostrano chi ha avuto accesso e che il privilegio minimo è stato applicato.
- **La fiducia nell'audit è supportata**: insieme, questi elementi danno agli auditor fiducia nell'affidabilità dell'evidence.

### Profili operativi raccomandati

Scegliere un profilo in base alla tolleranza al rischio e ai requisiti normativi. Sono raccomandazioni, non obblighi.

| Aspetto | Leggero | Standard | Rigoroso |
| --- | --- | --- | --- |
| **Caso d'uso** | Pilot interni, IA a basso rischio | Sistemi in produzione, rischio moderato | Industrie regolamentate, IA ad alto rischio |
| **Periodo di conservazione** | 1–2 anni | 5–7 anni | 7–10+ anni o minimo normativo |
| **Immutabilità** | Hash SHA-256 | SHA-256 + log solo append | Storage WORM + firme digitali |
| **Controllo accessi** | Basato su ruoli (base) | Basato su ruoli + registrazione accessi | Separazione delle funzioni + tracciabilità completa |
| **Tracciabilità audit** | Solo registro modifiche | Registro modifiche + registro accessi | Log di sistema completi + verifica periodica |
| **Frequenza verifica** | Su richiesta | Trimestrale | Mensile o continua |
| **Uso del Validator** | Opzionale | Richiesto prima della submission | Richiesto + controlli CI automatizzati |

!!! note "I periodi di conservazione sono esempi"
    I periodi indicati sono illustrativi. Le organizzazioni devono determinare la conservazione in base a leggi applicabili, contratti, requisiti di settore e politiche interne.

!!! tip "Come scegliere"
    - **Leggero**: Adatto a sperimentazione, strumenti interni o applicazioni a basso impatto dove un audit formale è improbabile.
    - **Standard**: Raccomandato per la maggior parte dei deployment in produzione dove possono esserci audit ma non continui.
    - **Rigoroso**: Richiesto per industrie regolamentate (finanza, sanità, governo) o sistemi IA con impatto sul rischio significativo.

## Nota importante

Questo insieme minimo supporta la spiegabilità e la prontezza dell'evidence; non costituisce di per sé parere legale né garantisce conformità.

Vedere [Evidence Bundle](../evidence-bundle/) per struttura e indice del bundle; [Modello EV](../../standard/current/06-ev-template/) e schemi per l'allineamento a livello di campo.

Vedere anche: [Log Schemas](../log-schemas/) — formati di log normalizzati per la scoperta Shadow AI e l'evidence sull'attività degli agenti.

## Overlay normativi (informativo)

Le **overlay** seguenti descrivono evidence aggiuntiva spesso attesa in contesti normativi o di approvvigionamento specifici. Sono **informative**; allegare modelli/liste di controllo ufficiali così come sono nella [sezione External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) del Modello EV e referenziarli per logical_id nel manifesto.

| Overlay | Artefatti aggiuntivi tipicamente attesi | Dove allegare | Profilo (opzionale) |
| --- | --- | --- | --- |
| **EU alto rischio** | Gestione del rischio, documentazione tecnica (Allegato IV), registrazione, supervisione umana, trasparenza (Art 50), segnalazione incidenti | payload_index; Evidence Bundle + profilo Annex IV | `eu_ai_act_annex_iv.json`, `eu_ai_act_high_risk.json` |
| **EU GPAI CoP** | Model Documentation Form (trasparenza, diritti d'autore, sicurezza) | External Forms; logical_id es. GPAI_MODEL_DOC_FORM | `eu_gp_ai_cop.json` |
| **NIST GenAI** | Artefatti del profilo GenAI (adattamento modello, valutazione, monitoraggio) | payload_index; change_log; External Forms / registri GenAI | `nist_ai_600_1_genai.json` |
| **UK ATRS / appalti** | Registro di trasparenza ATRS; responsabile della responsabilità; note di valutazione appalti | External Forms; Summary, review | `uk_atrs_procurement.json` |
| **JP appalti** | Lista di controllo appalti pubblici GenAI governo; lista di controllo AI Business Guidelines | External Forms; logical_id es. JP_PROCUREMENT_CHECKLIST | `jp_gov_genai_procurement.json` |

I nomi dei file di profilo seguono il pattern `coverage_map/profiles/<target>_<purpose>.json`; ciascuno include `target_version`. Vedere [Coverage Map — Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/) per UK e Giappone; [EU AI Act](../../coverage-map/eu-ai-act/) e [NIST AI RMF](../../coverage-map/nist-ai-rmf/) per UE e NIST.
