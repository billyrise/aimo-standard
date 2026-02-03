---
description: Formato e convenções de nomenclatura do Sistema de Códigos AIMO. Define estrutura de código (XX-NNN), estados de ciclo de vida, versionamento e políticas de depreciação para códigos de taxonomia.
---

# Códigos

Esta página define o formato, convenções de nomenclatura e gestão de ciclo de vida do Sistema de Códigos AIMO.

## Formato de Código

Todos os códigos AIMO seguem o formato: **`<PREFIXO>-<TOKEN>`**

| Componente | Descrição | Formato | Exemplo |
| --- | --- | --- | --- |
| `<PREFIXO>` | Identificador de dimensão | 2 letras maiúsculas | FS, UC, DT |
| `-` | Separador | Hífen | - |
| `<TOKEN>` | Token único dentro da dimensão | 3 dígitos (zero-padded) | 001, 002, 003 |

### Exemplos

- `FS-001` - Escopo Funcional: Produtividade do Usuário Final
- `UC-005` - Classe de Caso de Uso: Geração de Código
- `DT-004` - Tipo de Dados: Dados Pessoais
- `CH-003` - Canal: Plugin de IDE
- `IM-002` - Modo de Integração: SaaS Integrado
- `RS-001` - Superfície de Risco: Vazamento de Dados
- `OB-001` - Resultado/Benefício: Eficiência
- `LG-001` - Tipo de Log/Registro: Registro de Solicitação

## Namespaces

A taxonomia AIMO usa 8 namespaces de dimensão:

| ID | Nome | Prefixo | Contagem de Códigos |
| --- | --- | --- | --- |
| **FS** | Escopo Funcional | `FS-` | 6 |
| **UC** | Classe de Caso de Uso | `UC-` | 30 |
| **DT** | Tipo de Dados | `DT-` | 10 |
| **CH** | Canal | `CH-` | 8 |
| **IM** | Modo de Integração | `IM-` | 7 |
| **RS** | Superfície de Risco | `RS-` | 8 |
| **OB** | Resultado / Benefício | `OB-` | 7 |
| **LG** | Tipo Log/Evento | `LG-` | 15 |

**Total: 91 códigos em 8 dimensões**

### Regras de Namespace

1. **Prefixo é fixo**: O prefixo de dimensão de duas letras (FS, UC, etc.) é permanente e nunca mudará.
2. **Zero-padding**: Tokens são sempre 3 dígitos, zero-padded (ex: `001` não `1`).
3. **Atribuição sequencial**: Novos códigos recebem o próximo número disponível dentro de uma dimensão.
4. **Sem reutilização**: Códigos removidos nunca são reatribuídos a significados diferentes.

## Regras de Estabilidade

Estabilidade de código é um princípio crítico para rastreabilidade de auditoria.

### Imutabilidade de ID

- **IDs de código são imutáveis** — uma vez atribuído, um ID de código nunca muda de significado
- Um código como `UC-001` sempre significará "Q&A Geral" por todo seu ciclo de vida
- Se o significado precisar mudar, um novo código é criado

### Política de Não Reutilização

- Códigos deprecados ou removidos **nunca são reatribuídos** a significados diferentes
- Isso garante que evidências históricas permaneçam válidas e rastreáveis
- Exemplo: Se `UC-010` for deprecado, um novo caso de uso recebe `UC-031` (não `UC-010`)

### Depreciação Antes da Remoção

