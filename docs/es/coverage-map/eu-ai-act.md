---
description: Mapeo de AIMO Standard a la Ley de IA de la UE. Trazabilidad entre códigos de taxonomía AIMO y categorías de riesgo y requisitos de la Ley de IA de la UE.
---
<!-- aimo:translation_status=translated -->

# Mapeo Ley de IA de la UE

> Atajos de trazabilidad: Taxonomía → Requisitos Mínimos de Evidencia → Validador → Protocolo de Supervisión Humana.

- [Taxonomía](../../standard/current/03-taxonomy/)
- [Requisitos Mínimos de Evidencia](../../artifacts/minimum-evidence/)
- [Esquemas de Registro](../../artifacts/log-schemas/)
- [Validador](../../validator/)
- [Protocolo de Supervisión Humana](../../governance/human-oversight-protocol/)

Esta página mapea temas seleccionados de la Ley de IA de la UE (documentación, registro, gestión de riesgos, supervisión humana, transparencia) a evidencia y artefactos AIMO. Es solo de alto nivel y **no** constituye asesoramiento jurídico ni garantiza conformidad. Verifique contra el texto legal oficial.

**Referencia:** Reglamento (UE) 2024/1689 (Ley de Inteligencia Artificial). Todos los números de artículo siguientes se refieren a ese reglamento.

## Tabla de mapeo

