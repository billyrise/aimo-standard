---
description: Requisitos mínimos de evidência AIMO. Lista de verificação MUST por ciclo de vida (solicitação, revisão, aprovação, alteração, renovação) para prontidão de evidência em governança de IA.
---
<!-- aimo:translation_status=translated -->

# Requisitos mínimos de evidência (Minimum Evidence Requirements)

Esta página é a lista de verificação de **Requisitos mínimos de evidência** para auditores e implementadores. Define os requisitos mínimos como lista MUST por ciclo de vida. Apoia a explicabilidade e a prontidão de evidência; não constitui aconselhamento jurídico nem garante conformidade.

Use esta página junto com [Pacote de Evidências](../evidence-bundle/) e o [Validador](../../standard/current/07-validator/) ao preparar ou revisar submissões.

## 1) Solicitação (Request)

- **Campos MUST**: identificador, marca(s) de tempo, ator/papel, escopo (o que é solicitado), justificativa (rationale).
- **Vínculos MUST**: o id da solicitação é referenciado pela revisão e pelos itens EV que registram o uso.
- **O que comprova**: que o uso foi solicitado e delimitado antes da aprovação e do uso.

## 2) Revisão / Aprovação (Review / Approval)

- **Campos MUST**: identificador, marca(s) de tempo, ator/papel, decisão (aprovado/rejeitado/condicional), escopo, justificativa, referência à solicitação.
- **Vínculos MUST**: o id da revisão é referenciado pelo EV e por qualquer exceção ou renovação subsequente.
- **O que comprova**: que uma revisão e aprovação definidas ocorreram antes do uso (ou exceção).

## 3) Exceção (Exception)

- **Campos MUST**: identificador, marca(s) de tempo, escopo, expiração (ou prazo), controles compensatórios, justificativa, referência à revisão/solicitação.
- **Vínculos MUST**: exceção → controles compensatórios; exceção → expiração; exceção → renovação (quando a reavaliação é devida).
- **O que comprova**: que os desvios têm prazo, têm controles compensatórios e estão vinculados à renovação.

## 4) Renovação / Reavaliação (Renewal / Re-evaluation)

- **Campos MUST**: identificador, marca(s) de tempo, ator/papel, decisão (renovado/revogado/condicional), referências à exceção/solicitação/revisão/EV anteriores.
- **Vínculos MUST**: a renovação referencia a exceção ou aprovação renovada; os itens EV podem referenciar o id de renovação.
- **O que comprova**: que exceções e aprovações são reavaliadas e renovadas ou revogadas com base definida.

## 5) Registro de alterações (Change Log)

- **Campos MUST**: identificador, marca de tempo, ator/papel, descrição da alteração, referências (ex. a EV, solicitação, revisão, exceção, renovação afetados).
- **Vínculos MUST**: as entradas do registro de alterações referenciam os artefatos que modificam ou que disparam a alteração.
- **O que comprova**: que as alterações ao pacote ou seu conteúdo são registradas e rastreáveis.

## 6) Integridade e acesso (Integrity & Access)

A integridade das evidências e o controle de acesso são essenciais para a confiança na auditoria. A AIMO não prescreve controles técnicos específicos; os adoptantes devem documentar como essas expectativas são atendidas.

### Orientação sobre controle de acesso

| Aspecto | Orientação |
| --- | --- |
| **Acesso baseado em função** | Definir funções (ex. criador de evidências, revisor, auditor, admin) e documentar quem pode criar, ler, atualizar ou excluir evidências. |
| **Privilégio mínimo** | Conceder o acesso mínimo necessário; restringir a escrita ao pessoal autorizado. |
| **Registro de acesso** | Registrar eventos de acesso (quem, quando, o quê) para rastreabilidade de auditoria. |
| **Separação de funções** | Quando prático, separar a criação de evidências dos papéis de aprovação. |

### Orientação sobre retenção

| Aspecto | Orientação |
| --- | --- |
| **Período de retenção** | Definir e documentar períodos com base em requisitos regulatórios e política organizacional (ex. 5–7 anos para auditorias financeiras). |
| **Cronograma de retenção** | Manter um cronograma mostrando quais evidências são retidas, por quanto tempo e quando podem ser descartadas. |
| **Retenção legal** | Suportar processos de retenção legal que suspendem a retenção/exclusão normal em litígios ou investigações. |

### Opções de imutabilidade

| Opção | Descrição |
| --- | --- |
| **Hash criptográfico** | Gerar hashes SHA-256 (ou superiores) para arquivos de evidência; armazenar hashes separadamente para verificação. |
| **Armazenamento WORM** | Usar armazenamento de gravação única e leitura múltipla (WORM) para arquivos de evidência para evitar modificação. |
| **Registros somente anexo** | Usar registros de auditoria somente anexo para rastreamento de alterações. |
| **Assinaturas digitais** | Assinar pacotes de evidência para comprovar autoria e detectar adulteração. |

### Expectativas de rastreabilidade de auditoria

