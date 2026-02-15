---
description: Evidence Bundle Coverage Map テンプレート（v0.1）。監査向け一枚まとめ（スコープ、証跡種別、コントロール対応、除外、整合性の証明）。
---
<!-- aimo:translation_status=translated -->

# Evidence Bundle Coverage Map（テンプレート）

!!! info "参考 — 推奨プラクティス"
    本ページは、一枚の Evidence Bundle Coverage Map の**推奨プラクティステンプレート**を定義する。規格の**規範要件ではない**。バンドルがカバーする範囲としない範囲を監査引き継ぎ用に文書化する際に利用する。フレームワーク等への参照は安定しているが、採用は実装者の判断に委ねる。

---

## 1. スコープ

| 項目 | 説明 |
|------|--------------|
| **スコープ参照** | バンドルマニフェストの `scope_ref`（例: `SC-001`）。本バンドルを宣言スコープに紐づける。 |
| **Bundle ID** | `bundle_id`（UUID）— 本バンドルの一意識別子。 |
| **Bundle バージョン** | `bundle_version`（SemVer）— バンドルのバージョン。 |
| **期間 / スナップショット** | 任意：本バンドルが表す期間またはスナップショット日（例: 2026-Q1、as-of 2026-02-03）。 |

---

## 2. 証跡タイプ（EV / objects と payloads）

| カテゴリ | 内容 | v0.1 最小例 |
|----------|----------|------------------------|
| **object_index** | 列挙オブジェクト（メタデータ、索引）。各エントリ: `id`, `type`, `path`, `sha256`。 | 例: `objects/index.json`（index 型）。 |
| **payload_index** | ペイロードファイル（ルート EV JSON、Evidence Pack ファイル）。各エントリ: `logical_id`, `path`, `sha256`, `mime`, `size`。 | 例: `payloads/root.json`（ルート AIMO EV JSON）。 |
| **EV タイプ** | 証跡レコード（ルートまたはリンク先ペイロード内）— request, review, exception, renewal, change log。 | [Evidence Pack テンプレート](../../standard/current/06-ev-template/) および [Minimum Evidence Requirements](../minimum-evidence/) に整合。 |

*実装者は object_index と payload_index を拡張してよい。パスはバンドルルート内に留め、[Evidence Bundle ルート構造（v0.1）](../../standard/current/09-evidence-bundle-structure/) を満たすこと。*

---

## 3. コントロール対応（参照のみ）

外部フレームワークへの対応は**参照のみ**。規格は特定の規制への準拠を要求しない。

| フレームワーク | 本バンドルでの利用 | 参照 |
|-----------|--------------------|-----------|
| **ISO/IEC 42001** | 任意：本バンドルが対応する AI MS の観点を文書化。 | [Coverage Map → ISO 42001](../../coverage-map/iso-42001/) |
| **EU AI Act** | 任意：文書化・記録管理の高レベル対応。 | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/) |
| **NIST AI RMF** | 任意：Govern, Map, Measure, Manage の対応。 | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/) |
| **EU GPAI CoP** | 任意：Model Documentation Form。External Forms に添付し logical_id で参照。 | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/)；プロファイル `eu_gp_ai_cop.json` |
| **NIST AI RMF / GenAI** | 任意：GenAI プロファイル（AI 600-1）のアーティファクト。 | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/)；プロファイル `nist_ai_600_1_genai.json` |
| **UK ATRS** | 任意：ATRS 記録、調達評価。 | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/)；プロファイル `uk_atrs_procurement.json` |
| **JP Gov GenAI 調達** | 任意：JP 調達チェックリスト、AI Business Guidelines。 | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/)；プロファイル `jp_gov_genai_procurement.json` |
| **ISMS (27001/27002)** | 任意：変更管理、アクセス、ログ、整合性。 | [Coverage Map → ISMS](../../coverage-map/isms/) |

*「本バンドルでの利用」は提出ごとに記入。規格は特定のコントロールカバレッジを要求しない。*

### External Forms とマニフェスト参照

**External Forms**（公式テンプレート・チェックリストをそのまま添付）は、バンドルの **payload_index** に安定した `logical_id`, `path`, `sha256`, `mime`, `size` で列挙すること。監査人はマニフェストからファイルを辿りハッシュを検証できる。[EV Template — External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) および [EV Template — Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index) を参照。

---

## 4. 除外 / 前提

| 領域 | 本バンドルが**カバーしない**内容（例 — 提出ごとに調整） |
|------|-------------------------------------------------------------------------------|
| **除外** | 例：スコープ外のシステム・ユースケース、証跡のない第三者コンポーネント、本バンドルの期間外。 |
| **前提** | 例：Dictionary/タクソノミーバージョン、使用した validator/スキーマ版、保管・保持は実装定義。 |
| **制限** | 例：v0.1 では署名検証はスコープ外；規制の法解釈は行わない。 |

*プレースホルダを提出固有の除外・前提に置き換えること。*

---

## 5. 整合性証明のまとめ（v0.1）

