---
description: AIMO Standardバージョン履歴。監査対応PDF、機械可読アーティファクト、チェックサム、ビルド来歴証明書付き公式凍結リリース。
---

# バージョン一覧

公式リリースは固定されたスナップショットとして、監査対応PDFおよび機械可読アーティファクトとともに公開されます。

## 最新リリース

!!! success "現在のバージョン"
    **v0.0.3** (2026-02-02) — [ドキュメントを見る](../current/index.md) | [GitHub Release](https://github.com/billyrise/aimo-standard/releases/tag/v0.0.3)

## バージョン履歴

| バージョン | 日付 | リリースノート | PDF (EN) | PDF (JA) | アーティファクト | チェックサム |
| :--------- | :--- | :------------- | :------- | :------- | :--------------- | :----------- |
| **v0.0.3** | 2026-02-02 | [Changelog](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.3/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.3/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.3/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.3/SHA256SUMS.txt) |
| **v0.0.2** | 2026-02-02 | [Changelog](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/SHA256SUMS.txt) |
| **v0.0.1** | 2026-02-02 | [Changelog](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/SHA256SUMS.txt) |

!!! note "データソース"
    このバージョンテーブルは [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) と同期しています。各リリースタグ（`vX.Y.Z`）は仕様の固定スナップショットに対応します。

## 検証手順

監査人および実装者は、SHA-256 チェックサムを使用してダウンロードの整合性を検証すべきです。

### 1. リリースアセットのダウンロード

=== "Linux / macOS"

    ```bash
    # 特定バージョンの全アセットをダウンロード
    VERSION=v0.0.3
    BASE_URL="https://github.com/billyrise/aimo-standard/releases/download/${VERSION}"

    curl -LO "${BASE_URL}/trust_package.pdf"
    curl -LO "${BASE_URL}/trust_package.ja.pdf"
    curl -LO "${BASE_URL}/aimo-standard-artifacts.zip"
    curl -LO "${BASE_URL}/SHA256SUMS.txt"
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 特定バージョンの全アセットをダウンロード
    $VERSION = "v0.0.1"
    $BASE_URL = "https://github.com/billyrise/aimo-standard/releases/download/$VERSION"

    Invoke-WebRequest -Uri "$BASE_URL/trust_package.pdf" -OutFile trust_package.pdf
    Invoke-WebRequest -Uri "$BASE_URL/trust_package.ja.pdf" -OutFile trust_package.ja.pdf
    Invoke-WebRequest -Uri "$BASE_URL/aimo-standard-artifacts.zip" -OutFile aimo-standard-artifacts.zip
    Invoke-WebRequest -Uri "$BASE_URL/SHA256SUMS.txt" -OutFile SHA256SUMS.txt
    ```

### 2. チェックサム検証

=== "Linux"

    ```bash
    # ダウンロードした全ファイルをチェックサムで検証
    sha256sum -c SHA256SUMS.txt

    # 期待される出力（すべて "OK" と表示されるべき）:
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "macOS"

    ```bash
    # ダウンロードした全ファイルをチェックサムで検証
    shasum -a 256 -c SHA256SUMS.txt

    # 期待される出力（すべて "OK" と表示されるべき）:
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 各ファイルを検証
    Get-FileHash .\trust_package.pdf -Algorithm SHA256
    Get-FileHash .\trust_package.ja.pdf -Algorithm SHA256
    Get-FileHash .\aimo-standard-artifacts.zip -Algorithm SHA256

    # Hash 出力を SHA256SUMS.txt と比較
    Get-Content .\SHA256SUMS.txt
    ```

### 3. 手動検証（代替方法）

=== "Linux"

    ```bash
    # 特定ファイルのハッシュを計算
    sha256sum trust_package.pdf

    # 出力を SHA256SUMS.txt と比較
    cat SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # 特定ファイルのハッシュを計算
    shasum -a 256 trust_package.pdf

    # 出力を SHA256SUMS.txt と比較
    cat SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 特定ファイルのハッシュを計算
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # チェックサムファイルを表示
    Get-Content .\SHA256SUMS.txt
    ```

!!! tip "監査人向け"
    チェックサムファイルは常に公式 GitHub Release から直接取得し、提出者からは受け取らないでください。これにより独立した検証が保証されます。

### 4. ビルド来歴の検証（Attestation）

すべてのリリースアセットには GitHub Actions によって生成された暗号署名付きビルド来歴証明（attestation）が含まれています。これにより、アセットが公式リポジトリで改ざんなくビルドされたことを検証できます。

**前提条件**: [GitHub CLI](https://cli.github.com/) (`gh`) のインストール

```bash
# GitHub CLI でリリースアセットをダウンロード
VERSION=v0.0.3
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

- 本番環境: `https://standard.aimoaas.com/{version}/`（例: `/0.0.1/`）
- GitHub Pages: `https://billyrise.github.io/aimo-standard/{version}/`

### URL タイプとその意味

| URLパターン | 説明 | 監査引用に使用可能？ |
|-------------|------|---------------------|
| `/X.Y.Z/`（例: `/0.0.1/`） | **固定リリース** — 不変のスナップショット | **はい**（推奨） |
| `/latest/` | **エイリアス** — 最新リリースへリダイレクト | はい（`/X.Y.Z/`に解決） |
| `/dev/` | **プレビュー** — 未リリースのmainブランチ内容 | **いいえ**（引用不可） |

!!! warning "`/latest/` と `/dev/` の違いについて"
    - **`/latest/`** は最新の**リリース済み**バージョンへのエイリアス（リダイレクト）です。固定スナップショットに解決されるため、引用に安全です。
    - **`/dev/`** は現在の `main` ブランチを反映しており、**未リリースの変更**が含まれている可能性があります。監査レポートでは `/dev/` を絶対に引用しないでください。

### よくある質問

??? question "`/latest/` がバージョン番号でないのはなぜですか？"
    `/latest/` は最新の安定リリース（例: `/0.0.1/`）に常にリダイレクトする便利なエイリアスです。これにより、ユーザーは単一のURLをブックマークしながら、自動的に現行バージョンを取得できます。不変性が必要な正式監査では、代わりに明示的なバージョンURLを引用してください。

??? question "監査人はどのURLを引用すべきですか？"
    - **正式監査（不変性が必要）**: `/X.Y.Z/` を使用（例: `https://standard.aimoaas.com/0.0.1/standard/current/`）
    - **一般的な参照**: `/latest/` は現行リリースにリダイレクトされるため許容可能
    - **絶対に引用しないでください**: `/dev/`（未リリース、変更される可能性あり）

??? question "`/latest/` が期待と異なる内容を表示した場合は？"
    これはデプロイメントのバグです。`/latest/` が最新の [GitHub Release](https://github.com/billyrise/aimo-standard/releases) と異なると思われる場合は、[Issue を報告](https://github.com/billyrise/aimo-standard/issues)してください。`/latest/` エイリアスは常に最新のタグ付きリリースにリダイレクトされるべきです。

## リソース

- **[リリースハブ](../../releases/index.md)** — 提出準備、監査人による検証、非過剰主張ステートメント
- **[Trust Package](../../governance/trust-package.md)** — 監査対応保証資料
- **[Changelog（詳細）](../current/08-changelog.md)** — 廃止追跡を含む完全な変更履歴
- **[VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)** — 完全なバージョニングポリシー
