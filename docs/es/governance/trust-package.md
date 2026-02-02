---
description: Paquete de Confianza AIMO - Paquete de materiales listos para auditores. Documentación mínima para auditores, legal y seguridad de TI para evaluar preparación de adopción de gobernanza de IA.
---

# Paquete de Confianza (Paquete de Aseguramiento)

Esta página agrupa los materiales mínimos que auditores, legal y seguridad de TI necesitan para evaluar preparación de adopción.
Es solo un centro; el TOC detallado de Evidencia y las tablas de Cobertura se mantienen en sus respectivas secciones.

## Descargar

**[Descargar Paquete de Confianza PDF (Última Versión)](https://github.com/billyrise/aimo-standard/releases/latest)**

El PDF del Paquete de Confianza consolida materiales listos para auditores en un solo documento. Cada GitHub Release incluye:

- `trust_package.pdf` — Paquete de Confianza en Inglés
- `trust_package.ja.pdf` — Paquete de Confianza en Japonés
- `aimo-standard-artifacts.zip` — Esquemas, plantillas, ejemplos, reglas del validador
- `SHA256SUMS.txt` — Checksums para verificación

## Qué obtiene

- **Conformidad**: cómo reclamar cumplimiento y qué significan los niveles — [Conformidad](../conformance/index.md)
- **Mapa de Cobertura**: mapeo a estándares externos — [Índice de Mapa de Cobertura](../coverage-map/index.md), [Metodología del Mapa de Cobertura](../coverage-map/methodology.md)
- **Estándar**: requisitos y definiciones normativas — [Estándar (Actual)](../standard/current/index.md)
- **Taxonomía**: sistema de clasificación de 8 dimensiones para gobernanza de IA — [Taxonomía](../standard/current/03-taxonomy.md), [Códigos](../standard/current/04-codes.md), [Diccionario](../standard/current/05-dictionary.md)
- **Paquete de Evidencia**: estructura, TOC, trazabilidad — [Paquete de Evidencia](../artifacts/evidence-bundle.md)
- **Requisitos Mínimos de Evidencia**: lista de verificación de nivel DEBE por ciclo de vida — [Requisitos Mínimos de Evidencia](../artifacts/minimum-evidence.md)
- **Validador**: reglas y verificaciones de referencia — [Validador](../validator/index.md)
- **Ejemplos**: paquetes de muestra listos para auditoría — [Ejemplos](../examples/index.md)
- **Versiones**: historial de cambios y distribución — [Versiones](../releases/index.md)
- **Gobernanza**: políticas, seguridad, licencias — [Gobernanza](../governance/index.md)

## Conjunto mínimo para preparación de auditoría

| Elemento | Dónde encontrarlo | Resultado / qué demuestra |
| --- | --- | --- |
| Niveles de conformidad | [Conformidad](../conformance/index.md) | Cómo reclamar cumplimiento y el alcance de evidencia requerida |
| Mapeo de cobertura | [Índice de Mapa de Cobertura](../coverage-map/index.md), [Metodología del Mapa de Cobertura](../coverage-map/methodology.md) | Explicabilidad contra regulaciones y estándares externos |
| Taxonomía y Diccionario | [Taxonomía](../standard/current/03-taxonomy.md), [Códigos](../standard/current/04-codes.md), [Diccionario](../standard/current/05-dictionary.md) | Sistema de clasificación para sistemas de IA (8 dimensiones, 91 códigos) |
| Artefactos de evidencia | [Paquete de Evidencia](../artifacts/evidence-bundle.md), [Evidencia Mínima](../artifacts/minimum-evidence.md), [Plantilla EV](../standard/current/06-ev-template.md) | Qué datos deben existir para soportar trazabilidad |
| Verificaciones del validador | [Validador](../validator/index.md) | Cómo verificar consistencia y completitud interna |
| Paquete de ejemplo | [Ejemplos](../examples/index.md) | Cómo se ve un paquete listo para auditoría en práctica |
| Control de cambios | [Versiones](../releases/index.md), [Gobernanza](../governance/index.md) | Cómo se gestionan y comunican las actualizaciones |
| Seguridad / Licencia / Marcas | [Gobernanza](../governance/index.md) | Postura legal y de seguridad para decisiones de adopción |

## Cómo citar

Use el README del repositorio para guía de citación y contexto; los enlaces de gobernanza apuntan a las políticas autoritativas.
Consulte [README.md](https://github.com/billyrise/aimo-standard/blob/main/README.md) y [Gobernanza](../governance/index.md).

## Contenido del zip de artefactos

El `aimo-standard-artifacts.zip` incluye:

- **Taxonomía (SSOT)**: `source_pack/03_taxonomy/` — CSV del Diccionario (91 códigos), YAML, sistema de códigos
- **JSON Schemas**: `schemas/jsonschema/` — Esquemas de validación legibles por máquina
- **Plantillas**: `templates/ev/` — Plantillas de registros de evidencia (JSON + Markdown)
- **Ejemplos**: `examples/` — Paquetes de muestra mínimos para adopción rápida
- **Mapa de Cobertura**: `coverage_map/coverage_map.yaml` — Mapeo a estándares externos
- **Reglas del Validador**: `validator/rules/` — Definiciones de reglas de validación
- **Docs de gobernanza**: `VERSIONING.md`, `GOVERNANCE.md`, `SECURITY.md`, `LICENSE.txt`, etc.

## Límite de responsabilidad

El AIMO Standard proporciona un formato de evidencia estructurado y marco de explicabilidad. **No** proporciona asesoramiento legal, certificación de cumplimiento, evaluación de riesgos ni ejecución de auditoría.

Para la definición completa de alcance, suposiciones y responsabilidades del adoptante, consulte [Límite de Responsabilidad](responsibility-boundary.md).

## Cómo preparar un paquete de envío

Siga estos pasos para preparar un envío listo para auditoría:

1. **Generar Paquete de Evidencia**: Cree registros EV, Diccionario, Resumen y Registro de Cambios según [Paquete de Evidencia](../artifacts/evidence-bundle.md) y [Requisitos Mínimos de Evidencia](../artifacts/minimum-evidence.md).
2. **Ejecutar Validador**: Ejecute `python validator/src/validate.py bundle/root.json` para verificar consistencia estructural. Corrija cualquier error antes de continuar.
3. **Crear Checksums**: Genere checksums SHA-256 para todos los archivos de envío:

    === "Linux"

        ```bash
        sha256sum *.json *.pdf > SHA256SUMS.txt
        ```

    === "macOS"

        ```bash
        shasum -a 256 *.json *.pdf > SHA256SUMS.txt
        ```

    === "Windows (PowerShell)"

        ```powershell
        Get-ChildItem *.json, *.pdf | ForEach-Object {
            $hash = (Get-FileHash $_.FullName -Algorithm SHA256).Hash.ToLower()
            "$hash  $($_.Name)"
        } | Out-File SHA256SUMS.txt -Encoding UTF8
        ```
4. **Empaquetar Artefactos**: Cree un archivo zip de su paquete de evidencia:
   ```bash
   zip -r evidence_bundle.zip bundle_directory/
   ```
5. **Referenciar Versión de Release**: Note qué versión del AIMO Standard (ej., `v1.0.0`) su paquete alinea.
6. **Entregar**: Proporcione el zip, checksums y referencia de versión a su auditor o función de cumplimiento.

Para activos de release y verificación, consulte [Versiones](../releases/index.md).

## Declaración de no sobre-reclamación

!!! warning "Importante"
    El AIMO Standard soporta **explicabilidad y preparación de evidencia**. **No** proporciona asesoramiento legal, garantiza cumplimiento ni certifica conformidad con ninguna regulación o marco. Los adoptantes deben verificar reclamaciones contra textos autoritativos y obtener asesoramiento profesional según sea apropiado.

Consulte [Límite de Responsabilidad](responsibility-boundary.md) para detalles sobre alcance, suposiciones y responsabilidades del adoptante.

## Para auditores: Procedimiento de verificación

Al recibir un envío de evidencia, los auditores deben verificar integridad y estructura usando los siguientes pasos:

!!! success "Procedencia de Build Disponible"
    Todos los activos de release incluyen atestaciones de procedencia de build firmadas criptográficamente. Consulte [Procedimiento de Verificación](../standard/versions/index.md#4-verify-build-provenance-attestation) para pasos de verificación de atestación.

### Paso 1: Verificar checksums (SHA-256)

=== "Linux"

    ```bash
    # Descargue o reciba SHA256SUMS.txt con el envío
    # Verifique que todos los archivos coincidan con sus checksums registrados
    sha256sum -c SHA256SUMS.txt

    # O verifique archivos individuales manualmente:
    sha256sum evidence_bundle.zip
    # Compare salida con el valor en SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # Verifique que todos los archivos coincidan con sus checksums registrados
    shasum -a 256 -c SHA256SUMS.txt

    # O verifique archivos individuales manualmente:
    shasum -a 256 evidence_bundle.zip
    # Compare salida con el valor en SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Verifique archivos individuales
    Get-FileHash .\evidence_bundle.zip -Algorithm SHA256

    # Compare la salida Hash con SHA256SUMS.txt
    Get-Content .\SHA256SUMS.txt
    ```

Si algún checksum falla, el envío debe ser rechazado o re-solicitado.

### Paso 2: Verificar estructura del paquete (Validador)

**Requisitos previos** (configuración única):

```bash
# Clone el release oficial de AIMO Standard
git clone https://github.com/billyrise/aimo-standard.git
cd aimo-standard

# IMPORTANTE: Use la versión exacta indicada en el envío
# Reemplace VERSION con la versión declarada del remitente (ej., v0.0.1)
VERSION=v0.0.1  # ← Coincida la versión en el envío
git checkout "$VERSION"

# Configure entorno Python
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

!!! warning "Coincidencia de Versión"
    Siempre use la versión exacta del AIMO Standard indicada en el envío. Usar una versión diferente puede causar discrepancias de validación debido a cambios de esquema o reglas entre versiones.

**Ejecutar validación**:

```bash
# Extraiga el paquete enviado
unzip evidence_bundle.zip -d bundle/

# Ejecute validador contra el root.json del paquete
python validator/src/validate.py bundle/root.json

# Salida esperada: "validation OK" o lista de errores
```

**Ejemplo** (usando muestra incorporada):

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

El validador verifica:

- Los archivos requeridos existen (registros EV, Diccionario)
- Los archivos JSON conforman al esquema
- Las referencias cruzadas (request_id, review_id, etc.) son válidas
- Las marcas de tiempo están presentes y formateadas correctamente

### Paso 3: Verificar alineación de versión

Verifique que el envío referencia un release oficial del AIMO Standard:

1. Confirme que la versión indicada (ej., `v0.0.1`) existe en [GitHub Releases](https://github.com/billyrise/aimo-standard/releases)
2. Compare esquemas enviados contra los artefactos del release
3. Note cualquier desviación del release oficial

### Qué buscar

| Verificación | Criterio de Aprobación | Acción en Fallo |
| --- | --- | --- |
| Checksums coinciden | Todas las verificaciones `sha256sum -c` pasan | Rechazar o re-solicitar |
| Validador pasa | Sin errores de `validate.py` | Solicitar correcciones antes de aceptación |
| Versión existe | Tag de release existe en GitHub | Clarificar alineación de versión |
| Campos requeridos presentes | Registros EV tienen id, timestamp, source, summary | Solicitar completación |
| Trazabilidad intacta | Referencias cruzadas resuelven correctamente | Solicitar correcciones de vinculación |

!!! info "Independencia del auditor"
    Los auditores deben obtener el validador y esquemas directamente del release oficial del AIMO Standard, no de la parte que envía, para asegurar independencia de verificación.

## Recorrido de auditoría

Desde esta página, el recorrido de auditoría recomendado es:

1. **Sistema de clasificación**: [Taxonomía](../standard/current/03-taxonomy.md) + [Diccionario](../standard/current/05-dictionary.md) — comprenda el sistema de códigos de 8 dimensiones
2. **Estructura de evidencia**: [Paquete de Evidencia](../artifacts/evidence-bundle.md) — comprenda TOC del paquete y trazabilidad
3. **Evidencia requerida**: [Requisitos Mínimos de Evidencia](../artifacts/minimum-evidence.md) — lista de verificación de nivel DEBE por ciclo de vida
4. **Alineación de marco**: [Mapa de Cobertura](../coverage-map/index.md) + [Metodología](../coverage-map/methodology.md) — vea cómo AIMO mapea a marcos externos
5. **Validación**: [Validador](../validator/index.md) — ejecute verificaciones de consistencia estructural
6. **Descargar**: [Versiones](../releases/index.md) — obtenga activos de release y verifique checksums
