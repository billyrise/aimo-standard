---
description: AIMOローカライゼーションガイド - 多言語ドキュメントのi18n構造、メンテナンスワークフロー、SSOT原則。
---

# ローカライゼーションガイド

本ページでは、AIMO Standard ドキュメントのローカライゼーション（i18n）構造、メンテナンスワークフロー、SSOT（Single Source of Truth）原則について説明します。

## 言語純度ポリシー

**各言語ページはその言語のコンテンツのみを含むべきです。**

| ルール | 説明 |
| --- | --- |
| **ENページ** | CJK文字や言語固有カラム（`_ja`サフィックス等）への参照を含まない |
| **JAページ** | EN固有の用語を正規構造として説明しない |
| **例外** | `tooling/checks/lint_i18n.py` の `MIXED_LANGUAGE_ALLOWLIST` に記載 |

このポリシーにより：
1. 読者は選択した言語のみを見る
2. 新言語追加時に既存ページを更新する必要がない
3. CIが自動的に違反を検出できる

## 言語構造

AIMO Standard ドキュメントは**フォルダベースの i18n 構造**を採用しています：

```
docs/
├── en/           # 英語（正本）
├── ja/           # 日本語（日本語）
├── es/           # スペイン語（Español）
├── fr/           # フランス語（Français）
├── de/           # ドイツ語（Deutsch）
├── pt/           # ポルトガル語（Português）
├── it/           # イタリア語（Italiano）
├── zh/           # 簡体字中国語（简体中文）
├── zh-TW/        # 繁体字中国語（繁體中文）
└── ko/           # 韓国語（한국어）
```

- **英語が正本（canonical）**: `docs/en/` フォルダがドキュメントコンテンツの正式なソースです。
- **他の言語は構造を反映**: 各言語フォルダ（`ja/` 等）は `en/` と同じファイル構造を維持します。
- **同一ファイル名**: すべての言語で `.md` 拡張子を使用（ファイル名に言語サフィックスなし）。
- **英語へのフォールバック**: 翻訳がないページは自動的に英語コンテンツにフォールバックします。

## タクソノミーデータモデル

タクソノミーは**言語中立のcanonical構造**と個別の翻訳パックを使用します：

```
data/
└── taxonomy/
    ├── canonical.yaml           # 言語中立（コード、ステータス、ライフサイクル）
    └── i18n/
        ├── en.yaml              # 英語ラベルと定義
        ├── ja.yaml              # 日本語ラベルと定義
        └── {lang}.yaml          # 追加言語（空のテンプレート）
```

### Canonical構造 (`canonical.yaml`)

言語中立のデータを含みます：

- コード識別子（例: `FS-001`, `UC-001`）
- ステータス（`active`, `deprecated`, `removed`）
- ライフサイクルメタデータ（`introduced_in`, `deprecated_in`, `removed_in`, `replaced_by`）
- スコープノートと例（技術的参照として英語）

### 翻訳パック (`i18n/*.yaml`)

各言語パックには以下が含まれます：

- 次元名（例: "Functional Scope" / "機能スコープ"）
- コードラベル（例: "End-user Productivity" / "社内生産性"）
- コード定義

**フォールバック**: 翻訳がない場合、システムは英語を使用します。

## SSOT原則

AIMOはタクソノミーデータに**SSOT-firstアーキテクチャ**を採用しています：

| アセットタイプ | SSOT場所 | 説明 |
| --- | --- | --- |
| **タクソノミー（構造）** | `data/taxonomy/canonical.yaml` | 言語中立構造（SSOT） |
| **タクソノミー（i18n）** | `data/taxonomy/i18n/*.yaml` | 言語別翻訳（SSOT） |
| **カバレッジマップ** | `coverage_map/coverage_map.yaml` | フレームワークと証跡のマッピング |
| **スキーマ** | `schemas/jsonschema/` | JSON検証スキーマ |

### 派生ファイル

以下のファイルはSSOTから**生成**されるため、手動編集禁止です：

| ファイル | 生成元 | ジェネレータ |
| --- | --- | --- |
| `artifacts/taxonomy/{version}/{lang}/taxonomy_dictionary.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_en.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_ja.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/code_system.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/dimensions_en_ja.md` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_dictionary.json` | canonical + i18n | `build_artifacts.py` |

### 言語コード（BCP47）

AIMOはBCP47言語コードを採用しています：

| コード | 言語 | ステータス |
| --- | --- | --- |
| `en` | English | 正本（ソース） |
| `ja` | 日本語 | アクティブ |
| `es` | Español（スペイン語） | アクティブ |
| `fr` | Français（フランス語） | アクティブ |
| `de` | Deutsch（ドイツ語） | アクティブ |
| `pt` | Português（ポルトガル語） | アクティブ |
| `it` | Italiano（イタリア語） | アクティブ |
| `zh` | 简体中文（簡体字中国語） | アクティブ |
| `zh-TW` | 繁體中文（繁体字中国語） | アクティブ |
| `ko` | 한국어（韓国語） | アクティブ |

### レガシーCSVファイル（凍結）

`source_pack/03_taxonomy/legacy/` にあるレガシー英日混在CSVファイルは：

- **21列で凍結** — 新しい言語列は追加されません
- **後方互換性のため維持** — 既存の連携は引き続き使用可能
- **CIで強制** — `label_es`, `definition_de` などを追加するとビルドが失敗します

新しい言語には `artifacts/taxonomy/{version}/{lang}/` の言語別アーティファクトを使用してください。

## 翻訳鮮度トラッキング

AIMOは英語（ソース）と翻訳コンテンツの整合性を維持するための**翻訳鮮度トラッキング**システムを使用しています。

### 仕組み

1. 各翻訳ファイルには、どのバージョンの英語ソースから翻訳されたかを追跡するメタデータが含まれます
2. 英語コンテンツが更新されると、システムが古くなった翻訳を検出します
3. CIは古い翻訳について警告しますが、ブロックはしません（翻訳は遅れても問題ありません）

### 翻訳メタデータ

翻訳ファイルにはフロントマターメタデータが含まれます：

```yaml
---
# TRANSLATION METADATA - DO NOT REMOVE
source_file: en/standard/current/01-overview.md
source_hash: abc123def456
translation_date: 2026-02-02
translator: human|machine|hybrid
translation_status: current|outdated|needs_review
---
```

### 同期ツールの使用方法

```bash
# すべての翻訳の鮮度をチェック
python tooling/i18n/sync_translations.py --check

