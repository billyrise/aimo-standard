---
description: AIMO 标准与 ISMS（ISO 27001/27002）的映射。AIMO 分类法与信息安全管理系统控制之间的可追溯性。
---

# ISMS 视图（ISO/IEC 27001/27002）映射

> 可追溯性快捷方式：分类法 → 最低证据 → 验证器 → 人工监督协议。

- [分类法](../../standard/current/03-taxonomy/)
- [最低证据要求](../../artifacts/minimum-evidence/)
- [日志模式](../../artifacts/log-schemas/)
- [验证器](../../validator/)
- [人工监督协议](../../governance/human-oversight-protocol/)

本页将选定的 ISO/IEC 27001/27002 主题（变更管理、访问控制、日志、证据完整性）映射到 AIMO 证据和工件。这仅用于可解释性；不保证符合 ISO/IEC 27001 或 27002。请根据已发布的标准进行验证。


## 映射表

| 框架引用/主题 | AIMO 证据/在 AIMO 中的位置 | 证据包/最低证据 | 工件与验证 | 说明 |
| --- | --- | --- | --- | --- |
| A.5.24 – 项目管理中的信息安全 | [范围](../../standard/current/02-scope/) | request, review | templates/ev/ | 仅供参考；请根据官方文本验证。 |
| A.5.29 – 中断期间的信息安全 | [最低证据](../../artifacts/minimum-evidence/) | exception, renewal | templates/ev/ev_template.md | 仅供参考；请根据官方文本验证。 |
| A.5.30 – 业务连续性的ICT就绪 | [概述](../../standard/current/01-overview/) | Summary; integrity | — | 仅供参考；请根据官方文本验证。 |
| A.8.1 – 资产清单 | [字典](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | 仅供参考；请根据官方文本验证。 |
| A.8.2 – 信息分类 | [分类法](../../standard/current/03-taxonomy/) | Dictionary; review | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | 仅供参考；请根据官方文本验证。 |
| A.8.3 – 访问控制 | [最低证据](../../artifacts/minimum-evidence/) | —; integrity | — | 仅供参考；请根据官方文本验证。 |
| A.8.15 – 日志 | [EV 模板](../../standard/current/06-ev-template/) | EV, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | 仅供参考；请根据官方文本验证。 |
| A.8.16 – 监控活动 | [最低证据](../../artifacts/minimum-evidence/) | EV, change_log; change_log, integrity | templates/ev/ | 仅供参考；请根据官方文本验证。 |
| A.8.32 – 变更管理 | [证据包](../../artifacts/evidence-bundle/) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | 仅供参考；请根据官方文本验证。 |
| A.8.33 – 测试信息 | [验证器](../../standard/current/07-validator/) | EV | validator/rules/, validator/src/; schema_validate_ev | 仅供参考；请根据官方文本验证。 |
