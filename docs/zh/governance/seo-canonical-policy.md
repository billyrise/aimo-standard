---
description: AIMO SEO 和规范URL政策 - 面向搜索引擎、审计师和外部引用的URL规范化策略。
---
<!-- aimo:translation_status=translated -->

# SEO 与规范策略

本页记录 AIMO 标准如何管理面向搜索引擎、审计师和外部引用的URL规范化。

## 生产与镜像站点

| 环境 | URL | 角色 | 可索引 |
|-------------|-----|------|-----------|
| **生产** | `https://standard.aimoaas.com/` | 所有用途的规范站点 | 是 |
| GitHub Pages | `https://billyrise.github.io/aimo-standard/` | 临时镜像/CI预览 | 否（noindex） |

**关键原则**：生产（`standard.aimoaas.com`）是权威URL。GitHub Pages 作为临时备份/镜像，不应在审计报告或外部引用中引用。

## 规范URL策略

### 规范URL如何生成

AIMO 标准使用 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)，配置如下：

```yaml
# mkdocs.yml
site_url: https://standard.aimoaas.com/
```

此 `site_url` 设置确保：

1. **`<link rel="canonical">`** — 每个生成的HTML页面包含指向生产URL的规范链接。
2. **`sitemap.xml`** — 站点地图中的所有URL引用生产。
3. **`robots.txt`** — 站点地图引用指向生产。
4. **`hreflang` 备选** — 语言备选使用生产URL。

### 语言特定的规范

| 语言 | URL 模式 | 示例 |
|----------|-------------|---------|
| 英语（默认） | `https://standard.aimoaas.com/{X.Y.Z}/{path}` | `https://standard.aimoaas.com/{X.Y.Z}/governance/` |
| 日语 | `https://standard.aimoaas.com/{X.Y.Z}/ja/{path}` | `https://standard.aimoaas.com/{X.Y.Z}/ja/governance/` |

每个语言版本是自规范的，并包含指向其他语言的 `hreflang` 备选，以及指向英语版本的 `x-default`。

### 版本化文档和规范

AIMO 标准使用 [mike](https://github.com/jimporter/mike) 进行文档版本控制，配置 `alias_type: redirect`：

| 版本 | URL 模式 | 规范状态 | 可索引 |
|---------|-------------|------------------|-----------|
| 版本化（例如 `0.0.1`） | `https://standard.aimoaas.com/0.0.1/` | 该特定版本的规范 | 是 |
| `latest`（别名） | `https://standard.aimoaas.com/latest/` | **重定向**到当前版本 | 是（通过目标） |
| `dev` | `https://standard.aimoaas.com/dev/` | 仅预览 | **否**（强制 noindex） |

**关键区别：**

| 方面 | `/X.Y.Z/` | `/latest/` | `/dev/` |
|--------|-----------|------------|---------|
| 内容 | 冻结快照 | 重定向到 `/X.Y.Z/` | 主分支预览 |
| 可变 | 从不 | 指针在发布时更新 | 持续 |
| 用于审计 | **是（首选）** | 是（解析到冻结版本） | **从不** |
| SEO | 已索引 | 通过目标索引 | noindex |

**alias_type: redirect 如何工作：**

`/latest/` 包含指向当前版本的重定向页面，而不是复制文件：

```html
<!-- /latest/index.html -->
<!-- Latest alias (redirect stub); canonical points to versioned snapshot -->
<meta http-equiv="refresh" content="0; url=../{X.Y.Z}/">
<link rel="canonical" href="https://standard.aimoaas.com/{X.Y.Z}/">
```

这确保：

1. **无内容漂移** — `/latest/` 不会与其指向的版本产生偏差。
2. **无重复内容** — 搜索引擎看到一个规范来源。
3. **原子更新** — 更改别名会一次更新所有页面。

!!! info "Git 标签与站点路径"
    Git 发布标签使用 `v` 前缀（例如 `v0.0.1`），但站点路径省略 `v`（例如 `/0.0.1/`）。这是 mike 等文档版本控制工具的标准做法。

## 审计师指南：引用哪个URL

在审计报告、合规文档或外部引用中引用 AIMO 标准时：

### 推荐的引用URL

| 用例 | 推荐URL |
|----------|-----------------|
| 当前稳定规范 | `https://standard.aimoaas.com/{X.Y.Z}/standard/current/` |
| 特定版本（用于审计） | `https://standard.aimoaas.com/{X.Y.Z}/standard/current/` |
| 治理与政策 | `https://standard.aimoaas.com/{X.Y.Z}/governance/` |
| 信任包 | `https://standard.aimoaas.com/{X.Y.Z}/governance/trust-package/` |

### 不要引用

- ~~`https://billyrise.github.io/aimo-standard/`~~ — 临时镜像，非规范
- ~~`https://standard.aimoaas.com/dev/`~~ — 开发版本，可能会更改

### 不可变性的版本化引用

对于需要不可变引用的正式审计，使用版本化快照URL：

```
https://standard.aimoaas.com/1.0.0/standard/current/01-overview/
```

版本化快照在发布时冻结，不会更改。

!!! note "URL 格式"
    站点路径使用不带 `v` 前缀的版本号。对于版本 `v1.0.0`，在URL中使用 `/1.0.0/`。

## 技术实现

### 生成的HTML示例

每个生成的HTML页面在 `<head>` 中包含规范和 hreflang 标签：

```html
<!-- 规范（始终指向生产） -->
<link rel="canonical" href="https://standard.aimoaas.com/{X.Y.Z}/governance/">

<!-- 语言备选 -->
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

### 站点地图

站点地图由 `mkdocs-static-i18n` 插件生成，包括：

- 所有生产URL
- 每种语言的 `hreflang` 备选

## Noindex 配置

### `/dev/`（预览）— 强制 Noindex

`/dev/` 版本包含未发布的内容，必须有 noindex 以防止：

- 搜索引擎索引不稳定内容
- 用户通过搜索找到 `/dev/` 并在审计中引用
- 已发布和未发布内容之间的混淆

**实现：**

`deploy-dev.yml` 工作流通过主题覆盖将 noindex 元标签注入所有 `/dev/` 页面：

```html
<!-- 仅注入到 /dev/ 页面 -->
<meta name="robots" content="noindex, nofollow">
```

### GitHub Pages 镜像 — Noindex

部署到 GitHub Pages（`billyrise.github.io` 的镜像站点）时，所有页面应有 noindex 以防止重复索引：

```html
<meta name="robots" content="noindex, nofollow">
```

这确保搜索引擎始终优先考虑 `standard.aimoaas.com` 上的生产规范URL。

## 验证

每次构建后，您可以通过以下方式验证规范URL：

1. **检查生成的HTML** — 在 `mkdocs build` 后检查 `site/` 目录
2. **使用浏览器开发者工具** — 检查已部署页面的 `<head>` 部分
3. **Google Search Console** — 监控哪些URL被索引

示例验证命令：

```bash
mkdocs build
grep -r 'rel="canonical"' site/ | head -5
```

预期输出应显示生产URL，例如：

```
site/index.html:<link rel="canonical" href="https://standard.aimoaas.com/">
site/governance/index.html:<link rel="canonical" href="https://standard.aimoaas.com/governance/">
```

## 相关文档

- [信任包](../trust-package/) — 审计师就绪材料
- [发布](../../releases/) — 版本历史和变更日志
- [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) — 版本政策
