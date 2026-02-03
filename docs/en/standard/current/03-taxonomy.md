---
description: AIMO Taxonomy - 8-dimension classification system with 91 codes for categorizing AI systems. Covers functional scope, use cases, data types, channels, integration, risks, outcomes, and evidence.
---

# Taxonomy

The AIMO Taxonomy provides a structured classification system for categorizing AI systems, their uses, and associated governance requirements. It consists of **8 dimensions** with **91 codes** that enable consistent classification and evidence management across organizations.

## Purpose

The taxonomy serves three primary purposes from an audit perspective:

1. **Explainability**: Provides a common vocabulary for describing AI use cases across the organization, supporting clear communication with auditors and stakeholders.

2. **Evidence Readiness**: Enables systematic documentation of AI systems using a standardized classification, making evidence collection and review more efficient.

3. **Comparability**: Allows organizations to compare AI use cases across different contexts using consistent terminology.

## What It Is Not (Non-Overclaim)

!!! warning "Important"
    The AIMO Standard supports **explainability and evidence readiness**. It does **not** provide legal advice, guarantee compliance, or certify conformity to any regulation or framework. See [Responsibility Boundary](../../governance/responsibility-boundary.md) for details.

The taxonomy is a classification system only. It does not:

- Guarantee compliance with any law or regulation
- Replace professional legal, security, or compliance advice
- Certify conformity to external frameworks (ISO, NIST, EU AI Act, etc.)
- Provide risk assessments or control recommendations

## Examples of AI/agentic-specific risks (why an AI-specific standard is needed)

Traditional security controls (e.g., ISMS) alone often fail to capture LLM/agent-specific failure modes and autonomous agent deviations (e.g., unintended tool execution, recursive loops) in an **audit-explainable** manner.
AIMO Taxonomy provides a shared language to classify these AI-specific risks and connect them to evidence requirements and remediation workflows.

(Reference examples for differentiation. The codes below are illustrative placeholders; the official code system follows the Standard definitions.)
- AG-01 Runaway Loop / Recursion
- AG-02 Unauthorized Tool Use (confused deputy-style misuse)
- AG-03 Privilege Boundary Drift

## Dimensions Overview

AIMO uses 8 dimensions to classify AI use cases. Each dimension has a unique 2-letter prefix.

| ID | Name | Code Count | Description |
| --- | --- | --- | --- |
| **FS** | Functional Scope | 6 | Which business function is supported |
| **UC** | Use Case Class | 30 | What type of task is performed |
| **DT** | Data Type | 10 | What data classifications are involved |
| **CH** | Channel | 8 | How users access the AI |
| **IM** | Integration Mode | 7 | How AI connects to enterprise systems |
| **RS** | Risk Surface | 8 | What risks are associated |
| **OB** | Outcome / Benefit | 7 | What benefits are expected |
| **LG** | Log/Event Type | 15 | What log/event/record type is required (request record, access log, etc.) |

**Total: 91 codes across 8 dimensions**

See [ID Policy / Namespace](./04b-id-policy-namespace.md): **EV-** is reserved for Evidence *artifact* IDs only; taxonomy log/event dimension uses **LG-** (e.g. LG-001 … LG-015).

### Usage Rules

| Dimension | Selection | Audit Implication |
| --- | --- | --- |
| FS, IM | Exactly 1 | Primary classification for responsibility assignment |
| UC, DT, CH, RS, LG | 1 or more | Complete enumeration required for risk coverage |
| OB | 0 or more | Optional; documents expected business value |

## Dimension Definitions

### FS: Functional Scope

Categorizes AI use by the business function it supports. **Select exactly one.**

| Code | Label | Definition |
| --- | --- | --- |
| FS-001 | End-user Productivity | AI used to improve productivity of internal end users (writing, search, summarization, meeting notes). |
| FS-002 | Customer-facing Features | AI embedded in product/service features provided to customers. |
| FS-003 | Developer Tooling | AI used to assist software development and engineering tasks. |
| FS-004 | IT Operations | AI used for IT operations and system administration (monitoring, incident handling). |
| FS-005 | Security Operations | AI used for security monitoring/response (SOC, detection, triage). |
| FS-006 | Governance & Compliance | AI used to support governance/compliance activities (policy, audit evidence). |

