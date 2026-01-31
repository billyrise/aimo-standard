# Methodology

本ページでは、Coverage Map の位置づけ、監査での利用方法、Evidence Bundle および Minimum Evidence Requirements との関係を説明する。

## What the mapping is

- 外部フレームワーク・規制の参照（トピック別）から、AIMO の証跡、Evidence Bundle TOC 項目、Minimum Evidence のライフサイクルグループ、アーティファクト、バリデータチェックへの**情報提供**用マッピング。
- **説明可能性**のための支援：どの AIMO 証跡・アーティファクトが、ある外部要求への対応の説明に役立つかを示す（適合の主張はしない）。
- 単一の信頼できる情報源（SSOT）: リポジトリの `coverage_map/coverage_map.yaml`。ドキュメントの表はこれに基づく。更新時は両方を同期する。

## What the mapping is not

- いかなるフレームワーク・規制への**適合を保証するものではない**。
- **法的助言**ではなく、権威ある条文との照合に代わるものではない。
- **網羅的**ではなく、監査対応と説明可能性のための実務的なサブセットである。

## How to use it in audit

**要求 → 証跡 → アーティファクト → 検証** の流れで利用する。

1. **要求**: 外部フレームワークの参照とトピックを特定する（例: ISO 42001 の文書化、EU AI Act の記録保持）。
2. **証跡**: その要求の説明可能性を支える AIMO Evidence Bundle 項目と Minimum Evidence ライフサイクルグループ（request, review, exception, renewal, change_log, integrity）を確認する。
3. **アーティファクト**: その証跡を実装または例示するアーティファクト（スキーマ、テンプレート、例）を特定する。
4. **検証**: 参照されたバリデータ・スキーマチェックで構造の整合性を確認する。

読者は各フレームワーク・規制の権威ある条文と照合すること。

## Update policy

- マッピングデータは、AIMO の証跡・アーティファクトまたはフレームワークの解釈が変わったときに更新する。
- 更新時はまず `coverage_map/coverage_map.yaml` を変更し、次にフレームワーク別ドキュメントの表を SSOT と整合するよう更新する。

## Relationship to Evidence Bundle and Minimum Evidence Requirements

- **[Evidence Bundle](../artifacts/evidence-bundle.md)**: バンドル構造、TOC、追跡可能性を定義する。Coverage Map の行は Evidence Bundle のセクション（EV, Dictionary, Summary, change_log, request, review, exception, renewal）を参照する。
- **[Minimum Evidence Requirements](../artifacts/minimum-evidence.md)**: MUST レベルのライフサイクルグループ（request, review, exception, renewal, change_log, integrity）を定義する。Coverage Map の行は `minimum_evidence_refs` でこれらのグループを参照する。

ある外部要求について、どの Evidence Bundle 項目と Minimum Evidence グループが説明可能性を支えるかは、Coverage Map で確認する。
