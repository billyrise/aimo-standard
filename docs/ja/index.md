---
description: AIMO（AI Management Office）Standard - AIガバナンスと監査のためのオープン標準。8次元91コードのタクソノミーでAI利用を分類し、証跡要件とバリデーターで企業コンプライアンスを支援。
---
<!-- aimo:translation_status=translated -->

# AIMO Standard

**AIMO** は **AI Management Office**（AI マネジメントオフィス）の略称です。本サイトは AIMO Standard の仕様を公開します。

## なぜ今、Agentic AI監査が必要か

企業のAIリスクは、**「未承認AI（Shadow AI）」の拡大**と、**「自律エージェント（Agentic AI）」の権限暴走**により、従来のISMS/IT統制だけでは追跡・説明が困難になっています。
AIMO Standardは、AI利用を共通言語（Taxonomy）で分類し、証跡（Evidence）を最小要件で揃え、Validatorで整合性を担保することで、監査説明と是正を加速します。
※本標準は法的助言や特定規制・規格への準拠保証を提供するものではありません（[Coverage Map](coverage-map/)を参照してください）。

- [Taxonomy](standard/current/03-taxonomy/)（共通言語で分類する）
- [Minimum Evidence Requirements](artifacts/minimum-evidence/)（最低限の証跡要件）
- [Validator](validator/)（整合性チェック）

**トップレベルセクション**

1. [Standard](standard/) — 仕様（[Current](standard/current/) | [Versions](standard/versions/)）、[Conformance](conformance/)、[Coverage Map](coverage-map/)
2. [Artifacts](artifacts/) — タクソノミー、コード体系、辞書、証跡テンプレート、スキーマ
3. [Validator](validator/) — ルール、参照チェック、実行方法
4. [Examples](examples/) — エンドツーエンド・最小サンプル
5. [Releases](releases/) — Changelog、移行、チェックサム、PDF
6. [Governance](governance/) — バージョニング、セキュリティ、ライセンス、商標、[Contributing](contributing/localization/)

**対象者別クイックリンク**

- **監査向け**: [Trust Package](governance/trust-package/)、[タクソノミー](standard/current/03-taxonomy/)、[辞書](standard/current/05-dictionary/)、[Evidence Bundle](artifacts/evidence-bundle/)、[Minimum Evidence Requirements](artifacts/minimum-evidence/)、[Coverage Map](coverage-map/)、[Validator](validator/)、[Releases](releases/)
- **セキュリティ向け**: [Trust Package](governance/trust-package/)、[タクソノミー](standard/current/03-taxonomy/)、[Minimum Evidence Requirements](artifacts/minimum-evidence/)、[責任境界](governance/responsibility-boundary/)、[Governance](governance/)、[Validator](validator/)、[Standard > EV Template](standard/current/06-ev-template/)
- **IT運用向け**: [Trust Package](governance/trust-package/)、[タクソノミー](standard/current/03-taxonomy/)、[Minimum Evidence Requirements](artifacts/minimum-evidence/)、[Releases](releases/)、[Validator](validator/)、[Examples](examples/)、[Conformance](conformance/)
- **法務/調達向け**: [Trust Package](governance/trust-package/)、[責任境界](governance/responsibility-boundary/)、[Coverage Map Methodology](coverage-map/methodology/)、[Releases](releases/)、[Governance](governance/)（ライセンス、商標）

**監査ジャーニー**（2クリックパス）：

1. [Trust Package](governance/trust-package/) — 監査対応資料のスタート地点
2. [タクソノミー](standard/current/03-taxonomy/) + [辞書](standard/current/05-dictionary/) — 8次元コード体系を理解
3. [Evidence Bundle](artifacts/evidence-bundle/) — 構造と TOC
4. [Minimum Evidence Requirements](artifacts/minimum-evidence/) — MUST レベルチェックリスト
5. [Coverage Map](coverage-map/) + [Methodology](coverage-map/methodology/) — フレームワーク対応
6. [Validator](validator/) — 構造チェックを実行
7. [Releases](releases/) — アセットをダウンロードして検証
