---
description: Evidence Bundle（v0.1）の規範的ルート構造とマニフェスト。Integrity は MUST；Custody は実装定義。
---
<!-- aimo:translation_status=translated -->

# Evidence Bundle ルート構造（v0.1）

本ページは、Evidence Bundle の**規範的**ルートレイアウトとマニフェストを定義します。Validator は、これらの要件を満たさないバンドルをスキーマ検証の前に拒否しなければなりません。

## v0.1 規範 MUST（概要）

- バンドルルートに **manifest.json** が必須。
- **object_index** と **payload_index**: 各エントリは **sha256**（64 文字小 hex）を含むこと；パスは相対で、`../` を含まずバンドルルートから脱しないこと。
- **signing.signatures** は空でない配列（空配列は無効）。
- 各署名エントリは: `signatures/` 下の **path**（パス横断禁止）、**targets**（配列、少なくとも 1 パス）、かつバンドル内の少なくとも 1 つの署名が **targets** に **manifest.json** を含むこと（manifest への署名は必須）。
- **hash_chain**: v0.1 では **algorithm**、**head**、**path**（`hashes/` 下）、**covers**（少なくとも **manifest.json** と **objects/index.json**）を含むこと。

Validator はバンドル受理前にこれらを強制します。JSON Schema と参照 Validator は同じルールを実装します。

## ルート必須構造（MUST）

バンドルルートに以下が存在すること:

| 項目 | 型 | 目的 |
| --- | --- | --- |
| **manifest.json** | ファイル | バンドルマニフェスト（下記）。バンドルの正規記述子。 |
| **objects/** | ディレクトリ | 列挙オブジェクト（メタデータ、インデックス等）。`manifest.json` の `object_index` に列挙。 |
| **payloads/** | ディレクトリ | Payload ファイル（ルート EV JSON、Evidence Pack ファイル等）。`manifest.json` の `payload_index` に列挙。 |
| **signatures/** | ディレクトリ | デジタル署名。v0.1 では manifest を参照する少なくとも 1 つの署名ファイルが必須（存在とターゲット参照；暗号検証は将来拡張）。 |
| **hashes/** | ディレクトリ | ハッシュチェーンまたは整合性記録（`manifest.json` の `hash_chain` に従う）。 |

実装者はこれらを欠くバンドルを提出してはなりません。ルート構造が不完全な場合、Validator は明確なメッセージで失敗しなければなりません。

## Integrity（規範）と Custody（実装）

- **Integrity** は v0.1 で**規範**です：標準は、バンドルが整合性メタデータ（manifest、索引ファイルの sha256、manifest への署名の存在）を持つことを要求します。Validator は以下を確認しなければなりません：
  - 必須ディレクトリ・ファイルが存在する。
  - `manifest.json` が存在し有効（スキーマおよび前スキーマチェック）。
  - `object_index` と `payload_index` に列挙された全ファイルが指定パスに存在し、内容が宣言された `sha256` と一致する。
  - `signatures/` に manifest をターゲットとする少なくとも 1 つの署名が含まれる（v0.1: 存在と参照のみ；v0.1.1: 検証メタデータを RECOMMENDED；v0.2 予定: 暗号検証をスコープに含める）。
- **Custody**（保管、アクセス制御、保持、WORM）は**実装定義**です。標準は保管者がバンドルをどう保管・保護するかは規定せず、提出時点のパッケージが上記 Integrity 要件を満たすことのみを要求します。

## manifest.json（MUST フィールド）

マニフェストは少なくとも以下を含むこと:

| フィールド | 型 | 説明 |
| --- | --- | --- |
| **bundle_id** | string (UUID) | 当該バンドルの一意識別子。 |
| **bundle_version** | string (SemVer) | バンドルのバージョン。 |
| **created_at** | string (date-time) | 作成タイムスタンプ。 |
| **scope_ref** | string | スコープ参照（例: `SC-001`）。パターン `SC-*`。 |
| **object_index** | array | オブジェクト一覧: `id`、`type`、`path`、`sha256`。パスは相対、`../` を含まず `/` で始まらず、Evidence Bundle ルート内に留まること（Validator はルート外へのパスを拒否する）。 |
| **payload_index** | array | Payload 一覧: `logical_id`、`path`、`sha256`、`mime`、`size`。object_index と同じパスルール（相対、`../` なし、先頭 `/` なし、バンドルルート内）。 |
| **hash_chain** | object | **規範 (v0.1):** `algorithm`（sha256 \| merkle）、`head`（64 文字小 hex）、`path`（`hashes/` 下の相対パス；`../` なし、先頭 `/` なし）、`covers`（配列、少なくとも 1 要素）を含むこと。v0.1 では `covers` に `manifest.json` と `objects/index.json` を含むこと。 |
| **signing** | object | **規範 (v0.1):** `signatures`（配列、少なくとも 1 エントリ）を含むこと。各エントリは: `signature_id`（例 SIG-... または UUID）、`path`（`signatures/` 下の相対；`../` なし、先頭 `/` なし）、`targets`（配列、少なくとも 1 パス；v0.1 では少なくとも 1 つの署名の targets に `manifest.json` を含む）、`algorithm`（ed25519、rsa-pss、ecdsa、unspecified のいずれか）。`created_at`（date-time）は MAY。**注:** v0.1 では署名の暗号検証はスコープ外；参照（どのファイルを何にターゲットするか）が必須。 |

**v0.1.1 オプション署名メタデータ（第三者による再実行には RECOMMENDED）:**

| フィールド | 型 | 説明 |
| --- | --- | --- |
| **signer_identity** | string | 署名者の identity（例: PGP フィンガープリント、did:key）。 |
| **signed_at** | string (date-time) | 署名が付与された時刻（ISO 8601）。 |
| **verification_command** | string | 監査人が検証を再実行するための例示 CLI コマンド。 |
| **canonicalization** | string | 署名対象 payload の正規化方法: `rfc8785_json`、`cbor`、`unspecified`。 |

Integrity と検証: **v0.1** — 参照と存在のみ。**v0.1.1** — 検証用メタデータを RECOMMENDED。**v0.2**（予定）— 暗号検証をスコープに含める。

- **sha256** 値は 64 文字の小文字十六進位でなければなりません。
- **path** は相対パスとし、`../` を含まず `/` で始まらず、Evidence Bundle ルート内に留まること。
- マニフェストは、自身の整合性がカバーされるよう、明示的な自己参照（例: `object_index` または専用フィールド）を含んでよい；Validator は、マニフェストが何らかのインデックスに列挙されているか、署名で明示的に参照されているバンドルを受け入れなければなりません。

JSON Schema: `schemas/jsonschema/evidence_bundle_manifest.schema.json` を参照。

## 将来拡張（参考）

- **Control/Requirement リンク**: 将来バージョンで、Evidence Bundle 要素を Control または Requirement 識別子にリンクする標準的な方法（例: NIST OSCAL 等へのエクスポート）を追加する可能性があります。v0.1 および v0.1.1 では不要です。

## 参考文献

- [Evidence Bundle（アーティファクト概要）](../../../artifacts/evidence-bundle/) — 目的と目次
- [EV テンプレート — External Forms と監査引き継ぎインデックス](../06-ev-template/#external-forms-official-templateschecklists-attached-as-is) — 公式テンプレート/チェックリストの添付とマニフェストでの参照方法
- [署名検証ロードマップ](../../../artifacts/signature-verification-roadmap/) — v0.1.1 メタデータと v0.2 検証計画
- [Validator](../../../validator/) — 当該構造の強制方法
- [最低証拠要件](../../../artifacts/minimum-evidence/) — MUST レベルチェックリスト
