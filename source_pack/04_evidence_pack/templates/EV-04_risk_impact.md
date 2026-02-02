# EV-04: Risk & Impact Assessment / リスク影響評価

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
| **RS** (Risk Surface) | `RS-001, RS-003, RS-005` | Data Leakage, Compliance Breach, Model Misuse |
| **OB** (Outcome / Benefit) | `OB-001` | Efficiency |
| **EV** (Evidence Type) | `EV-004` | Risk & Impact Assessment |

---

## 1. Risk Assessment Summary / リスク評価サマリー

| Risk Category (RS Code) | Likelihood | Impact | Risk Level | Mitigation Status |
| --- | --- | --- | --- | --- |
| RS-001 Data Leakage | Medium | High | High | Mitigated |
| RS-003 Compliance Breach | Low | High | Medium | Mitigated |
| RS-005 Model Misuse | Medium | Medium | Medium | In Progress |

---

## 2. Detailed Risk Analysis / 詳細リスク分析

### RS-001: Data Leakage / 情報漏えい

| Attribute | Description |
| --- | --- |
| **Risk Description** | _Unintended disclosure of internal data via AI prompts or responses_ |
| **Threat Scenarios** | _1. User inputs confidential data 2. Model retains/learns from prompts_ |
| **Affected Assets** | _Internal documents, customer data_ |
| **Likelihood** | Medium |
| **Impact** | High |
| **Risk Score** | High |
| **Existing Controls** | _DLP, user training, vendor agreement (no training on data)_ |
| **Residual Risk** | Medium |
| **Mitigation Plan** | _Implement prompt filtering, enhance monitoring_ |

### RS-003: Compliance Breach / 法令/規程違反

| Attribute | Description |
| --- | --- |
| **Risk Description** | _Violation of privacy laws or internal policies_ |
| **Threat Scenarios** | _1. Cross-border data transfer 2. Processing without consent_ |
| **Affected Regulations** | _GDPR, APPI, internal AI policy_ |
| **Likelihood** | Low |
| **Impact** | High |
| **Risk Score** | Medium |
| **Existing Controls** | _DPA, legal review, data classification_ |
| **Residual Risk** | Low |
| **Mitigation Plan** | _Regular compliance review_ |

### RS-005: Model Misuse / モデル誤用

| Attribute | Description |
| --- | --- |
| **Risk Description** | _Inappropriate reliance on AI outputs or use beyond intended scope_ |
| **Threat Scenarios** | _1. Treating AI output as authoritative 2. Using for restricted purposes_ |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Risk Score** | Medium |
| **Existing Controls** | _User guidelines, output disclaimers_ |
| **Residual Risk** | Medium |
| **Mitigation Plan** | _Enhanced training, usage monitoring_ |

---

## 3. Impact Assessment / 影響評価

### 3.1 Business Impact / ビジネス影響

| Impact Type | Severity | Description |
| --- | --- | --- |
| Financial | Medium | _Potential regulatory fines, remediation costs_ |
| Reputational | High | _Trust damage if data breach occurs_ |
| Operational | Low | _Minimal operational disruption expected_ |
| Legal | Medium | _Regulatory investigation possible_ |

### 3.2 Stakeholder Impact / ステークホルダー影響

| Stakeholder | Impact Description |
| --- | --- |
| Employees | _Privacy concerns if personal data processed_ |
| Customers | _Data protection concerns_ |
| Regulators | _Compliance expectations_ |
| Partners | _Contractual obligations_ |

---

## 4. Risk Treatment Plan / リスク対応計画

| Risk | Treatment | Action | Owner | Due Date | Status |
| --- | --- | --- | --- | --- | --- |
| RS-001 | Mitigate | Implement prompt filtering | IT Security | YYYY-MM-DD | In Progress |
| RS-003 | Accept | Document residual risk | Legal | YYYY-MM-DD | Done |
| RS-005 | Mitigate | Enhanced user training | HR | YYYY-MM-DD | Planned |

---

## 5. Risk Acceptance / リスク受容

| Risk | Residual Level | Accepted By | Acceptance Date | Review Date |
| --- | --- | --- | --- | --- |
| RS-001 | Medium | _CISO_ | YYYY-MM-DD | YYYY-MM-DD |
| RS-003 | Low | _Legal Head_ | YYYY-MM-DD | YYYY-MM-DD |

---

## 6. References / 参照

- Related Evidence: [EV-05 Controls Approvals](./EV-05_controls_approvals.md), [EV-07 Incident Exception](./EV-07_incident_exception.md)
- Risk Assessment Framework:
- Previous Risk Assessments:

---

## Revision History / 改訂履歴

| Date | Version | Author | Changes |
| --- | --- | --- | --- |
| YYYY-MM-DD | 0.1.0 | | Initial draft |
