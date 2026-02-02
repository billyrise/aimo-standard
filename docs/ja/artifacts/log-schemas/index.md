---
description: AIMOログスキーマ - AI証跡用ベンダー非依存ログ形式。Shadow AI検知とエージェント活動監視スキーマを含む。
---

# ログスキーマ

## これは何か

本セクションは、Evidence Bundle に含めることができる証跡のための**正規化ログ形式**を定義する。これらのスキーマは、AI利用監視およびエージェント運用に関連するログのベンダー非依存の構造を提供する。

## いつ使うか

- **Shadow AI の可視化**: 未承認AI利用の検知、棚卸し、是正の文書化。
- **エージェント運用の監査**: 自律エージェントの権限行使、ツール実行、再帰的操作の説明。
- **インシデントの再現性**: インシデント調査と根本原因分析のための構造化された証跡の提供。

## これではないこと

!!! warning "重要"
    これらのスキーマは**証跡提出のためのログ形式**を定義する。以下は**行わない**：

    - システムからのログ自動収集
    - ログ集約または監視ツールの提供
    - いかなる規制・規格への準拠保証
    - ベンダー固有のログ実装の代替

    組織は独自のログ収集パイプラインを実装し、証跡提出のためにこれらのスキーマにログを正規化する必要がある。

## スキーマ

| スキーマ | 目的 | ダウンロード |
| --- | --- | --- |
| [Shadow AI 検知ログ](shadow-ai-discovery.md) | 未承認AI利用の検知と棚卸し | [shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json) |
| [エージェント活動ログ](agent-activity.md) | エージェントAIの権限行使とツール実行 | [agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json) |

## 関連ページ

- [Minimum Evidence Requirements](../minimum-evidence.md) — MUST レベル証跡チェックリスト
- [Evidence Bundle](../evidence-bundle.md) — バンドル構造と TOC
- [タクソノミー](../../standard/current/03-taxonomy.md) — 分類コード（UC-010 エージェント自動化、IM-007 シャドー/未管理を含む）
