---
description: AIMO 标准引用指南 - 如何在学术论文、审计报告和提案中引用。CITATION.cff 和 BibTeX 格式。
---

# 如何引用

本页提供在学术论文、审计报告和提案中引用 AIMO 标准的指南。

## CITATION.cff

仓库包含一个遵循 Citation File Format 标准的 [CITATION.cff](https://github.com/billyrise/aimo-standard/blob/main/CITATION.cff) 文件。

GitHub 会自动显示此文件中的引用信息。

## 推荐引用

### 简短形式（行内）

> AIMO Standard Contributors. (2026). AIMO Standard. https://standard.aimoaas.com/

### BibTeX

```bibtex
@software{aimo_standard,
  author = {{AIMO Standard Contributors}},
  title = {AIMO Standard},
  url = {https://standard.aimoaas.com/},
  version = {0.0.2},
  year = {2026}
}
```

### APA 风格

> AIMO Standard Contributors. (2026). *AIMO Standard* (Version 0.0.2) [Software]. https://standard.aimoaas.com/

## 特定版本引用

引用特定版本时：

> AIMO Standard Contributors. (2026). AIMO Standard v0.0.2. https://github.com/billyrise/aimo-standard/releases/tag/v0.0.2

## 审计文档

对于审计报告和合规文档：

| 字段 | 值 |
| ----- | ----- |
| 标准名称 | AIMO Standard |
| 版本 | （指定使用的版本，例如 v0.0.1） |
| 网站 | https://standard.aimoaas.com/ |
| 仓库 | https://github.com/billyrise/aimo-standard |
| 发布 | https://github.com/billyrise/aimo-standard/releases |

## URL 指南

### 规范URL

在官方文档中使用这些URL：

| 用途 | URL |
| ------- | --- |
| 最新文档 | https://standard.aimoaas.com/latest/ |
| 特定版本 | https://standard.aimoaas.com/0.0.2/ |
| GitHub 发布 | https://github.com/billyrise/aimo-standard/releases |

!!! note "站点路径格式"
    站点路径使用不带 `v` 前缀的版本号。对于版本 `v0.0.1`，在URL中使用 `/0.0.1/`。

### 避免使用

- GitHub Pages 镜像URL（临时）
- 分支特定URL（可能会更改）

## 相关页面

- [信任包](trust-package.md) — 审计师就绪材料
- [治理](index.md) — 项目治理
- [许可证](license.md) — 许可条款
