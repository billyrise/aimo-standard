---
description: Coverage Map方法論 - AIMOが外部フレームワークにマッピングする方法。監査での使用法、Evidence Bundleとの関係、対応関係アプローチ。
---

# Methodology

> 注：本Methodologyは対応関係（traceability）と証跡準備を支援します。特定規制・規格への準拠を保証するものではありません。

本ページでは、Coverage Map の位置づけ、監査での利用方法、Evidence Bundle および Minimum Evidence Requirements との関係を説明する。

## What the mapping is

- 外部フレームワーク・規制の参照（トピック別）から、AIMO の証跡、Evidence Bundle TOC 項目、Minimum Evidence のライフサイクルグループ、アーティファクト、バリデータチェックへの**情報提供**用マッピング。
- **説明可能性**のための支援：どの AIMO 証跡・アーティファクトが、ある外部要求への対応の説明に役立つかを示す（適合の主張はしない）。

## What the mapping is not

- いかなるフレームワーク・規制への**適合を保証するものではない**。
- **法的助言**ではなく、権威ある条文との照合に代わるものではない。
- **網羅的**ではなく、監査対応と説明可能性のための実務的なサブセットである。

## Audit questions（v0.1.1）

v0.1.1 から、マッピングに **audit_questions**（監査で想定される質問例）を付与できる。これらは**説明用**であり、保証・適合保証・網羅的監査プログラムを構成するものではない。読者は権威ある条文と照合し、専門家の判断を適用すること。

## How to use it in audit

**要求 → 証跡 → アーティファクト → 検証** の流れで利用する。

1. **要求**: 外部フレームワークの参照とトピックを特定する（例: ISO 42001 の文書化、EU AI Act の記録保持）。
2. **証跡**: その要求の説明可能性を支える AIMO Evidence Bundle 項目と Minimum Evidence ライフサイクルグループ（request, review, exception, renewal, change_log, integrity）を確認する。
3. **アーティファクト**: その証跡を実装または例示するアーティファクト（スキーマ、テンプレート、例）を特定する。
4. **検証**: 参照されたバリデータ・スキーマチェックで構造の整合性を確認する。

読者は各フレームワーク・規制の権威ある条文と照合すること。

## Relationship to Evidence Bundle and Minimum Evidence Requirements

- **[Evidence Bundle](../artifacts/evidence-bundle.md)**: バンドル構造、TOC、追跡可能性を定義する。Coverage Map の行は Evidence Bundle のセクション（EV, Dictionary, Summary, change_log, request, review, exception, renewal）を参照する。
- **[Minimum Evidence Requirements](../artifacts/minimum-evidence.md)**: MUST レベルのライフサイクルグループ（request, review, exception, renewal, change_log, integrity）を定義する。Coverage Map の行は `minimum_evidence_refs` でこれらのグループを参照する。

ある外部要求について、どの Evidence Bundle 項目と Minimum Evidence グループが説明可能性を支えるかは、Coverage Map で確認する。

## 非過剰主張ステートメント

!!! warning "重要"
    AIMO Standard は**説明可能性と証跡準備**を支援する。法的助言の提供、適合の保証、いかなる規制・フレームワークへの適合認証も**行わない**。採用者は権威ある条文と照合し、適切に専門家の助言を得ること。

スコープ、前提条件、採用者責任は [責任境界](../governance/responsibility-boundary.md) を参照。

## 監査ジャーニー

本ページから以下へ続く：

1. **フレームワーク対応表**: [ISO 42001](iso-42001.md)、[NIST AI RMF](nist-ai-rmf.md)、[EU AI Act](eu-ai-act.md)、[ISMS](isms.md)
2. **検証**: [Validator](../validator/index.md) — 構造チェックを実行
3. **ダウンロード**: [Releases](../../releases/) — リリースアセットを取得
