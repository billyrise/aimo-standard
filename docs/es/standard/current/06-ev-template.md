---
description: Plantillas y guía de uso de Paquetes de Evidencia AIMO. Estructura para documentar evidencia de gobernanza de IA con gestión de índice y formato listo para auditoría.
---

# Plantilla Evidence Pack (EP)

Esta sección define las plantillas de Paquetes de Evidencia y su uso. Un Paquete de Evidencia es una colección de documentación que demuestra gobernanza y cumplimiento para un sistema de IA.

## Espacio de nombres: tipos de documento Evidence Pack (EP) vs Taxonomy Log/Event Type (LG)

> **Importante**: **EP-01..EP-07** identifican *tipos de documento* (tipos de archivo del Evidence Pack). **LG-001, LG-002, …** en la [Taxonomía](../03-taxonomy/) identifican *tipos de log/registro* (Registro de Solicitud, Registro de Revisión/Aprobación, etc.). **EV-** reservado para ID de artefactos Evidence. Use EP para estructura del pack y LG para clasificación de evidencia del ciclo de vida.

## Principio Clave: Gestión de Índice y Diff

Lo que importa no es solo el contenido de envíos individuales, sino el **índice** y la **gestión de diff** entre elementos de evidencia.

Un Paquete de Evidencia sirve como índice vinculando sistemas de IA a sus artefactos de gobernanza. El valor radica en:

1. **Trazabilidad**: Vincular decisiones, aprobaciones y cambios a través del tiempo
2. **Auditabilidad**: Permitir a auditores navegar la estructura de evidencia
3. **Mantenibilidad**: Rastrear qué cambió, cuándo y por qué

## Conjunto Mínimo de Evidencia MVP (EP-01 a EP-07)

Los siguientes siete **tipos de documento Evidence Pack** (EP) forman el **conjunto mínimo viable** para demostrar gobernanza de IA. Cada uno es una plantilla de documento; los códigos **LG** de taxonomía (Registro de Solicitud, Revisión/Aprobación, etc.) se usan en el bundle y en `codes.LG` para clasificar evidencia de *log/registro*.

| ID | Tipo de documento | Propósito |
| --- | --- | --- |
| EP-01 | Descripción del Sistema | Documentar el sistema de IA y su propósito |
| EP-02 | Flujo de Datos | Mapear movimiento de datos a través del sistema |
| EP-03 | Inventario | Mantener catálogo de activos de IA |
| EP-04 | Evaluación de Riesgo e Impacto | Evaluar y documentar riesgos |
| EP-05 | Controles y Aprobaciones | Documentar controles y registros de aprobación |
| EP-06 | Registro y Monitoreo | Definir configuración de registro y monitoreo |
| EP-07 | Incidente y Excepción | Rastrear incidentes y excepciones |

## Manifiesto del Paquete de Evidencia

Cada Paquete de Evidencia DEBE incluir un archivo de manifiesto que contenga:

### Metadatos Obligatorios

| Campo | Descripción | Requerido |
| --- | --- | --- |
| `pack_id` | Identificador único (ej., EP-EXAMPLE-001) | Sí |
| `pack_version` | Versión SemVer del paquete | Sí |
| `taxonomy_version` | Versión de taxonomía AIMO usada | Sí |
| `created_date` | Fecha de creación del paquete | Sí |
| `last_updated` | Fecha de última actualización | Sí |
| `owner` | Parte responsable | Sí |

### Códigos AIMO (8 Dimensiones)

Cada Paquete de Evidencia DEBE incluir códigos de las 8 dimensiones. La dimensión **LG** lista los tipos de log/registro de *taxonomía* (p. ej. Registro de Solicitud, Revisión/Aprobación) aplicables a este pack—no códigos de tipo de documento. El tipo de documento viene dado por `evidence_files[].file_id` (EP-01..EP-07).

```json
{
  "codes": {
    "FS": ["FS-001"],
    "UC": ["UC-001", "UC-002"],
    "DT": ["DT-002"],
    "CH": ["CH-001"],
    "IM": ["IM-001"],
    "RS": ["RS-001", "RS-003"],
    "OB": ["OB-001"],
    "LG": ["LG-001", "LG-002", "LG-008", "LG-009"]
  }
}
```

