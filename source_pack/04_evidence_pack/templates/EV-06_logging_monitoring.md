# EV-06: Logging & Monitoring / ログ・監視

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
| **EV** (Evidence Type) | `EV-006` | Logging & Monitoring |

---

## 1. Logging Overview / ログ概要

### 1.1 Logging Objectives / ログの目的

- Accountability: Track who used AI and when
- Audit: Support compliance and audit requirements
- Security: Detect anomalies and potential incidents
- Troubleshooting: Diagnose issues and errors

### 1.2 Log Types / ログ種別

| Log Type | Content | Retention | Storage |
| --- | --- | --- | --- |
| Access Log | User, timestamp, action | 90 days | SIEM |
| Prompt Log | User, prompt (sanitized) | 30 days | Secure storage |
| Response Log | Response metadata | 30 days | Secure storage |
| Error Log | Error details | 90 days | SIEM |
| Audit Log | Admin actions | 1 year | WORM storage |

---

## 2. Log Content Specification / ログ内容仕様

### 2.1 Required Log Fields / 必須ログフィールド

| Field | Description | Example |
| --- | --- | --- |
| timestamp | ISO-8601 format | 2026-01-31T10:00:00Z |
| user_id | User identifier (anonymized if needed) | user-12345 |
| session_id | Session identifier | sess-abcdef |
| action | Type of action | prompt, response, error |
| source_ip | Client IP (if applicable) | 192.168.1.1 |
| ai_system_id | AI system identifier | AI-001 |
| status | Result status | success, error |

### 2.2 Prompt/Response Logging / プロンプト/レスポンスログ

| Attribute | Value |
| --- | --- |
| **Log Prompts** | Yes / No / Sanitized |
| **Log Responses** | Yes / No / Metadata only |
| **PII Handling** | _e.g., Masked, Tokenized, Not logged_ |
| **Encryption** | _e.g., AES-256 at rest_ |

---

## 3. Monitoring Configuration / 監視設定

### 3.1 Metrics Monitored / 監視メトリクス

| Metric | Threshold | Alert Level | Action |
| --- | --- | --- | --- |
| Request rate | > 1000/min | Warning | Notify ops |
| Error rate | > 5% | Critical | Notify security |
| Response time | > 5s avg | Warning | Notify ops |
| Unusual access pattern | Anomaly detection | Warning | Review |

### 3.2 Alerting Configuration / アラート設定

| Alert | Condition | Recipients | Channel |
| --- | --- | --- | --- |
| High error rate | Error rate > 5% | IT Security | Slack, Email |
| Unusual volume | Request spike | Ops team | PagerDuty |
| Security anomaly | Pattern match | Security | SIEM alert |

---

## 4. Log Access & Protection / ログアクセス・保護

### 4.1 Access Control / アクセス制御

| Role | Access Level | Purpose |
| --- | --- | --- |
| Security Team | Full | Incident investigation |
| Audit Team | Read (subset) | Compliance audit |
| Ops Team | Read (non-sensitive) | Troubleshooting |
| AI System Owner | Read (own system) | Usage monitoring |

### 4.2 Log Integrity / ログ完全性

| Control | Implementation |
| --- | --- |
| Tamper protection | WORM storage for audit logs |
| Integrity verification | Hash chain / digital signature |
| Backup | Daily backup to separate location |

---

## 5. Retention & Disposal / 保持・廃棄

| Log Type | Retention Period | Disposal Method | Legal Basis |
| --- | --- | --- | --- |
| Access Log | 90 days | Secure delete | Internal policy |
| Prompt Log | 30 days | Secure delete | Privacy policy |
| Audit Log | 1 year | Secure delete | Regulatory |

---

## 6. Monitoring Dashboard / 監視ダッシュボード

| Dashboard | Purpose | Access | Update Frequency |
| --- | --- | --- | --- |
| AI Usage Overview | Volume, user metrics | AI Governance | Real-time |
| Security Monitoring | Anomalies, alerts | Security | Real-time |
| Compliance Dashboard | Audit metrics | Audit | Daily |

---

## 7. References / 参照

- Related Evidence: [EV-05 Controls Approvals](./EV-05_controls_approvals.md), [EV-07 Incident Exception](./EV-07_incident_exception.md)
- Logging Policy:
- SIEM Configuration:

---

## Revision History / 改訂履歴

| Date | Version | Author | Changes |
| --- | --- | --- | --- |
| YYYY-MM-DD | 0.1.0 | | Initial draft |
