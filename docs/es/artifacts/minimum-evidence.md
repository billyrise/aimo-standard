---
description: Requisitos mínimos de evidencia AIMO. Lista de comprobación MUST por ciclo de vida (solicitud, revisión, aprobación, cambio, renovación) para la preparación de evidencia en gobernanza de IA.
---
<!-- aimo:translation_status=translated -->

# Requisitos mínimos de evidencia (Minimum Evidence Requirements)

Esta página es la lista de comprobación de **Requisitos mínimos de evidencia** para auditores e implementadores. Define los requisitos mínimos como lista MUST por ciclo de vida. Apoya la explicabilidad y la preparación de evidencia; no constituye asesoramiento legal ni garantiza cumplimiento.

Use esta página junto con [Paquete de Evidencia](../evidence-bundle/) y el [Validador](../../standard/current/07-validator/) al preparar o revisar envíos.

## 1) Solicitud (Request)

- **Campos MUST**: identificador, marca(s) de tiempo, actor/rol, alcance (qué se solicita), justificación (rationale).
- **Enlaces MUST**: el id de solicitud es referenciado por la revisión y por los elementos EV que registran el uso.
- **Qué demuestra**: que el uso fue solicitado y delimitado antes de la aprobación y el uso.

## 2) Revisión / Aprobación (Review / Approval)

- **Campos MUST**: identificador, marca(s) de tiempo, actor/rol, decisión (aprobado/rechazado/condicional), alcance, justificación, referencia a la solicitud.
- **Enlaces MUST**: el id de revisión es referenciado por EV y por cualquier excepción o renovación posterior.
- **Qué demuestra**: que ocurrió una revisión y aprobación definidas antes del uso (o excepción).

## 3) Excepción (Exception)

- **Campos MUST**: identificador, marca(s) de tiempo, alcance, vencimiento (o plazo), controles compensatorios, justificación, referencia a revisión/solicitud.
- **Enlaces MUST**: excepción → controles compensatorios; excepción → vencimiento; excepción → renovación (cuando corresponde reevaluación).
- **Qué demuestra**: que las desviaciones tienen plazo, tienen controles compensatorios y están vinculadas a la renovación.

## 4) Renovación / Reevaluación (Renewal / Re-evaluation)

- **Campos MUST**: identificador, marca(s) de tiempo, actor/rol, decisión (renovado/revocado/condicional), referencias a excepción/solicitud/revisión/EV previos.
- **Enlaces MUST**: la renovación referencia la excepción o aprobación que se renueva; los elementos EV pueden referenciar el id de renovación.
- **Qué demuestra**: que las excepciones y aprobaciones se reevalúan y renuevan o revocan con una base definida.

## 5) Registro de cambios (Change Log)

- **Campos MUST**: identificador, marca de tiempo, actor/rol, descripción del cambio, referencias (p. ej. a EV, solicitud, revisión, excepción, renovación afectados).
- **Enlaces MUST**: las entradas del registro de cambios referencian los artefactos que modifican o que desencadenan el cambio.
- **Qué demuestra**: que los cambios al paquete o su contenido quedan registrados y son trazables.

## 6) Integridad y acceso (Integrity & Access)

La integridad de la evidencia y el control de acceso son esenciales para la confianza en la auditoría. AIMO no prescribe controles técnicos concretos; los adoptantes deben documentar cómo se cumplen estas expectativas.

### Guía de control de acceso

| Aspecto | Guía |
| --- | --- |
| **Acceso por roles** | Definir roles (p. ej. creador de evidencia, revisor, auditor, admin) y documentar quién puede crear, leer, actualizar o eliminar evidencia. |
| **Mínimo privilegio** | Conceder el acceso mínimo necesario; restringir la escritura al personal autorizado. |
| **Registro de acceso** | Registrar eventos de acceso (quién, cuándo, qué) para la trazabilidad de auditoría. |
| **Separación de funciones** | Cuando sea práctico, separar la creación de evidencia de los roles de aprobación. |

### Guía de retención

| Aspecto | Guía |
| --- | --- |
| **Período de retención** | Definir y documentar períodos según requisitos regulatorios y política organizacional (p. ej. 5–7 años para auditorías financieras). |
| **Calendario de retención** | Mantener un calendario que indique qué evidencia se retiene, por cuánto tiempo y cuándo puede eliminarse. |
| **Retención legal** | Soportar procesos de retención legal que suspenden la retención/eliminación normal en litigios o investigaciones. |

### Opciones de inmutabilidad

| Opción | Descripción |
| --- | --- |
| **Hash criptográfico** | Generar hashes SHA-256 (o superiores) para archivos de evidencia; almacenar hashes por separado para verificación. |
| **Almacenamiento WORM** | Usar almacenamiento de una sola escritura y muchas lecturas (WORM) para archivos de evidencia y evitar modificación. |
| **Registros solo anexos** | Usar registros de auditoría solo anexos para el seguimiento de cambios. |
| **Firmas digitales** | Firmar paquetes de evidencia para probar autoría y detectar alteraciones. |

### Expectativas de trazabilidad de auditoría

