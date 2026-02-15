---
description: Limite di responsabilità AIMO — Definisce cosa fornisce la norma vs. responsabilità degli adottanti. Dichiarazione di non sovraffermazione e limiti di ambito.
---
<!-- aimo:translation_status=translated -->

# Limite di responsabilità（Responsibility Boundary）

Questa pagina definisce cosa fornisce e cosa non fornisce l'AIMO Standard, le ipotesi che fa e le responsabilità degli adottanti.

## Cosa fornisce l'AIMO Standard

- **Un formato di evidenza strutturato**: schemi, modelli e tassonomia per evidenza di governance IA.
- **Quadro di tracciabilità**: collegamento evidenze per ciclo di vita (richiesta → revisione → eccezione → rinnovo).
- **Supporto alla spiegabilità**: mappatura di copertura verso framework esterni per discussioni di audit.
- **Strumenti di validazione**: validatore di riferimento e regole per verifiche di coerenza strutturale.
- **Documentazione**: specifica normativa, esempi e guida.

## Cosa l'AIMO Standard NON fornisce

| Fuori ambito | Spiegazione |
| --- | --- |
| **Consulenza legale** | AIMO non interpreta leggi o regolamenti. Consultare consulenza legale qualificata per conformità normativa. |
| **Certificazione di conformità** | L'uso di AIMO non certifica la conformità a normative o framework (ISO 42001, EU AI Act, NIST AI RMF, ecc.). |
| **"Certificato ISO da AIMO"** | AIMO non emette certificazioni. La certificazione è effettuata da organismi di certificazione accreditati. |
| **"Conforme EU AI Act grazie ad AIMO"** | AIMO struttura le evidenze; non garantisce né certifica la conformità normativa. |
| **Valutazione dei rischi** | AIMO struttura le evidenze ma non esegue né valida valutazioni del rischio IA. |
| **Controlli tecnici** | AIMO non implementa controllo degli accessi, crittografia o altri controlli di sicurezza; documenta le aspettative. |
| **Esecuzione dell'audit** | AIMO fornisce materiali agli auditor ma non conduce audit. |
| **Valutazione di modelli IA** | AIMO non valuta prestazioni, bias o sicurezza dei modelli. |

## Ipotesi

L'AIMO Standard assume:

1. **Gli adottanti hanno processi di governance**: esistono flussi di richiesta, revisione, approvazione ed eccezione.
2. **Gli adottanti mantengono le evidenze**: le evidenze sono create, memorizzate e conservate dai sistemi dell'adottante.
3. **Gli adottanti verificano rispetto ai testi autorevoli**: nell'uso della Coverage Map, gli adottanti verificano il framework o il regolamento originale.
4. **Gli strumenti sono opzionali**: il validatore di riferimento è una comodità; gli adottanti possono usare la propria validazione.

## Responsabilità degli adottanti

| Responsabilità | Descrizione |
| --- | --- |
| **Creazione di evidenze** | Generare registri di evidenza accurati e tempestivi allineati allo schema EV. |
| **Archiviazione e conservazione delle evidenze** | Conservare le evidenze in modo sicuro con controlli di accesso e periodi di conservazione adeguati. |
| **Integrità e controllo di accesso** | Implementare controlli (hashing, WORM, log di audit) per preservare l'integrità delle evidenze. |
| **Verifica legale** | Verificare le affermazioni di conformità rispetto ai testi legali autorevoli e ottenere consulenza legale se necessario. |
| **Allineamento continuo** | Aggiornare evidenze e mappature al variare delle versioni dell'AIMO Standard e dei framework esterni. |
| **Preparazione all'audit** | Impacchettare Evidence Bundle ed eseguire la validazione prima della consegna agli auditor. |

## Matrice RACI

La seguente matrice RACI chiarisce le responsabilità tra AIMO Standard, Adottante e Auditor.

| Attività | AIMO Standard | Adottante | Auditor |
| --- | :---: | :---: | :---: |
| **Definire schema e modelli di evidenza** | R/A | I | I |
| **Creare registri di evidenza** | — | R/A | I |
| **Archiviare e conservare evidenze** | — | R/A | I |
| **Implementare controlli di accesso** | — | R/A | I |
| **Implementare controlli di integrità (hash, WORM)** | — | R/A | I |
| **Eseguire validatore sul bundle** | C | R/A | C |
| **Impacchettare consegna (zip, checksum)** | C | R/A | I |
| **Verificare checksum (sha256)** | — | C | R/A |
| **Verificare struttura del bundle (validatore)** | — | C | R/A |
| **Interpretare requisiti normativi** | — | R/A | C |
| **Emettere conclusione di audit** | — | — | R/A |
| **Fornire consulenza legale** | — | — | — |

**Legenda**: R = Responsabile, A = Accountable, C = Consultato, I = Informato, — = Non applicabile

!!! note "Punto chiave"
    L'AIMO Standard è responsabile di **definire il formato**. Gli adottanti sono responsabili di **creare, archiviare e validare le evidenze**. Gli auditor sono responsabili di **verificare le consegne e emettere le conclusioni di audit**.

!!! warning "Avviso di non certificazione"
    L'AIMO Standard è informativo; non certifica la conformità né fornisce consulenza legale. Le conclusioni di audit e le valutazioni di conformità sono di esclusiva responsabilità di auditor e professionisti legali qualificati.

## Politica sulle affermazioni

| Accettabile | Inaccettabile |
| --- | --- |
| "Un Evidence Bundle è stato prodotto secondo AIMO Standard v0.1.2 e validato strutturalmente dall'AIMO Validator." | "Conforme EU AI Act", "certificato ISO 42001", "approvato dal governo", ecc. |
| "Utilizziamo gli artefatti AIMO per supportare la preparazione ISO/IEC 42001; le decisioni di certificazione spettano agli organismi di certificazione accreditati." | Affermare che AIMO certifica la conformità o fornisce consulenza legale. |

## Dichiarazione di non sovraffermazione

!!! warning "Importante"
    L'AIMO Standard supporta **spiegabilità e preparazione delle evidenze**. **Non** fornisce consulenza legale, **non** garantisce la conformità né **non** certifica la conformità a normative o framework. Gli adottanti devono verificare le affermazioni rispetto ai testi autorevoli e ottenere parere professionale se del caso.

Questa dichiarazione si applica a tutta la documentazione dell'AIMO Standard, inclusi Trust Package, Evidence Bundle, Minimum Evidence Requirements, Coverage Map e Releases.

## Pagine correlate

- [Trust Package](../trust-package/) — hub materiali pronti per l'audit
- [Human Oversight Protocol](../human-oversight-protocol/) — confine revisione macchina vs. umana
- [Minimum Evidence Requirements](../../artifacts/minimum-evidence/) — checklist MUST per ciclo di vita
- [Coverage Map Methodology](../../coverage-map/methodology/) — cos'è e cos'è il mapping
