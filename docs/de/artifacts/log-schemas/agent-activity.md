---
description: Agent Activity Log-Format - Herstellerneutrales Schema für die Überwachung von agentenbasierter KI-Berechtigungsausübung, Tool-Ausführung und rekursiven Operationen in Unternehmen.
---

# Agent Activity Log-Format

## Zweck

Dieses Schema definiert ein herstellerneutrales Format für Protokolle, die **agentenbasierte KI-Berechtigungsausübung, Tool-Ausführung und rekursive Operationen** dokumentieren. Es ermöglicht Organisationen:

- Eine auditierbare Aufzeichnung autonomer Agentenaktionen zu führen
- "Wer hat was mit welcher Berechtigung getan" für Compliance und Incident-Untersuchungen nachzuverfolgen
- Erklärbarkeit für agentenbasierte KI-Operationen im Audit-Kontext zu unterstützen

## Ereignismodell

Das Schema unterstützt vier Ereignistypen, die den Lebenszyklus agentenbasierter Operationen erfassen:

| Ereignistyp | Beschreibung |
| --- | --- |
| `agent_run` | Start oder Abschluss einer Agenten-Ausführungssitzung |
| `tool_call` | Agent ruft ein Tool oder eine externe Aktion auf |
| `tool_result` | Ergebnis, das von einem Tool-Aufruf zurückgegeben wird |
| `escalation` | Agent fordert menschliches Eingreifen oder erhöhte Berechtigungen an |

## Erforderliche Felder (MUSS)

| Feld | Typ | Beschreibung | Beispiel |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | Zeitstempel des Ereignisses | `2026-01-15T09:30:00Z` |
| `agent_id` | string | Identifikator des Agenten | `agent-coding-assistant-v2` |
| `agent_version` | string | Version des Agenten | `2.1.0` |
| `run_id` | string | Eindeutiger Identifikator für diesen Lauf/diese Sitzung | `run-20260115-abc123` |
| `event_type` | string | Typ des Ereignisses | `agent_run`, `tool_call`, `tool_result`, `escalation` |
| `actor_id` | string | Initiierender Benutzer oder Dienst | `user@example.com` |
| `tool_name` | string | Name des aufgerufenen Tools | `file_write`, `api_call`, `shell_exec` |
| `tool_action` | string | Vom Tool ausgeführte Aktion | `create`, `read`, `update`, `delete`, `execute` |
| `tool_target` | string | Ziel der Aktion | `/path/to/file`, `https://api.example.com` |
| `auth_context` | string | Berechtigungs-/Rollenzusammenfassung | `role:developer, scope:project-x` |
| `input_ref` | string | Hash oder URI zur Eingabe (nicht der Inhalt selbst) | `sha256:def456...` |
| `output_ref` | string | Hash oder URI zur Ausgabe (nicht der Inhalt selbst) | `sha256:ghi789...` |
| `decision` | string | Angewandte Policy-Entscheidung | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | Verweis auf zugehöriges Evidence | `urn:evidence:...` |

## Optionale Felder (SOLLTE/KANN)

| Feld | Typ | Beschreibung |
| --- | --- | --- |
| `recursion_depth` | number | Aktuelle Rekursionstiefe für verschachtelte Agentenaufrufe |
| `retry_count` | number | Anzahl der Wiederholungsversuche für diese Aktion |
| `policy_id` | string | Policy, die die Entscheidung ausgelöst hat |
| `prompt_template_id` | string | Prompt-Template-Identifikator |
| `model` | string | Für diese Aktion verwendetes Modell |
| `latency_ms` | number | Latenz in Millisekunden |
| `cost_estimate` | number | Geschätzte Kosten dieser Aktion |
| `error_code` | string | Fehlercode, falls die Aktion fehlgeschlagen ist |

## Sicherheitshinweise

!!! warning "Risikoannahmen für agentenbasierte KI"
    Bei der Protokollierung agentenbasierter KI-Aktivitäten sind folgende Risiken anzunehmen:

    - **Prompt Injection**: Böswillige Eingaben können versuchen, das Agentenverhalten zu manipulieren
    - **Überberechtigungen**: Agenten haben möglicherweise breitere Berechtigungen als für eine bestimmte Aufgabe vorgesehen
    - **Rekursive Schleifen**: Agenten können in unbeabsichtigte rekursive Ausführungsmuster geraten
    - **Confused Deputy**: Agenten können dazu verleitet werden, im Namen nicht autorisierter Parteien zu handeln

    Das Schema ist darauf ausgelegt, "wer hat was mit welcher Berechtigung getan" zu erfassen, um Post-Incident-Analysen und Audit-Erklärungen zu unterstützen. Es verhindert diese Risiken nicht; Organisationen müssen entsprechende Schutzmaßnahmen implementieren.

!!! warning "Datenhandhabung"
    - **Betten Sie keine** Geheimnisse, Anmeldeinformationen oder sensible Inhalte in `input_ref` oder `output_ref` ein.
    - Verwenden Sie Hash-Referenzen oder sichere URIs zu separat gespeicherten Inhalten.
    - Wenden Sie entsprechende Zugriffskontrollen und Aufbewahrungsrichtlinien an.

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

## Verwandte Seiten

- [Log Schemas-Index](index.md)
- [Shadow AI Discovery Log](shadow-ai-discovery.md)
- [Mindestanforderungen an Evidence](../minimum-evidence.md)
- [Taxonomie: UC-010 Agentic Automation](../../standard/current/03-taxonomy.md)
