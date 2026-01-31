# Taxonomy

The AIMO Taxonomy provides a structured framework for categorizing AI systems, their uses, and associated governance requirements. It consists of **8 dimensions** that together enable consistent classification and evidence management across organizations.

## Purpose and Audit Context

The taxonomy serves two primary purposes from an audit perspective:

1. **Evidence Readiness**: Enables systematic documentation of AI systems using a standardized classification, making evidence collection and review more efficient.

2. **Explainability**: Provides a common vocabulary for describing AI use cases across the organization, supporting clear communication with auditors and stakeholders.

!!! warning "Non-Overclaim"
    The AIMO Standard supports **explainability and evidence readiness**. It does **not** provide legal advice, guarantee compliance, or certify conformity to any regulation or framework. See [Responsibility Boundary](../../governance/responsibility-boundary.md) for details.

## Single Source of Truth (SSOT)

The authoritative definition of the taxonomy is maintained in machine-readable files:

| File | Description |
| --- | --- |
| `taxonomy_dictionary_v0.1.csv` | SSOT for all codes (91 codes across 8 dimensions) |
| `taxonomy_en.yaml` | English taxonomy (generated from CSV) |
| `taxonomy_ja.yaml` | Japanese taxonomy (generated from CSV) |

**This documentation page is explanatory.** For authoritative definitions, always reference the SSOT files in `source_pack/03_taxonomy/`.

## Code System Overview

AIMO uses a code system with the format `<DIM>-<TOKEN>`, where:

- `<DIM>`: Two-letter dimension identifier (e.g., FS, UC, DT)
- `<TOKEN>`: Three-digit numeric token (e.g., 001, 002, 003)

**Examples:**

- `UC-001`: General Q&A (Use Case Class)
- `DT-004`: Personal Data (Data Type)
- `CH-003`: IDE Plugin (Channel)
- `IM-002`: SaaS Integrated (Integration Mode)

## The 8 Dimensions

| Priority | ID | Name | Required | Multi-select | What it distinguishes |
| --- | --- | --- | --- | --- | --- |
| 1 | **FS** | Functional Scope | Yes | No | Which business function is supported |
| 2 | **UC** | Use Case Class | Yes | Yes | What type of task is performed |
| 3 | **DT** | Data Type | Yes | Yes | What data sensitivity is involved |
| 4 | **CH** | Channel | Yes | Yes | How users access the AI |
| 5 | **IM** | Integration Mode | Yes | No | How AI connects to enterprise systems |
| 6 | **RS** | Risk Surface | Yes | Yes | What risks are associated |
| 7 | **OB** | Outcome / Benefit | No | Yes | What benefits are expected |
| 8 | **EV** | Evidence Type | Yes | Yes | What evidence is required |

### Usage Rules Summary

| Dimension | Selection | Audit Implication |
| --- | --- | --- |
| FS, IM | Exactly 1 | Primary classification for responsibility assignment |
| UC, DT, CH, RS, EV | 1 or more | Complete enumeration required for risk coverage |
| OB | 0 or more | Optional; documents expected business value |

## Dimension Definitions

### FS: Functional Scope

Categorizes AI use by the business function it supports. **Select exactly one.**

| Code | Label | Description |
| --- | --- | --- |
| FS-001 | End-user Productivity | AI for internal productivity (writing, search, summarization) |
| FS-002 | Customer-facing Features | AI in customer-facing products/services |
| FS-003 | Developer Tooling | AI for software development |
| FS-004 | IT Operations | AI for IT ops and system administration |
| FS-005 | Security Operations | AI for security monitoring/response |
| FS-006 | Governance & Compliance | AI for governance/compliance activities |

### UC: Use Case Class

Categorizes AI use by the type of task or interaction. **Select one or more.** Full list includes 30 codes; representative examples below.

| Code | Label | Description |
| --- | --- | --- |
| UC-001 | General Q&A | General question answering |
| UC-002 | Summarization | Summarizing documents/meetings |
| UC-003 | Translation | Translation between languages |
| UC-004 | Content Drafting | Generating drafts for documents |
| UC-005 | Code Generation | Generating code or scripts |
| UC-010 | Agentic Automation | Autonomous agents executing actions |

See [Dictionary](./05-dictionary.md) for the complete list of 30 UC codes.

### DT: Data Type

Categorizes the sensitivity and classification of data involved. **Select one or more.**

| Code | Label | Description |
| --- | --- | --- |
| DT-001 | Public | Publicly available data |
| DT-002 | Internal | Non-public internal business data |
| DT-003 | Confidential | Highly sensitive data with restricted access |
| DT-004 | Personal Data | Personal data per privacy laws |
| DT-005 | Sensitive Personal Data | Special category personal data |
| DT-006 | Credentials | Authentication secrets and credentials |
| DT-007 | Source Code | Source code and related artifacts |
| DT-008 | Customer Data | Customer-provided or customer-related data |
| DT-009 | Operational Logs | System operational logs |
| DT-010 | Security Telemetry | Security monitoring data |