- Códigos devem ser marcados `deprecated` por pelo menos uma versão MINOR antes da remoção
- Remoção só ocorre em incrementos de versão MAJOR
- Veja seção [Ciclo de Vida](#ciclo-de-vida) para detalhes

## Uso

### Dimensões Obrigatórias

Para cada sistema ou caso de uso de IA, você DEVE especificar pelo menos um código de cada dimensão obrigatória:

| Dimensão | Seleção | Notas |
| --- | --- | --- |
| FS | Exatamente 1 | Função de negócio primária |
| UC | 1 ou mais | Tipos de tarefa realizadas |
| DT | 1 ou mais | Classificações de dados |
| CH | 1 ou mais | Canais de acesso |
| IM | Exatamente 1 | Modo de integração |
| RS | 1 ou mais | Categorias de risco |
| LG | 1 ou mais | Tipos de log/evento |

### Dimensões Opcionais

| Dimensão | Seleção | Notas |
| --- | --- | --- |
| OB | 0 ou mais | Benefícios esperados (opcional) |

### Composição de Código

Ao documentar um sistema de IA, códigos de múltiplas dimensões são combinados. A **prioridade de composição** determina a ordem ao listar códigos:

1. FS (Escopo Funcional)
2. UC (Classe de Caso de Uso)
3. DT (Tipo de Dados)
4. CH (Canal)
5. IM (Modo de Integração)
6. RS (Superfície de Risco)
7. OB (Resultado / Benefício)
8. LG (Tipo de Log/Registro)

**Exemplo de composição:**

```
FS: FS-001
UC: UC-001, UC-002
DT: DT-002, DT-004
CH: CH-001
IM: IM-002
RS: RS-001, RS-003
OB: OB-001
LG: LG-001, LG-002
```

## Ciclo de Vida

### Valores de Status

| Status | Descrição | Comportamento do Validador |
| --- | --- | --- |
| `active` | Atualmente válido e em uso | Aceito |
| `deprecated` | Ainda válido mas agendado para remoção | Aceito com aviso |
| `removed` | Não mais válido; não usar | Rejeitado |

### Campos de Metadados de Ciclo de Vida

O dicionário rastreia ciclo de vida com estes campos:

| Campo | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- |
| `status` | Sim | Status atual | `active` |
| `introduced_in` | Sim | Versão quando código foi adicionado | `0.1.0` |
| `deprecated_in` | Não | Versão quando marcado deprecated | `1.2.0` |
| `removed_in` | Não | Versão quando removido | `2.0.0` |
| `replaced_by` | Não | Código(s) de substituição | `UC-015` |
| `backward_compatible` | Sim | Se mudança quebra uso existente | `true` |

### Regras de Depreciação

1. Códigos DEVEM ser marcados `deprecated` por pelo menos uma versão MINOR antes da remoção
2. Códigos deprecated incluem versão `deprecated_in` e `replaced_by` se aplicável
3. Remoção ocorre apenas em incrementos de versão MAJOR
4. Códigos deprecated permanecem válidos para compatibilidade retroativa durante o período de depreciação

**Exemplo de timeline:**

| Versão | Status | Ação |
| --- | --- | --- |
| 0.1.0 | `active` | Código `UC-010` introduzido |
| 1.2.0 | `deprecated` | Marcado deprecated, `replaced_by: UC-031` |
| 2.0.0 | `removed` | Não mais aceito pelo validador |

### Versionamento

Mudanças de código seguem [Semantic Versioning](./08-changelog.md):

- **MAJOR**: Remoção de código ou breaking changes
- **MINOR**: Novos códigos adicionados, códigos deprecated
- **PATCH**: Apenas esclarecimentos de definição (sem mudanças estruturais)

### Compatibilidade Retroativa

O campo `backward_compatible` indica se uma mudança quebra uso existente:

| Valor | Significado |
| --- | --- |
| `true` | Evidências existentes usando este código permanecem válidas |
| `false` | Evidências existentes podem precisar de atualizações (mudança de versão MAJOR) |

## Validação

O validador verifica:

1. Todas as dimensões obrigatórias têm pelo menos um código
2. Dimensões de seleção única têm exatamente um código
3. Todos os códigos existem no dicionário de taxonomia atual
4. Formato de código corresponde ao padrão `<PREFIXO>-<TOKEN>` (ex: `UC-001`)
5. Códigos deprecated são sinalizados com avisos

Veja [Validador](./07-validator.md) para detalhes de implementação.

## Referência SSOT

!!! info "Fonte de Verdade"
    A definição autoritativa é `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv`. Esta página é explicativa. Veja [Guia de Localização](../../contributing/localization.md) para fluxos de trabalho de atualização.

## Páginas Relacionadas

- [Taxonomia](./03-taxonomy.md) - Definições completas de dimensão
- [Dicionário](./05-dictionary.md) - Listagens completas de códigos e definições de colunas
- [Validador](./07-validator.md) - Regras de validação
- [Changelog](./08-changelog.md) - Histórico de versões
