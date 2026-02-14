---
description: Taxonomía AIMO - Sistema de clasificación de 8 dimensiones con 91 códigos para categorizar sistemas de IA. Cubre alcance funcional, casos de uso, tipos de datos, canales, integración, riesgos, resultados y evidencia.
---

# Taxonomía

La Taxonomía AIMO proporciona un sistema de clasificación estructurado para categorizar sistemas de IA, sus usos y requisitos de gobernanza asociados. Consiste en **8 dimensiones** con **91 códigos** que permiten clasificación consistente y gestión de evidencia en las organizaciones.

## Propósito

La taxonomía sirve tres propósitos principales desde una perspectiva de auditoría:

1. **Explicabilidad**: Proporciona un vocabulario común para describir casos de uso de IA en la organización, soportando comunicación clara con auditores y stakeholders.

2. **Preparación de Evidencia**: Permite documentación sistemática de sistemas de IA usando una clasificación estandarizada, haciendo la recopilación y revisión de evidencia más eficiente.

3. **Comparabilidad**: Permite a las organizaciones comparar casos de uso de IA en diferentes contextos usando terminología consistente.

## Qué No Es (No Sobre-Reclamar)

!!! warning "Importante"
    El AIMO Standard soporta **explicabilidad y preparación de evidencia**. **No** proporciona asesoramiento legal, garantiza cumplimiento ni certifica conformidad con ninguna regulación o marco. Consulte [Límite de Responsabilidad](../../governance/responsibility-boundary.md) para detalles.

La taxonomía es solo un sistema de clasificación. No:

- Garantiza cumplimiento con ninguna ley o regulación
- Reemplaza asesoramiento profesional legal, de seguridad o de cumplimiento
- Certifica conformidad con marcos externos (ISO, NIST, EU AI Act, etc.)
- Proporciona evaluaciones de riesgo o recomendaciones de control

## Ejemplos de riesgos específicos de IA/agéntica (por qué se necesita un estándar específico de IA)

Los controles de seguridad tradicionales (ej., ISMS) solos a menudo fallan en capturar modos de fallo específicos de LLM/agente y desviaciones de agentes autónomos (ej., ejecución no intencional de herramientas, bucles recursivos) de una manera **explicable para auditoría**.
La Taxonomía AIMO proporciona un lenguaje compartido para clasificar estos riesgos específicos de IA y conectarlos con requisitos de evidencia y flujos de trabajo de remediación.

!!! warning "Solo ejemplos de referencia — no son códigos normativos"
    Los códigos siguientes son **marcadores de posición ilustrativos** y **no** forman parte del sistema de códigos normativo AIMO. No los use en envíos; use las dimensiones y códigos normativos en [Codes](./04-codes.md) y [Dictionary](./05-dictionary.md).

- **AG-01** Bucle Desbocado / Recursión
- **AG-02** Uso No Autorizado de Herramientas (mal uso estilo deputy confundido)
- **AG-03** Deriva de Límite de Privilegios

No use AG-* en envíos; use las dimensiones y códigos normativos definidos en Codes/Dictionary.

## Descripción General de Dimensiones

AIMO usa 8 dimensiones para clasificar casos de uso de IA. Cada dimensión tiene un prefijo único de 2 letras.

| ID | Nombre | Conteo de Códigos | Descripción |
| --- | --- | --- | --- |
| **FS** | Alcance Funcional | 6 | Qué función de negocio es soportada |
| **UC** | Clase de Caso de Uso | 30 | Qué tipo de tarea se realiza |
| **DT** | Tipo de Datos | 10 | Qué clasificaciones de datos están involucradas |
| **CH** | Canal | 8 | Cómo acceden los usuarios a la IA |
| **IM** | Modo de Integración | 7 | Cómo se conecta la IA a sistemas empresariales |
| **RS** | Superficie de Riesgo | 8 | Qué riesgos están asociados |
| **OB** | Resultado / Beneficio | 7 | Qué beneficios se esperan |
| **LG** | Tipo de Log/Registro | 15 | Qué log/registro se requiere |

**Total: 91 códigos en 8 dimensiones**（**EV-** reservado para ID de artefactos Evidence; dimensión log/registro de taxonomía: **LG-**.)

### Reglas de Uso

| Dimensión | Selección | Implicación de Auditoría |
| --- | --- | --- |
| FS, IM | Exactamente 1 | Clasificación primaria para asignación de responsabilidad |
| UC, DT, CH, RS, LG | 1 o más | Enumeración completa requerida para cobertura de riesgo |
| OB | 0 o más | Opcional; documenta valor de negocio esperado |

## Definiciones de Dimensiones

### FS: Alcance Funcional

Categoriza el uso de IA por la función de negocio que soporta. **Seleccione exactamente uno.**

