---
description: AIMO Standard 符合性级别。组织如何声明符合、证据要求，以及各符合性级别对 AI 治理的意义。
---
<!-- aimo:translation_status=translated -->

# 符合性

!!! warning "重要：非认证、非鉴证、非法律符合声明"
    AIMO Standard 定义的是**证据包装与验证格式**。不认证对法律或标准的符合。
    审计与鉴证意见由独立审计员及采用组织自行负责。
    **适当声明：**「证据包系依 AIMO Standard v0.1.2 产制，并经 AIMO 验证器进行结构验证。」
    <!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
    **不当声明：**「符合欧盟 AI 法」、「ISO 42001 认证」、「政府核可」。
    <!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

AIMO Standard 定位于**鉴证/审计交接/持续证据**层：提供证据包装、验证器与可追溯性，供采用方与审计方使用结构化证据。AIMO **不是**认证机构；认证与符合性决定由认可认证机构、审计方与采用组织负责。

上述层级为包装与可追溯性之**内部证据成熟度**。**不是**认证、**不是**鉴证意见，也**不是**法律或法规符合。

## 兼容性声明（ISO/NIST/欧盟 AI 法）

下列**参考映射**将 AIMO 证据与工件链接至外部框架。用于可解释性与审计交接；**不**授予认证亦不保证符合。请对照各框架权威文本验证。

- [Coverage Map — ISO/IEC 42001](../coverage-map/iso-42001/) — 映射至 ISO/IEC 42001（AI 管理系统）
- [Coverage Map — NIST AI RMF](../coverage-map/nist-ai-rmf/) — 映射至 NIST AI 风险管理框架
- [Coverage Map — 欧盟 AI 法](../coverage-map/eu-ai-act/) — 映射至欧盟 AI 法主题（高层；非法律意见）

主要来源与声明用语见各 Coverage Map 页面及 [责任边界](../governance/responsibility-boundary/)。

## 非声明（AIMO 不声明之内容）

- AIMO **不**认证对 ISO/IEC 42001、NIST AI RMF、欧盟 AI 法或任何其他框架的符合。
- AIMO **不**保证法规或法律符合。
- AIMO **不**提供鉴证意见或法律建议。
- AIMO **不**判断组织是否满足外部要求；由采用方、审计方与认证机构负责。

!!! note "层级名称别名"
    最高层级过去在非正式讨论中曾称「Gold」；**正式层级名称为 Audit-Ready**。

## AIMO 符合性框架（AIMO-MS / AIMO-Controls / AIMO-Audit）

| 组件 | 说明 | 证据期望 |
| --- | --- | --- |
| **AIMO-MS** | 管理系统导向结构：可支持 ISO/IEC 42001 型控制的方针、角色、PDCA 对齐工件。 | Request、review、exception、renewal、change log；Summary 与 Dictionary。 |
| **AIMO-Controls** | 生命周期与完整性控制：request→review→exception→renewal、哈希、签名（依 [证据包结构](../../standard/current/09-evidence-bundle-structure/)）。 | Object_index、payload_index、hash_chain、signing；生命周期记录。 |
| **AIMO-Audit** | 审计交接准备：验证器通过、校验和、可选声明与审计交接索引。 | 验证器输出、bundle_id、产制者身份、可选签名元数据与交接索引。 |

证据期望详见 [最低证据要求](../artifacts/minimum-evidence/) 与 [证据包](../artifacts/evidence-bundle/)。

## 符合性级别（仅 AIMO）

### 级别 1 — Foundation

**目的：** 可追溯基线。使组合可识别、可验证完整性并经验证器检查的最小集合。

| 项目 | 要求 |
| --- | --- |
| **必要工件** | [证据包](../artifacts/evidence-bundle/) 结构（manifest.json、objects/、依规格的 payload_index）；[验证器](../validator/) 通过；链接至 [最低证据](../artifacts/minimum-evidence/)。 |
| **典型审计提问** | 范围为何？谁产制组合？哈希可否验证？ |
| **典型差距** | 缺少 manifest 元数据（bundle_id、created_at、producer）；未执行或未附验证器。 |

### 级别 2 — Operational

**目的：** 运营控制证据。在 Foundation 上建立生命周期轨迹与监控。

