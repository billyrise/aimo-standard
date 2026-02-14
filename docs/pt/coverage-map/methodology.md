---
description: Metodologia do Mapa de Cobertura - Como AIMO mapeia para frameworks externos. Uso em auditorias, relação com Pacote de Evidências e abordagem de rastreabilidade.
---

# Metodologia

> Nota: Esta metodologia suporta rastreabilidade e prontidão de evidências. Não garante conformidade com qualquer regulamentação/padrão específico.

Esta página explica o que o Mapa de Cobertura é e não é, como usá-lo em auditoria, e como ele se relaciona com o Pacote de Evidências e Requisitos Mínimos de Evidências.

## O que o mapeamento é

- Um mapeamento **informativo** de referências de framework/regulamentação externos (por tópico) para evidências AIMO, itens do sumário do Pacote de Evidências, grupos de ciclo de vida de Requisitos Mínimos de Evidências, artefatos e verificações de validador.
- Uma ferramenta de suporte para **explicabilidade**: quais evidências e artefatos AIMO podem ajudar a demonstrar ou explicar alinhamento com um dado requisito externo (sem reivindicar conformidade).

## O que o mapeamento não é

- **Não** é uma garantia de conformidade com qualquer framework ou regulamentação.
- **Não** é aconselhamento jurídico ou substituto para verificação contra textos autoritativos.
- **Não** é exaustivo; é um subconjunto prático para prontidão de auditoria e explicabilidade.

## Como usá-lo em auditoria

Use o fluxo: **requisito → evidência → artefato → validação**.

1. **Requisito**: Identifique a referência do framework externo e tópico (ex: documentação ISO 42001, manutenção de registros EU AI Act).
2. **Evidência**: Veja quais itens do Pacote de Evidências AIMO e grupos de ciclo de vida de Requisitos Mínimos de Evidências (solicitação, revisão, exceção, renovação, change_log, integridade) suportam explicabilidade para aquele requisito.
3. **Artefato**: Localize os artefatos (schemas, templates, exemplos) que implementam ou ilustram aquela evidência.
4. **Validação**: Use o validador e verificações de schema referenciadas para verificar consistência estrutural.

Leitores devem verificar contra o texto autoritativo de cada framework ou regulamentação.

## Relação com Pacote de Evidências e Requisitos Mínimos de Evidências

- **[Pacote de Evidências](../../artifacts/evidence-bundle/)**: Define a estrutura do pacote, sumário e rastreabilidade. Linhas do Mapa de Cobertura referenciam seções do Pacote de Evidências (ex: EV, Dictionary, Summary, change_log, request, review, exception, renewal).
- **[Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/)**: Define grupos de ciclo de vida de nível DEVE (solicitação, revisão, exceção, renovação, change_log, integridade). Linhas do Mapa de Cobertura referenciam esses grupos em `minimum_evidence_refs`.

Use o Mapa de Cobertura para ver quais itens do Pacote de Evidências e grupos de Requisitos Mínimos de Evidências suportam explicabilidade para um dado requisito externo.

## Declaração de não-sobrereivindicação

!!! warning "Importante"
    O AIMO Standard suporta **explicabilidade e prontidão de evidências**. Ele **não** fornece aconselhamento jurídico, garante conformidade, nem certifica conformidade com qualquer regulamentação ou framework. Adotantes devem verificar reivindicações contra textos autoritativos e obter aconselhamento profissional conforme apropriado.

Veja [Limite de Responsabilidade](../../governance/responsibility-boundary/) para escopo, suposições e responsabilidades do adotante.

## Jornada de auditoria

A partir desta página, continue para:

1. **Mapeamentos de framework**: [ISO 42001](../iso-42001/), [NIST AI RMF](../nist-ai-rmf/), [EU AI Act](../eu-ai-act/), [ISMS](../isms/)
2. **Validar**: [Validador](../../validator/) — execute verificações estruturais
3. **Download**: [Releases](../../releases/) — obtenha ativos de release