| Código | Etiqueta | Definición |
| --- | --- | --- |
| FS-001 | Productividad de Usuario Final | IA usada para mejorar productividad de usuarios finales internos (escritura, búsqueda, resumen, notas de reuniones). |
| FS-002 | Características de Cara al Cliente | IA integrada en características de producto/servicio proporcionadas a clientes. |
| FS-003 | Herramientas de Desarrollador | IA usada para asistir desarrollo de software y tareas de ingeniería. |
| FS-004 | Operaciones de TI | IA usada para operaciones de TI y administración de sistemas (monitoreo, manejo de incidentes). |
| FS-005 | Operaciones de Seguridad | IA usada para monitoreo/respuesta de seguridad (SOC, detección, triaje). |
| FS-006 | Gobernanza y Cumplimiento | IA usada para soportar actividades de gobernanza/cumplimiento (política, evidencia de auditoría). |

### UC: Clase de Caso de Uso

Categoriza el uso de IA por el tipo de tarea o interacción. **Seleccione uno o más.** La lista completa incluye 30 códigos; ejemplos representativos a continuación.

| Código | Etiqueta | Definición |
| --- | --- | --- |
| UC-001 | Q&A General | Respuesta a preguntas generales y uso conversacional. |
| UC-002 | Resumen | Resumir documentos, reuniones o mensajes. |
| UC-003 | Traducción | Traducción entre idiomas. |
| UC-004 | Redacción de Contenido | Generar borradores para correos, documentos o reportes. |
| UC-005 | Generación de Código | Generar código o scripts. |
| UC-006 | Revisión de Código | Revisar código para problemas y mejoras. |
| UC-009 | Búsqueda/RAG | Recuperación basada en RAG y respuesta a preguntas. |
| UC-010 | Automatización Agéntica | Agentes autónomos o semi-autónomos ejecutando acciones. |

Consulte [Diccionario](./05-dictionary.md) para la lista completa de 30 códigos UC.

### DT: Tipo de Datos

Categoriza la sensibilidad y clasificación de datos involucrados. **Seleccione uno o más.**

| Código | Etiqueta | Definición |
| --- | --- | --- |
| DT-001 | Público | Datos públicamente disponibles y destinados a divulgación pública. |
| DT-002 | Interno | Datos de negocio internos no públicos. |
| DT-003 | Confidencial | Datos internos altamente sensibles que requieren acceso restringido. |
| DT-004 | Datos Personales | Datos personales según lo definido por leyes de privacidad aplicables. |
| DT-005 | Datos Personales Sensibles | Datos personales de categoría especial/sensible. |
| DT-006 | Credenciales | Secretos de autenticación y credenciales. |
| DT-007 | Código Fuente | Código fuente y artefactos relacionados. |
| DT-008 | Datos de Cliente | Datos proporcionados por clientes o relacionados con clientes. |
| DT-009 | Registros Operacionales | Registros operacionales o del sistema usados para monitoreo y resolución de problemas. |
| DT-010 | Telemetría de Seguridad | Telemetría de seguridad como alertas y detecciones. |

### CH: Canal

Categoriza cómo los usuarios acceden o interactúan con la IA. **Seleccione uno o más.**

| Código | Etiqueta | Definición |
| --- | --- | --- |
| CH-001 | UI Web | Uso vía interfaz de usuario web. |
| CH-002 | API | Uso vía integración programática de API. |
| CH-003 | Plugin de IDE | Uso vía plugin de IDE/editor. |
| CH-004 | ChatOps | Uso vía integraciones de plataformas de chat (Slack/Teams). |
| CH-005 | App de Escritorio | Uso vía aplicación nativa de escritorio. |
| CH-006 | App Móvil | Uso vía aplicación nativa móvil. |
| CH-007 | Correo Electrónico | Uso vía interfaz de correo electrónico o automatización basada en correo. |
| CH-008 | Línea de Comandos | Uso vía interfaz de línea de comandos. |

### IM: Modo de Integración

Categoriza cómo la IA está integrada en sistemas empresariales. **Seleccione exactamente uno.**

| Código | Etiqueta | Definición |
| --- | --- | --- |
| IM-001 | Independiente | Usada de forma independiente sin integración en sistemas empresariales. |
| IM-002 | SaaS Integrado | Aplicación SaaS integra características de IA. |
| IM-003 | App Empresarial Embebida | IA embebida en aplicaciones empresariales internas. |
| IM-004 | RPA/Workflow | IA invocada dentro de automatización de workflow o RPA. |
| IM-005 | On-prem / Privado | IA alojada en entorno privado/on-prem. |
| IM-006 | Servicio Gestionado | Uso vía servicio gestionado con controles empresariales. |
| IM-007 | Shadow / No Gestionado | Uso fuera de controles de gobernanza aprobados. |

### RS: Superficie de Riesgo

Categoriza los tipos de riesgos asociados con el uso de IA. **Seleccione uno o más.**

