---
description: Histórico de versões do AIMO Standard. Releases oficiais congelados com PDFs prontos para auditoria, artefatos legíveis por máquina, checksums e atestações de proveniência de build.
---

# Versões

Releases oficiais são snapshots congelados publicados com PDFs prontos para auditoria e artefatos legíveis por máquina.

## Release Mais Recente

!!! success "Versão Atual"
    **v0.0.2** (2026-02-02) — [Ver Documentação](../current/index.md) | [GitHub Release](https://github.com/billyrise/aimo-standard/releases/tag/v0.0.2)

## Histórico de Versões

| Versão | Data | Notas de Release | PDF (EN) | PDF (JA) | Artefatos | Checksums |
| :------ | :--- | :------------ | :------- | :------- | :-------- | :-------- |
| **v0.0.2** | 2026-02-02 | [Changelog](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/SHA256SUMS.txt) |
| **v0.0.1** | 2026-02-02 | [Changelog](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/SHA256SUMS.txt) |

!!! note "Fonte de Dados"
    Esta tabela de versões está sincronizada com [GitHub Releases](https://github.com/billyrise/aimo-standard/releases). Cada tag de release (`vX.Y.Z`) corresponde a um snapshot congelado da especificação.

## Fonte única de verdade (SSOT) para "latest"

A **definição autoritativa de "latest"** é a tag **latest** dos [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) (`releases/latest`). O caminho do site `/latest/` redireciona sempre para esse release. Não existe um "latest do site" separado — o fluxo de release implanta a versão etiquetada e define-a como alias `latest` num único passo.

| Fonte | Papel |
|--------|------|
| **Tag latest do GitHub Release** | SSOT — única definição de "release atual" |
| **Tabela de versões** (esta página) | Sincronizada com releases via fluxo de release; deve coincidir com o tag antes do deploy |
| **Changelog** | Histórico de alterações normativo; as notas de release referenciam-no |
| **Site `/latest/`** | Redirecionamento para a mesma versão que GitHub Release latest |

Para detalhes do processo de release, ver [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) e o [fluxo de release](https://github.com/billyrise/aimo-standard/blob/main/.github/workflows/release.yml). A tabela de versões e o Changelog são atualizados como parte da preparação do release para coincidirem sempre com a versão implantada.

## Avisos legais e marcas

**English notice (key facts):** Only AIMOaaS has been filed for trademark registration by RISEby Inc. (pending). "AIMO" is a registered trademark owned by third parties; RISEby Inc. does not claim ownership. For full trademark status and usage, see [Governance → Marcas Registradas](../../governance/trademarks.md) and [TRADEMARKS.md](https://github.com/billyrise/aimo-standard/blob/main/TRADEMARKS.md).

## Para auditores: URL canónica e fixação de versão

Para citar uma versão específica em relatórios de auditoria e garantir reprodutibilidade:

1. **URL canónica**: Use a URL de documentação fixa para essa versão, ex. `https://standard.aimoaas.com/0.0.3/` (substitua `0.0.3` pela versão utilizada).
2. **Fixação de versão**: Registe o **tag de release** (ex. `v0.0.3`) e opcionalmente o **hash de commit** da página [GitHub Release](https://github.com/billyrise/aimo-standard/releases). Isto permite verificação independente de que o snapshot da especificação corresponde aos ativos do release (PDF, ZIP, checksums).
3. **Alinhamento de evidência**: Indique na sua submissão com que versão do AIMO Standard (ex. `v0.0.3`) o seu evidence bundle está alinhado, e obtenha o validador e os esquemas desse mesmo release.

## Camadas de versão

O AIMO Standard utiliza três conceitos de versão. No release atual estão alinhados; em releases futuros podem ser versionados independentemente.

| Camada | Descrição | Onde aparece |
|--------|-----------|--------------|
| **Versão Standard** (site/release) | O tag de release e o snapshot de documentação (ex. `v0.0.3`). | Tabela de versões, GitHub Releases, URLs `/X.Y.Z/`. |
| **Versão do esquema Taxonomy** | Versão do sistema de códigos e definições taxonomy/esquema. | `taxonomy_version` em manifestos; `$id` do esquema ou docs. |
| **Versão do conteúdo Dictionary** | Versão das entradas do dicionário (códigos e definições). | Metadados do dicionário; igual à taxonomy em 0.0.x. |

Ao citar "AIMO Standard vX.Y.Z", a **versão Standard** é a que define o snapshot canónico. O Validator e os Minimum Evidence Requirements referem-se aos artefactos e esquemas desse release.

## Procedimento de Verificação

Auditores e implementadores devem verificar integridade de download usando checksums SHA-256:

### 1. Baixar Ativos de Release

=== "Linux / macOS"

    ```bash
    # Baixar todos os ativos para uma versão específica
    VERSION=v0.0.1
    BASE_URL="https://github.com/billyrise/aimo-standard/releases/download/${VERSION}"

    curl -LO "${BASE_URL}/trust_package.pdf"
    curl -LO "${BASE_URL}/trust_package.ja.pdf"
    curl -LO "${BASE_URL}/aimo-standard-artifacts.zip"
    curl -LO "${BASE_URL}/SHA256SUMS.txt"
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Baixar todos os ativos para uma versão específica
    $VERSION = "v0.0.1"
    $BASE_URL = "https://github.com/billyrise/aimo-standard/releases/download/$VERSION"

    Invoke-WebRequest -Uri "$BASE_URL/trust_package.pdf" -OutFile trust_package.pdf
    Invoke-WebRequest -Uri "$BASE_URL/trust_package.ja.pdf" -OutFile trust_package.ja.pdf
    Invoke-WebRequest -Uri "$BASE_URL/aimo-standard-artifacts.zip" -OutFile aimo-standard-artifacts.zip
    Invoke-WebRequest -Uri "$BASE_URL/SHA256SUMS.txt" -OutFile SHA256SUMS.txt
    ```

### 2. Verificar Checksums

=== "Linux"

    ```bash
    # Verificar todos os arquivos baixados contra checksums
    sha256sum -c SHA256SUMS.txt

    # Saída esperada (todos devem mostrar "OK"):
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "macOS"

    ```bash
    # Verificar todos os arquivos baixados contra checksums
    shasum -a 256 -c SHA256SUMS.txt

    # Saída esperada (todos devem mostrar "OK"):
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Verificar cada arquivo
    Get-FileHash .\trust_package.pdf -Algorithm SHA256
    Get-FileHash .\trust_package.ja.pdf -Algorithm SHA256
    Get-FileHash .\aimo-standard-artifacts.zip -Algorithm SHA256

    # Comparar saída de Hash com SHA256SUMS.txt
    Get-Content .\SHA256SUMS.txt
    ```

### 3. Verificação Manual (Alternativa)

=== "Linux"

    ```bash
    # Calcular hash para um arquivo específico
    sha256sum trust_package.pdf

    # Comparar saída com SHA256SUMS.txt
    cat SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # Calcular hash para um arquivo específico
    shasum -a 256 trust_package.pdf

    # Comparar saída com SHA256SUMS.txt
    cat SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Calcular hash para um arquivo específico
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # Ver arquivo de checksums
    Get-Content .\SHA256SUMS.txt
    ```

!!! tip "Para Auditores"
    Sempre obtenha o arquivo de checksums diretamente do GitHub Release oficial, não da parte submissora. Isso garante verificação independente.

### 4. Verificar Proveniência de Build (Atestação)

Todos os ativos de release incluem atestações de proveniência de build assinadas criptograficamente geradas pelo GitHub Actions. Isso permite verificar que ativos foram construídos no repositório oficial sem adulteração.

**Pré-requisitos**: Instale [GitHub CLI](https://cli.github.com/) (`gh`)

```bash
# Baixar ativos de release usando GitHub CLI
VERSION=v0.0.1
gh release download "$VERSION" --repo billyrise/aimo-standard

# Verificar atestação para cada ativo
gh attestation verify trust_package.pdf --repo billyrise/aimo-standard
gh attestation verify trust_package.ja.pdf --repo billyrise/aimo-standard
gh attestation verify aimo-standard-artifacts.zip --repo billyrise/aimo-standard
gh attestation verify SHA256SUMS.txt --repo billyrise/aimo-standard
```

**Saída esperada** (sucesso):

```
Loaded digest sha256:abc123... for file trust_package.pdf
Loaded 1 attestation from GitHub API
✓ Verification succeeded!
```

**Verificação offline** (ambientes air-gapped):

```bash
# Primeiro, baixe a trusted root (requer rede uma vez)
gh attestation trusted-root > trusted-root.jsonl

# Depois verifique offline
gh attestation verify trust_package.pdf \
  --repo billyrise/aimo-standard \
  --custom-trusted-root trusted-root.jsonl
```

!!! info "O que atestação prova"
    Atestação de proveniência de build prova criptograficamente que os ativos de release foram:

    1. Construídos pelo GitHub Actions (não pela máquina local de um desenvolvedor)
    2. Construídos do repositório oficial `billyrise/aimo-standard`
    3. Construídos do commit exato associado à tag de release
    4. Não modificados após o build ser concluído

## Compatibilidade

AIMO Standard segue [Semantic Versioning](https://semver.org/) (SemVer):

| Tipo de Mudança | Bump de Versão | Impacto |
| :---------- | :----------- | :----- |
| **MAJOR** | X.0.0 | Breaking changes — migração necessária |
| **MINOR** | 0.X.0 | Adições backward-compatible |
| **PATCH** | 0.0.X | Correções e esclarecimentos |

Para a política de versionamento completa, veja [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md).

## Migração

Ao fazer upgrade entre versões com breaking changes:

1. Verifique o [Changelog](../current/08-changelog.md) para breaking changes
2. Revise o [Guia de Migração](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) para caminhos de upgrade específicos
3. Atualize seu Pacote de Evidências para alinhar com os novos requisitos de schema
4. Re-execute o validador para verificar conformidade

!!! warning "Breaking Changes"
    Atualizações de versão MAJOR podem requerer mudanças em Pacotes de Evidências existentes. Sempre revise o guia de migração antes de fazer upgrade.

## Snapshots de Documentação Versionados

Cada release cria um snapshot de documentação congelado acessível em:

- Produção: `https://standard.aimoaas.com/{version}/` (ex: `/0.0.1/`)
- GitHub Pages: `https://billyrise.github.io/aimo-standard/{version}/`

### Tipos de URL e Seus Significados

| Padrão de URL | Descrição | Para Citações de Auditoria? |
|-------------|-------------|---------------------|
| `/X.Y.Z/` (ex: `/0.0.1/`) | **Release congelado** — snapshot imutável | **Sim** (preferido) |
| `/latest/` | **Alias** — redireciona para release mais recente | Sim (resolve para `/X.Y.Z/`) |
| `/dev/` | **Preview** — conteúdo não lançado da branch main | **Não** (não para citações) |

!!! warning "Entendendo `/latest/` vs `/dev/`"
    - **`/latest/`** é um alias (redirect) para a versão mais recente **lançada**. É seguro para citações pois resolve para um snapshot congelado.
    - **`/dev/`** reflete a branch `main` atual e pode conter **mudanças não lançadas**. Nunca cite `/dev/` em relatórios de auditoria.

### FAQ

??? question "Por que `/latest/` não é um número de versão?"
    `/latest/` é um alias de conveniência que sempre redireciona para o release estável mais recente (ex: `/0.0.1/`). Isso permite que usuários salvem um único URL enquanto automaticamente obtêm a versão atual. Para auditorias formais requerendo imutabilidade, cite a URL de versão explícita.

??? question "Qual URL auditores devem citar?"
    - **Auditorias formais (imutabilidade necessária)**: Use `/X.Y.Z/` (ex: `https://standard.aimoaas.com/0.0.1/standard/current/`)
    - **Referências gerais**: `/latest/` é aceitável pois redireciona para o release atual
    - **Nunca cite**: `/dev/` (não lançado, sujeito a mudanças)

??? question "E se `/latest/` mostrar conteúdo diferente do esperado?"
    Isso seria um bug de deployment. Se você suspeita que `/latest/` difere do [GitHub Release](https://github.com/billyrise/aimo-standard/releases) mais recente, por favor [reporte uma issue](https://github.com/billyrise/aimo-standard/issues). O alias `/latest/` deve sempre redirecionar para o release com tag mais recente.

## Recursos

- **[Hub de Releases](../../../releases/)** — Preparação de submissão, verificação de auditor, declaração de não-sobrereivindicação
- **[Trust Package](../../governance/trust-package.md)** — Materiais de garantia prontos para auditoria
- **[Changelog (detalhado)](../current/08-changelog.md)** — Histórico completo de mudanças com rastreamento de depreciação
- **[VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)** — Política de versionamento completa
