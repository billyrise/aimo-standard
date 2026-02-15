---
description: AIMO Standard 符合性級別。組織如何聲明符合、證據要求，以及各符合性級別對 AI 治理的意義。
---
<!-- aimo:translation_status=translated -->

# 符合性

!!! warning "重要：非認證、非確信、非法律符合聲明"
    AIMO Standard 定義的是**證據包裝與驗證格式**。不認證對法律或標準的符合。
    審計與確信意見由獨立審計員及採用組織自行負責。
    **適當聲明：**「證據包係依 AIMO Standard v0.1.2 產製，並經 AIMO 驗證器進行結構驗證。」
    <!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
    **不當聲明：**「符合歐盟 AI 法」、「ISO 42001 認證」、「政府核可」。
    <!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

上述層級為包裝與可追溯性之**內部證據成熟度**。**不是**認證、**不是**確信意見，也**不是**法律或法規符合。

!!! note "層級名稱別名"
    最高層級過去在非正式討論中曾稱「Gold」；**正式層級名稱為 Audit-Ready**。

## AIMO 符合性架構（AIMO-MS / AIMO-Controls / AIMO-Audit）

| 元件 | 說明 | 證據期望 |
| --- | --- | --- |
| **AIMO-MS** | 管理系統導向結構：可支援 ISO/IEC 42001 型控制之方針、角色、PDCA 對齊人工產物。 | Request、review、exception、renewal、change log；Summary 與 Dictionary。 |
| **AIMO-Controls** | 生命週期與完整性控制：request→review→exception→renewal、雜湊、簽章（依 [證據包結構](../../standard/current/09-evidence-bundle-structure/)）。 | Object_index、payload_index、hash_chain、signing；生命週期紀錄。 |
| **AIMO-Audit** | 審計交接準備：驗證器通過、校驗和、選用聲明與審計交接索引。 | 驗證器輸出、bundle_id、產製者身分、選用簽章詮釋資料與交接索引。 |

證據期望詳見 [最低證據要求](../artifacts/minimum-evidence/) 與 [證據包](../artifacts/evidence-bundle/)。

## 符合性級別（僅 AIMO）

### 級別 1 — Foundation

**目的：** 可追溯基線。使組合可識別、可驗證完整性並經驗證器檢查之最小集合。

| 項目 | 要求 |
| --- | --- |
| **必要人工產物** | [證據包](../artifacts/evidence-bundle/) 結構（manifest.json、objects/、依規格之 payload_index）；[驗證器](../validator/) 通過；連結至 [最低證據](../artifacts/minimum-evidence/)。 |
| **典型審計提問** | 範圍為何？誰產製組合？雜湊可否驗證？ |
| **典型落差** | 缺少 manifest 詮釋資料（bundle_id、created_at、producer）；未執行或未附驗證器。 |

### 級別 2 — Operational

**目的：** 營運控制證據。在 Foundation 上建立生命週期軌跡與監控。

| 項目 | 要求 |
| --- | --- |
| **必要人工產物** | 全部 Foundation MUST 項目；生命週期控制軌跡（request／核准、review、exception 或「無例外」、renewal 排程）；至少一項監控人工產物（事件日誌或定期檢查或人工監督抽樣）；具完整性連結之 change log；證明與確信邊界聲明。 |
| **典型審計提問** | 誰核准使用？例外如何追蹤？最近一次審查時間？ |
| **典型落差** | 審查／核准未連結至 request；無監控人工產物；change log 未參照受影響物件。 |

### 級別 3 — Audit-Ready

**目的：** 審計交接品質。完整聲明、可重現性與外部表單欄位。

