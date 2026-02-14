---
description: Política de SEO e URL canônica AIMO - Estratégia de canonicalização de URL para mecanismos de busca, auditores e referências externas.
---

# SEO e Política Canônica

Esta página documenta como o AIMO Standard gerencia canonicalização de URL para mecanismos de busca, auditores e referências externas.

## Sites de Produção vs Espelho

| Ambiente | URL | Papel | Indexável |
|-------------|-----|------|-----------|
| **Produção** | `https://standard.aimoaas.com/` | Site canônico para todos os propósitos | Sim |
| GitHub Pages | `https://billyrise.github.io/aimo-standard/` | Espelho temporário / preview de CI | Não (noindex) |

**Princípio chave**: Produção (`standard.aimoaas.com`) é a URL autoritativa. GitHub Pages serve como backup/espelho temporário e não deve ser citado em relatórios de auditoria ou referências externas.

## Estratégia de URL Canônica

### Como URLs Canônicas São Geradas

AIMO Standard usa [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) com a seguinte configuração:

```yaml
# mkdocs.yml
site_url: https://standard.aimoaas.com/
```

Esta configuração `site_url` garante:

1. **`<link rel="canonical">`** — Cada página HTML gerada inclui um link canônico apontando para a URL de Produção.
2. **`sitemap.xml`** — Todas as URLs no sitemap referenciam Produção.
3. **`robots.txt`** — Referência de sitemap aponta para Produção.
4. **Alternates `hreflang`** — Alternates de idioma usam URLs de Produção.

### Canônicos Específicos por Idioma

| Idioma | Padrão de URL | Exemplo |
|----------|-------------|---------|
| Inglês (padrão) | `https://standard.aimoaas.com/{X.Y.Z}/{path}` | `https://standard.aimoaas.com/{X.Y.Z}/governance/` |
| Japonês | `https://standard.aimoaas.com/{X.Y.Z}/ja/{path}` | `https://standard.aimoaas.com/{X.Y.Z}/ja/governance/` |

Cada versão de idioma é auto-canônica e inclui alternates `hreflang` para o(s) outro(s) idioma(s) mais `x-default` apontando para a versão em inglês.

### Documentação Versionada e Canônicos

