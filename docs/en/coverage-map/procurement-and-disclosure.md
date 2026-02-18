---
description: Procurement and disclosure overlays (UK, Japan). UK ATRS, UK procurement guidance, Japan government GenAI procurement and AI Business Guidelines. Reference mapping only.
---
<!-- aimo:translation_status=source -->

# Procurement & Disclosure Overlays (UK, Japan)

This page describes **reference mappings** between AIMO evidence and selected **UK** and **Japan** procurement and disclosure frameworks. The goal is **burden reduction via reuse of AIMO evidence**: adopters can reuse evidence they already produce for AIMO to support procurement and disclosure requirements. It is **informative mapping only**; AIMO does not guarantee full compliance with government requirements. Verify against the official sources below.

## Primary sources

**UK**

- [Algorithmic Transparency Recording Standard (ATRS) Hub](https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub) — GOV.UK (template, guidance, published records)
- [ATRS template](https://www.gov.uk/government/publications/algorithmic-transparency-template) — Official template for public sector
- [Guidance for organisations using the ATRS](https://www.gov.uk/government/publications/guidance-for-organisations-using-the-algorithmic-transparency-standard/algorithmic-transparency-recording-standard-guidance-for-public-sector-bodies) — GOV.UK

**Japan**

- [デジタル庁 — 生成AIの調達・利活用に係るガイドライン](https://www.digital.go.jp/news/3579c42d-b11c-4756-b66e-3d3e35175623) — Digital Agency (Cabinet Secretariat): "行政の進化と革新のための生成AIの調達・利活用に係るガイドライン"
- [AI事業者ガイドライン](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/index.html) — METI / MIC (AI Business Guidelines; 経済産業省・総務省)

## Mapping table (UK)

| Government requirement (topic) | AIMO artifact(s) | Where in Evidence Bundle | Validator coverage | Note |
| --- | --- | --- | --- | --- |
| ATRS — accountability / owner | Summary, review | manifest; objects/ (EV, Summary); payload_index | schema_validate_ev | Informative mapping; does not guarantee full compliance. |
| ATRS — system / model description | Dictionary, EV | objects/; schemas/jsonschema/aimo-dictionary.schema.json | schema_validate_dictionary | Attach official ATRS record in External Forms; link by logical_id. |
| ATRS — risk considerations | Dictionary, request, review, exception | objects/; templates/ev/ | schema_validate_ev | Profile: `coverage_map/profiles/uk_atrs_procurement.json`. |
| Procurement — supplier evidence | request, review, exception; Evidence Bundle | manifest, object_index, payload_index; examples/evidence_bundle_minimal/ | schema_validate_ev | Use bundle to structure evidence; UK guidance remains authoritative. |

## Mapping table (Japan)

| Government requirement (topic) | AIMO artifact(s) | Where in Evidence Bundle | Validator coverage | Note |
| --- | --- | --- | --- | --- |
| GenAI procurement checklist (デジタル庁) | External Form (checklist as-is); Dictionary, Summary | payload_index; External Forms section; manifest reference | N/A (attachment) | Informative mapping; does not guarantee full compliance. Profile: `coverage_map/profiles/jp_gov_genai_procurement.json`. |
| AI Business Guidelines — governance / traceability | Summary, dictionary, request, review, change_log | objects/; manifest; templates/ev/ | schema_validate_dictionary, schema_validate_ev | Map checklist items to AIMO taxonomy where useful for traceability. |
| Risk / accountability documentation | Dictionary, EV, review, exception | objects/; schemas/jsonschema/ | schema_validate_ev | Verify against official デジタル庁 and METI/MIC guidance. |

## UK: ATRS and AI procurement (summary)

| Topic | AIMO evidence / mapping | Notes |
| --- | --- | --- |
| **UK ATRS** (AI Transparency Record) | Summary, review (accountability owner), evidence (model/system description), dictionary (risk considerations). Profile: `coverage_map/profiles/uk_atrs_procurement.json`. | Attach or reference ATRS-style transparency record in External Forms; link to bundle objects by logical_id. |
| **UK procurement guidance** | Request, review, exception; Evidence Bundle for supplier evaluation. | Use AIMO bundle to structure evidence for procurement evaluation; official UK guidance remains authoritative. |

## Japan: Government GenAI procurement and AI Business Guidelines (summary)

| Topic | AIMO evidence / mapping | Notes |
| --- | --- | --- |
| **JP government GenAI procurement checklist** | Attach checklist as External Form (e.g. payload: JP_PROCUREMENT_CHECKLIST); reference in manifest. Profile: `coverage_map/profiles/jp_gov_genai_procurement.json`. | Reference mapping only; AIMO does not replace official checklists. |
| **AI Business Guidelines** | Summary, dictionary; map checklist items to AIMO taxonomy codes where useful for traceability. | Use for explainability; verify against official Japanese guidance. |

## How to use

- **External Forms**: Attach UK or Japan official templates/checklists **as-is** (PDF, DOC, etc.), hash them, and list them in the Evidence Bundle [payload_index](../../standard/current/09-evidence-bundle-structure/) or in the [EV Template External Forms section](../../standard/current/06-ev-template/). Reference them by logical_id in the manifest and in coverage mappings.
- **Profiles**: The profiles listed above define optional machine-readable mappings; they do not impose legal or contractual obligations.

See [Conformance](../../conformance/) for levels and [Minimum Evidence — Regulatory overlays](../../artifacts/minimum-evidence/) for overlay summary.
