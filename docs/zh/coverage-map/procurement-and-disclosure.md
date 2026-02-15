---
description: 采购与披露叠加（英国、日本）。英国 ATRS、英国采购指南、日本政府 GenAI 采购与 AI 商业指南。仅为参考映射。
---
<!-- aimo:translation_status=translated -->

# 采购与披露叠加（英国、日本）

本页说明 AIMO 证据与选定**英国**及**日本**采购与披露框架之间的**参考映射**。仅为**参考映射**；AIMO 不取代正式检查表或政府指南。

## 英国：ATRS 与 AI 采购

| 主题 | AIMO 证据 / 映射 | 备注 |
| --- | --- | --- |
| **英国 ATRS**（AI 透明度记录） | Summary、review（问责负责人）、evidence（模型/系统描述）、dictionary（风险考量）。配置文件：`coverage_map/profiles/uk_atrs_procurement.json`。 | 于外部表单附上或参照 ATRS 式透明度记录；以 logical_id 链接组合对象。 |
| **英国采购指南** | Request、review、exception；以证据包供供应商评估。 | 以 AIMO 组合结构化证据供采购评估；正式英国指南仍为权威。 |

## 日本：政府 GenAI 采购与 AI 商业指南

| 主题 | AIMO 证据 / 映射 | 备注 |
| --- | --- | --- |
| **日本政府 GenAI 采购检查表** | 将检查表作为外部表单附上（例如 payload：JP_PROCUREMENT_CHECKLIST）；在 manifest 中参照。配置文件：`coverage_map/profiles/jp_gov_genai_procurement.json`。 | 仅参考映射；AIMO 不取代正式检查表。 |
| **AI 商业指南** | Summary、dictionary；在有利于可追溯性时将检查表项目映射至 AIMO 分类代码。 | 供可解释性使用；请对照日本正式指南验证。 |

## 使用方式

- **外部表单**：将英国或日本正式模板/检查表**原样**附上（PDF、DOC 等），进行哈希，并列于证据包 [payload_index](../../standard/current/09-evidence-bundle-structure/) 或 [EV 模板外部表单章节](../../standard/current/06-ev-template/)。在 manifest 与映射中以 logical_id 参照。
- **配置文件**：上列配置文件定义可选用的机器可读映射；不施加法律或契约义务。

级别见 [符合性](../../conformance/)；叠加摘要见 [最低证据 — 法规叠加](../../artifacts/minimum-evidence/)。
