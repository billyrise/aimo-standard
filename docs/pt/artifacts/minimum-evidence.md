---
description: Requisitos mínimos de evidências AIMO. Checklist de nível DEVE por ciclo de vida (solicitação, revisão, aprovação, alteração, renovação) para prontidão de evidências de governança de IA.
---

# Requisitos Mínimos de Evidências

Esta página define os requisitos mínimos de evidências como um checklist de nível DEVE, agrupados por ciclo de vida. Suporta explicabilidade e prontidão de evidências; não fornece aconselhamento jurídico nem garante conformidade.

## 1) Solicitação

- **Campos DEVE**: identificador, timestamp(s), ator/papel, escopo (o que é solicitado), justificativa (por quê).
- **Vinculações DEVE**: id da solicitação referenciado pela revisão e por itens EV que registram o uso.
- **O que comprova**: que o uso foi solicitado e definido antes da aprovação e uso.

## 2) Revisão / Aprovação

- **Campos DEVE**: identificador, timestamp(s), ator/papel, decisão (aprovado/rejeitado/condicional), escopo, justificativa, referência à solicitação.
- **Vinculações DEVE**: id da revisão referenciado por EV e por qualquer exceção ou renovação subsequente.
- **O que comprova**: que uma revisão e aprovação definidas ocorreram antes do uso (ou exceção).

## 3) Exceção

- **Campos DEVE**: identificador, timestamp(s), escopo, expiração (ou prazo), controles compensatórios, justificativa, referência à revisão/solicitação.
- **Vinculações DEVE**: exceção → controles compensatórios; exceção → expiração; exceção → renovação (quando reavaliação for devida).
- **O que comprova**: que desvios são limitados no tempo, têm controles compensatórios e estão vinculados à renovação.

## 4) Renovação / Reavaliação

- **Campos DEVE**: identificador, timestamp(s), ator/papel, decisão (renovado/revogado/condicional), referências a exceção/solicitação/revisão/EV anteriores.
- **Vinculações DEVE**: renovação referencia a exceção ou aprovação sendo renovada; itens EV podem referenciar id de renovação.
- **O que comprova**: que exceções e aprovações são reavaliadas e renovadas ou revogadas em base definida.

## 5) Log de Alterações

- **Campos DEVE**: identificador, timestamp, ator/papel, descrição da alteração, referências (ex: a EV, solicitação, revisão, exceção, renovação afetados).
- **Vinculações DEVE**: entradas do log de alterações referenciam os artefatos que modificam ou que disparam a alteração.
- **O que comprova**: que alterações no pacote ou seu conteúdo são registradas e rastreáveis.

## 6) Integridade e Acesso

Integridade de evidências e controle de acesso são essenciais para confiança da auditoria. Embora o AIMO não prescreva controles técnicos específicos, adotantes devem documentar como essas expectativas são atendidas.

### Orientação de controle de acesso

| Aspecto | Orientação |
| --- | --- |
| **Acesso baseado em papéis** | Defina papéis (ex: criador de evidências, revisor, auditor, admin) e documente quem pode criar, ler, atualizar ou excluir evidências. |
| **Privilégio mínimo** | Conceda acesso mínimo necessário; restrinja acesso de escrita a pessoal autorizado. |
| **Log de acesso** | Registre eventos de acesso (quem, quando, o quê) para fins de trilha de auditoria. |
| **Separação de funções** | Quando prático, separe criação de evidências de papéis de aprovação. |

### Orientação de retenção

| Aspecto | Orientação |
| --- | --- |
| **Período de retenção** | Defina e documente períodos de retenção baseados em requisitos regulatórios e política organizacional (ex: 5-7 anos para auditorias financeiras). |
| **Cronograma de retenção** | Mantenha um cronograma mostrando quais evidências são retidas, por quanto tempo, e quando podem ser descartadas. |
| **Retenção legal** | Suporte processos de retenção legal que suspendem retenção/exclusão normal para litígio ou investigação. |

