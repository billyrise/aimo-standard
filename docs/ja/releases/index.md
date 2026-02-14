---
description: AIMO Standardリリース - バージョン別PDF、アーティファクト、チェックサムのダウンロード。変更履歴、移行ガイド、ビルド来歴証明書。
---

# リリース（Releases）

本セクションは、バージョン付きリリース、changelog、移行、配布アーティファクトのハブです。

## 最新リリースのダウンロード

**[GitHub Releases](https://github.com/billyrise/aimo-standard/releases/latest)** — これが「latest」リリースの単一の真実の情報源です。サイトの `/latest/` は同じバージョンへリダイレクトします。

## 検証手順（恒久ページ）

監査人向けの**検証手順**（資産のダウンロード、チェックサム検証、ビルド来歴証明）は PDF に限定されず、恒久の Web ページでも参照できます。

- **[Standard → Versions → 検証手順](../standard/versions/)** — Linux/macOS/Windows でのステップごとのチェックサム検証とビルド来歴証明

監査成果物で検証手順を記載する際はこのページを参照してください。

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

=== "Linux"

    ```bash
    # チェックサムファイルをダウンロード
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # 特定のファイルを検証
    sha256sum -c SHA256SUMS.txt --ignore-missing

    # または手動で検証：
    sha256sum trust_package.pdf
    # 出力を SHA256SUMS.txt と比較
    ```

=== "macOS"

    ```bash
    # チェックサムファイルをダウンロード
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # 特定のファイルを検証
    shasum -a 256 -c SHA256SUMS.txt

    # または手動で検証：
    shasum -a 256 trust_package.pdf
    # 出力を SHA256SUMS.txt と比較
    ```

=== "Windows (PowerShell)"

    ```powershell
    # チェックサムファイルをダウンロード
    Invoke-WebRequest -Uri "https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt" -OutFile SHA256SUMS.txt

    # 特定のファイルを検証
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # Hash 出力を SHA256SUMS.txt と比較
    Get-Content .\SHA256SUMS.txt
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

- **バージョン履歴テーブル**: [Standard > Versions](../standard/versions/) — 全リリースアセット（PDF、ZIP、SHA256）への直接リンク付きバージョンテーブル
- **Changelog（仕様）**: [Standard > Current > Changelog](../standard/current/08-changelog/) — 規範・非規範の変更履歴。
- **リリースプロセス**: タグ `vX.Y.Z`、CI ビルド、`dist/` 下の PDF、チェックサム、GitHub Release アセット。リポジトリの [GOVERNANCE.md](https://github.com/billyrise/aimo-standard/blob/main/GOVERNANCE.md) および [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) を参照。
- **移行ガイド**: [MIGRATION.md](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) — 破壊的変更のアップグレードパス。

ガバナンスとバージョニングポリシーは [Governance](../governance/) を参照。

## 提出パッケージの準備

監査提出用の証跡を準備する際：

1. **Evidence Bundle の作成**: [Evidence Bundle](../artifacts/evidence-bundle/) と [Minimum Evidence Requirements](../artifacts/minimum-evidence/) に従い、EV レコード、Dictionary、Summary、Change Log を作成する。
2. **Validator の実行**: `python validator/src/validate.py bundle/root.json` を実行して構造整合性を確認する。エラーはすべて修正する。
3. **チェックサムの生成**: 検証用の SHA-256 チェックサムを作成する：

    === "Linux"

        ```bash
        sha256sum *.json *.pdf > SHA256SUMS.txt
        ```

    === "macOS"

        ```bash
        shasum -a 256 *.json *.pdf > SHA256SUMS.txt
        ```

    === "Windows (PowerShell)"

        ```powershell
        Get-ChildItem *.json, *.pdf | ForEach-Object {
            $hash = (Get-FileHash $_.FullName -Algorithm SHA256).Hash.ToLower()
            "$hash  $($_.Name)"
        } | Out-File SHA256SUMS.txt -Encoding UTF8
        ```
4. **パッケージ化**: バンドルディレクトリの zip アーカイブを作成する。
5. **バージョン整合の記録**: 証跡が整合する AIMO Standard リリース（例：`v1.0.0`）を記録する。
6. **提出**: パッケージ、チェックサム、バージョン参照を監査人に提供する。

完全な準備ガイドは [Trust Package](../governance/trust-package/) を参照。

## 監査人向け：検証手順

証跡提出物を受領した監査人は、完全性と構造を検証すべきである：

1. **チェックサム検証**: チェックサム検証（Linux: `sha256sum -c`、macOS: `shasum -a 256 -c`、Windows: `Get-FileHash`）を実行してファイルの完全性を確認
2. **バリデータ実行**: `python validator/src/validate.py bundle/root.json` を実行して構造を確認
3. **バージョン確認**: 記載された AIMO Standard バージョンが [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) に存在することを確認

!!! tip "ツールを独立に取得"
    監査人はバリデータとスキーマを、提出者からではなく、公式 AIMO Standard リリースから直接ダウンロードすべきである。

完全な検証手順（チェックサム、証明、ステップごと）は **[Standard → Versions → 検証手順](../standard/versions/)** を参照。監査対応資料は [Trust Package](../governance/trust-package/) も参照。

## 非過剰主張ステートメント

!!! warning "重要"
    AIMO Standard は**説明可能性と証跡準備**を支援する。法的助言の提供、適合の保証、いかなる規制・フレームワークへの適合認証も**行わない**。採用者は権威ある条文と照合し、適切に専門家の助言を得ること。

スコープ、前提条件、採用者責任は [責任境界](../governance/responsibility-boundary/) を参照。
