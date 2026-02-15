---
description: Shadow AI Discovery Log Schema - Herstellerneutrales Format zur Dokumentation von Erkennung, Inventarisierung und Behebung nicht genehmigter KI-Nutzung in Unternehmen.
---
<!-- aimo:translation_status=translated -->

# Shadow AI Discovery Log Schema

## Zweck

Dieses Schema definiert ein herstellerneutrales Format für Protokolle, die die Erkennung, Inventarisierung und Behebung **nicht genehmigter KI-Nutzung (Shadow AI)** dokumentieren. Es ermöglicht Organisationen:

- Eine auditierbare Aufzeichnung von Shadow AI-Erkennungsereignissen zu führen
- Protokolle aus verschiedenen Quellen (CASB, Proxy, IdP, EDR, SaaS-Audit-Logs) in ein konsistentes Format zu normalisieren
- Evidence-Einreichung für Compliance- und Auditzwecke zu unterstützen

## Normalisierungsprinzipien

| Prinzip | Beschreibung |
| --- | --- |
| **Herstellerneutral** | Keine Abhängigkeit von spezifischen Hersteller-Log-Formaten; anwendbar auf Netskope, Zscaler, Microsoft Defender und andere |
| **Minimale erforderliche Felder** | Nur wesentliche Felder sind MUSS; Organisationen können optionale Felder weglassen |
| **Erweiterbar** | `additionalProperties: true` ermöglicht herstellerspezifische oder organisationsspezifische Erweiterungen |
| **Datenschutzbewusst** | Felder sind darauf ausgelegt, sensible Inhalte zu referenzieren (nicht einzubetten) |

## Erforderliche Felder (MUSS)

| Feld | Typ | Beschreibung | Beispiel |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | Zeitstempel des Ereignisses | `2026-01-15T09:30:00Z` |
| `actor_id` | string | Benutzer- oder Dienstidentifikator | `user@example.com` |
| `actor_type` | string | Typ des Akteurs | `user` oder `service` |
| `source_system` | string | System, das das Ereignis erkannt hat | `proxy`, `casb`, `idp`, `edr`, `saas_audit` |
| `ai_service` | string | Aufgerufenes KI-Produkt oder Domain | `chat.openai.com`, `claude.ai` |
| `action` | string | Ausgeführte Aktion | `chat`, `upload`, `download`, `tool_execute`, `api_call` |
| `data_classification` | string | Datenklassifizierungsstufe | `public`, `internal`, `confidential`, `restricted` |
| `decision` | string | Angewandte Policy-Entscheidung | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | Verweis auf zugehöriges Evidence | `sha256:abc123...` oder `urn:evidence:...` |
| `record_id` | string | Eindeutiger Identifikator für diesen Datensatz | `evt-20260115-001` |

## Optionale Felder (SOLLTE/KANN)

| Feld | Typ | Beschreibung |
| --- | --- | --- |
| `session_id` | string | Sitzungsidentifikator |
| `device_id` | string | Geräteidentifikator |
| `ip` | string | IP-Adresse |
| `user_agent` | string | User-Agent-String |
| `department` | string | Organisationsabteilung |
| `project_id` | string | Projektidentifikator |
| `prompt_category` | string | Kategorie des Prompts/der Anfrage |
| `model_family` | string | KI-Modellfamilie (z.B. GPT-4, Claude) |
| `destination` | string | Ziel-URL oder Endpunkt |
| `policy_id` | string | Policy, die die Entscheidung ausgelöst hat |
| `remediation_ticket` | string | Referenz auf Behebungsticket |

## Datenschutz-/Sicherheitshinweise

!!! warning "Datenhandhabung"
    - **Betten Sie keine** personenbezogenen Daten, Anmeldeinformationen oder Prompt-Inhalte direkt in Log-Felder ein.
    - Verwenden Sie `evidence_ref`, um separat gespeicherte sensible Inhalte zu referenzieren.
    - Wenden Sie entsprechende Zugriffskontrollen auf die Log-Speicherung an.
    - Berücksichtigen Sie Datenaufbewahrungsrichtlinien, die an den [Mindestanforderungen an Evidence](../../minimum-evidence/) ausgerichtet sind.

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

## Verwandte Seiten

- [Log Schemas-Index](../)
- [Agent Activity Log](../agent-activity/)
- [Mindestanforderungen an Evidence](../../minimum-evidence/)
- [Taxonomie: IM-007 Shadow/Unmanaged](../../../standard/current/03-taxonomy/)
