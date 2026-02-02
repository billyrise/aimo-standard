---
description: Schemas de Log AIMO - Formatos de log neutros de fornecedor para evidências de IA. Inclui schemas de descoberta de Shadow AI e monitoramento de atividade de agentes.
---

# Schemas de Log

## O que é isso

Esta seção define **formatos de log normalizados** para evidências que podem ser incluídas em um Pacote de Evidências. Esses schemas fornecem uma estrutura neutra de fornecedor para logs relacionados a monitoramento de uso de IA e operações agênticas.

## Quando usar

- **Visibilidade de Shadow AI**: Documentando detecção, inventário e remediação de uso não aprovado de IA.
- **Auditorias de operações agênticas**: Explicando exercício de privilégios de agentes autônomos, execução de ferramentas e operações recursivas.
- **Reprodutibilidade de incidentes**: Fornecendo evidências estruturadas para investigação de incidentes e análise de causa raiz.

## O que NÃO é

!!! warning "Importante"
    Esses schemas definem **formatos de log para submissão de evidências**. Eles NÃO:

    - Coletam automaticamente logs dos seus sistemas
    - Fornecem ferramentas de agregação ou monitoramento de logs
    - Garantem conformidade com qualquer regulamentação ou padrão
    - Substituem implementações de log específicas de fornecedor

    Organizações devem implementar seus próprios pipelines de coleta de logs e normalizar logs para esses schemas para submissão de evidências.

## Schemas

| Schema | Propósito | Download |
| --- | --- | --- |
| [Log de Descoberta de Shadow AI](shadow-ai-discovery.md) | Detecção e inventário de uso não aprovado de IA | [shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json) |
| [Log de Atividade de Agente](agent-activity.md) | Exercício de privilégios de IA agêntica e execução de ferramentas | [agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json) |

## Páginas relacionadas

- [Requisitos Mínimos de Evidências](../minimum-evidence.md) — Checklist de evidências de nível DEVE
- [Pacote de Evidências](../evidence-bundle.md) — Estrutura do pacote e sumário
- [Taxonomia](../../standard/current/03-taxonomy.md) — Códigos de classificação (incluindo UC-010 Automação Agêntica, IM-007 Shadow/Não Gerenciado)