| Referencia del marco / tema | Evidencia AIMO / dónde en AIMO | Paquete de Evidencia / Evidencia Mínima | Artefactos y validación | Notas |
| --- | --- | --- | --- | --- |
| Art. 4 – Alfabetización en IA | [Alcance](../../standard/current/02-scope/) | Summary, EV; review | templates/ev/ | Transversal; evidencia de capacidad/formación organizativa (alto nivel). No es asesoramiento jurídico. Verifique contra texto oficial. |
| Art. 9 – Sistema de gestión de riesgos | [Alcance](../../standard/current/02-scope/) | request, review, exception, renewal | templates/ev/ | Sistemas de IA de alto riesgo (Título III). No es asesoramiento jurídico. Verifique contra texto oficial. |
| Art. 10 – Datos y gobernanza de datos | [Diccionario](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/; schema_validate_dictionary | No es asesoramiento jurídico. Verifique contra texto oficial. |
| Art. 11 – Documentación técnica (alto riesgo) | [Plantilla EV](../../standard/current/06-ev-template/), [Paquete de Evidencia](../../artifacts/evidence-bundle/) | EV, Dictionary, Summary; request, review | schemas/jsonschema/, templates/ev/; **Anexo IV**: [Ejemplos > Muestra Anexo IV UE](../../examples/) (`examples/evidence_bundle_v01_annex_iv_sample/`); perfil: `coverage_map/profiles/eu_ai_act_annex_iv.json`. Paquete de ejemplo conforme (signatures/, hashes/, payload con documentación técnica orientada al Anexo IV). Véase Ejemplos (más contenido en futura versión). | Solo alto nivel; no es asesoramiento jurídico. Verifique contra texto oficial. |
| Art. 12 – Registro | [Paquete de Evidencia](../../artifacts/evidence-bundle/), [Requisitos Mínimos de Evidencia](../../artifacts/minimum-evidence/) | EV, change_log, request, review | examples/evidence_bundle_minimal/; schema_validate_ev | No es asesoramiento jurídico. Verifique contra texto oficial. |
| Art. 13 – Transparencia e información a desplegadores/usuarios | [Alcance](../../standard/current/02-scope/) | Summary, EV; review | templates/ev/ | Contexto de alto riesgo. No es asesoramiento jurídico. Verifique contra texto oficial. |
| Art. 14 – Supervisión humana | [Requisitos Mínimos de Evidencia](../../artifacts/minimum-evidence/) | review, exception | templates/ev/ev_template.md | No es asesoramiento jurídico. Verifique contra texto oficial. |
| Art. 15 – Precisión, robustez, ciberseguridad | [Requisitos Mínimos de Evidencia](../../artifacts/minimum-evidence/) | EV (códigos de evidencia/riesgo, alto nivel) | templates/ev/ | Solo mapeo de alto nivel. No es asesoramiento jurídico. Verifique contra texto oficial. |
| Art. 17 – Sistema de gestión de la calidad | [Alcance](../../standard/current/02-scope/) | Summary, review (proceso organizativo) | templates/ev/ | Distinto del Art. 9 (sistema de gestión de riesgos). No es asesoramiento jurídico. Verifique contra texto oficial. |
| Obligaciones de transparencia (según caso de uso) | [Alcance](../../standard/current/02-scope/), [Requisitos Mínimos de Evidencia](../../artifacts/minimum-evidence/) | Summary, EV; review | templates/ev/ | Las disposiciones aplicables dependen del caso de uso (p. ej. riesgo limitado, obligaciones del desplegador). No es asesoramiento jurídico. Verifique contra texto oficial. |
| Obligaciones de modelos GPAI | [Plantilla EV](../../standard/current/06-ev-template/), [Paquete de Evidencia](../../artifacts/evidence-bundle/) | Plantilla EV, Paquete de Evidencia (marco de estructuración de evidencia) | schemas/jsonschema/; schema_validate_ev | AIMO proporciona un marco para organizar la evidencia; las obligaciones reales las define el reglamento. No es asesoramiento jurídico. Verifique contra texto oficial. |
| Considerandos – Responsabilidad | [Paquete de Evidencia](../../artifacts/evidence-bundle/) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | No es asesoramiento jurídico. Verifique contra texto oficial. |

## Fechas de aplicación / aplicabilidad (alto nivel)

Lo siguiente se alinea con el **calendario oficial de la UE** (Servicio de la Ley de IA / Comisión). **No es asesoramiento jurídico** y no garantiza exactitud. Confirme siempre con el **texto legal oficial** y las autoridades competentes.

| Fase | Fecha | Qué se aplica (alto nivel) |
| --- | --- | --- |
| Entrada en vigor | Agosto 2024 | Reglamento en vigor; la mayoría de obligaciones sustantivas aún no aplicables. |
| Disposiciones generales y prohibiciones | 02 feb 2025 | Prácticas prohibidas (riesgo inaceptable); ciertas disposiciones sobre alfabetización en IA. |
| Normas GPAI y gobernanza | 02 ago 2025 | Normas sobre organismos notificados, GPAI, gobernanza, confidencialidad, sanciones; códigos de conducta. |
| Normas principales + Anexo III alto riesgo + Art. 50 transparencia | 02 ago 2026 | Aplicabilidad plena para sistemas de IA de alto riesgo (Anexo III), obligaciones de transparencia del Art. 50. |
| Alto riesgo embebido en productos regulados | 02 ago 2027 | Sistemas de IA de alto riesgo embebidos en productos sujetos a la legislación de productos de la UE. |

## Normas armonizadas y presunción de conformidad (Art. 40)

Cuando se publiquen **normas armonizadas** en el Diario Oficial de la UE con arreglo a la Ley de IA, su cumplimiento puede dar **presunción de conformidad** con los requisitos correspondientes. La lista y fechas exactas dependen del trabajo de normalización y la publicación en el DO. Los mapeos AIMO son informativos y no confieren presunción de conformidad. Para el estado actual, véase la [estandarización de la Ley de IA](https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation) de la Comisión y **Referencias** más abajo.

## Directrices 2026 de la Oficina de IA (detalle de aplicación)

La Comisión Europea ha indicado que la **Oficina de IA** preparará **directrices prácticas** durante 2026, entre otras sobre:

- Clasificación de alto riesgo
- Aplicación del Art. 50 (transparencia)
- Notificación de incidentes
- Elementos relacionados con el SGQ

Estas directrices son **desencadenantes de actualización** para perfiles y mapeos de cobertura AIMO: una vez publicadas, los adoptantes deben alinear la evidencia y los mapeos con la última orientación oficial. AIMO no interpreta ni garantiza conformidad con estas directrices.

!!! warning "No es asesoramiento jurídico"
    Esta página es solo para uso explicativo. Debe verificar la aplicabilidad y las fechas contra el reglamento oficial y cualquier acto de ejecución o modificación. AIMO no proporciona asesoramiento jurídico ni garantiza conformidad.

!!! note "Nota legal / Mapeo informativo"
    Esta página es **informativa**. La interpretación jurídica debe basarse en el reglamento oficial (EUR-Lex) y en las publicaciones de la Comisión Europea. AIMO no proporciona asesoramiento jurídico ni garantiza conformidad.

## Referencias

**Fuentes primarias**

- [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689) (EUR-Lex) — Ley de Inteligencia Artificial (texto legal)
- [Calendario de aplicación de la Ley de IA de la UE](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act) — Servicio de la Ley de IA de la Comisión Europea (calendario de aplicación)
- [Estandarización de la Ley de IA](https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation) — Estrategia Digital de la Comisión Europea (normas armonizadas, presunción de conformidad)

**Otros**

- Comisión Europea / Oficina de IA — directrices y calendario (véase Servicio de la Ley de IA y noticias de la Comisión para URLs actuales)
- [EPRS — Aplicación de la Ley de IA de la UE](https://www.europarl.europa.eu/thinktank/) — resumen del Parlamento (informativo)
