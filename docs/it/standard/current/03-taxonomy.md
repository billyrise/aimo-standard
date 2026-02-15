---
description: Tassonomia AIMO - Sistema di classificazione a 8 dimensioni con 91 codici per categorizzare i sistemi IA. Copre ambito funzionale, casi d'uso, tipi di dati, canali, integrazione, rischi, risultati ed evidence.
---
<!-- aimo:translation_status=translated -->

# Tassonomia

La Tassonomia AIMO fornisce un sistema di classificazione strutturato per categorizzare i sistemi IA, i loro usi e i requisiti di governance associati. Consiste di **8 dimensioni** con **91 codici** che abilitano classificazione ed gestione dell'evidence coerenti tra le organizzazioni.

## Scopo

La tassonomia serve tre scopi primari dal punto di vista dell'audit:

1. **Spiegabilità**: Fornisce un vocabolario comune per descrivere i casi d'uso dell'IA attraverso l'organizzazione, supportando una comunicazione chiara con auditor e stakeholder.

2. **Prontezza dell'Evidence**: Abilita una documentazione sistematica dei sistemi IA usando una classificazione standardizzata, rendendo la raccolta e la revisione dell'evidence più efficienti.

3. **Comparabilità**: Permette alle organizzazioni di confrontare casi d'uso dell'IA in contesti diversi usando una terminologia coerente.

## Cosa Non È (Non Sovra-dichiarazione)

!!! warning "Importante"
    Lo Standard AIMO supporta **spiegabilità e prontezza dell'evidence**. **Non** fornisce consulenza legale, garantisce conformità o certifica la conformità a qualsiasi normativa o framework. Vedere [Confini di Responsabilità](../../../governance/responsibility-boundary/) per i dettagli.

La tassonomia è solo un sistema di classificazione. Non:

- Garantisce la conformità a qualsiasi legge o normativa
- Sostituisce consulenza professionale legale, di sicurezza o di conformità
- Certifica la conformità a framework esterni (ISO, NIST, EU AI Act, ecc.)
- Fornisce valutazioni del rischio o raccomandazioni di controllo

## Esempi di rischi specifici IA/agente (perché serve uno standard specifico per l'IA)

I controlli di sicurezza tradizionali (es. ISMS) da soli spesso non riescono a catturare i modi di fallimento specifici degli LLM/agent e le deviazioni degli agent autonomi (es. esecuzione di strumenti non intenzionata, loop ricorsivi) in modo **spiegabile per l'audit**.
La Tassonomia AIMO fornisce un linguaggio condiviso per classificare questi rischi specifici dell'IA e collegarli ai requisiti di evidence e ai workflow di remediation.

!!! warning "Solo esempi di riferimento — non codici normativi"
    I codici seguenti sono **placeholder illustrativi** e **non** fanno parte del sistema di codici normativo AIMO. Non usarli nelle submission; usare dimensioni e codici normativi in [Codes](../04-codes/) e [Dictionary](../05-dictionary/).

- **AG-01** Loop/Ricorsione Fuori Controllo
- **AG-02** Uso Non Autorizzato di Strumenti (abuso stile confused deputy)
- **AG-03** Deriva dei Confini di Privilegio

Non usare AG-* nelle submission; usare le dimensioni e i codici normativi definiti in Codes/Dictionary.

## Panoramica delle Dimensioni

AIMO utilizza 8 dimensioni per classificare i casi d'uso dell'IA. Ogni dimensione ha un prefisso univoco di 2 lettere.

| ID | Nome | Conteggio Codici | Descrizione |
| --- | --- | --- | --- |
| **FS** | Functional Scope | 6 | Quale funzione aziendale è supportata |
| **UC** | Use Case Class | 30 | Che tipo di attività viene eseguita |
| **DT** | Data Type | 10 | Quali classificazioni di dati sono coinvolte |
| **CH** | Channel | 8 | Come gli utenti accedono all'IA |
| **IM** | Integration Mode | 7 | Come l'IA si connette ai sistemi aziendali |
| **RS** | Risk Surface | 8 | Quali rischi sono associati |
| **OB** | Outcome / Benefit | 7 | Quali benefici sono attesi |
| **LG** | Log/Event Type | 15 | Quale log/registro è richiesto |

**Totale: 91 codici in 8 dimensioni**（**EV-** riservato per ID artefatti Evidence; dimensione log/registro della tassonomia: **LG-**.)

### Regole d'Uso

| Dimensione | Selezione | Implicazione per l'Audit |
| --- | --- | --- |
| FS, IM | Esattamente 1 | Classificazione primaria per l'assegnazione di responsabilità |
| UC, DT, CH, RS, LG | 1 o più | Enumerazione completa richiesta per la copertura del rischio |
| OB | 0 o più | Opzionale; documenta il valore aziendale atteso |

## Definizioni delle Dimensioni

### FS: Functional Scope

Categorizza l'uso dell'IA per la funzione aziendale che supporta. **Selezionare esattamente una.**

