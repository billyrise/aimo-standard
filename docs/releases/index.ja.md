# リリース（Releases）

本セクションは、バージョン付きリリース、changelog、移行、配布アーティファクトのハブです。

## 最新リリースのダウンロード

**[GitHub Releases](https://github.com/billyrise/aimo-standard/releases/latest)**

## リリースアセット

各公式リリース（`vX.Y.Z` タグ）には以下が含まれます：

| アセット | 説明 |
| --- | --- |
| `trust_package.pdf` | 英語版 Trust Package — 監査対応の保証資料 |
| `trust_package.ja.pdf` | 日本語版 Trust Package |
| `aimo-standard-artifacts.zip` | スキーマ、テンプレート、サンプル、バリデータルール |
| `SHA256SUMS.txt` | 全アセットの SHA-256 チェックサム |

### ダウンロードの検証

ダウンロード後、チェックサムでファイルの整合性を検証できます：

```bash
# チェックサムファイルをダウンロード
curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

# 特定のファイルを検証
sha256sum -c SHA256SUMS.txt --ignore-missing
```

または手動で：

```bash
sha256sum trust_package.pdf
# 出力を SHA256SUMS.txt と比較
```

## Artifacts Zip の内容

`aimo-standard-artifacts.zip` には以下が含まれます：

- `schemas/jsonschema/*` — 検証用 JSON スキーマ
- `templates/ev/*` — エビデンステンプレート（JSON + Markdown）
- `examples/*` — サンプルエビデンスバンドル
- `coverage_map/coverage_map.yaml` — 外部標準へのマッピング
- `validator/rules/*` — 検証ルール定義
- `VERSIONING.md`、`GOVERNANCE.md`、`SECURITY.md` など

## リソース

- **Changelog（仕様）**: [Standard > Current > Changelog](../standard/current/08-changelog.md) — 規範・非規範の変更履歴。
- **バージョンスナップショット**: [Standard > Versions](../standard/versions/index.md) — 固定リリースと過去版。
- **リリースプロセス**: タグ `vX.Y.Z`、CI ビルド、`dist/` 下の PDF、チェックサム、GitHub Release アセット。リポジトリの [GOVERNANCE.md](https://github.com/billyrise/aimo-standard/blob/main/GOVERNANCE.md) および [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) を参照。
- **移行とチェックサム**: リリースごとに文書化。破壊的変更には移行ガイドが必要。

ガバナンスとバージョニングポリシーは [Governance](../governance/index.md) を参照。
