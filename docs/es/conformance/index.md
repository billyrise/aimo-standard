---
description: Niveles de conformidad de AIMO Standard. Cómo las organizaciones declaran conformidad, requisitos de evidencia y qué significa cada nivel para la gobernanza de la IA.
---
<!-- aimo:translation_status=translated -->

# Conformidad

!!! warning "Importante: No es certificación, no es aseguramiento, no es declaración de conformidad legal"
    AIMO Standard define un **formato de empaquetado y validación de evidencia**. No certifica conformidad con leyes o normas.
    Las opiniones de auditoría y aseguramiento son responsabilidad de los auditores independientes y de la organización adoptante.
    **Declaración apropiada:** "Un Paquete de Evidencia se produjo según AIMO Standard v0.1.2 y fue validado estructuralmente por el Validador AIMO."
    <!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
    **Declaración inapropiada:** "Conforme a la Ley de IA de la UE", "ISO 42001 certificado", "aprobado por el gobierno".
    <!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

AIMO Standard se posiciona como **capa de aseguramiento / traspaso a auditoría / evidencia continua**: proporciona empaquetado de evidencia, validadores y trazabilidad para que adoptantes y auditores trabajen con evidencia estructurada. AIMO **no** es un certificador; las decisiones de certificación y conformidad las toman los organismos de certificación acreditados, los auditores y la organización adoptante.

Estos niveles son **niveles internos de madurez de evidencia** para empaquetado y trazabilidad. **No** son certificación, **no** son opinión de aseguramiento ni conformidad legal o regulatoria.

## Declaraciones de compatibilidad (ISO/NIST/Ley de IA de la UE)

Los siguientes **mapeos informativos** enlazan evidencia y artefactos AIMO con marcos externos. Apoyan la explicabilidad y el traspaso a auditoría; **no** confieren certificación ni garantizan conformidad. Verifique contra los textos autoritativos de cada marco.

- [Coverage Map — ISO/IEC 42001](../coverage-map/iso-42001/) — mapeo a ISO/IEC 42001 (sistema de gestión de IA)
- [Coverage Map — NIST AI RMF](../coverage-map/nist-ai-rmf/) — mapeo al Marco de Gestión de Riesgos de IA de NIST
- [Coverage Map — Ley de IA de la UE](../coverage-map/eu-ai-act/) — mapeo a temas de la Ley de IA (alto nivel; no es asesoramiento jurídico)

Las fuentes primarias y el lenguaje de declaración se documentan en cada página del Coverage Map y en [Límite de responsabilidad](../governance/responsibility-boundary/).

## No declaraciones (lo que AIMO NO declara)

- AIMO **no** certifica conformidad con ISO/IEC 42001, NIST AI RMF, Ley de IA de la UE ni ningún otro marco.
- AIMO **no** garantiza cumplimiento regulatorio ni legal.
- AIMO **no** proporciona opiniones de aseguramiento ni asesoramiento jurídico.
- AIMO **no** decide si una organización cumple requisitos externos; eso es responsabilidad de adoptantes, auditores y organismos de certificación.

AIMO **sí** proporciona: formato de evidencia estructurado, validador, mapeos de cobertura (informativos) y materiales para traspaso a auditoría. Véase [Límite de responsabilidad](../governance/responsibility-boundary/) para el alcance completo.

!!! note "Alias del nombre del nivel"
    El nivel superior se denominó informalmente "Gold" en el pasado; el **nombre oficial del nivel es Audit-Ready**.

## Marco de conformidad AIMO (AIMO-MS / AIMO-Controls / AIMO-Audit)

