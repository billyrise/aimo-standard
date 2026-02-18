---
description: AIMO Standard の適合性レベル。組織の適合主張の仕方、エビデンス要件、各レベルが AI ガバナンスで意味する内容。
---
<!-- aimo:translation_status=translated -->

# 適合性

!!! warning "重要: 認証ではなく、保証ではなく、法・規制適合の主張ではない"
    AIMO Standard は**エビデンスのパッケージ化・検証フォーマット**を定義します。法令や規格への適合を認証するものではありません。
    監査・保証の意見は、独立した監査人および採用組織の責任です。
    **適切な主張例:** 「Evidence Bundle は AIMO Standard v0.1.2 に従って作成され、AIMO Validator により構造検証されました。」
    <!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
    **不適切な主張例:** 「EU AI 法適合」「ISO 42001 認証」「政府承認」。
    <!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

AIMO Standard は**保証・監査引き継ぎ・継続的証跡のレイヤー**として位置づけます：構造化証跡のパッケージ化、Validator、トレーサビリティを提供し、採用者と監査人が構造化証跡を扱えるようにします。AIMO は**認証機関ではありません**。認証・適合の判断は認定認証機関、監査人、採用組織が行います。

これらのティアは、パッケージ化とトレーサビリティのための**内部エビデンス成熟度レベル**です。認証でも、保証意見でも、法・規制適合でも**ありません**。

## 互換性の主張（ISO/NIST/EU AI Act）

以下の**参考マッピング**は、AIMO の証跡・アーティファクトと外部フレームワークを対応づけます。説明可能性と監査引き継ぎを支援するものであり、認証や適合保証を**付与しません**。権威あるフレームワーク本文で照合してください。

- [Coverage Map — ISO/IEC 42001](../coverage-map/iso-42001/) — ISO/IEC 42001（AI マネジメントシステム）へのマッピング
- [Coverage Map — NIST AI RMF](../coverage-map/nist-ai-rmf/) — NIST AI リスクマネジメントフレームワークへのマッピング
- [Coverage Map — EU AI Act](../coverage-map/eu-ai-act/) — EU AI 法テーマへのマッピング（概要；法務助言ではない）

一次ソースと主張文言は各 Coverage Map ページおよび [Responsibility Boundary](../governance/responsibility-boundary/) に記載しています。

## 主張しないこと（Non-claims）

- AIMO は ISO/IEC 42001、NIST AI RMF、EU AI Act その他いかなるフレームワークへの適合**認証を行いません**。
- AIMO は規制・法適合を**保証しません**。
- AIMO は保証意見や法務助言を**提供しません**。
- AIMO は組織が外部要求を満たすかどうかを**判断しません**。それは採用者、監査人、認証機関の責任です。

AIMO が**提供するもの**：構造化証跡フォーマット、Validator、Coverage Map（参考）、監査引き継ぎを支援する資料。詳細は [Responsibility Boundary](../governance/responsibility-boundary/) を参照。

!!! note "ティア名の別名"
    最上位ティアは非公式な議論で以前「Gold」と呼ばれたことがあります；**公式ティア名は Audit-Ready** です。

## AIMO 適合性フレームワーク（AIMO-MS / AIMO-Controls / AIMO-Audit）

| コンポーネント | 説明 | エビデンス期待 |
| --- | --- | --- |
| **AIMO-MS** | マネジメントシステム志向の構造：ISO/IEC 42001 型コントロールを支えうる方針・役割・PDCA に沿ったアーティファクト。 | Request、review、exception、renewal、change log；Summary と Dictionary。 |
| **AIMO-Controls** | ライフサイクル・整合性コントロール：request→review→exception→renewal、ハッシュ、署名（[Evidence Bundle 構造](../../standard/current/09-evidence-bundle-structure/)に準拠）。 | Object_index、payload_index、hash_chain、signing；ライフサイクル記録。 |
| **AIMO-Audit** | 監査引き継ぎの準備：Validator 合格、チェックサム、オプションの attestation と監査引き継ぎインデックス。 | Validator 出力、bundle_id、producer identity、オプションの署名メタデータと引き継ぎインデックス。 |

エビデンス期待の詳細は [最低証拠要件](../artifacts/minimum-evidence/) と [Evidence Bundle](../artifacts/evidence-bundle/) を参照。

## 適合性レベル（AIMO のみ）

### レベル 1 — Foundation

**目的:** トレーサブルなベースライン。バンドルを識別可能・整合性検証可能・Validator チェック済みとする最小セット。

| 項目 | 要件 |
| --- | --- |
| **必須アーティファクト** | [Evidence Bundle](../artifacts/evidence-bundle/) 構造（manifest.json、objects/、仕様通りの payload_index）；[Validator](../validator/) 合格；[最低証拠](../artifacts/minimum-evidence/)へのリンク。 |
| **典型的な監査質問** | スコープは何か？バンドルは誰が作成したか？ハッシュは検証できるか？ |
| **典型的なギャップ** | manifest メタデータ（bundle_id、created_at、producer）欠落；Validator 未実行または未添付。 |

### レベル 2 — Operational

**目的:** 運用コントロールのエビデンス。Foundation にライフサイクル証跡とモニタリングを積み上げる。