# 特定の言語をチェック
python tooling/i18n/sync_translations.py --check --lang ja

# 翻訳レポートを生成
python tooling/i18n/sync_translations.py --report

# 新しい言語を初期化（ENをベースとしてコピー）
python tooling/i18n/sync_translations.py --init-lang es

# 翻訳完了後にメタデータを更新
python tooling/i18n/sync_translations.py --update-meta docs/ja/index.md
```

詳細な技術仕様については、`tooling/i18n/TRANSLATION_SYNC_SPEC.md` を参照してください。

## 更新ワークフロー

### タクソノミーの更新（新しいSSOT-Firstワークフロー）

1. `data/taxonomy/` のSSOTを編集:
   - 構造変更 → `canonical.yaml`
   - 英語翻訳 → `i18n/en.yaml`
   - 日本語翻訳 → `i18n/ja.yaml`
2. 検証を実行: `python tooling/checks/lint_taxonomy_ssot.py`
3. 全派生ファイルを再生成: `python tooling/taxonomy/build_artifacts.py --version current --langs en ja`
4. 必要に応じてドキュメントページを更新
5. すべての変更をまとめてコミット

### カバレッジマップの更新

1. `coverage_map/coverage_map.yaml`（SSOT）を編集
2. 対応するフレームワークページの表を更新（`docs/en/coverage-map/*.md`）
3. 日本語訳を更新（`docs/ja/coverage-map/*.md`）
4. すべての変更をまとめてコミット

### ドキュメントの更新

1. 英語ソース（`docs/en/...`）を編集
2. 必要に応じて翻訳を更新（または後で更新としてマーク）
3. `python tooling/i18n/sync_translations.py --check` を実行して古い翻訳を確認
4. `python tooling/checks/lint_i18n.py` を実行して見出し整合性を確認
5. `mkdocs build --strict` を実行してビルドを確認
6. すべての変更をまとめてコミット

!!! note "翻訳の優先度"
    すべての翻訳をすぐに更新する必要はありません。Tier 1（重要）ページを優先してください：
    
    - `index.md`
    - `standard/current/*.md`
    - `governance/index.md`
    - `releases/`

## 新言語の追加（5ステップ）

新しい言語（例：スペイン語）を追加するには：

### ステップ1: タクソノミーパックを生成

```bash
python tooling/taxonomy/build_i18n_taxonomy.py --add-lang es --lang-name "Español"
```

英語参照をコメントとして含む `data/taxonomy/i18n/es.yaml` が作成されます。

### ステップ2: ドキュメントフォルダを作成

```bash
mkdir -p docs/es && cp -r docs/en/* docs/es/
```

### ステップ3: mkdocs.ymlを更新

```yaml
plugins:
  - i18n:
      languages:
        - locale: es
          name: Español
          build: true
```

### ステップ4: 翻訳

- `data/taxonomy/i18n/es.yaml` を翻訳
- `docs/es/` のファイルを翻訳

### ステップ5: 検証

```bash
python tooling/checks/lint_i18n.py && mkdocs build --strict
```

!!! success "完了"
    新言語は `/dev/es/` で利用可能になります

## ファイル命名規則

| パターン | 例 | 説明 |
| --- | --- | --- |
| `index.md` | `docs/ja/governance/index.md` | セクションランディングページ |
| `{topic}.md` | `docs/ja/governance/trust-package.md` | トピックページ |
| `{NN}-{topic}.md` | `docs/ja/standard/current/03-taxonomy.md` | 番号付き仕様ページ |

## 品質チェック

コミット前に以下のチェックを実行：

```bash
# i18n構造、見出し整合性、旧フレーズ検出
python tooling/checks/lint_i18n.py

# スキーマとマニフェストのlint
python tooling/checks/lint_schema.py
python tooling/checks/lint_manifest.py

# タクソノミーSSOT lint
python tooling/checks/lint_taxonomy_ssot.py --required-langs en
python tooling/checks/lint_legacy_csv.py
python tooling/checks/lint_taxonomy_dictionary.py
python tooling/checks/lint_taxonomy_json.py

# タクソノミーアーティファクトが最新か確認
python tooling/taxonomy/build_artifacts.py --check

# ビルド確認
mkdocs build --strict
```

## 関連ページ

- [Releases](../../releases/) — ダウンロード可能なパッケージ
- [Governance](../../governance/) — プロジェクトガバナンス
