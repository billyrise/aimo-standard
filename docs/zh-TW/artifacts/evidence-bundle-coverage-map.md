---
description: 證據包覆蓋範圍對應範本（v0.1）。面向稽核方的一頁摘要 — 範圍、證據類型、控制對應、排除、完整性證明。
---
<!-- aimo:translation_status=translated -->

# 證據包覆蓋範圍對應（範本）

!!! info "參考 — 推薦做法"
    本頁定義一頁式證據包覆蓋範圍對應的**推薦做法範本**。**非**標準規範性要求。用於記錄套件所涵蓋與未涵蓋範圍以便稽核交接。對框架等的引用穩定；採用由實作方自行決定。

---

## 1. 範圍

| 項目 | 說明 |
|------|--------------|
| **範圍參照** | 套件 manifest 的 `scope_ref`（如 `SC-001`）。將本套件與宣告的範圍關聯。 |
| **Bundle ID** | `bundle_id`（UUID）— 本套件的一識別碼。 |
| **Bundle 版本** | `bundle_version`（SemVer）— 套件的版本。 |
| **期間 / 快照** | 選用：本套件所代表的時間段或快照日期（如 2026-Q1、as-of 2026-02-03）。 |

---

## 2. 證據類型（EV / objects 與 payloads）

| 類別 | 內容 | v0.1 最小例 |
|----------|----------|------------------------|
| **object_index** | 列舉物件（中繼資料、索引）。每項：`id`, `type`, `path`, `sha256`。 | 如 `objects/index.json`（index 類型）。 |
| **payload_index** | 承載檔案（根 EV JSON、Evidence Pack 檔案）。每項：`logical_id`, `path`, `sha256`, `mime`, `size`。 | 如 `payloads/root.json`（根 AIMO EV JSON）。 |
| **EV 類型** | 證據記錄（根或連結承載內）— request, review, exception, renewal, change log。 | 與 [Evidence Pack 範本](../../standard/current/06-ev-template/) 及 [最低證據要求](../minimum-evidence/) 一致。 |

*實作者可擴充 object_index 與 payload_index；路徑須保持在套件根內並滿足 [證據包根結構（v0.1）](../../standard/current/09-evidence-bundle-structure/)。*

---

## 3. 控制對應（僅供參考）

與外部框架的對應**僅供參考**；標準不強制任何特定法規的合規。

| 框架 | 本套件中的使用 | 參考 |
|-----------|--------------------|-----------|
| **ISO/IEC 42001** | 選用：文件化本套件支援的 AI MS 主題。 | [Coverage Map → ISO 42001](../../coverage-map/iso-42001/) |
| **EU AI Act** | 選用：高階文件/記錄保存對齊。 | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/) |
| **NIST AI RMF** | 選用：Govern、Map、Measure、Manage 對應。 | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/) |
| **EU GPAI CoP** | 選用：Model Documentation Form；在 External Forms 中附上並以 logical_id 引用。 | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/)；設定 `eu_gp_ai_cop.json` |
| **NIST AI RMF / GenAI** | 選用：GenAI 設定（AI 600-1）產物。 | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/)；設定 `nist_ai_600_1_genai.json` |
| **UK ATRS** | 選用：ATRS 記錄、採購評估。 | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/)；設定 `uk_atrs_procurement.json` |
| **JP Gov GenAI 採購** | 選用：JP 採購清單、AI Business Guidelines。 | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/)；設定 `jp_gov_genai_procurement.json` |
| **ISMS (27001/27002)** | 選用：變更管理、存取、日誌、完整性。 | [Coverage Map → ISMS](../../coverage-map/isms/) |

*「本套件中的使用」依每次提交填寫；標準不要求任何特定控制涵蓋。*

### External Forms 與 manifest 引用

**External Forms**（原樣附上的官方範本/清單）應在套件的 **payload_index** 中列出，並具備穩定的 `logical_id`、`path`、`sha256`、`mime`、`size`。稽核方可從 manifest 追溯到檔案並驗證雜湊。見 [EV Template — External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) 與 [EV Template — Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index)。

---

## 4. 排除 / 假設

| 領域 | 本套件**不涵蓋**的內容（示例列 — 依提交調整） |
|------|-------------------------------------------------------------------------------|
| **排除** | 如：範圍外的系統/使用案例、無證據的第三方元件、本套件期間以外。 |
| **假設** | 如：Dictionary/分類法版本、所用 validator/結構描述版本、保管與保留由實作定義。 |
| **限制** | 如：v0.1 中簽章驗證在範圍外；不對法規進行法律解釋。 |

*將佔位文字替換為提交專用的排除與假設。*

---

## 5. 完整性證明摘要（v0.1）

