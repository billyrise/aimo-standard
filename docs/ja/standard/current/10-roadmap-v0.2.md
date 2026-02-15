---
description: v0.2 の参考ロードマップ。監査オブジェクト SSOT、Evidence-as-Code、出力プロファイル、テストライブラリ、ライフサイクル、JNC。
---
<!-- aimo:translation_status=translated -->

# v0.2 ロードマップ（参考）

本ページは、**将来のメジャーバージョン**（v0.2）の計画方向をまとめます。**参考**であり、各リリースの規範は当該バージョンの標準とスキーマです。目標時期: 2026 Q4–2027。

## 計画テーマ

| テーマ | 概要 |
| --- | --- |
| **監査オブジェクトモデル（SSOT）** | Requirement、Control、Claim、Evidence、Test、Finding、Remediation、Approval、Scope、VersionChange を固定 ID と参照整合性を持つ規範オブジェクトとして定義。 |
| **外部フレームワークブリッジ** | EU 附属書 IV、GPAI フォーム、ISO 42001、NIST AI RMF 向け出力プロファイル；機械可読マッピングとオプションのワンクリックエクスポート。 |
| **Evidence-as-Code** | 規範的整合性：署名検証、プロベナンス（SLSA 型等）、再現性と変更追跡。 |
| **テスト手順ライブラリ** | コントロール別標準テストテンプレート；ISAE 3000、SOC 2、ISO 19011 との整合。 |
| **運用ライフサイクル** | イベント駆動プロセス（Intake → Review → Exception → Renewal → Change → Decommission）と必須ログ・エビデンス。 |
| **業界・法域プロファイル** | セクター・法域別のオプションプロファイル。 |
| **正当化された不適合（JNC）** | 意図的な不適合を記録・正当化するオプション機構（参考）。 |
| **OSCAL 連携** | Evidence Bundle を Control/Requirement にリンクし NIST OSCAL 等へエクスポートする標準的な方法。 |

## 参考文献

- [v0.1 オブジェクトモデルスコープ](https://github.com/billyrise/aimo-standard/blob/main/source_pack/07_release/v0.1_object_model_scope.md) — v0.1 MUST と予約
- [署名検証ロードマップ](../../../artifacts/signature-verification-roadmap/) — 署名・検証の進化
- [Releases](../../../releases/) — リリース資産と changelog
