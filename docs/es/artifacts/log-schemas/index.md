---
description: Esquemas de Registro AIMO - Formatos de registro neutrales a proveedores para evidencia de IA. Incluye esquemas de descubrimiento de Shadow AI y monitoreo de actividad de agentes.
---

# Esquemas de Registro

## Qué es esto

Esta sección define **formatos de registro normalizados** para evidencia que puede incluirse en un Paquete de Evidencia. Estos esquemas proporcionan una estructura neutral a proveedores para registros relacionados con monitoreo de uso de IA y operaciones agénticas.

## Cuándo usar

- **Visibilidad de Shadow AI**: Documentar detección, inventario y remediación de uso no aprobado de IA.
- **Auditorías de operaciones agénticas**: Explicar ejercicio de privilegios de agentes autónomos, ejecución de herramientas y operaciones recursivas.
- **Reproducibilidad de incidentes**: Proporcionar evidencia estructurada para investigación de incidentes y análisis de causa raíz.

## Qué NO es

!!! warning "Importante"
    Estos esquemas definen **formatos de registro para envío de evidencia**. NO:

    - Recopilan automáticamente registros de sus sistemas
    - Proporcionan herramientas de agregación o monitoreo de registros
    - Garantizan cumplimiento con ninguna regulación o estándar
    - Reemplazan implementaciones de registro específicas de proveedores

    Las organizaciones deben implementar sus propios pipelines de recopilación de registros y normalizar los registros a estos esquemas para envío de evidencia.

## Esquemas

| Esquema | Propósito | Descargar |
| --- | --- | --- |
| [Registro de Descubrimiento de Shadow AI](shadow-ai-discovery.md) | Detección e inventario de uso no aprobado de IA | [shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json) |
| [Registro de Actividad de Agente](agent-activity.md) | Ejercicio de privilegios de IA agéntica y ejecución de herramientas | [agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json) |

## Páginas relacionadas

- [Requisitos Mínimos de Evidencia](../minimum-evidence.md) — Lista de verificación de evidencia de nivel DEBE
- [Paquete de Evidencia](../evidence-bundle.md) — Estructura del paquete e índice
- [Taxonomía](../../standard/current/03-taxonomy.md) — Códigos de clasificación (incluyendo UC-010 Automatización Agéntica, IM-007 Shadow/No Gestionado)
