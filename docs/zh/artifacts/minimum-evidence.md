---
description: AIMO 最低证据要求。按生命周期（申请、审查、批准、变更、更新）划分的 MUST 级清单，用于 AI 治理证据就绪。
---
<!-- aimo:translation_status=translated -->

# 最低证据要求（Minimum Evidence Requirements）

本页为面向审计方与实施方的**最低证据要求**清单，按生命周期分组定义 MUST 级最低证据要求，用于支持可解释性与证据就绪；不提供法律意见也不保证合规。

准备或审查提交物时，请与 [Evidence Bundle](../evidence-bundle/) 及 [Validator](../../standard/current/07-validator/) 一并使用本页。

## 1) 申请（Request）

- **MUST 字段**：标识符、时间戳、执行者/角色、范围（申请内容）、理由（rationale）。
- **MUST 关联**：审查及记录使用的 EV 项须可引用申请 id。
- **证明内容**：使用在批准与实施前已申请并划定范围。

## 2) 审查 / 批准（Review / Approval）

- **MUST 字段**：标识符、时间戳、执行者/角色、决定（批准/拒绝/有条件）、范围、理由、对申请的引用。
- **MUST 关联**：EV 及后续例外或更新须可引用审查 id。
- **证明内容**：在使用（或例外）前已进行规定的审查与批准。

## 3) 例外（Exception）

- **MUST 字段**：标识符、时间戳、范围、到期（或截止日）、补偿性控制、理由、对审查/申请的引用。
- **MUST 关联**：例外 → 补偿性控制；例外 → 到期；例外 → 更新（再评估到期时）。
- **证明内容**：偏离有时限、具备补偿性控制并与更新关联。

## 4) 更新 / 再评估（Renewal / Re-evaluation）

- **MUST 字段**：标识符、时间戳、执行者/角色、决定（续期/撤销/有条件）、对先前例外/申请/审查/EV 的引用。
- **MUST 关联**：更新引用被续期的例外或批准；EV 项可引用更新 id。
- **证明内容**：例外与批准按既定基准再评估并续期或撤销。

## 5) 变更日志（Change Log）

- **MUST 字段**：标识符、时间戳、执行者/角色、变更说明、引用（如受影响的 EV、申请、审查、例外、更新）。
- **MUST 关联**：变更日志条目引用其修改或触发的制品。
- **证明内容**：对包或其内容的变更已记录且可追溯。

## 6) 完整性与访问（Integrity & Access）

证据完整性与访问控制对审计依赖至关重要。AIMO 不规定具体技术控制，采用方应文档化如何满足这些预期。

### 访问控制指南

| 方面 | 指南 |
| --- | --- |
| **基于角色的访问** | 定义角色（如证据创建者、审查者、审计员、管理员）并文档化谁可创建、读取、更新或删除证据。 |
| **最小权限** | 仅授予必要最小访问；写权限限于授权人员。 |
| **访问日志** | 为审计线索记录访问事件（谁、何时、何事）。 |
| **职责分离** | 在可行范围内将证据创建与批准角色分离。 |

### 保留指南

| 方面 | 指南 |
| --- | --- |
| **保留期** | 根据法规要求与组织政策（如财务审计 5–7 年）定义并文档化保留期。 |
| **保留计划** | 维护计划，说明保留哪些证据、保留多久、何时可处置。 |
| **诉讼保留** | 支持在诉讼或调查中暂停正常保留/删除的流程。 |

### 不可篡改选项

| 选项 | 说明 |
| --- | --- |
| **加密哈希** | 为证据文件生成 SHA-256（或更强）哈希；单独存储哈希以供验证。 |
| **WORM 存储** | 对证据归档使用一次写入多次读取（WORM）存储以防篡改。 |
| **仅追加日志** | 使用仅追加审计日志进行变更跟踪。 |
| **数字签名** | 对证据包签名以证明来源并检测篡改。 |

### 审计线索预期

