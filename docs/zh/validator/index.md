---
description: AIMO 验证器中心 - 验证工具快速入门。30秒内安装、运行和解释结果。证据包验证和合规检查。
---
<!-- aimo:translation_status=translated -->

# 验证器

本页是验证工具和规则的中心。验证器及其规则的规范性规范在标准中。

## 快速入门（30秒）

**1. 前提条件**

```bash
pip install jsonschema   # 如果尚未安装
```

**2. 对示例包运行验证**

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

**3. 阅读报告并修复错误/警告**

示例输出（成功）：

```
OK
```

示例输出（失败）：

```
Schema validation failed:
<root>: 'version' is a required property
<root>: 'dictionary' is a required property
<root>: 'evidence' is a required property
```

退出代码：`0` = 成功，`1` = 验证错误，`2` = 使用错误。

---

## 它检查什么

- **模式验证**：根对象、字典和证据符合 JSON Schema
- **字典一致性**：所有代码存在于分类法字典中
- **代码状态**：弃用的代码警告，已删除的代码错误

## 它不检查什么

- **内容准确性**：验证器检查结构，而非含义
- **合规保证**：通过验证不保证监管合规
- **人工判断**：依赖上下文的决策需要人工审查（参见 [人工监督协议](../governance/human-oversight-protocol/)）
- **自动日志收集**：验证器验证提交的证据；它不收集日志

---

## 资源

- **规范**：[标准 > 当前 > 验证器](../standard/current/07-validator/) — 规则、参考检查以及验证与证据的关系。
- **规则和实现**：仓库 `validator/rules/`（检查）、`validator/src/`（参考实现）。运行和 CI 使用在规范中描述。
- **解释**：验证"失败"对审计师意味着什么（在规范中解释）。

有关符合性和工件使用，请参阅 [符合性](../conformance/) 和 [工件](../artifacts/)。
