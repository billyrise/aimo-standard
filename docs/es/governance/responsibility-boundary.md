---
description: Límite de Responsabilidad AIMO - Define qué proporciona el estándar vs. responsabilidades del adoptante. Declaración de no sobre-reclamación y limitaciones de alcance.
---

# Límite de Responsabilidad

Esta página define qué proporciona y qué no proporciona el AIMO Standard, las suposiciones que hace y las responsabilidades de los adoptantes.

## Qué proporciona AIMO Standard

- **Un formato de evidencia estructurado**: esquemas, plantillas y taxonomía para evidencia de gobernanza de IA.
- **Marco de trazabilidad**: vinculación de evidencia basada en ciclo de vida (solicitud → revisión → excepción → renovación).
- **Soporte de explicabilidad**: mapeo de cobertura a marcos externos para discusiones de auditoría.
- **Herramientas de validación**: validador de referencia y reglas para verificaciones de consistencia estructural.
- **Documentación**: especificación normativa, ejemplos y guía.

## Qué NO proporciona AIMO Standard

| Fuera de alcance | Explicación |
| --- | --- |
| **Asesoramiento legal** | AIMO no interpreta leyes ni regulaciones. Consulte asesor legal calificado para cumplimiento regulatorio. |
| **Certificación de cumplimiento** | Usar AIMO no certifica cumplimiento con ninguna regulación o marco (ISO 42001, EU AI Act, NIST AI RMF, etc.). |
| **Evaluación de riesgos** | AIMO estructura evidencia pero no realiza ni valida evaluaciones de riesgo de IA. |
| **Controles técnicos** | AIMO no implementa control de acceso, cifrado u otros controles de seguridad; documenta expectativas. |
| **Ejecución de auditoría** | AIMO proporciona materiales para auditores pero no conduce auditorías. |
| **Evaluación de modelo de IA** | AIMO no evalúa rendimiento del modelo, sesgo o seguridad. |

## Suposiciones

El AIMO Standard asume:

1. **Los adoptantes tienen procesos de gobernanza**: existen flujos de trabajo de solicitud, revisión, aprobación y excepción.
2. **Los adoptantes mantienen evidencia**: la evidencia es creada, almacenada y retenida por los sistemas del adoptante.
3. **Los adoptantes verifican contra textos autoritativos**: al usar el Mapa de Cobertura, los adoptantes verifican el marco o regulación original.
4. **El tooling es opcional**: el validador de referencia es una conveniencia; los adoptantes pueden usar su propia validación.

## Responsabilidades del adoptante

| Responsabilidad | Descripción |
| --- | --- |
| **Creación de evidencia** | Generar registros de evidencia precisos y oportunos alineados con el esquema EV. |
| **Almacenamiento y retención de evidencia** | Almacenar evidencia de forma segura con controles de acceso y períodos de retención apropiados. |
| **Integridad y control de acceso** | Implementar controles (hash, WORM, registros de auditoría) para preservar integridad de evidencia. |
| **Verificación legal** | Verificar reclamaciones de cumplimiento contra textos legales autoritativos y obtener asesoramiento legal según sea necesario. |
| **Alineación continua** | Actualizar evidencia y mapeos a medida que evolucionen las versiones del AIMO Standard y los marcos externos. |
| **Preparación de auditoría** | Empaquetar paquetes de evidencia y ejecutar validación antes de envío a auditores. |

## Matriz RACI

La siguiente matriz RACI clarifica responsabilidades entre roles de AIMO Standard, Adoptante y Auditor.

| Actividad | AIMO Standard | Adoptante | Auditor |
| --- | :---: | :---: | :---: |
| **Definir esquema y plantillas de evidencia** | R/A | I | I |
| **Crear registros de evidencia** | — | R/A | I |
| **Almacenar y retener evidencia** | — | R/A | I |
| **Implementar controles de acceso** | — | R/A | I |
| **Implementar controles de integridad (hash, WORM)** | — | R/A | I |
| **Ejecutar validador en paquete** | C | R/A | C |
| **Empaquetar envío (zip, checksums)** | C | R/A | I |
| **Verificar checksums (sha256)** | — | C | R/A |
| **Verificar estructura del paquete (validador)** | — | C | R/A |
| **Interpretar requisitos regulatorios** | — | R/A | C |
| **Emitir conclusión de auditoría** | — | — | R/A |
| **Proporcionar asesoramiento legal** | — | — | — |

**Leyenda**: R = Responsable, A = Accountable, C = Consultado, I = Informado, — = No aplica

!!! note "Conclusión clave"
    AIMO Standard es responsable de **definir el formato**. Los adoptantes son responsables de **crear, almacenar y validar evidencia**. Los auditores son responsables de **verificar envíos y emitir conclusiones de auditoría**.

!!! warning "Aviso de no-certificación"
    AIMO Standard es informativo; no certifica cumplimiento ni proporciona asesoramiento legal. Las conclusiones de auditoría y evaluaciones de conformidad son responsabilidad exclusiva de auditores calificados y profesionales legales.

## Declaración de no sobre-reclamación

!!! warning "Importante"
    El AIMO Standard soporta **explicabilidad y preparación de evidencia**. **No** proporciona asesoramiento legal, garantiza cumplimiento ni certifica conformidad con ninguna regulación o marco. Los adoptantes deben verificar reclamaciones contra textos autoritativos y obtener asesoramiento profesional según sea apropiado.

Esta declaración aplica a toda la documentación del AIMO Standard, incluyendo Paquete de Confianza, Paquete de Evidencia, Requisitos Mínimos de Evidencia, Mapa de Cobertura y Versiones.

## Páginas relacionadas

- [Paquete de Confianza](trust-package.md) — centro de materiales listos para auditores
- [Protocolo de Supervisión Humana](human-oversight-protocol.md) — límite de revisión máquina vs. humano
- [Requisitos Mínimos de Evidencia](../artifacts/minimum-evidence.md) — lista de verificación de ciclo de vida de nivel DEBE
- [Metodología del Mapa de Cobertura](../coverage-map/methodology.md) — qué es y qué no es el mapeo
