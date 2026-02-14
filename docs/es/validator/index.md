---
description: Centro del Validador AIMO - Inicio rápido de herramientas de validación. Instale, ejecute e interprete resultados en 30 segundos. Validación de paquetes de evidencia y verificaciones de cumplimiento.
---

# Validador

Esta página es un centro para herramientas de validación y reglas. La especificación normativa para el validador y sus reglas está en el Estándar.

## Inicio Rápido (30 segundos)

**1. Requisitos previos**

```bash
pip install jsonschema   # si no está instalado
```

**2. Ejecutar validación contra un paquete de muestra**

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

**3. Leer el reporte y corregir errores/advertencias**

Salida de ejemplo (éxito):

```
OK
```

Salida de ejemplo (fallo):

```
Schema validation failed:
<root>: 'version' is a required property
<root>: 'dictionary' is a required property
<root>: 'evidence' is a required property
```

Códigos de salida: `0` = éxito, `1` = errores de validación, `2` = error de uso.

---

## Qué verifica

- **Validación de esquema**: objeto raíz, diccionario y evidencia conforman a JSON Schema
- **Consistencia del diccionario**: todos los códigos existen en el diccionario de taxonomía
- **Estado del código**: advierte para códigos obsoletos, errores para códigos eliminados

## Qué NO verifica

- **Precisión del contenido**: el validador verifica estructura, no significado
- **Garantía de cumplimiento**: pasar la validación no garantiza cumplimiento regulatorio
- **Juicio humano**: decisiones dependientes del contexto requieren revisión humana (consulte [Protocolo de Supervisión Humana](../governance/human-oversight-protocol/))
- **Recopilación automática de registros**: el validador valida evidencia enviada; no recopila registros

---

## Recursos

- **Especificación**: [Estándar > Actual > Validador](../standard/current/07-validator/) — reglas, verificaciones de referencia y cómo se relaciona la validación con la evidencia.
- **Reglas e implementación**: repositorio `validator/rules/` (verificaciones), `validator/src/` (implementación de referencia). El uso de ejecución y CI se describe en la especificación.
- **Interpretación**: qué significa un "fallo" de validación para auditores (explicado en la especificación).

Para conformidad y uso de artefactos, consulte [Conformidad](../conformance/) y [Artefactos](../artifacts/).
