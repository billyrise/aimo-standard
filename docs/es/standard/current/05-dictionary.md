---
description: Diccionario AIMO - Lista autoritativa de 91 códigos de taxonomía en 8 dimensiones. Definiciones completas, etiquetas e información de ciclo de vida para clasificación de IA.
---

# Diccionario

El Diccionario AIMO es la lista autoritativa de todos los códigos válidos dentro de la taxonomía. Proporciona definiciones completas para cada código incluyendo etiquetas, descripciones e información de ciclo de vida.

## Qué es el Diccionario

El diccionario proporciona un conjunto completo, legible por máquina de todos los códigos de taxonomía AIMO. Contiene:

- Los 91 códigos en 8 dimensiones
- Etiquetas y definiciones (con traducciones en paquetes de idioma)
- Metadatos de ciclo de vida (estado, versión introducida, deprecada, eliminada)
- Notas de alcance y ejemplos para uso de código

El diccionario permite:

1. **Plantillas de Evidencia**: Los códigos se usan en plantillas EV para clasificar sistemas de IA
2. **Validador**: El validador verifica que todos los códigos existan en el diccionario
3. **Mapa de Cobertura**: Los códigos permiten mapeo a marcos y regulaciones externos

!!! info "Single Source of Truth (SSOT)"
    El SSOT para el diccionario es:

    - **Estructura**: `data/taxonomy/canonical.yaml` (códigos, estado, ciclo de vida)
    - **Traducciones**: `data/taxonomy/i18n/*.yaml` (etiquetas, definiciones por idioma)

    Los archivos CSV son **artefactos generados** para distribución. Consulte [Versiones](../../../releases/) para descargas.

## Esquema de Columnas

El diccionario canónico usa **18 columnas** (estructura neutral al idioma):

### Columnas de Identificación (5)

| # | Columna | Requerido | Descripción | Ejemplo |
| --- | --- | --- | --- | --- |
| 1 | `standard_id` | Sí | Identificador del estándar | `AIMO-STD` |
| 2 | `standard_version` | Sí | Formato SemVer | `0.1.0` |
| 3 | `dimension_id` | Sí | ID de dimensión de dos letras | `FS`, `UC`, `DT` |
| 4 | `dimension_name` | Sí | Nombre de dimensión | `Functional Scope` |
| 5 | `code` | Sí | Código completo | `UC-001` |

### Columnas de Etiqueta y Definición (4)

| # | Columna | Requerido | Descripción | Ejemplo |
| --- | --- | --- | --- | --- |
| 6 | `label` | Sí | Etiqueta del código (máx 50 caracteres) | `General Q&A` |
| 7 | `definition` | Sí | Definición del código (1-2 oraciones) | `General question answering...` |
| 8 | `scope_notes` | No | Clarificación de alcance de uso | `Low to medium risk...` |
| 9 | `examples` | No | Ejemplos separados por pipe | `chatbot\|recommendation` |

!!! note "Traducciones"
    El modelo de datos canónico separa traducciones en paquetes de idioma (`data/taxonomy/i18n/*.yaml`). Cada paquete de idioma proporciona valores localizados de `dimension_name`, `label` y `definition`. Consulte [Guía de Localización](../../contributing/localization.md) para detalles.

### Columnas de Ciclo de Vida (6)

| # | Columna | Requerido | Descripción | Ejemplo |
| --- | --- | --- | --- | --- |
| 10 | `status` | Sí | `active`, `deprecated`, `removed` | `active` |
| 11 | `introduced_in` | Sí | Versión cuando se agregó | `0.1.0` |
| 12 | `deprecated_in` | No | Versión cuando se deprecó | `1.2.0` |
| 13 | `removed_in` | No | Versión cuando se eliminó | `2.0.0` |
| 14 | `replaced_by` | No | Código de reemplazo | `UC-015` |
| 15 | `backward_compatible` | Sí | `true` o `false` | `true` |

### Columnas de Gobernanza (3)

| # | Columna | Requerido | Descripción | Ejemplo |
| --- | --- | --- | --- | --- |
| 16 | `references` | No | Referencias externas | ISO/IEC 42001 |
| 17 | `owner` | No | Parte responsable | `AIMO WG` |
| 18 | `last_reviewed_date` | No | Última revisión (YYYY-MM-DD) | `2026-01-19` |

## Entradas Iniciales

La versión actual del diccionario es **v0.1.0** y contiene:

| Dimensión | Nombre | Códigos Activos | Deprecados | Total |
| --- | --- | --- | --- | --- |
| FS | Alcance Funcional | 6 | 0 | 6 |
| UC | Clase de Caso de Uso | 30 | 0 | 30 |
| DT | Tipo de Datos | 10 | 0 | 10 |
| CH | Canal | 8 | 0 | 8 |
| IM | Modo de Integración | 7 | 0 | 7 |
| RS | Superficie de Riesgo | 8 | 0 | 8 |
| OB | Resultado / Beneficio | 7 | 0 | 7 |
| LG | Tipo Log/Evento | 15 | 0 | 15 |
| **Total** | | **91** | **0** | **91** |

