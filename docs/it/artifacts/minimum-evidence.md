---
description: Requisiti minimi di evidence AIMO. Checklist MUST-level per ciclo di vita (richiesta, revisione, approvazione, modifica, rinnovo) per la prontezza dell'evidence nella governance dell'IA.
---

# Requisiti Minimi di Evidence

Questa pagina definisce i requisiti minimi di evidence come checklist MUST-level, raggruppati per ciclo di vita. Supporta la spiegabilità e la prontezza dell'evidence; non fornisce consulenza legale né garantisce la conformità.

## 1) Richiesta

- **Campi MUST**: identificatore, timestamp, attore/ruolo, ambito (cosa viene richiesto), motivazione (perché).
- **Collegamenti MUST**: id della richiesta referenziato dalla revisione e dagli elementi EV che registrano l'uso.
- **Cosa dimostra**: che l'uso è stato richiesto e circoscritto prima dell'approvazione e dell'uso.

## 2) Revisione / Approvazione

- **Campi MUST**: identificatore, timestamp, attore/ruolo, decisione (approvato/rifiutato/condizionale), ambito, motivazione, riferimento alla richiesta.
- **Collegamenti MUST**: id della revisione referenziato dall'EV e da qualsiasi eccezione o rinnovo successivo.
- **Cosa dimostra**: che una revisione e approvazione definite sono avvenute prima dell'uso (o dell'eccezione).

## 3) Eccezione

- **Campi MUST**: identificatore, timestamp, ambito, scadenza (o deadline), controlli compensativi, motivazione, riferimento alla revisione/richiesta.
- **Collegamenti MUST**: eccezione → controlli compensativi; eccezione → scadenza; eccezione → rinnovo (quando è dovuta la rivalutazione).
- **Cosa dimostra**: che le deviazioni sono temporalmente limitate, hanno controlli compensativi e sono collegate al rinnovo.

## 4) Rinnovo / Rivalutazione

- **Campi MUST**: identificatore, timestamp, attore/ruolo, decisione (rinnovato/revocato/condizionale), riferimenti a eccezione/richiesta/revisione/EV precedenti.
- **Collegamenti MUST**: il rinnovo referenzia l'eccezione o l'approvazione che viene rinnovata; gli elementi EV possono referenziare l'id del rinnovo.
- **Cosa dimostra**: che le eccezioni e le approvazioni vengono rivalutate e rinnovate o revocate su base definita.

## 5) Change Log

- **Campi MUST**: identificatore, timestamp, attore/ruolo, descrizione della modifica, riferimenti (es. a EV, richiesta, revisione, eccezione, rinnovo interessati).
- **Collegamenti MUST**: le voci del change log referenziano gli artefatti che modificano o che attivano la modifica.
- **Cosa dimostra**: che le modifiche al bundle o ai suoi contenuti sono registrate e tracciabili.

## 6) Integrità & Accesso

L'integrità dell'evidence e il controllo degli accessi sono essenziali per l'affidabilità dell'audit. Sebbene AIMO non prescriva controlli tecnici specifici, gli adottanti dovrebbero documentare come vengono soddisfatte queste aspettative.

### Guida al controllo degli accessi

| Aspetto | Guida |
| --- | --- |
| **Accesso basato sui ruoli** | Definire i ruoli (es. creatore di evidence, revisore, auditor, admin) e documentare chi può creare, leggere, aggiornare o eliminare evidence. |
| **Privilegio minimo** | Concedere l'accesso minimo necessario; limitare l'accesso in scrittura al personale autorizzato. |
| **Logging degli accessi** | Registrare gli eventi di accesso (chi, quando, cosa) per scopi di traccia di audit. |
| **Separazione dei compiti** | Dove praticabile, separare la creazione dell'evidence dai ruoli di approvazione. |

### Guida alla conservazione

| Aspetto | Guida |
| --- | --- |
| **Periodo di conservazione** | Definire e documentare i periodi di conservazione basati sui requisiti normativi e sulla politica organizzativa (es. 5-7 anni per audit finanziari). |
| **Programma di conservazione** | Mantenere un programma che mostri quale evidence viene conservata, per quanto tempo e quando può essere eliminata. |
| **Blocco legale** | Supportare processi di blocco legale che sospendono la normale conservazione/eliminazione per contenziosi o indagini. |

