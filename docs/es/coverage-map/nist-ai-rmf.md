---
description: Mapeo de AIMO Standard a NIST AI RMF. Trazabilidad entre códigos de taxonomía AIMO y funciones del Marco de Gestión de Riesgos de IA de NIST.
---

# Mapeo NIST AI RMF

> Atajos de trazabilidad: Taxonomía → Requisitos Mínimos de Evidencia → Validador → Protocolo de Supervisión Humana.

- [Taxonomía](../../standard/current/03-taxonomy/)
- [Requisitos Mínimos de Evidencia](../../artifacts/minimum-evidence/)
- [Esquemas de Registro](../../artifacts/log-schemas/)
- [Validador](../../validator/)
- [Protocolo de Supervisión Humana](../../governance/human-oversight-protocol/)

Esta página mapea temas seleccionados del Marco de Gestión de Riesgos de IA de NIST (Gobernar, Mapear, Medir, Gestionar) a evidencia y artefactos AIMO. Es solo para explicabilidad; no garantiza conformidad con NIST AI RMF. Verifique contra la publicación de NIST.


## Tabla de mapeo

| Referencia del marco / tema | Evidencia AIMO / dónde en AIMO | Paquete de Evidencia / Evidencia Mínima | Artefactos y validación | Notas |
| --- | --- | --- | --- | --- |
| Govern 1.1 – Políticas | [Alcance](../../standard/current/02-scope/), [Taxonomía](../../standard/current/03-taxonomy/) | Diccionario, Resumen, revisión; revisión | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativo; verifique contra publicación de NIST. |
| Govern 1.2 – Roles y responsabilidades | [Evidencia Mínima](../../artifacts/minimum-evidence/) | solicitud, revisión | templates/ev/ev_template.md | Informativo; verifique contra publicación de NIST. |
| Govern 2.1 – Responsabilidad | [Paquete de Evidencia](../../artifacts/evidence-bundle/) | EV, solicitud, revisión, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | Informativo; verifique contra publicación de NIST. |
| Govern 3.1 – Gestión de riesgos | [Alcance](../../standard/current/02-scope/) | solicitud, revisión, excepción | templates/ev/ | Informativo; verifique contra publicación de NIST. |
| Govern 4.1 – Cultura | [Descripción General](../../standard/current/01-overview/) | Resumen, revisión; revisión | — | Informativo; verifique contra publicación de NIST. |
| Map 1.1 – Mapeo de contexto | [Alcance](../../standard/current/02-scope/), [Diccionario](../../standard/current/05-dictionary/) | Diccionario, Resumen; solicitud | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativo; verifique contra publicación de NIST. |
| Map 2.1 – Datos y documentación | [Plantilla EV](../../standard/current/06-ev-template/) | EV, Diccionario, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informativo; verifique contra publicación de NIST. |
| Map 3.1 – Gobernanza de datos | [Diccionario](../../standard/current/05-dictionary/) | Diccionario, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativo; verifique contra publicación de NIST. |
| Measure 1.1 – Rendimiento e impacto | [Plantilla EV](../../standard/current/06-ev-template/) | EV | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informativo; verifique contra publicación de NIST. |
| Measure 2.1 – Monitoreo | [Evidencia Mínima](../../artifacts/minimum-evidence/) | EV, change_log; change_log, integridad | templates/ev/ | Informativo; verifique contra publicación de NIST. |
| Measure 3.1 – Pruebas y validación | [Validador](../../standard/current/07-validator/) | EV | validator/rules/, validator/src/; schema_validate_ev | Informativo; verifique contra publicación de NIST. |
| Manage 1.1 – Asignación de recursos | [Descripción General](../../standard/current/01-overview/) | Resumen, revisión; revisión | — | Informativo; verifique contra publicación de NIST. |
| Manage 2.1 – Incidentes y respuestas | [Evidencia Mínima](../../artifacts/minimum-evidence/) | excepción, renovación, change_log | templates/ev/ev_template.md | Informativo; verifique contra publicación de NIST. |
| Manage 3.1 – Gestión de cambios | [Paquete de Evidencia](../../artifacts/evidence-bundle/) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | Informativo; verifique contra publicación de NIST. |
| Manage 4.1 – Revisión y actualización | [Evidencia Mínima](../../artifacts/minimum-evidence/) | renovación, revisión; revisión, renovación | templates/ev/ | Informativo; verifique contra publicación de NIST. |
| Manage 5.1 – Comunicación | [Paquete de Evidencia](../../artifacts/evidence-bundle/) | Resumen, change_log; change_log | templates/ev/ | Informativo; verifique contra publicación de NIST. |