| Componente | Descripción | Expectativas de evidencia |
| --- | --- | --- |
| **AIMO-MS** | Estructura orientada al sistema de gestión: políticas, roles, artefactos alineados con PDCA que pueden apoyar controles tipo ISO/IEC 42001. | Request, review, exception, renewal, change log; Summary y Dictionary. |
| **AIMO-Controls** | Controles de ciclo de vida e integridad: request→review→exception→renewal, hashing, firma (según [estructura del Paquete de Evidencia](../../standard/current/09-evidence-bundle-structure/)). | Object_index, payload_index, hash_chain, signing; registros de ciclo de vida. |
| **AIMO-Audit** | Preparación para traspaso a auditoría: validador aprobado, sumas de comprobación, attestation opcional e índice de traspaso a auditoría. | Salida del validador, bundle_id, identidad del productor, metadatos de firma opcionales e índice de traspaso. |

Las expectativas de evidencia se describen en [Requisitos Mínimos de Evidencia](../artifacts/minimum-evidence/) y [Paquete de Evidencia](../artifacts/evidence-bundle/).

## Niveles de conformidad (solo AIMO)

### Nivel 1 — Foundation

**Propósito:** Línea base trazable. Conjunto mínimo para que el paquete sea identificable, verificable en integridad y comprobado por el validador.

| Elemento | Requisito |
| --- | --- |
| **Artefactos requeridos** | Estructura del [Paquete de Evidencia](../artifacts/evidence-bundle/) (manifest.json, objects/, payload_index según espec.); [Validador](../validator/) aprobado; enlace a [Requisitos Mínimos de Evidencia](../artifacts/minimum-evidence/). |
| **Preguntas típicas de auditoría** | ¿Qué está en alcance? ¿Quién produjo el paquete? ¿Se pueden verificar los hashes? |
| **Lagunas típicas** | Metadatos del manifest faltantes (bundle_id, created_at, producer); validador no ejecutado o no adjunto. |

### Nivel 2 — Operational

**Propósito:** Evidencia de control operativo. Construye sobre Foundation con rastro de ciclo de vida y supervisión.

| Elemento | Requisito |
| --- | --- |
| **Artefactos requeridos** | Todos los MUST de Foundation; rastro de control de ciclo de vida (request/aprobación, review, exception o "sin excepciones", plan de renewal); al menos un artefacto de supervisión (registro de incidentes o comprobación periódica o muestreo de supervisión humana); change log con enlace de integridad; declaración de límite prueba vs. aseguramiento. |
| **Preguntas típicas de auditoría** | ¿Quién aprobó el uso? ¿Cómo se rastrean las excepciones? ¿Cuándo fue la última revisión? |
| **Lagunas típicas** | Review/aprobación no vinculada a request; sin artefacto de supervisión; change log no referencia objetos afectados. |

### Nivel 3 — Audit-Ready

**Propósito:** Calidad de traspaso a auditoría. Attestation completa, reproducibilidad y ranura de formularios externos.

| Elemento | Requisito |
| --- | --- |
| **Artefactos requeridos** | Todos los MUST de Operational; al menos una firma digital que cubra el manifest (identidad del firmante + algoritmo); TSA o declaración "sin TSA"; paquete de reproducibilidad (comando exacto del validador, salidas esperadas, metadatos de entorno); sección Formularios externos con plantillas/listas oficiales adjuntas tal cual y referenciadas entre sí; declaración de integridad acotada; índice de traspaso a auditoría de una página (artefacto → hash → productor → fecha). |
| **Preguntas típicas de auditoría** | ¿Cómo puede un auditor volver a ejecutar la validación? ¿Dónde están las listas externas y cómo se mapean al paquete? |
| **Lagunas típicas** | Firma presente pero firmante/algoritmo no documentados; sin índice de traspaso; formularios externos no hasheados o no referenciados en el manifest. |

## Evidencia mínima por nivel (resumen)

