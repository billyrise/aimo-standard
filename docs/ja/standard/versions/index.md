# バージョン一覧

公式リリースは固定されたスナップショットとして、監査対応PDFおよび機械可読アーティファクトとともに公開されます。

## 最新リリース

!!! success "現在のバージョン"
    **v0.1.6** (2026-02-01) — [ドキュメントを見る](../current/index.md) | [GitHub Release](https://github.com/billyrise/aimo-standard/releases/tag/v0.1.6)

## バージョン履歴

| バージョン | 日付 | リリースノート | PDF (EN) | PDF (JA) | アーティファクト | チェックサム |
| :--------- | :--- | :------------- | :------- | :------- | :--------------- | :----------- |
| **v0.1.6** | 2026-02-01 | [Changelog](../current/08-changelog.md#version-016) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.6/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.6/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.1.6/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.1.6/SHA256SUMS.txt) |
| **v0.1.3** | 2026-01-31 | [Changelog](../current/08-changelog.md#version-013) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.3/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.3/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.1.3/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.1.3/SHA256SUMS.txt) |
| **v0.1.2** | 2026-01-31 | [Changelog](../current/08-changelog.md#version-012) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.2/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.2/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.1.2/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.1.2/SHA256SUMS.txt) |
| **v0.1.1** | 2026-01-19 | [Changelog](../current/08-changelog.md#version-011) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.1/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.1/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.1.1/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.1.1/SHA256SUMS.txt) |
| **v0.1.0** | 2026-01-19 | [Changelog](../current/08-changelog.md#version-010) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.0/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.0/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.1.0/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.1.0/SHA256SUMS.txt) |

!!! note "データソース"
    このバージョンテーブルは [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) と同期しています。各リリースタグ（`vX.Y.Z`）は仕様の固定スナップショットに対応します。

## 検証手順

監査人および実装者は、SHA-256 チェックサムを使用してダウンロードの整合性を検証すべきです。

### 1. リリースアセットのダウンロード

```bash
# 特定バージョンの全アセットをダウンロード
VERSION=v0.1.6
BASE_URL="https://github.com/billyrise/aimo-standard/releases/download/${VERSION}"

curl -LO "${BASE_URL}/trust_package.pdf"
curl -LO "${BASE_URL}/trust_package.ja.pdf"
curl -LO "${BASE_URL}/aimo-standard-artifacts.zip"
curl -LO "${BASE_URL}/SHA256SUMS.txt"
```

### 2. チェックサム検証

```bash
# ダウンロードした全ファイルをチェックサムで検証
sha256sum -c SHA256SUMS.txt

# 期待される出力（すべて "OK" と表示されるべき）:
# trust_package.pdf: OK
# trust_package.ja.pdf: OK
# aimo-standard-artifacts.zip: OK
```

### 3. 手動検証（代替方法）

```bash
# 特定ファイルのハッシュを計算
sha256sum trust_package.pdf

# 出力を SHA256SUMS.txt と比較
cat SHA256SUMS.txt
```

!!! tip "監査人向け"
    チェックサムファイルは常に公式 GitHub Release から直接取得し、提出者からは受け取らないでください。これにより独立した検証が保証されます。

### 4. ビルド来歴の検証（Attestation）

v0.1.6以降、すべてのリリースアセットには GitHub Actions によって生成された暗号署名付きビルド来歴証明（attestation）が含まれています。これにより、アセットが公式リポジトリで改ざんなくビルドされたことを検証できます。

**前提条件**: [GitHub CLI](https://cli.github.com/) (`gh`) のインストール

```bash
# GitHub CLI でリリースアセットをダウンロード
VERSION=v0.1.6
gh release download "$VERSION" --repo billyrise/aimo-standard

# 各アセットの attestation を検証
gh attestation verify trust_package.pdf --repo billyrise/aimo-standard
gh attestation verify trust_package.ja.pdf --repo billyrise/aimo-standard
gh attestation verify aimo-standard-artifacts.zip --repo billyrise/aimo-standard
gh attestation verify SHA256SUMS.txt --repo billyrise/aimo-standard
```

**期待される出力**（成功時）:

```
Loaded digest sha256:abc123... for file trust_package.pdf
Loaded 1 attestation from GitHub API
✓ Verification succeeded!
```

**オフライン検証**（エアギャップ環境）:

```bash
# まず trusted root をダウンロード（ネットワーク接続が1回必要）
gh attestation trusted-root > trusted-root.jsonl

# その後オフラインで検証
gh attestation verify trust_package.pdf \
  --repo billyrise/aimo-standard \
  --custom-trusted-root trusted-root.jsonl
```

!!! info "attestation が証明すること"
    ビルド来歴証明は、リリースアセットが以下であることを暗号学的に証明します：

    1. GitHub Actions によってビルドされた（開発者のローカルマシンではない）
    2. 公式の `billyrise/aimo-standard` リポジトリからビルドされた
    3. リリースタグに関連付けられた正確なコミットからビルドされた
    4. ビルド完了後に改変されていない

## 互換性

AIMO Standard は [Semantic Versioning](https://semver.org/) (SemVer) に従います：

| 変更タイプ | バージョン更新 | 影響 |
| :--------- | :------------- | :--- |
| **MAJOR** | X.0.0 | 破壊的変更 — 移行が必要 |
| **MINOR** | 0.X.0 | 後方互換の追加 |
| **PATCH** | 0.0.X | 修正と明確化 |

完全なバージョニングポリシーは [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) を参照してください。

## 移行

破壊的変更を含むバージョン間のアップグレード時：

1. [Changelog](../current/08-changelog.md) で破壊的変更を確認
2. [移行ガイド](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) で具体的なアップグレードパスを確認
3. Evidence Bundle を新しいスキーマ要件に合わせて更新
4. バリデータを再実行して準拠を検証

!!! warning "破壊的変更"
    MAJOR バージョン更新では、既存の Evidence Bundle の変更が必要な場合があります。アップグレード前に必ず移行ガイドを確認してください。

## バージョン別ドキュメントスナップショット

各リリースは以下でアクセス可能な固定ドキュメントスナップショットを作成します：

- 本番環境: `https://standard.aimoaas.com/{version}/`（例: `/0.1.0/`）
- GitHub Pages: `https://billyrise.github.io/aimo-standard/{version}/`

`latest` エイリアスは常に最新リリースを指します。

## リソース

- **[リリースハブ](../../releases/index.md)** — 提出準備、監査人による検証、非過剰主張ステートメント
- **[Trust Package](../../governance/trust-package.md)** — 監査対応保証資料
- **[Changelog（詳細）](../current/08-changelog.md)** — 廃止追跡を含む完全な変更履歴
