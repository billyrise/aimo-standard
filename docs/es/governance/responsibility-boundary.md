---
description: Límite de responsabilidad AIMO — Define lo que ofrece la norma frente a las responsabilidades del adoptante. Declaración de no sobreafirmación y límites de alcance.
---
<!-- aimo:translation_status=translated -->

# Límite de responsabilidad（Responsibility Boundary）

Esta página define qué ofrece y qué no ofrece el AIMO Standard, las hipótesis que asume y las responsabilidades de los adoptantes.

## Límite prueba vs. aseguramiento (Proof vs assurance boundary)

| Límite | Lo que ofrece AIMO | Quién decide |
| --- | --- | --- |
| **Prueba (evidencia)** | Estructura del Evidence Bundle, validadores, esquemas, plantillas, mapeos de cobertura (informativos). AIMO produce **paquetes de evidencia** y **validadores** que comprueban la conformidad estructural. | El adoptante produce la evidencia; AIMO define el formato y las reglas. |
| **Aseguramiento / conformidad / certificación** | AIMO **no** emite certificaciones, opiniones de aseguramiento ni decisiones de conformidad. | **Externo:** el cliente, el auditor o el **organismo de certificación acreditado** decide la conformidad y la certificación. |

La conformidad y el lenguaje de declaración se unifican en [Conformidad](../../conformance/) y en el [Kit de preparación para certificación ISO 42001](../../artifacts/iso-42001-certification-readiness-toolkit/). AIMO apoya la **preparación de evidencia** y el **traspaso a auditoría**; no certifica ni garantiza conformidad.

## Qué ofrece el AIMO Standard

- **Un formato de evidencia estructurado**: esquemas, plantillas y taxonomía para evidencia de gobernanza de IA.
- **Marco de trazabilidad**: vinculación de evidencia por ciclo de vida (solicitud → revisión → excepción → renovación).
- **Soporte de explicabilidad**: mapeo de cobertura a marcos externos para discusiones de auditoría.
- **Herramientas de validación**: validador de referencia y reglas para comprobaciones de consistencia estructural.
- **Documentación**: especificación normativa, ejemplos y guía.

## Qué NO ofrece el AIMO Standard

| Fuera de alcance | Explicación |
| --- | --- |
| **Asesoramiento legal** | AIMO no interpreta leyes ni regulaciones. Consulte asesoría legal cualificada para cumplimiento normativo. |
| **Certificación de cumplimiento** | Usar AIMO no certifica cumplimiento de ninguna regulación o marco (ISO 42001, EU AI Act, NIST AI RMF, etc.). |
| **"Certificado ISO por AIMO"** | AIMO no emite certificaciones. La certificación la realizan organismos de certificación acreditados. |
| **"Cumplimiento EU AI Act por AIMO"** | AIMO estructura evidencia; no garantiza ni certifica cumplimiento normativo. |
| **Evaluación de riesgos** | AIMO estructura evidencia pero no realiza ni valida evaluaciones de riesgo de IA. |
| **Controles técnicos** | AIMO no implementa control de acceso, cifrado u otros controles de seguridad; documenta expectativas. |
| **Ejecución de auditoría** | AIMO proporciona materiales a auditores pero no realiza auditorías. |
| **Evaluación de modelos de IA** | AIMO no evalúa rendimiento, sesgo o seguridad de modelos. |

## Supuestos

El AIMO Standard asume:

1. **Los adoptantes tienen procesos de gobernanza**: existen flujos de solicitud, revisión, aprobación y excepción.
2. **Los adoptantes mantienen evidencia**: la evidencia es creada, almacenada y retenida por los sistemas del adoptante.
3. **Los adoptantes verifican frente a textos autoritativos**: al usar Coverage Map, los adoptantes comprueban el marco o regulación original.
4. **Las herramientas son opcionales**: el validador de referencia es una comodidad; los adoptantes pueden usar su propia validación.

## Responsabilidades del adoptante