### Opções de imutabilidade

| Opção | Descrição |
| --- | --- |
| **Hashing criptográfico** | Gere hashes SHA-256 (ou mais fortes) para arquivos de evidências; armazene hashes separadamente para verificação. |
| **Armazenamento WORM** | Use armazenamento Write-Once-Read-Many para arquivos de evidências para prevenir modificação. |
| **Logs somente-anexação** | Use logs de auditoria somente-anexação para rastreamento de alterações. |
| **Assinaturas digitais** | Assine pacotes de evidências para provar autoria e detectar adulteração. |

### Expectativas de trilha de auditoria

| Elemento | O que documentar |
| --- | --- |
| **Log de alterações** | Registre quem alterou o quê, quando e por quê (veja grupo de ciclo de vida Log de Alterações). |
| **Log de acesso** | Registre quem acessou evidências, quando e para qual propósito. |
| **Logs de sistema** | Retenha logs de sistema relevantes (autenticação, autorização) que suportam alegações de integridade de evidências. |
| **Registros de verificação** | Documente verificação periódica de integridade (verificações de hash, revisões de auditoria). |

### O que comprova

- **Evidência é preservada**: mecanismos de integridade (hashing, WORM, assinaturas) demonstram que evidências não foram adulteradas.
- **Acesso é controlado**: logs de acesso e definições de papéis mostram quem teve acesso e que privilégio mínimo foi aplicado.
- **Confiança da auditoria é suportada**: juntos, esses elementos dão aos auditores confiança na confiabilidade das evidências.

### Perfis operacionais recomendados

Escolha um perfil baseado em sua tolerância a riscos e requisitos regulatórios. Estas são recomendações, não mandatos.

| Aspecto | Leve | Padrão | Rigoroso |
| --- | --- | --- | --- |
| **Caso de uso** | Pilotos internos, IA de baixo risco | Sistemas de produção, risco moderado | Indústrias reguladas, IA de alto risco |
| **Período de retenção** | 1-2 anos | 5-7 anos | 7-10+ anos ou mínimo regulatório |
| **Imutabilidade** | Hashes SHA-256 | SHA-256 + logs somente-anexação | Armazenamento WORM + assinaturas digitais |
| **Controle de acesso** | Baseado em papéis (básico) | Baseado em papéis + log de acesso | Separação de funções + trilha de auditoria completa |
| **Trilha de auditoria** | Somente log de alterações | Log de alterações + log de acesso | Logs de sistema completos + verificação periódica |
| **Frequência de verificação** | Sob demanda | Trimestral | Mensal ou contínua |
| **Uso do validador** | Opcional | Obrigatório antes da submissão | Obrigatório + verificações automatizadas de CI |

!!! note "Períodos de retenção são exemplos"
    Períodos de retenção mostrados são ilustrativos. Organizações devem determinar retenção baseada em leis aplicáveis, contratos, requisitos da indústria e políticas internas.

!!! tip "Como escolher"
    - **Leve**: Adequado para experimentação, ferramentas internas ou aplicações de baixo impacto onde auditorias formais são improváveis.
    - **Padrão**: Recomendado para a maioria das implantações de produção onde auditorias podem ocorrer mas não são contínuas.
    - **Rigoroso**: Requerido para indústrias reguladas (financeiro, saúde, governo) ou sistemas de IA com impacto de risco significativo.

## Nota importante

Este conjunto mínimo suporta explicabilidade e prontidão de evidências; não fornece aconselhamento jurídico nem garante conformidade por si só.

Veja [Pacote de Evidências](evidence-bundle.md) para estrutura do pacote e sumário; veja [Template EV](../standard/current/06-ev-template.md) e schemas para alinhamento em nível de campo.

Veja também: [Schemas de Log](log-schemas/index.md) — formatos de log normalizados para evidências de descoberta de Shadow AI e atividade de agentes.
