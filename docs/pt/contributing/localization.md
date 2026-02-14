---
description: Guia de localização AIMO - estrutura i18n, fluxo de manutenção e princípios SSOT para documentação multilíngue.
---

# Guia de Localização

Esta página documenta a estrutura de localização (i18n), fluxo de trabalho de manutenção e princípios SSOT (Single Source of Truth) para a documentação do AIMO Standard.

## Política de Pureza de Idioma

**Cada página de idioma deve conter apenas conteúdo daquele idioma.**

| Regra | Descrição |
| --- | --- |
| **Páginas EN** | Não devem conter caracteres CJK ou referências a colunas específicas de idioma (ex: sufixos `_ja`) |
| **Páginas JA** | Não devem explicar terminologia específica de EN como se fosse a estrutura canônica |
| **Exceções** | Listadas em `MIXED_LANGUAGE_ALLOWLIST` em `tooling/checks/lint_i18n.py` |

Esta política garante:
1. Leitores veem apenas seu idioma selecionado
2. Adicionar novos idiomas não requer atualizar páginas existentes
3. CI pode detectar violações automaticamente

## Estrutura de Idiomas

A documentação do AIMO Standard usa uma **estrutura i18n baseada em pastas**:

```
docs/
├── en/           # Inglês (canônico)
├── ja/           # Japonês (日本語)
├── es/           # Espanhol (Español)
├── fr/           # Francês (Français)
├── de/           # Alemão (Deutsch)
├── pt/           # Português (Português)
├── it/           # Italiano (Italiano)
├── zh/           # Chinês Simplificado (简体中文)
├── zh-TW/        # Chinês Tradicional (繁體中文)
└── ko/           # Coreano (한국어)
```

- **Inglês é canônico**: A pasta `docs/en/` é a fonte autoritativa para conteúdo da documentação.
- **Outros idiomas espelham a estrutura**: Cada pasta de idioma (`ja/`, etc.) mantém a mesma estrutura de arquivos que `en/`.
- **Mesmos nomes de arquivo**: Todos os idiomas usam extensão `.md` (sem sufixo de idioma em nomes de arquivo).
- **Fallback para inglês**: Traduções ausentes automaticamente recorrem ao conteúdo em inglês.

## Modelo de Dados da Taxonomia

A taxonomia usa uma **estrutura canônica neutra de idioma** com pacotes de tradução separados:

```
data/
└── taxonomy/
    ├── canonical.yaml           # Neutro de idioma (códigos, status, ciclo de vida)
    └── i18n/
        ├── en.yaml              # Rótulos e definições em inglês
        ├── ja.yaml              # Rótulos e definições em japonês
        └── {lang}.yaml          # Idiomas adicionais (template vazio)
```

### Estrutura Canônica (`canonical.yaml`)

Contém dados neutros de idioma:

- Identificadores de código (ex: `FS-001`, `UC-001`)
- Status (`active`, `deprecated`, `removed`)
- Metadados de ciclo de vida (`introduced_in`, `deprecated_in`, `removed_in`, `replaced_by`)
- Notas de escopo e exemplos (em inglês, como referências técnicas)

### Pacotes de Tradução (`i18n/*.yaml`)

Cada pacote de idioma contém:

- Nomes de dimensões (ex: "Functional Scope")
- Rótulos de códigos (ex: "End-user Productivity")
- Definições de códigos

**Fallback**: Se uma tradução estiver ausente, o sistema usa inglês.

## Princípio SSOT

AIMO usa uma **arquitetura SSOT-first** para dados de taxonomia:

| Tipo de Ativo | Localização SSOT | Descrição |
| --- | --- | --- |
| **Taxonomia (estrutura)** | `data/taxonomy/canonical.yaml` | Estrutura neutra de idioma (SSOT) |
| **Taxonomia (i18n)** | `data/taxonomy/i18n/*.yaml` | Traduções por idioma (SSOT) |
| **Mapa de Cobertura** | `coverage_map/coverage_map.yaml` | Mapeamento framework-para-evidência |
| **Schemas** | `schemas/jsonschema/` | Schemas de validação JSON |

### Arquivos Derivados

Os seguintes arquivos são **gerados** do SSOT e NÃO devem ser editados manualmente:

| Arquivo | Gerado De | Gerador |
| --- | --- | --- |
| `artifacts/taxonomy/{version}/{lang}/taxonomy_dictionary.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_en.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_ja.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/code_system.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/dimensions_en_ja.md` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_dictionary.json` | canonical + i18n | `build_artifacts.py` |

### Códigos de Idioma (BCP47)

AIMO usa códigos de idioma BCP47:

| Código | Idioma | Status |
| --- | --- | --- |
| `en` | Inglês | Canônico (fonte) |
| `ja` | Japonês (日本語) | Ativo |
| `es` | Espanhol (Español) | Ativo |
| `fr` | Francês (Français) | Ativo |
| `de` | Alemão (Deutsch) | Ativo |
| `pt` | Português (Português) | Ativo |
| `it` | Italiano (Italiano) | Ativo |
| `zh` | Chinês Simplificado (简体中文) | Ativo |
| `zh-TW` | Chinês Tradicional (繁體中文) | Ativo |
| `ko` | Coreano (한국어) | Ativo |

### Arquivos CSV Legados (Congelados)

Os arquivos CSV legados EN/JA mistos em `source_pack/03_taxonomy/legacy/` são:

- **Congelados em 21 colunas** — nenhuma nova coluna de idioma será adicionada
- **Mantidos para compatibilidade retroativa** — integrações existentes podem continuar a usá-los
- **Aplicados por CI** — adicionar `label_es`, `definition_de`, etc. falhará o build

Para novos idiomas, use os artefatos por idioma em `artifacts/taxonomy/{version}/{lang}/`.

## Rastreamento de Frescor de Tradução

AIMO usa um sistema de **Rastreamento de Frescor de Tradução** para manter consistência entre inglês (fonte) e conteúdo traduzido.

### Como Funciona

1. Cada arquivo traduzido contém metadados rastreando de qual versão da fonte em inglês foi traduzido
2. Quando conteúdo em inglês é atualizado, o sistema detecta traduções desatualizadas
3. CI avisa sobre traduções desatualizadas mas não bloqueia (traduções podem atrasar)

### Metadados de Tradução

Arquivos traduzidos incluem metadados de frontmatter:

```yaml
---
# TRANSLATION METADATA - DO NOT REMOVE
source_file: en/standard/current/01-overview.md
source_hash: abc123def456
translation_date: 2026-02-02
translator: human|machine|hybrid
translation_status: current|outdated|needs_review
---
```

### Usando a Ferramenta de Sincronização

```bash
# Verificar todas as traduções quanto ao frescor
python tooling/i18n/sync_translations.py --check

