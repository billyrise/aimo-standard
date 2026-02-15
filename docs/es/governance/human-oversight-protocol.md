---
description: Protocolo de Supervisión Humana AIMO - Límite entre validación automatizada y revisión humana. Responsabilidades de juicio máquina vs. humano en gobernanza de IA.
---
<!-- aimo:translation_status=translated -->

# Protocolo de Supervisión Humana

Esta página define el límite entre lo que la validación automatizada (Validador) puede verificar y lo que requiere revisión humana (Human-in-the-Loop). Clarifica las responsabilidades para juicio de máquina vs. humano en procesos de evidencia de gobernanza de IA.

## Propósito

Las herramientas de validación automatizada pueden verificar eficientemente la corrección estructural y sintáctica, pero no pueden reemplazar el juicio humano para decisiones dependientes del contexto. Este protocolo:

- Clarifica qué puede y no puede verificar el Validador
- Define el alcance de la revisión humana requerida para gobernanza efectiva
- Soporta explicaciones de auditoría documentando el proceso de supervisión humana
- Proporciona un marco para organizaciones implementando flujos de trabajo de gobernanza de IA

## Qué puede hacer la validación automatizada (alcance del Validador)

El Validador AIMO y herramientas automatizadas similares pueden verificar:

| Capacidad | Descripción |
| --- | --- |
| **Completitud de campos/documentos requeridos** | Verificar que todos los campos obligatorios están presentes en manifiestos, registros EV y otros artefactos |
| **Consistencia estructural** | Validar referencias, IDs y enlaces cruzados entre artefactos (ej., request_id → review_id) |
| **Validación de esquema** | Verificar que artefactos JSON/YAML conforman a esquemas definidos |
| **Validación de formato de código** | Verificar que códigos de taxonomía coinciden con patrones esperados (ej., `UC-001`) |
| **Verificaciones de integridad** | Validar formato y presencia de hash (no recálculo contra contenido) |
| **Validación de diccionario** | Confirmar que los códigos existen en el diccionario de taxonomía |

Consulte [Validador](../../standard/current/07-validator/) para reglas de validación detalladas e implementación de referencia.

## Qué requiere revisión humana (alcance Human-in-the-Loop)

Las siguientes áreas requieren juicio humano y no pueden automatizarse:

| Capacidad | Descripción |
| --- | --- |
| **Juicio de riesgo dependiente del contexto** | Evaluar riesgos de negocio, éticos y operacionales basados en contexto organizacional |
| **Justificación de aprobación de excepciones** | Evaluar si una excepción está justificada y los controles compensatorios son adecuados |
| **Toma de decisiones de remediación** | Priorizar correcciones, asignar recursos y determinar cronogramas |
| **Compensaciones de políticas** | Balancear requisitos competidores (ej., velocidad vs. minuciosidad, costo vs. riesgo) |
| **Aceptación de riesgo residual** | Decidir si los riesgos restantes son aceptables después de controles |
| **Evaluación de impacto entre dominios** | Evaluar implicaciones para legal, RRHH, operaciones y otras funciones |
| **Verificación de precisión del contenido** | Confirmar que el contenido de evidencia es factualmente correcto y completo |
| **Comunicación con stakeholders** | Explicar decisiones a auditores, reguladores y liderazgo |

## Límite de responsabilidad

| Aspecto | Validador (Máquina) | Revisor Humano |
| --- | --- | --- |
| **Estructura** | ✓ Puede verificar | Revisar si se marca |
| **Completitud** | ✓ Puede verificar campos | Verificar adecuación del contenido |
| **Formato** | ✓ Puede verificar | — |
| **Juicio de riesgo** | ✗ No puede evaluar | ✓ Debe evaluar |
| **Aprobación de excepción** | ✗ No puede decidir | ✓ Debe decidir |
| **Prioridad de remediación** | ✗ No puede priorizar | ✓ Debe priorizar |
| **Interpretación legal** | ✗ No puede interpretar | ✓ Debe verificar con asesor |
| **Conclusión de auditoría** | ✗ No puede concluir | ✓ Responsabilidad del auditor |

!!! note "Roles complementarios"
    Validador y revisión humana son **complementarios**, no alternativas. El Validador asegura consistencia estructural antes de la revisión humana; la revisión humana asegura adecuación contextual.

## Expectativas de evidencia

Las organizaciones implementando supervisión humana deben documentar:

| Tipo de Evidencia | Descripción |
| --- | --- |
| **Registro de revisión** | Quién revisó, cuándo y qué decisión se tomó |
| **Justificación de aprobación** | Por qué se tomó la decisión (especialmente para excepciones) |
| **Registro de escalación** | Cuándo y por qué se escalaron issues a autoridad superior |
| **Plan de remediación** | Acciones planificadas, responsables y cronogramas para abordar issues |
| **Firma** | Atestación formal de que la revisión fue completada |

Estos registros deben incluirse en el Paquete de Evidencia según [Requisitos Mínimos de Evidencia](../../artifacts/minimum-evidence/).

## No sobre-reclamar

!!! warning "Importante"
    Este protocolo define un **marco para documentar supervisión humana**. **No**:

    - Proporciona asesoramiento legal ni interpretación regulatoria
    - Garantiza cumplimiento con ninguna regulación o estándar
    - Reemplaza juicio humano calificado con decisiones automatizadas
    - Prescribe procesos organizacionales específicos

    Las organizaciones deben adaptar este marco a su contexto específico, perfil de riesgo y requisitos regulatorios.

## Páginas relacionadas

- [Validador](../../standard/current/07-validator/) — reglas de validación automatizada e implementación de referencia
- [Límite de Responsabilidad](../responsibility-boundary/) — qué proporciona AIMO vs. responsabilidades del adoptante
- [Requisitos Mínimos de Evidencia](../../artifacts/minimum-evidence/) — lista de verificación de evidencia de nivel DEBE
- [Paquete de Confianza](../trust-package/) — centro de materiales listos para auditores
