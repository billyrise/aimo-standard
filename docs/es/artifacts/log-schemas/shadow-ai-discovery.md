---
description: Esquema de Registro de Descubrimiento de Shadow AI - Formato neutral a proveedores para documentar detección, inventario y remediación de uso no aprobado de IA en empresas.
---
<!-- aimo:translation_status=translated -->

# Esquema de Registro de Descubrimiento de Shadow AI

## Propósito

Este esquema define un formato neutral a proveedores para registros que documentan la detección, inventario y remediación de **uso no aprobado de IA (Shadow AI)**. Permite a las organizaciones:

- Mantener un registro auditable de eventos de detección de Shadow AI
- Normalizar registros de diversas fuentes (CASB, proxy, IdP, EDR, registros de auditoría SaaS) en un formato consistente
- Soportar envío de evidencia para propósitos de cumplimiento y auditoría

## Principios de normalización

| Principio | Descripción |
| --- | --- |
| **Neutral a proveedores** | Sin dependencia de formatos de registro de proveedores específicos; aplicable a Netskope, Zscaler, Microsoft Defender y otros |
| **Campos requeridos mínimos** | Solo los campos esenciales son DEBE; las organizaciones pueden omitir campos opcionales |
| **Extensible** | `additionalProperties: true` permite extensiones específicas de proveedor u organización |
| **Consciente de privacidad** | Los campos están diseñados para referenciar (no incrustar) contenido sensible |

## Campos requeridos (DEBE)

| Campo | Tipo | Descripción | Ejemplo |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | Marca de tiempo del evento | `2026-01-15T09:30:00Z` |
| `actor_id` | string | Identificador de usuario o servicio | `user@example.com` |
| `actor_type` | string | Tipo de actor | `user` o `service` |
| `source_system` | string | Sistema que detectó el evento | `proxy`, `casb`, `idp`, `edr`, `saas_audit` |
| `ai_service` | string | Producto de IA o dominio accedido | `chat.openai.com`, `claude.ai` |
| `action` | string | Acción realizada | `chat`, `upload`, `download`, `tool_execute`, `api_call` |
| `data_classification` | string | Nivel de clasificación de datos | `public`, `internal`, `confidential`, `restricted` |
| `decision` | string | Decisión de política aplicada | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | Referencia a evidencia relacionada | `sha256:abc123...` o `urn:evidence:...` |
| `record_id` | string | Identificador único para este registro | `evt-20260115-001` |

## Campos opcionales (DEBERÍA/PUEDE)

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `session_id` | string | Identificador de sesión |
| `device_id` | string | Identificador de dispositivo |
| `ip` | string | Dirección IP |
| `user_agent` | string | Cadena de user agent |
| `department` | string | Departamento organizacional |
| `project_id` | string | Identificador de proyecto |
| `prompt_category` | string | Categoría del prompt/consulta |
| `model_family` | string | Familia del modelo de IA (ej., GPT-4, Claude) |
| `destination` | string | URL o endpoint de destino |
| `policy_id` | string | Política que desencadenó la decisión |
| `remediation_ticket` | string | Referencia a ticket de remediación |

## Notas de privacidad/seguridad

!!! warning "Manejo de datos"
    - **No incruste** PII, credenciales o contenido de prompts directamente en campos de registro.
    - Use `evidence_ref` para referenciar contenido sensible almacenado por separado.
    - Aplique controles de acceso apropiados al almacenamiento de registros.
    - Considere políticas de retención de datos alineadas con [Requisitos Mínimos de Evidencia](../../minimum-evidence/).

## JSON Schema

Descargar: [shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json)

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

## Páginas relacionadas

- [Índice de Esquemas de Registro](../)
- [Registro de Actividad de Agente](../agent-activity/)
- [Requisitos Mínimos de Evidencia](../../minimum-evidence/)
- [Taxonomía: IM-007 Shadow/No Gestionado](../../../standard/current/03-taxonomy/)
