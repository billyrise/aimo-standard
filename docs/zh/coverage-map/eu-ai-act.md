---
description: AIMO 标准与欧盟AI法案的映射。AIMO 分类法代码与欧盟AI法案风险类别和要求之间的可追溯性。
---

# 欧盟AI法案映射

> 可追溯性快捷方式：分类法 → 最低证据 → 验证器 → 人工监督协议。

- [分类法](../../standard/current/03-taxonomy/)
- [最低证据要求](../../artifacts/minimum-evidence/)
- [日志模式](../../artifacts/log-schemas/)
- [验证器](../../validator/)
- [人工监督协议](../../governance/human-oversight-protocol/)

本页将选定的欧盟AI法案主题（文档、记录保存、风险管理、人工监督、透明度）映射到 AIMO 证据和工件。这只是高级别的映射，**不**构成法律建议或保证合规。请根据官方法律文本进行验证。


## 映射表

| 框架引用/主题 | AIMO 证据/在 AIMO 中的位置 | 证据包/最低证据 | 工件与验证 | 说明 |
| --- | --- | --- | --- | --- |
| Art 9 – 风险管理（义务） | [范围](../../standard/current/02-scope/) | request, review, exception | templates/ev/ | 仅高级别；非法律建议。请根据官方文本验证。 |
| Art 10 – 数据治理 | [字典](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/; schema_validate_dictionary | 仅高级别；非法律建议。请根据官方文本验证。 |
| Art 11 – 文档（高风险） | [EV 模板](../../standard/current/06-ev-template/), [证据包](../../artifacts/evidence-bundle/) | EV, Dictionary, Summary; request, review | schemas/jsonschema/, templates/ev/; schema_validate_ev | 仅高级别；非法律建议。请根据官方文本验证。 |
| Art 12 – 记录保存 | [证据包](../../artifacts/evidence-bundle/), [最低证据](../../artifacts/minimum-evidence/) | EV, change_log, request, review | examples/evidence_bundle_minimal/; schema_validate_ev | 仅高级别；非法律建议。请根据官方文本验证。 |
| Art 13 – 透明度（用户信息） | [范围](../../standard/current/02-scope/) | Summary, EV; review | templates/ev/ | 仅高级别；非法律建议。请根据官方文本验证。 |
| Art 14 – 人工监督 | [最低证据](../../artifacts/minimum-evidence/) | review, exception; review, exception | templates/ev/ev_template.md | 仅高级别；非法律建议。请根据官方文本验证。 |
| Art 17 – 风险管理（高风险） | [范围](../../standard/current/02-scope/) | request, review, exception, renewal | templates/ev/ | 仅高级别；非法律建议。请根据官方文本验证。 |
| Art 26 – 透明度（有限风险） | [范围](../../standard/current/02-scope/) | Summary, EV; review | templates/ev/ | 仅高级别；非法律建议。请根据官方文本验证。 |
| Art 29 – 文档（通用AI） | [EV 模板](../../standard/current/06-ev-template/) | EV, Dictionary, Summary; request, review | schemas/jsonschema/; schema_validate_ev | 仅高级别；非法律建议。请根据官方文本验证。 |
| Art 52 – 透明度（部署者） | [最低证据](../../artifacts/minimum-evidence/) | EV, Summary; review | templates/ev/ | 仅高级别；非法律建议。请根据官方文本验证。 |
| 序言 – 问责 | [证据包](../../artifacts/evidence-bundle/) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | 仅高级别；非法律建议。请根据官方文本验证。 |
