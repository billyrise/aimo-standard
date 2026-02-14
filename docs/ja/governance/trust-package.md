---
description: AIMO Trust Package - 監査対応資料バンドル。監査人、法務、ITセキュリティがAIガバナンス採用準備を評価するための最小ドキュメント。
---

# Trust Package（保証パッケージ）

このページは、監査人、法務、ITセキュリティが採用準備を評価するために必要な最小限の資料をまとめています。
これはハブのみであり、詳細なエビデンスTOCとカバレッジテーブルはそれぞれのセクションで管理されています。

## ダウンロード

**[Trust Package PDF をダウンロード（最新リリース）](https://github.com/billyrise/aimo-standard/releases/latest)**

Trust Package PDF は監査対応資料を単一ドキュメントにまとめたものです。各 GitHub Release には以下が含まれます：

- `trust_package.pdf` — 英語版 Trust Package
- `trust_package.ja.pdf` — 日本語版 Trust Package
- `aimo-standard-artifacts.zip` — スキーマ、テンプレート、サンプル、バリデータルール
- `SHA256SUMS.txt` — 検証用チェックサム

## 含まれるもの

- **適合性**: コンプライアンスの主張方法とレベルの意味 — [Conformance](../../conformance/)
- **カバレッジマップ**: 外部標準へのマッピング — [カバレッジマップ索引](../../coverage-map/)、[カバレッジマップ方法論](../../coverage-map/methodology/)
- **標準**: 規範的要件と定義 — [Standard (Current)](../../standard/current/)
- **タクソノミー**: AIガバナンスの8次元分類体系 — [タクソノミー](../../standard/current/03-taxonomy/)、[コード](../../standard/current/04-codes/)、[辞書](../../standard/current/05-dictionary/)
- **エビデンスバンドル**: 構造、TOC、トレーサビリティ — [Evidence Bundle](../../artifacts/evidence-bundle/)
- **最小エビデンス要件**: ライフサイクル別MUSTレベルチェックリスト — [Minimum Evidence Requirements](../../artifacts/minimum-evidence/)
- **バリデータ**: ルールと参照チェック — [Validator](../../validator/)
- **例**: 監査対応サンプルバンドル — [Examples](../../examples/)
- **リリース**: 変更履歴と配布 — [Releases](../../releases/)
- **ガバナンス**: ポリシー、セキュリティ、ライセンス — [Governance](../../governance/)

## 監査対応のための最小セット

| 項目 | 場所 | 成果 / 証明されること |
| --- | --- | --- |
| 適合性レベル | [Conformance](../../conformance/) | コンプライアンスの主張方法と必要なエビデンスの範囲 |
| カバレッジマッピング | [カバレッジマップ索引](../../coverage-map/)、[カバレッジマップ方法論](../../coverage-map/methodology/) | 外部規制・標準に対する説明可能性 |
| タクソノミー＆辞書 | [タクソノミー](../../standard/current/03-taxonomy/)、[コード](../../standard/current/04-codes/)、[辞書](../../standard/current/05-dictionary/) | AIシステムの分類体系（8次元、91コード） |
| エビデンス成果物 | [Evidence Bundle](../../artifacts/evidence-bundle/)、[Minimum Evidence](../../artifacts/minimum-evidence/)、[EV Template](../../standard/current/06-ev-template/) | トレーサビリティをサポートするために存在すべきデータ |
| バリデータチェック | [Validator](../../validator/) | 内部一貫性と完全性の検証方法 |
| サンプルバンドル | [Examples](../../examples/) | 監査対応パッケージの実例 |
| 変更管理 | [Releases](../../releases/)、[Governance](../../governance/) | 更新の管理と通知方法 |
| セキュリティ / ライセンス / 商標 | [Governance](../../governance/) | 採用決定のための法的・セキュリティ体制 |

## 引用方法

引用ガイダンスとコンテキストはリポジトリREADMEを使用してください。ガバナンスは権威あるポリシーにリンクしています。
[README.md](https://github.com/billyrise/aimo-standard/blob/main/README.md) と [Governance](../../governance/) を参照。

## Artifacts zip の内容

`aimo-standard-artifacts.zip` には以下が含まれます：

- **タクソノミー（SSOT）**: `source_pack/03_taxonomy/` — 辞書CSV（91コード）、YAML、コード体系
- **JSON スキーマ**: `schemas/jsonschema/` — 機械可読な検証スキーマ
- **テンプレート**: `templates/ev/` — エビデンス記録テンプレート（JSON + Markdown）
- **サンプル**: `examples/` — 素早い導入のための最小サンプルバンドル
- **カバレッジマップ**: `coverage_map/coverage_map.yaml` — 外部標準へのマッピング
- **バリデータルール**: `validator/rules/` — 検証ルール定義
- **ガバナンス文書**: `VERSIONING.md`、`GOVERNANCE.md`、`SECURITY.md`、`LICENSE.txt` など

## 責任境界

AIMO Standard は構造化された証跡フォーマットと説明可能性フレームワークを提供する。法的助言、適合認証、リスク評価、監査実施は**提供しない**。

スコープ定義、前提条件、採用者責任の詳細は [責任境界](../responsibility-boundary/) を参照。

## 提出パッケージの準備方法

監査対応の提出物を準備するには、以下のステップに従う：

1. **Evidence Bundle の生成**: [Evidence Bundle](../../artifacts/evidence-bundle/) と [Minimum Evidence Requirements](../../artifacts/minimum-evidence/) に従い、EV レコード、Dictionary、Summary、Change Log を作成する。
2. **Validator の実行**: `python validator/src/validate.py bundle/root.json` を実行し、構造整合性を確認する。エラーがあれば修正する。
3. **チェックサムの作成**: 提出ファイルすべての SHA-256 チェックサムを生成する：

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
4. **アーティファクトのパッケージ化**: 証跡バンドルの zip アーカイブを作成する：
   ```bash
   zip -r evidence_bundle.zip bundle_directory/
   ```
5. **リリースバージョンの参照**: バンドルが整合する AIMO Standard バージョン（例：`v1.0.0`）を記録する。
6. **提出**: zip、チェックサム、バージョン参照を監査人またはコンプライアンス機能に提供する。

リリースアセットと検証については [Releases](../../releases/) を参照。

## 非過剰主張ステートメント

!!! warning "重要"
    AIMO Standard は**説明可能性と証跡準備**を支援する。法的助言の提供、適合の保証、いかなる規制・フレームワークへの適合認証も**行わない**。採用者は権威ある条文と照合し、適切に専門家の助言を得ること。

スコープ、前提条件、採用者責任の詳細は [責任境界](../responsibility-boundary/) を参照。

## 監査人向け：検証手順

証跡提出物を受領した際、監査人は以下の手順で完全性と構造を検証すべきである：

!!! success "ビルド来歴証明が利用可能"
    すべてのリリースアセットには暗号署名付きビルド来歴証明が含まれています。attestation 検証手順は [バージョンページの検証手順](../../standard/versions/) を参照してください。

### ステップ1：チェックサムの検証（SHA-256）

=== "Linux"

    ```bash
    # 提出物と一緒に SHA256SUMS.txt を受領
    # 全ファイルが記録されたチェックサムと一致することを確認
    sha256sum -c SHA256SUMS.txt

    # または個別ファイルを手動検証：
    sha256sum evidence_bundle.zip
    # 出力を SHA256SUMS.txt の値と比較
    ```

=== "macOS"

    ```bash
    # 全ファイルがチェックサムと一致することを確認
    shasum -a 256 -c SHA256SUMS.txt

    # または個別ファイルを手動検証：
    shasum -a 256 evidence_bundle.zip
    # 出力を SHA256SUMS.txt の値と比較
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 個別ファイルを検証
    Get-FileHash .\evidence_bundle.zip -Algorithm SHA256

    # Hash 出力を SHA256SUMS.txt と比較
    Get-Content .\SHA256SUMS.txt
    ```

チェックサムが一致しない場合、提出物を却下または再提出を要求すべきである。

### ステップ2：バンドル構造の検証（バリデータ）

**前提条件**（初回セットアップ）：

```bash
# 公式 AIMO Standard リリースをクローン
git clone https://github.com/billyrise/aimo-standard.git
cd aimo-standard

# 重要：提出物に記載された正確なバージョンを使用
# VERSION を提出者が宣言したバージョンに置き換える（例：v0.0.1）
VERSION=v0.0.1  # ← 提出物のバージョンに合わせる
git checkout "$VERSION"

# Python 環境のセットアップ
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

!!! warning "バージョン一致"
    常に提出物に記載された正確な AIMO Standard バージョンを使用してください。異なるバージョンを使用すると、バージョン間のスキーマやルール変更により検証結果が一致しない場合があります。

**検証の実行**：

```bash
# 提出されたバンドルを展開
unzip evidence_bundle.zip -d bundle/

# バンドルの root.json に対してバリデータを実行
python validator/src/validate.py bundle/root.json

# 期待出力：「validation OK」またはエラーリスト
```

**例**（組み込みサンプル使用）：

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

バリデータは以下を確認する：

- 必須ファイルの存在（EV レコード、Dictionary）
- JSON ファイルのスキーマ準拠
- 相互参照（request_id、review_id 等）の有効性
- タイムスタンプの存在と適切な形式

### ステップ3：バージョン整合の確認

提出物が公式 AIMO Standard リリースを参照していることを確認する：

1. 記載バージョン（例：`v0.0.1`）が [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) に存在することを確認
2. 提出されたスキーマをリリースアーティファクトと比較
3. 公式リリースからの逸脱を記録

### 確認ポイント

| 確認項目 | 合格基準 | 不合格時の対応 |
| --- | --- | --- |
| チェックサム一致 | 全 `sha256sum -c` チェック合格 | 却下または再提出要求 |
| バリデータ合格 | `validate.py` でエラーなし | 受領前に修正要求 |
| バージョン存在 | リリースタグが GitHub に存在 | バージョン整合を明確化 |
| 必須フィールド存在 | EV レコードに id, timestamp, source, summary | 完成を要求 |
| トレーサビリティ維持 | 相互参照が正しく解決 | リンク修正を要求 |

!!! info "監査人の独立性"
    監査人はバリデータとスキーマを、提出者からではなく、公式 AIMO Standard リリースから直接取得し、検証の独立性を確保すべきである。

## 監査ジャーニー

本ページからの推奨監査ジャーニー：

1. **分類体系**: [タクソノミー](../../standard/current/03-taxonomy/) + [辞書](../../standard/current/05-dictionary/) — 8次元コード体系を理解
2. **証跡構造**: [Evidence Bundle](../../artifacts/evidence-bundle/) — バンドル TOC と追跡可能性を理解
3. **必須証跡**: [Minimum Evidence Requirements](../../artifacts/minimum-evidence/) — ライフサイクル別 MUST チェックリスト
4. **フレームワーク整合**: [Coverage Map](../../coverage-map/) + [Methodology](../../coverage-map/methodology/) — AIMO と外部フレームワークの対応を確認
5. **検証**: [Validator](../../validator/) — 構造整合性チェックを実行
6. **ダウンロード**: [Releases](../../releases/) — リリースアセットを取得しチェックサムを検証