| Elemento | O que documentar |
| --- | --- |
| **Registro de alterações** | Registrar quem alterou o quê, quando e por quê (ver grupo de ciclo de vida Change Log). |
| **Registro de acesso** | Registrar quem acessou as evidências, quando e para qual propósito. |
| **Registros do sistema** | Reter registros do sistema relevantes (autenticação, autorização) que apoiem as alegações de integridade. |
| **Registros de verificação** | Documentar a verificação periódica de integridade (verificações de hash, revisões de auditoria). |

### O que comprova

- **As evidências são preservadas**: mecanismos de integridade (hash, WORM, assinaturas) demonstram que as evidências não foram adulteradas.
- **O acesso é controlado**: registros de acesso e definições de funções mostram quem teve acesso e que o privilégio mínimo foi aplicado.
- **A confiança na auditoria é apoiada**: em conjunto, esses elementos dão aos auditores confiança na confiabilidade das evidências.

### Perfis operacionais recomendados

Escolha um perfil com base na sua tolerância ao risco e nos requisitos regulatórios. São recomendações, não mandatos.

| Aspecto | Leve | Padrão | Rigoroso |
| --- | --- | --- | --- |
| **Caso de uso** | Pilotos internos, IA de baixo risco | Sistemas em produção, risco moderado | Indústrias reguladas, IA de alto risco |
| **Período de retenção** | 1–2 anos | 5–7 anos | 7–10+ anos ou mínimo regulatório |
| **Imutabilidade** | Hashes SHA-256 | SHA-256 + registros somente anexo | Armazenamento WORM + assinaturas digitais |
| **Controle de acesso** | Por função (básico) | Por função + registro de acesso | Separação de funções + rastreabilidade completa |
| **Rastreabilidade de auditoria** | Apenas registro de alterações | Registro de alterações + registro de acesso | Registros do sistema completos + verificação periódica |
| **Frequência de verificação** | Sob demanda | Trimestral | Mensal ou contínua |
| **Uso do Validador** | Opcional | Obrigatório antes da submissão | Obrigatório + verificações CI automatizadas |

!!! note "Os períodos de retenção são exemplos"
    Os períodos mostrados são ilustrativos. As organizações devem determinar a retenção com base em leis aplicáveis, contratos, requisitos do setor e políticas internas.

!!! tip "Como escolher"
    - **Leve**: Adequado para experimentação, ferramentas internas ou aplicações de baixo impacto onde auditoria formal é improvável.
    - **Padrão**: Recomendado para a maioria das implantações em produção onde pode haver auditorias mas não contínuas.
    - **Rigoroso**: Necessário para indústrias reguladas (finanças, saúde, governo) ou sistemas de IA com impacto de risco significativo.

## Nota importante

Este conjunto mínimo apoia a explicabilidade e a prontidão de evidência; não constitui por si aconselhamento jurídico nem garante conformidade.

Veja [Pacote de Evidências](../evidence-bundle/) para estrutura e TOC do pacote; [Modelo EV](../../standard/current/06-ev-template/) e esquemas para alinhamento em nível de campo.

Veja também: [Esquemas de registro](../log-schemas/) — formatos de registro normalizados para descoberta Shadow AI e evidência de atividade de agentes.

## Sobreposições regulatórias (informativo)

As **sobreposições** a seguir descrevem evidência adicional frequentemente esperada em contextos regulatórios ou de contratação específicos. São **informativas**; anexe modelos/listas de verificação oficiais como estão na [seção External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) do Modelo EV e referencie-os por logical_id no manifesto.

| Sobreposição | Artefatos adicionais tipicamente esperados | Onde anexar | Perfil (opcional) |
| --- | --- | --- | --- |
| **EU alto risco** | Gestão de riscos, documentação técnica (Anexo IV), registro, supervisão humana, transparência (Art 50), notificação de incidentes | payload_index; Pacote de Evidências + perfil Annex IV | `eu_ai_act_annex_iv.json`, `eu_ai_act_high_risk.json` |
| **EU GPAI CoP** | Model Documentation Form (transparência, direitos autorais, segurança) | External Forms; logical_id ex. GPAI_MODEL_DOC_FORM | `eu_gp_ai_cop.json` |
| **NIST GenAI** | Artefatos do perfil GenAI (adaptação de modelo, avaliação, monitoramento) | payload_index; change_log; External Forms / registros GenAI | `nist_ai_600_1_genai.json` |
| **UK ATRS / contratação** | Registro de transparência ATRS; responsável pela prestação de contas; notas de avaliação de contratação | External Forms; Summary, review | `uk_atrs_procurement.json` |
| **JP contratação** | Lista de verificação de contratação pública GenAI do governo; lista de diretrizes AI Business Guidelines | External Forms; logical_id ex. JP_PROCUREMENT_CHECKLIST | `jp_gov_genai_procurement.json` |

Os nomes de arquivo de perfil seguem o padrão `coverage_map/profiles/<target>_<purpose>.json`; cada um inclui `target_version`. Veja [Coverage Map — Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/) para Reino Unido e Japão; [EU AI Act](../../coverage-map/eu-ai-act/) e [NIST AI RMF](../../coverage-map/nist-ai-rmf/) para UE e NIST.
