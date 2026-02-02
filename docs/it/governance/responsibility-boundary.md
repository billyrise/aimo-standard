---
description: Confini di Responsabilità AIMO - Definisce cosa fornisce lo standard vs. le responsabilità degli adottanti. Dichiarazione di non sovra-dichiarazione e limitazioni dell'ambito.
---

# Confini di Responsabilità

Questa pagina definisce cosa fornisce e non fornisce lo Standard AIMO, le assunzioni che fa e le responsabilità degli adottanti.

## Cosa fornisce lo Standard AIMO

- **Un formato di evidence strutturato**: schemi, template e tassonomia per l'evidence di governance dell'IA.
- **Framework di tracciabilità**: collegamento dell'evidence basato sul ciclo di vita (richiesta → revisione → eccezione → rinnovo).
- **Supporto alla spiegabilità**: mappatura di copertura verso framework esterni per discussioni di audit.
- **Tooling di validazione**: validator di riferimento e regole per controlli di coerenza strutturale.
- **Documentazione**: specifica normativa, esempi e guida.

## Cosa NON fornisce lo Standard AIMO

| Fuori ambito | Spiegazione |
| --- | --- |
| **Consulenza legale** | AIMO non interpreta leggi o normative. Consultare un consulente legale qualificato per la conformità normativa. |
| **Certificazione di conformità** | Usare AIMO non certifica la conformità a qualsiasi normativa o framework (ISO 42001, EU AI Act, NIST AI RMF, ecc.). |
| **Valutazione del rischio** | AIMO struttura l'evidence ma non esegue né valida valutazioni del rischio dell'IA. |
| **Controlli tecnici** | AIMO non implementa controllo degli accessi, crittografia o altri controlli di sicurezza; documenta le aspettative. |
| **Esecuzione dell'audit** | AIMO fornisce materiali per gli auditor ma non conduce audit. |
| **Valutazione del modello IA** | AIMO non valuta le performance del modello, il bias o la sicurezza. |

## Assunzioni

Lo Standard AIMO assume:

1. **Gli adottanti hanno processi di governance**: esistono workflow di richiesta, revisione, approvazione ed eccezione.
2. **Gli adottanti mantengono l'evidence**: l'evidence è creata, memorizzata e conservata dai sistemi dell'adottante.
3. **Gli adottanti verificano contro i testi autorevoli**: quando usano la Coverage Map, gli adottanti controllano il framework o la normativa originale.
4. **Il tooling è opzionale**: il validator di riferimento è una comodità; gli adottanti possono usare la propria validazione.

## Responsabilità degli adottanti

| Responsabilità | Descrizione |
| --- | --- |
| **Creazione dell'evidence** | Generare record di evidence accurati e tempestivi allineati allo schema EV. |
| **Storage & conservazione dell'evidence** | Memorizzare l'evidence in modo sicuro con controlli di accesso e periodi di conservazione appropriati. |
| **Integrità & controllo degli accessi** | Implementare controlli (hashing, WORM, log di audit) per preservare l'integrità dell'evidence. |
| **Verifica legale** | Verificare le dichiarazioni di conformità contro i testi legali autorevoli e ottenere consulenza legale se necessario. |
| **Allineamento continuo** | Aggiornare evidence e mappature man mano che evolvono le versioni dello Standard AIMO e i framework esterni. |
| **Preparazione all'audit** | Impacchettare gli evidence bundle e eseguire la validazione prima della presentazione agli auditor. |

## Matrice RACI

La seguente matrice RACI chiarisce le responsabilità tra i ruoli Standard AIMO, Adottante e Auditor.

| Attività | Standard AIMO | Adottante | Auditor |
| --- | :---: | :---: | :---: |
| **Definire schema & template di evidence** | R/A | I | I |
| **Creare record di evidence** | — | R/A | I |
| **Memorizzare & conservare evidence** | — | R/A | I |
| **Implementare controlli di accesso** | — | R/A | I |
| **Implementare controlli di integrità (hash, WORM)** | — | R/A | I |
| **Eseguire validator sul bundle** | C | R/A | C |
| **Impacchettare la submission (zip, checksum)** | C | R/A | I |
| **Verificare i checksum (sha256)** | — | C | R/A |
| **Verificare la struttura del bundle (validator)** | — | C | R/A |
| **Interpretare i requisiti normativi** | — | R/A | C |
| **Emettere la conclusione dell'audit** | — | — | R/A |
| **Fornire consulenza legale** | — | — | — |

**Legenda**: R = Responsible, A = Accountable, C = Consulted, I = Informed, — = Non applicabile

!!! note "Punto chiave"
    Lo Standard AIMO è responsabile della **definizione del formato**. Gli adottanti sono responsabili della **creazione, memorizzazione e validazione dell'evidence**. Gli auditor sono responsabili della **verifica delle submission e dell'emissione delle conclusioni di audit**.

!!! warning "Avviso di non certificazione"
    Lo Standard AIMO è informativo; non certifica la conformità né fornisce consulenza legale. Le conclusioni di audit e le valutazioni di conformità sono di esclusiva responsabilità di auditor qualificati e professionisti legali.

## Dichiarazione di non sovra-dichiarazione

!!! warning "Importante"
    Lo Standard AIMO supporta **spiegabilità e prontezza dell'evidence**. **Non** fornisce consulenza legale, garantisce conformità o certifica la conformità a qualsiasi normativa o framework. Gli adottanti devono verificare le dichiarazioni contro i testi autorevoli e ottenere consulenza professionale quando appropriato.

Questa dichiarazione si applica a tutta la documentazione dello Standard AIMO, inclusi Trust Package, Evidence Bundle, Requisiti Minimi di Evidence, Coverage Map e Release.

## Pagine correlate

- [Trust Package](trust-package.md) — hub dei materiali pronti per l'auditor
- [Protocollo di Supervisione Umana](human-oversight-protocol.md) — confine tra revisione macchina e umana
- [Requisiti Minimi di Evidence](../artifacts/minimum-evidence.md) — checklist MUST-level per ciclo di vita
- [Metodologia della Coverage Map](../coverage-map/methodology.md) — cosa è e non è la mappatura