| 要素 | 提供內容（v0.1 規範性） |
|---------|----------------------------------|
| **manifest.json** | 存在且結構描述有效；含 `object_index`、`payload_index`、`hash_chain`、`signing`。 |
| **sha256** | `object_index` 與 `payload_index` 中每個檔案宣告 64 字元小寫 hex sha256；Validator 檢查內容一致。 |
| **索引存在** | 所列路徑均在套件根下存在；無路徑遍歷（`../` 或前導 `/`）。 |
| **簽章存在** | `signatures/` 中至少一個簽章檔案；manifest 透過 `signing.signatures[]` 引用 `path` 與 `targets`（v0.1 的 targets 須含 `manifest.json`）。v0.1 不包含密碼學驗證。 |
| **Hash chain** | manifest 中的 `hash_chain`：`algorithm`、`head`（64 字元 hex）、`path`（`hashes/` 下檔案）、`covers`（v0.1 須含 `manifest.json` 與 `objects/index.json`）。`hash_chain.path` 處檔案存在。 |

*本表概括 [Validator](../../validator/) 對 v0.1 套件檢查的完整性保證。Custody（儲存、存取控制、保留）由實作定義。*

---

## Coverage Map（YAML）與設定（JSON）

| 產物 | 狀態 | 目的 |
|----------|--------|---------|
| **Coverage Map YAML**（`coverage_map/coverage_map.yaml` 等） | **參考** | AIMO 證據/產物與外部框架（ISO 42001、NIST AI RMF、EU AI Act 等）的高階對應主題，用於可解釋性。不施加規範性驗證要求。 |
| **Profile JSON**（`coverage_map/profiles/*.json`） | **規範** | 依 `schemas/jsonschema/aimo-profile.schema.json` 驗證的轉換規格。定義機器可讀對應（如哪些 AIMO 物件對應哪些框架條款）。[Validator](../../validator/) 使用 `--validate-profiles` 確保所有官方 profile JSON 符合結構描述（profile_id PR-* 模式、target 列舉、target_version、mappings）。 |

### 官方設定（Validator 驗證）

Profile JSON 位於 `coverage_map/profiles/`，由 Validator（`--validate-profiles`）驗證。命名：檔名 `<target>_<purpose>.json`；每檔含 `target_version`。

| 檔案 | profile_id | target | target_version |
|------|------------|--------|----------------|
| `iso42001.json` | PR-ISO42001-v0.1 | ISO_42001 | 1.0 |
| `iso_42001_readiness.json` | PR-ISO42001-READINESS-v0.1 | ISO_42001 | 2023 |
| `nist_ai_rmf.json` | PR-NIST-AI-RMF-v0.1 | NIST_AI_RMF | 1.0 |
| `nist_ai_600_1_genai.json` | PR-NIST-AI-600-1-v0.1 | NIST_AI_600_1 | 1.0 |
| `eu_ai_act_annex_iv.json` | PR-EU-AI-ACT-ANNEX-IV-v0.1 | EU_AI_ACT_ANNEX_IV | Annex IV |
| `eu_ai_act_high_risk.json` | PR-EU-AI-ACT-HIGH-RISK-v0.1 | EU_AI_ACT_HIGH_RISK | 2024/1689 |
| `eu_gp_ai_cop.json` | PR-EU-GPAI-COP-v0.1 | EU_GPAI_COP | current |
| `uk_atrs_procurement.json` | PR-UK-ATRS-v0.1 | UK_ATRS | current |
| `jp_gov_genai_procurement.json` | PR-JP-GOV-GENAI-PROCUREMENT-v0.1 | JP_GOV_GENAI_PROCUREMENT | current |

### 設定更新政策

- **EU AI Act 引用（0.1.2）**：為證據就緒一致，Coverage Map 與文件中的 EU AI Act 條文引用已與 Regulation (EU) 2024/1689 對齊；僅供參考，非法律意見。
- **ISO 42001 / NIST AI RMF**：目標框架新版本可在未來標準版本中以新設定檔或新 `target_version` 加入；v0.1 設定在 v0.1 發布中凍結。
- **EU AI Act Annex IV**：Annex IV 及相關條文可能由監管機構更新；設定對應可透過 **PATCH**（如 0.1.x）隨條文或條款變更更新，並保持同一 profile_id 以延續。實作者應與設定中 `target_version` 及發布說明所引版本一致。

---

## 參見

- [證據包（產物概覽）](../evidence-bundle/)
- [證據包根結構（v0.1）](../../standard/current/09-evidence-bundle-structure/)
- [最低證據要求](../minimum-evidence/)
- [Coverage Map（框架對應）](../../coverage-map/)
- [Validator](../../validator/)
