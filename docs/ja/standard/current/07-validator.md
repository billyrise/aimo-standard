---
description: AIMOバリデータ - Evidence PackがAIMO Standardスキーマに準拠していることを確認。検証ルール、エラー処理、コンプライアンスチェック用リファレンス実装。
---

# バリデータ

AIMOバリデータは、Evidence Packおよび関連アーティファクトがAIMO Standardスキーマと要件に準拠していることを確認します。

関連：[人による監督プロトコル](../../governance/human-oversight-protocol.md) — 機械チェックと人の判断の責任境界。

## バリデータが検証する対象（必須ファイルセット）

バリデータは **Evidence Bundle** の構造と関連アーティファクトを検証します。最小限の提出には以下が必要です。

| アーティファクト | 目的 | 正規の場所（リリースごと） |
|------------------|------|----------------------------|
| **Evidence Pack マニフェスト** | ルートマニフェスト（`root.json` 等） | スキーマ: [evidence_pack_manifest.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/evidence_pack_manifest.schema.json)；リリース ZIP: `schemas/jsonschema/` |
| **Dictionary** | マニフェストで使用する taxonomy コード | [Evidence Bundle](../../artifacts/evidence-bundle.md) 構造；[Dictionary](./05-dictionary.md) 仕様 |
| **Minimum Evidence Requirements** | 監査人・実装者向けチェックリスト | [Minimum Evidence Requirements](../../artifacts/minimum-evidence.md) |

バリデータは法的・規制上の適合を保証しません。構造がスキーマとコード体系に準拠しているかを検証します。含める証跡のチェックリストは [Minimum Evidence Requirements](../../artifacts/minimum-evidence.md) を参照してください。

