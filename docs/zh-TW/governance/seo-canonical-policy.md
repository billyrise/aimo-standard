---
description: AIMO SEO 和規範 URL 政策 - 搜尋引擎、稽核員和外部參照的 URL 規範化策略。
---

# SEO 與規範政策

本頁記錄 AIMO 標準如何為搜尋引擎、稽核員和外部參照管理 URL 規範化。

## 生產環境與鏡像網站

| 環境 | URL | 角色 | 可索引 |
|-------------|-----|------|-----------|
| **生產環境** | `https://standard.aimoaas.com/` | 所有用途的規範網站 | 是 |
| GitHub Pages | `https://billyrise.github.io/aimo-standard/` | 臨時鏡像 / CI 預覽 | 否（noindex） |

**主要原則**：生產環境（`standard.aimoaas.com`）是權威 URL。GitHub Pages 作為臨時備份/鏡像，不應在稽核報告或外部參照中引用。

## 規範 URL 策略

### 規範 URL 如何產生

AIMO 標準使用 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)，配置如下：

```yaml
# mkdocs.yml
site_url: https://standard.aimoaas.com/
```

此 `site_url` 設定確保：

1. **`<link rel="canonical">`** — 每個產生的 HTML 頁面包含指向生產環境 URL 的規範連結。
2. **`sitemap.xml`** — sitemap 中的所有 URL 參照生產環境。
3. **`robots.txt`** — Sitemap 參照指向生產環境。
4. **`hreflang` 替代版本** — 語言替代版本使用生產環境 URL。

### 特定語言的規範

| 語言 | URL 模式 | 範例 |
|----------|-------------|---------|
| 英文（預設） | `https://standard.aimoaas.com/{path}` | `https://standard.aimoaas.com/governance/` |
| 日文 | `https://standard.aimoaas.com/ja/{path}` | `https://standard.aimoaas.com/ja/governance/` |

每個語言版本都是自我規範的，並包含指向其他語言的 `hreflang` 替代版本，加上指向英文版本的 `x-default`。

### 版本化文件和規範