# Verificar idioma específico
python tooling/i18n/sync_translations.py --check --lang ja

# Gerar relatório de tradução
python tooling/i18n/sync_translations.py --report

# Inicializar novo idioma (copiar EN como base)
python tooling/i18n/sync_translations.py --init-lang es

# Atualizar metadados após completar tradução
python tooling/i18n/sync_translations.py --update-meta docs/ja/index.md
```

Para especificação técnica detalhada, veja `tooling/i18n/TRANSLATION_SYNC_SPEC.md`.

## Fluxos de Trabalho de Atualização

### Atualizações de Taxonomia (Novo Fluxo SSOT-First)

1. Edite o SSOT em `data/taxonomy/`:
   - Alterações de estrutura → `canonical.yaml`
   - Traduções em inglês → `i18n/en.yaml`
   - Traduções em japonês → `i18n/ja.yaml`
2. Execute validação: `python tooling/checks/lint_taxonomy_ssot.py`
3. Regenere todos os arquivos derivados: `python tooling/taxonomy/build_artifacts.py --version current --langs en ja`
4. Atualize páginas de documentação conforme necessário
5. Faça commit de todas as alterações juntas

### Atualizações do Mapa de Cobertura

1. Edite `coverage_map/coverage_map.yaml` (o SSOT)
2. Atualize as tabelas das páginas de framework correspondentes (`docs/en/coverage-map/*.md`)
3. Atualize traduções em japonês (`docs/ja/coverage-map/*.md`)
4. Faça commit de todas as alterações juntas

### Atualizações de Documentação

1. Edite a fonte em inglês (`docs/en/...`)
2. Atualize traduções conforme necessário (ou marque-as para atualização posterior)
3. Execute `python tooling/i18n/sync_translations.py --check` para ver traduções desatualizadas
4. Execute `python tooling/checks/lint_i18n.py` para verificar consistência de cabeçalhos
5. Execute `mkdocs build --strict` para verificar build
6. Faça commit de todas as alterações juntas

!!! note "Prioridade de Tradução"
    Nem todas as traduções precisam ser atualizadas imediatamente. Páginas Tier 1 (críticas) devem ser priorizadas:
    
    - `index.md`
    - `standard/current/*.md`
    - `governance/index.md`
    - `releases/`

## Adicionando um Novo Idioma (5 Passos)

Para adicionar um novo idioma (ex: Espanhol):

### Passo 1: Gerar Pacote de Taxonomia

```bash
python tooling/taxonomy/build_i18n_taxonomy.py --add-lang es --lang-name "Español"
```

Cria `data/taxonomy/i18n/es.yaml` com referências em inglês como comentários.

### Passo 2: Criar Pasta de Docs

```bash
mkdir -p docs/es && cp -r docs/en/* docs/es/
```

### Passo 3: Atualizar mkdocs.yml

```yaml
plugins:
  - i18n:
      languages:
        - locale: es
          name: Español
          build: true
```

### Passo 4: Traduzir

- Traduza `data/taxonomy/i18n/es.yaml`
- Traduza arquivos em `docs/es/`

### Passo 5: Verificar

```bash
python tooling/checks/lint_i18n.py && mkdocs build --strict
```

!!! success "Feito"
    Novo idioma agora está disponível em `/dev/es/`

## Convenções de Nomenclatura de Arquivos

| Padrão | Exemplo | Descrição |
| --- | --- | --- |
| `index.md` | `docs/en/governance/index.md` | Página de destino da seção |
| `{topic}.md` | `docs/en/governance/trust-package.md` | Página de tópico |
| `{NN}-{topic}.md` | `docs/en/standard/current/03-taxonomy.md` | Página de especificação numerada |

## Verificações de Qualidade

Execute estas verificações antes de fazer commit:

```bash
# estrutura i18n, consistência de cabeçalhos e detecção de frases obsoletas
python tooling/checks/lint_i18n.py

# lints de schema e manifesto
python tooling/checks/lint_schema.py
python tooling/checks/lint_manifest.py

# lints de SSOT de taxonomia
python tooling/checks/lint_taxonomy_ssot.py --required-langs en
python tooling/checks/lint_legacy_csv.py
python tooling/checks/lint_taxonomy_dictionary.py
python tooling/checks/lint_taxonomy_json.py

# artefatos de taxonomia atualizados
python tooling/taxonomy/build_artifacts.py --check

# verificação de build
mkdocs build --strict
```

## Páginas Relacionadas

- [Releases](../../releases/) — Pacotes para download
- [Governança](../../governance/) — Governança do projeto
