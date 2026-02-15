---
description: AIMO Standard 概述。定义 AI 治理审计的共享分类法、代码体系、词典、证据模板和验证器检查。
---
<!-- aimo:translation_status=translated -->

# 概述（Overview）

**AIMO** 代表 **AI Management Office**（AI 管理办公室）。AIMO Standard 定义：
- 共享分类法
- 代码体系
- 初始词典
- EV 模板
- 验证器检查（规范 + 最小参考实现）

本仓库发布：
- 人类可读规范（HTML）
- 机器可读制品（模式/模板/示例）
- 官方 PDF 发布版

## 定位：ISO/IEC 42001（AIMS）的配套

AIMO Standard 是**证据就绪与可解释性的实施加速器**，可用于支持与 ISO/IEC 42001 对齐的 AI 管理体系（AIMS）并构建可审计证据。它不替代 ISO/IEC 42001 或任何其他管理体系标准；而是增加分类法、Evidence Bundle 结构和 Coverage Map，以帮助实施并为这些控制提供证据。

**AIMO 提供的内容**

- AI 治理分类的分类法与代码体系
- Evidence Bundle 结构（manifest、object_index、payload_index、完整性）
- 可追溯性的验证器与 Coverage Map
- 符合性等级（Foundation、Operational、Audit-Ready）— 证据打包的 AIMO 专属成熟度层级

**AIMO 不提供的内容**

- 法律建议
- ISO 认证或认证替代
- 法规符合性保证
- 审计判断或认可认证机构的替代

**为何是现在**

- **ISO/IEC 42006**（2025-07 发布）规定了按 ISO/IEC 42001 对 AI 管理体系进行审计与认证的机构要求，提高了对可审计证据与可追溯性的期望。
- **EU AI Act** 正在分阶段适用（2025–2027）；在官方公报公布的协调标准将提供符合性推定。EU AI Office 正在 2026 年准备实用指南（高风险分类、第 50 条透明度、事件、QMS 要素）。
- 采用者与认证机构越来越多地将 ISO/IEC 42001 用作 AI 治理的系统层；AIMO 帮助构建支持该层级的证据，而不主张认证。

## 参考资料

- [ISO/IEC 42006](https://www.iso.org/standard/42006) — 对 AI 管理体系进行审计与认证的机构要求
- [EU AI Act 实施时间表](https://artificialintelligenceact.eu/implementation-timeline)（AI Act Service Desk / 委员会一致；参考）
- [European Commission — Clear guidelines for AI (2025年12月4日)](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_xxxx) — AI Office 指南准备（请查阅委员会新闻获取最新 URL）
- [EPRS — EU AI Act implementation timeline (2025年6月)](https://www.europarl.europa.eu/thinktank/en/document/EPRS_BRI) — 议会简报（参考）
