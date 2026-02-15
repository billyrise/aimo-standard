---
description: AIMO Standard 与欧盟 AI 法的映射。AIMO 分类代码与欧盟 AI 法风险类别及要求之间的可追溯性。
---
<!-- aimo:translation_status=translated -->

# 欧盟 AI 法映射

> 可追溯性快捷方式：分类法 → 最低证据 → 验证器 → 人工监督协议。

- [分类法](../../standard/current/03-taxonomy/)
- [最低证据要求](../../artifacts/minimum-evidence/)
- [日志模式](../../artifacts/log-schemas/)
- [验证器](../../validator/)
- [人工监督协议](../../governance/human-oversight-protocol/)

本页将选定的欧盟 AI 法主题（文件、记录保存、风险管理、人工监督、透明度）映射至 AIMO 证据与工件。仅为高阶映射，**不**构成法律意见或保证符合。请对照正式法律文本验证。

**参考：** 条例 (EU) 2024/1689（人工智能法）。下列条号均指该条例。

## 映射表

| 框架参照 / 主题 | AIMO 证据 / 在 AIMO 中的位置 | 证据包 / 最低证据 | 工件与验证 | 备注 |
| --- | --- | --- | --- | --- |
| 第 4 条 – AI 素养 | [范围](../../standard/current/02-scope/) | Summary、EV；review | templates/ev/ | 跨领域；组织能力/培训证据（高阶）。非法律意见。请对照官方文本验证。 |
| 第 9 条 – 风险管理系统 | [范围](../../standard/current/02-scope/) | request、review、exception、renewal | templates/ev/ | 高风险 AI 系统（第三章）。非法律意见。请对照官方文本验证。 |
| 第 10 条 – 数据与数据治理 | [字典](../../standard/current/05-dictionary/) | Dictionary、EV | schemas/jsonschema/；schema_validate_dictionary | 非法律意见。请对照官方文本验证。 |
| 第 11 条 – 技术文档（高风险） | [EV 模板](../../standard/current/06-ev-template/)、[证据包](../../artifacts/evidence-bundle/) | EV、Dictionary、Summary；request、review | schemas/jsonschema/、templates/ev/；**附件 IV**：见 [示例 > EU 附件 IV 示例](../../examples/)（`examples/evidence_bundle_v01_annex_iv_sample/`）；配置文件：`coverage_map/profiles/eu_ai_act_annex_iv.json`。示例组合符合规范（signatures/、hashes/、具附件 IV 导向技术文档的 payload）。详见示例（更多示例内容于后续版本提供）。 | 仅高阶；非法律意见。请对照官方文本验证。 |
| 第 12 条 – 记录保存 | [证据包](../../artifacts/evidence-bundle/)、[最低证据](../../artifacts/minimum-evidence/) | EV、change_log、request、review | examples/evidence_bundle_minimal/；schema_validate_ev | 非法律意见。请对照官方文本验证。 |
| 第 13 条 – 对部署者/使用者的透明度与信息提供 | [范围](../../standard/current/02-scope/) | Summary、EV；review | templates/ev/ | 高风险情境。非法律意见。请对照官方文本验证。 |
| 第 14 条 – 人工监督 | [最低证据](../../artifacts/minimum-evidence/) | review、exception | templates/ev/ev_template.md | 非法律意见。请对照官方文本验证。 |
| 第 15 条 – 准确性、稳健性、网络安全 | [最低证据](../../artifacts/minimum-evidence/) | EV（证据代码/风险代码，高阶） | templates/ev/ | 仅高阶映射。非法律意见。请对照官方文本验证。 |
| 第 17 条 – 质量管理体系 | [范围](../../standard/current/02-scope/) | Summary、review（组织流程） | templates/ev/ | 与第 9 条（风险管理系统）有别。非法律意见。请对照官方文本验证。 |
| 透明度义务（依使用情境） | [范围](../../standard/current/02-scope/)、[最低证据](../../artifacts/minimum-evidence/) | Summary、EV；review | templates/ev/ | 适用规定依使用情境（如有限风险、部署者义务）而异。非法律意见。请对照官方文本验证。 |
| GPAI 模型义务 | [EV 模板](../../standard/current/06-ev-template/)、[证据包](../../artifacts/evidence-bundle/) | EV 模板、证据包（证据结构化框架） | schemas/jsonschema/；schema_validate_ev | AIMO 提供组织证据的框架；实际义务由条例界定。非法律意见。请对照官方文本验证。 |
| 前言 – 问责 | [证据包](../../artifacts/evidence-bundle/) | EV、request、review、change_log | examples/evidence_bundle_minimal/；schema_validate_ev | 非法律意见。请对照官方文本验证。 |

## 生效日 / 适用性（高阶）

以下对齐**欧盟官方时间表**（AI 法服务台/委员会）。**非法律意见**，亦不保证正确性。请一律以**正式法律文本**及主管机关为准。

| 阶段 | 日期 | 适用内容（高阶） |
| --- | --- | --- |
| 生效 | 2024 年 8 月 | 条例已生效；多数实体义务尚未适用。 |
| 一般规定与禁止 | 2025 年 2 月 2 日 | 禁止做法（不可接受风险）；部分与 AI 素养相关规定。 |
| GPAI 规则与治理 | 2025 年 8 月 2 日 | 指定机构、GPAI、治理、保密、罚则；行为准则。 |
| 多数规则 + 附件 III 高风险 + 第 50 条透明度 | 2026 年 8 月 2 日 | 高风险 AI 系统（附件 III）全面适用、第 50 条透明度义务。 |
| 纳入受管制产品的高风险 | 2027 年 8 月 2 日 | 受欧盟产品法规规范的产品内嵌高风险 AI 系统。 |

## 协调标准与推定符合（第 40 条）

依 AI 法在欧盟公报公布**协调标准**后，符合该标准可对相关要求产生**推定符合**。确切清单与日期依标准化工作与公报公布而定。AIMO 映射仅供参考，不授予推定符合。现行状态请见下方**参考资料**之委员会与 AI 办公室来源。

## 2026 年 AI 办公室指南（实施细节）

欧洲委员会表示**AI 办公室**将于 2026 年拟定**实务指南**，包括：

- 高风险分类
- 第 50 条（透明度）实施
- 事件报告
- 与 QMS 相关要素

上述指南为 AIMO 配置文件与映射的**更新触发**：公布后，采用者应使证据与映射与最新官方指南一致。AIMO 不解释亦不保证符合该指南。

!!! warning "非法律意见"
    本页仅供参考。您必须依正式条例及任何实施或修正法案验证适用性与日期。AIMO 不提供法律意见亦不保证符合。

## 参考资料

- [条例 (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689)（EUR-Lex）— 人工智能法
- [欧盟 AI 法实施时间表](https://artificialintelligenceact.eu/implementation-timeline)（AI 法服务台/委员会对齐；参考用）
- 欧洲委员会 / AI 办公室 — 指南与时间表（请以委员会新闻与 AI 法服务台查询最新 URL）
- [EPRS — 欧盟 AI 法实施](https://www.europarl.europa.eu/thinktank/) — 议会简报（参考用）
