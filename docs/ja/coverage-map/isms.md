---
description: AIMO StandardからISMS（ISO 27001/27002）へのマッピング。AIMOタクソノミーと情報セキュリティ管理システム統制間の対応関係。
---
<!-- aimo:translation_status=translated -->

# ISMS view (ISO/IEC 27001/27002) mapping

> 参照ショートカット：Taxonomy → Minimum Evidence → Validator → 人による監督プロトコル

- [Taxonomy](../../standard/current/03-taxonomy/)
- [Minimum Evidence Requirements](../../artifacts/minimum-evidence/)
- [ログスキーマ](../../artifacts/log-schemas/)
- [Validator](../../validator/)
- [人による監督プロトコル](../../governance/human-oversight-protocol/)

本ページは、ISO/IEC 27001/27002 の主要テーマ（変更管理、アクセス制御、ログ、証跡の完全性）を AIMO の証跡・アーティファクトに対応付ける。説明可能性のためのものであり、ISO/IEC 27001 または 27002 への適合を保証しない。発行された規格と照合すること。


## Mapping table

| フレームワーク参照 / トピック | AIMO 証跡 / 記載箇所 | Evidence Bundle / Minimum Evidence | アーティファクト・検証 | Notes |
| --- | --- | --- | --- | --- |
| A.5.24 – Information security in project management | [Scope](../../standard/current/02-scope/) | request, review | templates/ev/ | 情報提供。正式文書と照合すること。 |
| A.5.29 – Information security during disruption | [Minimum Evidence](../../artifacts/minimum-evidence/) | exception, renewal | templates/ev/ev_template.md | 情報提供。正式文書と照合すること。 |
| A.5.30 – ICT readiness for business continuity | [Overview](../../standard/current/01-overview/) | Summary; integrity | — | 情報提供。正式文書と照合すること。 |
| A.8.1 – Inventory of assets | [Dictionary](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | 情報提供。正式文書と照合すること。 |
| A.8.2 – Information classification | [Taxonomy](../../standard/current/03-taxonomy/) | Dictionary; review | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | 情報提供。正式文書と照合すること。 |
| A.8.3 – Access control | [Minimum Evidence](../../artifacts/minimum-evidence/) | —; integrity | — | 情報提供。正式文書と照合すること。 |
| A.8.15 – Logging | [EV Template](../../standard/current/06-ev-template/) | EV, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | 情報提供。正式文書と照合すること。 |
| A.8.16 – Monitoring activities | [Minimum Evidence](../../artifacts/minimum-evidence/) | EV, change_log; change_log, integrity | templates/ev/ | 情報提供。正式文書と照合すること。 |
| A.8.32 – Change management | [Evidence Bundle](../../artifacts/evidence-bundle/) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | 情報提供。正式文書と照合すること。 |
| A.8.33 – Test information | [Validator](../../standard/current/07-validator/) | EV | validator/rules/, validator/src/; schema_validate_ev | 情報提供。正式文書と照合すること。 |
