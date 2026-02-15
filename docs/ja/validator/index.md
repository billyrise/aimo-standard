---
description: AIMOバリデータハブ - 検証ツールクイックスタート。30秒でインストール、実行、結果解釈。Evidence Pack検証とコンプライアンスチェック。
---
<!-- aimo:translation_status=translated -->

# Validator

本ページは検証ツールとルールのハブである。バリデータおよびルールの規範仕様は Standard に記載する。

## クイックスタート（30秒）

**1. 前提条件**

```bash
pip install jsonschema   # 未インストールの場合
```

**2. サンプルバンドルに対してバリデーションを実行**

```bash
# ルート JSON 単体
python validator/src/validate.py examples/evidence_bundle_minimal/root.json

# Evidence Bundle ディレクトリ（v0.1 最小例：manifest / object_index / payload_index / signing / hash_chain を検証）
python validator/src/validate.py examples/evidence_bundle_v01_minimal
```

**3. レポートを読み、エラー/警告を修正**

出力例（成功）：

```
OK
```

出力例（失敗）：

```
Schema validation failed:
<root>: 'version' is a required property
<root>: 'dictionary' is a required property
<root>: 'evidence' is a required property
```

**終了コード**: `0` = 成功, `1` = バリデーションエラー, `2` = 使用法エラー（引数不足など）

---

## 出力形式（--format）と CI での使い分け

| オプション | 用途 | 出力 |
|------------|------|------|
| `default`（省略時） | ローカルでの確認 | 人間向けメッセージ（OK / エラー一覧） |
| `--format json` | CI・スクリプト向け | 機械可読 JSON（`valid`, `errors`, `warnings`, `path`, `profiles_valid`） |
| `--format sarif` | GitHub Code Scanning | SARIF 2.1.0（ruleId, level, location, message）。提出前ゲートとして Code Scanning に結果を載せる際に使用。 |

**例（Evidence Bundle v0.1 最小例の検証）**

```bash
# ローカルで成功確認
python validator/src/validate.py examples/evidence_bundle_v01_minimal

# JSON で結果を取得（CI でパースする場合）
python validator/src/validate.py examples/evidence_bundle_v01_minimal --validate-profiles --format json

# SARIF をファイルに保存（Code Scanning アップロード用）
python validator/src/validate.py examples/evidence_bundle_v01_minimal --validate-profiles --format sarif > dist/validator.sarif
```

**GitHub 上での見え方**: Quality Gate ワークフローで `--format sarif` の結果を `upload-sarif` により Code Scanning に送信している。PR でバリデータが失敗すると、Code Scanning の「Security」タブに `aimo-standard/validation` の結果として表示され、どのパスでどのエラーかが確認できる。

---

## チェックする内容

- **スキーマ検証**: root オブジェクト、dictionary、evidence が JSON Schema に準拠しているか
- **辞書整合性**: すべてのコードがタクソノミー辞書に存在するか
- **コードステータス**: 非推奨コードは警告、削除コードはエラー

## チェックしない内容

- **コンテンツの正確性**: バリデータは構造をチェックし、意味はチェックしない
- **準拠保証**: バリデーション合格は規制への準拠を保証しない
- **人の判断**: 文脈依存の判断は人によるレビューが必要（[人による監督プロトコル](../governance/human-oversight-protocol/)参照）
- **ログの自動収集**: バリデータは提出された証跡を検証するが、ログを収集しない

---

## リソース

- **仕様**: [Standard > Current > Validator](../standard/current/07-validator/) — ルール、参照チェック、検証と証跡の関係。
- **ルールと実装**: リポジトリの `validator/rules/`（チェック）、`validator/src/`（参照実装）。実行方法と CI での利用は仕様に記載。
- **解釈**: 検証「失敗」が監査上何を意味するか（仕様で説明）。

適合性とアーティファクトの利用については [Conformance](../conformance/) と [Artifacts](../artifacts/) を参照。
