---
description: Formato de Log de Atividade de Agente - Schema neutro de fornecedor para exercício de privilégios de IA agêntica, execução de ferramentas e monitoramento de operações recursivas em empresas.
---
<!-- aimo:translation_status=translated -->

# Formato de Log de Atividade de Agente

## Propósito

Este schema define um formato neutro de fornecedor para logs que documentam **exercício de privilégios de IA agêntica, execução de ferramentas e operações recursivas**. Ele permite que organizações:

- Mantenham um registro auditável de ações de agentes autônomos
- Rastreiem "quem fez o quê com qual autoridade" para conformidade e investigação de incidentes
- Suportem explicabilidade para operações de IA agêntica em contextos de auditoria

## Modelo de evento

O schema suporta quatro tipos de evento que capturam o ciclo de vida da operação agêntica:

| Tipo de Evento | Descrição |
| --- | --- |
| `agent_run` | Início ou conclusão de uma sessão de execução de agente |
| `tool_call` | Agente invocando uma ferramenta ou ação externa |
| `tool_result` | Resultado retornado de uma invocação de ferramenta |
| `escalation` | Agente solicitando intervenção humana ou privilégios elevados |

## Campos obrigatórios (DEVE)

| Campo | Tipo | Descrição | Exemplo |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | Timestamp do evento | `2026-01-15T09:30:00Z` |
| `agent_id` | string | Identificador do agente | `agent-coding-assistant-v2` |
| `agent_version` | string | Versão do agente | `2.1.0` |
| `run_id` | string | Identificador único para esta execução/sessão | `run-20260115-abc123` |
| `event_type` | string | Tipo de evento | `agent_run`, `tool_call`, `tool_result`, `escalation` |
| `actor_id` | string | Usuário ou serviço iniciador | `user@example.com` |
| `tool_name` | string | Nome da ferramenta invocada | `file_write`, `api_call`, `shell_exec` |
| `tool_action` | string | Ação realizada pela ferramenta | `create`, `read`, `update`, `delete`, `execute` |
| `tool_target` | string | Alvo da ação | `/path/to/file`, `https://api.example.com` |
| `auth_context` | string | Resumo de permissão/papel | `role:developer, scope:project-x` |
| `input_ref` | string | Hash ou URI para entrada (não o conteúdo em si) | `sha256:def456...` |
| `output_ref` | string | Hash ou URI para saída (não o conteúdo em si) | `sha256:ghi789...` |
| `decision` | string | Decisão de política aplicada | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | Referência a evidência relacionada | `urn:evidence:...` |

## Campos opcionais (DEVERIA/PODE)

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `recursion_depth` | number | Profundidade de recursão atual para chamadas de agente aninhadas |
| `retry_count` | number | Número de tentativas para esta ação |
| `policy_id` | string | Política que disparou a decisão |
| `prompt_template_id` | string | Identificador do template de prompt |
| `model` | string | Modelo usado para esta ação |
| `latency_ms` | number | Latência em milissegundos |
| `cost_estimate` | number | Custo estimado desta ação |
| `error_code` | string | Código de erro se a ação falhou |

## Notas de segurança

!!! warning "Suposições de risco agêntico"
    Ao registrar atividade de IA agêntica, assuma os seguintes riscos:

    - **Injeção de prompt**: Entradas maliciosas podem tentar manipular comportamento do agente
    - **Super-privilégio**: Agentes podem ter permissões mais amplas do que o pretendido para uma tarefa específica
    - **Loops recursivos**: Agentes podem entrar em padrões de execução recursiva não intencionais
    - **Confused deputy**: Agentes podem ser enganados para agir em nome de partes não autorizadas

    O schema é projetado para capturar "quem fez o quê com qual autoridade" para suportar análise pós-incidente e explicações de auditoria. Ele não previne esses riscos; organizações devem implementar salvaguardas apropriadas.

!!! warning "Tratamento de dados"
    - **Não incorpore** segredos, credenciais ou conteúdo sensível em `input_ref` ou `output_ref`.
    - Use referências de hash ou URIs seguras para conteúdo armazenado separadamente.
    - Aplique controles de acesso e políticas de retenção apropriados.

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

## Páginas relacionadas

- [Índice de Schemas de Log](../)
- [Log de Descoberta de Shadow AI](../shadow-ai-discovery/)
- [Requisitos Mínimos de Evidências](../../minimum-evidence/)
- [Taxonomia: UC-010 Automação Agêntica](../../../standard/current/03-taxonomy/)
