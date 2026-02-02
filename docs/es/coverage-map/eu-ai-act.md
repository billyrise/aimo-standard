---
description: Mapeo de AIMO Standard a EU AI Act. Trazabilidad entre códigos de taxonomía AIMO y categorías de riesgo y requisitos del EU AI Act.
---

# Mapeo EU AI Act

> Atajos de trazabilidad: Taxonomía → Requisitos Mínimos de Evidencia → Validador → Protocolo de Supervisión Humana.

- [Taxonomía](../standard/current/03-taxonomy.md)
- [Requisitos Mínimos de Evidencia](../artifacts/minimum-evidence.md)
- [Esquemas de Registro](../artifacts/log-schemas/index.md)
- [Validador](../validator/index.md)
- [Protocolo de Supervisión Humana](../governance/human-oversight-protocol.md)

Esta página mapea temas seleccionados del EU AI Act (documentación, mantenimiento de registros, gestión de riesgos, supervisión humana, transparencia) a evidencia y artefactos AIMO. Es solo de alto nivel y **no** constituye asesoramiento legal ni garantiza conformidad. Verifique contra el texto legal oficial.


## Tabla de mapeo

| Referencia del marco / tema | Evidencia AIMO / dónde en AIMO | Paquete de Evidencia / Evidencia Mínima | Artefactos y validación | Notas |
| --- | --- | --- | --- | --- |
| Art 9 – Gestión de riesgos (obligaciones) | [Alcance](../standard/current/02-scope.md) | solicitud, revisión, excepción | templates/ev/ | Solo alto nivel; no es asesoramiento legal. Verifique contra texto oficial. |
| Art 10 – Gobernanza de datos | [Diccionario](../standard/current/05-dictionary.md) | Diccionario, EV | schemas/jsonschema/; schema_validate_dictionary | Solo alto nivel; no es asesoramiento legal. Verifique contra texto oficial. |
| Art 11 – Documentación (alto riesgo) | [Plantilla EV](../standard/current/06-ev-template.md), [Paquete de Evidencia](../artifacts/evidence-bundle.md) | EV, Diccionario, Resumen; solicitud, revisión | schemas/jsonschema/, templates/ev/; schema_validate_ev | Solo alto nivel; no es asesoramiento legal. Verifique contra texto oficial. |
| Art 12 – Mantenimiento de registros | [Paquete de Evidencia](../artifacts/evidence-bundle.md), [Evidencia Mínima](../artifacts/minimum-evidence.md) | EV, change_log, solicitud, revisión | examples/evidence_bundle_minimal/; schema_validate_ev | Solo alto nivel; no es asesoramiento legal. Verifique contra texto oficial. |
| Art 13 – Transparencia (información al usuario) | [Alcance](../standard/current/02-scope.md) | Resumen, EV; revisión | templates/ev/ | Solo alto nivel; no es asesoramiento legal. Verifique contra texto oficial. |
| Art 14 – Supervisión humana | [Evidencia Mínima](../artifacts/minimum-evidence.md) | revisión, excepción; revisión, excepción | templates/ev/ev_template.md | Solo alto nivel; no es asesoramiento legal. Verifique contra texto oficial. |
| Art 17 – Gestión de riesgos (alto riesgo) | [Alcance](../standard/current/02-scope.md) | solicitud, revisión, excepción, renovación | templates/ev/ | Solo alto nivel; no es asesoramiento legal. Verifique contra texto oficial. |
| Art 26 – Transparencia (riesgo limitado) | [Alcance](../standard/current/02-scope.md) | Resumen, EV; revisión | templates/ev/ | Solo alto nivel; no es asesoramiento legal. Verifique contra texto oficial. |
| Art 29 – Documentación (IA de propósito general) | [Plantilla EV](../standard/current/06-ev-template.md) | EV, Diccionario, Resumen; solicitud, revisión | schemas/jsonschema/; schema_validate_ev | Solo alto nivel; no es asesoramiento legal. Verifique contra texto oficial. |
| Art 52 – Transparencia (implementador) | [Evidencia Mínima](../artifacts/minimum-evidence.md) | EV, Resumen; revisión | templates/ev/ | Solo alto nivel; no es asesoramiento legal. Verifique contra texto oficial. |
| Considerandos – Responsabilidad | [Paquete de Evidencia](../artifacts/evidence-bundle.md) | EV, solicitud, revisión, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | Solo alto nivel; no es asesoramiento legal. Verifique contra texto oficial. |
