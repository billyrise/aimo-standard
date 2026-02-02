---
description: Mapeo de AIMO Standard a ISMS (ISO 27001/27002). Trazabilidad entre taxonomía AIMO y controles del sistema de gestión de seguridad de la información.
---

# Vista ISMS (ISO/IEC 27001/27002) mapeo

> Atajos de trazabilidad: Taxonomía → Requisitos Mínimos de Evidencia → Validador → Protocolo de Supervisión Humana.

- [Taxonomía](../standard/current/03-taxonomy.md)
- [Requisitos Mínimos de Evidencia](../artifacts/minimum-evidence.md)
- [Esquemas de Registro](../artifacts/log-schemas/index.md)
- [Validador](../validator/index.md)
- [Protocolo de Supervisión Humana](../governance/human-oversight-protocol.md)

Esta página mapea temas seleccionados de ISO/IEC 27001/27002 (gestión de cambios, control de acceso, registro, integridad de evidencia) a evidencia y artefactos AIMO. Es solo para explicabilidad; no garantiza conformidad con ISO/IEC 27001 o 27002. Verifique contra los estándares publicados.


## Tabla de mapeo

| Referencia del marco / tema | Evidencia AIMO / dónde en AIMO | Paquete de Evidencia / Evidencia Mínima | Artefactos y validación | Notas |
| --- | --- | --- | --- | --- |
| A.5.24 – Seguridad de la información en gestión de proyectos | [Alcance](../standard/current/02-scope.md) | solicitud, revisión | templates/ev/ | Informativo; verifique contra texto oficial. |
| A.5.29 – Seguridad de la información durante interrupción | [Evidencia Mínima](../artifacts/minimum-evidence.md) | excepción, renovación | templates/ev/ev_template.md | Informativo; verifique contra texto oficial. |
| A.5.30 – Preparación de TIC para continuidad del negocio | [Descripción General](../standard/current/01-overview.md) | Resumen; integridad | — | Informativo; verifique contra texto oficial. |
| A.8.1 – Inventario de activos | [Diccionario](../standard/current/05-dictionary.md) | Diccionario, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativo; verifique contra texto oficial. |
| A.8.2 – Clasificación de información | [Taxonomía](../standard/current/03-taxonomy.md) | Diccionario; revisión | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativo; verifique contra texto oficial. |
| A.8.3 – Control de acceso | [Evidencia Mínima](../artifacts/minimum-evidence.md) | —; integridad | — | Informativo; verifique contra texto oficial. |
| A.8.15 – Registro | [Plantilla EV](../standard/current/06-ev-template.md) | EV, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informativo; verifique contra texto oficial. |
| A.8.16 – Actividades de monitoreo | [Evidencia Mínima](../artifacts/minimum-evidence.md) | EV, change_log; change_log, integridad | templates/ev/ | Informativo; verifique contra texto oficial. |
| A.8.32 – Gestión de cambios | [Paquete de Evidencia](../artifacts/evidence-bundle.md) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | Informativo; verifique contra texto oficial. |
| A.8.33 – Información de pruebas | [Validador](../standard/current/07-validator.md) | EV | validator/rules/, validator/src/; schema_validate_ev | Informativo; verifique contra texto oficial. |
