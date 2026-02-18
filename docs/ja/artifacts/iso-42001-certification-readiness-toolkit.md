---
description: ISO/IEC 42001 認証準備ツールキット。AIMO アーティファクトで ISO 42001 に整合した監査可能エビデンスへの最短パス。準備支援のみ；認証を付与しない。
---
<!-- aimo:translation_status=translated -->

# ISO/IEC 42001 Certification Readiness Toolkit

本ページは、AIMO アーティファクトを用いて **ISO/IEC 42001** に整合した**監査可能エビデンス**を整えるための**実務的・採用志向**ガイドです。**準備を支援**するものであり、認証を**付与しません**。認証決定は**認定認証機関**が行います。

## Goal

ISO/IEC 42001 型コントロール（コンテキスト、リーダーシップ、計画、支援、運用、パフォーマンス評価、改善）を支える、バリデータチェック済みの Evidence Bundle を整え、監査人が効率的にエビデンスを特定・検証できるようにする。

## 5-step workflow

| Step | Action |
| --- | --- |
| **1. Establish scope and AI inventory** | scope_ref でスコープを定義；[taxonomy](../../standard/current/03-taxonomy/) と [dictionary](../../standard/current/05-dictionary/) で AI システムを分類。 |
| **2. Set management-system artifacts** | 方針・役割・PDCA に沿ったアーティファクトを作成または参照。[AIMO-MS / AIMO-Controls](../../conformance/) を構造に；[Evidence Pack Template](../../standard/current/06-ev-template/) (EP-01..EP-07) を参照。 |
| **3. Produce Evidence Bundle + minimum evidence** | [Evidence Bundle structure](../../standard/current/09-evidence-bundle-structure/) に従い manifest, object_index, payload_index, hash_chain, signing を構築。[Minimum Evidence Requirements](minimum-evidence.md) に従い request, review, exception, renewal, change_log を含める。 |
| **4. Run validator + checksums + change control** | `python validator/src/validate.py <bundle_path> --validate-profiles` を実行。バリデータ版と出力を記録。SHA-256 チェックサムを生成；影響オブジェクトを参照する change log を維持。 |
| **5. Prepare audit pack** | バンドルをパッケージ（zip 等）；チェックサムを提供。[audit report output](../../standard/current/07-validator/) (audit-json / audit-html) を任意で添付。標準引用時はバージョン付き URL（例 `/0.1.2/`）を使用。Audit-Ready レベルでは [Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index) と [External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) を追加。 |

## Checklist: ISO 42001 clause family → AIMO artifacts → evidence outputs

（EN 版と同じ表を参照: [Coverage Map — ISO/IEC 42001](../../coverage-map/iso-42001/) および [ISO/IEC 42006](https://www.iso.org/standard/42006)）

## Safe language

- **Use:** "We use AIMO artifacts to support ISO/IEC 42001 readiness; certification decisions remain with accredited certification bodies."
- **Do not use:** "ISO 42001 certified by AIMO" or "AIMO certifies compliance."

一次ソース（公式規格）: [ISO/IEC 42001:2023](https://www.iso.org/standard/42001)（ISO）。本ツールキットは [Conformance](../../conformance/) および [Responsibility Boundary](../../governance/responsibility-boundary/) と整合しており、AIMO は認証も適合保証も行いません。

## Related

- [Conformance](../../conformance/) — Levels (Foundation, Operational, Audit-Ready) and claim language
- [Trust Package](../../governance/trust-package/) — Auditor-ready materials
- [Responsibility Boundary](../../governance/responsibility-boundary/) — What AIMO does and does not provide
