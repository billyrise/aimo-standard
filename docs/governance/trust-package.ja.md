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

- **適合性**: コンプライアンスの主張方法とレベルの意味 — [Conformance](../conformance/index.ja.md)
- **カバレッジマップ**: 外部標準へのマッピング — [カバレッジマップ索引](../coverage-map/index.ja.md)、[カバレッジマップ方法論](../coverage-map/methodology.ja.md)
- **標準**: 規範的要件と定義 — [Standard (Current)](../standard/current/index.ja.md)
- **エビデンスバンドル**: 構造、TOC、トレーサビリティ — [Evidence Bundle](../artifacts/evidence-bundle.ja.md)
- **最小エビデンス要件**: ライフサイクル別MUSTレベルチェックリスト — [Minimum Evidence Requirements](../artifacts/minimum-evidence.ja.md)
- **バリデータ**: ルールと参照チェック — [Validator](../validator/index.ja.md)
- **例**: 監査対応サンプルバンドル — [Examples](../examples/index.ja.md)
- **リリース**: 変更履歴と配布 — [Releases](../releases/index.ja.md)
- **ガバナンス**: ポリシー、セキュリティ、ライセンス — [Governance](../governance/index.ja.md)

## 監査対応のための最小セット

| 項目 | 場所 | 成果 / 証明されること |
| --- | --- | --- |
| 適合性レベル | [Conformance](../conformance/index.ja.md) | コンプライアンスの主張方法と必要なエビデンスの範囲 |
| カバレッジマッピング | [カバレッジマップ索引](../coverage-map/index.ja.md)、[カバレッジマップ方法論](../coverage-map/methodology.ja.md) | 外部規制・標準に対する説明可能性 |
| エビデンス成果物 | [Evidence Bundle](../artifacts/evidence-bundle.ja.md)、[Minimum Evidence](../artifacts/minimum-evidence.ja.md)、[EV Template](../standard/current/06-ev-template.ja.md) | トレーサビリティをサポートするために存在すべきデータ |
| バリデータチェック | [Validator](../validator/index.ja.md) | 内部一貫性と完全性の検証方法 |
| サンプルバンドル | [Examples](../examples/index.ja.md) | 監査対応パッケージの実例 |
| 変更管理 | [Releases](../releases/index.ja.md)、[Governance](../governance/index.ja.md) | 更新の管理と通知方法 |
| セキュリティ / ライセンス / 商標 | [Governance](../governance/index.ja.md) | 採用決定のための法的・セキュリティ体制 |

## 引用方法

引用ガイダンスとコンテキストはリポジトリREADMEを使用してください。ガバナンスは権威あるポリシーにリンクしています。
[README.md](https://github.com/billyrise/aimo-standard/blob/main/README.md) と [Governance](../governance/index.ja.md) を参照。

## Artifacts zip の内容

`aimo-standard-artifacts.zip` には以下が含まれます：

- **JSON スキーマ**: `schemas/jsonschema/` — 機械可読な検証スキーマ
- **テンプレート**: `templates/ev/` — エビデンス記録テンプレート（JSON + Markdown）
- **サンプル**: `examples/` — 素早い導入のための最小サンプルバンドル
- **カバレッジマップ**: `coverage_map/coverage_map.yaml` — 外部標準へのマッピング
- **バリデータルール**: `validator/rules/` — 検証ルール定義
- **ガバナンス文書**: `VERSIONING.md`、`GOVERNANCE.md`、`SECURITY.md`、`LICENSE.txt` など

## 責任境界

AIMO Standard は構造化された証跡フォーマットと説明可能性フレームワークを提供する。法的助言、適合認証、リスク評価、監査実施は**提供しない**。

スコープ定義、前提条件、採用者責任の詳細は [責任境界](responsibility-boundary.ja.md) を参照。

## 提出パッケージの準備方法

監査対応の提出物を準備するには、以下のステップに従う：

1. **Evidence Bundle の生成**: [Evidence Bundle](../artifacts/evidence-bundle.ja.md) と [Minimum Evidence Requirements](../artifacts/minimum-evidence.ja.md) に従い、EV レコード、Dictionary、Summary、Change Log を作成する。
2. **Validator の実行**: `python validator/src/validate.py` をバンドルに対して実行し、構造整合性を確認する。エラーがあれば修正する。
3. **チェックサムの作成**: 提出ファイルすべての SHA-256 チェックサムを生成する：
   ```bash
   sha256sum *.json *.pdf > SHA256SUMS.txt
   ```
4. **アーティファクトのパッケージ化**: 証跡バンドルの zip アーカイブを作成する：
   ```bash
   zip -r evidence_bundle.zip bundle_directory/
   ```
5. **リリースバージョンの参照**: バンドルが整合する AIMO Standard バージョン（例：`v1.0.0`）を記録する。
6. **提出**: zip、チェックサム、バージョン参照を監査人またはコンプライアンス機能に提供する。

リリースアセットと検証については [Releases](../releases/index.ja.md) を参照。

## 非過剰主張ステートメント

!!! warning "重要"
    AIMO Standard は**説明可能性と証跡準備**を支援する。法的助言の提供、適合の保証、いかなる規制・フレームワークへの適合認証も**行わない**。採用者は権威ある条文と照合し、適切に専門家の助言を得ること。

スコープ、前提条件、採用者責任の詳細は [責任境界](responsibility-boundary.ja.md) を参照。

## 監査ジャーニー

本ページからの推奨監査ジャーニー：

1. **証跡構造**: [Evidence Bundle](../artifacts/evidence-bundle.ja.md) — バンドル TOC と追跡可能性を理解
2. **必須証跡**: [Minimum Evidence Requirements](../artifacts/minimum-evidence.ja.md) — ライフサイクル別 MUST チェックリスト
3. **フレームワーク整合**: [Coverage Map](../coverage-map/index.ja.md) + [Methodology](../coverage-map/methodology.ja.md) — AIMO と外部フレームワークの対応を確認
4. **検証**: [Validator](../validator/index.ja.md) — 構造整合性チェックを実行
5. **ダウンロード**: [Releases](../releases/index.ja.md) — リリースアセットを取得しチェックサムを検証
