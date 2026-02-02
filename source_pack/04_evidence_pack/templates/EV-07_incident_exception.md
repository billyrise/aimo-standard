# EV-07: Incident & Exception Handling / インシデント・例外対応

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
| **EV** (Evidence Type) | `EV-007` | Incident & Exception |

---

## 1. Incident Management / インシデント管理

### 1.1 Incident Classification / インシデント分類

| Severity | Definition | Response Time | Examples |
| --- | --- | --- | --- |
| Critical | Data breach, system compromise | < 1 hour | PII leak, unauthorized access |
| High | Policy violation, significant risk | < 4 hours | Sensitive data in prompt |
| Medium | Minor policy deviation | < 24 hours | Unapproved use case |
| Low | Informational, best practice gap | < 1 week | Training needed |

### 1.2 AI-Specific Incident Types / AI固有インシデント種別

| Type | Description | RS Code |
| --- | --- | --- |
| Data Leakage | Sensitive data exposed via AI | RS-001 |
| Model Abuse | AI used for malicious purposes | RS-002 |
| Compliance Violation | Regulatory or policy breach | RS-003 |
| Output Harm | Harmful or biased output | RS-005, RS-006 |
| Unauthorized Use | Use outside approved scope | RS-003 |

---

## 2. Incident Log / インシデントログ

| ID | Date | Severity | Type | Description | Status | Resolution |
| --- | --- | --- | --- | --- | --- | --- |
| INC-001 | YYYY-MM-DD | Medium | Data Leakage | _User submitted PII in prompt_ | Closed | _User warned, training provided_ |
| INC-002 | YYYY-MM-DD | | | | | |

---

## 3. Incident Response Procedure / インシデント対応手順

### 3.1 Detection / 検知
1. Automated alerts from monitoring (EV-06)
2. User reports
3. Audit findings
4. Third-party notifications

### 3.2 Triage / トリアージ
1. Classify severity
2. Assign incident owner
3. Notify stakeholders per severity

### 3.3 Containment / 封じ込め
1. Isolate affected systems if needed
2. Revoke access if compromised
3. Preserve evidence

### 3.4 Investigation / 調査
1. Collect logs and evidence
2. Determine root cause
3. Assess impact

### 3.5 Resolution / 解決
1. Implement fix
2. Verify resolution
3. Document lessons learned

### 3.6 Post-Incident Review / 事後レビュー
1. Conduct retrospective
2. Update controls if needed
3. Update training if needed

---

## 4. Exception Management / 例外管理

### 4.1 Exception Types / 例外種別

| Type | Description | Approval Authority | Max Duration |
| --- | --- | --- | --- |
| Policy Exception | Deviation from AI policy | CISO | 6 months |
| Technical Exception | Temporary control bypass | IT Security | 3 months |
| Scope Exception | Extended use case | AI Governance | 6 months |

### 4.2 Exception Log / 例外ログ

| ID | Date | Type | Scope | Requester | Approver | Expiry | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EXC-001 | YYYY-MM-DD | Policy | _Use of public AI for internal docs_ | _Name_ | _CISO_ | YYYY-MM-DD | Active |
| EXC-002 | | | | | | | |

### 4.3 Exception Details / 例外詳細

#### EXC-001: _Example Exception_

| Attribute | Value |
| --- | --- |
| **Exception ID** | EXC-001 |
| **Request Date** | YYYY-MM-DD |
| **Requester** | _Name, Department_ |
| **Scope** | _Describe what the exception allows_ |
| **Justification** | _Business rationale for exception_ |
| **Risk Assessment** | _Residual risk with this exception_ |
| **Compensating Controls** | _Controls in place to mitigate risk_ |
| **Approver** | _Name, Title_ |
| **Approval Date** | YYYY-MM-DD |
| **Expiry Date** | YYYY-MM-DD |
| **Review Schedule** | _Monthly / Quarterly_ |
| **Status** | Active / Expired / Revoked |

---

## 5. Compensating Controls / 代替統制

| Exception ID | Compensating Control | Implementation | Owner | Verification |
| --- | --- | --- | --- | --- |
| EXC-001 | Enhanced logging | _All prompts logged_ | IT | Monthly review |
| EXC-001 | User training | _Additional training completed_ | HR | Quarterly |

---

## 6. Exception Review / 例外レビュー

| Exception ID | Review Date | Reviewer | Decision | Notes |
| --- | --- | --- | --- | --- |
| EXC-001 | YYYY-MM-DD | _Name_ | Continue | _Risk acceptable_ |
| EXC-001 | YYYY-MM-DD | _Name_ | Expire | _Permanent solution deployed_ |

---

## 7. Metrics & Reporting / メトリクス・報告

### 7.1 Incident Metrics / インシデントメトリクス

| Metric | Current Period | Previous Period | Trend |
| --- | --- | --- | --- |
| Total Incidents | 0 | 0 | Stable |
| Critical/High | 0 | 0 | Stable |
| Mean Time to Detect | N/A | N/A | N/A |
| Mean Time to Resolve | N/A | N/A | N/A |

### 7.2 Exception Metrics / 例外メトリクス

| Metric | Value |
| --- | --- |
| Active Exceptions | 0 |
| Expired (last 90 days) | 0 |
| Pending Review | 0 |

---

## 8. References / 参照

- Related Evidence: [EV-04 Risk Impact](./EV-04_risk_impact.md), [EV-05 Controls Approvals](./EV-05_controls_approvals.md)
- Incident Response Plan:
- Exception Management Policy:

---

## Revision History / 改訂履歴

| Date | Version | Author | Changes |
| --- | --- | --- | --- |
| YYYY-MM-DD | 0.1.0 | | Initial draft |
