# EV-05: Controls & Approvals / 統制・承認

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
| **EV** (Evidence Type) | `EV-005` | Controls & Approvals |

---

## 1. Control Framework / 統制フレームワーク

### 1.1 Applicable Frameworks / 適用フレームワーク

| Framework | Applicability | Status |
| --- | --- | --- |
| ISO/IEC 42001 | Full | In Progress |
| NIST AI RMF | Reference | Aligned |
| EU AI Act | Partial | Monitoring |
| Internal AI Policy | Full | Implemented |

---

## 2. Control Inventory / 統制一覧

| Control ID | Control Name | Type | Risk Addressed | Status | Owner |
| --- | --- | --- | --- | --- | --- |
| CTL-001 | Data Classification | Preventive | RS-001 | Implemented | IT |
| CTL-002 | Access Control | Preventive | RS-001, RS-002 | Implemented | IT Security |
| CTL-003 | User Training | Preventive | RS-005 | Implemented | HR |
| CTL-004 | Prompt Logging | Detective | RS-001, RS-002 | Implemented | IT |
| CTL-005 | Output Review | Detective | RS-005 | Partial | Business |
| CTL-006 | Vendor Assessment | Preventive | RS-003 | Implemented | Procurement |

---

## 3. Control Details / 統制詳細

### CTL-001: Data Classification / データ分類

| Attribute | Description |
| --- | --- |
| **Objective** | Ensure data is classified before AI processing |
| **Description** | All data input to AI systems must be classified per DT codes |
| **Implementation** | Data classification labels in input workflow |
| **Evidence** | Classification logs, user attestations |
| **Testing Frequency** | Quarterly |
| **Last Tested** | YYYY-MM-DD |
| **Test Result** | Pass |

### CTL-002: Access Control / アクセス制御

| Attribute | Description |
| --- | --- |
| **Objective** | Restrict AI system access to authorized users |
| **Description** | SSO integration, role-based access, API key management |
| **Implementation** | SSO, RBAC, API gateway |
| **Evidence** | Access logs, RBAC configuration |
| **Testing Frequency** | Monthly |
| **Last Tested** | YYYY-MM-DD |
| **Test Result** | Pass |

---

## 4. Approval Records / 承認記録

### 4.1 Initial Approval / 初回承認

| Attribute | Value |
| --- | --- |
| **Request ID** | REQ-2026-001 |
| **Requested By** | _Requester Name_ |
| **Request Date** | YYYY-MM-DD |
| **Scope** | _AI system deployment for internal productivity_ |
| **Risk Assessment Ref** | [EV-04 Risk Impact](./EV-04_risk_impact.md) |
| **Approver** | _Approver Name, Title_ |
| **Approval Date** | YYYY-MM-DD |
| **Approval Decision** | Approved |
| **Conditions** | _e.g., Annual review required_ |

### 4.2 Subsequent Approvals / 後続承認

| Approval ID | Type | Date | Approver | Decision | Notes |
| --- | --- | --- | --- | --- | --- |
| APR-001 | Scope Change | YYYY-MM-DD | _Name_ | Approved | _Extended to new dept_ |
| APR-002 | Annual Review | YYYY-MM-DD | _Name_ | Approved | _Continued use_ |

---

## 5. Periodic Review / 定期レビュー

| Review Type | Frequency | Last Review | Next Review | Reviewer | Status |
| --- | --- | --- | --- | --- | --- |
| Risk Assessment | Annual | YYYY-MM-DD | YYYY-MM-DD | Risk Team | Current |
| Control Effectiveness | Quarterly | YYYY-MM-DD | YYYY-MM-DD | Audit | Current |
| Access Review | Monthly | YYYY-MM-DD | YYYY-MM-DD | IT Security | Current |

---

## 6. Segregation of Duties / 職務分離

| Function | Role | Separation From |
| --- | --- | --- |
| Request | Business Owner | Approval |
| Approval | IT Security / Risk | Request, Implementation |
| Implementation | IT | Approval |
| Monitoring | Audit | Implementation |

---

## 7. References / 参照

- Related Evidence: [EV-04 Risk Impact](./EV-04_risk_impact.md), [EV-06 Logging Monitoring](./EV-06_logging_monitoring.md)
- Internal AI Policy:
- Approval Workflow Documentation:

---

## Revision History / 改訂履歴

| Date | Version | Author | Changes |
| --- | --- | --- | --- |
| YYYY-MM-DD | 0.1.0 | | Initial draft |
