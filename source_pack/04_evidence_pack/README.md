# Evidence Pack (Authoring SSOT)

**Status**: Authoring input — not user-facing documentation  
**Canonical language**: English (EN)

This directory contains the Evidence Pack templates, schemas, and examples for the AIMO Standard.

---

## Directory Structure

```
04_evidence_pack/
├── README.md                 # This file
├── schemas/
│   └── evidence_pack_manifest.schema.json  # JSON Schema for manifests
├── templates/
│   ├── EV-01_system_overview.md
│   ├── EV-02_data_flow.md
│   ├── EV-03_inventory.md
│   ├── EV-04_risk_impact.md
│   ├── EV-05_controls_approvals.md
│   ├── EV-06_logging_monitoring.md
│   └── EV-07_incident_exception.md
└── examples/
    └── evidence_pack_manifest.example.json
```

---

## MVP Evidence Set (EV-01 to EV-07)

| Template | Evidence Type | Code | Description |
| --- | --- | --- | --- |
| EV-01 | System Overview | EV-001 | AI system purpose and architecture |
| EV-02 | Data Flow | EV-002 | Data movement and processing |
| EV-03 | Inventory | EV-003 | AI asset catalog |
| EV-04 | Risk & Impact | EV-004 | Risk assessment documentation |
| EV-05 | Controls & Approvals | EV-005 | Control measures and approvals |
| EV-06 | Logging & Monitoring | EV-006 | Logging and monitoring setup |
| EV-07 | Incident & Exception | EV-007 | Incident and exception handling |

---

## Template Structure

Each template includes:

1. **Mandatory Metadata Block**
   - pack_id, pack_version, taxonomy_version
   - created_date, last_updated, owner

2. **AIMO Codes (8 Dimensions)**
   - FS, UC, DT, CH, IM, RS, OB, EV

3. **Content Sections**
   - Domain-specific documentation

4. **References**
   - Links to related evidence

5. **Revision History**
   - Change tracking

---

## Evidence Pack Manifest

The manifest file (`evidence_pack_manifest.json`) indexes all evidence files and provides:

- Pack identification (pack_id, pack_version)
- Taxonomy version reference
- AIMO codes for all 8 dimensions
- List of evidence files with metadata
- Change log entries
- Optional integrity information (hashes)

---

## Schema

The manifest schema is at:
```
schemas/evidence_pack_manifest.schema.json
```

Key validations:
- Required fields: pack_id, pack_version, taxonomy_version, codes, evidence_files
- Codes: All required dimensions (FS, UC, DT, CH, IM, RS, EV) must have at least one code
- Code format: `<DIM>-<TOKEN>` (e.g., FS-001, UC-002)

---

## Usage

1. Copy templates to your evidence pack directory
2. Fill in the metadata and content sections
3. Create a manifest file referencing all evidence
4. Validate using the AIMO Validator

---

## Distribution Model

Templates are designed for distribution through:
- Audit firms
- System integrators
- Consultants

These parties maintain the linkage to the standard version and provide templates to enterprises.

---

## Authoring Notes

- Templates use EN/JA bilingual format
- All templates MUST include Mandatory Metadata and 8-dimension codes
- Content sections are guides; adapters may customize
- Keep source attribution when distributing
