---
description: Toolkit di prontezza per la certificazione ISO/IEC 42001. Percorso più breve verso evidence pronta per l'audit allineata all'ISO 42001 con gli artefatti AIMO. Supporta solo la prontezza; non conferisce certificazione.
---
<!-- aimo:translation_status=translated -->

# Toolkit di prontezza per la certificazione ISO/IEC 42001

Questa pagina è una guida **pratica e orientata all'adozione** per produrre **evidence pronta per l'audit** allineata all'ISO/IEC 42001 utilizzando gli artefatti AIMO. **Supporta la prontezza**; **non** conferisce certificazione. Le decisioni di certificazione restano presso **organismi di certificazione accreditati**.

## Obiettivo

Produrre un Evidence Bundle strutturato e verificato dal validatore che supporti controlli di tipo ISO/IEC 42001 (contesto, leadership, pianificazione, supporto, funzionamento, valutazione delle prestazioni, miglioramento), in modo che gli auditor possano individuare e verificare l'evidence in modo efficiente.

## Workflow in 5 passi

| Passo | Azione |
| --- | --- |
| **1. Stabilire ambito e inventario IA** | Definire l'ambito (scope_ref); classificare i sistemi di IA con la [tassonomia](../../standard/current/03-taxonomy/) e il [dizionario](../../standard/current/05-dictionary/). |
| **2. Impostare gli artefatti del sistema di gestione** | Creare o referenziare politiche, ruoli e artefatti allineati al PDCA. Usare [AIMO-MS / AIMO-Controls](../../conformance/) come struttura; referenziare il [modello Evidence Pack](../../standard/current/06-ev-template/) (EP-01..EP-07). |
| **3. Produrre Evidence Bundle e evidence minima** | Costruire manifest, object_index, payload_index, hash_chain, signing secondo la [struttura dell'Evidence Bundle](../../standard/current/09-evidence-bundle-structure/). Includere request, review, exception, renewal, change_log secondo i [Requisiti minimi di evidence](minimum-evidence.md). |
| **4. Eseguire validatore + checksum + controllo modifiche** | Eseguire `python validator/src/validate.py <bundle_path> --validate-profiles`. Registrare la versione del validatore e l'output. Generare checksum SHA-256; mantenere le voci del registro delle modifiche che referenziano gli oggetti impattati. |
| **5. Preparare il pacchetto di audit** | Impacchettare il bundle (zip o equivalente); fornire i checksum. Opzionalmente allegare l'[output del report di audit](../../standard/current/07-validator/) (audit-json / audit-html). Usare URL versionate (es. `/0.1.2/`) quando si cita lo standard. Per il livello Audit-Ready, aggiungere [Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index) e [External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is). |

## Lista di controllo: famiglia di clausole ISO 42001 → artefatti AIMO → output di evidence

| Famiglia di clausole ISO 42001 | Artefatti AIMO | Output di evidence |
| --- | --- | --- |
| Contesto (4.1) | Summary, Dictionary, scope_ref | scope_ref del manifesto; Summary; Dictionary |
| Leadership / Politica (5.x) | Summary, review, dictionary | Registri di revisione; riferimenti alla politica |
| Pianificazione (6.x) | request, review, exception, EV, Dictionary | Richiesta/approvazione; rischio/obiettivi in EV o Dictionary |
| Supporto (7.x) | Summary, review, EV, change_log | Documentazione; evidence di competenza/consapevolezza |
| Funzionamento (8.x) | EV, request, review, exception | Controlli operativi; applicabilità |
| Valutazione delle prestazioni (9.x) | EV, change_log, review, renewal | Monitoraggio; audit interno; riesame della direzione |
| Miglioramento (10.x) | exception, renewal, change_log | Azione correttiva; miglioramento continuo |

Vedere [Coverage Map — ISO/IEC 42001](../../coverage-map/iso-42001/) e [ISO/IEC 42006](https://www.iso.org/standard/42006) per le aspettative degli organismi di audit.

## Linguaggio sicuro

- **Usare:** "Utilizziamo gli artefatti AIMO per supportare la prontezza all'ISO/IEC 42001; le decisioni di certificazione restano presso gli organismi di certificazione accreditati."
- **Non usare:** "ISO 42001 certificato da AIMO" o "AIMO certifica la conformità."

Standard ufficiale (fonte primaria): [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) (ISO). Questo toolkit è allineato con [Conformità](../../conformance/) e [Limite di responsabilità](../../governance/responsibility-boundary/) — AIMO non certifica né garantisce conformità.

## Correlati

- [Conformità](../../conformance/) — Livelli (Foundation, Operational, Audit-Ready) e linguaggio di dichiarazione
- [Trust Package](../../governance/trust-package/) — Materiali pronti per l'auditor
- [Responsibility Boundary](../../governance/responsibility-boundary/) — Cosa fornisce e non fornisce AIMO
