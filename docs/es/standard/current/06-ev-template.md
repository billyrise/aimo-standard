---
description: Plantillas y guía de uso de Paquetes de Evidencia AIMO. Estructura para documentar evidencia de gobernanza de IA con gestión de índice y formato listo para auditoría.
---

# Plantilla EV

Esta sección define las plantillas de Paquetes de Evidencia y su uso. Un Paquete de Evidencia es una colección de documentación que demuestra gobernanza y cumplimiento para un sistema de IA.

## Principio Clave: Gestión de Índice y Diff

> **Importante**: Lo que importa no es el contenido de envíos individuales, sino la **gestión de índice** y **diff** a través de elementos de evidencia.

Un Paquete de Evidencia sirve como índice vinculando sistemas de IA a sus artefactos de gobernanza. El valor radica en:

1. **Trazabilidad**: Vincular decisiones, aprobaciones y cambios a través del tiempo
2. **Auditabilidad**: Permitir a auditores navegar la estructura de evidencia
3. **Mantenibilidad**: Rastrear qué cambió, cuándo y por qué

## Conjunto Mínimo de Evidencia MVP (EV-01 a EV-07)

Los siguientes siete tipos de evidencia forman el **conjunto mínimo viable** para demostrar gobernanza de IA:

| ID | Tipo de Evidencia | Código | Propósito |
| --- | --- | --- | --- |
| EV-01 | Descripción del Sistema | EV-001 | Documentar el sistema de IA y su propósito |
| EV-02 | Flujo de Datos | EV-002 | Mapear movimiento de datos a través del sistema |
| EV-03 | Inventario | EV-003 | Mantener catálogo de activos de IA |
| EV-04 | Evaluación de Riesgo e Impacto | EV-004 | Evaluar y documentar riesgos |
| EV-05 | Controles y Aprobaciones | EV-005 | Documentar controles y registros de aprobación |
| EV-06 | Registro y Monitoreo | EV-006 | Definir configuración de registro y monitoreo |
| EV-07 | Incidente y Excepción | EV-007 | Rastrear incidentes y excepciones |

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

Cada Paquete de Evidencia DEBE incluir códigos de las 8 dimensiones:

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
    "EV": ["EV-001", "EV-002", "EV-003", "EV-004", "EV-005", "EV-006", "EV-007"]
  }
}
```

### Lista de Archivos de Evidencia

```json
{
  "evidence_files": [
    {
      "file_id": "EV-01",
      "filename": "EV-01_system_overview.md",
      "ev_type": "EV-001",
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
# EV-01: Descripción del Sistema

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
| **EV** | `EV-001` | System Overview |
```

## Descargas

### Plantillas

Las plantillas de Paquetes de Evidencia están disponibles en:

- `source_pack/04_evidence_pack/templates/EV-01_system_overview.md`
- `source_pack/04_evidence_pack/templates/EV-02_data_flow.md`
- `source_pack/04_evidence_pack/templates/EV-03_inventory.md`
- `source_pack/04_evidence_pack/templates/EV-04_risk_impact.md`
- `source_pack/04_evidence_pack/templates/EV-05_controls_approvals.md`
- `source_pack/04_evidence_pack/templates/EV-06_logging_monitoring.md`
- `source_pack/04_evidence_pack/templates/EV-07_incident_exception.md`

### Esquemas y Ejemplos

- Esquema: `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json`
- Ejemplo: `source_pack/04_evidence_pack/examples/evidence_pack_manifest.example.json`

Consulte [Versiones](../../releases/index.md) para paquetes descargables.

## Modelo de Distribución

> **Nota**: Los objetivos principales de distribución son **firmas de auditoría e integradores de sistemas** (distribuidores de plantillas), no empresas individuales.

Las plantillas están diseñadas para ser:

1. Adoptadas por auditores y consultores como artefactos estándar
2. Distribuidas a empresas con atribución de fuente preservada
3. Versionadas junto con el AIMO Standard

Las empresas reciben plantillas a través de sus auditores, consultores o equipos de gobernanza internos que mantienen la vinculación a la versión del estándar.

## Referencias

- [Taxonomía](./03-taxonomy.md) - Definiciones de dimensiones
- [Códigos](./04-codes.md) - Formato de código
- [Validador](./07-validator.md) - Reglas de validación
- [Paquete de Evidencia](../../artifacts/evidence-bundle.md) - Estructura del paquete
