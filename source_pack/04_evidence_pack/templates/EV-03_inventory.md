# EV-03: AI Inventory / AI資産台帳

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
| **LG** (Log/Event Type) | `LG-003` | Inventory |

---

## 1. AI System Inventory / AIシステム台帳

| ID | System Name | Provider | Model | Version | Status | Owner | Last Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AI-001 | _Example System_ | _OpenAI_ | _GPT-4_ | _2024-01_ | Active | _IT Dept_ | YYYY-MM-DD |
| AI-002 | | | | | | | |

---

## 2. AI Service Inventory / AIサービス台帳

| ID | Service Name | Vendor | Contract ID | Start Date | End Date | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SVC-001 | _Example Service_ | _Vendor A_ | _CTR-001_ | YYYY-MM-DD | YYYY-MM-DD | Active |
| SVC-002 | | | | | | |

---

## 3. Model Details / モデル詳細

### AI-001: _Example System_

| Attribute | Value |
| --- | --- |
| **Provider** | _OpenAI / Anthropic / etc._ |
| **Model Name** | _GPT-4 / Claude 3 / etc._ |
| **Model Version** | _YYYY-MM version_ |
| **API Endpoint** | _api.openai.com_ |
| **Hosting Type** | _SaaS / On-prem / Hybrid_ |
| **Data Processing Location** | _USA / EU / Japan_ |
| **Training Data Opt-out** | _Yes / No_ |
| **Enterprise Agreement** | _Yes / No_ |
| **DPA Signed** | _Yes / No_ |

---

## 4. Integration Points / 連携ポイント

| AI System | Integrated With | Integration Type | Data Exchanged |
| --- | --- | --- | --- |
| AI-001 | _Internal App A_ | API | _User queries_ |
| AI-001 | _Logging System_ | API | _Audit logs_ |

---

## 5. Access Control / アクセス制御

| AI System | Access Method | Authorized Users | Authentication |
| --- | --- | --- | --- |
| AI-001 | _Web UI_ | _All employees_ | _SSO_ |
| AI-001 | _API_ | _Dev team_ | _API Key + IP whitelist_ |

---

## 6. Lifecycle Status / ライフサイクル状態

| AI System | Status | Deployment Date | Next Review | Retirement Plan |
| --- | --- | --- | --- | --- |
| AI-001 | Active | YYYY-MM-DD | YYYY-MM-DD | N/A |
| AI-002 | Deprecated | YYYY-MM-DD | N/A | YYYY-MM-DD |

---

## 7. Compliance Mapping / コンプライアンスマッピング

| AI System | Applicable Regulations | Compliance Status | Notes |
| --- | --- | --- | --- |
| AI-001 | _GDPR, APPI_ | Compliant | _DPA signed_ |
| AI-001 | _ISO 42001_ | In progress | _Assessment scheduled_ |

---

## 8. References / 参照

- Related Evidence: [EV-01 System Overview](./EV-01_system_overview.md), [EV-04 Risk Impact](./EV-04_risk_impact.md)
- Vendor Contracts:
- Security Assessments:

---

## Revision History / 改訂履歴

| Date | Version | Author | Changes |
| --- | --- | --- | --- |
| YYYY-MM-DD | 0.1.0 | | Initial draft |