### UC: Use Case Class

Categorizes AI use by the type of task or interaction. **Select one or more.** Full list includes 30 codes; representative examples below.

| Code | Label | Definition |
| --- | --- | --- |
| UC-001 | General Q&A | General question answering and conversational use. |
| UC-002 | Summarization | Summarizing documents, meetings, or messages. |
| UC-003 | Translation | Translation between languages. |
| UC-004 | Content Drafting | Generating drafts for emails, documents, or reports. |
| UC-005 | Code Generation | Generating code or scripts. |
| UC-006 | Code Review | Reviewing code for issues and improvements. |
| UC-009 | Search/RAG | RAG-based retrieval and question answering. |
| UC-010 | Agentic Automation | Autonomous or semi-autonomous agents executing actions. |

See [Dictionary](./05-dictionary.md) for the complete list of 30 UC codes.

### DT: Data Type

Categorizes the sensitivity and classification of data involved. **Select one or more.**

| Code | Label | Definition |
| --- | --- | --- |
| DT-001 | Public | Data that is publicly available and intended for public disclosure. |
| DT-002 | Internal | Non-public internal business data. |
| DT-003 | Confidential | Highly sensitive internal data requiring restricted access. |
| DT-004 | Personal Data | Personal data as defined by applicable privacy laws. |
| DT-005 | Sensitive Personal Data | Special category/sensitive personal data. |
| DT-006 | Credentials | Authentication secrets and credentials. |
| DT-007 | Source Code | Source code and related artifacts. |
| DT-008 | Customer Data | Customer-provided or customer-related data. |
| DT-009 | Operational Logs | Operational or system logs used for monitoring and troubleshooting. |
| DT-010 | Security Telemetry | Security telemetry such as alerts and detections. |

### CH: Channel

Categorizes how users access or interact with the AI. **Select one or more.**

| Code | Label | Definition |
| --- | --- | --- |
| CH-001 | Web UI | Use via a web user interface. |
| CH-002 | API | Use via programmatic API integration. |
| CH-003 | IDE Plugin | Use via IDE/editor plugin. |
| CH-004 | ChatOps | Use via chat platforms (Slack/Teams) integrations. |
| CH-005 | Desktop App | Use via native desktop application. |
| CH-006 | Mobile App | Use via native mobile application. |
| CH-007 | Email | Use via email interface or email-based automation. |
| CH-008 | Command Line | Use via command-line interface. |

### IM: Integration Mode

Categorizes how AI is integrated into enterprise systems. **Select exactly one.**

| Code | Label | Definition |
| --- | --- | --- |
| IM-001 | Standalone | Used standalone without integration into enterprise systems. |
| IM-002 | SaaS Integrated | SaaS application integrates AI features. |
| IM-003 | Enterprise App Embedded | AI embedded into internal enterprise applications. |
| IM-004 | RPA/Workflow | AI invoked within workflow automation or RPA. |
| IM-005 | On-prem / Private | AI hosted in private/on-prem environment. |
| IM-006 | Managed Service | Use via managed service with enterprise controls. |
| IM-007 | Shadow / Unmanaged | Use outside of approved governance controls. |

### RS: Risk Surface

Categorizes the types of risks associated with the AI use. **Select one or more.**

| Code | Label | Definition |
| --- | --- | --- |
| RS-001 | Data Leakage | Risk of unintended data disclosure. |
| RS-002 | Security Abuse | Risk that the system is abused for malicious purposes. |
| RS-003 | Compliance Breach | Risk of violating laws/regulations/policies. |
| RS-004 | IP Infringement | Risk of infringing copyright/patent/trade secrets. |
| RS-005 | Model Misuse | Risk from inappropriate model use or over-reliance. |
| RS-006 | Bias/Fairness | Risk of unfair or biased outcomes. |
| RS-007 | Safety | Risk of harmful content or unsafe recommendations. |
| RS-008 | Third-party Risk | Vendors, sub-processors, and model provider risks. |

