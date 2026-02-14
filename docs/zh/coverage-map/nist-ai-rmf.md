---
description: AIMO 标准与 NIST AI RMF 的映射。AIMO 分类法代码与 NIST AI风险管理框架功能之间的可追溯性。
---

# NIST AI RMF 映射

> 可追溯性快捷方式：分类法 → 最低证据 → 验证器 → 人工监督协议。

- [分类法](../../standard/current/03-taxonomy/)
- [最低证据要求](../../artifacts/minimum-evidence/)
- [日志模式](../../artifacts/log-schemas/)
- [验证器](../../validator/)
- [人工监督协议](../../governance/human-oversight-protocol/)

本页将选定的 NIST AI风险管理框架（治理、映射、度量、管理）主题映射到 AIMO 证据和工件。这仅用于可解释性；不保证符合 NIST AI RMF。请根据 NIST 出版物进行验证。


## 映射表

| 框架引用/主题 | AIMO 证据/在 AIMO 中的位置 | 证据包/最低证据 | 工件与验证 | 说明 |
| --- | --- | --- | --- | --- |
| Govern 1.1 – 政策 | [范围](../../standard/current/02-scope/), [分类法](../../standard/current/03-taxonomy/) | Dictionary, Summary, review; review | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | 仅供参考；请根据 NIST 出版物验证。 |
| Govern 1.2 – 角色和职责 | [最低证据](../../artifacts/minimum-evidence/) | request, review | templates/ev/ev_template.md | 仅供参考；请根据 NIST 出版物验证。 |
| Govern 2.1 – 问责 | [证据包](../../artifacts/evidence-bundle/) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | 仅供参考；请根据 NIST 出版物验证。 |
| Govern 3.1 – 风险管理 | [范围](../../standard/current/02-scope/) | request, review, exception | templates/ev/ | 仅供参考；请根据 NIST 出版物验证。 |
| Govern 4.1 – 文化 | [概述](../../standard/current/01-overview/) | Summary, review; review | — | 仅供参考；请根据 NIST 出版物验证。 |
| Map 1.1 – 背景映射 | [范围](../../standard/current/02-scope/), [字典](../../standard/current/05-dictionary/) | Dictionary, Summary; request | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | 仅供参考；请根据 NIST 出版物验证。 |
| Map 2.1 – 数据和文档 | [EV 模板](../../standard/current/06-ev-template/) | EV, Dictionary, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | 仅供参考；请根据 NIST 出版物验证。 |
| Map 3.1 – 数据治理 | [字典](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | 仅供参考；请根据 NIST 出版物验证。 |
| Measure 1.1 – 性能和影响 | [EV 模板](../../standard/current/06-ev-template/) | EV | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | 仅供参考；请根据 NIST 出版物验证。 |
| Measure 2.1 – 监控 | [最低证据](../../artifacts/minimum-evidence/) | EV, change_log; change_log, integrity | templates/ev/ | 仅供参考；请根据 NIST 出版物验证。 |
| Measure 3.1 – 测试和验证 | [验证器](../../standard/current/07-validator/) | EV | validator/rules/, validator/src/; schema_validate_ev | 仅供参考；请根据 NIST 出版物验证。 |
| Manage 1.1 – 资源分配 | [概述](../../standard/current/01-overview/) | Summary, review; review | — | 仅供参考；请根据 NIST 出版物验证。 |
| Manage 2.1 – 事件和响应 | [最低证据](../../artifacts/minimum-evidence/) | exception, renewal, change_log | templates/ev/ev_template.md | 仅供参考；请根据 NIST 出版物验证。 |
| Manage 3.1 – 变更管理 | [证据包](../../artifacts/evidence-bundle/) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | 仅供参考；请根据 NIST 出版物验证。 |
| Manage 4.1 – 审查和更新 | [最低证据](../../artifacts/minimum-evidence/) | renewal, review; review, renewal | templates/ev/ | 仅供参考；请根据 NIST 出版物验证。 |
| Manage 5.1 – 沟通 | [证据包](../../artifacts/evidence-bundle/) | Summary, change_log; change_log | templates/ev/ | 仅供参考；请根据 NIST 出版物验证。 |
