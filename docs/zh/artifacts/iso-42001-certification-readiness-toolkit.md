---
description: ISO/IEC 42001 认证就绪工具包。使用 AIMO 制品与 ISO 42001 对齐的审计就绪证据的最短路径。仅支持就绪；不授予认证。
---
<!-- aimo:translation_status=translated -->

# ISO/IEC 42001 认证就绪工具包

本页为使用 AIMO 制品产出与 **ISO/IEC 42001** 对齐的**审计就绪证据**的**实务与采用导向**指南。旨在**支持就绪**，**不**授予认证。认证决定由**认可认证机构**作出。

## 目标

产出经验证器检查的、支持 ISO/IEC 42001 型控制（语境、领导、策划、支持、运行、绩效评价、改进）的 Evidence Bundle，使审计方能高效定位并验证证据。

## 五步工作流

| 步骤 | 行动 |
| --- | --- |
| **1. 确定范围与 AI 清单** | 用 scope_ref 定义范围；使用 [分类法](../../standard/current/03-taxonomy/) 与 [字典](../../standard/current/05-dictionary/) 对 AI 系统分类。 |
| **2. 建立管理体系制品** | 创建或引用政策、角色及与 PDCA 对齐的制品。以 [AIMO-MS / AIMO-Controls](../../conformance/) 为结构；参考 [Evidence Pack 模板](../../standard/current/06-ev-template/)（EP-01..EP-07）。 |
| **3. 产出 Evidence Bundle 与最低证据** | 按 [Evidence Bundle 结构](../../standard/current/09-evidence-bundle-structure/) 构建 manifest、object_index、payload_index、hash_chain、signing。按 [最低证据要求](minimum-evidence.md) 包含 request、review、exception、renewal、change_log。 |
| **4. 运行验证器 + 校验和 + 变更控制** | 运行 `python validator/src/validate.py <bundle_path> --validate-profiles`。记录验证器版本与输出。生成 SHA-256 校验和；维护引用受影响对象的 change log。 |
| **5. 准备审计包** | 将包打包（zip 等）；提供校验和。可选附上 [审计报告输出](../../standard/current/07-validator/)（audit-json / audit-html）。引用标准时使用带版本 URL（如 `/0.1.2/`）。Audit-Ready 级别增加 [Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index) 与 [External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is)。 |

## 清单：ISO 42001 条款族 → AIMO 制品 → 证据输出

| ISO 42001 条款族 | AIMO 制品 | 证据输出 |
| --- | --- | --- |
| 语境 (4.1) | Summary、Dictionary、scope_ref | manifest scope_ref；Summary；Dictionary |
| 领导/方针 (5.x) | Summary、review、dictionary | 审查记录；方针引用 |
| 策划 (6.x) | request、review、exception、EV、Dictionary | 申请/批准；EV 或 Dictionary 中的风险/目标 |
| 支持 (7.x) | Summary、review、EV、change_log | 文档；能力/意识证据 |
| 运行 (8.x) | EV、request、review、exception | 运行控制；适用性 |
| 绩效评价 (9.x) | EV、change_log、review、renewal | 监测；内审；管理评审 |
| 改进 (10.x) | exception、renewal、change_log | 纠正措施；持续改进 |

参见 [Coverage Map — ISO/IEC 42001](../../coverage-map/iso-42001/) 与 [ISO/IEC 42006](https://www.iso.org/standard/42006) 了解审计机构预期。

## 稳妥表述

- **宜用**：“我们使用 AIMO 制品支持 ISO/IEC 42001 就绪；认证决定由认可认证机构作出。”
- **勿用**：“经 AIMO 认证符合 ISO 42001”或“AIMO 认证合规”。

## 相关

- [符合性](../../conformance/) — 级别（Foundation、Operational、Audit-Ready）与声明用语
- [Trust Package](../../governance/trust-package/) — 面向审计方的材料
- [Responsibility Boundary](../../governance/responsibility-boundary/) — AIMO 提供与不提供的内容