### OB: Outcome / Benefit

Categorizes the expected outcomes or benefits from AI use. **Optional; select zero or more.**

| Code | Label | Definition |
| --- | --- | --- |
| OB-001 | Efficiency | Improves time/cost efficiency. |
| OB-002 | Quality | Improves quality/accuracy of outputs. |
| OB-003 | Revenue | Contributes to revenue growth. |
| OB-004 | Risk Reduction | Reduces operational/security/compliance risk. |
| OB-005 | Innovation | Enables new capabilities or innovations. |
| OB-006 | Customer Satisfaction | Improves customer satisfaction. |
| OB-007 | Employee Experience | Improves employee experience. |

### LG: Log/Event Type

Categorizes the types of log/event/record evidence required or collected. **Select one or more.** (See [ID Policy / Namespace](./04b-id-policy-namespace.md): **EV-** is reserved for Evidence *artifact* IDs only.)

| Code | Label | Definition |
| --- | --- | --- |
| LG-001 | Request Record | Evidence that an AI use/service was requested and described. |
| LG-002 | Review/Approval Record | Evidence that a review/approval was performed. |
| LG-003 | Exception Record | Evidence that an exception was granted and tracked. |
| LG-004 | Renewal/Re-evaluation Record | Evidence that renewal or re-evaluation occurred. |
| LG-005 | Change Log Entry | Evidence of changes and their approvals. |
| LG-006 | Integrity Proof | Evidence of integrity (hash, signature, WORM). |
| LG-007 | Access Log | Evidence of access control and access history. |
| LG-008 | Model/Service Inventory | Inventory record of models/services used. |
| LG-009 | Risk Assessment | Documented risk assessment for the use/service. |
| LG-010 | Control Mapping | Control mapping evidence to external frameworks. |
| LG-011 | Training/Guidance | Evidence of training or guidance provided to users. |
| LG-012 | Monitoring Evidence | Evidence of monitoring and ongoing oversight. |
| LG-013 | Incident Record | Evidence of incident handling related to AI use. |
| LG-014 | Third-party Assessment | Evidence of vendor or third-party assessment. |
| LG-015 | Attestation/Sign-off | Formal attestation or sign-off record. |

## How to Use

### Relationship with Evidence

Each evidence document references codes from multiple dimensions to classify the AI system or use case being documented. **EV** denotes evidence *artifact* identifiers (e.g. `evidence[].id`, `references[]`); **LG** denotes log/event *taxonomy* codes (e.g. `evidence[].codes.LG`). The 8-dimension classification enables:

- **Consistent categorization** across the organization
- **Risk-based filtering** by dimension values
- **Framework mapping** via Coverage Map

### Referencing the Dictionary

For complete code definitions including scope notes and examples, refer to the [Dictionary](./05-dictionary.md).

### Example Classification

```
FS: FS-001 (End-user Productivity)
UC: UC-001 (General Q&A), UC-002 (Summarization)
DT: DT-002 (Internal), DT-004 (Personal Data)
CH: CH-001 (Web UI)
IM: IM-002 (SaaS Integrated)
RS: RS-001 (Data Leakage), RS-003 (Compliance Breach)
OB: OB-001 (Efficiency)
LG: LG-001 (Request Record), LG-002 (Review/Approval Record)
```

## SSOT Reference

!!! info "Source of Truth"
    The authoritative definitions are `data/taxonomy/canonical.yaml` and `data/taxonomy/i18n/*.yaml`. The file `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` is **generated** from the SSOT. This page is explanatory. See [Localization Guide](../../contributing/localization.md) for update workflows.

## Related Pages

- [Codes](./04-codes.md) - Code format, naming conventions, and lifecycle
- [Dictionary](./05-dictionary.md) - Complete code listings and column definitions
- [Evidence Templates](./06-ev-template.md) - How to use codes in evidence
- [Responsibility Boundary](../../governance/responsibility-boundary.md) - Non-overclaim statement