| Código | Etiqueta | Definición |
| --- | --- | --- |
| RS-001 | Fuga de Datos | Riesgo de divulgación no intencional de datos. |
| RS-002 | Abuso de Seguridad | Riesgo de que el sistema sea abusado para propósitos maliciosos. |
| RS-003 | Violación de Cumplimiento | Riesgo de violar leyes/regulaciones/políticas. |
| RS-004 | Infracción de PI | Riesgo de infringir derechos de autor/patente/secretos comerciales. |
| RS-005 | Mal Uso de Modelo | Riesgo de uso inapropiado de modelo o dependencia excesiva. |
| RS-006 | Sesgo/Equidad | Riesgo de resultados injustos o sesgados. |
| RS-007 | Seguridad | Riesgo de contenido dañino o recomendaciones inseguras. |
| RS-008 | Riesgo de Terceros | Riesgos de proveedores, subprocesadores y proveedores de modelos. |

### OB: Resultado / Beneficio

Categoriza los resultados o beneficios esperados del uso de IA. **Opcional; seleccione cero o más.**

| Código | Etiqueta | Definición |
| --- | --- | --- |
| OB-001 | Eficiencia | Mejora eficiencia de tiempo/costo. |
| OB-002 | Calidad | Mejora calidad/precisión de salidas. |
| OB-003 | Ingresos | Contribuye al crecimiento de ingresos. |
| OB-004 | Reducción de Riesgo | Reduce riesgo operacional/de seguridad/de cumplimiento. |
| OB-005 | Innovación | Habilita nuevas capacidades o innovaciones. |
| OB-006 | Satisfacción del Cliente | Mejora satisfacción del cliente. |
| OB-007 | Experiencia del Empleado | Mejora experiencia del empleado. |

### LG: Tipo de Log/Registro

Categoriza los tipos de log/registro requeridos o recopilados. **Seleccione uno o más.**（EV- reservado para ID de artefactos Evidence.)

| Código | Etiqueta | Definición |
| --- | --- | --- |
| LG-001 | Registro de Solicitud | Evidencia de que un uso/servicio de IA fue solicitado y descrito. |
| LG-002 | Registro de Revisión/Aprobación | Evidencia de que una revisión/aprobación fue realizada. |
| LG-003 | Registro de Excepción | Evidencia de que una excepción fue otorgada y rastreada. |
| LG-004 | Registro de Renovación/Reevaluación | Evidencia de que renovación o reevaluación ocurrió. |
| LG-005 | Entrada de Registro de Cambios | Evidencia de cambios y sus aprobaciones. |
| LG-006 | Prueba de Integridad | Evidencia de integridad (hash, firma, WORM). |
| LG-007 | Registro de Acceso | Evidencia de control de acceso e historial de acceso. |
| LG-008 | Inventario de Modelo/Servicio | Registro de inventario de modelos/servicios usados. |
| LG-009 | Evaluación de Riesgos | Evaluación de riesgos documentada para el uso/servicio. |
| LG-010 | Mapeo de Controles | Evidencia de mapeo de controles a marcos externos. |
| LG-011 | Capacitación/Guía | Evidencia de capacitación o guía proporcionada a usuarios. |
| LG-012 | Evidencia de Monitoreo | Evidencia de monitoreo y supervisión continua. |
| LG-013 | Registro de Incidente | Evidencia de manejo de incidentes relacionados con uso de IA. |
| LG-014 | Evaluación de Terceros | Evidencia de evaluación de proveedor o tercero. |
| LG-015 | Atestación/Firma | Registro de atestación o firma formal. |

## Cómo Usar

### Relación con Evidencia

Cada documento de evidencia referencia códigos de múltiples dimensiones para clasificar el sistema o caso de uso de IA que se documenta. La clasificación de 8 dimensiones permite:

- **Categorización consistente** en la organización
- **Filtrado basado en riesgo** por valores de dimensión
- **Mapeo de marcos** vía Mapa de Cobertura

### Referenciando el Diccionario

Para definiciones completas de códigos incluyendo notas de alcance y ejemplos, consulte el [Diccionario](./05-dictionary.md).

### Ejemplo de Clasificación

```
FS: FS-001 (Productividad de Usuario Final)
UC: UC-001 (Q&A General), UC-002 (Resumen)
DT: DT-002 (Interno), DT-004 (Datos Personales)
CH: CH-001 (UI Web)
IM: IM-002 (SaaS Integrado)
RS: RS-001 (Fuga de Datos), RS-003 (Violación de Cumplimiento)
OB: OB-001 (Eficiencia)
LG: LG-001 (Registro de Solicitud), LG-002 (Registro de Revisión/Aprobación)
```

## Referencia SSOT

!!! info "Fuente de Verdad"
    La definición autoritativa es `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv`. Esta página es explicativa. Consulte [Guía de Localización](../../contributing/localization.md) para flujos de trabajo de actualización.

## Páginas Relacionadas

- [Códigos](./04-codes.md) - Formato de código, convenciones de nomenclatura y ciclo de vida
- [Diccionario](./05-dictionary.md) - Listados completos de códigos y definiciones de columnas
- [Plantillas de Evidencia](./06-ev-template.md) - Cómo usar códigos en evidencia
- [Límite de Responsabilidad](../../governance/responsibility-boundary.md) - Declaración de no sobre-reclamación
