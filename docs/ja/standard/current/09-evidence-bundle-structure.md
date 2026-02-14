---
description: Evidence Bundle（v0.1）の規範的ルート構造とマニフェスト。Integrity は MUST、Custody は実装側。
---

# Evidence Bundle ルート構造（v0.1）

本ページは Evidence Bundle の**規範的**ルート構成とマニフェストを定義する。バリデータは、これらの要件を満たさないバンドルをスキーマ検証の前に拒否しなければならない。

## v0.1 規範 MUST（まとめ）

- バンドルルートに **manifest.json** が存在することは必須。
- **object_index** と **payload_index**：各エントリに **sha256**（64 文字小 hex）が必須。path は相対で `../` 禁止・ルート外参照禁止。
- **signing.signatures** は空でない配列であること（空配列は無効）。
- 各署名エントリは **path**（signatures/ 配下、パストラバーサル禁止）、**targets**（配列・最低1要素）を持ち、バンドル内の少なくとも1件の署名が **targets** に **manifest.json** を含むこと（マニフェスト署名は必須）。
- **hash_chain**：v0.1 では **algorithm**、**head**、**path**（hashes/ 配下）、**covers**（少なくとも **manifest.json** と **objects/index.json**）を必須とする。

バリデータはこれらを満たさないバンドルを拒否すること（MUST）。JSON Schema および参照バリデータは同一ルールを実装する。

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

- **Integrity** は v0.1 で**規範**とする：マニフェスト、索引ファイルの sha256、マニフェストに対する署名の存在を必須とする。バリデータは以下をチェックすることは MUST とする：必須ディレクトリ・ファイルの存在、manifest.json の存在と有効性、object_index / payload_index に列挙された全ファイルの存在と sha256 一致、signatures/ にマニフェストを対象とする署名が少なくとも1つ存在すること（v0.1：存在と参照のみ；v0.1.1：検証用メタデータは RECOMMENDED；v0.2 予定：暗号学的検証をスコープに含める）。
- **Custody**（保管・アクセス制御・保持）は**実装側**で定義する。標準は保管方法を規定しない。提出時点で Integrity 要件を満たすことを要求する。

## manifest.json（MUST 項目）

マニフェストには少なくとも以下を含めること（MUST）。

| フィールド | 型 | 説明 |
|------------|-----|------|
| **bundle_id** | string (UUID) | バンドル一意識別子。 |
| **bundle_version** | string (SemVer) | バンドルバージョン。 |
| **created_at** | string (date-time) | 作成日時。 |
| **scope_ref** | string | スコープ参照（例 SC-001）。パターン SC-*。 |
| **object_index** | array | オブジェクト一覧：id, type, path, sha256。path は相対パスで `../` および先頭 `/` 禁止。Evidence Bundle ルート外を指してはならず、バリデータはルート外へのパスを拒否すること（MUST）。 |
| **payload_index** | array | ペイロード一覧：logical_id, path, sha256, mime, size。object_index と同様の path 規則（相対、`../` 禁止、先頭 `/` 禁止、バンドル内）。 |
| **hash_chain** | object | **規範（v0.1）：** `algorithm`（sha256 \| merkle）、`head`（64 文字小 hex）、`path`（hashes/ 配下の相対パス；`../` 禁止・先頭 `/` 禁止）、`covers`（配列・最低1要素）を必須とする。v0.1 では `covers` に `manifest.json` と `objects/index.json` を含めること（MUST）。 |
| **signing** | object | **規範（v0.1）：** `signatures`（配列・最低1要素）を必須とする。各要素は MUST：`signature_id`（例 SIG-... または UUID）、`path`（signatures/ 配下の相対パス；`../` 禁止・先頭 `/` 禁止）、`targets`（配列・最低1要素；v0.1 では少なくとも1つの署名の targets に `manifest.json` を含めること）、`algorithm`（ed25519 \| rsa-pss \| ecdsa \| unspecified のいずれか）。`created_at`（date-time）は MAY。**注記：** 署名の暗号検証は v0.1 の範囲外とする。参照（どのファイルを指し、何を対象とするか）は v0.1 で必須。 |

**v0.1.1 オプション署名メタデータ（第三者による再実施のため RECOMMENDED）：**

| フィールド | 型 | 説明 |
|------------|------|------|
| **signer_identity** | string | 署名者識別（例 PGP フィンガープリント、did:key）。 |
| **signed_at** | string (date-time) | 署名適用日時（ISO 8601）。 |
| **verification_command** | string | 監査人が再検証するための例示 CLI コマンド。 |
| **canonicalization** | string | 署名対象ペイロードの正規化方式：`rfc8785_json`、`cbor`、`unspecified`。 |

Integrity と検証：**v0.1** — 参照と存在のみ。**v0.1.1** — 検証用メタデータは RECOMMENDED。**v0.2**（予定）— 暗号学的検証をスコープに含める。

- **sha256** は 64 文字の小 hex であること（MUST）。
- **path** は相対パスとし、`../` および先頭 `/` を含んではならない（MUST）。パスは Evidence Bundle ルート内に留まること（MUST）。

JSON Schema: `schemas/jsonschema/evidence_bundle_manifest.schema.json` を参照。

## 将来拡張（情報提供）

- **Control/Requirement リンク**: 将来バージョンで、Evidence Bundle 要素を Control または Requirement 識別子へリンクする標準方式を追加する可能性がある（例：NIST OSCAL 等へのエクスポート用）。v0.1 および v0.1.1 では不要。

## 関連

- [Evidence Bundle（概要）](../../../artifacts/evidence-bundle/)
- [署名検証ロードマップ](../../../artifacts/signature-verification-roadmap/)
- [Validator](../../../validator/)
- [Minimum Evidence Requirements](../../../artifacts/minimum-evidence/)
