---
description: Mappatura dello Standard AIMO verso l'EU AI Act. Tracciabilità tra i codici della tassonomia AIMO e le categorie di rischio e i requisiti dell'EU AI Act.
---

# Mappatura EU AI Act

> Scorciatoie di tracciabilità: Tassonomia → Requisiti Minimi di Evidence → Validator → Protocollo di Supervisione Umana.

- [Tassonomia](../standard/current/03-taxonomy.md)
- [Requisiti Minimi di Evidence](../artifacts/minimum-evidence.md)
- [Schemi Log](../artifacts/log-schemas/index.md)
- [Validator](../validator/index.md)
- [Protocollo di Supervisione Umana](../governance/human-oversight-protocol.md)

Questa pagina mappa temi selezionati dell'EU AI Act (documentazione, conservazione dei registri, gestione del rischio, supervisione umana, trasparenza) verso evidence e artefatti AIMO. È solo di alto livello e **non** costituisce consulenza legale né garantisce la conformità. Verificare contro il testo legale ufficiale.


## Tabella di mappatura

| Riferimento framework / argomento | Evidence AIMO / dove in AIMO | Evidence Bundle / Requisiti Minimi | Artefatti & validazione | Note |
| --- | --- | --- | --- | --- |
| Art 9 – Gestione del rischio (obblighi) | [Ambito](../standard/current/02-scope.md) | richiesta, revisione, eccezione | templates/ev/ | Solo alto livello; non consulenza legale. Verificare contro il testo ufficiale. |
| Art 10 – Governance dei dati | [Dizionario](../standard/current/05-dictionary.md) | Dizionario, EV | schemas/jsonschema/; schema_validate_dictionary | Solo alto livello; non consulenza legale. Verificare contro il testo ufficiale. |
| Art 11 – Documentazione (alto rischio) | [Template EV](../standard/current/06-ev-template.md), [Evidence Bundle](../artifacts/evidence-bundle.md) | EV, Dizionario, Riepilogo; richiesta, revisione | schemas/jsonschema/, templates/ev/; schema_validate_ev | Solo alto livello; non consulenza legale. Verificare contro il testo ufficiale. |
| Art 12 – Conservazione dei registri | [Evidence Bundle](../artifacts/evidence-bundle.md), [Requisiti Minimi](../artifacts/minimum-evidence.md) | EV, change_log, richiesta, revisione | examples/evidence_bundle_minimal/; schema_validate_ev | Solo alto livello; non consulenza legale. Verificare contro il testo ufficiale. |
| Art 13 – Trasparenza (informazioni utente) | [Ambito](../standard/current/02-scope.md) | Riepilogo, EV; revisione | templates/ev/ | Solo alto livello; non consulenza legale. Verificare contro il testo ufficiale. |
| Art 14 – Supervisione umana | [Requisiti Minimi](../artifacts/minimum-evidence.md) | revisione, eccezione; revisione, eccezione | templates/ev/ev_template.md | Solo alto livello; non consulenza legale. Verificare contro il testo ufficiale. |
| Art 17 – Gestione del rischio (alto rischio) | [Ambito](../standard/current/02-scope.md) | richiesta, revisione, eccezione, rinnovo | templates/ev/ | Solo alto livello; non consulenza legale. Verificare contro il testo ufficiale. |
| Art 26 – Trasparenza (rischio limitato) | [Ambito](../standard/current/02-scope.md) | Riepilogo, EV; revisione | templates/ev/ | Solo alto livello; non consulenza legale. Verificare contro il testo ufficiale. |
| Art 29 – Documentazione (IA di uso generale) | [Template EV](../standard/current/06-ev-template.md) | EV, Dizionario, Riepilogo; richiesta, revisione | schemas/jsonschema/; schema_validate_ev | Solo alto livello; non consulenza legale. Verificare contro il testo ufficiale. |
| Art 52 – Trasparenza (deployer) | [Requisiti Minimi](../artifacts/minimum-evidence.md) | EV, Riepilogo; revisione | templates/ev/ | Solo alto livello; non consulenza legale. Verificare contro il testo ufficiale. |
| Considerando – Responsabilità | [Evidence Bundle](../artifacts/evidence-bundle.md) | EV, richiesta, revisione, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | Solo alto livello; non consulenza legale. Verificare contro il testo ufficiale. |
