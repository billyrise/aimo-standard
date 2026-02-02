---
description: AIMO StandardからNIST AI RMFへのマッピング。AIMOタクソノミーコードとNIST AIリスクマネジメントフレームワーク機能間の対応関係。
---

# NIST AI RMF mapping

> 参照ショートカット：Taxonomy → Minimum Evidence → Validator → 人による監督プロトコル

- [Taxonomy](../standard/current/03-taxonomy.md)
- [Minimum Evidence Requirements](../artifacts/minimum-evidence.md)
- [ログスキーマ](../artifacts/log-schemas/index.md)
- [Validator](../validator/index.md)
- [人による監督プロトコル](../governance/human-oversight-protocol.md)

本ページは、NIST AI Risk Management Framework（Govern, Map, Measure, Manage）の主要テーマを AIMO の証跡・アーティファクトに対応付ける。説明可能性のためのものであり、NIST AI RMF への適合を保証しない。NIST 発行物と照合すること。


## Mapping table

| フレームワーク参照 / トピック | AIMO 証跡 / 記載箇所 | Evidence Bundle / Minimum Evidence | アーティファクト・検証 | Notes |
| --- | --- | --- | --- | --- |
| Govern 1.1 – Policies | [Scope](../standard/current/02-scope.md)、[Taxonomy](../standard/current/03-taxonomy.md) | Dictionary, Summary, review; review | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | 情報提供。NIST 発行物と照合すること。 |
| Govern 1.2 – Roles and responsibilities | [Minimum Evidence](../artifacts/minimum-evidence.md) | request, review | templates/ev/ev_template.md | 情報提供。NIST 発行物と照合すること。 |
| Govern 2.1 – Accountability | [Evidence Bundle](../artifacts/evidence-bundle.md) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | 情報提供。NIST 発行物と照合すること。 |
| Govern 3.1 – Risk management | [Scope](../standard/current/02-scope.md) | request, review, exception | templates/ev/ | 情報提供。NIST 発行物と照合すること。 |
| Govern 4.1 – Culture | [Overview](../standard/current/01-overview.md) | Summary, review; review | — | 情報提供。NIST 発行物と照合すること。 |
| Map 1.1 – Context mapping | [Scope](../standard/current/02-scope.md)、[Dictionary](../standard/current/05-dictionary.md) | Dictionary, Summary; request | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | 情報提供。NIST 発行物と照合すること。 |
| Map 2.1 – Data and documentation | [EV Template](../standard/current/06-ev-template.md) | EV, Dictionary, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | 情報提供。NIST 発行物と照合すること。 |
| Map 3.1 – Data governance | [Dictionary](../standard/current/05-dictionary.md) | Dictionary, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | 情報提供。NIST 発行物と照合すること。 |
| Measure 1.1 – Performance and impact | [EV Template](../standard/current/06-ev-template.md) | EV | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | 情報提供。NIST 発行物と照合すること。 |
| Measure 2.1 – Monitoring | [Minimum Evidence](../artifacts/minimum-evidence.md) | EV, change_log; change_log, integrity | templates/ev/ | 情報提供。NIST 発行物と照合すること。 |
| Measure 3.1 – Testing and validation | [Validator](../standard/current/07-validator.md) | EV | validator/rules/, validator/src/; schema_validate_ev | 情報提供。NIST 発行物と照合すること。 |
| Manage 1.1 – Allocation of resources | [Overview](../standard/current/01-overview.md) | Summary, review; review | — | 情報提供。NIST 発行物と照合すること。 |
| Manage 2.1 – Incidents and responses | [Minimum Evidence](../artifacts/minimum-evidence.md) | exception, renewal, change_log | templates/ev/ev_template.md | 情報提供。NIST 発行物と照合すること。 |
| Manage 3.1 – Change management | [Evidence Bundle](../artifacts/evidence-bundle.md) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | 情報提供。NIST 発行物と照合すること。 |
| Manage 4.1 – Review and update | [Minimum Evidence](../artifacts/minimum-evidence.md) | renewal, review; review, renewal | templates/ev/ | 情報提供。NIST 発行物と照合すること。 |
| Manage 5.1 – Communication | [Evidence Bundle](../artifacts/evidence-bundle.md) | Summary, change_log; change_log | templates/ev/ | 情報提供。NIST 発行物と照合すること。 |
