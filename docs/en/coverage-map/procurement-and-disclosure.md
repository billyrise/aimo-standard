---
description: Procurement and disclosure overlays (UK, Japan). UK ATRS, UK procurement guidance, Japan government GenAI procurement and AI Business Guidelines. Reference mapping only.
---
<!-- aimo:translation_status=source -->

# Procurement & Disclosure Overlays (UK, Japan)

This page describes **reference mappings** between AIMO evidence and selected **UK** and **Japan** procurement and disclosure frameworks. It is **reference mapping only**; AIMO does not replace official checklists or government guidance.

## UK: ATRS and AI procurement

| Topic | AIMO evidence / mapping | Notes |
| --- | --- | --- |
| **UK ATRS** (AI Transparency Record) | Summary, review (accountability owner), evidence (model/system description), dictionary (risk considerations). Profile: `coverage_map/profiles/uk_atrs_procurement.json`. | Attach or reference ATRS-style transparency record in External Forms; link to bundle objects by logical_id. |
| **UK procurement guidance** | Request, review, exception; Evidence Bundle for supplier evaluation. | Use AIMO bundle to structure evidence for procurement evaluation; official UK guidance remains authoritative. |

## Japan: Government GenAI procurement and AI Business Guidelines

| Topic | AIMO evidence / mapping | Notes |
| --- | --- | --- |
| **JP government GenAI procurement checklist** | Attach checklist as External Form (e.g. payload: JP_PROCUREMENT_CHECKLIST); reference in manifest. Profile: `coverage_map/profiles/jp_gov_genai_procurement.json`. | Reference mapping only; AIMO does not replace official checklists. |
| **AI Business Guidelines** | Summary, dictionary; map checklist items to AIMO taxonomy codes where useful for traceability. | Use for explainability; verify against official Japanese guidance. |

## How to use

- **External Forms**: Attach UK or Japan official templates/checklists **as-is** (PDF, DOC, etc.), hash them, and list them in the Evidence Bundle [payload_index](../../standard/current/09-evidence-bundle-structure/) or in the [EV Template External Forms section](../../standard/current/06-ev-template/). Reference them by logical_id in the manifest and in coverage mappings.
- **Profiles**: The profiles listed above define optional machine-readable mappings; they do not impose legal or contractual obligations.

See [Conformance](../../conformance/) for levels and [Minimum Evidence — Regulatory overlays](../../artifacts/minimum-evidence/) for overlay summary.
