---
description: Overlay di approvvigionamento e divulgazione (Regno Unito, Giappone). ATRS UK, orientamento approvvigionamento UK, approvvigionamento GenAI governo giapponese e linee guida aziendali IA. Solo mappatura di riferimento.
---
<!-- aimo:translation_status=translated -->

# Overlay di approvvigionamento e divulgazione (Regno Unito, Giappone)

Questa pagina descrive **mappature di riferimento** tra evidence AIMO e quadri di approvvigionamento e divulgazione selezionati del **Regno Unito** e del **Giappone**. L'obiettivo è **ridurre il carico riutilizzando l'evidence AIMO**. È **solo mappatura informativa**; AIMO non garantisce la piena conformità ai requisiti governativi. Verificare rispetto alle fonti ufficiali sotto.

## Fonti primarie

**Regno Unito**

- [Algorithmic Transparency Recording Standard (ATRS) Hub](https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub) — GOV.UK (modello, orientamento, registri pubblicati)
- [Modello ATRS](https://www.gov.uk/government/publications/algorithmic-transparency-template) — Modello ufficiale per il settore pubblico
- [Orientamento per le organizzazioni che usano l'ATRS](https://www.gov.uk/government/publications/guidance-for-organisations-using-the-algorithmic-transparency-standard/algorithmic-transparency-recording-standard-guidance-for-public-sector-bodies) — GOV.UK

**Giappone**

- [Digital Agency — Orientamento su approvvigionamento e utilizzo GenAI](https://www.digital.go.jp/news/3579c42d-b11c-4756-b66e-3d3e35175623) — Digital Agency (Cabinet Secretariat)
- [AI Business Guidelines](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/index.html) — METI / MIC (Ministero dell'Economia, Commercio e Industria / Ministero degli Affari Interni e delle Comunicazioni)

## Tabella di mappatura (Regno Unito)

| Requisito governativo (tema) | Artefatti AIMO | Dove nell'Evidence Bundle | Copertura validatore | Nota |
| --- | --- | --- | --- | --- |
| ATRS — responsabilità / proprietario | Summary, review | manifest; objects/ (EV, Summary); payload_index | schema_validate_ev | Mappatura informativa; non garantisce conformità completa. |
| ATRS — descrizione sistema / modello | Dictionary, EV | objects/; schemas/jsonschema/aimo-dictionary.schema.json | schema_validate_dictionary | Allegare registro ATRS ufficiale nei Formulari esterni; collegare per logical_id. |
| ATRS — considerazioni di rischio | Dictionary, request, review, exception | objects/; templates/ev/ | schema_validate_ev | Profilo: `coverage_map/profiles/uk_atrs_procurement.json`. |
| Approvvigionamento — evidence del fornitore | request, review, exception; Evidence Bundle | manifest, object_index, payload_index; examples/evidence_bundle_minimal/ | schema_validate_ev | Usare il pacchetto per strutturare l'evidence; l'orientamento UK rimane autorevole. |

## Tabella di mappatura (Giappone)

| Requisito governativo (tema) | Artefatti AIMO | Dove nell'Evidence Bundle | Copertura validatore | Nota |
| --- | --- | --- | --- | --- |
| Elenco di controllo approvvigionamento GenAI (Digital Agency) | Formulario esterno (elenco così com'è); Dictionary, Summary | payload_index; sezione External Forms; riferimento nel manifest | N/A (allegato) | Mappatura informativa; non garantisce conformità completa. Profilo: `coverage_map/profiles/jp_gov_genai_procurement.json`. |
| AI Business Guidelines — governance / tracciabilità | Summary, dictionary, request, review, change_log | objects/; manifest; templates/ev/ | schema_validate_dictionary, schema_validate_ev | Mappare le voci dell'elenco alla tassonomia AIMO quando utile. |
| Documentazione rischio / responsabilità | Dictionary, EV, review, exception | objects/; schemas/jsonschema/ | schema_validate_ev | Verificare rispetto all'orientamento ufficiale di Digital Agency e METI/MIC. |

## Regno Unito: ATRS e approvvigionamento IA (riepilogo)

| Tema | Evidence AIMO / mappatura | Note |
| --- | --- | --- |
| **ATRS UK** (registro di trasparenza IA) | Summary, review (responsabile della responsabilità), evidence (descrizione modello/sistema), dictionary (considerazioni di rischio). Profilo: `coverage_map/profiles/uk_atrs_procurement.json`. | Allegare o riferire registro di trasparenza tipo ATRS nei Formulari esterni; collegare agli oggetti del pacchetto per logical_id. |
| **Orientamento approvvigionamento UK** | Request, review, exception; Evidence Bundle per la valutazione dei fornitori. | Utilizzare il pacchetto AIMO per strutturare le evidence per la valutazione dell'approvvigionamento; l'orientamento ufficiale UK rimane autorevole. |

## Giappone: Approvvigionamento GenAI del governo e linee guida aziendali IA (riepilogo)

| Tema | Evidence AIMO / mappatura | Note |
| --- | --- | --- |
| **Elenco di controllo approvvigionamento GenAI governo JP** | Allegare l'elenco come Formulario esterno (es. payload: JP_PROCUREMENT_CHECKLIST); riferire nel manifest. Profilo: `coverage_map/profiles/jp_gov_genai_procurement.json`. | Solo mappatura di riferimento; AIMO non sostituisce gli elenchi ufficiali. |
| **Linee guida aziendali IA** | Summary, dictionary; mappare le voci dell'elenco ai codici della tassonomia AIMO quando utile per la tracciabilità. | Utilizzare per la spiegabilità; verificare contro l'orientamento ufficiale giapponese. |

## Come utilizzare

- **Formulari esterni**: Allegare modelli/elenchi ufficiali UK o Giappone **così come sono** (PDF, DOC, ecc.), eseguire l'hash e elencarli nel [payload_index](../../standard/current/09-evidence-bundle-structure/) dell'Evidence Bundle o nella [sezione Formulari esterni del Modello EV](../../standard/current/06-ev-template/). Riferirli per logical_id nel manifest e nelle mappature di copertura.
- **Profili**: I profili sopra definiscono mappature opzionali leggibili da macchina; non impongono obblighi legali o contrattuali.

Vedere [Conformità](../../conformance/) per i livelli e [Requisiti Minimi di Evidence — Overlay normativi](../../artifacts/minimum-evidence/) per il riepilogo degli overlay.
