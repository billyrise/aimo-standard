---
description: Protocollo di Supervisione Umana AIMO - Confine tra validazione automatizzata e revisione umana. Responsabilità di giudizio macchina vs. umano nella governance dell'IA.
---

# Protocollo di Supervisione Umana

Questa pagina definisce il confine tra ciò che la validazione automatizzata (Validator) può controllare e ciò che richiede revisione umana (Human-in-the-Loop). Chiarisce le responsabilità per il giudizio macchina vs. umano nei processi di evidence per la governance dell'IA.

## Scopo

Gli strumenti di validazione automatizzata possono controllare efficientemente la correttezza strutturale e sintattica, ma non possono sostituire il giudizio umano per decisioni dipendenti dal contesto. Questo protocollo:

- Chiarisce cosa il Validator può e non può verificare
- Definisce l'ambito della revisione umana richiesta per una governance efficace
- Supporta le spiegazioni di audit documentando il processo di supervisione umana
- Fornisce un framework per le organizzazioni che implementano workflow di governance dell'IA

## Cosa può fare la validazione automatizzata (ambito del Validator)

Il Validator AIMO e strumenti automatizzati simili possono controllare:

| Capacità | Descrizione |
| --- | --- |
| **Completezza dei campi/documenti richiesti** | Verificare che tutti i campi obbligatori siano presenti in manifest, record EV e altri artefatti |
| **Coerenza strutturale** | Validare riferimenti, ID e collegamenti incrociati tra artefatti (es. request_id → review_id) |
| **Validazione dello schema** | Controllare che gli artefatti JSON/YAML siano conformi agli schemi definiti |
| **Validazione del formato dei codici** | Verificare che i codici della tassonomia corrispondano ai pattern attesi (es. `UC-001`) |
| **Controlli di integrità** | Validare il formato e la presenza degli hash (non il ricalcolo contro il contenuto) |
| **Validazione del dizionario** | Confermare che i codici esistano nel dizionario della tassonomia |

Vedere [Validator](../../standard/current/07-validator/) per regole di validazione dettagliate e implementazione di riferimento.

## Cosa richiede revisione umana (ambito Human-in-the-Loop)

Le seguenti aree richiedono giudizio umano e non possono essere automatizzate:

| Capacità | Descrizione |
| --- | --- |
| **Giudizio del rischio dipendente dal contesto** | Valutare rischi aziendali, etici e operativi basati sul contesto organizzativo |
| **Motivazione dell'approvazione delle eccezioni** | Valutare se un'eccezione è giustificata e se i controlli compensativi sono adeguati |
| **Decision-making per la remediation** | Prioritizzare le correzioni, allocare risorse e determinare le tempistiche |
| **Trade-off delle policy** | Bilanciare requisiti in competizione (es. velocità vs. completezza, costo vs. rischio) |
| **Accettazione del rischio residuo** | Decidere se i rischi rimanenti sono accettabili dopo i controlli |
| **Valutazione dell'impatto cross-domain** | Valutare le implicazioni per legale, HR, operations e altre funzioni |
| **Verifica dell'accuratezza del contenuto** | Confermare che il contenuto dell'evidence sia fattualmente corretto e completo |
| **Comunicazione con gli stakeholder** | Spiegare le decisioni ad auditor, regolatori e leadership |

## Confine di responsabilità

| Aspetto | Validator (Macchina) | Revisore Umano |
| --- | --- | --- |
| **Struttura** | ✓ Può verificare | Revisionare se segnalato |
| **Completezza** | ✓ Può verificare i campi | Verificare l'adeguatezza del contenuto |
| **Formato** | ✓ Può verificare | — |
| **Giudizio del rischio** | ✗ Non può valutare | ✓ Deve valutare |
| **Approvazione eccezioni** | ✗ Non può decidere | ✓ Deve decidere |
| **Priorità remediation** | ✗ Non può prioritizzare | ✓ Deve prioritizzare |
| **Interpretazione legale** | ✗ Non può interpretare | ✓ Deve verificare con il consulente |
| **Conclusione dell'audit** | ✗ Non può concludere | ✓ Responsabilità dell'auditor |

!!! note "Ruoli complementari"
    Validator e revisione umana sono **complementari**, non alternative. Il Validator assicura la coerenza strutturale prima della revisione umana; la revisione umana assicura l'appropriatezza contestuale.

## Aspettative di evidence

Le organizzazioni che implementano la supervisione umana dovrebbero documentare:

| Tipo di Evidence | Descrizione |
| --- | --- |
| **Record di revisione** | Chi ha revisionato, quando e quale decisione è stata presa |
| **Motivazione dell'approvazione** | Perché la decisione è stata presa (specialmente per le eccezioni) |
| **Record di escalation** | Quando e perché i problemi sono stati escalati a un'autorità superiore |
| **Piano di remediation** | Azioni pianificate, responsabili e tempistiche per affrontare i problemi |
| **Sign-off** | Attestazione formale che la revisione è stata completata |

Questi record dovrebbero essere inclusi nell'Evidence Bundle secondo i [Requisiti Minimi di Evidence](../../artifacts/minimum-evidence/).

## Non sovra-dichiarazione

!!! warning "Importante"
    Questo protocollo definisce un **framework per documentare la supervisione umana**. **Non**:

    - Fornisce consulenza legale o interpretazione normativa
    - Garantisce la conformità a qualsiasi normativa o standard
    - Sostituisce il giudizio umano qualificato con decisioni automatizzate
    - Prescrive processi organizzativi specifici

    Le organizzazioni devono adattare questo framework al loro contesto specifico, profilo di rischio e requisiti normativi.

## Pagine correlate

- [Validator](../../standard/current/07-validator/) — regole di validazione automatizzata e implementazione di riferimento
- [Confini di Responsabilità](../responsibility-boundary/) — cosa fornisce AIMO vs. responsabilità degli adottanti
- [Requisiti Minimi di Evidence](../../artifacts/minimum-evidence/) — checklist MUST-level per evidence
- [Trust Package](../trust-package/) — hub dei materiali pronti per l'auditor
