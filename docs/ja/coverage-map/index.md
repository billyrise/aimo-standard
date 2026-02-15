---
description: AIMO Coverage Map - AIMO Standardと主要規制（ISO 42001、NIST AI RMF、EU AI Act、ISMS）間の対応関係で監査準備を支援。
---
<!-- aimo:translation_status=translated -->

# Coverage Map

## 重要：本Coverage Mapの位置づけ（準拠保証ではありません）

本Coverage Mapは、AIMO Standardの要素と主要規制・規格要求との**対応関係（traceability）**を示し、監査説明と証跡準備（evidence readiness）を効率化するための資料です。
**特定規制・規格への準拠（compliance）を自動的に保証するものではありません。**
適用義務は、役割（提供者/利用者等）、用途、リスク分類、移行期間、および各当局・認証スキームの解釈により変動します。

## 本マップの使い方（traceabilityの流れ）

1. 外部要求（ISO/NIST/EU AI Act/ISMS等）から出発し、対応するAIMO Standard要素を辿ります。
2. 対応するAIMO要素から、必要な提出物（Artifacts）と最低限の証跡要件（Minimum Evidence）を特定します。
3. Validatorで欠落・整合性を検査し、人の判断が必要な箇所は監督プロトコルに従ってレビューします（[人による監督プロトコル](../governance/human-oversight-protocol/)参照）。

**主要リソース:**

- [Taxonomy](../standard/current/03-taxonomy/) — 分類コード
- [Minimum Evidence Requirements](../artifacts/minimum-evidence/) — MUST レベルチェックリスト
- [Evidence Bundle](../artifacts/evidence-bundle/) — バンドル構造と TOC
- [ログスキーマ](../artifacts/log-schemas/) — Shadow AI / エージェント活動証跡
- [Validator](../validator/) — 構造整合性チェック
- [人による監督プロトコル](../governance/human-oversight-protocol/) — 機械と人の判断の責任境界

---

本セクションは、監査での説明可能性のため、AIMO Standard の証跡・アーティファクトと外部フレームワーク・規制の対応を示す。適合の保証や法的助言は**行わない**。

- **[Methodology](methodology/)**: マッピングの位置づけと利用方法、更新ポリシー、[Evidence Bundle](../artifacts/evidence-bundle/)・[Minimum Evidence Requirements](../artifacts/minimum-evidence/) との関係。
- **ISO/IEC 42001**: [ISO/IEC 42001 対応表](iso-42001/) — AIマネジメントシステムの観点。
- **ISO/IEC 42006**: [ISO/IEC 42006 対応表](iso-42006/) — AIMS の監査・認証を行う機関の要件（ISO/IEC 42001 準拠）。
- **NIST AI RMF**: [NIST AI RMF 対応表](nist-ai-rmf/) — Govern, Map, Measure, Manage。
- **EU AI Act**: [EU AI Act 対応表](eu-ai-act/) — 文書化・記録管理の概要（法解釈ではない）。
- **調達・開示（英国・日本）**: [調達・開示対応表](procurement-and-disclosure/) — 公共調達と開示（英国・日本）；参照用マッピングのみ。
- **ISMS 観点**: [ISMS 対応表](isms/) — ISO/IEC 27001/27002 の観点（変更管理、アクセス制御、ログ、証跡の完全性）。
