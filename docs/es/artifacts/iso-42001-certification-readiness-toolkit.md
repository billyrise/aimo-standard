---
description: Kit de preparación para certificación ISO/IEC 42001. Ruta más corta hacia evidencia lista para auditoría alineada con ISO 42001 usando artefactos AIMO. Solo apoya la preparación; no confiere certificación.
---
<!-- aimo:translation_status=translated -->

# Kit de preparación para certificación ISO/IEC 42001

Esta página es una guía **práctica y orientada a la adopción** para producir **evidencia lista para auditoría** alineada con ISO/IEC 42001 usando artefactos AIMO. **Apoya la preparación**; **no** confiere certificación. Las decisiones de certificación corresponden a **organismos de certificación acreditados**.

## Objetivo

Producir un Evidence Bundle estructurado y comprobado por el validador que apoye controles tipo ISO/IEC 42001 (contexto, liderazgo, planificación, soporte, operación, evaluación del desempeño, mejora), de modo que los auditores puedan localizar y verificar la evidencia con eficacia.

## Flujo de trabajo en 5 pasos

| Paso | Acción |
| --- | --- |
| **1. Establecer alcance e inventario de IA** | Definir alcance (scope_ref); clasificar sistemas de IA con la [taxonomía](../../standard/current/03-taxonomy/) y el [diccionario](../../standard/current/05-dictionary/). |
| **2. Definir artefactos del sistema de gestión** | Crear o referenciar políticas, roles y artefactos alineados con PDCA. Usar [AIMO-MS / AIMO-Controls](../../conformance/) como estructura; referenciar [Plantilla Evidence Pack](../../standard/current/06-ev-template/) (EP-01..EP-07). |
| **3. Producir Evidence Bundle y evidencia mínima** | Construir manifest, object_index, payload_index, hash_chain, signing según [estructura del Paquete de Evidencia](../../standard/current/09-evidence-bundle-structure/). Incluir request, review, exception, renewal, change_log según [Requisitos mínimos de evidencia](minimum-evidence.md). |
| **4. Ejecutar validador + sumas de comprobación + control de cambios** | Ejecutar `python validator/src/validate.py <bundle_path> --validate-profiles`. Registrar versión del validador y salida. Generar sumas SHA-256; mantener entradas del registro de cambios que referencien los objetos afectados. |
| **5. Preparar paquete de auditoría** | Empaquetar el paquete (zip o similar); proporcionar sumas de comprobación. Opcionalmente adjuntar [salida del informe de auditoría](../../standard/current/07-validator/) (audit-json / audit-html). Usar URLs versionadas (ej. `/0.1.2/`) al citar el estándar. Para nivel Audit-Ready, añadir [Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index) y [External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is). |

## Lista de comprobación: familia de cláusulas ISO 42001 → artefactos AIMO → salidas de evidencia

| Familia de cláusulas ISO 42001 | Artefactos AIMO | Salidas de evidencia |
| --- | --- | --- |
| Contexto (4.1) | Summary, Dictionary, scope_ref | scope_ref del manifiesto; Summary; Dictionary |
| Liderazgo / Política (5.x) | Summary, review, dictionary | Registros de revisión; referencias a política |
| Planificación (6.x) | request, review, exception, EV, Dictionary | Solicitud/aprobación; riesgo/objetivos en EV o Dictionary |
| Soporte (7.x) | Summary, review, EV, change_log | Documentación; evidencia de competencia/concienciación |
| Operación (8.x) | EV, request, review, exception | Controles operativos; aplicabilidad |
| Evaluación del desempeño (9.x) | EV, change_log, review, renewal | Seguimiento; auditoría interna; revisión por la dirección |
| Mejora (10.x) | exception, renewal, change_log | Acción correctiva; mejora continua |

Véase [Coverage Map — ISO/IEC 42001](../../coverage-map/iso-42001/) y [ISO/IEC 42006](https://www.iso.org/standard/42006) para expectativas de organismos de auditoría.

## Lenguaje seguro

- **Usar:** "Utilizamos artefactos AIMO para apoyar la preparación para ISO/IEC 42001; las decisiones de certificación corresponden a organismos de certificación acreditados."
- **No usar:** "ISO 42001 certificado por AIMO" o "AIMO certifica la conformidad."

Estándar oficial (fuente primaria): [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) (ISO). Este kit se alinea con [Conformidad](../../conformance/) y [Límite de responsabilidad](../../governance/responsibility-boundary/) — AIMO no certifica ni garantiza conformidad.

## Relacionado

- [Conformidad](../../conformance/) — Niveles (Foundation, Operational, Audit-Ready) y lenguaje de declaración
- [Trust Package](../../governance/trust-package/) — Materiales listos para auditor
- [Responsibility Boundary](../../governance/responsibility-boundary/) — Qué proporciona y no proporciona AIMO
