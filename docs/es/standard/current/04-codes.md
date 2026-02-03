---
description: Formato y convenciones de nomenclatura del Sistema de Códigos AIMO. Define estructura de códigos (XX-NNN), estados de ciclo de vida, versionado y políticas de deprecación para códigos de taxonomía.
---

# Códigos

Esta página define el formato del Sistema de Códigos AIMO, convenciones de nomenclatura y gestión de ciclo de vida.

## Formato de Código

Todos los códigos AIMO siguen el formato: **`<PREFIJO>-<TOKEN>`**

| Componente | Descripción | Formato | Ejemplo |
| --- | --- | --- | --- |
| `<PREFIJO>` | Identificador de dimensión | 2 letras mayúsculas | FS, UC, DT |
| `-` | Separador | Guión | - |
| `<TOKEN>` | Token único dentro de la dimensión | 3 dígitos (con ceros a la izquierda) | 001, 002, 003 |

### Ejemplos

- `FS-001` - Alcance Funcional: Productividad de Usuario Final
- `UC-005` - Clase de Caso de Uso: Generación de Código
- `DT-004` - Tipo de Datos: Datos Personales
- `CH-003` - Canal: Plugin de IDE
- `IM-002` - Modo de Integración: SaaS Integrado
- `RS-001` - Superficie de Riesgo: Fuga de Datos
- `OB-001` - Resultado/Beneficio: Eficiencia
- `LG-001` - Tipo de Log/Registro: Registro de Solicitud

## Espacios de Nombres

La taxonomía AIMO usa 8 espacios de nombres de dimensión:

| ID | Nombre | Prefijo | Conteo de Códigos |
| --- | --- | --- | --- |
| **FS** | Alcance Funcional | `FS-` | 6 |
| **UC** | Clase de Caso de Uso | `UC-` | 30 |
| **DT** | Tipo de Datos | `DT-` | 10 |
| **CH** | Canal | `CH-` | 8 |
| **IM** | Modo de Integración | `IM-` | 7 |
| **RS** | Superficie de Riesgo | `RS-` | 8 |
| **OB** | Resultado / Beneficio | `OB-` | 7 |
| **EV** | Tipo de Evidencia | `EV-` | 15 |

**Total: 91 códigos en 8 dimensiones**

### Reglas de Espacio de Nombres

1. **El prefijo es fijo**: El prefijo de dimensión de dos letras (FS, UC, etc.) es permanente y nunca cambiará.
2. **Relleno con ceros**: Los tokens siempre son 3 dígitos, con ceros a la izquierda (ej., `001` no `1`).
3. **Asignación secuencial**: Los nuevos códigos se asignan al siguiente número disponible dentro de una dimensión.
4. **Sin reutilización**: Los códigos eliminados nunca se reasignan a diferentes significados.

## Reglas de Estabilidad

La estabilidad de códigos es un principio crítico para la trazabilidad de auditoría.

### Inmutabilidad de ID

- **Los IDs de código son inmutables** — una vez asignado, un ID de código nunca cambia de significado
- Un código como `UC-001` siempre significará "Q&A General" durante todo su ciclo de vida
- Si el significado necesita cambiar, se crea un nuevo código en su lugar

### Política de No Reutilización

- Los códigos deprecados o eliminados **nunca se reasignan** a diferentes significados
- Esto asegura que la evidencia histórica permanezca válida y rastreable
- Ejemplo: Si `UC-010` es deprecado, un nuevo caso de uso obtiene `UC-031` (no `UC-010`)

### Deprecación Antes de Eliminación

