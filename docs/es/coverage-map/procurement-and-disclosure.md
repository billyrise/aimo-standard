---
description: Superposiciones de contratación y divulgación (Reino Unido, Japón). ATRS UK, orientación de contratación UK, contratación GenAI del gobierno de Japón y directrices empresariales de IA. Solo mapeo de referencia.
---
<!-- aimo:translation_status=translated -->

# Superposiciones de contratación y divulgación (Reino Unido, Japón)

Esta página describe **mapeos de referencia** entre la evidencia AIMO y marcos de contratación y divulgación seleccionados del **Reino Unido** y **Japón**. El objetivo es **reducir la carga mediante la reutilización de la evidencia AIMO**. Es **mapeo informativo únicamente**; AIMO no garantiza el cumplimiento completo de los requisitos gubernamentales. Verifique contra las fuentes oficiales siguientes.

## Fuentes primarias

**Reino Unido**

- [Algorithmic Transparency Recording Standard (ATRS) Hub](https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub) — GOV.UK (plantilla, orientación, registros publicados)
- [Plantilla ATRS](https://www.gov.uk/government/publications/algorithmic-transparency-template) — Plantilla oficial para el sector público
- [Orientación para organizaciones que usan el ATRS](https://www.gov.uk/government/publications/guidance-for-organisations-using-the-algorithmic-transparency-standard/algorithmic-transparency-recording-standard-guidance-for-public-sector-bodies) — GOV.UK

**Japón**

- [Digital Agency — GenAI procurement and utilisation guideline](https://www.digital.go.jp/news/3579c42d-b11c-4756-b66e-3d3e35175623) — Digital Agency (Cabinet Secretariat)
- [AI Business Guidelines](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/index.html) — METI / MIC (Ministry of Economy, Trade and Industry / Ministry of Internal Affairs and Communications)

## Tabla de mapeo (Reino Unido)

| Requisito gubernamental (tema) | Artefactos AIMO | Dónde en el Evidence Bundle | Cobertura del validador | Nota |
| --- | --- | --- | --- | --- |
| ATRS — responsabilidad / propietario | Summary, review | manifest; objects/ (EV, Summary); payload_index | schema_validate_ev | Mapeo informativo; no garantiza conformidad completa. |
| ATRS — descripción del sistema / modelo | Dictionary, EV | objects/; schemas/jsonschema/aimo-dictionary.schema.json | schema_validate_dictionary | Adjuntar registro ATRS oficial en External Forms; enlazar por logical_id. |
| ATRS — consideraciones de riesgo | Dictionary, request, review, exception | objects/; templates/ev/ | schema_validate_ev | Perfil: `coverage_map/profiles/uk_atrs_procurement.json`. |
| Contratación — evidencia del proveedor | request, review, exception; Evidence Bundle | manifest, object_index, payload_index; examples/evidence_bundle_minimal/ | schema_validate_ev | Usar el paquete para estructurar evidencia; la orientación UK sigue siendo autorizada. |

## Tabla de mapeo (Japón)

| Requisito gubernamental (tema) | Artefactos AIMO | Dónde en el Evidence Bundle | Cobertura del validador | Nota |
| --- | --- | --- | --- | --- |
| Lista de verificación de contratación GenAI (Digital Agency) | External Form (lista tal cual); Dictionary, Summary | payload_index; sección External Forms; referencia en manifest | N/A (adjunto) | Mapeo informativo; no garantiza conformidad completa. Perfil: `coverage_map/profiles/jp_gov_genai_procurement.json`. |
| AI Business Guidelines — gobernanza / trazabilidad | Summary, dictionary, request, review, change_log | objects/; manifest; templates/ev/ | schema_validate_dictionary, schema_validate_ev | Mapear ítems de la lista a la taxonomía AIMO cuando sea útil. |
| Documentación de riesgo / responsabilidad | Dictionary, EV, review, exception | objects/; schemas/jsonschema/ | schema_validate_ev | Verificar contra orientación oficial de Digital Agency y METI/MIC. |

## Reino Unido: ATRS y contratación de IA (resumen)

| Tema | Evidencia AIMO / mapeo | Notas |
| --- | --- | --- |
| **ATRS UK** (registro de transparencia de IA) | Summary, review (responsable de rendición de cuentas), evidence (descripción de modelo/sistema), dictionary (consideraciones de riesgo). Perfil: `coverage_map/profiles/uk_atrs_procurement.json`. | Adjuntar o referenciar registro de transparencia tipo ATRS en Formularios externos; enlazar a objetos del paquete por logical_id. |
| **Orientación de contratación UK** | Request, review, exception; Paquete de Evidencia para evaluación de proveedores. | Usar el paquete AIMO para estructurar evidencia para evaluación de contratación; la orientación oficial UK sigue siendo autorizada. |

## Japón: Contratación GenAI del gobierno y directrices empresariales de IA (resumen)

| Tema | Evidencia AIMO / mapeo | Notas |
| --- | --- | --- |
| **Lista de verificación de contratación GenAI del gobierno JP** | Adjuntar lista como Formulario externo (p. ej. payload: JP_PROCUREMENT_CHECKLIST); referenciar en el manifest. Perfil: `coverage_map/profiles/jp_gov_genai_procurement.json`. | Solo mapeo de referencia; AIMO no sustituye listas oficiales. |
| **Directrices empresariales de IA** | Summary, dictionary; mapear ítems de la lista a códigos de taxonomía AIMO cuando sea útil para trazabilidad. | Usar para explicabilidad; verificar contra orientación oficial japonesa. |

## Cómo usar

- **Formularios externos**: Adjuntar plantillas/listas oficiales del Reino Unido o Japón **tal cual** (PDF, DOC, etc.), hashearlas y listarlas en el [payload_index](../../standard/current/09-evidence-bundle-structure/) del Paquete de Evidencia o en la [sección Formularios externos de la plantilla EV](../../standard/current/06-ev-template/). Referenciarlas por logical_id en el manifest y en mapeos de cobertura.
- **Perfiles**: Los perfiles anteriores definen mapeos opcionales legibles por máquina; no imponen obligaciones legales o contractuales.

Véase [Conformidad](../../conformance/) para niveles y [Requisitos Mínimos de Evidencia — Superposiciones regulatorias](../../artifacts/minimum-evidence/) para resumen de superposiciones.
