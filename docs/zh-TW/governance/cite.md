---
description: AIMO 標準引用指南 - 如何在學術論文、稽核報告和提案中引用。CITATION.cff 和 BibTeX 格式。
---

# 如何引用

本頁提供在學術論文、稽核報告和提案中引用 AIMO 標準的指引。

## CITATION.cff

儲存庫包含一個遵循引用檔案格式標準的 [CITATION.cff](https://github.com/billyrise/aimo-standard/blob/main/CITATION.cff) 檔案。

GitHub 會自動從此檔案顯示引用資訊。

## 建議引用

### 簡短形式（行內）

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

### APA 格式

> AIMO Standard Contributors. (2026). *AIMO Standard* (Version 0.0.2) [Software]. https://standard.aimoaas.com/

## 特定版本引用

引用特定版本時：

> AIMO Standard Contributors. (2026). AIMO Standard v0.0.2. https://github.com/billyrise/aimo-standard/releases/tag/v0.0.2

## 稽核文件

用於稽核報告和合規文件：

| 欄位 | 值 |
| ----- | ----- |
| 標準名稱 | AIMO Standard |
| 版本 | （指定使用的版本，例如 v0.0.1） |
| 網站 | https://standard.aimoaas.com/ |
| 儲存庫 | https://github.com/billyrise/aimo-standard |
| 發布 | https://github.com/billyrise/aimo-standard/releases |

## URL 指引

### 規範 URL

在官方文件中使用這些 URL：

| 用途 | URL |
| ------- | --- |
| 最新文件 | https://standard.aimoaas.com/latest/ |
| 特定版本 | https://standard.aimoaas.com/0.0.2/ |
| GitHub 發布 | https://github.com/billyrise/aimo-standard/releases |

!!! note "網站路徑格式"
    網站路徑使用不帶 `v` 前綴的版本號。對於版本 `v0.0.1`，在 URL 中使用 `/0.0.1/`。

### 避免使用

- GitHub Pages 鏡像 URL（臨時）
- 特定分支的 URL（可能會變更）

## 相關頁面

- [信任套件](trust-package.md) — 稽核員就緒材料
- [治理](index.md) — 專案治理
- [授權](license.md) — 授權條款