AIMO Standard usa [mike](https://github.com/jimporter/mike) para versionamento de documentação com `alias_type: redirect`:

| Versão | Padrão de URL | Status Canônico | Indexável |
|---------|-------------|------------------|-----------|
| Versionada (ex: `0.0.1`) | `https://standard.aimoaas.com/0.0.1/` | Canônica para aquela versão específica | Sim |
| `latest` (alias) | `https://standard.aimoaas.com/latest/` | **Redireciona** para release atual | Sim (via alvo) |
| `dev` | `https://standard.aimoaas.com/dev/` | Apenas preview | **Não** (noindex aplicado) |

**Distinções críticas:**

| Aspecto | `/X.Y.Z/` | `/latest/` | `/dev/` |
|--------|-----------|------------|---------|
| Conteúdo | Snapshot congelado | Redirect para `/X.Y.Z/` | Preview da branch main |
| Mutável | Nunca | Ponteiro atualiza no release | Contínuo |
| Para auditorias | **Sim (preferido)** | Sim (resolve para congelado) | **Nunca** |
| SEO | Indexado | Indexado via alvo | noindex |

**Como alias_type: redirect funciona:**

Em vez de copiar arquivos, `/latest/` contém páginas de redirect apontando para o release atual:

```html
<!-- /latest/index.html -->
<!-- Latest alias (redirect stub); canonical points to versioned snapshot -->
<meta http-equiv="refresh" content="0; url=../{X.Y.Z}/">
<link rel="canonical" href="https://standard.aimoaas.com/{X.Y.Z}/">
```

Isso garante:

1. **Sem drift de conteúdo** — `/latest/` não pode divergir do release que aponta.
2. **Sem conteúdo duplicado** — Mecanismos de busca veem uma fonte canônica.
3. **Atualizações atômicas** — Mudar o alias atualiza todas as páginas de uma vez.

!!! info "Git Tag vs. Caminho do Site"
    Tags de release Git usam prefixo `v` (ex: `v0.0.1`), mas caminhos do site omitem o `v` (ex: `/0.0.1/`). Esta é prática padrão para ferramentas de versionamento de documentação como mike.

## Orientação para Auditores: Qual URL Citar

Ao citar AIMO Standard em relatórios de auditoria, documentação de conformidade ou referências externas:

### URLs de Citação Recomendadas

| Caso de Uso | URL Recomendada |
|----------|-----------------|
| Especificação estável atual | `https://standard.aimoaas.com/{X.Y.Z}/standard/current/` |
| Versão específica (para auditoria) | `https://standard.aimoaas.com/{X.Y.Z}/standard/current/` |
| Governança e políticas | `https://standard.aimoaas.com/{X.Y.Z}/governance/` |
| Trust Package | `https://standard.aimoaas.com/{X.Y.Z}/governance/trust-package/` |

### NÃO Citar

- ~~`https://billyrise.github.io/aimo-standard/`~~ — Espelho temporário, não canônico
- ~~`https://standard.aimoaas.com/dev/`~~ — Versão de desenvolvimento, sujeita a mudanças

### Citação Versionada para Imutabilidade

Para auditorias formais requerendo referências imutáveis, use URLs de snapshot versionado:

```
https://standard.aimoaas.com/1.0.0/standard/current/01-overview/
```

Snapshots versionados são congelados no momento do release e não mudarão.

!!! note "Formato de URL"
    Caminhos do site usam números de versão sem o prefixo `v`. Para versão `v1.0.0`, use `/1.0.0/` nas URLs.

## Implementação Técnica

### Exemplo de HTML Gerado

Cada página HTML gerada inclui tags canônicas e hreflang no `<head>`:

```html
<!-- Canônico (sempre aponta para Produção) -->
<link rel="canonical" href="https://standard.aimoaas.com/{X.Y.Z}/governance/">

<!-- Alternates de idioma -->
<link rel="alternate" hreflang="en" href="https://standard.aimoaas.com/{X.Y.Z}/governance/">
<link rel="alternate" hreflang="ja" href="https://standard.aimoaas.com/{X.Y.Z}/ja/governance/">
<link rel="alternate" hreflang="x-default" href="https://standard.aimoaas.com/{X.Y.Z}/governance/">
```

### robots.txt

```
User-agent: *
Allow: /

Sitemap: https://standard.aimoaas.com/sitemap.xml
```

### Sitemap

O sitemap é gerado pelo plugin `mkdocs-static-i18n` e inclui:

- Todas as URLs de Produção
- Alternates `hreflang` para cada idioma

## Configuração Noindex

### `/dev/` (Preview) — Noindex Obrigatório

A versão `/dev/` contém conteúdo não lançado e DEVE ter noindex para prevenir:

- Mecanismos de busca indexando conteúdo instável
- Usuários encontrando `/dev/` via busca e citando em auditorias
- Confusão entre conteúdo lançado e não lançado

**Implementação:**

O workflow `deploy-dev.yml` injeta uma tag meta noindex em todas as páginas `/dev/` via override de tema:

```html
<!-- Injetado em páginas /dev/ apenas -->
<meta name="robots" content="noindex, nofollow">
```

### Espelho GitHub Pages — Noindex

Ao implantar no GitHub Pages (o site espelho em `billyrise.github.io`), todas as páginas devem ter noindex para prevenir indexação duplicada:

```html
<meta name="robots" content="noindex, nofollow">
```

Isso garante que mecanismos de busca sempre priorizem as URLs canônicas de Produção em `standard.aimoaas.com`.

## Verificação

Após cada build, você pode verificar URLs canônicas por:

1. **Inspecionando HTML gerado** — Verifique diretório `site/` após `mkdocs build`
2. **Usando DevTools do navegador** — Inspecione seção `<head>` em páginas implantadas
3. **Google Search Console** — Monitore quais URLs estão indexadas

Comando de verificação exemplo:

```bash
mkdocs build
grep -r 'rel="canonical"' site/ | head -5
```

Saída esperada deve mostrar URLs de Produção, ex:

```
site/index.html:<link rel="canonical" href="https://standard.aimoaas.com/">
site/governance/index.html:<link rel="canonical" href="https://standard.aimoaas.com/governance/">
```

## Documentação Relacionada

- [Trust Package](../trust-package/) — Materiais prontos para auditoria
- [Releases](../../releases/) — Histórico de versões e changelog
- [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) — Política de versões
