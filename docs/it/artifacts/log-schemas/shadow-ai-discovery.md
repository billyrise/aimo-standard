---
description: Schema Log di Scoperta Shadow AI - Formato vendor-neutral per documentare il rilevamento, l'inventario e la remediation dell'uso non approvato dell'IA nelle aziende.
---
<!-- aimo:translation_status=translated -->

# Schema Log di Scoperta Shadow AI

## Scopo

Questo schema definisce un formato vendor-neutral per i log che documentano il rilevamento, l'inventario e la remediation dell'**uso non approvato dell'IA (Shadow AI)**. Permette alle organizzazioni di:

- Mantenere un registro verificabile degli eventi di rilevamento di Shadow AI
- Normalizzare i log da varie fonti (CASB, proxy, IdP, EDR, log di audit SaaS) in un formato coerente
- Supportare la presentazione di evidence per scopi di conformità e audit

## Principi di normalizzazione

| Principio | Descrizione |
| --- | --- |
| **Vendor-neutral** | Nessuna dipendenza da formati di log specifici del vendor; applicabile a Netskope, Zscaler, Microsoft Defender e altri |
| **Campi obbligatori minimi** | Solo i campi essenziali sono MUST; le organizzazioni possono omettere i campi opzionali |
| **Estensibile** | `additionalProperties: true` permette estensioni specifiche del vendor o dell'organizzazione |
| **Consapevole della privacy** | I campi sono progettati per referenziare (non incorporare) contenuti sensibili |

## Campi obbligatori (MUST)

| Campo | Tipo | Descrizione | Esempio |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | Timestamp dell'evento | `2026-01-15T09:30:00Z` |
| `actor_id` | string | Identificatore utente o servizio | `user@example.com` |
| `actor_type` | string | Tipo di attore | `user` o `service` |
| `source_system` | string | Sistema che ha rilevato l'evento | `proxy`, `casb`, `idp`, `edr`, `saas_audit` |
| `ai_service` | string | Prodotto o dominio IA acceduto | `chat.openai.com`, `claude.ai` |
| `action` | string | Azione eseguita | `chat`, `upload`, `download`, `tool_execute`, `api_call` |
| `data_classification` | string | Livello di classificazione dei dati | `public`, `internal`, `confidential`, `restricted` |
| `decision` | string | Decisione di policy applicata | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | Riferimento all'evidence correlata | `sha256:abc123...` o `urn:evidence:...` |
| `record_id` | string | Identificatore univoco per questo record | `evt-20260115-001` |

## Campi opzionali (SHOULD/MAY)

| Campo | Tipo | Descrizione |
| --- | --- | --- |
| `session_id` | string | Identificatore di sessione |
| `device_id` | string | Identificatore del dispositivo |
| `ip` | string | Indirizzo IP |
| `user_agent` | string | Stringa user agent |
| `department` | string | Dipartimento organizzativo |
| `project_id` | string | Identificatore del progetto |
| `prompt_category` | string | Categoria del prompt/query |
| `model_family` | string | Famiglia del modello IA (es. GPT-4, Claude) |
| `destination` | string | URL o endpoint di destinazione |
| `policy_id` | string | Policy che ha attivato la decisione |
| `remediation_ticket` | string | Riferimento al ticket di remediation |

## Note su privacy/sicurezza

!!! warning "Gestione dei dati"
    - **Non incorporare** PII, credenziali o contenuto dei prompt direttamente nei campi del log.
    - Utilizzare `evidence_ref` per referenziare contenuti sensibili memorizzati separatamente.
    - Applicare controlli di accesso appropriati allo storage dei log.
    - Considerare politiche di conservazione dei dati allineate con i [Requisiti Minimi di Evidence](../../minimum-evidence/).

## JSON Schema

Download: [shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "event_time", "actor_id", "actor_type", "source_system",
    "ai_service", "action", "data_classification", "decision",
    "evidence_ref", "record_id"
  ],
  "properties": {
    "event_time": { "type": "string", "format": "date-time" },
    "actor_id": { "type": "string", "minLength": 1 },
    "actor_type": { "type": "string", "enum": ["user", "service"] },
    "source_system": { "type": "string", "minLength": 1 },
    "ai_service": { "type": "string", "minLength": 1 },
    "action": { "type": "string", "minLength": 1 },
    "data_classification": { "type": "string", "minLength": 1 },
    "decision": { "type": "string", "enum": ["allow", "block", "needs_review", "unknown"] },
    "evidence_ref": { "type": "string", "minLength": 1 },
    "record_id": { "type": "string", "minLength": 1 }
  },
  "additionalProperties": true
}
```

## Pagine correlate

- [Indice Log Schemas](../)
- [Log Attività Agent](../agent-activity/)
- [Requisiti Minimi di Evidence](../../minimum-evidence/)
- [Tassonomia: IM-007 Shadow/Non Gestito](../../../standard/current/03-taxonomy/)