| 项目 | 要求 |
| --- | --- |
| **必要工件** | 全部 Foundation MUST 项目；生命周期控制轨迹（request/批准、review、exception 或「无例外」、renewal 排程）；至少一项监控工件（事件日志或定期检查或人工监督抽样）；具完整性链接的 change log；证明与鉴证边界声明。 |
| **典型审计提问** | 谁批准使用？例外如何跟踪？最近一次审查时间？ |
| **典型差距** | 审查/批准未链接至 request；无监控工件；change log 未参照受影响对象。 |

### 级别 3 — Audit-Ready

**目的：** 审计交接质量。完整声明、可重现性与外部表单槽位。

| 项目 | 要求 |
| --- | --- |
| **必要工件** | 全部 Operational MUST 项目；至少一组覆盖 manifest 的数字签名（签署者身份 + 算法）；TSA 或「无 TSA」声明；可重现包（确切验证器命令、预期输出、环境元数据）；外部表单章节附上正式模板/检查表并交叉参照；有界完整性声明；单页审计交接索引（工件 → 哈希 → 产制者 → 日期）。 |
| **典型审计提问** | 审计员如何重新执行验证？外部检查表在哪里、如何映射至组合？ |
| **典型差距** | 有签名但未记载签署者/算法；无交接索引；外部表单未哈希或未在 manifest 参照。 |

## 各级别最低证据（摘要）

| 级别 | MUST（摘要） |
| --- | --- |
| **Foundation** | 组合结构（manifest、object_index、payload_index）；所参照对象的 sha256；bundle_id、created_at、producer；验证器执行 + 版本；证据字典基线（系统名称、拥有者、目的、数据类别、生命周期阶段）；访问与保留声明（对象、期间、存储类型、防篡改）。SHOULD：最少一笔 change log 条目。 |
| **Operational** | 全部 Foundation MUST；生命周期轨迹（request/批准、review、exception 或「无」、renewal + 最近 renewal）；≥1 监控工件；change log 条目参照受影响对象；明确证明与鉴证边界声明。 |
| **Audit-Ready** | 全部 Operational MUST；≥1 组针对 manifest 的签名（签署者身份 + 算法）；TSA 或「无 TSA」；可重现包；外部表单列示并交叉参照；有界完整性声明；审计交接索引。 |

所有组合依规范 [证据包结构](../../standard/current/09-evidence-bundle-structure/) 均**必须**具备签名**存在**（至少一组以 manifest 为目标）。**Audit-Ready** 另要求更严格的**密码学声明**（签署者身份、算法、TSA 声明、再验证说明），使第三方能重新执行检查。

## ISO/IEC 42001 映射（参考）

下表说明 AIMO 工件**如何支持**典型 ISO/IEC 42001 条款族之证据。仅供参考；不表示认证或符合。

| ISO/IEC 42001 条款族 | 支持证据的 AIMO 工件 |
| --- | --- |
| 组织情境 | Summary、Dictionary、scope_ref |
| 领导/政策 | Summary、review、dictionary |
| 规划（风险、目标） | request、review、exception、EV、Dictionary |
| 支持（资源、能力、文档） | Summary、review、EV、change_log |
| 运营 | EV、request、review、exception；运营控制 |
| 绩效评价（监控、内部审核、管理评审） | EV、change_log、review、renewal |
| 改进 | exception、renewal、change_log |

详见 [覆盖图 — ISO/IEC 42001](../coverage-map/iso-42001/) 与 [ISO 42001 认证准备工具包](../artifacts/iso-42001-certification-readiness-toolkit/)。

## 声明用语模板（反过度声明）

仅使用如实描述所做事项之声明。认证与法律符合由采用者与认可机构负责。

**可接受（示例）**

- 「本组织为 AIMO Standard v0.1.2 之 AIMO 符合（级别 2）；不表示 ISO 认证或法律符合。」
- 「我们使用 AIMO 工件支持 ISO/IEC 42001 准备；认证决定由认可认证机构作出。」
- 「证据包系依 AIMO Standard v0.1.2 产制，并经 AIMO 验证器进行结构验证。」

<!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
**不可接受（示例）**

- 「符合欧盟 AI 法」（AIMO 不认证法规符合。）
- 「ISO 42001 认证」（认证由认可认证机构核发，非 AIMO。）
- 「政府核可」（AIMO 非政府核可机制。）
<!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

## 相关页面

- [Trust Package](../governance/trust-package/) — 审计员用整合入口
- [Responsibility Boundary](../governance/responsibility-boundary/) — AIMO 提供与不提供之内容
- [Standard (Current)](../standard/current/) — 规范要求
- [Artifacts](../artifacts/) — 证据结构与最低证据
- [Validator](../validator/) — 结构验证
