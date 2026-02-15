---
description: Superposiciones de contratación y divulgación (Reino Unido, Japón). ATRS UK, orientación de contratación UK, contratación GenAI del gobierno de Japón y directrices empresariales de IA. Solo mapeo de referencia.
---
<!-- aimo:translation_status=translated -->

# Superposiciones de contratación y divulgación (Reino Unido, Japón)

Esta página describe **mapeos de referencia** entre la evidencia AIMO y marcos de contratación y divulgación seleccionados del **Reino Unido** y **Japón**. Es **solo mapeo de referencia**; AIMO no sustituye listas de verificación oficiales ni orientación gubernamental.

## Reino Unido: ATRS y contratación de IA

| Tema | Evidencia AIMO / mapeo | Notas |
| --- | --- | --- |
| **ATRS UK** (registro de transparencia de IA) | Summary, review (responsable de rendición de cuentas), evidence (descripción de modelo/sistema), dictionary (consideraciones de riesgo). Perfil: `coverage_map/profiles/uk_atrs_procurement.json`. | Adjuntar o referenciar registro de transparencia tipo ATRS en Formularios externos; enlazar a objetos del paquete por logical_id. |
| **Orientación de contratación UK** | Request, review, exception; Paquete de Evidencia para evaluación de proveedores. | Usar el paquete AIMO para estructurar evidencia para evaluación de contratación; la orientación oficial UK sigue siendo autorizada. |

## Japón: Contratación GenAI del gobierno y directrices empresariales de IA

| Tema | Evidencia AIMO / mapeo | Notas |
| --- | --- | --- |
| **Lista de verificación de contratación GenAI del gobierno JP** | Adjuntar lista como Formulario externo (p. ej. payload: JP_PROCUREMENT_CHECKLIST); referenciar en el manifest. Perfil: `coverage_map/profiles/jp_gov_genai_procurement.json`. | Solo mapeo de referencia; AIMO no sustituye listas oficiales. |
| **Directrices empresariales de IA** | Summary, dictionary; mapear ítems de la lista a códigos de taxonomía AIMO cuando sea útil para trazabilidad. | Usar para explicabilidad; verificar contra orientación oficial japonesa. |

## Cómo usar

- **Formularios externos**: Adjuntar plantillas/listas oficiales del Reino Unido o Japón **tal cual** (PDF, DOC, etc.), hashearlas y listarlas en el [payload_index](../../standard/current/09-evidence-bundle-structure/) del Paquete de Evidencia o en la [sección Formularios externos de la plantilla EV](../../standard/current/06-ev-template/). Referenciarlas por logical_id en el manifest y en mapeos de cobertura.
- **Perfiles**: Los perfiles anteriores definen mapeos opcionales legibles por máquina; no imponen obligaciones legales o contractuales.

Véase [Conformidad](../../conformance/) para niveles y [Requisitos Mínimos de Evidencia — Superposiciones regulatorias](../../artifacts/minimum-evidence/) para resumen de superposiciones.
