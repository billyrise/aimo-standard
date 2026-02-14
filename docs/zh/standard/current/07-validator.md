---
description: AIMO 验证器 - 确保证据包符合 AIMO 标准模式。合规检查的验证规则、错误处理和参考实现。
---

# 验证器

AIMO 验证器确保证据包和相关工件符合 AIMO 标准模式和要求。

另请参阅：[人工监督协议](../../../governance/human-oversight-protocol/) — 机器与人工审查的责任边界。

## 实践中的验证器

有关30秒快速入门（安装、运行、解释输出），请参阅 [验证器中心](../../../validator/)。

## 验证器 MVP 要求

最小可行验证器必须执行以下检查：

### 1. 必需字段验证

检查所有必需字段是否存在：

| 工件 | 必需字段 |
| --- | --- |
| 证据包清单 | pack_id, pack_version, taxonomy_version, created_date, last_updated, codes, evidence_files |
| 代码对象 | FS, UC, DT, CH, IM, RS, EV（OB 可选） |
| 证据文件条目 | file_id（EP-01..EP-07）, filename, title（ev_type / ev_codes 可选） |

### 2. 维度代码验证

检查每个必需维度是否至少有一个代码：

| 维度 | 要求 |
| --- | --- |
| FS（功能范围） | 恰好1个代码 |
| UC（用例类别） | 至少1个代码 |
| DT（数据类型） | 至少1个代码 |
| CH（渠道） | 至少1个代码 |
| IM（集成模式） | 恰好1个代码 |
| RS（风险面） | 至少1个代码 |
| OB（结果/收益） | 可选（0个或多个） |
| LG（日志/记录类型） | 至少1个代码 |

### 3. 字典存在检查

验证所有代码是否存在于分类法字典中：

- 为指定的 `taxonomy_version` 加载分类法字典
- 验证清单中的每个代码是否存在于字典中
- 报告无效代码及其维度和值

### 4. 代码格式验证

检查所有代码是否匹配预期格式：

```regex
^(FS|UC|DT|CH|IM|RS|OB|LG)-\d{3}$
```

### 5. 模式验证

针对 JSON Schema 进行验证：

| 模式 | 目的 |
| --- | --- |
| `evidence_pack_manifest.schema.json` | 证据包清单 |
| `taxonomy_pack.schema.json` | 分类法包定义 |
| `changelog.schema.json` | 变更日志条目 |

## 验证规则

### 规则：必需维度

```yaml
rule_id: required_dimensions
description: 所有必需维度必须至少有一个代码
severity: error
check: |
  - FS: 恰好1个
  - UC: 至少1个
  - DT: 至少1个
  - CH: 至少1个
  - IM: 恰好1个
  - RS: 至少1个
  - LG: 至少1个
```

### 规则：有效代码

```yaml
rule_id: valid_codes
description: 所有代码必须存在于分类法字典中
severity: error
check: |
  对于 manifest.codes 中的每个代码：
    - 代码存在于指定 taxonomy_version 的字典中
    - 代码状态为 'active'（如果 'deprecated' 则警告）
```

### 规则：代码格式

```yaml
rule_id: code_format
description: 所有代码必须匹配标准格式
severity: error
pattern: "^(FS|UC|DT|CH|IM|RS|OB|LG)-\\d{3}$"
```

### 规则：版本格式

```yaml
rule_id: version_format
description: 版本必须是有效的 SemVer
severity: error
pattern: "^\\d+\\.\\d+\\.\\d+$"
fields:
  - pack_version
  - taxonomy_version
```

## 错误输出格式

验证错误按以下格式报告：

```
<路径>: <严重性>: <消息>
```

**示例：**

```
codes.FS: error: 必需维度 'FS' 没有代码
codes.UC[0]: error: 代码 'UC-999' 不存在于字典 v0.1.0 中
pack_version: error: 无效的版本格式 'v1.0'（预期 SemVer）
codes.RS[1]: warning: 代码 'RS-002' 在 v0.2.0 中已弃用
```

## 验证器不检查什么

验证器关注结构符合性，而非内容质量：

| 方面 | 原因 |
| --- | --- |
| 内容准确性 | 验证器检查结构，而非含义 |
| 证据完整性 | 模板是指南，不是强制格式 |
| 交叉引用解析 | 不验证文件是否存在 |
| 时间戳有效性 | 不严格验证 ISO-8601 |
| ID 唯一性 | 当前未强制执行 |
| 完整性哈希 | 采用者责任 |

## 参考实现

Python 参考实现提供在：

```
validator/src/validate.py
```

### 使用

```bash
python validator/src/validate.py <manifest.json>
```

### 示例输出

```
验证中: evidence_pack_manifest.json
分类法版本: 0.1.0

检查必需维度...
  FS: OK (1个代码)
  UC: OK (3个代码)
  DT: OK (1个代码)
  CH: OK (1个代码)
  IM: OK (1个代码)
  RS: OK (3个代码)
  OB: OK (2个代码)
  LG: OK (7个代码)

检查代码有效性...
  所有代码有效。

验证: 通过
```

## 版本控制政策

验证器规则遵循 SemVer：

- **MAJOR**：破坏性规则更改（使现有有效包失败的新必需检查）
- **MINOR**：新的可选检查、警告或信息性消息
- **PATCH**：不更改验证结果的错误修复

## 模式参考

| 模式 | 位置 |
| --- | --- |
| 证据包清单 | `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json` |
| 分类法包 | `source_pack/03_taxonomy/schemas/taxonomy_pack.schema.json` |
| 变更日志 | `source_pack/03_taxonomy/schemas/changelog.schema.json` |

## 参考

- [分类法](../03-taxonomy/) - 维度定义
- [代码](../04-codes/) - 代码格式
- [字典](../05-dictionary/) - 代码字典
- [验证器规则](../../../validator/) - 完整规则文档
