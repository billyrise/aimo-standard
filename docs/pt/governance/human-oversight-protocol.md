---
description: Protocolo de Supervisão Humana AIMO - Limite entre validação automatizada e revisão humana. Responsabilidades de julgamento máquina vs. humano na governança de IA.
---

# Protocolo de Supervisão Humana

Esta página define o limite entre o que a validação automatizada (Validador) pode verificar e o que requer revisão humana (Human-in-the-Loop). Esclarece as responsabilidades para julgamento máquina vs. humano em processos de evidências de governança de IA.

## Propósito

Ferramentas de validação automatizada podem verificar eficientemente correção estrutural e sintática, mas não podem substituir julgamento humano para decisões dependentes de contexto. Este protocolo:

- Esclarece o que o Validador pode e não pode verificar
- Define o escopo de revisão humana necessária para governança efetiva
- Suporta explicações de auditoria documentando o processo de supervisão humana
- Fornece um framework para organizações implementando fluxos de trabalho de governança de IA

## O que validação automatizada pode fazer (escopo do Validador)

O Validador AIMO e ferramentas automatizadas similares podem verificar:

| Capacidade | Descrição |
| --- | --- |
| **Completude de campos/documentos obrigatórios** | Verificar que todos os campos obrigatórios estão presentes em manifestos, registros EV e outros artefatos |
| **Consistência estrutural** | Validar referências, IDs e cross-links entre artefatos (ex: request_id → review_id) |
| **Validação de schema** | Verificar que artefatos JSON/YAML conformam a schemas definidos |
| **Validação de formato de código** | Verificar que códigos de taxonomia correspondem a padrões esperados (ex: `UC-001`) |
| **Verificações de integridade** | Validar formato e presença de hash (não recálculo contra conteúdo) |
| **Validação de dicionário** | Confirmar que códigos existem no dicionário de taxonomia |

Veja [Validador](../../standard/current/07-validator/) para regras de validação detalhadas e implementação de referência.

## O que requer revisão humana (escopo Human-in-the-Loop)

As seguintes áreas requerem julgamento humano e não podem ser automatizadas:

| Capacidade | Descrição |
| --- | --- |
| **Julgamento de risco dependente de contexto** | Avaliar riscos de negócio, éticos e operacionais baseados em contexto organizacional |
| **Justificativa de aprovação de exceção** | Avaliar se uma exceção é justificada e controles compensatórios são adequados |
| **Tomada de decisão de remediação** | Priorizar correções, alocar recursos e determinar cronogramas |
| **Trade-offs de política** | Equilibrar requisitos concorrentes (ex: velocidade vs. rigor, custo vs. risco) |
| **Aceitação de risco residual** | Decidir se riscos restantes são aceitáveis após controles |
| **Avaliação de impacto cross-domain** | Avaliar implicações para jurídico, RH, operações e outras funções |
| **Verificação de precisão de conteúdo** | Confirmar que conteúdo de evidências é factualmente correto e completo |
| **Comunicação com stakeholders** | Explicar decisões para auditores, reguladores e liderança |

## Limite de responsabilidade

| Aspecto | Validador (Máquina) | Revisor Humano |
| --- | --- | --- |
| **Estrutura** | ✓ Pode verificar | Revisar se sinalizado |
| **Completude** | ✓ Pode verificar campos | Verificar adequação do conteúdo |
| **Formato** | ✓ Pode verificar | — |
| **Julgamento de risco** | ✗ Não pode avaliar | ✓ Deve avaliar |
| **Aprovação de exceção** | ✗ Não pode decidir | ✓ Deve decidir |
| **Prioridade de remediação** | ✗ Não pode priorizar | ✓ Deve priorizar |
| **Interpretação jurídica** | ✗ Não pode interpretar | ✓ Deve verificar com assessoria |
| **Conclusão de auditoria** | ✗ Não pode concluir | ✓ Responsabilidade do auditor |

!!! note "Papéis complementares"
    Validador e revisão humana são **complementares**, não alternativas. Validador garante consistência estrutural antes da revisão humana; revisão humana garante adequação contextual.

## Expectativas de evidências

Organizações implementando supervisão humana devem documentar:

| Tipo de Evidência | Descrição |
| --- | --- |
| **Registro de revisão** | Quem revisou, quando e qual decisão foi tomada |
| **Justificativa de aprovação** | Por que a decisão foi tomada (especialmente para exceções) |
| **Registro de escalonamento** | Quando e por que issues foram escalonadas para autoridade superior |
| **Plano de remediação** | Ações planejadas, responsáveis e cronogramas para abordar issues |
| **Sign-off** | Atestação formal de que revisão foi concluída |

Esses registros devem ser incluídos no Pacote de Evidências conforme [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/).

## Não-sobrereivindicação

!!! warning "Importante"
    Este protocolo define um **framework para documentar supervisão humana**. Ele **não**:

    - Fornece aconselhamento jurídico ou interpretação regulatória
    - Garante conformidade com qualquer regulamentação ou padrão
    - Substitui julgamento humano qualificado por decisões automatizadas
    - Prescreve processos organizacionais específicos

    Organizações devem adaptar este framework ao seu contexto específico, perfil de risco e requisitos regulatórios.

## Páginas relacionadas

- [Validador](../../standard/current/07-validator/) — regras de validação automatizada e implementação de referência
- [Limite de Responsabilidade](../responsibility-boundary/) — o que AIMO fornece vs. responsabilidades do adotante
- [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/) — checklist de evidências de nível DEVE
- [Trust Package](../trust-package/) — hub de materiais prontos para auditoria
