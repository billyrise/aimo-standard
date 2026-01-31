# Validator

本セクションは、検証ルールと参照チェックのハブである。
規範仕様は Standard に記載する。

- **仕様**: [Standard > Validator](../standard/current/07-validator.md)。
- **ルールと実装**: リポジトリの `validator/rules/` と `validator/src/`。
- **監査での利用**: 内部整合性と完全性の確認に用いる。

証跡パッケージは [Examples](../examples/index.md) および [Trust Package](../governance/trust-package.md) を参照。
# バリデータ（Validator）

本ページは検証ツールとルールのハブである。バリデータおよびルールの規範仕様は Standard に記載する。

- **仕様**: [Standard > Current > Validator](../standard/current/07-validator.md) — ルール、参照チェック、検証と証跡の関係。
- **ルールと実装**: リポジトリの `validator/rules/`（チェック）、`validator/src/`（参照実装）。実行方法と CI での利用は仕様に記載。
- **解釈**: 検証「失敗」が監査上何を意味するか（仕様で説明。CU-01 では別ページは設けない）。

適合性とアーティファクトの利用については [Conformance](../conformance/index.md) と [Artifacts](../artifacts/index.md) を参照。
