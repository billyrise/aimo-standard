---
description: v0.2 参考路线图。审计对象 SSOT、Evidence-as-Code、输出配置、测试库、生命周期、JNC。
---
<!-- aimo:translation_status=translated -->

# v0.2 路线图（参考）

本页摘要**未来主版本**（v0.2）的规划方向。**仅供参考**；各版本的规范以该版本之标准与模式为准。目标时间表：2026 Q4–2027。

## 规划主题

| 主题 | 摘要 |
| --- | --- |
| **审计对象模型（SSOT）** | Requirement、Control、Claim、Evidence、Test、Finding、Remediation、Approval、Scope、VersionChange 作为具固定 ID 与参照完整性之规范对象。 |
| **外部框架桥接** | EU 附件 IV、GPAI 表单、ISO 42001、NIST AI RMF 之输出配置；机器可读映射与可选一键导出。 |
| **Evidence-as-Code** | 规范完整性：签名验证、出处（如 SLSA 式）、可重现性与变更跟踪。 |
| **测试程序库** | 每项控制之标准测试模板；与 ISAE 3000、SOC 2、ISO 19011 对齐。 |
| **运营生命周期** | 事件驱动流程（Intake → Review → Exception → Renewal → Change → Decommission）及必要日志与证据。 |
| **行业/法域配置** | 依行业与法域之可选配置。 |
| **正当不符合（JNC）** | 记录并正当化故意不符合之可选机制（参考）。 |
| **OSCAL 链接** | 将证据包链接至 Control/Requirement 以导出至 NIST OSCAL 或类似格式之标准方式。 |

## 参考资料

- [v0.1 对象模型范围](https://github.com/billyrise/aimo-standard/blob/main/source_pack/07_release/v0.1_object_model_scope.md) — v0.1 MUST 与保留
- [签名验证路线图](../../../artifacts/signature-verification-roadmap/) — 签署与验证演进
- [Releases](../../../releases/) — 发布资产与变更日志
