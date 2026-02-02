---
description: AIMOバリデータハブ - 検証ツールクイックスタート。30秒でインストール、実行、結果解釈。Evidence Pack検証とコンプライアンスチェック。
---

# Validator

本ページは検証ツールとルールのハブである。バリデータおよびルールの規範仕様は Standard に記載する。

## クイックスタート（30秒）

**1. 前提条件**

```bash
pip install jsonschema   # 未インストールの場合
```

**2. サンプルバンドルに対してバリデーションを実行**

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
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

終了コード: `0` = 成功, `1` = バリデーションエラー, `2` = 使用法エラー

---

## チェックする内容

- **スキーマ検証**: root オブジェクト、dictionary、evidence が JSON Schema に準拠しているか
- **辞書整合性**: すべてのコードがタクソノミー辞書に存在するか
- **コードステータス**: 非推奨コードは警告、削除コードはエラー

## チェックしない内容

- **コンテンツの正確性**: バリデータは構造をチェックし、意味はチェックしない
- **準拠保証**: バリデーション合格は規制への準拠を保証しない
- **人の判断**: 文脈依存の判断は人によるレビューが必要（[人による監督プロトコル](../governance/human-oversight-protocol.md)参照）
- **ログの自動収集**: バリデータは提出された証跡を検証するが、ログを収集しない

---

## リソース

- **仕様**: [Standard > Current > Validator](../standard/current/07-validator.md) — ルール、参照チェック、検証と証跡の関係。
- **ルールと実装**: リポジトリの `validator/rules/`（チェック）、`validator/src/`（参照実装）。実行方法と CI での利用は仕様に記載。
- **解釈**: 検証「失敗」が監査上何を意味するか（仕様で説明）。

適合性とアーティファクトの利用については [Conformance](../conformance/index.md) と [Artifacts](../artifacts/index.md) を参照。