| Codice | Etichetta | Definizione |
| --- | --- | --- |
| FS-001 | End-user Productivity | IA usata per migliorare la produttività degli utenti finali interni (scrittura, ricerca, riassunto, note riunioni). |
| FS-002 | Customer-facing Features | IA incorporata in funzionalità di prodotto/servizio fornite ai clienti. |
| FS-003 | Developer Tooling | IA usata per assistere lo sviluppo software e attività di engineering. |
| FS-004 | IT Operations | IA usata per operazioni IT e amministrazione di sistema (monitoraggio, gestione incidenti). |
| FS-005 | Security Operations | IA usata per monitoraggio/risposta di sicurezza (SOC, rilevamento, triage). |
| FS-006 | Governance & Compliance | IA usata per supportare attività di governance/conformità (policy, evidence di audit). |

### UC: Use Case Class

Categorizza l'uso dell'IA per il tipo di attività o interazione. **Selezionare una o più.** La lista completa include 30 codici; esempi rappresentativi sotto.

| Codice | Etichetta | Definizione |
| --- | --- | --- |
| UC-001 | General Q&A | Risposte a domande generali e uso conversazionale. |
| UC-002 | Summarization | Riassunto di documenti, riunioni o messaggi. |
| UC-003 | Translation | Traduzione tra lingue. |
| UC-004 | Content Drafting | Generazione di bozze per email, documenti o report. |
| UC-005 | Code Generation | Generazione di codice o script. |
| UC-006 | Code Review | Revisione del codice per problemi e miglioramenti. |
| UC-009 | Search/RAG | Recupero basato su RAG e risposta a domande. |
| UC-010 | Agentic Automation | Agent autonomi o semi-autonomi che eseguono azioni. |

Vedere [Dizionario](../05-dictionary/) per la lista completa dei 30 codici UC.

### DT: Data Type

Categorizza la sensibilità e la classificazione dei dati coinvolti. **Selezionare una o più.**

| Codice | Etichetta | Definizione |
| --- | --- | --- |
| DT-001 | Public | Dati pubblicamente disponibili e destinati alla divulgazione pubblica. |
| DT-002 | Internal | Dati aziendali interni non pubblici. |
| DT-003 | Confidential | Dati interni altamente sensibili che richiedono accesso ristretto. |
| DT-004 | Personal Data | Dati personali come definiti dalle leggi sulla privacy applicabili. |
| DT-005 | Sensitive Personal Data | Categoria speciale/dati personali sensibili. |
| DT-006 | Credentials | Segreti di autenticazione e credenziali. |
| DT-007 | Source Code | Codice sorgente e artefatti correlati. |
| DT-008 | Customer Data | Dati forniti dal cliente o relativi al cliente. |
| DT-009 | Operational Logs | Log operativi o di sistema usati per monitoraggio e troubleshooting. |
| DT-010 | Security Telemetry | Telemetria di sicurezza come alert e rilevamenti. |

### CH: Channel

Categorizza come gli utenti accedono o interagiscono con l'IA. **Selezionare una o più.**

| Codice | Etichetta | Definizione |
| --- | --- | --- |
| CH-001 | Web UI | Uso tramite interfaccia utente web. |
| CH-002 | API | Uso tramite integrazione API programmatica. |
| CH-003 | IDE Plugin | Uso tramite plugin IDE/editor. |
| CH-004 | ChatOps | Uso tramite integrazioni di piattaforme chat (Slack/Teams). |
| CH-005 | Desktop App | Uso tramite applicazione desktop nativa. |
| CH-006 | Mobile App | Uso tramite applicazione mobile nativa. |
| CH-007 | Email | Uso tramite interfaccia email o automazione basata su email. |
| CH-008 | Command Line | Uso tramite interfaccia a riga di comando. |

### IM: Integration Mode

Categorizza come l'IA è integrata nei sistemi aziendali. **Selezionare esattamente una.**

| Codice | Etichetta | Definizione |
| --- | --- | --- |
| IM-001 | Standalone | Usata standalone senza integrazione nei sistemi aziendali. |
| IM-002 | SaaS Integrated | Applicazione SaaS che integra funzionalità IA. |
| IM-003 | Enterprise App Embedded | IA incorporata in applicazioni aziendali interne. |
| IM-004 | RPA/Workflow | IA invocata all'interno di workflow automation o RPA. |
| IM-005 | On-prem / Private | IA ospitata in ambiente privato/on-prem. |
| IM-006 | Managed Service | Uso tramite servizio gestito con controlli aziendali. |
| IM-007 | Shadow / Unmanaged | Uso al di fuori dei controlli di governance approvati. |

### RS: Risk Surface

Categorizza i tipi di rischi associati all'uso dell'IA. **Selezionare una o più.**

