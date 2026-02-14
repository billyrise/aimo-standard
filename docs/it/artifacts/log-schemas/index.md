---
description: Schemi Log AIMO - Formati di log vendor-neutral per evidence IA. Include schemi per la scoperta di Shadow AI e il monitoraggio dell'attività degli agent.
---

# Schemi Log

## Che cos'è

Questa sezione definisce **formati di log normalizzati** per evidence che possono essere incluse in un Evidence Bundle. Questi schemi forniscono una struttura vendor-neutral per i log relativi al monitoraggio dell'uso dell'IA e alle operazioni agente.

## Quando utilizzarli

- **Visibilità Shadow AI**: Documentazione del rilevamento, inventario e remediation dell'uso non approvato dell'IA.
- **Audit delle operazioni agente**: Spiegazione dell'esercizio dei privilegi dell'agent autonomo, esecuzione degli strumenti e operazioni ricorsive.
- **Riproducibilità degli incidenti**: Fornire evidence strutturata per l'indagine degli incidenti e l'analisi delle cause profonde.

## Cosa NON è

!!! warning "Importante"
    Questi schemi definiscono **formati di log per la presentazione di evidence**. NON:

    - Raccolgono automaticamente i log dai vostri sistemi
    - Forniscono strumenti di aggregazione o monitoraggio dei log
    - Garantiscono la conformità a qualsiasi regolamento o standard
    - Sostituiscono le implementazioni di logging specifiche del vendor

    Le organizzazioni devono implementare le proprie pipeline di raccolta log e normalizzare i log secondo questi schemi per la presentazione di evidence.

## Schemi

| Schema | Scopo | Download |
| --- | --- | --- |
| [Log di Scoperta Shadow AI](shadow-ai-discovery/) | Rilevamento e inventario dell'uso non approvato dell'IA | [shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json) |
| [Log Attività Agent](agent-activity/) | Esercizio dei privilegi dell'IA agente ed esecuzione degli strumenti | [agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json) |

## Pagine correlate

- [Requisiti Minimi di Evidence](../minimum-evidence/) — Checklist MUST-level per evidence
- [Evidence Bundle](../evidence-bundle/) — Struttura del bundle e TOC
- [Tassonomia](../../standard/current/03-taxonomy/) — Codici di classificazione (inclusi UC-010 Automazione Agente, IM-007 Shadow/Non Gestito)