!!! note "Listados Completos de Códigos"
    La lista completa de 91 códigos está disponible en los artefactos CSV generados. Esta página de documentación proporciona definiciones de columnas y guía de uso. Para definiciones detalladas de códigos:

    - **Descargar**: Consulte [Versiones](../../../releases/) para archivos CSV por idioma
    - **CSV por idioma**: `artifacts/taxonomy/current/{lang}/taxonomy_dictionary.csv`
    - **CSV legacy EN/JA mixto**: `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` (congelado, solo para compatibilidad hacia atrás)

## Política de Actualización

### Agregar Nuevos Códigos

1. Asigne el siguiente número disponible dentro de la dimensión (ej., `UC-031` después de `UC-030`)
2. Establezca `status` a `active`
3. Establezca `introduced_in` a la versión actual
4. Establezca `backward_compatible` a `true`
5. Proporcione etiqueta y definición (agregue traducciones a paquetes de idioma)

### Modificar Códigos Existentes

| Tipo de Cambio | Permitido | Impacto en Versión |
| --- | --- | --- |
| Clarificación de definición | Sí | PATCH |
| Actualización de notas de alcance | Sí | PATCH |
| Cambio de etiqueta (significado preservado) | Sí | MINOR |
| Cambio de significado | No | Cree nuevo código en su lugar |

### Deprecar Códigos

1. Establezca `status` a `deprecated`
2. Establezca `deprecated_in` a versión actual
3. Establezca `replaced_by` al nuevo código (si aplica)
4. El código permanece funcional para compatibilidad hacia atrás
5. Documente la razón en scope_notes

### Eliminar Códigos

1. Deprece por al menos una versión MINOR primero
2. Establezca `status` a `removed`
3. Establezca `removed_in` a versión MAJOR actual
4. El código ya no es válido para nueva evidencia

### Política de Compatibilidad

| Acción | Impacto en Versión | Compatible Hacia Atrás |
| --- | --- | --- |
| Agregar nuevo código | MINOR | Sí |
| Deprecar código | MINOR | Sí |
| Clarificar definición | PATCH | Sí |
| Eliminar código | MAJOR | No |
| Cambiar significado de código | No permitido | - |

## Cómo Usar

### En Plantillas de Evidencia

Cada plantilla EV incluye una tabla de códigos de 8 dimensiones:

```markdown
## Códigos AIMO (8 Dimensiones)

| Dimensión | Código(s) | Etiqueta |
| --- | --- | --- |
| **FS** | `FS-001` | End-user Productivity |
| **UC** | `UC-001`, `UC-002` | General Q&A, Summarization |
| **DT** | `DT-002`, `DT-004` | Internal, Personal Data |
| **CH** | `CH-001` | Web UI |
| **IM** | `IM-002` | SaaS Integrated |
| **RS** | `RS-001`, `RS-003` | Data Leakage, Compliance Breach |
| **OB** | `OB-001` | Efficiency |
| **LG** | `LG-001`, `LG-002` | Request Record, Review/Approval Record |
```

### En el Validador

El validador verifica:

1. Todos los códigos referenciados en evidencia existen en el diccionario
2. El formato de código coincide con el patrón esperado (`PREFIX-###`)
3. Los códigos deprecados disparan advertencias
4. Los códigos eliminados son rechazados

### Guías de Extensión

Las organizaciones PUEDEN extender el diccionario con códigos personalizados:

**Prefijo de Extensión:**

```
X-<ORG>-<DIM>-<TOKEN>
```

Ejemplo: `X-ACME-UC-901` para el código de caso de uso personalizado de ACME Corporation.

**Reglas de Extensión:**

1. Los códigos personalizados NO DEBEN conflicir con códigos estándar
2. Los códigos personalizados DEBERÍAN documentarse en un diccionario de extensión local
3. Al intercambiar evidencia con partes externas, use solo códigos estándar

## Descargas

Consulte [Versiones](../../../releases/) para paquetes descargables que contienen el diccionario y archivos relacionados.

## Páginas Relacionadas

- [Taxonomía](./03-taxonomy.md) - Definiciones de dimensiones y tablas de códigos
- [Códigos](./04-codes.md) - Formato de código, nomenclatura y ciclo de vida
- [Plantillas de Evidencia](./06-ev-template.md) - Cómo se usan los códigos en plantillas
- [Validador](./07-validator.md) - Reglas de validación de códigos
- [Registro de Cambios](./08-changelog.md) - Historial de versiones
