---
description: v0.2 參考路線圖。審計物件 SSOT、Evidence-as-Code、輸出設定檔、測試庫、生命週期、JNC。
---
<!-- aimo:translation_status=translated -->

# v0.2 路線圖（參考）

本頁摘要**未來主版本**（v0.2）的規劃方向。**僅供參考**；各版本的規範以該版本之標準與結構描述為準。目標時程：2026 Q4–2027。

## 規劃主題

| 主題 | 摘要 |
| --- | --- |
| **審計物件模型（SSOT）** | Requirement、Control、Claim、Evidence、Test、Finding、Remediation、Approval、Scope、VersionChange 作為具固定 ID 與參照完整性之規範物件。 |
| **外部架構橋接** | EU 附件 IV、GPAI 表單、ISO 42001、NIST AI RMF 之輸出設定檔；機器可讀對應與選用一鍵匯出。 |
| **Evidence-as-Code** | 規範完整性：簽章驗證、出處（如 SLSA 式）、可重現性與變更追蹤。 |
| **測試程序庫** | 每項控制之標準測試範本；與 ISAE 3000、SOC 2、ISO 19011 對齊。 |
| **營運生命週期** | 事件驅動流程（Intake → Review → Exception → Renewal → Change → Decommission）及必要日誌與證據。 |
| **產業／法域設定檔** | 依產業與法域之選用設定檔。 |
| **正當不符合（JNC）** | 紀錄並正當化故意不符合之選用機制（參考）。 |
| **OSCAL 連結** | 將證據包連結至 Control/Requirement 以匯出至 NIST OSCAL 或類似格式之標準方式。 |

## 參考資料

- [v0.1 物件模型範圍](https://github.com/billyrise/aimo-standard/blob/main/source_pack/07_release/v0.1_object_model_scope.md) — v0.1 MUST 與保留
- [簽章驗證路線圖](../../../artifacts/signature-verification-roadmap/) — 簽署與驗證演進
- [Releases](../../../releases/) — 發布資產與變更日誌
