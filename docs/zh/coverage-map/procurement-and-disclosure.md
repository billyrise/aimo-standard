---
description: 采购与披露叠加（英国、日本）。英国 ATRS、英国采购指南、日本政府 GenAI 采购与 AI 商业指南。仅为参考映射。
---
<!-- aimo:translation_status=translated -->

# 采购与披露叠加（英国、日本）

本页说明 AIMO 证据与选定**英国**及**日本**采购与披露框架之间的**参考映射**。旨在**通过复用 AIMO 证据减轻负担**。仅为**参考映射**；AIMO 不保证完全满足政府要求。请对照下列官方来源验证。

## 主要来源

**英国**

- [Algorithmic Transparency Recording Standard (ATRS) Hub](https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub) — GOV.UK（模板、指南、已发布记录）
- [ATRS 模板](https://www.gov.uk/government/publications/algorithmic-transparency-template) — 公共部门官方模板
- [使用 ATRS 的组织指南](https://www.gov.uk/government/publications/guidance-for-organisations-using-the-algorithmic-transparency-standard/algorithmic-transparency-recording-standard-guidance-for-public-sector-bodies) — GOV.UK

**日本**

- [数字厅 — GenAI 采购与利用指南](https://www.digital.go.jp/news/3579c42d-b11c-4756-b66e-3d3e35175623) — 数字厅（内阁官房）
- [AI 商业指南](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/index.html) — 经济产业省 / 总务省

## 映射表（英国）

| 政府要求（主题） | AIMO 工件 | 在 Evidence Bundle 中的位置 | 验证器覆盖 | 备注 |
| --- | --- | --- | --- | --- |
| ATRS — 问责/负责人 | Summary、review | manifest；objects/（EV、Summary）；payload_index | schema_validate_ev | 参考映射；不保证完全符合。 |
| ATRS — 系统/模型描述 | Dictionary、EV | objects/；schemas/jsonschema/aimo-dictionary.schema.json | schema_validate_dictionary | 于外部表单附上正式 ATRS 记录；以 logical_id 链接。 |
| ATRS — 风险考量 | Dictionary、request、review、exception | objects/；templates/ev/ | schema_validate_ev | 配置：`coverage_map/profiles/uk_atrs_procurement.json`。 |
| 采购 — 供应商证据 | request、review、exception；Evidence Bundle | manifest、object_index、payload_index；examples/evidence_bundle_minimal/ | schema_validate_ev | 以组合结构化证据；英国正式指南仍为权威。 |

## 映射表（日本）

| 政府要求（主题） | AIMO 工件 | 在 Evidence Bundle 中的位置 | 验证器覆盖 | 备注 |
| --- | --- | --- | --- | --- |
| GenAI 采购检查表（数字厅） | 外部表单（检查表原文）；Dictionary、Summary | payload_index；外部表单节；manifest 参照 | N/A（附件） | 参考映射；不保证完全符合。配置：`coverage_map/profiles/jp_gov_genai_procurement.json`。 |
| AI 商业指南 — 治理/可追溯性 | Summary、dictionary、request、review、change_log | objects/；manifest；templates/ev/ | schema_validate_dictionary、schema_validate_ev | 在有利于可追溯性时将列表项映射至 AIMO 分类法。 |
| 风险/责任文档 | Dictionary、EV、review、exception | objects/；schemas/jsonschema/ | schema_validate_ev | 请对照数字厅与经产省/总务省正式指南验证。 |

## 英国：ATRS 与 AI 采购（摘要）

| 主题 | AIMO 证据 / 映射 | 备注 |
| --- | --- | --- |
| **英国 ATRS**（AI 透明度记录） | Summary、review（问责负责人）、evidence（模型/系统描述）、dictionary（风险考量）。配置文件：`coverage_map/profiles/uk_atrs_procurement.json`。 | 于外部表单附上或参照 ATRS 式透明度记录；以 logical_id 链接组合对象。 |
| **英国采购指南** | Request、review、exception；以证据包供供应商评估。 | 以 AIMO 组合结构化证据供采购评估；正式英国指南仍为权威。 |

## 日本：政府 GenAI 采购与 AI 商业指南（摘要）

| 主题 | AIMO 证据 / 映射 | 备注 |
| --- | --- | --- |
| **日本政府 GenAI 采购检查表** | 将检查表作为外部表单附上（例如 payload：JP_PROCUREMENT_CHECKLIST）；在 manifest 中参照。配置文件：`coverage_map/profiles/jp_gov_genai_procurement.json`。 | 仅参考映射；AIMO 不取代正式检查表。 |
| **AI 商业指南** | Summary、dictionary；在有利于可追溯性时将检查表项目映射至 AIMO 分类代码。 | 供可解释性使用；请对照日本正式指南验证。 |

## 使用方式

- **外部表单**：将英国或日本正式模板/检查表**原样**附上（PDF、DOC 等），进行哈希，并列于证据包 [payload_index](../../standard/current/09-evidence-bundle-structure/) 或 [EV 模板外部表单章节](../../standard/current/06-ev-template/)。在 manifest 与映射中以 logical_id 参照。
- **配置文件**：上列配置文件定义可选用的机器可读映射；不施加法律或契约义务。

级别见 [符合性](../../conformance/)；叠加摘要见 [最低证据 — 法规叠加](../../artifacts/minimum-evidence/)。
