---
description: AIMO Trust Package — 監査人向け資料パック。監査・法務・ITセキュリティが AI ガバナンス採用準備を評価するための最小ドキュメント。
---
<!-- aimo:translation_status=translated -->

# Trust Package（Assurance Package）

本ページは、監査人・法務・ITセキュリティが採用準備を評価するために必要な最小資料をまとめたハブです。証跡の目次や Coverage 表の詳細は各セクションで管理されています。

## ダウンロード

**[Trust Package PDF のダウンロード（最新リリース）](https://github.com/billyrise/aimo-standard/releases/latest)**

Trust Package PDF は監査人向け資料を1つの文書に集約しています。各 GitHub リリースには以下が含まれます：

- `trust_package.pdf` — 英語版 Trust Package
- `trust_package.ja.pdf` — 日本語版 Trust Package
- `aimo-standard-artifacts.zip` — スキーマ、テンプレート、例、Validator ルール
- `SHA256SUMS.txt` — 検証用チェックサム

## 含まれる内容

- **Conformance**: 適合の主張方法と各レベルの意味 — [Conformance](../../conformance/)
- **Coverage Map**: 外部標準との対応 — [Coverage Map 索引](../../coverage-map/)、[Coverage Map 方法論](../../coverage-map/methodology/)
- **Standard**: 規範要件と定義 — [Standard (Current)](../../standard/current/)
- **Taxonomy**: AI ガバナンスの 8 次元分類 — [Taxonomy](../../standard/current/03-taxonomy/)、[Codes](../../standard/current/04-codes/)、[Dictionary](../../standard/current/05-dictionary/)
- **Evidence Bundle**: 構造、目次、追跡可能性 — [Evidence Bundle](../../artifacts/evidence-bundle/)
- **Minimum Evidence Requirements**: ライフサイクル別 MUST チェックリスト — [Minimum Evidence Requirements](../../artifacts/minimum-evidence/)
- **ISO/IEC 42001 Certification Readiness Toolkit**: ISO 42001 に沿った監査可能証跡への最短経路 — [ISO 42001 Certification Readiness Toolkit](../../artifacts/iso-42001-certification-readiness-toolkit/)。ツールキットは準備の支援のみ。認証の判断は認定認証機関が行います。
- **Validator**: ルールと参照チェック — [Validator](../../validator/)
- **Examples**: 監査可能なサンプルバンドル — [Examples](../../examples/)
- **Releases**: 変更履歴と配布 — [Releases](../../releases/)
- **Governance**: ポリシー、セキュリティ、ライセンス — [Governance](../../governance/)

## 監査準備の最小セット

| 項目 | 参照先 | 成果／証明内容 |
| --- | --- | --- |
| 適合レベル | [Conformance](../../conformance/) | 適合の主張方法と必要な証跡の範囲 |
| Coverage マッピング | [Coverage Map 索引](../../coverage-map/)、[Coverage Map 方法論](../../coverage-map/methodology/) | 外部規制・標準への説明可能性 |
| Taxonomy & Dictionary | [Taxonomy](../../standard/current/03-taxonomy/)、[Codes](../../standard/current/04-codes/)、[Dictionary](../../standard/current/05-dictionary/) | AI システムの分類（8 次元、91 コード） |
| 証跡アーティファクト | [Evidence Bundle](../../artifacts/evidence-bundle/)、[Minimum Evidence](../../artifacts/minimum-evidence/)、[EV Template](../../standard/current/06-ev-template/) | 追跡可能性を支える必要データ |
| Validator チェック | [Validator](../../validator/) | 内部一貫性・完全性の検証方法 |
| サンプルバンドル | [Examples](../../examples/) | 監査可能パッケージの実例 |
| 変更管理 | [Releases](../../releases/)、[Governance](../../governance/) | 更新の管理・共有方法 |
| セキュリティ／ライセンス／商標 | [Governance](../../governance/) | 採用判断のための法的・セキュリティ姿勢 |

## 引用方法

引用のガイダンスと文脈はリポジトリの README を、権威あるポリシーへのリンクは Governance を参照してください。
[README.md](https://github.com/billyrise/aimo-standard/blob/main/README.md) および [Governance](../../governance/) を参照。

## Artifacts zip の内容

`aimo-standard-artifacts.zip` には以下が含まれます：

- **Taxonomy (SSOT)**: `source_pack/03_taxonomy/` — 辞書 CSV（91 コード）、YAML、コード体系
- **JSON Schemas**: `schemas/jsonschema/` — 機械可読な検証スキーマ
- **Templates**: `templates/ev/` — 証跡レコードテンプレート（JSON + Markdown）
- **Examples**: `examples/` — 迅速な採用のための最小サンプルバンドル
- **Coverage Map**: `coverage_map/coverage_map.yaml` — 外部標準との対応
- **Validator Rules**: `validator/rules/` — 検証ルール定義
- **Governance ドキュメント**: `VERSIONING.md`, `GOVERNANCE.md`, `SECURITY.md`, `LICENSE.txt` 等

## 責任の境界

Trust Package は**保証・監査引き継ぎ**の入口です：監査人と採用者向けの資料を集約しています。AIMO Standard は構造化証跡フォーマットと説明可能性の枠組みを提供しますが、**認証、適合保証、法務助言、監査の実施は行いません**。認証・適合の判断は認定認証機関、監査人、採用組織にあります。

スコープの定義、前提、採用者責任の詳細は [Responsibility Boundary](../responsibility-boundary/) および [Conformance](../../conformance/) を参照してください。

## 提出パッケージの準備方法

監査可能な提出物を準備するには、次の手順に従ってください。

1. **Evidence Bundle の生成**: [Evidence Bundle](../../artifacts/evidence-bundle/) および [Minimum Evidence Requirements](../../artifacts/minimum-evidence/) に従い、EV レコード、Dictionary、Summary、Change Log を作成してください。ISO 42001 を意識した準備については [ISO 42001 Certification Readiness Toolkit](../../artifacts/iso-42001-certification-readiness-toolkit/) を参照してください。
2. **Validator の実行**: `python validator/src/validate.py bundle/root.json` を実行して構造の一貫性を確認してください。エラーがあれば修正してから先に進んでください。
3. **チェックサムの作成**: 提出する全ファイルの SHA-256 チェックサムを生成してください：

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
4. **アーティファクトのパッケージ化**: Evidence Bundle の zip アーカイブを作成してください：
   ```bash
   zip -r evidence_bundle.zip bundle_directory/
   ```
5. **リリースバージョンの参照**: バンドルが対応する AIMO Standard のバージョン（例: `v1.0.0`）を明記してください。
6. **提出**: zip、チェックサム、バージョン参照を監査人またはコンプライアンス担当に提供してください。

リリース資産と検証については [Releases](../../releases/) を参照してください。

## 過大主張禁止

!!! warning "重要：認証・保証・法規適合の主張は行いません"
    - AIMO Standard は**証跡のパッケージングと検証のフォーマット**を定義します。法令や標準への適合を認証するものではありません。
    - 監査・保証の意見は、独立した監査人と採用組織の責任です。
    - **適切な主張**: 「Evidence Bundle は AIMO Standard v0.1.2 に従って作成され、AIMO Validator により構造検証されました。」
    - **不適切な主張**: 「EU AI Act 適合」「ISO 42001 認証取得」「政府承認」等。

スコープ、前提、採用者責任の詳細は [Responsibility Boundary](../responsibility-boundary/) を参照してください。

## 監査人向け：検証手順

証跡の提出物を受け取った際は、次の手順で整合性と構造を検証してください。

!!! success "ビルド出所の提供"
    すべてのリリース資産には暗号署名付きのビルド attestation が含まれます。attestation の検証手順は [Verification Procedure](../../standard/versions/#4-verify-build-provenance-attestation) を参照してください。

### Step 1: チェックサムの検証（SHA-256）

=== "Linux"

    ```bash
    # 提出物とともに SHA256SUMS.txt をダウンロードまたは受け取る
    # 全ファイルが記録されたチェックサムと一致することを確認
    sha256sum -c SHA256SUMS.txt

    # または個別ファイルを手動で検証：
    sha256sum evidence_bundle.zip
    # 出力を SHA256SUMS.txt の値と比較
    ```

=== "macOS"

    ```bash
    # 全ファイルが記録されたチェックサムと一致することを確認
    shasum -a 256 -c SHA256SUMS.txt

    # または個別ファイルを手動で検証：
    shasum -a 256 evidence_bundle.zip
    # 出力を SHA256SUMS.txt の値と比較
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 個別ファイルの検証
    Get-FileHash .\evidence_bundle.zip -Algorithm SHA256

    # Hash の出力を SHA256SUMS.txt と比較
    Get-Content .\SHA256SUMS.txt
    ```

いずれかのチェックサムが失敗した場合は、提出物を却下するか再提出を求めてください。

### Step 2: バンドル構造の検証（Validator）

**前提**（初回のみ）：

```bash
# 公式 AIMO Standard リリースをクローン
git clone https://github.com/billyrise/aimo-standard.git
cd aimo-standard

# 重要: 提出物に記載されたバージョンと一致させる
# VERSION を提出者が申告したバージョン（例: v0.0.1）に置き換える
VERSION=v0.0.1  # ← 提出物のバージョンに合わせる
git checkout "$VERSION"

# Python 環境のセットアップ
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

!!! warning "バージョン一致"
    提出物に記載された AIMO Standard のバージョンを必ず使用してください。異なるバージョンではスキーマやルールの違いにより検証結果が一致しない場合があります。

**検証の実行**:

```bash
# 提出されたバンドルを展開
unzip evidence_bundle.zip -d bundle/

# バンドルの root.json に対して Validator を実行
python validator/src/validate.py bundle/root.json

# 想定出力: "validation OK" またはエラー一覧
```

**例**（同梱サンプル使用）:

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

Validator は以下をチェックします：

- 必須ファイルの存在（EV レコード、Dictionary）
- JSON がスキーマに準拠していること
- 相互参照（request_id、review_id 等）が有効であること
- タイムスタンプが存在し適切にフォーマットされていること

### Step 3: バージョン整合の確認

提出物が公式 AIMO Standard リリースを参照していることを確認してください：

1. 記載されたバージョン（例: `v0.0.1`）が [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) に存在することを確認する
2. 提出されたスキーマをリリース資産と比較する
3. 公式リリースからの相違があれば記録する

### 確認ポイント

| チェック | 合格基準 | 不合格時の対応 |
| --- | --- | --- |
| チェックサム一致 | すべての `sha256sum -c` が成功 | 却下または再提出依頼 |
| Validator 成功 | `validate.py` からエラーなし | 受領前に修正を依頼 |
| バージョン存在 | GitHub にリリースタグが存在 | バージョン整合を確認 |
| 必須フィールド | EV レコードに id、timestamp、source、summary がある | 完成を依頼 |
| 追跡可能性 | 相互参照が正しく解決する | リンク修正を依頼 |

!!! info "監査人の独立性"
    検証の独立性のため、Validator とスキーマは提出者ではなく公式 AIMO Standard リリースから直接取得してください。

## 監査の流れ

このページから推奨される監査の流れは以下のとおりです。

1. **分類体系**: [Taxonomy](../../standard/current/03-taxonomy/) + [Dictionary](../../standard/current/05-dictionary/) — 8 次元コード体系の理解
2. **証跡構造**: [Evidence Bundle](../../artifacts/evidence-bundle/) — バンドル目次と追跡可能性の理解
3. **必要証跡**: [Minimum Evidence Requirements](../../artifacts/minimum-evidence/) — ライフサイクル別 MUST チェックリスト
4. **フレームワーク対応**: [Coverage Map](../../coverage-map/) + [Methodology](../../coverage-map/methodology/) — AIMO と外部フレームワークの対応
5. **検証**: [Validator](../../validator/) — 構造一貫性チェックの実行
6. **ダウンロード**: [Releases](../../releases/) — リリース資産の取得とチェックサム検証