| 要素 | 提供内容（v0.1 規範） |
|---------|----------------------------------|
| **manifest.json** | 存在しスキーマ妥当。`object_index`, `payload_index`, `hash_chain`, `signing` を含む。 |
| **sha256** | `object_index` と `payload_index` の全ファイルに 64 文字小 hex の sha256 を宣言。Validator が内容一致を検査。 |
| **索引の存在** | 列挙パスはバンドルルート配下に存在。パストラバーサル（`../` や先頭 `/`）なし。 |
| **署名の存在** | `signatures/` に少なくとも 1 つの署名ファイル。マニフェストは `signing.signatures[]` で `path` と `targets` を参照（v0.1 では targets に `manifest.json` を MUST で含む）。暗号検証は v0.1 ではスコープ外。 |
| **Hash chain** | マニフェストの `hash_chain`: `algorithm`, `head`（64 文字 hex）, `path`（`hashes/` 配下ファイル）, `covers`（v0.1 では `manifest.json` と `objects/index.json` を MUST で含む）。`hash_chain.path` のファイルが存在する。 |

*本表は [Validator](../../validator/) が v0.1 バンドルに対して検査する整合性保証の要約。Custody（保管・アクセス制御・保持）は実装定義。*

---

## Coverage Map（YAML）とプロファイル（JSON）

| アーティファクト | ステータス | 目的 |
|----------|--------|---------|
| **Coverage Map YAML**（`coverage_map/coverage_map.yaml` 等） | **参考** | AIMO 証跡・アーティファクトと外部フレームワーク（ISO 42001、NIST AI RMF、EU AI Act 等）の高レベル対応テーマ。規範的な検証要件は課さない。 |
| **Profile JSON**（`coverage_map/profiles/*.json`） | **規範** | `schemas/jsonschema/aimo-profile.schema.json` で検証する変換仕様。機械可読な対応（どの AIMO オブジェクトがどの規格条項に対応するか）を定義。[Validator](../../validator/) は `--validate-profiles` で公式プロファイル JSON がスキーマ（profile_id PR-* パターン、target 列挙、target_version、mappings）に準拠することを確認する。 |

### 公式プロファイル（Validator 検証済み）

プロファイル JSON は `coverage_map/profiles/` にあり、Validator（`--validate-profiles`）で検証される。命名: ファイル名 `<target>_<purpose>.json`。各ファイルに `target_version` を含む。

| ファイル | profile_id | target | target_version |
|------|------------|--------|----------------|
| `iso42001.json` | PR-ISO42001-v0.1 | ISO_42001 | 1.0 |
| `iso_42001_readiness.json` | PR-ISO42001-READINESS-v0.1 | ISO_42001 | 2023 |
| `nist_ai_rmf.json` | PR-NIST-AI-RMF-v0.1 | NIST_AI_RMF | 1.0 |
| `nist_ai_600_1_genai.json` | PR-NIST-AI-600-1-v0.1 | NIST_AI_600_1 | 1.0 |
| `eu_ai_act_annex_iv.json` | PR-EU-AI-ACT-ANNEX-IV-v0.1 | EU_AI_ACT_ANNEX_IV | Annex IV |
| `eu_ai_act_high_risk.json` | PR-EU-AI-ACT-HIGH-RISK-v0.1 | EU_AI_ACT_HIGH_RISK | 2024/1689 |
| `eu_gp_ai_cop.json` | PR-EU-GPAI-COP-v0.1 | EU_GPAI_COP | current |
| `uk_atrs_procurement.json` | PR-UK-ATRS-v0.1 | UK_ATRS | current |
| `jp_gov_genai_procurement.json` | PR-JP-GOV-GENAI-PROCUREMENT-v0.1 | JP_GOV_GENAI_PROCUREMENT | current |

### プロファイル更新ポリシー

- **EU AI Act 参照（0.1.2）**: 証跡準備の一貫性のため、Coverage Map およびドキュメント内の EU AI Act の条文参照を規則 (EU) 2024/1689 に合わせた。参考であり法解釈ではない。
- **ISO 42001 / NIST AI RMF**: 対象フレームワークの新バージョンは、将来の規格バージョンで新プロファイルファイルまたは新 `target_version` として追加可能。v0.1 プロファイルは v0.1 リリースで固定。
- **EU AI Act Annex IV**: Annex IV および関連条文は規制当局により更新され得る。プロファイルの対応は **PATCH**（例: 0.1.x）で文言・条項変更に追随し、同一 profile_id で継続可能。実装者はプロファイルの `target_version` およびリリースノートで参照される版に合わせること。

---

## 関連

- [Evidence Bundle（アーティファクト概要）](../evidence-bundle/)
- [Evidence Bundle ルート構造（v0.1）](../../standard/current/09-evidence-bundle-structure/)
- [Minimum Evidence Requirements](../minimum-evidence/)
- [Coverage Map（フレームワーク対応）](../../coverage-map/)
- [Validator](../../validator/)
