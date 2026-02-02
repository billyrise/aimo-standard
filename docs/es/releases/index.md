---
description: Versiones de AIMO Standard - Descargue PDFs versionados, artefactos y checksums. Registro de cambios, guías de migración y atestaciones de procedencia de build.
---

# Versiones

Esta sección es un centro para versiones versionadas, registro de cambios, migración y artefactos de distribución.

## Descargar Última Versión

**[GitHub Releases](https://github.com/billyrise/aimo-standard/releases/latest)**

## Activos de Release

Cada release oficial (tag `vX.Y.Z`) incluye:

| Activo | Descripción |
| --- | --- |
| `trust_package.pdf` | Paquete de Confianza en Inglés — materiales de aseguramiento listos para auditores |
| `trust_package.ja.pdf` | Paquete de Confianza en Japonés |
| `aimo-standard-artifacts.zip` | Esquemas, plantillas, ejemplos, reglas del validador |
| `SHA256SUMS.txt` | Checksums SHA-256 para todos los activos |

### Verificando Descargas

Después de descargar, verifique la integridad del archivo usando checksums:

=== "Linux"

    ```bash
    # Descargue el archivo de checksums
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # Verifique un archivo específico
    sha256sum -c SHA256SUMS.txt --ignore-missing

    # O verifique manualmente:
    sha256sum trust_package.pdf
    # Compare salida con SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # Descargue el archivo de checksums
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # Verifique un archivo específico
    shasum -a 256 -c SHA256SUMS.txt

    # O verifique manualmente:
    shasum -a 256 trust_package.pdf
    # Compare salida con SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Descargue el archivo de checksums
    Invoke-WebRequest -Uri "https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt" -OutFile SHA256SUMS.txt

    # Verifique un archivo específico
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # Compare la salida Hash con SHA256SUMS.txt
    Get-Content .\SHA256SUMS.txt
    ```

## Contenido del Zip de Artefactos

El `aimo-standard-artifacts.zip` contiene:

- `schemas/jsonschema/*` — JSON Schemas para validación
- `templates/ev/*` — Plantillas de evidencia (JSON + Markdown)
- `examples/*` — Paquetes de evidencia de muestra
- `coverage_map/coverage_map.yaml` — Mapeo de estándares externos
- `validator/rules/*` — Definiciones de reglas de validación
- `VERSIONING.md`, `GOVERNANCE.md`, `SECURITY.md`, etc.

## Recursos

- **Tabla de Historial de Versiones**: [Estándar > Versiones](../standard/versions/index.md) — tabla de versiones con enlaces directos a todos los activos de release (PDF, ZIP, SHA256)
- **Registro de cambios (spec)**: [Estándar > Actual > Registro de Cambios](../standard/current/08-changelog.md) — historial de cambios normativos y no-normativos.
- **Proceso de release**: etiquetado `vX.Y.Z`, CI build, PDF bajo `dist/`, checksums, activos de GitHub Release. Consulte [GOVERNANCE.md](https://github.com/billyrise/aimo-standard/blob/main/GOVERNANCE.md) y [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) en el repositorio.
- **Guía de migración**: [MIGRATION.md](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) — rutas de actualización para cambios disruptivos.

Para gobernanza y política de versionado, consulte [Gobernanza](../governance/index.md).

## Preparando su paquete de envío

Al preparar evidencia para envío de auditoría:

1. **Cree su Paquete de Evidencia**: Siga [Paquete de Evidencia](../artifacts/evidence-bundle.md) y [Requisitos Mínimos de Evidencia](../artifacts/minimum-evidence.md) para crear registros EV, Diccionario, Resumen y Registro de Cambios.
2. **Ejecute el Validador**: Ejecute `python validator/src/validate.py bundle/root.json` para verificar consistencia estructural. Corrija todos los errores antes de continuar.
3. **Genere Checksums**: Cree checksums SHA-256 para verificación:

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
4. **Empaquete**: Cree un archivo zip de su directorio de paquete.
5. **Documente alineación de versión**: Note qué release del AIMO Standard (ej., `v1.0.0`) alinea su evidencia.
6. **Entregue**: Proporcione el paquete, checksums y referencia de versión a su auditor.

Para la guía completa de preparación, consulte [Paquete de Confianza](../governance/trust-package.md).

## Para auditores: Procedimiento de verificación

Los auditores que reciben envíos de evidencia deben verificar integridad y estructura:

1. **Verificar checksums**: Ejecute verificación de checksum (Linux: `sha256sum -c`, macOS: `shasum -a 256 -c`, Windows: `Get-FileHash`) para confirmar integridad del archivo
2. **Ejecutar validador**: Ejecute `python validator/src/validate.py bundle/root.json` para verificar estructura
3. **Confirmar versión**: Verifique que la versión indicada del AIMO Standard existe en [GitHub Releases](https://github.com/billyrise/aimo-standard/releases)

!!! tip "Obtenga herramientas de forma independiente"
    Los auditores deben descargar el validador y esquemas directamente del release oficial del AIMO Standard, no de la parte que envía.

Para el procedimiento de verificación completo, consulte [Paquete de Confianza](../governance/trust-package.md).

## Declaración de no sobre-reclamación

!!! warning "Importante"
    El AIMO Standard soporta **explicabilidad y preparación de evidencia**. **No** proporciona asesoramiento legal, garantiza cumplimiento ni certifica conformidad con ninguna regulación o marco. Los adoptantes deben verificar reclamaciones contra textos autoritativos y obtener asesoramiento profesional según sea apropiado.

Consulte [Límite de Responsabilidad](../governance/responsibility-boundary.md) para alcance, suposiciones y responsabilidades del adoptante.
