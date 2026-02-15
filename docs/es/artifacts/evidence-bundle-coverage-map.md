---
description: Evidence Bundle Coverage Map template (v0.1). Informative one-page summary for auditors — scope, evidence types, controls mapping, exclusions, integrity proof.
---
<!-- aimo:translation_status=translated -->

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
| **EU GPAI CoP** | Optional: Model Documentation Form; attach in External Forms, reference by logical_id. | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/); profile `eu_gp_ai_cop.json` |
| **NIST AI RMF / GenAI** | Optional: GenAI profile (AI 600-1) artifacts. | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/); profile `nist_ai_600_1_genai.json` |
| **UK ATRS** | Optional: ATRS record, procurement evaluation. | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/); profile `uk_atrs_procurement.json` |
| **JP Gov GenAI procurement** | Optional: JP procurement checklist, AI Business Guidelines. | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/); profile `jp_gov_genai_procurement.json` |
| **ISMS (27001/27002)** | Optional: change management, access, logging, integrity. | [Coverage Map → ISMS](../../coverage-map/isms/) |

*Fill in “Use in this bundle” per submission; the standard does not require any specific control coverage.*

### External Forms and manifest reference

**External Forms** (official templates/checklists attached as-is) should be listed in the bundle **payload_index** with a stable `logical_id`, `path`, `sha256`, `mime`, and `size`. Auditors can then trace from the manifest to the file and verify the hash. See [EV Template — External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) and [EV Template — Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index).

---

## 4. Exclusiones / suposiciones

| Área | Lo que este paquete **no** cubre (filas de ejemplo — ajustar por envío) |
|------|-------------------------------------------------------------------------------|
| **Exclusiones** | ej. Sistemas o casos de uso fuera de alcance; componentes de terceros no evidenciados; período fuera de este paquete. |
| **Suposiciones** | ej. Versión de diccionario/taxonomía; versión de validador/esquema usada; custodia y retención son definidas por implementación. |
| **Limitaciones** | ej. La verificación de firmas está fuera de alcance en v0.1; no hay interpretación legal de regulaciones. |

*Sustituya el texto placeholder por exclusiones y suposiciones específicas del envío.*

---

## 5. Resumen de prueba de integridad (v0.1)

| Elemento | Lo que se proporciona (v0.1 normativo) |
|---------|----------------------------------|
| **manifest.json** | Presente y válido según esquema; incluye `object_index`, `payload_index`, `hash_chain`, `signing`. |
| **sha256** | Cada archivo en `object_index` y `payload_index` tiene un sha256 hex en minúsculas de 64 caracteres declarado; el validador comprueba la coincidencia de contenido. |
| **Existencia de índice** | Todas las rutas listadas existen bajo la raíz del paquete; sin recorrido de ruta (`../` o `/` inicial). |
| **Existencia de firma** | Al menos un archivo de firma en `signatures/`; el manifiesto lo referencía vía `signing.signatures[]` con `path` y `targets` (v0.1 DEBE incluir `manifest.json` en targets). La verificación criptográfica está fuera de alcance en v0.1. |
| **Cadena de hash** | `hash_chain` en manifiesto: `algorithm`, `head` (64 caracteres hex), `path` (archivo bajo `hashes/`), `covers` (v0.1 DEBE incluir `manifest.json` y `objects/index.json`). Existe el archivo en `hash_chain.path`. |

*Esta tabla resume las garantías de integridad que el [Validador](../../validator/) comprueba para paquetes v0.1. Custody (almacenamiento, control de acceso, retención) es definido por implementación.*

---

## Coverage Map (YAML) vs Perfiles (JSON)

| Artefacto | Estado | Propósito |
|----------|--------|---------|
| **Coverage Map YAML** (`coverage_map/coverage_map.yaml` o similar) | **Informativo** | Temas de mapeo de alto nivel entre evidencia/artefactos AIMO y marcos externos (ISO 42001, NIST AI RMF, EU AI Act, etc.) para explicabilidad. No impone requisitos de validación normativos. |
| **Profile JSONs** (`coverage_map/profiles/*.json`) | **Normativo** | Especificaciones de conversión validadas contra `schemas/jsonschema/aimo-profile.schema.json`. Definen mapeos legibles por máquina (p. ej. qué objetos AIMO se mapean a qué cláusulas de marco). El [Validador](../../validator/) ejecuta `--validate-profiles` para asegurar que todos los profile JSON oficiales conforman el esquema (patrón profile_id PR-*, enumeración target, target_version, mappings). |

### Perfiles oficiales (validados por validador)

Los Profile JSON están en `coverage_map/profiles/` y son validados por el validador (`--validate-profiles`). Nombres: nombre de archivo `<target>_<purpose>.json`; cada uno incluye `target_version`.

| File | profile_id | target | target_version |
|------|------------|--------|----------------|
| `iso42001.json` | PR-ISO42001-v0.1 | ISO_42001 | 1.0 |
| `iso_42001_readiness.json` | PR-ISO42001-READINESS-v0.1 | ISO_42001 | 2023 |
| `nist_ai_rmf.json` | PR-NIST-AI-RMF-v0.1 | NIST_AI_RMF | 1.0 |
| `nist_ai_600_1_genai.json` | PR-NIST-AI-600-1-v0.1 | NIST_AI_600_1 | 1.0 |
| `eu_ai_act_annex_iv.json` | PR-EU-AI-ACT-ANNEX-IV-v0.1 | EU_AI_ACT_ANNEX_IV | Annex IV |
| `eu_ai_act_high_risk.json` | PR-EU-AI-ACT-HIGH-RISK-v0.1 | EU_AI_ACT_HIGH_RISK | 2024/1689 |
| `eu_gp_ai_cop.json` | PR-EU-GPAI-COP-v0.1 | EU_GPAI_COP | current |
| `uk_atrs_procurement.json` | PR-UK-ATRS-v0.1 | UK_ATRS | current |
| `jp_gov_genai_procurement.json` | PR-JP-GOV-GENAI-PROCUREMENT-v0.1 | JP_GOV_GENAI_PROCUREMENT | current |

### Política de actualización de perfiles

- **Refs EU AI Act (0.1.2)**: Las referencias a artículos del EU AI Act en el mapeo de cobertura y en la documentación se alinearon con el Reglamento (UE) 2024/1689 para una preparación de evidencia coherente; solo informativo, no asesoramiento legal.
- **ISO 42001 / NIST AI RMF**: Nuevas versiones del marco objetivo pueden añadirse como nuevos archivos de perfil o nuevos valores `target_version` en una versión futura del estándar; los perfiles v0.1 permanecen congelados para la release v0.1.
- **EU AI Act Annex IV**: El Anexo IV y los artículos relacionados pueden ser actualizados por los reguladores; los mapeos de perfil pueden actualizarse vía **PATCH** (ej. 0.1.x) para seguir cambios de redacción o cláusulas manteniendo el mismo profile_id para continuidad. Los implementadores deben alinearse con la versión referenciada en `target_version` del perfil y las notas de release.

---

## Véase también

- [Paquete de Evidencia (resumen de artefacto)](../evidence-bundle/)
- [Estructura raíz del Paquete de Evidencia (v0.1)](../../standard/current/09-evidence-bundle-structure/)
- [Requisitos Mínimos de Evidencia](../minimum-evidence/)
- [Coverage Map (mapeos de marcos)](../../coverage-map/)
- [Validador](../../validator/)