**特定バージョンの正規 URL**：準拠するバージョン（例：`v0.0.3`）の [GitHub Release](https://github.com/billyrise/aimo-standard/releases) からスキーマとバリデータを取得してください。リリース ZIP（`aimo-standard-artifacts.zip`）には `schemas/jsonschema/`、テンプレート、バリデータルールが含まれます。

## 実運用でのValidator

30秒クイックスタート（インストール、実行、出力の解釈）は [Validator ハブ](../../validator/index.md) を参照。

## バリデータMVP要件

最小限のバリデータは以下のチェックを実行する必要があります：

### 1. 必須フィールドバリデーション

すべての必須フィールドが存在することを確認：

| アーティファクト | 必須フィールド |
| --- | --- |
| Evidence Packマニフェスト | pack_id, pack_version, taxonomy_version, created_date, last_updated, codes, evidence_files |
| Codesオブジェクト | FS, UC, DT, CH, IM, RS, EV（OBは任意） |
| Evidence Fileエントリ | file_id, filename, ev_type, title |

### 2. 次元コードバリデーション

各必須次元に少なくとも1つのコードがあることを確認：

| 次元 | 要件 |
| --- | --- |
| FS（機能スコープ） | 正確に1つのコード |
| UC（ユースケース分類） | 少なくとも1つのコード |
| DT（データ種別） | 少なくとも1つのコード |
| CH（チャネル） | 少なくとも1つのコード |
| IM（統合形態） | 正確に1つのコード |
| RS（リスク面） | 少なくとも1つのコード |
| OB（成果） | 任意（0個以上） |
| EV（証跡種別） | 少なくとも1つのコード |

### 3. 辞書存在チェック

すべてのコードがタクソノミー辞書に存在することを検証：

- 指定された`taxonomy_version`のタクソノミー辞書をロード
- マニフェスト内の各コードが辞書に存在することを確認
- 無効なコードを次元と値と共に報告

### 4. コードフォーマットバリデーション

すべてのコードが期待されるフォーマットに一致することを確認：

```regex
^(FS|UC|DT|CH|IM|RS|OB|EV)-\d{3}$
```

### 5. スキーマバリデーション

JSON Schemaに対してバリデーション：

| スキーマ | 目的 |
| --- | --- |
| `evidence_pack_manifest.schema.json` | Evidence Packマニフェスト |
| `taxonomy_pack.schema.json` | タクソノミーパック定義 |
| `changelog.schema.json` | 変更履歴エントリ |

## バリデーションルール

### ルール：必須次元

```yaml
rule_id: required_dimensions
description: すべての必須次元に少なくとも1つのコードが必要
severity: error
check: |
  - FS: 正確に1つ
  - UC: 少なくとも1つ
  - DT: 少なくとも1つ
  - CH: 少なくとも1つ
  - IM: 正確に1つ
  - RS: 少なくとも1つ
  - EV: 少なくとも1つ
```

### ルール：有効なコード

```yaml
rule_id: valid_codes
description: すべてのコードがタクソノミー辞書に存在する必要がある
severity: error
check: |
  manifest.codes内の各コードについて：
    - 指定されたtaxonomy_versionの辞書にコードが存在する
    - コードステータスが'active'（'deprecated'の場合は警告）
```

### ルール：コードフォーマット

```yaml
rule_id: code_format
description: すべてのコードが標準フォーマットに一致する必要がある
severity: error
pattern: "^(FS|UC|DT|CH|IM|RS|OB|EV)-\\d{3}$"
```

### ルール：バージョンフォーマット

```yaml
rule_id: version_format
description: バージョンは有効なSemVerである必要がある
severity: error
pattern: "^\\d+\\.\\d+\\.\\d+$"
fields:
  - pack_version
  - taxonomy_version
```

## エラー出力フォーマット

バリデーションエラーは以下のフォーマットで報告されます：

```
<path>: <severity>: <message>
```

**例：**

```
codes.FS: error: 必須次元'FS'にコードがありません
codes.UC[0]: error: コード'UC-999'は辞書v0.1.0に存在しません
pack_version: error: 無効なバージョンフォーマット'v1.0'（SemVer形式が必要）
codes.RS[1]: warning: コード'RS-002'はv0.2.0で非推奨です
```

## バリデータがチェックしないこと

バリデータは構造的な適合性に焦点を当て、コンテンツ品質はチェックしません：

| 側面 | 理由 |
| --- | --- |
| コンテンツの正確性 | バリデータは構造をチェックし、意味はチェックしない |
| 証跡の完全性 | テンプレートはガイドであり、強制フォーマットではない |
| 相互参照の解決 | ファイル存在は検証されない |
| タイムスタンプの有効性 | ISO-8601は厳密にバリデーションされない |
| IDの一意性 | 現在は強制されていない |
| 完全性ハッシュ | 採用者の責任 |

## リファレンス実装

Pythonでのリファレンス実装が提供されています：

```
validator/src/validate.py
```

### 使用方法

```bash
python validator/src/validate.py <manifest.json>
```

### 出力例

```
Validating: evidence_pack_manifest.json
Taxonomy version: 0.1.0

Checking required dimensions...
  FS: OK (1 code)
  UC: OK (3 codes)
  DT: OK (1 code)
  CH: OK (1 code)
  IM: OK (1 code)
  RS: OK (3 codes)
  OB: OK (2 codes)
  EV: OK (7 codes)

Checking code validity...
  All codes valid.

Validation: PASSED
```

## バージョニングポリシー

バリデータルールはSemVerに従います：

- **MAJOR**: 破壊的なルール変更（既存の有効なパックを失敗させる新しい必須チェック）
- **MINOR**: 新しい任意チェック、警告、または情報メッセージ
- **PATCH**: バリデーション結果を変更しないバグ修正

## スキーマ参照

| スキーマ | 場所 |
| --- | --- |
| Evidence Packマニフェスト | `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json` |
| タクソノミーパック | `source_pack/03_taxonomy/schemas/taxonomy_pack.schema.json` |
| 変更履歴 | `source_pack/03_taxonomy/schemas/changelog.schema.json` |

## 参照

- [タクソノミー](./03-taxonomy.md) - 次元定義
- [コード](./04-codes.md) - コードフォーマット
- [辞書](./05-dictionary.md) - コード辞書
- [バリデータルール](../../validator/index.md) - 完全なルールドキュメント