| 項目 | 要求 |
| --- | --- |
| **必要人工產物** | 全部 Operational MUST 項目；至少一組涵蓋 manifest 的數位簽章（簽署者身分＋演算法）；TSA 或「無 TSA」聲明；可重現套件（確切驗證器指令、預期輸出、環境詮釋資料）；外部表單章節附上正式範本／檢查表並交叉參照；有界完整性聲明；單頁審計交接索引（人工產物 → 雜湊 → 產製者 → 日期）。 |
| **典型審計提問** | 審計員如何重新執行驗證？外部檢查表在哪裡、如何對應至組合？ |
| **典型落差** | 有簽章但未記載簽署者／演算法；無交接索引；外部表單未雜湊或未於 manifest 參照。 |

## 各級別最低證據（摘要）

| 級別 | MUST（摘要） |
| --- | --- |
| **Foundation** | 組合結構（manifest、object_index、payload_index）；所參照物件之 sha256；bundle_id、created_at、producer；驗證器執行＋版本；證據字典基線（系統名稱、擁有者、目的、資料類別、生命週期階段）；存取與保留聲明（對象、期間、儲存類型、防篡改）。SHOULD：最少一筆 change log 條目。 |
| **Operational** | 全部 Foundation MUST；生命週期軌跡（request／核准、review、exception 或「無」、renewal＋最近 renewal）；≥1 監控人工產物；change log 條目參照受影響物件；明確證明與確信邊界聲明。 |
| **Audit-Ready** | 全部 Operational MUST；≥1 組針對 manifest 之簽章（簽署者身分＋演算法）；TSA 或「無 TSA」；可重現套件；外部表單列示並交叉參照；有界完整性聲明；審計交接索引。 |

所有組合依規範 [證據包結構](../../standard/current/09-evidence-bundle-structure/) 均**必須**具備簽章**存在**（至少一組以 manifest 為目標）。**Audit-Ready** 另要求更嚴格的**密碼學聲明**（簽署者身分、演算法、TSA 聲明、再驗證說明），使第三方能重新執行檢查。

## ISO/IEC 42001 對應（參考）

下表說明 AIMO 人工產物**如何支援**典型 ISO/IEC 42001 條款族之證據。僅供參考；不表示認證或符合。

| ISO/IEC 42001 條款族 | 支援證據的 AIMO 人工產物 |
| --- | --- |
| 組織情境 | Summary、Dictionary、scope_ref |
| 領導／政策 | Summary、review、dictionary |
| 規劃（風險、目標） | request、review、exception、EV、Dictionary |
| 支援（資源、能力、文件） | Summary、review、EV、change_log |
| 營運 | EV、request、review、exception；營運控制 |
| 績效評估（監控、內部稽核、管理審查） | EV、change_log、review、renewal |
| 改進 | exception、renewal、change_log |

詳見 [對應圖 — ISO/IEC 42001](../coverage-map/iso-42001/) 與 [ISO 42001 認證準備工具組](../artifacts/iso-42001-certification-readiness-toolkit/)。

## 聲明用語範本（反過度聲明）

僅使用如實描述所做事項的聲明。認證與法律符合由採用者與認可機構負責。

**可接受（範例）**

- 「本組織為 AIMO Standard v0.1.2 之 AIMO 符合（級別 2）；不表示 ISO 認證或法律符合。」
- 「我們使用 AIMO 人工產物支援 ISO/IEC 42001 準備；認證決定由認可認證機構作成。」
- 「證據包係依 AIMO Standard v0.1.2 產製，並經 AIMO 驗證器進行結構驗證。」

<!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
**不可接受（範例）**

- 「符合歐盟 AI 法」（AIMO 不認證法規符合。）
- 「ISO 42001 認證」（認證由認可認證機構核發，非 AIMO。）
- 「政府核可」（AIMO 非政府核可機制。）
<!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

## 相關頁面

- [Trust Package](../governance/trust-package/) — 審計員用整合入口
- [Responsibility Boundary](../governance/responsibility-boundary/) — AIMO 提供與不提供之內容
- [Standard (Current)](../standard/current/) — 規範要求
- [Artifacts](../artifacts/) — 證據結構與最低證據
- [Validator](../validator/) — 結構驗證
