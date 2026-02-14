---
description: エージェント活動ログ形式 - 企業内のエージェントAI権限行使、ツール実行、再帰的操作監視のためのベンダー非依存スキーマ。
---

# エージェント活動ログ形式

## 目的

本スキーマは、**エージェントAIの権限行使、ツール実行、再帰的操作**を文書化するログのベンダー非依存形式を定義する。これにより組織は以下が可能になる：

- 自律エージェントのアクションの監査可能な記録の維持
- コンプライアンスおよびインシデント調査のための「誰が、何を、どの権限で行ったか」の追跡
- 監査コンテキストにおけるエージェントAI運用の説明可能性の支援

## イベントモデル

本スキーマはエージェント運用ライフサイクルを捕捉する4つのイベントタイプをサポートする：

| イベントタイプ | 説明 |
| --- | --- |
| `agent_run` | エージェント実行セッションの開始または完了 |
| `tool_call` | エージェントによるツールまたは外部アクションの呼び出し |
| `tool_result` | ツール呼び出しから返された結果 |
| `escalation` | エージェントによる人的介入または権限昇格の要求 |

## 必須フィールド（MUST）

| フィールド | 型 | 説明 | 例 |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | イベントのタイムスタンプ | `2026-01-15T09:30:00Z` |
| `agent_id` | string | エージェントの識別子 | `agent-coding-assistant-v2` |
| `agent_version` | string | エージェントのバージョン | `2.1.0` |
| `run_id` | string | この実行/セッションの一意識別子 | `run-20260115-abc123` |
| `event_type` | string | イベントの種類 | `agent_run`, `tool_call`, `tool_result`, `escalation` |
| `actor_id` | string | 起動したユーザーまたはサービス | `user@example.com` |
| `tool_name` | string | 呼び出されたツールの名前 | `file_write`, `api_call`, `shell_exec` |
| `tool_action` | string | ツールが実行したアクション | `create`, `read`, `update`, `delete`, `execute` |
| `tool_target` | string | アクションの対象 | `/path/to/file`, `https://api.example.com` |
| `auth_context` | string | 権限/ロールの要約 | `role:developer, scope:project-x` |
| `input_ref` | string | 入力へのハッシュまたはURI（内容そのものではない） | `sha256:def456...` |
| `output_ref` | string | 出力へのハッシュまたはURI（内容そのものではない） | `sha256:ghi789...` |
| `decision` | string | 適用されたポリシー決定 | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | 関連証跡への参照 | `urn:evidence:...` |

## オプションフィールド（SHOULD/MAY）

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `recursion_depth` | number | ネストされたエージェント呼び出しの現在の再帰深度 |
| `retry_count` | number | このアクションのリトライ回数 |
| `policy_id` | string | 決定をトリガーしたポリシー |
| `prompt_template_id` | string | プロンプトテンプレート識別子 |
| `model` | string | このアクションで使用されたモデル |
| `latency_ms` | number | レイテンシ（ミリ秒） |
| `cost_estimate` | number | このアクションの推定コスト |
| `error_code` | string | アクションが失敗した場合のエラーコード |

## 安全性に関する注意

!!! warning "エージェントリスクの前提"
    エージェントAI活動をログ記録する際、以下のリスクを前提とすること：

    - **プロンプトインジェクション**: 悪意のある入力がエージェントの動作を操作しようとする可能性
    - **過剰権限**: エージェントが特定タスクに対して意図より広い権限を持つ可能性
    - **再帰ループ**: エージェントが意図しない再帰的実行パターンに入る可能性
    - **Confused deputy**: エージェントが権限のない当事者の代わりに行動するよう騙される可能性

    本スキーマはインシデント後の分析と監査説明を支援するため「誰が、何を、どの権限で行ったか」を捕捉するよう設計されている。これらのリスクを防止するものではなく、組織は適切なガードレールを実装する必要がある。

!!! warning "データ取り扱い"
    - `input_ref` や `output_ref` にシークレット、認証情報、機微なコンテンツを**埋め込まない**こと。
    - 別途保管されたコンテンツへのハッシュ参照またはセキュアなURIを使用する。
    - 適切なアクセス制御と保持ポリシーを適用する。

## JSON Schema

ダウンロード: [agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "event_time", "agent_id", "agent_version", "run_id", "event_type",
    "actor_id", "tool_name", "tool_action", "tool_target", "auth_context",
    "input_ref", "output_ref", "decision", "evidence_ref"
  ],
  "properties": {
    "event_time": { "type": "string", "format": "date-time" },
    "agent_id": { "type": "string", "minLength": 1 },
    "agent_version": { "type": "string", "minLength": 1 },
    "run_id": { "type": "string", "minLength": 1 },
    "event_type": { "type": "string", "enum": ["agent_run", "tool_call", "tool_result", "escalation"] },
    "actor_id": { "type": "string", "minLength": 1 },
    "tool_name": { "type": "string", "minLength": 1 },
    "tool_action": { "type": "string", "minLength": 1 },
    "tool_target": { "type": "string", "minLength": 1 },
    "auth_context": { "type": "string", "minLength": 1 },
    "input_ref": { "type": "string", "minLength": 1 },
    "output_ref": { "type": "string", "minLength": 1 },
    "decision": { "type": "string", "enum": ["allow", "block", "needs_review", "unknown"] },
    "evidence_ref": { "type": "string", "minLength": 1 }
  },
  "additionalProperties": true
}
```

## 関連ページ

- [ログスキーマ索引](../)
- [Shadow AI 検知ログ](../shadow-ai-discovery/)
- [Minimum Evidence Requirements](../../minimum-evidence/)
- [タクソノミー: UC-010 エージェント自動化](../../../standard/current/03-taxonomy/)
