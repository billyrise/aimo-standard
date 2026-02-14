---
description: Registro de cambios y política de versionado de AIMO Standard. Documenta historial de versiones, reglas de versionado semántico y guía de migración entre releases.
---

# Registro de Cambios

Esta sección documenta la política de versionado e historial de cambios para el AIMO Standard.

## Política de Versionado

AIMO Standard sigue [Semantic Versioning](https://semver.org/) (SemVer):

### Formato de Versión: MAJOR.MINOR.PATCH

| Tipo de Cambio | Bump de Versión | Ejemplos |
| --- | --- | --- |
| **MAJOR** | X.0.0 | Cambios de esquema disruptivos, eliminación de código, cambios de campos requeridos |
| **MINOR** | 0.X.0 | Nuevos códigos, nuevos campos opcionales, nuevas dimensiones (opcionales) |
| **PATCH** | 0.0.X | Correcciones de documentación, clarificaciones de definición, correcciones de bugs del validador |

### Cambios Disruptivos vs. Compatibles

**Cambios Disruptivos (MAJOR):**

- Eliminación de códigos (después del período de deprecación)
- Cambios a campos requeridos en esquemas
- Cambios estructurales que invalidan documentos existentes
- Cambios a patrones de formato de código

**Cambios Compatibles Hacia Atrás (MINOR):**

- Agregar nuevos códigos a dimensiones existentes
- Agregar nuevos campos opcionales a esquemas
- Agregar nuevas dimensiones opcionales
- Agregar nuevas plantillas de evidencia

**Cambios No-Disruptivos (PATCH):**

- Correcciones de documentación
- Clarificación de definiciones existentes
- Mejoras de traducción
- Correcciones de bugs del validador

## Política de Deprecación

### Proceso de Deprecación

1. **Marcar como Deprecado**: Código o característica se marca con `status: deprecated` y `deprecated_in: X.Y.Z`
2. **Período de Deprecación**: Al menos una versión MINOR debe pasar antes de la eliminación
3. **Proporcionar Reemplazo**: Si aplica, `replaced_by` indica el reemplazo
4. **Eliminar en MAJOR**: La eliminación ocurre en la siguiente versión MAJOR

### Ejemplo de Ciclo de Vida

```
v0.0.1: FS-007 introducido (status: active)
v0.1.0: FS-007 deprecado (status: deprecated, replaced_by: FS-008)
v0.2.0: FS-007 aún disponible con advertencia de deprecación
v1.0.0: FS-007 eliminado (status: removed)
```

### Usando Códigos Deprecados

- Los códigos deprecados permanecen válidos para validación
- El validador DEBERÍA emitir una advertencia para códigos deprecados
- Las nuevas implementaciones DEBERÍAN usar códigos de reemplazo
- Los documentos existentes PUEDEN continuar usando códigos deprecados hasta la migración

## Artefactos de Release

Cada release oficial incluye:

| Artefacto | Descripción |
| --- | --- |
| Snapshot versionado del sitio | `https://standard.aimoaas.com/0.0.1/` |
| Especificación PDF | `trust_package.pdf` |
| Paquete de activos (ZIP) | Esquemas, plantillas, diccionario |
| Checksums | Hashes SHA-256 para integridad |
| Registro de cambios | Este documento |

## Historial de Cambios

### No publicado (correcciones de namespace y normativa)

**Resumen:** Resolución de colisión de códigos EV, clarificación de EV (índice) vs Evidence Pack (payload), endurecimiento de /dev frente a citación errónea en auditoría. Tipos de documento del Evidence Pack usan EP-01..EP-07; Taxonomy EV permanece para tipos de evento. Relación normativa EV↔Evidence Pack documentada en Evidence Bundle. Banner y canonical para /dev.

### Versión 0.0.1 (2026-02-02)

**Resumen:** Release inicial de AIMO Standard con sistema de códigos de 8 dimensiones, plantillas de Paquetes de Evidencia y documentación completa de gobernanza.

#### Agregado

**Sistema de Códigos (8 Dimensiones)**

| Dimensión | Códigos Agregados | Descripción |
| --- | --- | --- |
| FS | FS-001 a FS-006 | Alcance Funcional |
| UC | UC-001 a UC-010 | Clase de Caso de Uso |
| DT | DT-001 a DT-008 | Tipo de Datos |
| CH | CH-001 a CH-006 | Canal |
| IM | IM-001 a IM-005 | Modo de Integración |
| RS | RS-001 a RS-005 | Superficie de Riesgo |
| OB | OB-001 a OB-005 | Resultado / Beneficio |
| LG | LG-001 a LG-015 | Tipo de Log/Registro |

**Esquemas**

- `taxonomy_pack.schema.json`: Definición de paquete de taxonomía
- `changelog.schema.json`: Entradas de registro de cambios
- `evidence_pack_manifest.schema.json`: Manifiestos de Paquetes de Evidencia
- `shadow-ai-discovery.schema.json`: Evidencia de descubrimiento de Shadow AI
- `agent-activity.schema.json`: Evidencia de actividad de agente

**Plantillas de Paquetes de Evidencia (MVP)**

- EV-01: Descripción del Sistema
- EV-02: Flujo de Datos
- EV-03: Inventario de IA
- EV-04: Evaluación de Riesgo e Impacto
- EV-05: Controles y Aprobaciones
- EV-06: Registro y Monitoreo
- EV-07: Manejo de Incidentes y Excepciones

**Documentación**

- Documentación de taxonomía con definiciones de 8 dimensiones
- Especificación de formato del Sistema de Códigos
- Especificación de formato del CSV del Diccionario
- Política de versionado y cambios
- Requisitos MVP del Validador
- Protocolo de Supervisión Humana
- Mapa de Cobertura (ISO 42001, NIST AI RMF, EU AI Act, ISMS)
- Paquete de Confianza

#### Compatibilidad Hacia Atrás

Este es el release inicial; sin preocupaciones de compatibilidad hacia atrás.

---

## Registro de Cambios Legible por Máquina

Un registro de cambios legible por máquina está disponible:

- `changelog/changelog.json`

Este archivo sigue el esquema `changelog.schema.json` y puede ser parseado programáticamente.

## Referencias

- [Taxonomía](../03-taxonomy/) - Definiciones de dimensiones
- [Diccionario](../05-dictionary/) - Diccionario de códigos
- [Política de Versionado](../../../governance/) - Política de versionado (ver VERSIONING.md en la raíz del repositorio)
