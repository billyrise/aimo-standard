---
description: Requisitos mínimos de evidencia AIMO. Lista de verificación de nivel DEBE por ciclo de vida (solicitud, revisión, aprobación, cambio, renovación) para preparación de evidencia de gobernanza de IA.
---

# Requisitos Mínimos de Evidencia

Esta página define los requisitos mínimos de evidencia como una lista de verificación de nivel DEBE, agrupados por ciclo de vida. Respalda la explicabilidad y preparación de evidencia; no proporciona asesoramiento legal ni garantiza cumplimiento.

## 1) Solicitud

- **Campos DEBE**: identificador, marca(s) de tiempo, actor/rol, alcance (qué se solicita), justificación (por qué).
- **Vinculaciones DEBE**: id de solicitud referenciado por revisión y por elementos EV que registran el uso.
- **Qué demuestra**: que el uso fue solicitado y delimitado antes de la aprobación y uso.

## 2) Revisión / Aprobación

- **Campos DEBE**: identificador, marca(s) de tiempo, actor/rol, decisión (aprobado/rechazado/condicional), alcance, justificación, referencia a solicitud.
- **Vinculaciones DEBE**: id de revisión referenciado por EV y por cualquier excepción o renovación que siga.
- **Qué demuestra**: que ocurrió una revisión y aprobación definida antes del uso (o excepción).

## 3) Excepción

- **Campos DEBE**: identificador, marca(s) de tiempo, alcance, vencimiento (o fecha límite), controles compensatorios, justificación, referencia a revisión/solicitud.
- **Vinculaciones DEBE**: excepción → controles compensatorios; excepción → vencimiento; excepción → renovación (cuando la reevaluación sea necesaria).
- **Qué demuestra**: que las desviaciones tienen límite de tiempo, tienen controles compensatorios y están vinculadas a renovación.

## 4) Renovación / Reevaluación

- **Campos DEBE**: identificador, marca(s) de tiempo, actor/rol, decisión (renovado/revocado/condicional), referencias a excepción/solicitud/revisión/EV anterior.
- **Vinculaciones DEBE**: renovación referencia la excepción o aprobación que se renueva; elementos EV pueden referenciar id de renovación.
- **Qué demuestra**: que las excepciones y aprobaciones se reevalúan y renuevan o revocan de forma definida.

## 5) Registro de Cambios

- **Campos DEBE**: identificador, marca de tiempo, actor/rol, descripción del cambio, referencias (ej. a EV, solicitud, revisión, excepción, renovación afectados).
- **Vinculaciones DEBE**: entradas del registro de cambios referencian los artefactos que modifican o que desencadenan el cambio.
- **Qué demuestra**: que los cambios al paquete o su contenido se registran y son rastreables.

## 6) Integridad y Acceso

La integridad de la evidencia y el control de acceso son esenciales para la confianza de auditoría. Aunque AIMO no prescribe controles técnicos específicos, los adoptantes deben documentar cómo se cumplen estas expectativas.

### Guía de control de acceso

| Aspecto | Guía |
| --- | --- |
| **Acceso basado en roles** | Defina roles (ej., creador de evidencia, revisor, auditor, admin) y documente quién puede crear, leer, actualizar o eliminar evidencia. |
| **Mínimo privilegio** | Otorgue acceso mínimo necesario; restrinja acceso de escritura a personal autorizado. |
| **Registro de acceso** | Registre eventos de acceso (quién, cuándo, qué) para propósitos de pista de auditoría. |
| **Separación de funciones** | Donde sea práctico, separe la creación de evidencia de los roles de aprobación. |

### Guía de retención

| Aspecto | Guía |
| --- | --- |
| **Período de retención** | Defina y documente períodos de retención basados en requisitos regulatorios y política organizacional (ej., 5-7 años para auditorías financieras). |
| **Calendario de retención** | Mantenga un calendario que muestre qué evidencia se retiene, por cuánto tiempo y cuándo puede eliminarse. |
| **Retención legal** | Soporte procesos de retención legal que suspendan la retención/eliminación normal para litigios o investigaciones. |

