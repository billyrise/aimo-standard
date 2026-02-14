---
description: Evidence Bundle Coverage Map template (v0.1). Informative one-page summary for auditors — scope, evidence types, controls mapping, exclusions, integrity proof.
---

# Evidence Bundle Coverage Map (Template)

!!! info "Informative — recommended practice"
    This page defines a **recommended practice template** for a one-page Evidence Bundle Coverage Map. It is **not** a normative requirement of the standard. Use it to document what a bundle covers and does not cover for auditor handoff. References (e.g. to frameworks) are stable; adoption is at the implementer's discretion.

---

## 1. Scope

| Item | Description |
|------|--------------|
| **Scope reference** | `scope_ref` from the bundle manifest (e.g. `SC-001`). Links this bundle to the declared scope. |
| **Bundle ID** | `bundle_id` (UUID) — unique identifier for this bundle. |
| **Bundle version** | `bundle_version` (SemVer) — version of the bundle. |
| **Period / snapshot** | Optional: time period or snapshot date this bundle represents (e.g. 2026-Q1, as-of 2026-02-03). |

---

## 2. Evidence types (EV / objects vs payloads)

| Category | Contents | v0.1 minimal example |
|----------|----------|------------------------|
| **object_index** | Enumerated objects (metadata, indexes). Each entry: `id`, `type`, `path`, `sha256`. | e.g. `objects/index.json` (index type). |
| **payload_index** | Payload files (root EV JSON, Evidence Pack files). Each entry: `logical_id`, `path`, `sha256`, `mime`, `size`. | e.g. `payloads/root.json` (root AIMO EV JSON). |
| **EV types** | Evidence records (in root or linked payloads) — request, review, exception, renewal, change log. | Aligned with [Evidence Pack Template](../../standard/current/06-ev-template/) and [Minimum Evidence Requirements](../minimum-evidence/). |

*Implementers may extend object_index and payload_index; paths MUST remain within the bundle root and satisfy the [Evidence Bundle root structure (v0.1)](../../standard/current/09-evidence-bundle-structure/).*

---

## 3. Controls mapping (reference only)

Mapping to external frameworks is **for reference only**; the standard does not mandate compliance with any specific regulation.

| Framework | Use in this bundle | Reference |
|-----------|--------------------|-----------|
| **ISO/IEC 42001** | Optional: document which AI MS themes this bundle supports. | [Coverage Map → ISO 42001](../../coverage-map/iso-42001/) |
| **EU AI Act** | Optional: high-level documentation/record-keeping alignment. | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/) |
| **NIST AI RMF** | Optional: Govern, Map, Measure, Manage mapping. | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/) |
| **ISMS (27001/27002)** | Optional: change management, access, logging, integrity. | [Coverage Map → ISMS](../../coverage-map/isms/) |

*Fill in “Use in this bundle” per submission; the standard does not require any specific control coverage.*

---

## 4. Exclusions / assumptions

| Area | What this bundle does **not** cover (example rows — adjust per submission) |
|------|-------------------------------------------------------------------------------|
| **Exclusions** | e.g. Systems or use cases out of scope; third-party components not evidenced; time period outside this bundle. |
| **Assumptions** | e.g. Dictionary/taxonomy version; validator/schema version used; custody and retention are implementation-defined. |
| **Limitations** | e.g. Signature verification is out of scope in v0.1; no legal interpretation of regulations. |

*Replace placeholder text with submission-specific exclusions and assumptions.*

---

## 5. Integrity proof summary (v0.1)

| Element | What is provided (v0.1 normative) |
|---------|----------------------------------|
| **manifest.json** | Present and schema-valid; includes `object_index`, `payload_index`, `hash_chain`, `signing`. |
| **sha256** | Every file in `object_index` and `payload_index` has a declared 64-char lowercase hex sha256; validator checks content match. |
| **Index existence** | All listed paths exist under the bundle root; no path traversal (`../` or leading `/`). |
| **Signature existence** | At least one signature file in `signatures/`; manifest references it via `signing.signatures[]` with `path` and `targets` (v0.1 MUST include `manifest.json` in targets). Cryptographic verification is out of scope for v0.1. |
| **Hash chain** | `hash_chain` in manifest: `algorithm`, `head` (64-char hex), `path` (file under `hashes/`), `covers` (v0.1 MUST include `manifest.json` and `objects/index.json`). File at `hash_chain.path` exists. |

*This table summarizes the integrity guarantees that the [Validator](../../validator/) checks for v0.1 bundles. Custody (storage, access control, retention) is implementation-defined.*

---

## Coverage Map (YAML) vs Profiles (JSON)

| Artifact | Status | Purpose |
|----------|--------|---------|
| **Coverage Map YAML** (`coverage_map/coverage_map.yaml` or similar) | **Informative** | High-level mapping themes between AIMO evidence/artifacts and external frameworks (ISO 42001, NIST AI RMF, EU AI Act, etc.) for explainability. It does not impose normative validation requirements. |
| **Profile JSONs** (`coverage_map/profiles/*.json`) | **Normative** | Conversion specifications validated against `schemas/jsonschema/aimo-profile.schema.json`. They define machine-readable mappings (e.g. which AIMO objects map to which framework clauses). The [Validator](../../validator/) runs `--validate-profiles` to ensure all official profile JSONs conform to the schema (profile_id PR-* pattern, target enum, target_version, mappings). |

### v0.1 official profiles (frozen set)

The v0.1 release includes **three** normative profile JSONs, all validated by the validator:

| File | profile_id | target | target_version |
|------|------------|--------|----------------|
| `iso42001.json` | PR-ISO42001-v0.1 | ISO_42001 | 1.0 |
| `nist_ai_rmf.json` | PR-NIST-AI-RMF-v0.1 | NIST_AI_RMF | 1.0 |
| `eu_ai_act_annex_iv.json` | PR-EU-AI-ACT-ANNEX-IV-v0.1 | EU_AI_ACT_ANNEX_IV | Annex IV |

### Profile update policy

- **EU AI Act refs (0.1.2)**: Article references for the EU AI Act in the coverage map and docs were aligned to Regulation (EU) 2024/1689 for consistent evidence readiness; informative only, not legal advice.
- **ISO 42001 / NIST AI RMF**: New versions of the target framework may be added as new profile files or new `target_version` values in a future standard version; v0.1 profiles remain frozen for the v0.1 release.
- **EU AI Act Annex IV**: Annex IV and related articles may be updated by regulators; profile mappings may be updated via **PATCH** (e.g. 0.1.x) to follow wording or clause changes while keeping the same profile_id for continuity. Implementers should align with the version referenced in the profile’s `target_version` and release notes.

---

## See also

- [Evidence Bundle (artifact overview)](../evidence-bundle/)
- [Evidence Bundle root structure (v0.1)](../../standard/current/09-evidence-bundle-structure/)
- [Minimum Evidence Requirements](../minimum-evidence/)
- [Coverage Map (framework mappings)](../../coverage-map/)
- [Validator](../../validator/)
