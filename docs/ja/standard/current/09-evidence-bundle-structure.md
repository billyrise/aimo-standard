---
description: Evidence Bundle（v0.1）の規範的ルート構造とマニフェスト。Integrity は MUST、Custody は実装側。
---

# Evidence Bundle ルート構造（v0.1）

本ページは Evidence Bundle の**規範的**ルート構成とマニフェストを定義する。バリデータは、これらの要件を満たさないバンドルをスキーマ検証の前に拒否しなければならない。

## ルート必須構成（MUST）

バンドルルートに以下が存在することは MUST とする。

| 項目 | 種別 | 目的 |
|------|------|------|
| **manifest.json** | ファイル | バンドルマニフェスト（後述）。正規の記述子。 |
| **objects/** | ディレクトリ | 列挙オブジェクト（メタデータ・索引等）。manifest.json の object_index に列挙。 |
| **payloads/** | ディレクトリ | ペイロード（ルート EV JSON、Evidence Pack 等）。payload_index に列挙。 |
| **signatures/** | ディレクトリ | デジタル署名。v0.1 ではマニフェストを参照する署名ファイルが少なくとも1つ存在することは MUST（存在と対象参照；暗号検証は将来拡張）。 |
| **hashes/** | ディレクトリ | ハッシュチェーンまたは整合性記録（manifest の hash_chain に従う）。 |

提出時、上記のいずれかが欠けているバンドルは MUST NOT とする。バリデータはルート構成が不完全な場合、明確なメッセージで失敗することは MUST とする。

## Integrity（規範）と Custody（実装側）

- **Integrity** は v0.1 で**規範**とする：マニフェスト、索引ファイルの sha256、マニフェストに対する署名の存在を必須とする。バリデータは以下をチェックすることは MUST とする：必須ディレクトリ・ファイルの存在、manifest.json の存在と有効性、object_index / payload_index に列挙された全ファイルの存在と sha256 一致、signatures/ にマニフェストを対象とする署名が少なくとも1つ存在すること（v0.1 では存在と参照のみ；検証は v0.1 の範囲外）。
- **Custody**（保管・アクセス制御・保持）は**実装側**で定義する。標準は保管方法を規定しない。提出時点で Integrity 要件を満たすことを要求する。

## manifest.json（MUST 項目）

マニフェストには少なくとも以下を含めること（MUST）。

| フィールド | 型 | 説明 |
|------------|-----|------|
| **bundle_id** | string (UUID) | バンドル一意識別子。 |
| **bundle_version** | string (SemVer) | バンドルバージョン。 |
| **created_at** | string (date-time) | 作成日時。 |
| **scope_ref** | string | スコープ参照（例 SC-001）。パターン SC-*。 |
| **object_index** | array | オブジェクト一覧：id, type, path, sha256。path は相対パスで ../ 禁止。 |
| **payload_index** | array | ペイロード一覧：logical_id, path, sha256, mime, size。同様の path 規則。 |
| **hash_chain** | object | チェーン先頭と方式（sha256, merkle 等）。 |
| **signing** | object | 署名方式（将来拡張）。v0.1 では signatures/ にマニフェストを参照する署名が1つ以上必須。 |

- **sha256** は 64 文字の小 hex であること（MUST）。
- **path** は相対パスで、`../` を含んではならない（MUST）。

JSON Schema: `schemas/jsonschema/evidence_bundle_manifest.schema.json` を参照。

## 関連

- [Evidence Bundle（概要）](../../artifacts/evidence-bundle.md)
- [Validator](../../validator/index.md)
- [Minimum Evidence Requirements](../../artifacts/minimum-evidence.md)
