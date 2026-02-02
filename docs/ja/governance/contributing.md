---
description: AIMO Standardコントリビュートガイド - コード、ドキュメント、翻訳の貢献方法。Issue・PRガイドライン。
---

# コントリビュート

本ページでは、AIMO Standard へのコントリビュートガイドラインを提供する。

## クイックスタート

1. リポジトリをフォーク
2. フィーチャーブランチを作成
3. 以下のガイドラインに従って変更
4. 品質チェックを実行
5. プルリクエストを提出

## 主要原則

| 原則 | 説明 |
| ---- | ---- |
| 英語が正 | まず `docs/en/` を編集し、その後 `docs/ja/` を更新 |
| SSOT | このリポジトリが唯一の情報源 |
| 生成ファイルを手動編集しない | ソースを編集、再生成、コミット |
| すべての変更は PR 経由 | メンテナも PR を使用 |

## 品質チェック

PR 提出前に実行：

```bash
# 仮想環境を有効化
source .venv/bin/activate

# lint 実行
python tooling/checks/lint_i18n.py
python tooling/checks/lint_schema.py
python tooling/audit/baseline_audit.py --check

# ドキュメントビルド
mkdocs build --strict
```

## 変更の種類

| 種類 | 例 | レビュー要件 |
| ---- | -- | ------------ |
| 規範的 | スキーマ変更、要件 | メンテナ＋議論 |
| 非規範的 | 誤字修正、明確化 | メンテナ承認 |
| i18n | 翻訳 | 構造が EN と一致 |
| ツール | CI/CD、スクリプト | メンテナ承認 |

## i18n ガイドライン

### 更新順序

1. 英語ソースを編集（`docs/en/...`）
2. 日本語翻訳を更新（`docs/ja/...`）
3. `lint_i18n.py` で整合性を確認
4. 両方を一緒にコミット

### 構造要件

- 両言語で同じファイル名
- 同じ見出し階層
- セクションごとに同じページ数

## PR チェックリスト

PR 提出時に確認：

- [ ] 変更の種類を特定（docs / schema / examples / tooling）
- [ ] 破壊的変更の評価を完了
- [ ] i18n: EN と JA を一緒に更新（該当する場合）
- [ ] 品質チェック合格
- [ ] 関連 issue をリンク

## 破壊的変更

破壊的変更には以下が必要：

1. 実装前に issue で議論
2. [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) に従いバージョンアップ
3. 移行ガイダンス付きの変更履歴エントリ

## 適合性主張の更新

適合性主張を追加・変更するには：

1. カバレッジマップ YAML を更新
2. 対応するドキュメントページを更新
3. バリデータテストを実行
4. マッピング根拠を文書化

## 完全なガイドライン

ルートレベルのガイドは [CONTRIBUTING.md](https://github.com/billyrise/aimo-standard/blob/main/CONTRIBUTING.md) を参照。

## 関連ページ

- [ガバナンス](index.md) — プロジェクトガバナンス
- [ローカライゼーションガイド](../contributing/localization.md) — i18n 詳細
- [責任境界](responsibility-boundary.md) — AIMO が提供するもの