| 要素 | 需文档化内容 |
| --- | --- |
| **变更日志** | 记录谁在何时因何变更了何内容（见 Change Log 生命周期组）。 |
| **访问日志** | 记录谁在何时以何目的访问了证据。 |
| **系统日志** | 保留支持证据完整性主张的相关系统日志（认证、授权）。 |
| **验证记录** | 文档化定期完整性验证（哈希核对、审计审查）。 |

### 证明内容

- **证据已保全**：哈希、WORM、签名等完整性机制表明证据未被篡改。
- **访问受控**：访问日志与角色定义表明谁有访问权及最小权限已落实。
- **支持审计依赖**：综合上述要素使审计方对证据可靠性有信心。

### 推荐运行配置

根据风险承受能力与法规要求选择配置；仅为建议，非强制。

| 方面 | 轻量 | 标准 | 严格 |
| --- | --- | --- | --- |
| **用途** | 内部试点、低风险 AI | 生产系统、中等风险 | 受监管行业、高风险 AI |
| **保留期** | 1–2 年 | 5–7 年 | 7–10+ 年或法规最低 |
| **不可篡改** | SHA-256 哈希 | SHA-256 + 仅追加日志 | WORM 存储 + 数字签名 |
| **访问控制** | 基于角色（基础） | 基于角色 + 访问日志 | 职责分离 + 完整审计线索 |
| **审计线索** | 仅变更日志 | 变更日志 + 访问日志 | 完整系统日志 + 定期验证 |
| **验证频率** | 按需 | 季度 | 月度或持续 |
| **Validator 使用** | 可选 | 提交前必须 | 必须 + 自动化 CI 检查 |

!!! note "保留期为示例"
    所示保留期仅为示例。组织须根据适用法律、合同、行业要求及内部政策确定保留期。

!!! tip "如何选择"
    - **轻量**：适用于实验、内部工具或正式审计可能性低的低风险场景。
    - **标准**：适用于多数生产部署，可能接受审计但非持续。
    - **严格**：适用于受监管行业（金融、医疗、政府）或风险影响显著的 AI 系统。

## 重要说明

本最低集支持可解释性与证据就绪；本身不提供法律意见也不保证合规。

包结构与 TOC 见 [Evidence Bundle](../evidence-bundle/)；字段级对齐见 [EV Template](../../standard/current/06-ev-template/) 与 schemas。[Log Schemas](../log-schemas/) 为 Shadow AI 发现与代理活动证据的规范化日志格式。

## 法规叠加（参考）

以下**叠加**描述在特定法规或采购情境中常被要求的额外证据，仅供**参考**；请将官方模板/清单原样附于 EV Template 的 [External Forms 节](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is)，并在 manifest 中以 logical_id 引用。

| 叠加 | 通常预期的额外制品 | 附于 | 配置（可选） |
| --- | --- | --- | --- |
| **EU 高风险** | 风险管理、技术文档（Annex IV）、日志、人类监督、透明性（Art 50）、事件报告 | payload_index；Evidence Bundle + Annex IV 配置 | `eu_ai_act_annex_iv.json`、`eu_ai_act_high_risk.json` |
| **EU GPAI CoP** | Model Documentation Form（透明性、版权、安全与保障） | External Forms；logical_id 如 GPAI_MODEL_DOC_FORM | `eu_gp_ai_cop.json` |
| **NIST GenAI** | GenAI 配置制品（模型适配、评估、监测） | payload_index；change_log；External Forms / GenAI 记录 | `nist_ai_600_1_genai.json` |
| **UK ATRS / 采购** | ATRS 透明性记录、问责负责人、采购评估说明 | External Forms；Summary、review | `uk_atrs_procurement.json` |
| **JP 采购** | 政府 GenAI 采购清单、AI 商业指南清单 | External Forms；logical_id 如 JP_PROCUREMENT_CHECKLIST | `jp_gov_genai_procurement.json` |

配置文件名格式为 `coverage_map/profiles/<target>_<purpose>.json`，均含 `target_version`。英国与日本见 [Coverage Map — Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/)；EU 与 NIST 见 [EU AI Act](../../coverage-map/eu-ai-act/) 与 [NIST AI RMF](../../coverage-map/nist-ai-rmf/)。
