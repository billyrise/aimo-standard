---
description: AIMO Standard引用ガイド - 学術論文、監査報告書、提案書での引用方法。CITATION.cffとBibTeX形式。
---

# 引用方法

本ページでは、学術論文、監査報告書、提案書における AIMO Standard の引用ガイダンスを提供する。

## CITATION.cff

リポジトリには Citation File Format 標準に従った [CITATION.cff](https://github.com/billyrise/aimo-standard/blob/main/CITATION.cff) ファイルが含まれる。

GitHub はこのファイルから引用情報を自動表示する。

## 推奨引用

### 短縮形（インライン）

> AIMO Standard Contributors. (2026). AIMO Standard. https://standard.aimoaas.com/

### BibTeX

```bibtex
@software{aimo_standard,
  author = {{AIMO Standard Contributors}},
  title = {AIMO Standard},
  url = {https://standard.aimoaas.com/},
  version = {0.1.1},
  year = {2026}
}
```

### APA スタイル

> AIMO Standard Contributors. (2026). *AIMO Standard* (Version 0.1.1) [Software]. https://standard.aimoaas.com/

## バージョン固有の引用

特定バージョンを引用する場合：

> AIMO Standard Contributors. (2026). AIMO Standard v0.1.1. https://github.com/billyrise/aimo-standard/releases/tag/v0.1.1

## 監査ドキュメント

監査報告書・コンプライアンス文書向け：

| 項目 | 値 |
| ---- | -- |
| 標準名 | AIMO Standard |
| バージョン | （使用バージョンを指定、例：v0.1.1） |
| ウェブサイト | https://standard.aimoaas.com/ |
| リポジトリ | https://github.com/billyrise/aimo-standard |
| リリース | https://github.com/billyrise/aimo-standard/releases |

## URL ガイダンス

### 正規 URL

公式ドキュメントにはこれらの URL を使用：

| 用途 | URL |
| ---- | --- |
| 最新ドキュメント | https://standard.aimoaas.com/latest/ |
| 特定バージョン | https://standard.aimoaas.com/0.1.1/ |
| GitHub リリース | https://github.com/billyrise/aimo-standard/releases |

!!! note "サイトパスのフォーマット"
    サイトパスでは `v` プレフィックスを省略します。バージョン `v0.1.1` の場合、URLでは `/0.1.1/` を使用します。

### 避けるべき URL

- GitHub Pages ミラー URL（一時的）
- ブランチ固有 URL（変更される可能性）

## 関連ページ

- [Trust Package](trust-package.md) — 監査対応資料
- [ガバナンス](index.md) — プロジェクトガバナンス
- [ライセンス](license.md) — ライセンス条件
