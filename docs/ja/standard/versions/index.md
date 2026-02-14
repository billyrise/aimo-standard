---
description: AIMO Standardバージョン履歴。監査対応PDF、機械可読アーティファクト、チェックサム、ビルド来歴証明書付き公式凍結リリース。
---

# バージョン一覧

公式リリースは固定されたスナップショットとして、監査対応PDFおよび機械可読アーティファクトとともに公開されます。

## 最新リリース

!!! success "現在のバージョン"
    **v0.1.2** (2026-02-13) — [ドキュメントを見る](../current/index.md) | [GitHub Release](https://github.com/billyrise/aimo-standard/releases/tag/v0.1.2)

## バージョン履歴

| バージョン | 日付 | リリースノート | PDF (EN) | PDF (JA) | アーティファクト | チェックサム |
| :--------- | :--- | :------------- | :------- | :------- | :--------------- | :----------- |
| **v0.1.2** | 2026-02-13 | [Changelog](../current/08-changelog.md#version-012) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.2/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.2/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.1.2/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.1.2/SHA256SUMS.txt) |
| **v0.1.1** | 2026-02-04 | [Changelog](../current/08-changelog.md#version-011) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.1/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.1/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.1.1/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.1.1/SHA256SUMS.txt) |
| **v0.1.0** | 2026-02-03 | [Changelog](../current/08-changelog.md#version-010) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.0/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.0/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.1.0/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.1.0/SHA256SUMS.txt) |
| **v0.0.3** | 2026-02-02 | [Changelog](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.3/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.3/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.3/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.3/SHA256SUMS.txt) |
| **v0.0.2** | 2026-02-02 | [Changelog](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/SHA256SUMS.txt) |
| **v0.0.1** | 2026-02-02 | [Changelog](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/SHA256SUMS.txt) |

!!! note "データソース"
    このバージョンテーブルは [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) と同期しています。各リリースタグ（`vX.Y.Z`）は仕様の固定スナップショットに対応します。

## /latest とバージョン付き URL — 誤引用を防ぐ

| URL | 用途 | 監査・証跡 |
|-----|------|------------|
| **`/X.Y.Z/`**（例：`/0.1.1/`） | 固定スナップショット；変更されない。 | 監査引用・再現可能な証跡には**必須**で使用。 |
| **`/latest/`** | 現行リリースへのリダイレクト；新タグリリース時に更新。 | 参照用；監査証跡としては**非推奨**（指し先が変わるため）。 |

**「latest」の正式な定義**は [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) の **latest** タグです。サイトの `/latest/` はそのリリースへリダイレクトします。**リリースワークフロー**（タグ push で起動）のみが `/latest/` を更新します。詳細は [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) を参照してください。

| ソース | 役割 |
|--------|------|
| **GitHub Release の latest タグ** | SSOT — 「現行リリース」の唯一の定義 |
| **バージョンテーブル**（本ページ） | リリースワークフローでリリースと同期。デプロイ前にタグと一致している必要あり |
| **Changelog** | 規範的な変更履歴。リリースノートが参照 |
| **サイトの `/latest/`** | GitHub Release の latest と同じバージョンへリダイレクト |

リリース手順の詳細は [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) および [release ワークフロー](https://github.com/billyrise/aimo-standard/blob/main/.github/workflows/release.yml) を参照してください。バージョンテーブルと Changelog はリリース準備の一環で更新され、デプロイ済みバージョンと常に一致します。

## 法的・商標に関する注意

商標の帰属・使用（「AIMO」が第三者の登録商標であること、RISEby が商標出願しているのは AIMOaaS のみであることを含む）は [Governance → 商標](../../governance/trademarks.md) およびリポジトリの [TRADEMARKS.md](https://github.com/billyrise/aimo-standard/blob/main/TRADEMARKS.md) に記載しています。最新の商標・法的注意は、最新リリースのドキュメントまたは上記 TRADEMARKS.md を参照してください。

## 監査人向け：正規 URL とバージョン固定

監査報告書で特定バージョンを引用し、再現性を確保するには：

1. **正規 URL**：そのバージョンの固定ドキュメント URL を使用（例：`https://standard.aimoaas.com/0.1.1/`。使用したバージョンで `0.0.3` を置き換え）。**v0.1.1 以降**：監査証跡では `/latest/` よりバージョン付き URL（例：`https://standard.aimoaas.com/0.1.1/`）の引用を推奨し、スナップショットの曖昧さを避けてください。
2. **バージョン固定**：[GitHub Release](https://github.com/billyrise/aimo-standard/releases) ページの**リリースタグ**（例：`v0.1.1`）および任意で**コミットハッシュ**を記録。これにより、仕様スナップショットがリリース資産（PDF、ZIP、チェックサム）と一致することを独立に検証できます。
3. **エビデンスの整合**：提出物に、準拠した AIMO Standard のバージョン（例：`v0.1.1`）を明記し、バリデータとスキーマは同一リリースから取得してください。

## バージョン層

AIMO Standard では三つのバージョン概念を使用します。現行リリースでは一致していますが、将来のリリースでは独立してバージョン管理する場合があります。

| 層 | 説明 | 記載箇所 |
|----|------|----------|
| **Standard バージョン**（サイト/リリース） | リリースタグとドキュメントスナップショット（例：`v0.1.1`）。 | バージョンテーブル、GitHub Releases、`/X.Y.Z/` URL。 |
| **Taxonomy スキーマバージョン** | コード体系と taxonomy/スキーマ定義のバージョン。 | マニフェストの `taxonomy_version`；スキーマの `$id` またはドキュメント。 |
| **Dictionary コンテンツバージョン** | 辞書エントリ（コードと定義）のバージョン。 | 辞書メタデータ；0.0.x では taxonomy と同じ。 |

「AIMO Standard vX.Y.Z」を引用する場合、**Standard バージョン**が正規スナップショットを定義します。Validator と Minimum Evidence Requirements は、そのリリースのアーティファクトとスキーマを参照します。

## 検証手順

監査人および実装者は、SHA-256 チェックサムを使用してダウンロードの整合性を検証すべきです。

### 1. リリースアセットのダウンロード

=== "Linux / macOS"

    ```bash
    # 特定バージョンの全アセットをダウンロード
    VERSION=v0.1.2
    BASE_URL="https://github.com/billyrise/aimo-standard/releases/download/${VERSION}"

    curl -LO "${BASE_URL}/trust_package.pdf"
    curl -LO "${BASE_URL}/trust_package.ja.pdf"
    curl -LO "${BASE_URL}/aimo-standard-artifacts.zip"
    curl -LO "${BASE_URL}/SHA256SUMS.txt"
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 特定バージョンの全アセットをダウンロード
    $VERSION = "v0.1.1"
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
VERSION=v0.1.2
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

**運用規約**（URL の意味と MUST ルール）は [バージョニング・参照方針](../current/00-versioning-reference-policy.md) を参照。完全なバージョニングポリシーは [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) を参照してください。

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

- 本番環境: `https://standard.aimoaas.com/{version}/`（例: `/0.1.1/`）
- GitHub Pages: `https://billyrise.github.io/aimo-standard/{version}/`

### URL タイプとその意味

| URLパターン | 説明 | 監査引用に使用可能？ |
|-------------|------|---------------------|
| `/X.Y.Z/`（例: `/0.1.1/`） | **固定リリース** — 不変のスナップショット | **はい**（推奨） |
| `/latest/` | **エイリアス** — 最新リリースへリダイレクト | はい（`/X.Y.Z/`に解決） |
| `/dev/` | **プレビュー** — 未リリースのmainブランチ内容 | **いいえ**（引用不可） |

!!! warning "`/latest/` と `/dev/` の違いについて"
    - **`/latest/`** は最新の**リリース済み**バージョンへのエイリアス（リダイレクト）です。固定スナップショットに解決されるため、引用に安全です。
    - **`/dev/`** は現在の `main` ブランチを反映しており、**未リリースの変更**が含まれている可能性があります。監査レポートでは `/dev/` を絶対に引用しないでください。

### よくある質問

??? question "`/latest/` がバージョン番号でないのはなぜですか？"
    `/latest/` は最新の安定リリース（例: `/0.1.1/`）に常にリダイレクトする便利なエイリアスです。これにより、ユーザーは単一のURLをブックマークしながら、自動的に現行バージョンを取得できます。不変性が必要な正式監査では、代わりに明示的なバージョンURLを引用してください。

??? question "監査人はどのURLを引用すべきですか？"
    - **正式監査（不変性が必要）**: `/X.Y.Z/` を使用（例: `https://standard.aimoaas.com/0.1.1/standard/current/`）
    - **一般的な参照**: `/latest/` は現行リリースにリダイレクトされるため許容可能
    - **絶対に引用しないでください**: `/dev/`（未リリース、変更される可能性あり）

??? question "`/latest/` が期待と異なる内容を表示した場合は？"
    これはデプロイメントのバグです。`/latest/` が最新の [GitHub Release](https://github.com/billyrise/aimo-standard/releases) と異なると思われる場合は、[Issue を報告](https://github.com/billyrise/aimo-standard/issues)してください。`/latest/` エイリアスは常に最新のタグ付きリリースにリダイレクトされるべきです。

## リソース

- **[リリースハブ](../../../releases/)** — 提出準備、監査人による検証、非過剰主張ステートメント
- **[Trust Package](../../governance/trust-package.md)** — 監査対応保証資料
- **[Changelog（詳細）](../current/08-changelog.md)** — 廃止追跡を含む完全な変更履歴
- **[VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)** — 完全なバージョニングポリシー
