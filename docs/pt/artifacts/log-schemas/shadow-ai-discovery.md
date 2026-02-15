---
description: Schema de Log de Descoberta de Shadow AI - Formato neutro de fornecedor para documentar detecção, inventário e remediação de uso não aprovado de IA em empresas.
---
<!-- aimo:translation_status=translated -->

# Schema de Log de Descoberta de Shadow AI

## Propósito

Este schema define um formato neutro de fornecedor para logs que documentam a detecção, inventário e remediação de **uso não aprovado de IA (Shadow AI)**. Ele permite que organizações:

- Mantenham um registro auditável de eventos de detecção de Shadow AI
- Normalizem logs de várias fontes (CASB, proxy, IdP, EDR, logs de auditoria SaaS) em um formato consistente
- Suportem submissão de evidências para fins de conformidade e auditoria

## Princípios de normalização

| Princípio | Descrição |
| --- | --- |
| **Neutro de fornecedor** | Sem dependência de formatos de log de fornecedores específicos; aplicável a Netskope, Zscaler, Microsoft Defender e outros |
| **Campos obrigatórios mínimos** | Apenas campos essenciais são DEVE; organizações podem omitir campos opcionais |
| **Extensível** | `additionalProperties: true` permite extensões específicas de fornecedor ou organização |
| **Consciente de privacidade** | Campos são projetados para referenciar (não incorporar) conteúdo sensível |

## Campos obrigatórios (DEVE)

| Campo | Tipo | Descrição | Exemplo |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | Timestamp do evento | `2026-01-15T09:30:00Z` |
| `actor_id` | string | Identificador de usuário ou serviço | `user@example.com` |
| `actor_type` | string | Tipo de ator | `user` ou `service` |
| `source_system` | string | Sistema que detectou o evento | `proxy`, `casb`, `idp`, `edr`, `saas_audit` |
| `ai_service` | string | Produto ou domínio de IA acessado | `chat.openai.com`, `claude.ai` |
| `action` | string | Ação realizada | `chat`, `upload`, `download`, `tool_execute`, `api_call` |
| `data_classification` | string | Nível de classificação de dados | `public`, `internal`, `confidential`, `restricted` |
| `decision` | string | Decisão de política aplicada | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | Referência a evidência relacionada | `sha256:abc123...` ou `urn:evidence:...` |
| `record_id` | string | Identificador único para este registro | `evt-20260115-001` |

## Campos opcionais (DEVERIA/PODE)

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `session_id` | string | Identificador de sessão |
| `device_id` | string | Identificador de dispositivo |
| `ip` | string | Endereço IP |
| `user_agent` | string | String de user agent |
| `department` | string | Departamento organizacional |
| `project_id` | string | Identificador de projeto |
| `prompt_category` | string | Categoria do prompt/consulta |
| `model_family` | string | Família do modelo de IA (ex: GPT-4, Claude) |
| `destination` | string | URL ou endpoint de destino |
| `policy_id` | string | Política que disparou a decisão |
| `remediation_ticket` | string | Referência de ticket de remediação |

## Notas de privacidade/segurança

!!! warning "Tratamento de dados"
    - **Não incorpore** PII, credenciais ou conteúdo de prompt diretamente em campos de log.
    - Use `evidence_ref` para referenciar conteúdo sensível armazenado separadamente.
    - Aplique controles de acesso apropriados ao armazenamento de logs.
    - Considere políticas de retenção de dados alinhadas com [Requisitos Mínimos de Evidências](../../minimum-evidence/).

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

## Páginas relacionadas

- [Índice de Schemas de Log](../)
- [Log de Atividade de Agente](../agent-activity/)
- [Requisitos Mínimos de Evidências](../../minimum-evidence/)
- [Taxonomia: IM-007 Shadow/Não Gerenciado](../../../standard/current/03-taxonomy/)
