---
description: Shadow AI検知ログスキーマ - 企業内の未承認AI利用の検知、棚卸し、是正を文書化するベンダー非依存形式。
---

# Shadow AI 検知ログスキーマ

## 目的

本スキーマは、**未承認AI利用（Shadow AI）**の検知、棚卸し、是正を文書化するログのベンダー非依存形式を定義する。これにより組織は以下が可能になる：

- Shadow AI 検知イベントの監査可能な記録の維持
- 様々なソース（CASB、プロキシ、IdP、EDR、SaaS監査ログ）からのログを一貫した形式に正規化
- コンプライアンスおよび監査目的の証跡提出の支援

## 正規化の原則

| 原則 | 説明 |
| --- | --- |
| **ベンダー非依存** | 特定ベンダーのログ形式に依存しない；Netskope、Zscaler、Microsoft Defender等に適用可能 |
| **最小限の必須フィールド** | 必須は本質的なフィールドのみ；組織はオプションフィールドを省略可能 |
| **拡張可能** | `additionalProperties: true` によりベンダー固有または組織固有の拡張が可能 |
| **プライバシー配慮** | フィールドは機微なコンテンツを埋め込むのではなく参照するよう設計 |

## 必須フィールド（MUST）

| フィールド | 型 | 説明 | 例 |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | イベントのタイムスタンプ | `2026-01-15T09:30:00Z` |
| `actor_id` | string | ユーザーまたはサービスの識別子 | `user@example.com` |
| `actor_type` | string | アクターの種類 | `user` または `service` |
| `source_system` | string | イベントを検知したシステム | `proxy`, `casb`, `idp`, `edr`, `saas_audit` |
| `ai_service` | string | アクセスされたAI製品またはドメイン | `chat.openai.com`, `claude.ai` |
| `action` | string | 実行されたアクション | `chat`, `upload`, `download`, `tool_execute`, `api_call` |
| `data_classification` | string | データ分類レベル | `public`, `internal`, `confidential`, `restricted` |
| `decision` | string | 適用されたポリシー決定 | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | 関連証跡への参照 | `sha256:abc123...` または `urn:evidence:...` |
| `record_id` | string | このレコードの一意識別子 | `evt-20260115-001` |

## オプションフィールド（SHOULD/MAY）

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `session_id` | string | セッション識別子 |
| `device_id` | string | デバイス識別子 |
| `ip` | string | IPアドレス |
| `user_agent` | string | ユーザーエージェント文字列 |
| `department` | string | 組織の部門 |
| `project_id` | string | プロジェクト識別子 |
| `prompt_category` | string | プロンプト/クエリのカテゴリ |
| `model_family` | string | AIモデルファミリー（例：GPT-4、Claude） |
| `destination` | string | 宛先URLまたはエンドポイント |
| `policy_id` | string | 決定をトリガーしたポリシー |
| `remediation_ticket` | string | 是正チケットの参照 |

## プライバシー/セキュリティ上の注意

!!! warning "データ取り扱い"
    - PII、認証情報、プロンプト内容をログフィールドに**直接埋め込まない**こと。
    - 別途保管された機微なコンテンツを参照するために `evidence_ref` を使用する。
    - ログ保管に適切なアクセス制御を適用する。
    - [Minimum Evidence Requirements](../minimum-evidence.md) に沿ったデータ保持ポリシーを検討する。

## JSON Schema

ダウンロード: [shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "event_time", "actor_id", "actor_type", "source_system",
    "ai_service", "action", "data_classification", "decision",
    "evidence_ref", "record_id"
  ],
  "properties": {
    "event_time": { "type": "string", "format": "date-time" },
    "actor_id": { "type": "string", "minLength": 1 },
    "actor_type": { "type": "string", "enum": ["user", "service"] },
    "source_system": { "type": "string", "minLength": 1 },
    "ai_service": { "type": "string", "minLength": 1 },
    "action": { "type": "string", "minLength": 1 },
    "data_classification": { "type": "string", "minLength": 1 },
    "decision": { "type": "string", "enum": ["allow", "block", "needs_review", "unknown"] },
    "evidence_ref": { "type": "string", "minLength": 1 },
    "record_id": { "type": "string", "minLength": 1 }
  },
  "additionalProperties": true
}
```

## 関連ページ

- [ログスキーマ索引](index.md)
- [エージェント活動ログ](agent-activity.md)
- [Minimum Evidence Requirements](../minimum-evidence.md)
- [タクソノミー: IM-007 シャドー/未管理](../../standard/current/03-taxonomy.md)