### CH: Channel

Categorizes how users access or interact with the AI. **Select one or more.**

| Code | Label | Description |
| --- | --- | --- |
| CH-001 | Web UI | Via web user interface |
| CH-002 | API | Via programmatic API integration |
| CH-003 | IDE Plugin | Via IDE/editor plugin |
| CH-004 | ChatOps | Via Slack/Teams integrations |
| CH-005 | Desktop App | Via native desktop application |
| CH-006 | Mobile App | Via native mobile application |
| CH-007 | Embedded Widget | Embedded in other applications |
| CH-008 | Batch/CLI | Via command-line or batch processing |

### IM: Integration Mode

Categorizes how AI is integrated into enterprise systems. **Select exactly one.**

| Code | Label | Description |
| --- | --- | --- |
| IM-001 | Standalone | Used standalone without enterprise integration |
| IM-002 | SaaS Integrated | SaaS application with AI features |
| IM-003 | Enterprise App Embedded | AI embedded in internal applications |
| IM-004 | RPA/Workflow | AI invoked within workflow automation |
| IM-005 | On-prem / Private | AI in private/on-prem environment |
| IM-006 | Hybrid Cloud | Combination of cloud and on-prem |
| IM-007 | Multi-tenant SaaS | Shared SaaS infrastructure |

### RS: Risk Surface

Categorizes the types of risks associated with the AI use. **Select one or more.**

| Code | Label | Description |
| --- | --- | --- |
| RS-001 | Data Leakage | Risk of unintended data disclosure |
| RS-002 | Security Abuse | Risk of system abuse for malicious purposes |
| RS-003 | Compliance Breach | Risk of violating laws/regulations/policies |
| RS-004 | IP Infringement | Risk of copyright/patent/trade secret infringement |
| RS-005 | Model Misuse | Risk from inappropriate model use or over-reliance |
| RS-006 | Bias/Fairness | Risk of discriminatory outputs |
| RS-007 | Availability | Risk of service disruption |
| RS-008 | Supply Chain | Risk from third-party dependencies |

### OB: Outcome / Benefit

Categorizes the expected outcomes or benefits from AI use. **Optional; select zero or more.**

| Code | Label | Description |
| --- | --- | --- |
| OB-001 | Efficiency | Improves time/cost efficiency |
| OB-002 | Quality | Improves quality/accuracy of outputs |
| OB-003 | Revenue | Contributes to revenue growth |
| OB-004 | Risk Reduction | Reduces operational/security/compliance risk |
| OB-005 | Innovation | Enables new capabilities or innovations |
| OB-006 | Customer Satisfaction | Improves customer experience |
| OB-007 | Employee Experience | Improves employee productivity/satisfaction |

### EV: Evidence Type

Categorizes the types of evidence required or collected. **Select one or more.** The following are **MVP required** evidence types (EV-001 to EV-007):

| Code | Label | Description |
| --- | --- | --- |
| EV-001 | System Overview | Overview of the AI system |
| EV-002 | Data Flow | Data flow diagram and description |
| EV-003 | Inventory | Inventory of AI systems/models |
| EV-004 | Risk & Impact Assessment | Risk and impact assessment |
| EV-005 | Controls & Approvals | Control measures and approvals |
| EV-006 | Logging & Monitoring | Logging and monitoring configuration |
| EV-007 | Incident & Exception | Incident and exception handling |

Additional evidence types (EV-008 to EV-015) are available for extended documentation. See [Dictionary](./05-dictionary.md) for the complete list.

## SSOT References

| Resource | Path | Description |
| --- | --- | --- |
| Dictionary CSV | `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv` | All 91 codes with full metadata |
| Taxonomy YAML (EN) | `source_pack/03_taxonomy/taxonomy_en.yaml` | Generated English taxonomy |
| Taxonomy YAML (JA) | `source_pack/03_taxonomy/taxonomy_ja.yaml` | Generated Japanese taxonomy |
| Taxonomy Pack Schema | `source_pack/03_taxonomy/schemas/taxonomy_pack.schema.json` | JSON Schema for validation |

## Downloads

Download the complete taxonomy package from the [Releases](../../releases/index.md) page.

## Related Pages

- [Codes](./04-codes.md) - Code format, naming conventions, and lifecycle
- [Dictionary](./05-dictionary.md) - Complete code listings and column definitions
- [Evidence Templates](./06-ev-template.md) - MVP evidence templates
- [Responsibility Boundary](../../governance/responsibility-boundary.md) - Non-overclaim statement
