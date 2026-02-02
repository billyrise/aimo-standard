---
description: AIMO 标准贡献指南 - 如何贡献代码、文档和翻译。问题和PR指南。
---

# 贡献

本页提供向 AIMO 标准贡献的指南。

## 快速开始

1. Fork 仓库
2. 创建功能分支
3. 按照以下指南进行更改
4. 运行质量检查
5. 提交拉取请求

## 关键原则

| 原则 | 描述 |
| --------- | ----------- |
| 英语是规范的 | 先编辑 `docs/en/`，然后更新 `docs/ja/` |
| SSOT | 此仓库是单一事实来源 |
| 不要手动编辑生成的文件 | 编辑源文件，重新生成，提交 |
| 所有更改通过 PR | 即使是维护者也使用拉取请求 |

## 质量检查

在提交 PR 之前，运行：

```bash
# 激活虚拟环境
source .venv/bin/activate

# 运行检查
python tooling/checks/lint_i18n.py
python tooling/checks/lint_schema.py
python tooling/audit/baseline_audit.py --check

# 构建文档
mkdocs build --strict
```

## 变更类型

| 类型 | 示例 | 审查要求 |
| ---- | -------- | ------------------- |
| 规范性 | 模式更改、要求 | 维护者 + 讨论 |
| 非规范性 | 错别字、澄清 | 维护者批准 |
| i18n | 翻译 | 结构必须与 EN 匹配 |
| 工具 | CI/CD、脚本 | 维护者批准 |

## i18n 指南

### 更新顺序

1. 编辑英语源（`docs/en/...`）
2. 更新日语翻译（`docs/ja/...`）
3. 运行 `lint_i18n.py` 验证一致性
4. 一起提交

### 结构要求

- 两种语言使用相同的文件名
- 相同的标题层次结构
- 每个部分的页面数量相同

## PR 清单

提交 PR 时，验证：

- [ ] 已识别变更类型（docs / schema / examples / tooling）
- [ ] 已完成破坏性变更评估
- [ ] i18n：EN 和 JA 一起更新（如适用）
- [ ] 质量检查通过
- [ ] 已链接相关问题

## 破坏性变更

破坏性变更需要：

1. 实施前的问题讨论
2. 按照 [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) 进行版本升级
3. 带有迁移指南的变更日志条目

## 符合性声明更新

要添加或修改符合性声明：

1. 更新覆盖映射 YAML
2. 更新相应的文档页面
3. 运行验证器测试
4. 记录映射理由

## 完整指南

请参阅 [CONTRIBUTING.md](https://github.com/billyrise/aimo-standard/blob/main/CONTRIBUTING.md) 获取根级别指南。

## 相关页面

- [治理](index.md) — 项目治理
- [本地化指南](../contributing/localization.md) — i18n 详情
- [责任边界](responsibility-boundary.md) — AIMO 提供什么
