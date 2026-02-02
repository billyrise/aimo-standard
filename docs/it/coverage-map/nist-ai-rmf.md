---
description: Mappatura dello Standard AIMO verso NIST AI RMF. Tracciabilità tra i codici della tassonomia AIMO e le funzioni del NIST AI Risk Management Framework.
---

# Mappatura NIST AI RMF

> Scorciatoie di tracciabilità: Tassonomia → Requisiti Minimi di Evidence → Validator → Protocollo di Supervisione Umana.

- [Tassonomia](../standard/current/03-taxonomy.md)
- [Requisiti Minimi di Evidence](../artifacts/minimum-evidence.md)
- [Schemi Log](../artifacts/log-schemas/index.md)
- [Validator](../validator/index.md)
- [Protocollo di Supervisione Umana](../governance/human-oversight-protocol.md)

Questa pagina mappa temi selezionati del NIST AI Risk Management Framework (Govern, Map, Measure, Manage) verso evidence e artefatti AIMO. È solo per la spiegabilità; non garantisce la conformità al NIST AI RMF. Verificare contro la pubblicazione NIST.


## Tabella di mappatura

| Riferimento framework / argomento | Evidence AIMO / dove in AIMO | Evidence Bundle / Requisiti Minimi | Artefatti & validazione | Note |
| --- | --- | --- | --- | --- |
| Govern 1.1 – Politiche | [Ambito](../standard/current/02-scope.md), [Tassonomia](../standard/current/03-taxonomy.md) | Dizionario, Riepilogo, revisione; revisione | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativo; verificare contro la pubblicazione NIST. |
| Govern 1.2 – Ruoli e responsabilità | [Requisiti Minimi](../artifacts/minimum-evidence.md) | richiesta, revisione | templates/ev/ev_template.md | Informativo; verificare contro la pubblicazione NIST. |
| Govern 2.1 – Responsabilità | [Evidence Bundle](../artifacts/evidence-bundle.md) | EV, richiesta, revisione, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | Informativo; verificare contro la pubblicazione NIST. |
| Govern 3.1 – Gestione del rischio | [Ambito](../standard/current/02-scope.md) | richiesta, revisione, eccezione | templates/ev/ | Informativo; verificare contro la pubblicazione NIST. |
| Govern 4.1 – Cultura | [Panoramica](../standard/current/01-overview.md) | Riepilogo, revisione; revisione | — | Informativo; verificare contro la pubblicazione NIST. |
| Map 1.1 – Mappatura del contesto | [Ambito](../standard/current/02-scope.md), [Dizionario](../standard/current/05-dictionary.md) | Dizionario, Riepilogo; richiesta | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativo; verificare contro la pubblicazione NIST. |
| Map 2.1 – Dati e documentazione | [Template EV](../standard/current/06-ev-template.md) | EV, Dizionario, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informativo; verificare contro la pubblicazione NIST. |
| Map 3.1 – Governance dei dati | [Dizionario](../standard/current/05-dictionary.md) | Dizionario, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativo; verificare contro la pubblicazione NIST. |
| Measure 1.1 – Performance e impatto | [Template EV](../standard/current/06-ev-template.md) | EV | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informativo; verificare contro la pubblicazione NIST. |
| Measure 2.1 – Monitoraggio | [Requisiti Minimi](../artifacts/minimum-evidence.md) | EV, change_log; change_log, integrità | templates/ev/ | Informativo; verificare contro la pubblicazione NIST. |
| Measure 3.1 – Test e validazione | [Validator](../standard/current/07-validator.md) | EV | validator/rules/, validator/src/; schema_validate_ev | Informativo; verificare contro la pubblicazione NIST. |
| Manage 1.1 – Allocazione delle risorse | [Panoramica](../standard/current/01-overview.md) | Riepilogo, revisione; revisione | — | Informativo; verificare contro la pubblicazione NIST. |
| Manage 2.1 – Incidenti e risposte | [Requisiti Minimi](../artifacts/minimum-evidence.md) | eccezione, rinnovo, change_log | templates/ev/ev_template.md | Informativo; verificare contro la pubblicazione NIST. |
| Manage 3.1 – Gestione delle modifiche | [Evidence Bundle](../artifacts/evidence-bundle.md) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | Informativo; verificare contro la pubblicazione NIST. |
| Manage 4.1 – Revisione e aggiornamento | [Requisiti Minimi](../artifacts/minimum-evidence.md) | rinnovo, revisione; revisione, rinnovo | templates/ev/ | Informativo; verificare contro la pubblicazione NIST. |
| Manage 5.1 – Comunicazione | [Evidence Bundle](../artifacts/evidence-bundle.md) | Riepilogo, change_log; change_log | templates/ev/ | Informativo; verificare contro la pubblicazione NIST. |
