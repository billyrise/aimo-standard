---
description: Estructura del Paquete de Evidencia AIMO. Formato de paquete de auditoría con índice, trazabilidad y artefactos para cumplimiento de gobernanza de IA y entrega a auditores.
---

# Paquete de Evidencia

Un **Paquete de Evidencia** es un paquete de auditoría: un conjunto estructurado de artefactos que respalda la explicabilidad y trazabilidad para la gobernanza de IA. No es una característica del producto sino un formato de entrega para auditores y cumplimiento.

## Estructura y nomenclatura del paquete

- **Nomenclatura de la raíz del paquete**: use un patrón consistente como `{org}_{sistema}_{período}_{versión}` (ej. `acme_ai-usage_2026-Q1_v1`).
- **Archivos requeridos**: al menos un conjunto de Evidencia (EV) alineado con la [Plantilla Evidence Pack (EP)](../../standard/current/06-ev-template/), un [Diccionario](../../standard/current/05-dictionary/), un breve **Resumen** (resumen ejecutivo del paquete), y un **Registro de Cambios** (o referencia a él) para cambios al paquete o su contenido.
- **Adjuntos opcionales**: registros, registros de revisión, aprobaciones de excepciones, registros de renovación; mantenga la nomenclatura consistente y referenciable desde el EV/Diccionario principal.

## Tabla de contenido (TOC)

| Sección | Artefacto | ¿Requerido? | Propósito | Campos mínimos | Validación |
| --- | --- | --- | --- | --- | --- |
| Evidencia | Registros EV (JSON/array) | Sí | Registro de lo que sucedió; enlace a solicitud/revisión/excepción/renovación | id, timestamp, source, summary; refs de ciclo de vida opcionales | [Validador](../../validator/), aimo-ev.schema.json |
| Diccionario | dictionary.json | Sí | Claves/etiquetas/descripciones para códigos y dimensiones | entries (key, label, description) | aimo-dictionary.schema.json |
| Resumen | resumen (doc o campo) | Sí | Descripción general de una página para auditores | alcance, período, decisiones clave, excepciones | — |
| Registro de cambios | change_log o referencia | Sí | Pista de auditoría de cambios del paquete/contenido | id, timestamp, actor, descripción del cambio, referencias | — |
| Solicitud | registro(s) de solicitud | Si aplica | Solicitud/petición de uso | id, timestamp, actor/rol, alcance, justificación | — |
| Revisión/Aprobación | registro(s) de revisión | Si aplica | Resultado de revisión y aprobación | id, timestamp, actor/rol, decisión, referencias | — |
| Excepción | registro(s) de excepción | Si aplica | Excepción con controles compensatorios y vencimiento | id, timestamp, alcance, vencimiento, controles compensatorios, ref de renovación | — |
| Renovación | registro(s) de renovación | Si aplica | Reevaluación y renovación | id, timestamp, actor/rol, decisión, referencias a excepción/EV anterior | — |

## Relación normativa: registros EV (índice) y Evidence Pack (payload)

Para evitar doble construcción y ambigüedad en auditoría, lo siguiente es **normativo**: (1) Los registros EV (JSON) son el **índice/ledger** (trazabilidad verificable por máquina). (2) Los archivos del Evidence Pack (EP-01..EP-07 y manifiesto) son el **payload**. (3) Los registros EV DEBERÍAN referenciar el payload mediante `evidence_file_ids` (ej. EP-01) y/o hashes; el [Validador](../../validator/) comprueba la integridad referencial. (4) **Conjunto mínimo de entrega**: EV JSON + Dictionary + Summary + Change Log + Evidence Pack (zip). Véase [Plantilla Evidence Pack](../../standard/current/06-ev-template/) para tipos de documento EP-01..EP-07.

## Trazabilidad

- **IDs estables**: cada registro (EV, solicitud, revisión, excepción, renovación, entrada de registro de cambios) DEBE tener un identificador estable y único.
- **Referencias cruzadas**: enlace Solicitud → Revisión → Excepción (si existe) → Renovación y enlace elementos EV a estos mediante campos de referencia (ej. `request_id`, `review_id`, `exception_id`, `renewal_id`).
- **Vinculación**: asegúrese de que los auditores puedan seguir una cadena desde un uso de IA (o excepción) hasta la solicitud, aprobación, cualquier excepción y sus controles compensatorios y vencimiento, y renovación.

## Cómo usan esto los auditores

Los auditores usan el Paquete de Evidencia para verificar que el uso de IA se solicita, revisa y aprueba; que las excepciones tienen límite de tiempo y tienen controles compensatorios y renovación; y que los cambios se registran. Las reglas de TOC y trazabilidad les permiten localizar artefactos requeridos y seguir IDs y referencias a través de registros de solicitud, revisión, excepción, renovación y EV. El Resumen proporciona una visión general rápida; el Registro de Cambios respalda el control de cambios y la responsabilidad.

Consulte [Requisitos Mínimos de Evidencia](../minimum-evidence/) para campos de nivel DEBE y grupos de ciclo de vida.

## Guía operacional

!!! info "Integridad y control de acceso"
    Aunque AIMO no prescribe controles específicos, los adoptantes deben documentar:
    
    - **Roles de acceso**: quién puede crear, leer, actualizar o eliminar evidencia
    - **Política de retención**: cuánto tiempo se retiene la evidencia y bajo qué calendario
    - **Mecanismos de integridad**: hash, almacenamiento WORM o firmas digitales utilizadas
    - **Pista de auditoría**: registros de acceso y cambios al paquete
    
    Consulte [Requisitos Mínimos de Evidencia > Integridad y Acceso](../minimum-evidence/#6-integridad-acceso) para guía detallada.

## Recorrido de auditoría

Desde esta página, el recorrido de auditoría típico continúa:

1. **Siguiente**: [Requisitos Mínimos de Evidencia](../minimum-evidence/) — lista de verificación de nivel DEBE por ciclo de vida
2. **Luego**: [Mapa de Cobertura](../../coverage-map/) — mapeo a marcos externos
3. **Validar**: [Validador](../../validator/) — ejecutar verificaciones estructurales
4. **Descargar**: [Versiones](../../releases/) — obtener activos de versión y verificar sumas de verificación