AIMO 標準使用 [mike](https://github.com/jimporter/mike) 進行文件版本控制，使用 `alias_type: redirect`：

| 版本 | URL 模式 | 規範狀態 | 可索引 |
|---------|-------------|------------------|-----------|
| 版本化（例如 `0.0.1`） | `https://standard.aimoaas.com/0.0.1/` | 該特定版本的規範 | 是 |
| `latest`（別名） | `https://standard.aimoaas.com/latest/` | **重新導向**到目前發布 | 是（透過目標） |
| `dev` | `https://standard.aimoaas.com/dev/` | 僅預覽 | **否**（強制 noindex） |

**關鍵區別：**

| 面向 | `/X.Y.Z/` | `/latest/` | `/dev/` |
|--------|-----------|------------|---------|
| 內容 | 凍結快照 | 重新導向到 `/X.Y.Z/` | 主分支預覽 |
| 可變 | 從不 | 發布時更新指標 | 持續 |
| 用於稽核 | **是（首選）** | 是（解析到凍結版本） | **從不** |
| SEO | 已索引 | 透過目標索引 | noindex |

**alias_type: redirect 的運作方式：**

不是複製檔案，`/latest/` 包含指向目前發布的重新導向頁面：

```html
<!-- /latest/index.html -->
<meta http-equiv="refresh" content="0; url=../0.0.1/">
<link rel="canonical" href="https://standard.aimoaas.com/0.0.1/">
```

這確保：

1. **無內容漂移** — `/latest/` 無法與其指向的發布版本分歧。
2. **無重複內容** — 搜尋引擎看到一個規範來源。
3. **原子更新** — 變更別名會一次更新所有頁面。

!!! info "Git 標籤與網站路徑"
    Git 發布標籤使用 `v` 前綴（例如 `v0.0.1`），但網站路徑省略 `v`（例如 `/0.0.1/`）。這是 mike 等文件版本控制工具的標準做法。

## 稽核員指引：引用哪個 URL

在稽核報告、合規文件或外部參照中引用 AIMO 標準時：

### 建議引用 URL

| 使用案例 | 建議 URL |
|----------|-----------------|
| 目前穩定規格 | `https://standard.aimoaas.com/latest/standard/current/` |
| 特定版本（用於稽核） | `https://standard.aimoaas.com/{X.Y.Z}/standard/current/` |
| 治理與政策 | `https://standard.aimoaas.com/latest/governance/` |
| 信任套件 | `https://standard.aimoaas.com/latest/governance/trust-package/` |

### 請勿引用

- ~~`https://billyrise.github.io/aimo-standard/`~~ — 臨時鏡像，非規範
- ~~`https://standard.aimoaas.com/dev/`~~ — 開發版本，可能變更

### 不可變性的版本化引用

對於需要不可變參照的正式稽核，使用版本化快照 URL：

```
https://standard.aimoaas.com/1.0.0/standard/current/01-overview/
```

版本化快照在發布時凍結，不會變更。

!!! note "URL 格式"
    網站路徑使用不帶 `v` 前綴的版本號。對於版本 `v1.0.0`，在 URL 中使用 `/1.0.0/`。

## 技術實作

### 產生的 HTML 範例

每個產生的 HTML 頁面在 `<head>` 中包含規範和 hreflang 標籤：

```html
<!-- 規範（始終指向生產環境） -->
<link rel="canonical" href="https://standard.aimoaas.com/latest/governance/">

<!-- 語言替代版本 -->
<link rel="alternate" hreflang="en" href="https://standard.aimoaas.com/latest/governance/">
<link rel="alternate" hreflang="ja" href="https://standard.aimoaas.com/latest/ja/governance/">
<link rel="alternate" hreflang="x-default" href="https://standard.aimoaas.com/latest/governance/">
```

### robots.txt

```
User-agent: *
Allow: /

Sitemap: https://standard.aimoaas.com/sitemap.xml
```

### Sitemap

sitemap 由 `mkdocs-static-i18n` 外掛程式產生，包含：

- 所有生產環境 URL
- 每種語言的 `hreflang` 替代版本

## Noindex 配置

### `/dev/`（預覽）— 強制 Noindex

`/dev/` 版本包含未發布的內容，必須有 noindex 以防止：

- 搜尋引擎索引不穩定的內容
- 使用者透過搜尋找到 `/dev/` 並在稽核中引用它
- 已發布和未發布內容之間的混淆

**實作：**

`deploy-dev.yml` 工作流程透過主題覆蓋將 noindex meta 標籤注入所有 `/dev/` 頁面：

```html
<!-- 僅注入到 /dev/ 頁面 -->
<meta name="robots" content="noindex, nofollow">
```

### GitHub Pages 鏡像 — Noindex

部署到 GitHub Pages（`billyrise.github.io` 的鏡像網站）時，所有頁面應有 noindex 以防止重複索引：

```html
<meta name="robots" content="noindex, nofollow">
```

這確保搜尋引擎始終優先考慮 `standard.aimoaas.com` 的生產環境規範 URL。

## 驗證

每次建置後，您可以透過以下方式驗證規範 URL：

1. **檢查產生的 HTML** — 在 `mkdocs build` 後檢查 `site/` 目錄
2. **使用瀏覽器 DevTools** — 在部署的頁面上檢查 `<head>` 區段
3. **Google Search Console** — 監控哪些 URL 被索引

範例驗證命令：

```bash
mkdocs build
grep -r 'rel="canonical"' site/ | head -5
```

預期輸出應顯示生產環境 URL，例如：

```
site/index.html:<link rel="canonical" href="https://standard.aimoaas.com/">
site/governance/index.html:<link rel="canonical" href="https://standard.aimoaas.com/governance/">
```

## 相關文件

- [信任套件](trust-package.md) — 稽核員就緒材料
- [發布](../releases/index.md) — 版本歷史和變更日誌
- [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) — 版本政策
