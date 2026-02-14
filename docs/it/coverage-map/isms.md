---
description: Mappatura dello Standard AIMO verso ISMS (ISO 27001/27002). Tracciabilità tra la tassonomia AIMO e i controlli del sistema di gestione della sicurezza delle informazioni.
---

# Vista ISMS (ISO/IEC 27001/27002) mappatura

> Scorciatoie di tracciabilità: Tassonomia → Requisiti Minimi di Evidence → Validator → Protocollo di Supervisione Umana.

- [Tassonomia](../../standard/current/03-taxonomy/)
- [Requisiti Minimi di Evidence](../../artifacts/minimum-evidence/)
- [Schemi Log](../../artifacts/log-schemas/)
- [Validator](../../validator/)
- [Protocollo di Supervisione Umana](../../governance/human-oversight-protocol/)

Questa pagina mappa temi selezionati di ISO/IEC 27001/27002 (gestione delle modifiche, controllo degli accessi, logging, integrità dell'evidence) verso evidence e artefatti AIMO. È solo per la spiegabilità; non garantisce la conformità a ISO/IEC 27001 o 27002. Verificare contro gli standard pubblicati.


## Tabella di mappatura

| Riferimento framework / argomento | Evidence AIMO / dove in AIMO | Evidence Bundle / Requisiti Minimi | Artefatti & validazione | Note |
| --- | --- | --- | --- | --- |
| A.5.24 – Sicurezza delle informazioni nella gestione dei progetti | [Ambito](../../standard/current/02-scope/) | richiesta, revisione | templates/ev/ | Informativo; verificare contro il testo ufficiale. |
| A.5.29 – Sicurezza delle informazioni durante le interruzioni | [Requisiti Minimi](../../artifacts/minimum-evidence/) | eccezione, rinnovo | templates/ev/ev_template.md | Informativo; verificare contro il testo ufficiale. |
| A.5.30 – Prontezza ICT per la continuità operativa | [Panoramica](../../standard/current/01-overview/) | Riepilogo; integrità | — | Informativo; verificare contro il testo ufficiale. |
| A.8.1 – Inventario degli asset | [Dizionario](../../standard/current/05-dictionary/) | Dizionario, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativo; verificare contro il testo ufficiale. |
| A.8.2 – Classificazione delle informazioni | [Tassonomia](../../standard/current/03-taxonomy/) | Dizionario; revisione | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativo; verificare contro il testo ufficiale. |
| A.8.3 – Controllo degli accessi | [Requisiti Minimi](../../artifacts/minimum-evidence/) | —; integrità | — | Informativo; verificare contro il testo ufficiale. |
| A.8.15 – Logging | [Template EV](../../standard/current/06-ev-template/) | EV, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informativo; verificare contro il testo ufficiale. |
| A.8.16 – Attività di monitoraggio | [Requisiti Minimi](../../artifacts/minimum-evidence/) | EV, change_log; change_log, integrità | templates/ev/ | Informativo; verificare contro il testo ufficiale. |
| A.8.32 – Gestione delle modifiche | [Evidence Bundle](../../artifacts/evidence-bundle/) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | Informativo; verificare contro il testo ufficiale. |
| A.8.33 – Informazioni di test | [Validator](../../standard/current/07-validator/) | EV | validator/rules/, validator/src/; schema_validate_ev | Informativo; verificare contro il testo ufficiale. |
