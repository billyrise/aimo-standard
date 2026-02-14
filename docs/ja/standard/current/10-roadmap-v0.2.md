---
description: v0.2 の情報提供用ロードマップ。監査オブジェクト SSOT、Evidence-as-Code、出力プロファイル、Test ライブラリ、ライフサイクル、JNC。
---

# v0.2 ロードマップ（情報提供）

本ページは**将来のメジャー版**（v0.2）の計画方針をまとめる。**情報提供**のみ。各リリースの規範は当該バージョンの標準とスキーマによる。目標時期：2026 Q4–2027。

## 計画テーマ

| テーマ | 概要 |
|--------|------|
| **監査オブジェクトモデル（SSOT）** | Requirement, Control, Claim, Evidence, Test, Finding, Remediation, Approval, Scope, VersionChange を規範オブジェクトとして固定 ID と参照整合で定義。 |
| **外部フレームワークブリッジ** | EU Annex IV、GPAI Form、ISO 42001、NIST AI RMF 向け出力プロファイル。機械可読マッピングとオプションのワンクリックエクスポート。 |
| **Evidence-as-Code** | 整合性の規範化：署名検証、プロビナンス（SLSA 風）、再現性・変更追跡。 |
| **Test 手順ライブラリ** | 統制ごとの標準テストテンプレート。ISAE 3000、SOC 2、ISO 19011 との整合。 |
| **運用ライフサイクル** | イベント駆動プロセス（Intake → Review → Exception → Renewal → Change → Decommission）と必須ログ・証跡。 |
| **業界・法域プロファイル** | 業種・法域別のオプションプロファイル。 |
| **Justified Non-Compliance（JNC）** | 意図的な不適合の記録・正当化のオプション機構（情報提供）。 |
| **OSCAL 連携** | Evidence Bundle から Control/Requirement への標準的リンク方式（NIST OSCAL 等へのエクスポート用）。 |

## 参照

- [v0.1 オブジェクトモデルスコープ](https://github.com/billyrise/aimo-standard/blob/main/source_pack/07_release/v0.1_object_model_scope.md)
- [署名検証ロードマップ](../../artifacts/signature-verification-roadmap.md)
- [Releases](../../../releases/)
