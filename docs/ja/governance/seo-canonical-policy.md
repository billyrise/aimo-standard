# SEO & Canonical ポリシー

このページでは、AIMO Standardが検索エンジン、監査人、外部参照に対してどのようにURL正規化を管理しているかを説明します。

## 本番サイト vs ミラーサイト

| 環境 | URL | 役割 | インデックス可 |
|------|-----|------|----------------|
| **本番（Production）** | `https://standard.aimoaas.com/` | 正規サイト（すべての目的で使用） | はい |
| GitHub Pages | `https://billyrise.github.io/aimo-standard/` | 一時的なミラー / CIプレビュー | いいえ (noindex) |

**基本原則**: 本番サイト（`standard.aimoaas.com`）が正規URLです。GitHub Pagesは一時的なバックアップ/ミラーとして機能し、監査レポートや外部参照で引用すべきではありません。

## Canonical URL 戦略

### Canonical URL の生成方法

AIMO Standardは[MkDocs Material](https://squidfunk.github.io/mkdocs-material/)を使用し、以下の設定で運用しています：

```yaml
# mkdocs.yml
site_url: https://standard.aimoaas.com/
```

この`site_url`設定により：

1. **`<link rel="canonical">`** — 生成される各HTMLページに本番URLを指すcanonicalリンクが含まれます。
2. **`sitemap.xml`** — サイトマップ内のすべてのURLが本番を参照します。
3. **`robots.txt`** — サイトマップ参照が本番を指します。
4. **`hreflang` alternates** — 言語代替が本番URLを使用します。

### 言語別の Canonical URL

| 言語 | URLパターン | 例 |
|------|-------------|-----|
| 英語（デフォルト） | `https://standard.aimoaas.com/{path}` | `https://standard.aimoaas.com/governance/` |
| 日本語 | `https://standard.aimoaas.com/ja/{path}` | `https://standard.aimoaas.com/ja/governance/` |

各言語バージョンは自己参照のcanonicalを持ち、他の言語への`hreflang`代替と、英語版を指す`x-default`を含みます。

### バージョン管理とCanonical

AIMO Standardはドキュメントのバージョン管理に[mike](https://github.com/jimporter/mike)を使用しています：

| バージョン | URLパターン | Canonical状態 |
|-----------|-------------|---------------|
| `latest`（エイリアス） | `https://standard.aimoaas.com/latest/` | 現行安定版の正規 |
| `dev` | `https://standard.aimoaas.com/dev/` | 開発版の正規（noindex推奨） |
| バージョン指定（例：`1.0.0`） | `https://standard.aimoaas.com/1.0.0/` | 特定バージョンの正規 |

**重要事項：**

- `latest`は最新の安定リリースを指すエイリアスです。
- `dev`は`main`ブランチを反映し、変更される可能性があります。正式な監査では引用を避けてください。
- バージョン指定スナップショットは不変であり、監査引用に安全です。

!!! info "Git タグ vs. サイトパス"
    Git リリースタグは `v` プレフィックスを使用します（例：`v0.1.6`）が、サイトパスでは `v` を省略します（例：`/0.1.6/`）。これは mike などのドキュメントバージョン管理ツールの標準的な方法です。

## 監査人ガイダンス：引用すべきURL

監査レポート、コンプライアンス文書、または外部参照でAIMO Standardを引用する際：

### 推奨される引用URL

| ユースケース | 推奨URL |
|--------------|---------|
| 現行安定版仕様 | `https://standard.aimoaas.com/latest/standard/current/` |
| 特定バージョン（監査用） | `https://standard.aimoaas.com/{X.Y.Z}/standard/current/` |
| ガバナンス & ポリシー | `https://standard.aimoaas.com/latest/governance/` |
| Trust Package | `https://standard.aimoaas.com/latest/governance/trust-package/` |

### 引用すべきでないURL

- ~~`https://billyrise.github.io/aimo-standard/`~~ — 一時的なミラー、正規ではない
- ~~`https://standard.aimoaas.com/dev/`~~ — 開発版、変更される可能性あり

### 不変性のためのバージョン指定引用

不変の参照が必要な正式監査では、バージョン指定スナップショットURLを使用してください：

```
https://standard.aimoaas.com/1.0.0/standard/current/01-overview/
```

バージョン指定スナップショットはリリース時点で凍結され、変更されません。

!!! note "URLフォーマット"
    サイトパスでは `v` プレフィックスを省略します。バージョン `v1.0.0` の場合、URLでは `/1.0.0/` を使用します。

## 技術的実装

### 生成されるHTMLの例

生成される各HTMLページの`<head>`には、canonicalとhreflangタグが含まれます：

```html
<!-- Canonical（常に本番を指す） -->
<link rel="canonical" href="https://standard.aimoaas.com/latest/governance/">

<!-- 言語代替 -->
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

### サイトマップ

サイトマップは`mkdocs-static-i18n`プラグインによって生成され、以下を含みます：

- すべての本番URL
- 各言語の`hreflang`代替

## GitHub Pages の noindex 設定

GitHub Pages（ミラーサイト）へのデプロイ時、デプロイワークフローは検索エンジンがミラーをインデックスしないように`noindex`メタタグを追加する必要があります：

```html
<meta name="robots" content="noindex, nofollow">
```

これにより、検索エンジンは常に本番のcanonical URLを優先します。

## 検証方法

各ビルド後、以下の方法でcanonical URLを検証できます：

1. **生成されたHTMLの確認** — `mkdocs build`後に`site/`ディレクトリをチェック
2. **ブラウザDevToolsの使用** — デプロイされたページの`<head>`セクションを検査
3. **Google Search Console** — どのURLがインデックスされているかを監視

検証コマンドの例：

```bash
mkdocs build
grep -r 'rel="canonical"' site/ | head -5
```

期待される出力は本番URLを表示します。例：

```
site/index.html:<link rel="canonical" href="https://standard.aimoaas.com/">
site/governance/index.html:<link rel="canonical" href="https://standard.aimoaas.com/governance/">
```

## 関連ドキュメント

- [Trust Package](trust-package.md) — 監査対応資料
- [Releases](../releases/index.md) — バージョン履歴と変更履歴
- [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) — バージョンポリシー