### Lista de Archivos de Evidencia

Cada entrada identifica un documento del pack por **file_id** (EP-01..EP-07). Opcionalmente **ev_codes** puede listar códigos LG de taxonomía (LG-xxx) que el documento soporta.

```json
{
  "evidence_files": [
    {
      "file_id": "EP-01",
      "filename": "EP-01_system_overview.md",
      "title": "System Overview",
      "required": true
    }
  ]
}
```

## Estructura de Plantilla

Cada plantilla de evidencia incluye:

1. **Bloque de Metadatos Obligatorios** - pack_id, version, taxonomy_version, fechas, owner
2. **Tabla de Códigos AIMO** - Las 8 dimensiones con códigos aplicables
3. **Secciones de Contenido** - Secciones de documentación específicas del dominio
4. **Referencias** - Enlaces a evidencia relacionada
5. **Historial de Revisiones** - Seguimiento de cambios

### Ejemplo de Encabezado de Plantilla

```markdown
# EP-01: Descripción del Sistema

---

## Metadatos Obligatorios

| Campo | Valor |
| --- | --- |
| **pack_id** | `EP-EXAMPLE-001` |
| **pack_version** | `0.1.0` |
| **taxonomy_version** | `0.1.0` |
| **created_date** | `2026-01-31` |
| **last_updated** | `2026-01-31` |
| **owner** | `AI Governance Team` |

---

## Códigos AIMO (8 Dimensiones)

| Dimensión | Código(s) | Etiqueta |
| --- | --- | --- |
| **FS** | `FS-001` | End-user Productivity |
| **UC** | `UC-001` | General Q&A |
| **DT** | `DT-002` | Internal |
| **CH** | `CH-001` | Web UI |
| **IM** | `IM-001` | Standalone |
| **RS** | `RS-001` | Data Leakage |
| **OB** | `OB-001` | Efficiency |
| **LG** | `LG-001`, `LG-002` | Request Record, Review/Approval Record |
```

## Descargas

### Plantillas

Las plantillas de Evidence Pack están disponibles en el repositorio. Use **file_id** EP-01..EP-07 en el manifiesto; los nombres de archivo pueden ser EP-01_... o legacy EV-01_... por compatibilidad.

- `source_pack/04_evidence_pack/templates/EV-01_system_overview.md` → file_id **EP-01**
- `source_pack/04_evidence_pack/templates/EV-02_data_flow.md` → file_id **EP-02**
- `source_pack/04_evidence_pack/templates/EV-03_inventory.md` → file_id **EP-03**
- `source_pack/04_evidence_pack/templates/EV-04_risk_impact.md` → file_id **EP-04**
- `source_pack/04_evidence_pack/templates/EV-05_controls_approvals.md` → file_id **EP-05**
- `source_pack/04_evidence_pack/templates/EV-06_logging_monitoring.md` → file_id **EP-06**
- `source_pack/04_evidence_pack/templates/EV-07_incident_exception.md` → file_id **EP-07**

### Esquemas y Ejemplos

- Esquema: `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json`
- Ejemplo: `source_pack/04_evidence_pack/examples/evidence_pack_manifest.example.json`

Consulte [Versiones](../../../releases/) para paquetes descargables.

## Modelo de Distribución

> **Nota**: Los objetivos principales de distribución son **firmas de auditoría e integradores de sistemas** (distribuidores de plantillas), no empresas individuales.

Las plantillas están diseñadas para ser:

1. Adoptadas por auditores y consultores como artefactos estándar
2. Distribuidas a empresas con atribución de fuente preservada
3. Versionadas junto con el AIMO Standard

Las empresas reciben plantillas a través de sus auditores, consultores o equipos de gobernanza internos que mantienen la vinculación a la versión del estándar.

## Referencias

- [Taxonomía](../03-taxonomy/) - Definiciones de dimensiones
- [Códigos](../04-codes/) - Formato de código
- [Validador](../07-validator/) - Reglas de validación
- [Paquete de Evidencia](../../../artifacts/evidence-bundle/) - Estructura del paquete
