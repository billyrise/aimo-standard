---
description: Formato Log Attività Agent - Schema vendor-neutral per l'esercizio dei privilegi dell'IA agente, esecuzione di strumenti e monitoraggio delle operazioni ricorsive nelle aziende.
---
<!-- aimo:translation_status=translated -->

# Formato Log Attività Agent

## Scopo

Questo schema definisce un formato vendor-neutral per i log che documentano **l'esercizio dei privilegi dell'IA agente, l'esecuzione di strumenti e le operazioni ricorsive**. Permette alle organizzazioni di:

- Mantenere un registro verificabile delle azioni degli agent autonomi
- Tracciare "chi ha fatto cosa con quale autorità" per conformità e indagini sugli incidenti
- Supportare la spiegabilità per le operazioni dell'IA agente nei contesti di audit

## Modello degli eventi

Lo schema supporta quattro tipi di eventi che catturano il ciclo di vita dell'operazione agente:

| Tipo di Evento | Descrizione |
| --- | --- |
| `agent_run` | Avvio o completamento di una sessione di esecuzione dell'agent |
| `tool_call` | Agent che invoca uno strumento o un'azione esterna |
| `tool_result` | Risultato restituito da un'invocazione di strumento |
| `escalation` | Agent che richiede intervento umano o privilegi elevati |

## Campi obbligatori (MUST)

| Campo | Tipo | Descrizione | Esempio |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | Timestamp dell'evento | `2026-01-15T09:30:00Z` |
| `agent_id` | string | Identificatore dell'agent | `agent-coding-assistant-v2` |
| `agent_version` | string | Versione dell'agent | `2.1.0` |
| `run_id` | string | Identificatore univoco per questa esecuzione/sessione | `run-20260115-abc123` |
| `event_type` | string | Tipo di evento | `agent_run`, `tool_call`, `tool_result`, `escalation` |
| `actor_id` | string | Utente o servizio che ha avviato | `user@example.com` |
| `tool_name` | string | Nome dello strumento invocato | `file_write`, `api_call`, `shell_exec` |
| `tool_action` | string | Azione eseguita dallo strumento | `create`, `read`, `update`, `delete`, `execute` |
| `tool_target` | string | Target dell'azione | `/path/to/file`, `https://api.example.com` |
| `auth_context` | string | Riepilogo permessi/ruolo | `role:developer, scope:project-x` |
| `input_ref` | string | Hash o URI dell'input (non il contenuto stesso) | `sha256:def456...` |
| `output_ref` | string | Hash o URI dell'output (non il contenuto stesso) | `sha256:ghi789...` |
| `decision` | string | Decisione di policy applicata | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | Riferimento all'evidence correlata | `urn:evidence:...` |

## Campi opzionali (SHOULD/MAY)

| Campo | Tipo | Descrizione |
| --- | --- | --- |
| `recursion_depth` | number | Profondità di ricorsione corrente per chiamate agent annidate |
| `retry_count` | number | Numero di tentativi per questa azione |
| `policy_id` | string | Policy che ha attivato la decisione |
| `prompt_template_id` | string | Identificatore del template di prompt |
| `model` | string | Modello utilizzato per questa azione |
| `latency_ms` | number | Latenza in millisecondi |
| `cost_estimate` | number | Costo stimato di questa azione |
| `error_code` | string | Codice di errore se l'azione è fallita |

## Note sulla sicurezza

!!! warning "Assunzioni di rischio agente"
    Quando si registra l'attività dell'IA agente, assumere i seguenti rischi:

    - **Prompt injection**: Input malevoli possono tentare di manipolare il comportamento dell'agent
    - **Eccesso di privilegi**: Gli agent possono avere permessi più ampi del previsto per un'attività specifica
    - **Loop ricorsivi**: Gli agent possono entrare in pattern di esecuzione ricorsiva non intenzionali
    - **Confused deputy**: Gli agent possono essere ingannati ad agire per conto di parti non autorizzate

    Lo schema è progettato per catturare "chi ha fatto cosa con quale autorità" per supportare l'analisi post-incidente e le spiegazioni di audit. Non previene questi rischi; le organizzazioni devono implementare appropriate misure di protezione.

!!! warning "Gestione dei dati"
    - **Non incorporare** segreti, credenziali o contenuti sensibili in `input_ref` o `output_ref`.
    - Utilizzare riferimenti hash o URI sicuri a contenuti memorizzati separatamente.
    - Applicare controlli di accesso e politiche di conservazione appropriati.

## JSON Schema

Download: [agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "event_time", "agent_id", "agent_version", "run_id", "event_type",
    "actor_id", "tool_name", "tool_action", "tool_target", "auth_context",
    "input_ref", "output_ref", "decision", "evidence_ref"
  ],
  "properties": {
    "event_time": { "type": "string", "format": "date-time" },
    "agent_id": { "type": "string", "minLength": 1 },
    "agent_version": { "type": "string", "minLength": 1 },
    "run_id": { "type": "string", "minLength": 1 },
    "event_type": { "type": "string", "enum": ["agent_run", "tool_call", "tool_result", "escalation"] },
    "actor_id": { "type": "string", "minLength": 1 },
    "tool_name": { "type": "string", "minLength": 1 },
    "tool_action": { "type": "string", "minLength": 1 },
    "tool_target": { "type": "string", "minLength": 1 },
    "auth_context": { "type": "string", "minLength": 1 },
    "input_ref": { "type": "string", "minLength": 1 },
    "output_ref": { "type": "string", "minLength": 1 },
    "decision": { "type": "string", "enum": ["allow", "block", "needs_review", "unknown"] },
    "evidence_ref": { "type": "string", "minLength": 1 }
  },
  "additionalProperties": true
}
```

## Pagine correlate

- [Indice Log Schemas](../)
- [Log di Scoperta Shadow AI](../shadow-ai-discovery/)
- [Requisiti Minimi di Evidence](../../minimum-evidence/)
- [Tassonomia: UC-010 Automazione Agente](../../../standard/current/03-taxonomy/)