### Opzioni di immutabilità

| Opzione | Descrizione |
| --- | --- |
| **Hashing crittografico** | Generare hash SHA-256 (o più forti) per i file di evidence; memorizzare gli hash separatamente per la verifica. |
| **Storage WORM** | Utilizzare storage Write-Once-Read-Many per gli archivi di evidence per prevenire modifiche. |
| **Log append-only** | Utilizzare log di audit append-only per il tracciamento delle modifiche. |
| **Firme digitali** | Firmare i bundle di evidence per dimostrare l'autorialità e rilevare manomissioni. |

### Aspettative per la traccia di audit

| Elemento | Cosa documentare |
| --- | --- |
| **Change log** | Registrare chi ha modificato cosa, quando e perché (vedere gruppo del ciclo di vita Change Log). |
| **Log degli accessi** | Registrare chi ha acceduto all'evidence, quando e per quale scopo. |
| **Log di sistema** | Conservare i log di sistema rilevanti (autenticazione, autorizzazione) che supportano le affermazioni di integrità dell'evidence. |
| **Record di verifica** | Documentare la verifica periodica dell'integrità (controlli hash, revisioni di audit). |

### Cosa dimostra

- **L'evidence è preservata**: i meccanismi di integrità (hashing, WORM, firme) dimostrano che l'evidence non è stata manomessa.
- **L'accesso è controllato**: i log degli accessi e le definizioni dei ruoli mostrano chi aveva accesso e che il privilegio minimo è stato applicato.
- **L'affidabilità dell'audit è supportata**: insieme, questi elementi danno agli auditor fiducia nell'affidabilità dell'evidence.

### Profili operativi raccomandati

Scegliere un profilo in base alla tolleranza al rischio e ai requisiti normativi. Queste sono raccomandazioni, non mandati.

| Aspetto | Leggero | Standard | Rigoroso |
| --- | --- | --- | --- |
| **Caso d'uso** | Piloti interni, IA a basso rischio | Sistemi di produzione, rischio moderato | Industrie regolamentate, IA ad alto rischio |
| **Periodo di conservazione** | 1-2 anni | 5-7 anni | 7-10+ anni o minimo normativo |
| **Immutabilità** | Hash SHA-256 | SHA-256 + log append-only | Storage WORM + firme digitali |
| **Controllo degli accessi** | Basato sui ruoli (base) | Basato sui ruoli + logging degli accessi | Separazione dei compiti + traccia di audit completa |
| **Traccia di audit** | Solo change log | Change log + log degli accessi | Log di sistema completi + verifica periodica |
| **Frequenza di verifica** | Su richiesta | Trimestrale | Mensile o continua |
| **Uso del validator** | Opzionale | Obbligatorio prima della presentazione | Obbligatorio + controlli CI automatizzati |

!!! note "I periodi di conservazione sono esempi"
    I periodi di conservazione mostrati sono illustrativi. Le organizzazioni devono determinare la conservazione in base alle leggi applicabili, ai contratti, ai requisiti di settore e alle politiche interne.

!!! tip "Come scegliere"
    - **Leggero**: Adatto per sperimentazione, strumenti interni o applicazioni a bassa posta in gioco dove gli audit formali sono improbabili.
    - **Standard**: Raccomandato per la maggior parte delle implementazioni di produzione dove gli audit possono verificarsi ma non sono continui.
    - **Rigoroso**: Richiesto per industrie regolamentate (finanza, sanità, governo) o sistemi IA con impatto di rischio significativo.

## Nota importante

Questo set minimo supporta la spiegabilità e la prontezza dell'evidence; non fornisce di per sé consulenza legale né garantisce la conformità.

Vedere [Evidence Bundle](../evidence-bundle/) per la struttura del bundle e il TOC; vedere [Template EV](../../standard/current/06-ev-template/) e gli schemi per l'allineamento a livello di campo.

Vedere anche: [Schemi Log](../log-schemas/) — formati di log normalizzati per evidence di scoperta Shadow AI e attività agent.
