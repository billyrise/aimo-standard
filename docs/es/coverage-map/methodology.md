---
description: Metodología del Mapa de Cobertura - Cómo AIMO mapea a marcos externos. Uso en auditorías, relación con Paquete de Evidencia y enfoque de trazabilidad.
---

# Metodología

> Nota: Esta metodología soporta trazabilidad y preparación de evidencia. No garantiza cumplimiento con ninguna regulación/estándar específico.

Esta página explica qué es y qué no es el Mapa de Cobertura, cómo usarlo en auditoría, y cómo se relaciona con el Paquete de Evidencia y los Requisitos Mínimos de Evidencia.

## Qué es el mapeo

- Un mapeo **informativo** desde referencias de marcos/regulaciones externos (por tema) a evidencia AIMO, elementos TOC del Paquete de Evidencia, grupos de ciclo de vida de Evidencia Mínima, artefactos y verificaciones del validador.
- Una herramienta de soporte para **explicabilidad**: qué evidencia y artefactos AIMO pueden ayudar a demostrar o explicar alineación con un requisito externo dado (sin reclamar conformidad).

## Qué no es el mapeo

- **No** es una garantía de cumplimiento con ningún marco o regulación.
- **No** es asesoramiento legal ni un sustituto de verificación contra textos autoritativos.
- **No** es exhaustivo; es un subconjunto práctico para preparación de auditoría y explicabilidad.

## Cómo usarlo en auditoría

Use el flujo: **requisito → evidencia → artefacto → validación**.

1. **Requisito**: Identifique la referencia del marco externo y el tema (ej. documentación ISO 42001, mantenimiento de registros EU AI Act).
2. **Evidencia**: Vea qué elementos del Paquete de Evidencia AIMO y grupos de ciclo de vida de Evidencia Mínima (solicitud, revisión, excepción, renovación, change_log, integridad) soportan explicabilidad para ese requisito.
3. **Artefacto**: Localice los artefactos (esquemas, plantillas, ejemplos) que implementan o ilustran esa evidencia.
4. **Validación**: Use el validador y verificaciones de esquema referenciadas para verificar consistencia estructural.

Los lectores deben verificar contra el texto autoritativo de cada marco o regulación.

## Relación con Paquete de Evidencia y Requisitos Mínimos de Evidencia

- **[Paquete de Evidencia](../../artifacts/evidence-bundle/)**: Define la estructura del paquete, TOC y trazabilidad. Las filas del Mapa de Cobertura referencian secciones del Paquete de Evidencia (ej. EV, Diccionario, Resumen, change_log, solicitud, revisión, excepción, renovación).
- **[Requisitos Mínimos de Evidencia](../../artifacts/minimum-evidence/)**: Define grupos de ciclo de vida de nivel DEBE (solicitud, revisión, excepción, renovación, change_log, integridad). Las filas del Mapa de Cobertura referencian estos grupos en `minimum_evidence_refs`.

Use el Mapa de Cobertura para ver qué elementos del Paquete de Evidencia y grupos de Evidencia Mínima soportan explicabilidad para un requisito externo dado.

## Declaración de no sobre-reclamación

!!! warning "Importante"
    El AIMO Standard soporta **explicabilidad y preparación de evidencia**. **No** proporciona asesoramiento legal, garantiza cumplimiento ni certifica conformidad con ninguna regulación o marco. Los adoptantes deben verificar reclamaciones contra textos autoritativos y obtener asesoramiento profesional según sea apropiado.

Consulte [Límite de Responsabilidad](../../governance/responsibility-boundary/) para alcance, suposiciones y responsabilidades del adoptante.

## Recorrido de auditoría

Desde esta página, continúe a:

1. **Mapeos de marcos**: [ISO 42001](../iso-42001/), [NIST AI RMF](../nist-ai-rmf/), [EU AI Act](../eu-ai-act/), [ISMS](../isms/)
2. **Validar**: [Validador](../../validator/) — ejecutar verificaciones estructurales
3. **Descargar**: [Versiones](../../releases/) — obtener activos de versión
