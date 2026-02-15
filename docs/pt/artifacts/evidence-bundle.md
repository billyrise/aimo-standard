---
description: Estrutura do Pacote de Evidências AIMO. Formato de pacote de auditoria com sumário, rastreabilidade e artefatos para conformidade de governança de IA e entrega a auditores.
---
<!-- aimo:translation_status=translated -->

# Pacote de Evidências

Um **Pacote de Evidências** é um pacote de auditoria: um conjunto estruturado de artefatos que suporta explicabilidade e rastreabilidade para governança de IA. Não é uma funcionalidade de produto, mas um formato de entrega para auditores e conformidade.

## Estrutura e nomenclatura do pacote

- **Nomenclatura da raiz do pacote**: use um padrão consistente como `{org}_{sistema}_{período}_{versão}` (ex: `acme_ai-usage_2026-Q1_v1`).
- **Arquivos obrigatórios**: pelo menos um conjunto de Evidências (EV) alinhado com o [Template Evidence Pack (EP)](../../standard/current/06-ev-template/), um [Dicionário](../../standard/current/05-dictionary/), um breve **Resumo** (resumo executivo do pacote) e um **Log de Alterações** (ou referência a ele) para mudanças no pacote ou seu conteúdo.
- **Anexos opcionais**: logs, registros de revisão, aprovações de exceções, registros de renovação; mantenha a nomenclatura consistente e referenciável a partir do EV/Dicionário principal.

## Sumário (TOC)

| Seção | Artefato | Obrigatório? | Propósito | Campos mínimos | Validação |
| --- | --- | --- | --- | --- | --- |
| Evidência | Registros EV (JSON/array) | Sim | Registro do que aconteceu; link para solicitação/revisão/exceção/renovação | id, timestamp, source, summary; refs de ciclo de vida opcionais | [Validador](../../validator/), aimo-ev.schema.json |
| Dicionário | dictionary.json | Sim | Chaves/rótulos/descrições para códigos e dimensões | entries (key, label, description) | aimo-dictionary.schema.json |
| Resumo | summary (doc ou campo) | Sim | Visão geral de uma página para auditores | escopo, período, decisões principais, exceções | — |
| Log de alterações | change_log ou referência | Sim | Trilha de auditoria de alterações no pacote/conteúdo | id, timestamp, actor, descrição da alteração, referências | — |
| Solicitação | registro(s) de solicitação | Se aplicável | Aplicação/solicitação de uso | id, timestamp, actor/role, escopo, justificativa | — |
| Revisão/Aprovação | registro(s) de revisão | Se aplicável | Resultado de revisão e aprovação | id, timestamp, actor/role, decisão, referências | — |
| Exceção | registro(s) de exceção | Se aplicável | Exceção com controles compensatórios e expiração | id, timestamp, escopo, expiração, controles compensatórios, ref de renovação | — |
| Renovação | registro(s) de renovação | Se aplicável | Reavaliação e renovação | id, timestamp, actor/role, decisão, referências a exceção/EV anterior | — |

## Relação normativa: registros EV (índice) e Evidence Pack (payload)

Para evitar construção dupla e ambiguidade em auditoria, o seguinte é **normativo**: (1) Registros EV (JSON) são o **índice/ledger** (rastreabilidade verificável por máquina). (2) Arquivos Evidence Pack (EP-01..EP-07 e manifesto) são o **payload**. (3) Registros EV DEVEM referenciar o payload por `evidence_file_ids` (ex. EP-01) e/ou hashes; o [Validador](../../validator/) verifica integridade referencial. (4) **Conjunto mínimo de submissão**: EV JSON + Dictionary + Summary + Change Log + Evidence Pack (zip). Ver [Template Evidence Pack](../../standard/current/06-ev-template/) para tipos de documento EP-01..EP-07.

## Rastreabilidade

- **IDs estáveis**: cada registro (EV, solicitação, revisão, exceção, renovação, entrada de log de alterações) DEVE ter um identificador único e estável.
- **Referências cruzadas**: vincule Solicitação → Revisão → Exceção (se houver) → Renovação e vincule itens EV a estes via campos de referência (ex: `request_id`, `review_id`, `exception_id`, `renewal_id`).
- **Vinculação**: garanta que auditores possam seguir uma cadeia de um uso de IA (ou exceção) até a solicitação, aprovação, qualquer exceção e seus controles compensatórios e expiração, e renovação.

## Como auditores usam isso

Auditores usam o Pacote de Evidências para verificar que o uso de IA é solicitado, revisado e aprovado; que exceções são limitadas no tempo e têm controles compensatórios e renovação; e que alterações são registradas. O sumário e regras de rastreabilidade permitem localizar artefatos necessários e seguir IDs e referências entre registros de solicitação, revisão, exceção, renovação e EV. O Resumo fornece uma visão rápida; o Log de Alterações suporta controle de mudanças e responsabilidade.

Veja [Requisitos Mínimos de Evidências](../minimum-evidence/) para campos de nível DEVE e grupos de ciclo de vida.

## Orientação operacional

!!! info "Integridade e controle de acesso"
    Embora o AIMO não prescreva controles específicos, adotantes devem documentar:
    
    - **Papéis de acesso**: quem pode criar, ler, atualizar ou excluir evidências
    - **Política de retenção**: por quanto tempo evidências são retidas e sob qual cronograma
    - **Mecanismos de integridade**: hashing, armazenamento WORM ou assinaturas digitais usados
    - **Trilha de auditoria**: logs de acesso e alterações no pacote
    
    Veja [Requisitos Mínimos de Evidências > Integridade e Acesso](../minimum-evidence/#6-integridade-acesso) para orientação detalhada.

## Jornada de auditoria

A partir desta página, a jornada típica de auditoria continua:

1. **Próximo**: [Requisitos Mínimos de Evidências](../minimum-evidence/) — checklist de nível DEVE por ciclo de vida
2. **Depois**: [Mapa de Cobertura](../../coverage-map/) — mapeamento para frameworks externos
3. **Validar**: [Validador](../../validator/) — execute verificações estruturais
4. **Download**: [Releases](../../releases/) — obtenha ativos de release e verifique checksums