| 項目 | 要件 |
| --- | --- |
| **必須アーティファクト** | Foundation の全 MUST 項目；ライフサイクルコントロール証跡（request/承認、review、exception または「例外なし」、renewal スケジュール）；少なくとも 1 件のモニタリングアーティファクト（インシデントログまたは定期チェックまたは人間監督サンプリング）；整合性リンク付き change log；証明と保証の境界の明示。 |
| **典型的な監査質問** | 利用承認者は誰か？例外はどう追跡しているか？最終 review はいつか？ |
| **典型的なギャップ** | review/承認が request にリンクされていない；モニタリングアーティファクトなし；change log が影響オブジェクトを参照していない。 |

### レベル 3 — Audit-Ready

**目的:** 監査引き継ぎの品質。完全な attestation、再現性、外部フォームのスロット。

| 項目 | 要件 |
| --- | --- |
| **必須アーティファクト** | Operational の全 MUST 項目；manifest をカバーする少なくとも 1 つのデジタル署名（署名者 identity + アルゴリズム）；TSA または「TSA なし」の表明；再現パケット（正確な Validator コマンド、期待出力、環境メタデータ）；公式テンプレート/チェックリストをそのまま添付・相互参照した External Forms 節；有界完全性表明；1 ページの監査引き継ぎインデックス（アーティファクト → ハッシュ → producer → 日付）。 |
| **典型的な監査質問** | 監査人が検証を再実行する方法は？外部チェックリストはどこにあり、バンドルにどうマッピングするか？ |
| **典型的なギャップ** | 署名はあるが署名者/アルゴリズムが文書化されていない；引き継ぎインデックスなし；外部フォームがハッシュされていないか manifest で参照されていない。 |

## レベル別最低証拠（概要）

| レベル | MUST（概要） |
| --- | --- |
| **Foundation** | バンドル構造（manifest、object_index、payload_index）；参照オブジェクトの sha256；bundle_id、created_at、producer；Validator 実行 + バージョン；エビデンス辞書ベースライン（システム名、オーナー、目的、データカテゴリ、ライフサイクル段階）；アクセス・保持の表明（誰が、期間、保存種別、改ざん検知）。SHOULD: 最小限の change log エントリ。 |
| **Operational** | Foundation の全 MUST；ライフサイクル証跡（request/承認、review、exception または「なし」、renewal + 最終 renewal）；≥1 のモニタリングアーティファクト；change log エントリが影響オブジェクトを参照；証明と保証の境界の明示。 |
| **Audit-Ready** | Operational の全 MUST；manifest に対する ≥1 の署名（署名者 identity + アルゴリズム）；TSA または「TSA なし」；再現パケット；External Forms の列挙と相互参照；有界完全性表明；監査引き継ぎインデックス。 |

署名の**存在**（manifest をターゲットとする少なくとも 1 つの署名）は、規範的 [Evidence Bundle 構造](../../standard/current/09-evidence-bundle-structure/)により全バンドルで必須です。**Audit-Ready** は、第三者による再検証を可能にするため、より厳格な**暗号 attestation**（署名者 identity、アルゴリズム、TSA 表明、再検証手順）を追加します。

## ISO/IEC 42001 マッピング（参考）

以下の表は、AIMO アーティファクトが典型的な ISO/IEC 42001 条項族のエビデンスを**どう支えるか**を示します。参考であり、認証や適合を意味しません。

| ISO/IEC 42001 条項族 | エビデンスを支える AIMO アーティファクト |
| --- | --- |
| 組織の状況 | Summary、Dictionary、scope_ref |
| リーダーシップ / 方針 | Summary、review、dictionary |
| 計画（リスク、目標） | request、review、exception、EV、Dictionary |
| 支援（リソース、能力、文書） | Summary、review、EV、change_log |
| 運用 | EV、request、review、exception；運用コントロール |
| パフォーマンス評価（モニタリング、内部監査、マネジメントレビュー） | EV、change_log、review、renewal |
| 改善 | exception、renewal、change_log |

詳細は [Coverage Map — ISO/IEC 42001](../coverage-map/iso-42001/) と [ISO 42001 認証準備ツールキット](../artifacts/iso-42001-certification-readiness-toolkit/) を参照。

## 主張文言テンプレート（過大主張防止）

実際に行ったことを正確に表す主張のみを使用してください。認証と法適合は採用者と認定機関の責任です。

**受容可能（例）**

- 「当社は AIMO Standard v0.1.2 に対する AIMO 適合（レベル 2）です；ISO 認証や法適合を意味しません。」
- 「AIMO アーティファクトで ISO/IEC 42001 準備を支援しています；認証判断は認定認証機関にあります。」
- 「Evidence Bundle は AIMO Standard v0.1.2 に従って作成され、AIMO Validator により構造検証されました。」

<!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
**受容不可（例）**

- 「EU AI 法適合」（AIMO は規制適合を認証しません。）
- 「ISO 42001 認証」（認証は認定認証機関が発行し、AIMO ではありません。）
- 「政府承認」（AIMO は政府承認制度ではありません。）
<!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

## 関連ページ

- [Trust Package](../governance/trust-package/) — 監査人向け統合エントリ
- [Responsibility Boundary](../governance/responsibility-boundary/) — AIMO が提供するもの・しないもの
- [Standard (Current)](../standard/current/) — 規範要件
- [Artifacts](../artifacts/) — エビデンス構造と最低証拠
- [Validator](../validator/) — 構造検証
