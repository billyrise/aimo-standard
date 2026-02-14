---
description: Dicionário AIMO - Lista autoritativa de 91 códigos de taxonomia em 8 dimensões. Definições completas, rótulos e informações de ciclo de vida para classificação de IA.
---

# Dicionário

O Dicionário AIMO é a lista autoritativa de todos os códigos válidos dentro da taxonomia. Fornece definições completas para cada código incluindo rótulos, descrições e informações de ciclo de vida.

## O que é Dicionário

O dicionário fornece um conjunto completo, legível por máquina, de todos os códigos de taxonomia AIMO. Ele contém:

- Todos os 91 códigos em 8 dimensões
- Rótulos e definições (com traduções em pacotes de idioma)
- Metadados de ciclo de vida (status, versão introduzida, deprecated, removida)
- Notas de escopo e exemplos para uso de código

O dicionário permite:

1. **Templates de Evidências**: Códigos são usados em templates EV para classificar sistemas de IA
2. **Validador**: O validador verifica que todos os códigos existem no dicionário
3. **Mapa de Cobertura**: Códigos permitem mapeamento para frameworks e regulamentações externos

!!! info "Single Source of Truth (SSOT)"
    O SSOT para o dicionário é:

    - **Estrutura**: `data/taxonomy/canonical.yaml` (códigos, status, ciclo de vida)
    - **Traduções**: `data/taxonomy/i18n/*.yaml` (rótulos, definições por idioma)

    Arquivos CSV são **artefatos gerados** para distribuição. Veja [Releases](../../../releases/) para downloads.

## Schema de Colunas

O dicionário canônico usa **18 colunas** (estrutura neutra de idioma):

### Colunas de Identificação (5)

| # | Coluna | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- | --- |
| 1 | `standard_id` | Sim | Identificador do padrão | `AIMO-STD` |
| 2 | `standard_version` | Sim | Formato SemVer | `0.1.0` |
| 3 | `dimension_id` | Sim | ID de dimensão de duas letras | `FS`, `UC`, `DT` |
| 4 | `dimension_name` | Sim | Nome da dimensão | `Functional Scope` |
| 5 | `code` | Sim | Código completo | `UC-001` |

### Colunas de Rótulo e Definição (4)

| # | Coluna | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- | --- |
| 6 | `label` | Sim | Rótulo do código (máx 50 chars) | `General Q&A` |
| 7 | `definition` | Sim | Definição do código (1-2 sentenças) | `General question answering...` |
| 8 | `scope_notes` | Não | Esclarecimento de escopo de uso | `Low to medium risk...` |
| 9 | `examples` | Não | Exemplos separados por pipe | `chatbot\|recommendation` |

!!! note "Traduções"
    O modelo de dados canônico separa traduções em pacotes de idioma (`data/taxonomy/i18n/*.yaml`). Cada pacote de idioma fornece valores localizados de `dimension_name`, `label` e `definition`. Veja [Guia de Localização](../../contributing/localization.md) para detalhes.

### Colunas de Ciclo de Vida (6)

| # | Coluna | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- | --- |
| 10 | `status` | Sim | `active`, `deprecated`, `removed` | `active` |
| 11 | `introduced_in` | Sim | Versão quando adicionado | `0.1.0` |
| 12 | `deprecated_in` | Não | Versão quando deprecated | `1.2.0` |
| 13 | `removed_in` | Não | Versão quando removido | `2.0.0` |
| 14 | `replaced_by` | Não | Código de substituição | `UC-015` |
| 15 | `backward_compatible` | Sim | `true` ou `false` | `true` |

### Colunas de Governança (3)

| # | Coluna | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- | --- |
| 16 | `references` | Não | Referências externas | ISO/IEC 42001 |
| 17 | `owner` | Não | Parte responsável | `AIMO WG` |
| 18 | `last_reviewed_date` | Não | Última revisão (YYYY-MM-DD) | `2026-01-19` |

## Entradas Iniciais

A versão atual do dicionário é **v0.1.0** e contém:

| Dimensão | Nome | Códigos Ativos | Deprecated | Total |
| --- | --- | --- | --- | --- |
| FS | Escopo Funcional | 6 | 0 | 6 |
| UC | Classe de Caso de Uso | 30 | 0 | 30 |
| DT | Tipo de Dados | 10 | 0 | 10 |
| CH | Canal | 8 | 0 | 8 |
| IM | Modo de Integração | 7 | 0 | 7 |
| RS | Superfície de Risco | 8 | 0 | 8 |
| OB | Resultado / Benefício | 7 | 0 | 7 |
| LG | Tipo Log/Evento | 15 | 0 | 15 |
| **Total** | | **91** | **0** | **91** |

