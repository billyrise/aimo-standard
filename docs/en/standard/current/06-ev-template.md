---
description: AIMO Evidence Pack templates and usage guide. Structure for documenting AI governance evidence with index management and audit-ready formatting.
---

# EV Template

This section defines the Evidence Pack templates and their usage. An Evidence Pack is a collection of documentation that demonstrates governance and compliance for an AI system.

## Key Principle: Index and Diff Management

> **Important**: What matters is not the content of individual submissions, but the **index** and **diff management** across evidence items.

An Evidence Pack serves as an index linking AI systems to their governance artifacts. The value lies in:

1. **Traceability**: Linking decisions, approvals, and changes across time
2. **Auditability**: Enabling auditors to navigate the evidence structure
3. **Maintainability**: Tracking what changed, when, and why

## MVP Evidence Set (EV-01 to EV-07)

The following seven evidence types form the **minimum viable set** for demonstrating AI governance:

| ID | Evidence Type | Code | Purpose |
| --- | --- | --- | --- |
| EV-01 | System Overview | EV-001 | Document the AI system and its purpose |
| EV-02 | Data Flow | EV-002 | Map data movement through the system |
| EV-03 | Inventory | EV-003 | Maintain catalog of AI assets |
| EV-04 | Risk & Impact Assessment | EV-004 | Assess and document risks |
| EV-05 | Controls & Approvals | EV-005 | Document controls and approval records |
| EV-06 | Logging & Monitoring | EV-006 | Define logging and monitoring setup |
| EV-07 | Incident & Exception | EV-007 | Track incidents and exceptions |

## Evidence Pack Manifest

Each Evidence Pack MUST include a manifest file containing:

### Mandatory Metadata

| Field | Description | Required |
| --- | --- | --- |
| `pack_id` | Unique identifier (e.g., EP-EXAMPLE-001) | Yes |
| `pack_version` | SemVer version of the pack | Yes |
| `taxonomy_version` | Version of AIMO taxonomy used | Yes |
| `created_date` | Pack creation date | Yes |
| `last_updated` | Last update date | Yes |
| `owner` | Responsible party | Yes |

### AIMO Codes (8 Dimensions)

Each Evidence Pack MUST include codes from all 8 dimensions:

```json
{
  "codes": {
    "FS": ["FS-001"],
    "UC": ["UC-001", "UC-002"],
    "DT": ["DT-002"],
    "CH": ["CH-001"],
    "IM": ["IM-001"],
    "RS": ["RS-001", "RS-003"],
    "OB": ["OB-001"],
    "EV": ["EV-001", "EV-002", "EV-003", "EV-004", "EV-005", "EV-006", "EV-007"]
  }
}
```

### Evidence Files List

```json
{
  "evidence_files": [
    {
      "file_id": "EV-01",
      "filename": "EV-01_system_overview.md",
      "ev_type": "EV-001",
      "title": "System Overview",
      "required": true
    }
  ]
}
```

## Template Structure

Each evidence template includes:

1. **Mandatory Metadata Block** - pack_id, version, taxonomy_version, dates, owner
2. **AIMO Codes Table** - All 8 dimensions with applicable codes
3. **Content Sections** - Domain-specific documentation sections
4. **References** - Links to related evidence
5. **Revision History** - Change tracking

### Template Header Example

```markdown
# EV-01: System Overview

---

## Mandatory Metadata

| Field | Value |
| --- | --- |
| **pack_id** | `EP-EXAMPLE-001` |
| **pack_version** | `0.1.0` |
| **taxonomy_version** | `0.1.0` |
| **created_date** | `2026-01-31` |
| **last_updated** | `2026-01-31` |
| **owner** | `AI Governance Team` |

---

## AIMO Codes (8 Dimensions)

| Dimension | Code(s) | Label |
| --- | --- | --- |
| **FS** | `FS-001` | End-user Productivity |
| **UC** | `UC-001` | General Q&A |
| **DT** | `DT-002` | Internal |
| **CH** | `CH-001` | Web UI |
| **IM** | `IM-001` | Standalone |
| **RS** | `RS-001` | Data Leakage |
| **OB** | `OB-001` | Efficiency |
| **EV** | `EV-001` | System Overview |
```

## Downloads

### Templates

Evidence Pack templates are available in:

- `source_pack/04_evidence_pack/templates/EV-01_system_overview.md`
- `source_pack/04_evidence_pack/templates/EV-02_data_flow.md`
- `source_pack/04_evidence_pack/templates/EV-03_inventory.md`
- `source_pack/04_evidence_pack/templates/EV-04_risk_impact.md`
- `source_pack/04_evidence_pack/templates/EV-05_controls_approvals.md`
- `source_pack/04_evidence_pack/templates/EV-06_logging_monitoring.md`
- `source_pack/04_evidence_pack/templates/EV-07_incident_exception.md`

### Schemas and Examples

- Schema: `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json`
- Example: `source_pack/04_evidence_pack/examples/evidence_pack_manifest.example.json`

See [Releases](../../releases/index.md) for downloadable packages.

## Distribution Model

> **Note**: The primary distribution targets are **audit firms and system integrators** (template distributors), not individual enterprises.

The templates are designed to be:

1. Adopted by auditors and consultants as standard artifacts
2. Distributed to enterprises with source attribution preserved
3. Versioned alongside the AIMO Standard

Enterprises receive templates through their auditors, consultants, or internal governance teams who maintain the linkage to the standard version.

## References

- [Taxonomy](./03-taxonomy.md) - Dimension definitions
- [Codes](./04-codes.md) - Code format
- [Validator](./07-validator.md) - Validation rules
- [Evidence Bundle](../../artifacts/evidence-bundle.md) - Bundle structure
