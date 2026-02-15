---
description: Guia de contribuição do AIMO Standard - Como contribuir código, documentação e traduções. Diretrizes de issues e PRs.
---
<!-- aimo:translation_status=translated -->

# Contribuindo

Esta página fornece diretrizes para contribuir com o AIMO Standard.

## Início Rápido

1. Faça fork do repositório
2. Crie uma branch de feature
3. Faça alterações seguindo as diretrizes abaixo
4. Execute verificações de qualidade
5. Envie um pull request

## Princípios Chave

| Princípio | Descrição |
| --------- | ----------- |
| Inglês é canônico | Edite `docs/en/` primeiro, depois atualize `docs/ja/` |
| SSOT | Este repositório é a fonte única de verdade |
| Sem edições manuais em arquivos gerados | Edite fontes, regenere, faça commit |
| Todas as alterações via PR | Mesmo mantenedores usam pull requests |

## Verificações de Qualidade

Antes de enviar um PR, execute:

```bash
# Ative ambiente virtual
source .venv/bin/activate

# Execute lints
python tooling/checks/lint_i18n.py
python tooling/checks/lint_schema.py
python tooling/audit/baseline_audit.py --check

# Build da documentação
mkdocs build --strict
```

## Tipos de Alteração

| Tipo | Exemplos | Requisitos de Revisão |
| ---- | -------- | ------------------- |
| Normativa | Alterações de schema, requisitos | Mantenedor + discussão |
| Não-normativa | Typos, esclarecimentos | Aprovação do mantenedor |
| i18n | Traduções | Estrutura deve corresponder a EN |
| Tooling | CI/CD, scripts | Aprovação do mantenedor |

## Diretrizes i18n

### Ordem de Atualização

1. Edite fonte em inglês (`docs/en/...`)
2. Atualize tradução em japonês (`docs/ja/...`)
3. Execute `lint_i18n.py` para verificar consistência
4. Faça commit de ambos juntos

### Requisitos de Estrutura

- Mesmos nomes de arquivo em ambos os idiomas
- Mesma hierarquia de cabeçalhos
- Mesma contagem de páginas por seção

## Checklist de PR

Ao enviar um PR, verifique:

- [ ] Tipo de alteração identificado (docs / schema / examples / tooling)
- [ ] Avaliação de breaking change concluída
- [ ] i18n: EN e JA atualizados juntos (se aplicável)
- [ ] Verificações de qualidade passam
- [ ] Issues relacionadas vinculadas

## Breaking Changes

Breaking changes requerem:

1. Discussão em issue antes da implementação
2. Bump de versão conforme [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)
3. Entrada no changelog com orientação de migração

## Atualizações de Reivindicação de Conformidade

Para adicionar ou modificar reivindicações de conformidade:

1. Atualize o YAML do mapa de cobertura
2. Atualize páginas de documentação correspondentes
3. Execute testes do validador
4. Documente a justificativa do mapeamento

## Diretrizes Completas

Veja [CONTRIBUTING.md](https://github.com/billyrise/aimo-standard/blob/main/CONTRIBUTING.md) para o guia de nível raiz.

## Páginas Relacionadas

- [Governança](../) — Governança do projeto
- [Guia de Localização](../../contributing/localization/) — Detalhes de i18n
- [Limite de Responsabilidade](../responsibility-boundary/) — O que AIMO fornece
