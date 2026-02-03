---
description: Validador AIMO - Asegura que los Paquetes de Evidencia conformen a los esquemas del AIMO Standard. Reglas de validación, manejo de errores e implementación de referencia para verificaciones de cumplimiento.
---

# Validador

El Validador AIMO asegura que los Paquetes de Evidencia y artefactos relacionados conformen a los esquemas y requisitos del AIMO Standard.

Consulte también: [Protocolo de Supervisión Humana](../../governance/human-oversight-protocol.md) — límite de responsabilidad para revisión máquina vs. humano.

## Validador en práctica

Para un inicio rápido de 30 segundos (instalar, ejecutar, interpretar salida), consulte [Centro del Validador](../../validator/index.md).

## Requisitos MVP del Validador

El validador mínimo viable DEBE realizar las siguientes verificaciones:

### 1. Validación de Campos Requeridos

Verificar que todos los campos obligatorios estén presentes:

| Artefacto | Campos Requeridos |
| --- | --- |
| Manifiesto del Paquete de Evidencia | pack_id, pack_version, taxonomy_version, created_date, last_updated, codes, evidence_files |
| Objeto de Códigos | FS, UC, DT, CH, IM, RS, EV (OB opcional) |
| Entrada de Archivo de Evidencia | file_id (EP-01..EP-07), filename, title (ev_type / ev_codes opcional) |

### 2. Validación de Códigos de Dimensión

Verificar que cada dimensión requerida tenga al menos un código:

| Dimensión | Requisito |
| --- | --- |
| FS (Alcance Funcional) | Exactamente 1 código |
| UC (Clase de Caso de Uso) | Al menos 1 código |
| DT (Tipo de Datos) | Al menos 1 código |
| CH (Canal) | Al menos 1 código |
| IM (Modo de Integración) | Exactamente 1 código |
| RS (Superficie de Riesgo) | Al menos 1 código |
| OB (Resultado / Beneficio) | Opcional (0 o más) |
| LG (Tipo de log/registro) | Al menos 1 código |

### 3. Verificación de Existencia en Diccionario

Validar que todos los códigos existan en el diccionario de taxonomía:

- Cargar el diccionario de taxonomía para la `taxonomy_version` especificada
- Verificar que cada código en el manifiesto exista en el diccionario
- Reportar códigos inválidos con su dimensión y valor

### 4. Validación de Formato de Código

Verificar que todos los códigos coincidan con el formato esperado:

```regex
^(FS|UC|DT|CH|IM|RS|OB|LG)-\d{3}$
```

### 5. Validación de Esquema

Validar contra JSON Schemas:

| Esquema | Propósito |
| --- | --- |
| `evidence_pack_manifest.schema.json` | Manifiestos de Paquetes de Evidencia |
| `taxonomy_pack.schema.json` | Definiciones de paquetes de taxonomía |
| `changelog.schema.json` | Entradas de registro de cambios |

## Reglas de Validación

### Regla: Dimensiones Requeridas

```yaml
rule_id: required_dimensions
description: Todas las dimensiones requeridas deben tener al menos un código
severity: error
check: |
  - FS: exactamente 1
  - UC: al menos 1
  - DT: al menos 1
  - CH: al menos 1
  - IM: exactamente 1
  - RS: al menos 1
  - LG: al menos 1
```

### Regla: Códigos Válidos

```yaml
rule_id: valid_codes
description: Todos los códigos deben existir en el diccionario de taxonomía
severity: error
check: |
  Para cada código en manifest.codes:
    - El código existe en el diccionario para la taxonomy_version especificada
    - El estado del código es 'active' (advertencia si 'deprecated')
```

### Regla: Formato de Código

```yaml
rule_id: code_format
description: Todos los códigos deben coincidir con el formato estándar
severity: error
pattern: "^(FS|UC|DT|CH|IM|RS|OB|LG)-\\d{3}$"
```

### Regla: Formato de Versión

```yaml
rule_id: version_format
description: Las versiones deben ser SemVer válido
severity: error
pattern: "^\\d+\\.\\d+\\.\\d+$"
fields:
  - pack_version
  - taxonomy_version
```

## Formato de Salida de Errores

Los errores de validación se reportan en el siguiente formato:

```
<ruta>: <severidad>: <mensaje>
```

**Ejemplos:**

```
codes.FS: error: La dimensión requerida 'FS' no tiene códigos
codes.UC[0]: error: El código 'UC-999' no existe en el diccionario v0.1.0
pack_version: error: Formato de versión inválido 'v1.0' (esperado SemVer)
codes.RS[1]: warning: El código 'RS-002' está deprecado en v0.2.0
```

## Qué NO Verifica el Validador

El validador se enfoca en conformidad estructural, no calidad de contenido:

| Aspecto | Razón |
| --- | --- |
| Precisión del contenido | El validador verifica estructura, no significado |
| Completitud de evidencia | Las plantillas son guías, no formatos aplicados |
| Resolución de referencias cruzadas | La existencia de archivos no se verifica |
| Validez de timestamp | ISO-8601 no se valida estrictamente |
| Unicidad de ID | No se aplica actualmente |
| Hashes de integridad | Responsabilidad del adoptante |

## Implementación de Referencia

Se proporciona una implementación de referencia en Python:

```
validator/src/validate.py
```

### Uso

```bash
python validator/src/validate.py <manifest.json>
```

### Ejemplo de Salida

```
Validating: evidence_pack_manifest.json
Taxonomy version: 0.1.0

Checking required dimensions...
  FS: OK (1 código)
  UC: OK (3 códigos)
  DT: OK (1 código)
  CH: OK (1 código)
  IM: OK (1 código)
  RS: OK (3 códigos)
  OB: OK (2 códigos)
  LG: OK (7 códigos)

Checking code validity...
  Todos los códigos válidos.

Validation: PASSED
```

## Política de Versionado

Las reglas del validador siguen SemVer:

- **MAJOR**: Cambios de reglas disruptivos (nuevas verificaciones requeridas que fallan paquetes válidos existentes)
- **MINOR**: Nuevas verificaciones opcionales, advertencias o mensajes informativos
- **PATCH**: Correcciones de bugs que no cambian resultados de validación

## Referencias de Esquema

| Esquema | Ubicación |
| --- | --- |
| Manifiesto de Paquete de Evidencia | `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json` |
| Paquete de Taxonomía | `source_pack/03_taxonomy/schemas/taxonomy_pack.schema.json` |
| Registro de Cambios | `source_pack/03_taxonomy/schemas/changelog.schema.json` |

## Referencias

- [Taxonomía](./03-taxonomy.md) - Definiciones de dimensiones
- [Códigos](./04-codes.md) - Formato de código
- [Diccionario](./05-dictionary.md) - Diccionario de códigos
- [Reglas del Validador](../../validator/index.md) - Documentación completa de reglas
