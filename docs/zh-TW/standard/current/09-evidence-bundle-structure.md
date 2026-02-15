---
description: 證據包之規範根結構與 manifest（v0.1）。完整性為 MUST；保管為實作定義。
---
<!-- aimo:translation_status=translated -->

# 證據包根結構（v0.1）

本頁定義證據包之**規範**根配置與 manifest。驗證器必須在進行任何結構描述驗證前，拒絕不符合這些要求的組合。

## v0.1 規範 MUST（摘要）

- 組合根目錄下**必須**有 **manifest.json**。
- **object_index** 與 **payload_index**：每筆條目必須包含 **sha256**（64 位小寫十六進位）；路徑必須為相對路徑，且不得包含 `../` 或脫離組合根目錄。
- **signing.signatures** 必須為非空陣列（空陣列無效）。
- 每筆簽章條目必須具備：位於 `signatures/` 下之 **path**（禁止路徑遍歷）、**targets**（陣列，至少一路徑），且組合內至少一組簽章必須在 **targets** 中列出 **manifest.json**（manifest 簽章為強制）。
- **hash_chain**：v0.1 必須包含 **algorithm**、**head**、**path**（位於 `hashes/` 下）以及 **covers**（至少含 **manifest.json** 與 **objects/index.json**）。

驗證器必須在接受組合前強制上述規則。JSON Schema 與參考驗證器實作相同規則。

## 根必要結構（MUST）

組合根目錄下必須存在下列項目：

| 項目 | 類型 | 用途 |
| --- | --- | --- |
| **manifest.json** | 檔案 | 組合 manifest（見下）。組合的標準描述子。 |
| **objects/** | 目錄 | 列舉物件（如詮釋資料、索引）。列於 `manifest.json` 之 `object_index`。 |
| **payloads/** | 目錄 | Payload 檔案（如根 EV JSON、Evidence Pack 檔案）。列於 `manifest.json` 之 `payload_index`。 |
| **signatures/** | 目錄 | 數位簽章。v0.1 必須至少包含一組參照 manifest 的簽章檔案（存在與目標參照；密碼學驗證為未來擴充）。 |
| **hashes/** | 目錄 | 雜湊鏈或完整性紀錄（依 `manifest.json` 之 `hash_chain` 所需）。 |

實作者不得提交缺少任一项的組合。根結構不完整時，驗證器必須以明確訊息失敗。

## 完整性（規範）與保管（實作）

- **完整性**在 v0.1 為**規範**：標準要求組合具備完整性詮釋資料（manifest、索引檔案之 sha256、manifest 之簽章存在）。驗證器必須檢查：
  - 必要目錄與檔案存在。
  - `manifest.json` 存在且有效（結構描述與前結構描述檢查）。
  - `object_index` 與 `payload_index` 所列每個檔案在給定路徑存在，且內容與宣告之 `sha256` 一致。
  - `signatures/` 至少包含一組以 manifest 為目標的簽章（v0.1：僅存在與參照；v0.1.1：建議驗證詮釋資料；v0.2 規劃：密碼學驗證納入範圍）。
- **保管**（儲存、存取控制、保留、WORM）為**實作定義**。標準不規定保管人如何儲存或保護組合；僅要求提交時之套件滿足上述完整性要求。

## manifest.json（MUST 欄位）

manifest 至少須包含：

| 欄位 | 類型 | 說明 |
| --- | --- | --- |
| **bundle_id** | string (UUID) | 本組合之唯一識別碼。 |
| **bundle_version** | string (SemVer) | 組合版本。 |
| **created_at** | string (date-time) | 建立時間戳。 |
| **scope_ref** | string | 範圍參照（如 `SC-001`）。模式 `SC-*`。 |
| **object_index** | array | 物件清單：`id`、`type`、`path`、`sha256`。路徑必須為相對、不得含 `../` 或以 `/` 開頭，且須位於證據包根目錄內（驗證器必須拒絕脫離組合根之路徑）。 |
| **payload_index** | array | Payload 清單：`logical_id`、`path`、`sha256`、`mime`、`size`。路徑規則與 object_index 相同（相對、無 `../`、無前導 `/`、位於組合根內）。 |
| **hash_chain** | object | **規範 (v0.1)：** 必須包含 `algorithm`（sha256 \| merkle）、`head`（64 位小寫十六進位）、`path`（`hashes/` 下之相對路徑；無 `../`、無前導 `/`）及 `covers`（陣列，至少一元素）。v0.1 之 `covers` 必須包含 `manifest.json` 與 `objects/index.json`。 |
| **signing** | object | **規範 (v0.1)：** 必須包含 `signatures`（陣列，至少一筆）。每筆須具：`signature_id`（如 SIG-... 或 UUID）、`path`（`signatures/` 下相對路徑；無 `../`、無前導 `/`）、`targets`（陣列，至少一路徑；v0.1 至少一組簽章之 targets 須含 `manifest.json`）、`algorithm`（ed25519、rsa-pss、ecdsa、unspecified 之一）。`created_at`（date-time）為 MAY。**註：** v0.1 不涵蓋簽章之密碼學驗證；僅要求參照（哪個檔案、目標為何）。 |

**v0.1.1 選用簽章詮釋資料（建議供第三方重新執行）：**

| 欄位 | 類型 | 說明 |
| --- | --- | --- |
| **signer_identity** | string | 簽署者身分（如 PGP 指紋、did:key）。 |
| **signed_at** | string (date-time) | 簽章施加時間（ISO 8601）。 |
| **verification_command** | string | 供審計員重新執行驗證的範例 CLI 指令。 |
| **canonicalization** | string | 簽署 payload 之標準化方式：`rfc8785_json`、`cbor` 或 `unspecified`。 |

完整性與驗證：**v0.1** — 僅參照與存在。**v0.1.1** — 建議驗證用詮釋資料。**v0.2**（規劃）— 密碼學驗證納入範圍。

- **sha256** 值必須為 64 位小寫十六進位字元。
- **path** 必須為相對路徑；不得包含 `../` 或以 `/` 開頭；路徑須位於證據包根目錄內。
- manifest 可包含明確自參照（如於 `object_index` 或專用欄位），使 manifest 自身完整性被涵蓋；驗證器必須接受 manifest 列於某索引或由某簽章明確參照的組合。

JSON Schema 見：`schemas/jsonschema/evidence_bundle_manifest.schema.json`。

## 未來擴充（參考）

- **Control/Requirement 連結**：未來版本可能新增將證據包元素連結至 Control 或 Requirement 識別碼的標準方式（例如匯出至 NIST OSCAL 或類似審計自動化格式）。v0.1 與 v0.1.1 不要求。

## 參考資料

- [證據包（人工產物總覽）](../../../artifacts/evidence-bundle/) — 目的與目次
- [EV 範本 — 外部表單與審計交接索引](../06-ev-template/#external-forms-official-templateschecklists-attached-as-is) — 附上正式範本／檢查表及於 manifest 參照之方式
- [簽章驗證路線圖](../../../artifacts/signature-verification-roadmap/) — v0.1.1 詮釋資料與 v0.2 驗證計畫
- [驗證器](../../../validator/) — 驗證器如何強制此結構
- [最低證據要求](../../../artifacts/minimum-evidence/) — MUST 級檢查表