| Nivel | MUST (resumen) |
| --- | --- |
| **Foundation** | Estructura del paquete (manifest, object_index, payload_index); sha256 para objetos referenciados; bundle_id, created_at, producer; ejecución del validador + versión; línea base del diccionario de evidencia (nombre del sistema, propietario, propósito, categorías de datos, etapa de ciclo de vida); declaración de acceso y retención (quién, duración, tipo de almacenamiento, prueba de alteración). SHOULD: entrada mínima en change log. |
| **Operational** | Todos los MUST de Foundation; rastro de ciclo de vida (request/aprobación, review, exception o "ninguna", renewal + última renewal); ≥1 artefacto de supervisión; entradas del change log referencian objetos afectados; declaración explícita de límite prueba vs. aseguramiento. |
| **Audit-Ready** | Todos los MUST de Operational; ≥1 firma sobre el manifest (identidad del firmante + algoritmo); TSA o "sin TSA"; paquete de reproducibilidad; Formularios externos listados y referenciados entre sí; declaración de integridad acotada; índice de traspaso a auditoría. |

La **presencia** de al menos una firma (que tenga como objetivo el manifest) es exigida por la [estructura del Paquete de Evidencia](../../standard/current/09-evidence-bundle-structure/) normativa para todos los paquetes. **Audit-Ready** añade una **attestation criptográfica** más estricta (identidad del firmante, algoritmo, declaración TSA, instrucciones de revalidación) para que un tercero pueda repetir las comprobaciones.

## Mapeo ISO/IEC 42001 (informativo)

La tabla siguiente muestra cómo los artefactos AIMO **apoyan la evidencia** de familias de cláusulas típicas de ISO/IEC 42001. Es solo informativa; no implica certificación ni conformidad.

| Familia de cláusulas ISO/IEC 42001 | Artefactos AIMO que apoyan la evidencia |
| --- | --- |
| Contexto de la organización | Summary, Dictionary, scope_ref |
| Liderazgo / Política | Summary, review, dictionary |
| Planificación (riesgos, objetivos) | request, review, exception, EV, Dictionary |
| Apoyo (recursos, competencia, documentación) | Summary, review, EV, change_log |
| Operación | EV, request, review, exception; controles operativos |
| Evaluación del desempeño (supervisión, auditoría interna, revisión por la dirección) | EV, change_log, review, renewal |
| Mejora | exception, renewal, change_log |

Véase [Mapa de Cobertura — ISO/IEC 42001](../coverage-map/iso-42001/) y [Kit de preparación para certificación ISO 42001](../artifacts/iso-42001-certification-readiness-toolkit/) para más detalle.

## Plantillas de redacción de declaraciones (anti-sobredeclaración)

Use solo declaraciones que describan con precisión lo realizado. La certificación y la conformidad legal siguen siendo responsabilidad de los adoptantes y los organismos acreditados.

**Aceptables (ejemplos)**

- "Somos conformes AIMO (Nivel 2) con AIMO Standard v0.1.2; esto no implica certificación ISO ni conformidad legal."
- "Utilizamos artefactos AIMO para apoyar la preparación para ISO/IEC 42001; las decisiones de certificación corresponden a los organismos de certificación acreditados."
- "Un Paquete de Evidencia se produjo según AIMO Standard v0.1.2 y fue validado estructuralmente por el Validador AIMO."

<!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
**Inaceptables (ejemplos)**

- "Conforme a la Ley de IA de la UE" (AIMO no certifica conformidad regulatoria.)
- "ISO 42001 certificado" (La certificación la emiten organismos de certificación acreditados, no AIMO.)
- "Aprobado por el gobierno" (AIMO no es un esquema de aprobación gubernamental.)
<!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

## Páginas relacionadas

- [Trust Package](../governance/trust-package/) — Punto de entrada consolidado para auditores
- [Responsibility Boundary](../governance/responsibility-boundary/) — Lo que AIMO ofrece y no ofrece
- [Standard (Current)](../standard/current/) — Requisitos normativos
- [Artifacts](../artifacts/) — Estructura de evidencia y requisitos mínimos
- [Validator](../validator/) — Validación estructural
