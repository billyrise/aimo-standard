---
description: AIMO StandardからEU AI Actへのマッピング。AIMOタクソノミーコードとEU AI Actリスクカテゴリ・要件間の対応関係。
---

# EU AI Act mapping

> 参照ショートカット：Taxonomy → Minimum Evidence → Validator → 人による監督プロトコル

- [Taxonomy](../standard/current/03-taxonomy.md)
- [Minimum Evidence Requirements](../artifacts/minimum-evidence.md)
- [ログスキーマ](../artifacts/log-schemas/index.md)
- [Validator](../validator/index.md)
- [人による監督プロトコル](../governance/human-oversight-protocol.md)

本ページは、EU AI Act の主要テーマ（文書化、記録保持、リスク管理、人的監督、透明性）を AIMO の証跡・アーティファクトに対応付ける。概要レベルであり、**法的助言**や適合の保証ではない。正式な法令と照合すること。


## Mapping table

| フレームワーク参照 / トピック | AIMO 証跡 / 記載箇所 | Evidence Bundle / Minimum Evidence | アーティファクト・検証 | Notes |
| --- | --- | --- | --- | --- |
| Art 9 – Risk management (obligations) | [Scope](../standard/current/02-scope.md) | request, review, exception | templates/ev/ | 概要のみ。法的助言ではない。正式文書と照合すること。 |
| Art 10 – Data governance | [Dictionary](../standard/current/05-dictionary.md) | Dictionary, EV | schemas/jsonschema/; schema_validate_dictionary | 概要のみ。法的助言ではない。正式文書と照合すること。 |
| Art 11 – Documentation (high-risk) | [EV Template](../standard/current/06-ev-template.md)、[Evidence Bundle](../artifacts/evidence-bundle.md) | EV, Dictionary, Summary; request, review | schemas/jsonschema/, templates/ev/; schema_validate_ev | 概要のみ。法的助言ではない。正式文書と照合すること。 |
| Art 12 – Record-keeping | [Evidence Bundle](../artifacts/evidence-bundle.md)、[Minimum Evidence](../artifacts/minimum-evidence.md) | EV, change_log, request, review | examples/evidence_bundle_minimal/; schema_validate_ev | 概要のみ。法的助言ではない。正式文書と照合すること。 |
| Art 13 – Transparency (user information) | [Scope](../standard/current/02-scope.md) | Summary, EV; review | templates/ev/ | 概要のみ。法的助言ではない。正式文書と照合すること。 |
| Art 14 – Human oversight | [Minimum Evidence](../artifacts/minimum-evidence.md) | review, exception; review, exception | templates/ev/ev_template.md | 概要のみ。法的助言ではない。正式文書と照合すること。 |
| Art 17 – Risk management (high-risk) | [Scope](../standard/current/02-scope.md) | request, review, exception, renewal | templates/ev/ | 概要のみ。法的助言ではない。正式文書と照合すること。 |
| Art 26 – Transparency (limited risk) | [Scope](../standard/current/02-scope.md) | Summary, EV; review | templates/ev/ | 概要のみ。法的助言ではない。正式文書と照合すること。 |
| Art 29 – Documentation (general-purpose AI) | [EV Template](../standard/current/06-ev-template.md) | EV, Dictionary, Summary; request, review | schemas/jsonschema/; schema_validate_ev | 概要のみ。法的助言ではない。正式文書と照合すること。 |
| Art 52 – Transparency (deployer) | [Minimum Evidence](../artifacts/minimum-evidence.md) | EV, Summary; review | templates/ev/ | 概要のみ。法的助言ではない。正式文書と照合すること。 |
| Recitals – Accountability | [Evidence Bundle](../artifacts/evidence-bundle.md) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | 概要のみ。法的助言ではない。正式文書と照合すること。 |