- Los códigos deben marcarse como `deprecated` por al menos una versión MINOR antes de la eliminación
- La eliminación solo ocurre en incrementos de versión MAJOR
- Consulte la sección [Ciclo de Vida](#ciclo-de-vida) para detalles

## Uso

### Dimensiones Requeridas

Para cada sistema o caso de uso de IA, DEBE especificar al menos un código de cada dimensión requerida:

| Dimensión | Selección | Notas |
| --- | --- | --- |
| FS | Exactamente 1 | Función de negocio primaria |
| UC | 1 o más | Tipos de tarea realizados |
| DT | 1 o más | Clasificaciones de datos |
| CH | 1 o más | Canales de acceso |
| IM | Exactamente 1 | Modo de integración |
| RS | 1 o más | Categorías de riesgo |
| EV | 1 o más | Tipos de evidencia |

### Dimensiones Opcionales

| Dimensión | Selección | Notas |
| --- | --- | --- |
| OB | 0 o más | Beneficios esperados (opcional) |

### Composición de Códigos

Al documentar un sistema de IA, los códigos de múltiples dimensiones se combinan. La **prioridad de composición** determina el orden al listar códigos:

1. FS (Alcance Funcional)
2. UC (Clase de Caso de Uso)
3. DT (Tipo de Datos)
4. CH (Canal)
5. IM (Modo de Integración)
6. RS (Superficie de Riesgo)
7. OB (Resultado / Beneficio)
8. EV (Tipo de Evidencia)

**Ejemplo de composición:**

```
FS: FS-001
UC: UC-001, UC-002
DT: DT-002, DT-004
CH: CH-001
IM: IM-002
RS: RS-001, RS-003
OB: OB-001
LG: LG-001, LG-002
```

## Ciclo de Vida

### Valores de Estado

| Estado | Descripción | Comportamiento del Validador |
| --- | --- | --- |
| `active` | Actualmente válido y en uso | Aceptado |
| `deprecated` | Aún válido pero programado para eliminación | Aceptado con advertencia |
| `removed` | Ya no es válido; no usar | Rechazado |

### Campos de Metadatos de Ciclo de Vida

El diccionario rastrea el ciclo de vida con estos campos:

| Campo | Requerido | Descripción | Ejemplo |
| --- | --- | --- | --- |
| `status` | Sí | Estado actual | `active` |
| `introduced_in` | Sí | Versión cuando se agregó el código | `0.1.0` |
| `deprecated_in` | No | Versión cuando se marcó como deprecado | `1.2.0` |
| `removed_in` | No | Versión cuando se eliminó | `2.0.0` |
| `replaced_by` | No | Código(s) de reemplazo | `UC-015` |
| `backward_compatible` | Sí | Si el cambio rompe uso existente | `true` |

### Reglas de Deprecación

1. Los códigos DEBEN marcarse como `deprecated` por al menos una versión MINOR antes de la eliminación
2. Los códigos deprecados incluyen versión `deprecated_in` y `replaced_by` si aplica
3. La eliminación ocurre solo en incrementos de versión MAJOR
4. Los códigos deprecados permanecen válidos para compatibilidad hacia atrás durante el período de deprecación

**Ejemplo de línea de tiempo:**

| Versión | Estado | Acción |
| --- | --- | --- |
| 0.1.0 | `active` | Código `UC-010` introducido |
| 1.2.0 | `deprecated` | Marcado deprecado, `replaced_by: UC-031` |
| 2.0.0 | `removed` | Ya no aceptado por el validador |

### Versionado

Los cambios de código siguen [Semantic Versioning](./08-changelog.md):

- **MAJOR**: Eliminación de código o cambios disruptivos
- **MINOR**: Nuevos códigos agregados, códigos deprecados
- **PATCH**: Solo clarificaciones de definición (sin cambios estructurales)

### Compatibilidad Hacia Atrás

El campo `backward_compatible` indica si un cambio rompe uso existente:

| Valor | Significado |
| --- | --- |
| `true` | La evidencia existente usando este código permanece válida |
| `false` | La evidencia existente puede necesitar actualizaciones (cambio de versión MAJOR) |

## Validación

El validador verifica:

1. Todas las dimensiones requeridas tienen al menos un código
2. Las dimensiones de selección única tienen exactamente un código
3. Todos los códigos existen en el diccionario de taxonomía actual
4. El formato de código coincide con el patrón `<PREFIJO>-<TOKEN>` (ej., `UC-001`)
5. Los códigos deprecados se marcan con advertencias

Consulte [Validador](./07-validator.md) para detalles de implementación.

## Referencia SSOT

!!! info "Fuente de Verdad"
    La definición autoritativa es `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv`. Esta página es explicativa. Consulte [Guía de Localización](../../contributing/localization.md) para flujos de trabajo de actualización.

## Páginas Relacionadas

- [Taxonomía](./03-taxonomy.md) - Definiciones completas de dimensiones
- [Diccionario](./05-dictionary.md) - Listados completos de códigos y definiciones de columnas
- [Validador](./07-validator.md) - Reglas de validación
- [Registro de Cambios](./08-changelog.md) - Historial de versiones
