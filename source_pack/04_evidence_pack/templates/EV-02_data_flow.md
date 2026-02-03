# EV-02: Data Flow / データフロー

---

## Mandatory Metadata / 必須メタデータ

| Field | Value |
| --- | --- |
| **pack_id** | `EP-EXAMPLE-001` |
| **pack_version** | `0.1.0` |
| **taxonomy_version** | `0.1.0` |
| **created_date** | `YYYY-MM-DD` |
| **last_updated** | `YYYY-MM-DD` |
| **owner** | `<Owner Name>` |

---

## AIMO Codes (8 Dimensions) / AIMOコード（8次元）

| Dimension | Code(s) | Label |
| --- | --- | --- |
| **FS** (Functional Scope) | `FS-001` | End-user Productivity |
| **UC** (Use Case Class) | `UC-001` | General Q&A |
| **DT** (Data Type) | `DT-002` | Internal |
| **CH** (Channel) | `CH-001` | Web UI |
| **IM** (Integration Mode) | `IM-001` | Standalone |
| **RS** (Risk Surface) | `RS-001` | Data Leakage |
| **OB** (Outcome / Benefit) | `OB-001` | Efficiency |
| **LG** (Log/Event Type) | `LG-002` | Data Flow |

---

## 1. Data Flow Overview / データフロー概要

_Describe the overall data flow through the AI system._

_AIシステムを通じたデータフローの全体像を記述してください。_

---

## 2. Data Flow Diagram / データフロー図

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   User      │────▶│  AI System  │────▶│   Output    │
│   Input     │     │  (Process)  │     │  (Response) │
└─────────────┘     └─────────────┘     └─────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  External   │
                    │  API/Model  │
                    └─────────────┘
```

_Replace with your actual data flow diagram._

_実際のデータフロー図に置き換えてください。_

---

## 3. Data Sources / データソース

| Source | Data Type (DT Code) | Description |
| --- | --- | --- |
| _e.g., User input_ | DT-002 (Internal) | _User-provided queries_ |
| _e.g., Database_ | DT-004 (Personal Data) | _Customer records_ |

---

## 4. Data Destinations / データ送信先

| Destination | Data Type (DT Code) | Purpose | Retention |
| --- | --- | --- | --- |
| _e.g., AI Provider API_ | DT-002 | Inference | _Vendor policy_ |
| _e.g., Logs_ | DT-002 | Audit | _90 days_ |

---

## 5. Data Processing / データ処理

### 5.1 Input Processing / 入力処理
_Describe how input data is processed before being sent to the AI model._

### 5.2 Model Processing / モデル処理
_Describe the AI model processing._

### 5.3 Output Processing / 出力処理
_Describe how output data is processed before being returned to users._

---

## 6. Data Sensitivity Analysis / データ機密性分析

| Data Element | Classification | Controls Applied |
| --- | --- | --- |
| _e.g., User query_ | Internal (DT-002) | _Encryption, access control_ |
| _e.g., Response_ | Internal (DT-002) | _Logging, retention policy_ |

---

## 7. Cross-Border Data Transfers / 国際データ移転

| Transfer | From | To | Legal Basis |
| --- | --- | --- | --- |
| _e.g., API call_ | Japan | USA | _SCCs, DPA_ |

---

## 8. References / 参照

- Related Evidence: [EV-01 System Overview](./EV-01_system_overview.md), [EV-03 Inventory](./EV-03_inventory.md)
- Data Classification Policy:
- Privacy Policy:

---

## Revision History / 改訂履歴

| Date | Version | Author | Changes |
| --- | --- | --- | --- |
| YYYY-MM-DD | 0.1.0 | | Initial draft |