| Elemento | Qué documentar |
| --- | --- |
| **Registro de cambios** | Registrar quién cambió qué, cuándo y por qué (véase el grupo de ciclo de vida Change Log). |
| **Registro de acceso** | Registrar quién accedió a la evidencia, cuándo y con qué propósito. |
| **Registros del sistema** | Retener registros del sistema relevantes (autenticación, autorización) que respalden las afirmaciones de integridad. |
| **Registros de verificación** | Documentar la verificación periódica de integridad (comprobación de hashes, revisiones de auditoría). |

### Qué demuestra

- **La evidencia se preserva**: los mecanismos de integridad (hash, WORM, firmas) demuestran que la evidencia no ha sido alterada.
- **El acceso está controlado**: los registros de acceso y las definiciones de roles muestran quién tuvo acceso y que se aplicó el mínimo privilegio.
- **Se respalda la confianza en la auditoría**: en conjunto, estos elementos dan a los auditores confianza en la fiabilidad de la evidencia.

### Perfiles operativos recomendados

Elija un perfil según su tolerancia al riesgo y requisitos regulatorios. Son recomendaciones, no mandatos.

| Aspecto | Ligero | Estándar | Estricto |
| --- | --- | --- | --- |
| **Caso de uso** | Pilotos internos, IA de bajo riesgo | Sistemas en producción, riesgo moderado | Industrias reguladas, IA de alto riesgo |
| **Período de retención** | 1–2 años | 5–7 años | 7–10+ años o mínimo regulatorio |
| **Inmutabilidad** | Hashes SHA-256 | SHA-256 + registros solo anexos | Almacenamiento WORM + firmas digitales |
| **Control de acceso** | Por roles (básico) | Por roles + registro de acceso | Separación de funciones + trazabilidad completa |
| **Trazabilidad de auditoría** | Solo registro de cambios | Registro de cambios + registro de acceso | Registros del sistema completos + verificación periódica |
| **Frecuencia de verificación** | Bajo demanda | Trimestral | Mensual o continua |
| **Uso del Validador** | Opcional | Requerido antes del envío | Requerido + comprobaciones CI automatizadas |

!!! note "Los períodos de retención son ejemplos"
    Los períodos mostrados son ilustrativos. Las organizaciones deben determinar la retención según leyes aplicables, contratos, requisitos del sector y políticas internas.

!!! tip "Cómo elegir"
    - **Ligero**: Adecuado para experimentación, herramientas internas o aplicaciones de bajo impacto donde es poco probable una auditoría formal.
    - **Estándar**: Recomendado para la mayoría de despliegues en producción donde puede haber auditorías pero no continuas.
    - **Estricto**: Requerido para industrias reguladas (finanzas, salud, gobierno) o sistemas de IA con impacto de riesgo significativo.

## Nota importante

Este conjunto mínimo apoya la explicabilidad y la preparación de evidencia; no constituye por sí mismo asesoramiento legal ni garantiza cumplimiento.

Véase [Paquete de Evidencia](../evidence-bundle/) para estructura y TOC del paquete; [Plantilla EV](../../standard/current/06-ev-template/) y esquemas para alineación a nivel de campo.

Véase también: [Esquemas de registro](../log-schemas/) — formatos de registro normalizados para evidencia de descubrimiento Shadow AI y actividad de agentes.

## Superposiciones regulatorias (informativo)

Las siguientes **superposiciones** describen evidencia adicional a menudo esperada en contextos regulatorios o de contratación concretos. Son **informativas**; adjunte plantillas/listas de comprobación oficiales tal cual en la [sección External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) de la Plantilla EV y referéncielas por logical_id en el manifiesto.

| Superposición | Artefactos adicionales típicamente esperados | Dónde adjuntar | Perfil (opcional) |
| --- | --- | --- | --- |
| **EU alto riesgo** | Gestión de riesgos, documentación técnica (Anexo IV), registro, supervisión humana, transparencia (Art 50), notificación de incidentes | payload_index; Paquete de Evidencia + perfil Annex IV | `eu_ai_act_annex_iv.json`, `eu_ai_act_high_risk.json` |
| **EU GPAI CoP** | Model Documentation Form (transparencia, derechos de autor, seguridad) | External Forms; logical_id p. ej. GPAI_MODEL_DOC_FORM | `eu_gp_ai_cop.json` |
| **NIST GenAI** | Artefactos del perfil GenAI (adaptación de modelo, evaluación, supervisión) | payload_index; change_log; External Forms / registros GenAI | `nist_ai_600_1_genai.json` |
| **UK ATRS / contratación** | Registro de transparencia ATRS; responsable de rendición de cuentas; notas de evaluación de contratación | External Forms; Summary, review | `uk_atrs_procurement.json` |
| **JP contratación** | Lista de comprobación de contratación pública GenAI; lista de directrices AI Business Guidelines | External Forms; logical_id p. ej. JP_PROCUREMENT_CHECKLIST | `jp_gov_genai_procurement.json` |

Los nombres de archivo de perfil siguen el patrón `coverage_map/profiles/<target>_<purpose>.json`; cada uno incluye `target_version`. Véase [Coverage Map — Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/) para UK y Japón; [EU AI Act](../../coverage-map/eu-ai-act/) y [NIST AI RMF](../../coverage-map/nist-ai-rmf/) para EU y NIST.
