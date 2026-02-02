---
description: Formato de Registro de Actividad de Agente - Esquema neutral a proveedores para ejercicio de privilegios de IA agéntica, ejecución de herramientas y monitoreo de operaciones recursivas en empresas.
---

# Formato de Registro de Actividad de Agente

## Propósito

Este esquema define un formato neutral a proveedores para registros que documentan **ejercicio de privilegios de IA agéntica, ejecución de herramientas y operaciones recursivas**. Permite a las organizaciones:

- Mantener un registro auditable de acciones de agentes autónomos
- Rastrear "quién hizo qué con qué autoridad" para cumplimiento e investigación de incidentes
- Soportar explicabilidad para operaciones de IA agéntica en contextos de auditoría

## Modelo de eventos

El esquema soporta cuatro tipos de eventos que capturan el ciclo de vida de operación agéntica:

| Tipo de Evento | Descripción |
| --- | --- |
| `agent_run` | Inicio o finalización de una sesión de ejecución de agente |
| `tool_call` | Agente invocando una herramienta o acción externa |
| `tool_result` | Resultado devuelto de una invocación de herramienta |
| `escalation` | Agente solicitando intervención humana o privilegios elevados |

## Campos requeridos (DEBE)

| Campo | Tipo | Descripción | Ejemplo |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | Marca de tiempo del evento | `2026-01-15T09:30:00Z` |
| `agent_id` | string | Identificador del agente | `agent-coding-assistant-v2` |
| `agent_version` | string | Versión del agente | `2.1.0` |
| `run_id` | string | Identificador único para esta ejecución/sesión | `run-20260115-abc123` |
| `event_type` | string | Tipo de evento | `agent_run`, `tool_call`, `tool_result`, `escalation` |
| `actor_id` | string | Usuario o servicio iniciador | `user@example.com` |
| `tool_name` | string | Nombre de la herramienta invocada | `file_write`, `api_call`, `shell_exec` |
| `tool_action` | string | Acción realizada por la herramienta | `create`, `read`, `update`, `delete`, `execute` |
| `tool_target` | string | Objetivo de la acción | `/path/to/file`, `https://api.example.com` |
| `auth_context` | string | Resumen de permiso/rol | `role:developer, scope:project-x` |
| `input_ref` | string | Hash o URI a la entrada (no el contenido en sí) | `sha256:def456...` |
| `output_ref` | string | Hash o URI a la salida (no el contenido en sí) | `sha256:ghi789...` |
| `decision` | string | Decisión de política aplicada | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | Referencia a evidencia relacionada | `urn:evidence:...` |

## Campos opcionales (DEBERÍA/PUEDE)

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `recursion_depth` | number | Profundidad de recursión actual para llamadas de agente anidadas |
| `retry_count` | number | Número de reintentos para esta acción |
| `policy_id` | string | Política que desencadenó la decisión |
| `prompt_template_id` | string | Identificador de plantilla de prompt |
| `model` | string | Modelo usado para esta acción |
| `latency_ms` | number | Latencia en milisegundos |
| `cost_estimate` | number | Costo estimado de esta acción |
| `error_code` | string | Código de error si la acción falló |

## Notas de seguridad

!!! warning "Suposiciones de riesgo agéntico"
    Al registrar actividad de IA agéntica, asuma los siguientes riesgos:

    - **Inyección de prompt**: Entradas maliciosas pueden intentar manipular el comportamiento del agente
    - **Sobre-privilegio**: Los agentes pueden tener permisos más amplios de lo previsto para una tarea específica
    - **Bucles recursivos**: Los agentes pueden entrar en patrones de ejecución recursiva no intencionales
    - **Deputy confundido**: Los agentes pueden ser engañados para actuar en nombre de partes no autorizadas

    El esquema está diseñado para capturar "quién hizo qué con qué autoridad" para soportar análisis post-incidente y explicaciones de auditoría. No previene estos riesgos; las organizaciones deben implementar salvaguardas apropiadas.

!!! warning "Manejo de datos"
    - **No incruste** secretos, credenciales o contenido sensible en `input_ref` o `output_ref`.
    - Use referencias hash o URIs seguros a contenido almacenado por separado.
    - Aplique controles de acceso y políticas de retención apropiados.

## JSON Schema

Descargar: [agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json)

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

## Páginas relacionadas

- [Índice de Esquemas de Registro](index.md)
- [Registro de Descubrimiento de Shadow AI](shadow-ai-discovery.md)
- [Requisitos Mínimos de Evidencia](../minimum-evidence.md)
- [Taxonomía: UC-010 Automatización Agéntica](../../standard/current/03-taxonomy.md)
