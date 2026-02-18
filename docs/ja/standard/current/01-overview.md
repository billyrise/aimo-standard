---
description: AIMO Standard の概要。AIガバナンス監査のための共通タクソノミー、コード体系、辞書、証跡テンプレート、Validator チェックを定義。
---
<!-- aimo:translation_status=translated -->

# 概要（Overview）

**AIMO** は **AI Management Office** を表します。AIMO Standard は以下を定義します：
- 共通タクソノミー
- コード体系
- 初期辞書
- EV テンプレート
- Validator チェック（仕様＋最小参照実装）

本リポジトリは以下を公開します：
- 人間可読な仕様（HTML）
- 機械可読なアーティファクト（スキーマ／テンプレート／例）
- 公式 PDF リリース

## 位置づけ：ISO/IEC 42001（AIMS）のコンパニオン

AIMO Standard は、**証跡準備と説明可能性のための実装アクセラレータ**であり、ISO/IEC 42001 に整合した AI マネジメントシステム（AIMS）の支援と監査可能な証跡の構造化に利用できます。ISO/IEC 42001 や他のマネジメントシステム規格に**取って代わるものではなく**、タクソノミー、Evidence Bundle 構造、Coverage Map を追加し、それらのコントロールの運用化と証跡化を支援します。

**AIMO が提供するもの**

- AI ガバナンス分類のためのタクソノミーとコード体系
- Evidence Bundle 構造（manifest、object_index、payload_index、整合性）
- 追跡可能性のための Validator と Coverage Map
- 適合レベル（Foundation、Operational、Audit-Ready）— 証跡パッケージングの AIMO 独自成熟度段階

**AIMO が提供しないもの**

- 法的助言
- ISO 認証または認証の代替
- 規制適合の保証
- 監査人判断や認定認証機関の代替

**なぜ今か**

- **ISO/IEC 42006**（2025-07 発行）は、ISO/IEC 42001 に基づく AI マネジメントシステムの監査・認証を行う機関の要件を規定し、監査可能な証跡と追跡可能性への期待を高めています。
- **EU AI Act** は段階的適用中（2025–2027）。官報に公布された調和標準は適合の推定を提供します。EU AI Office は 2026 年に実務ガイドライン（ハイリスク分類、Art 50 透明性、インシデント、QMS 要素）の準備を進めています。
- 採用者と認証機関は、AI ガバナンスのシステム層として ISO/IEC 42001 を利用するケースが増えており、AIMO は認証を主張せずにその層を支える証跡の構造化を支援します。

## 参照

- [ISO/IEC 42006](https://www.iso.org/standard/42006) — AI マネジメントシステムの監査・認証を行う機関の要件
- [EU AI Act 実施タイムライン](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act)（欧州委員会 AI 法サービスデスク；一次）
- [European Commission — Clear guidelines for AI (2025年12月4日)](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_xxxx) — AI Office ガイドライン準備（最新 URL は委員会ニュースを確認）
- [EPRS — EU AI Act implementation timeline (2025年6月)](https://www.europarl.europa.eu/thinktank/en/document/EPRS_BRI) — 議会ブリーフィング（参考）
