---
description: Evidence Bundle Coverage Map テンプレ（v0.1）。監査向け一枚まとめ — スコープ、エビデンス種別、コントロール対応、除外・前提、整合性証明の要約。
---

# Evidence Bundle Coverage Map（テンプレ）

!!! info "Informative — 推奨実務テンプレ"
    本ページは、Evidence Bundle の**推奨実務テンプレ**としての「Coverage Map」一枚の雛形を定義する。標準の必須項目ではなく、**informative** とする。監査人への引き継ぎ用に「このバンドルで何をカバーし、何をカバーしないか」を記載するために利用できる。参照（例：フレームワークへのリンク）は安定させる；採用は実装者判断とする。

---

## 1. スコープ（Scope）

| 項目 | 説明 |
|------|------|
| **スコープ参照** | マニフェストの `scope_ref`（例: `SC-001`）。本バンドルが対象とするスコープ。 |
| **Bundle ID** | `bundle_id`（UUID）— 本バンドルの一意識別子。 |
| **Bundle バージョン** | `bundle_version`（SemVer）— バンドルのバージョン。 |
| **対象期間 / スナップショット** | 任意：本バンドルが対象とする期間または日付（例: 2026-Q1、as-of 2026-02-03）。 |

---

## 2. エビデンス種別（EV / objects と payloads）

| 区分 | 内容 | v0.1 minimal の例 |
|------|------|-------------------|
| **object_index** | 列挙オブジェクト（メタデータ・索引）。各要素: `id`, `type`, `path`, `sha256`。 | 例: `objects/index.json`（index 型）。 |
| **payload_index** | ペイロード（ルート EV JSON、Evidence Pack 等）。各要素: `logical_id`, `path`, `sha256`, `mime`, `size`。 | 例: `payloads/root.json`（ルート AIMO EV JSON）。 |
| **EV 種別** | エビデンスレコード（ルートまたはペイロード内）— request, review, exception, renewal, change log。 | [Evidence Pack Template](../standard/current/06-ev-template.md) および [Minimum Evidence Requirements](minimum-evidence.md) に準拠。 |

*object_index / payload_index は拡張可能。path はバンドルルート内に留め、[Evidence Bundle ルート構造（v0.1）](../standard/current/09-evidence-bundle-structure.md) を満たすこと。*

---

## 3. コントロール対応（参照のみ）

外部フレームワークとの対応は**参照用**であり、標準は特定規制への適合を義務付けない。

| フレームワーク | 本バンドルでの利用 | 参照 |
|----------------|--------------------|------|
| **ISO/IEC 42001** | 任意：本バンドルがカバーする AI MS テーマを記載。 | [Coverage Map → ISO 42001](../coverage-map/iso-42001.md) |
| **EU AI Act** | 任意：ドキュメント・記録保持の対応レベル。 | [Coverage Map → EU AI Act](../coverage-map/eu-ai-act.md) |
| **NIST AI RMF** | 任意：Govern, Map, Measure, Manage の対応。 | [Coverage Map → NIST AI RMF](../coverage-map/nist-ai-rmf.md) |
| **ISMS (27001/27002)** | 任意：変更管理、アクセス、ログ、整合性。 | [Coverage Map → ISMS](../coverage-map/isms.md) |

*「本バンドルでの利用」は提出ごとに記入。標準は特定のコントロール網羅を要求しない。*

---

## 4. 除外・前提（Exclusions / Assumptions）

| 区分 | 本バンドルで**カバーしない**もの（例 — 提出ごとに調整） |
|------|--------------------------------------------------------|
| **除外** | 例：スコープ外のシステム・ユースケース；エビデンス対象外の第三者コンポーネント；本バンドル対象期間外。 |
| **前提** | 例：Dictionary/ taxonomy バージョン；使用した Validator/スキーマバージョン；Custody・保持は実装側で定義。 |
| **制限** | 例：v0.1 では署名の暗号検証は範囲外；規制の法的解釈は行わない。 |

*プレースホルダを提出ごとの除外・前提に置き換える。*

---

## 5. 整合性証明の要約（Integrity proof summary）（v0.1）

| 要素 | 提供内容（v0.1 規範） |
|------|------------------------|
| **manifest.json** | 存在しスキーマ有効。`object_index`, `payload_index`, `hash_chain`, `signing` を含む。 |
| **sha256** | `object_index` / `payload_index` の全ファイルに 64 文字小 hex の sha256 を宣言；バリデータが内容一致を検証。 |
| **索引の存在** | 列挙された全 path がバンドルルート配下に存在；path traversal（`../`・先頭 `/`）なし。 |
| **署名の存在** | `signatures/` に少なくとも 1 つの署名ファイル；マニフェストの `signing.signatures[]` で `path` と `targets` を参照（v0.1 では targets に `manifest.json` を含む MUST）。暗号検証は v0.1 範囲外。 |
| **Hash chain** | マニフェストの `hash_chain`：`algorithm`, `head`（64 文字 hex）, `path`（`hashes/` 配下のファイル）, `covers`（v0.1 で `manifest.json` と `objects/index.json` を含む MUST）。`hash_chain.path` のファイルが存在。 |

*上記は v0.1 バンドルに対して [Validator](../validator/index.md) が検証する整合性保証の要約。Custody（保管・アクセス制御・保持）は実装定義。*

---

## 関連

- [Evidence Bundle（概要）](evidence-bundle.md)
- [Evidence Bundle ルート構造（v0.1）](../standard/current/09-evidence-bundle-structure.md)
- [Minimum Evidence Requirements](minimum-evidence.md)
- [Coverage Map（フレームワーク対応）](../coverage-map/index.md)
- [Validator](../validator/index.md)
