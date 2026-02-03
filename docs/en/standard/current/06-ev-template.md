---
description: AIMO Evidence Pack templates and usage guide. Structure for documenting AI governance evidence with index management and audit-ready formatting.
---

# Evidence Pack Template (EP)

This section defines the Evidence Pack templates and their usage. An Evidence Pack is a collection of documentation that demonstrates governance and compliance for an AI system.

## Namespace: Evidence Pack document types (EP) vs Taxonomy Log/Event Type (LG)

> **Important**: **EP-01..EP-07** identify *document types* (Evidence Pack file types). **LG-001, LG-002, …** in the [Taxonomy](./03-taxonomy.md) identify *log/event types* (Request Record, Review/Approval, Exception, etc.). **EV-** is reserved for [Evidence artifact IDs](./04b-id-policy-namespace.md) only. Use EP for pack structure and LG for lifecycle log/event classification.

## Key Principle: Index and Diff Management

What matters is not the content of individual submissions alone, but the **index** and **diff management** across evidence items.

An Evidence Pack serves as an index linking AI systems to their governance artifacts. The value lies in:

1. **Traceability**: Linking decisions, approvals, and changes across time
2. **Auditability**: Enabling auditors to navigate the evidence structure
3. **Maintainability**: Tracking what changed, when, and why

## MVP Evidence Set (EP-01 to EP-07)

The following seven **Evidence Pack document types** (EP) form the **minimum viable set** for demonstrating AI governance. Each is a document template; taxonomy **LG** codes (Request Record, Review/Approval, etc.) are used elsewhere in the bundle and in `codes.LG` to classify *log/event* evidence.

| ID | Document Type | Purpose |
| --- | --- | --- |
| EP-01 | System Overview | Document the AI system and its purpose |
| EP-02 | Data Flow | Map data movement through the system |
| EP-03 | Inventory | Maintain catalog of AI assets |
| EP-04 | Risk & Impact Assessment | Assess and document risks |
| EP-05 | Controls & Approvals | Document controls and approval records |
| EP-06 | Logging & Monitoring | Define logging and monitoring setup |
| EP-07 | Incident & Exception | Track incidents and exceptions |

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

Each Evidence Pack MUST include codes from all 8 dimensions. The **LG** dimension lists *taxonomy* Log/Event Types (e.g. Request Record, Review/Approval) applicable to this pack—not document type codes. Document type is given by `evidence_files[].file_id` (EP-01..EP-07). See [ID Policy / Namespace](./04b-id-policy-namespace.md).

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
    "LG": ["LG-001", "LG-002", "LG-008", "LG-009"]
  }
}
```

### Evidence Files List

Each entry identifies a document in the pack by **file_id** (EP-01..EP-07). Optional **ev_codes** may list taxonomy LG codes (LG-xxx) that the document supports.

```json
{
  "evidence_files": [
    {
      "file_id": "EP-01",
      "filename": "EP-01_system_overview.md",
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
# EP-01: System Overview

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
| **LG** | `LG-001`, `LG-002` | Request Record, Review/Approval Record |
```

## Downloads

### Templates

Evidence Pack templates are available in the repository. Use **file_id** EP-01..EP-07 in the manifest; filenames may be EP-01_... or legacy EV-01_... for backward compatibility.

- `source_pack/04_evidence_pack/templates/EV-01_system_overview.md` → file_id **EP-01**
- `source_pack/04_evidence_pack/templates/EV-02_data_flow.md` → file_id **EP-02**
- `source_pack/04_evidence_pack/templates/EV-03_inventory.md` → file_id **EP-03**
- `source_pack/04_evidence_pack/templates/EV-04_risk_impact.md` → file_id **EP-04**
- `source_pack/04_evidence_pack/templates/EV-05_controls_approvals.md` → file_id **EP-05**
- `source_pack/04_evidence_pack/templates/EV-06_logging_monitoring.md` → file_id **EP-06**
- `source_pack/04_evidence_pack/templates/EV-07_incident_exception.md` → file_id **EP-07**

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
