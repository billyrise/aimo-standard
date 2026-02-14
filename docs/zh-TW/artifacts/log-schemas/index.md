---
description: AIMO 日誌結構描述 - AI 證據的廠商中立日誌格式。包含 Shadow AI 發現和代理活動監控結構描述。
---

# 日誌結構描述

## 這是什麼

本節定義了可納入證據包的**標準化日誌格式**。這些結構描述為與 AI 使用監控和代理式操作相關的日誌提供廠商中立的結構。

## 何時使用

- **Shadow AI 可見性**：記錄未經核准 AI 使用的偵測、清查和補救。
- **代理式操作稽核**：說明自主代理的權限執行、工具執行和遞迴操作。
- **事件可重現性**：為事件調查和根本原因分析提供結構化證據。

## 這不是什麼

!!! warning "重要"
    這些結構描述定義了**用於證據提交的日誌格式**。它們不會：

    - 自動從您的系統收集日誌
    - 提供日誌彙總或監控工具
    - 保證符合任何法規或標準
    - 取代廠商特定的日誌實作

    組織必須實作自己的日誌收集管道，並將日誌標準化為這些結構描述以進行證據提交。

## 結構描述

| 結構描述 | 用途 | 下載 |
| --- | --- | --- |
| [Shadow AI 發現日誌](shadow-ai-discovery/) | 未經核准 AI 使用的偵測和清查 | [shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json) |
| [代理活動日誌](agent-activity/) | 代理式 AI 權限執行和工具執行 | [agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json) |

## 相關頁面

- [最低證據要求](../minimum-evidence/) — 必要層級證據檢查清單
- [證據包](../evidence-bundle/) — 套件結構和目錄
- [分類法](../../standard/current/03-taxonomy/) — 分類代碼（包含 UC-010 代理式自動化、IM-007 Shadow/未受管理）
