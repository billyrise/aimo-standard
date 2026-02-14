---
description: AIMO（AI Management Office）Standard - AIガバナンスと監査のためのオープン標準。8次元91コードのタクソノミーでAI利用を分類し、証跡要件とバリデーターで企業コンプライアンスを支援。
---

# AIMO Standard

**AIMO** は **AI Management Office**（AI マネジメントオフィス）の略称です。本サイトは AIMO Standard の仕様を公開します。

## なぜ今、Agentic AI監査が必要か

企業のAIリスクは、**「未承認AI（Shadow AI）」の拡大**と、**「自律エージェント（Agentic AI）」の権限暴走**により、従来のISMS/IT統制だけでは追跡・説明が困難になっています。
AIMO Standardは、AI利用を共通言語（Taxonomy）で分類し、証跡（Evidence）を最小要件で揃え、Validatorで整合性を担保することで、監査説明と是正を加速します。
※本標準は法的助言や特定規制・規格への準拠保証を提供するものではありません（[Coverage Map](coverage-map/index.md)を参照してください）。

- [Taxonomy](standard/current/03-taxonomy.md)（共通言語で分類する）
- [Minimum Evidence Requirements](artifacts/minimum-evidence.md)（最低限の証跡要件）
- [Validator](validator/index.md)（整合性チェック）

**トップレベルセクション**

1. [Standard](standard/index.md) — 仕様（[Current](standard/current/index.md) | [Versions](standard/versions/index.md)）、[Conformance](conformance/index.md)、[Coverage Map](coverage-map/index.md)
2. [Artifacts](artifacts/index.md) — タクソノミー、コード体系、辞書、証跡テンプレート、スキーマ
3. [Validator](validator/index.md) — ルール、参照チェック、実行方法
4. [Examples](examples/index.md) — エンドツーエンド・最小サンプル
5. [Releases](releases/) — Changelog、移行、チェックサム、PDF
6. [Governance](governance/index.md) — バージョニング、セキュリティ、ライセンス、商標、[Contributing](contributing/localization.md)

**対象者別クイックリンク**

- **監査向け**: [Trust Package](governance/trust-package.md)、[タクソノミー](standard/current/03-taxonomy.md)、[辞書](standard/current/05-dictionary.md)、[Evidence Bundle](artifacts/evidence-bundle.md)、[Minimum Evidence Requirements](artifacts/minimum-evidence.md)、[Coverage Map](coverage-map/index.md)、[Validator](validator/index.md)、[Releases](releases/)
- **セキュリティ向け**: [Trust Package](governance/trust-package.md)、[タクソノミー](standard/current/03-taxonomy.md)、[Minimum Evidence Requirements](artifacts/minimum-evidence.md)、[責任境界](governance/responsibility-boundary.md)、[Governance](governance/index.md)、[Validator](validator/index.md)、[Standard > EV Template](standard/current/06-ev-template.md)
- **IT運用向け**: [Trust Package](governance/trust-package.md)、[タクソノミー](standard/current/03-taxonomy.md)、[Minimum Evidence Requirements](artifacts/minimum-evidence.md)、[Releases](releases/)、[Validator](validator/index.md)、[Examples](examples/index.md)、[Conformance](conformance/index.md)
- **法務/調達向け**: [Trust Package](governance/trust-package.md)、[責任境界](governance/responsibility-boundary.md)、[Coverage Map Methodology](coverage-map/methodology.md)、[Releases](releases/)、[Governance](governance/index.md)（ライセンス、商標）

**監査ジャーニー**（2クリックパス）：

1. [Trust Package](governance/trust-package.md) — 監査対応資料のスタート地点
2. [タクソノミー](standard/current/03-taxonomy.md) + [辞書](standard/current/05-dictionary.md) — 8次元コード体系を理解
3. [Evidence Bundle](artifacts/evidence-bundle.md) — 構造と TOC
4. [Minimum Evidence Requirements](artifacts/minimum-evidence.md) — MUST レベルチェックリスト
5. [Coverage Map](coverage-map/index.md) + [Methodology](coverage-map/methodology.md) — フレームワーク対応
6. [Validator](validator/index.md) — 構造チェックを実行
7. [Releases](releases/) — アセットをダウンロードして検証
