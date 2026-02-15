---
description: Overlay di approvvigionamento e divulgazione (Regno Unito, Giappone). ATRS UK, orientamento approvvigionamento UK, approvvigionamento GenAI governo giapponese e linee guida aziendali IA. Solo mappatura di riferimento.
---
<!-- aimo:translation_status=translated -->

# Overlay di approvvigionamento e divulgazione (Regno Unito, Giappone)

Questa pagina descrive **mappature di riferimento** tra evidence AIMO e quadri di approvvigionamento e divulgazione selezionati del **Regno Unito** e del **Giappone**. È **solo mappatura di riferimento**; AIMO non sostituisce elenchi di controllo ufficiali né orientamento governativo.

## Regno Unito: ATRS e approvvigionamento IA

| Tema | Evidence AIMO / mappatura | Note |
| --- | --- | --- |
| **ATRS UK** (registro di trasparenza IA) | Summary, review (responsabile della responsabilità), evidence (descrizione modello/sistema), dictionary (considerazioni di rischio). Profilo: `coverage_map/profiles/uk_atrs_procurement.json`. | Allegare o riferire registro di trasparenza tipo ATRS nei Formulari esterni; collegare agli oggetti del pacchetto per logical_id. |
| **Orientamento approvvigionamento UK** | Request, review, exception; Evidence Bundle per la valutazione dei fornitori. | Utilizzare il pacchetto AIMO per strutturare le evidence per la valutazione dell'approvvigionamento; l'orientamento ufficiale UK rimane autorevole. |

## Giappone: Approvvigionamento GenAI del governo e linee guida aziendali IA

| Tema | Evidence AIMO / mappatura | Note |
| --- | --- | --- |
| **Elenco di controllo approvvigionamento GenAI governo JP** | Allegare l'elenco come Formulario esterno (es. payload: JP_PROCUREMENT_CHECKLIST); riferire nel manifest. Profilo: `coverage_map/profiles/jp_gov_genai_procurement.json`. | Solo mappatura di riferimento; AIMO non sostituisce gli elenchi ufficiali. |
| **Linee guida aziendali IA** | Summary, dictionary; mappare le voci dell'elenco ai codici della tassonomia AIMO quando utile per la tracciabilità. | Utilizzare per la spiegabilità; verificare contro l'orientamento ufficiale giapponese. |

## Come utilizzare

- **Formulari esterni**: Allegare modelli/elenchi ufficiali UK o Giappone **così come sono** (PDF, DOC, ecc.), eseguire l'hash e elencarli nel [payload_index](../../standard/current/09-evidence-bundle-structure/) dell'Evidence Bundle o nella [sezione Formulari esterni del Modello EV](../../standard/current/06-ev-template/). Riferirli per logical_id nel manifest e nelle mappature di copertura.
- **Profili**: I profili sopra definiscono mappature opzionali leggibili da macchina; non impongono obblighi legali o contrattuali.

Vedere [Conformità](../../conformance/) per i livelli e [Requisiti Minimi di Evidence — Overlay normativi](../../artifacts/minimum-evidence/) per il riepilogo degli overlay.