### Opciones de inmutabilidad

| Opción | Descripción |
| --- | --- |
| **Hash criptográfico** | Genere hashes SHA-256 (o más fuertes) para archivos de evidencia; almacene hashes por separado para verificación. |
| **Almacenamiento WORM** | Use almacenamiento Write-Once-Read-Many para archivos de evidencia para prevenir modificaciones. |
| **Registros solo-anexar** | Use registros de auditoría solo-anexar para seguimiento de cambios. |
| **Firmas digitales** | Firme paquetes de evidencia para probar autoría y detectar manipulación. |

### Expectativas de pista de auditoría

| Elemento | Qué documentar |
| --- | --- |
| **Registro de cambios** | Registre quién cambió qué, cuándo y por qué (ver grupo de ciclo de vida de Registro de Cambios). |
| **Registro de acceso** | Registre quién accedió a la evidencia, cuándo y con qué propósito. |
| **Registros del sistema** | Retenga registros del sistema relevantes (autenticación, autorización) que respalden las afirmaciones de integridad de evidencia. |
| **Registros de verificación** | Documente verificación periódica de integridad (verificaciones de hash, revisiones de auditoría). |

### Qué demuestra

- **La evidencia se preserva**: mecanismos de integridad (hash, WORM, firmas) demuestran que la evidencia no ha sido manipulada.
- **El acceso está controlado**: registros de acceso y definiciones de roles muestran quién tuvo acceso y que se aplicó el mínimo privilegio.
- **La confianza de auditoría está respaldada**: juntos, estos elementos dan a los auditores confianza en la fiabilidad de la evidencia.

### Perfiles operacionales recomendados

Elija un perfil basado en su tolerancia al riesgo y requisitos regulatorios. Estas son recomendaciones, no mandatos.

| Aspecto | Ligero | Estándar | Estricto |
| --- | --- | --- | --- |
| **Caso de uso** | Pilotos internos, IA de bajo riesgo | Sistemas de producción, riesgo moderado | Industrias reguladas, IA de alto riesgo |
| **Período de retención** | 1-2 años | 5-7 años | 7-10+ años o mínimo regulatorio |
| **Inmutabilidad** | Hashes SHA-256 | SHA-256 + registros solo-anexar | Almacenamiento WORM + firmas digitales |
| **Control de acceso** | Basado en roles (básico) | Basado en roles + registro de acceso | Separación de funciones + pista de auditoría completa |
| **Pista de auditoría** | Solo registro de cambios | Registro de cambios + registro de acceso | Registros completos del sistema + verificación periódica |
| **Frecuencia de verificación** | Bajo demanda | Trimestral | Mensual o continua |
| **Uso del validador** | Opcional | Requerido antes de envío | Requerido + verificaciones CI automatizadas |

!!! note "Los períodos de retención son ejemplos"
    Los períodos de retención mostrados son ilustrativos. Las organizaciones deben determinar la retención basada en leyes aplicables, contratos, requisitos de la industria y políticas internas.

!!! tip "Cómo elegir"
    - **Ligero**: Adecuado para experimentación, herramientas internas o aplicaciones de bajo riesgo donde las auditorías formales son poco probables.
    - **Estándar**: Recomendado para la mayoría de implementaciones de producción donde las auditorías pueden ocurrir pero no son continuas.
    - **Estricto**: Requerido para industrias reguladas (finanzas, salud, gobierno) o sistemas de IA con impacto de riesgo significativo.

## Nota importante

Este conjunto mínimo respalda la explicabilidad y preparación de evidencia; no proporciona en sí mismo asesoramiento legal ni garantiza cumplimiento.

Consulte [Paquete de Evidencia](evidence-bundle.md) para estructura del paquete y TOC; consulte [Plantilla EV](../standard/current/06-ev-template.md) y esquemas para alineación a nivel de campo.

Consulte también: [Esquemas de Registro](log-schemas/index.md) — formatos de registro normalizados para evidencia de descubrimiento de Shadow AI y actividad de agentes.