!!! note "Listagens Completas de Códigos"
    A lista completa de 91 códigos está disponível nos artefatos CSV gerados. Esta página de documentação fornece definições de colunas e orientação de uso. Para definições detalhadas de códigos:

    - **Download**: Veja [Releases](../../../releases/) para arquivos CSV por idioma
    - **CSV por idioma**: `artifacts/taxonomy/current/{lang}/taxonomy_dictionary.csv`
    - **CSV legado EN/JA misto**: `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` (congelado, apenas para compatibilidade retroativa)

## Política de Atualização

### Adicionando Novos Códigos

1. Atribua o próximo número disponível dentro da dimensão (ex: `UC-031` após `UC-030`)
2. Defina `status` como `active`
3. Defina `introduced_in` para a versão atual
4. Defina `backward_compatible` como `true`
5. Forneça rótulo e definição (adicione traduções aos pacotes de idioma)

### Modificando Códigos Existentes

| Tipo de Mudança | Permitido | Impacto na Versão |
| --- | --- | --- |
| Esclarecimento de definição | Sim | PATCH |
| Atualização de notas de escopo | Sim | PATCH |
| Mudança de rótulo (significado preservado) | Sim | MINOR |
| Mudança de significado | Não | Criar novo código |

### Depreciando Códigos

1. Defina `status` como `deprecated`
2. Defina `deprecated_in` para versão atual
3. Defina `replaced_by` para o novo código (se aplicável)
4. Código permanece funcional para compatibilidade retroativa
5. Documente a razão em scope_notes

### Removendo Códigos

1. Deprecie por pelo menos uma versão MINOR primeiro
2. Defina `status` como `removed`
3. Defina `removed_in` para versão MAJOR atual
4. Código não é mais válido para novas evidências

### Política de Compatibilidade

| Ação | Impacto na Versão | Backward Compatible |
| --- | --- | --- |
| Adicionar novo código | MINOR | Sim |
| Deprecar código | MINOR | Sim |
| Esclarecer definição | PATCH | Sim |
| Remover código | MAJOR | Não |
| Mudar significado de código | Não permitido | - |

## Como Usar

### Em Templates de Evidências

Cada template EV inclui uma tabela de códigos de 8 dimensões:

```markdown
## Códigos AIMO (8 Dimensões)

| Dimensão | Código(s) | Rótulo |
| --- | --- | --- |
| **FS** | `FS-001` | Produtividade do Usuário Final |
| **UC** | `UC-001`, `UC-002` | Q&A Geral, Sumarização |
| **DT** | `DT-002`, `DT-004` | Interno, Dados Pessoais |
| **CH** | `CH-001` | UI Web |
| **IM** | `IM-002` | SaaS Integrado |
| **RS** | `RS-001`, `RS-003` | Vazamento de Dados, Violação de Conformidade |
| **OB** | `OB-001` | Eficiência |
| **LG** | `LG-001`, `LG-002` | Registro de Solicitação, Registro de Revisão/Aprovação |
```

### No Validador

O validador verifica:

1. Todos os códigos referenciados em evidências existem no dicionário
2. Formato de código corresponde ao padrão esperado (`PREFIXO-###`)
3. Códigos deprecated disparam avisos
4. Códigos removidos são rejeitados

### Diretrizes de Extensão

Organizações PODEM estender o dicionário com códigos customizados:

**Prefixo de Extensão:**

```
X-<ORG>-<DIM>-<TOKEN>
```

Exemplo: `X-ACME-UC-901` para código de caso de uso customizado da ACME Corporation.

**Regras de Extensão:**

1. Códigos customizados NÃO DEVEM conflitar com códigos padrão
2. Códigos customizados DEVERIAM ser documentados em um dicionário de extensão local
3. Ao trocar evidências com partes externas, use apenas códigos padrão

## Downloads

Veja [Releases](../../../releases/) para pacotes para download contendo o dicionário e arquivos relacionados.

## Páginas Relacionadas

- [Taxonomia](./03-taxonomy.md) - Definições de dimensão e tabelas de código
- [Códigos](./04-codes.md) - Formato de código, nomenclatura e ciclo de vida
- [Templates de Evidências](./06-ev-template.md) - Como códigos são usados em templates
- [Validador](./07-validator.md) - Regras de validação de código
- [Changelog](./08-changelog.md) - Histórico de versões