| Codice | Etichetta | Definizione |
| --- | --- | --- |
| RS-001 | Data Leakage | Rischio di divulgazione non intenzionale di dati. |
| RS-002 | Security Abuse | Rischio che il sistema sia abusato per scopi malevoli. |
| RS-003 | Compliance Breach | Rischio di violazione di leggi/normative/policy. |
| RS-004 | IP Infringement | Rischio di violazione di copyright/brevetti/segreti commerciali. |
| RS-005 | Model Misuse | Rischio da uso inappropriato del modello o eccessiva dipendenza. |
| RS-006 | Bias/Fairness | Rischio di risultati ingiusti o di parte. |
| RS-007 | Safety | Rischio di contenuti dannosi o raccomandazioni non sicure. |
| RS-008 | Third-party Risk | Rischi di vendor, sub-processori e provider di modelli. |

### OB: Outcome / Benefit

Categorizza i risultati o i benefici attesi dall'uso dell'IA. **Opzionale; selezionare zero o più.**

| Codice | Etichetta | Definizione |
| --- | --- | --- |
| OB-001 | Efficiency | Migliora l'efficienza di tempo/costi. |
| OB-002 | Quality | Migliora la qualità/accuratezza degli output. |
| OB-003 | Revenue | Contribuisce alla crescita dei ricavi. |
| OB-004 | Risk Reduction | Riduce il rischio operativo/di sicurezza/di conformità. |
| OB-005 | Innovation | Abilita nuove capacità o innovazioni. |
| OB-006 | Customer Satisfaction | Migliora la soddisfazione del cliente. |
| OB-007 | Employee Experience | Migliora l'esperienza dei dipendenti. |

### LG: Log/Event Type

Categorizza i tipi di log/registro richiesti o raccolti. **Selezionare una o più.**（EV- riservato per ID artefatti Evidence.)

| Codice | Etichetta | Definizione |
| --- | --- | --- |
| LG-001 | Request Record | Evidence che un uso/servizio IA è stato richiesto e descritto. |
| LG-002 | Review/Approval Record | Evidence che una revisione/approvazione è stata eseguita. |
| LG-003 | Exception Record | Evidence che un'eccezione è stata concessa e tracciata. |
| LG-004 | Renewal/Re-evaluation Record | Evidence che è avvenuto rinnovo o rivalutazione. |
| LG-005 | Change Log Entry | Evidence delle modifiche e delle loro approvazioni. |
| LG-006 | Integrity Proof | Evidence di integrità (hash, firma, WORM). |
| LG-007 | Access Log | Evidence di controllo degli accessi e cronologia degli accessi. |
| LG-008 | Model/Service Inventory | Record di inventario dei modelli/servizi utilizzati. |
| LG-009 | Risk Assessment | Valutazione del rischio documentata per l'uso/servizio. |
| LG-010 | Control Mapping | Evidence di mappatura dei controlli verso framework esterni. |
| LG-011 | Training/Guidance | Evidence di formazione o guida fornita agli utenti. |
| LG-012 | Monitoring Evidence | Evidence di monitoraggio e supervisione continua. |
| LG-013 | Incident Record | Evidence di gestione degli incidenti relativi all'uso dell'IA. |
| LG-014 | Third-party Assessment | Evidence di valutazione del vendor o di terze parti. |
| LG-015 | Attestation/Sign-off | Record di attestazione formale o sign-off. |

## Come Usare

### Relazione con l'Evidence

Ogni documento Evidence referenzia codici da più dimensioni per classificare il sistema IA o il caso d'uso documentato. La classificazione a 8 dimensioni abilita:

- **Categorizzazione coerente** attraverso l'organizzazione
- **Filtraggio basato sul rischio** per valori dimensionali
- **Mappatura ai framework** tramite la Coverage Map

### Referenziare il Dizionario

Per definizioni complete dei codici incluse note sull'ambito ed esempi, fare riferimento al [Dizionario](../05-dictionary/).

### Esempio di Classificazione

```
FS: FS-001 (End-user Productivity)
UC: UC-001 (General Q&A), UC-002 (Summarization)
DT: DT-002 (Internal), DT-004 (Personal Data)
CH: CH-001 (Web UI)
IM: IM-002 (SaaS Integrated)
RS: RS-001 (Data Leakage), RS-003 (Compliance Breach)
OB: OB-001 (Efficiency)
LG: LG-001 (Request Record), LG-002 (Review/Approval Record)
```

## Riferimento SSOT

!!! info "Fonte di Verità"
    La definizione autorevole è `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv`. Questa pagina è esplicativa. Vedere [Guida alla Localizzazione](../../../contributing/localization/) per i workflow di aggiornamento.

## Pagine Correlate

- [Codici](../04-codes/) - Formato dei codici, convenzioni di denominazione e ciclo di vita
- [Dizionario](../05-dictionary/) - Liste complete dei codici e definizioni delle colonne
- [Template di Evidence](../06-ev-template/) - Come usare i codici nell'evidence
- [Confini di Responsabilità](../../../governance/responsibility-boundary/) - Dichiarazione di non sovra-dichiarazione
