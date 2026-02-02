---
description: AIMO Evidence Packテンプレートと使用ガイド。索引管理と監査対応フォーマットでAIガバナンス証跡を文書化するための構造。
---

# EVテンプレート

このセクションでは、Evidence Packテンプレートとその使用方法を定義します。Evidence Packは、AIシステムのガバナンスとコンプライアンスを示すドキュメントのコレクションです。

## 重要原則：索引と差分管理

> **重要**: 重要なのは個々の提出物の中身ではなく、証跡項目全体の**索引**と**差分管理**です。

Evidence Packは、AIシステムをそのガバナンスアーティファクトにリンクする索引として機能します。価値は以下にあります：

1. **トレーサビリティ**: 時間を通じた決定、承認、変更のリンク
2. **監査可能性**: 監査人が証跡構造をナビゲートできること
3. **保守性**: 何が、いつ、なぜ変更されたかの追跡

## MVP証跡セット（EV-01〜EV-07）

以下の7つの証跡種別が、AIガバナンスを示すための**最小限の必要セット**を構成します：

| ID | 証跡種別 | コード | 目的 |
| --- | --- | --- | --- |
| EV-01 | システム概要 | EV-001 | AIシステムとその目的の文書化 |
| EV-02 | データフロー | EV-002 | システムを通じたデータの流れのマッピング |
| EV-03 | 資産台帳 | EV-003 | AI資産のカタログ維持 |
| EV-04 | リスク影響評価 | EV-004 | リスクの評価と文書化 |
| EV-05 | 統制・承認 | EV-005 | 統制と承認記録の文書化 |
| EV-06 | ログ・監視 | EV-006 | ログと監視の設定定義 |
| EV-07 | インシデント・例外 | EV-007 | インシデントと例外の追跡 |

## Evidence Packマニフェスト

各Evidence Packには以下を含むマニフェストファイルが必須です：

### 必須メタデータ

| フィールド | 説明 | 必須 |
| --- | --- | --- |
| `pack_id` | 一意識別子（例：EP-EXAMPLE-001） | はい |
| `pack_version` | パックのSemVerバージョン | はい |
| `taxonomy_version` | 使用するAIMOタクソノミーのバージョン | はい |
| `created_date` | パック作成日 | はい |
| `last_updated` | 最終更新日 | はい |
| `owner` | 責任者 | はい |

### AIMOコード（8次元）

各Evidence Packには8次元すべてからのコードが必須です：

```json
{
  "codes": {
    "FS": ["FS-001"],
    "UC": ["UC-001", "UC-002"],
    "DT": ["DT-002"],
    "CH": ["CH-001"],
    "IM": ["IM-001"],
    "RS": ["RS-001", "RS-003"],
    "OB": ["OB-001"],
    "EV": ["EV-001", "EV-002", "EV-003", "EV-004", "EV-005", "EV-006", "EV-007"]
  }
}
```

### 証跡ファイルリスト

```json
{
  "evidence_files": [
    {
      "file_id": "EV-01",
      "filename": "EV-01_system_overview.md",
      "ev_type": "EV-001",
      "title": "System Overview",
      "required": true
    }
  ]
}
```

## テンプレート構造

各証跡テンプレートには以下が含まれます：

1. **必須メタデータブロック** - pack_id、バージョン、taxonomy_version、日付、owner
2. **AIMOコードテーブル** - 該当するコードを含む8次元すべて
3. **コンテンツセクション** - ドメイン固有のドキュメントセクション
4. **参照** - 関連証跡へのリンク
5. **改訂履歴** - 変更追跡

### テンプレートヘッダー例

```markdown
# EV-01: システム概要

---

## 必須メタデータ

| フィールド | 値 |
| --- | --- |
| **pack_id** | `EP-EXAMPLE-001` |
| **pack_version** | `0.1.0` |
| **taxonomy_version** | `0.1.0` |
| **created_date** | `2026-01-31` |
| **last_updated** | `2026-01-31` |
| **owner** | `AI Governance Team` |

---

## AIMOコード（8次元）

| 次元 | コード | ラベル |
| --- | --- | --- |
| **FS** | `FS-001` | 社内生産性 |
| **UC** | `UC-001` | 一般QA |
| **DT** | `DT-002` | 社内情報 |
| **CH** | `CH-001` | Web UI |
| **IM** | `IM-001` | 単体利用 |
| **RS** | `RS-001` | 情報漏えい |
| **OB** | `OB-001` | 効率化 |
| **EV** | `EV-001` | システム概要 |
```

## ダウンロード

### テンプレート

Evidence Packテンプレートは以下で利用可能です：

- `source_pack/04_evidence_pack/templates/EV-01_system_overview.md`
- `source_pack/04_evidence_pack/templates/EV-02_data_flow.md`
- `source_pack/04_evidence_pack/templates/EV-03_inventory.md`
- `source_pack/04_evidence_pack/templates/EV-04_risk_impact.md`
- `source_pack/04_evidence_pack/templates/EV-05_controls_approvals.md`
- `source_pack/04_evidence_pack/templates/EV-06_logging_monitoring.md`
- `source_pack/04_evidence_pack/templates/EV-07_incident_exception.md`

### スキーマと例

- スキーマ: `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json`
- 例: `source_pack/04_evidence_pack/examples/evidence_pack_manifest.example.json`

ダウンロード可能なパッケージは[リリース](../../releases/index.md)を参照してください。

## 配布モデル

> **注**: 主要な配布対象は個々の企業ではなく、**監査法人とシステムインテグレーター**（テンプレート流通者）です。

テンプレートは以下のように設計されています：

1. 監査人とコンサルタントが標準アーティファクトとして採用
2. 出典の帰属を保持して企業に配布
3. AIMO Standardと共にバージョン管理

企業は、標準バージョンへのリンクを維持する監査人、コンサルタント、または社内ガバナンスチームを通じてテンプレートを受け取ります。

## 参照

- [タクソノミー](./03-taxonomy.md) - 次元定義
- [コード](./04-codes.md) - コードフォーマット
- [バリデータ](./07-validator.md) - バリデーションルール
- [エビデンスバンドル](../../artifacts/evidence-bundle.md) - バンドル構造