| Responsabilidad | Descripción |
| --- | --- |
| **Creación de evidencia** | Generar registros de evidencia precisos y oportunos alineados con el esquema EV. |
| **Almacenamiento y retención de evidencia** | Almacenar evidencia de forma segura con controles de acceso y períodos de retención adecuados. |
| **Integridad y control de acceso** | Implementar controles (hashing, WORM, registros de auditoría) para preservar la integridad de la evidencia. |
| **Verificación legal** | Verificar afirmaciones de cumplimiento frente a textos legales autoritativos y obtener asesoría legal según convenga. |
| **Alineación continua** | Actualizar evidencia y mapeos conforme evolucionan versiones del AIMO Standard y marcos externos. |
| **Preparación de auditoría** | Empaquetar Evidence Bundles y ejecutar validación antes de entregar a auditores. |

## Matriz RACI

La siguiente matriz RACI aclara responsabilidades entre AIMO Standard, Adoptante y Auditor.

| Actividad | AIMO Standard | Adoptante | Auditor |
| --- | :---: | :---: | :---: |
| **Definir esquema y plantillas de evidencia** | R/A | I | I |
| **Crear registros de evidencia** | — | R/A | I |
| **Almacenar y retener evidencia** | — | R/A | I |
| **Implementar controles de acceso** | — | R/A | I |
| **Implementar controles de integridad (hash, WORM)** | — | R/A | I |
| **Ejecutar validador sobre el bundle** | C | R/A | C |
| **Empaquetar entrega (zip, checksums)** | C | R/A | I |
| **Verificar checksums (sha256)** | — | C | R/A |
| **Verificar estructura del bundle (validador)** | — | C | R/A |
| **Interpretar requisitos regulatorios** | — | R/A | C |
| **Emitir conclusión de auditoría** | — | — | R/A |
| **Proporcionar asesoramiento legal** | — | — | — |

**Leyenda**: R = Responsable, A = Accountable, C = Consultado, I = Informado, — = No aplicable

!!! note "Conclusión clave"
    El AIMO Standard es responsable de **definir el formato**. Los adoptantes son responsables de **crear, almacenar y validar evidencia**. Los auditores son responsables de **verificar entregas y emitir conclusiones de auditoría**.

!!! warning "Aviso de no certificación"
    El AIMO Standard es informativo; no certifica cumplimiento ni proporciona asesoramiento legal. Las conclusiones de auditoría y las evaluaciones de conformidad son responsabilidad exclusiva de auditores y profesionales legales cualificados.

## Política de afirmaciones

| Aceptable | Inaceptable |
| --- | --- |
| "Se produjo un Evidence Bundle según AIMO Standard v0.1.2 y validado estructuralmente por el AIMO Validator." | "Cumplimiento EU AI Act", "ISO 42001 certificado", "aprobación gubernamental", etc. |
| "Usamos artefactos AIMO para apoyar la preparación ISO/IEC 42001; las decisiones de certificación corresponden a organismos de certificación acreditados." | Afirmar que AIMO certifica cumplimiento o proporciona asesoramiento legal. |

## Declaración de no sobreafirmación

!!! warning "Importante"
    El AIMO Standard apoya **explicabilidad y preparación de evidencia**. **No** proporciona asesoramiento legal, **no** garantiza cumplimiento ni **no** certifica conformidad con ninguna regulación o marco. Los adoptantes deben verificar afirmaciones frente a textos autoritativos y obtener asesoría profesional según convenga.

Esta declaración se aplica a toda la documentación del AIMO Standard, incluidos Trust Package, Evidence Bundle, Minimum Evidence Requirements, Coverage Map y Releases.

## Páginas relacionadas

- [Trust Package](../trust-package/) — centro de materiales listos para auditoría
- [Human Oversight Protocol](../human-oversight-protocol/) — límite revisión máquina vs. humana
- [Minimum Evidence Requirements](../../artifacts/minimum-evidence/) — checklist MUST por ciclo de vida
- [Coverage Map Methodology](../../coverage-map/methodology/) — qué es y qué no es el mapeo
