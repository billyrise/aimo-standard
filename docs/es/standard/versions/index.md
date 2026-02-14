---
description: Historial de versiones de AIMO Standard. Releases oficiales congelados con PDFs listos para auditores, artefactos legibles por máquina, checksums y atestaciones de procedencia de build.
---

# Versiones

Los releases oficiales son snapshots congelados publicados con PDFs listos para auditores y artefactos legibles por máquina.

## Última Versión

!!! success "Versión Actual"
    **v0.0.2** (2026-02-02) — [Ver Documentación](../current/) | [GitHub Release](https://github.com/billyrise/aimo-standard/releases/tag/v0.0.2)

## Historial de Versiones

| Versión | Fecha | Notas de Release | PDF (EN) | PDF (JA) | Artefactos | Checksums |
| :------ | :--- | :------------ | :------- | :------- | :-------- | :-------- |
| **v0.0.2** | 2026-02-02 | [Registro de Cambios](../current/08-changelog/) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/SHA256SUMS.txt) |
| **v0.0.1** | 2026-02-02 | [Registro de Cambios](../current/08-changelog/) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/SHA256SUMS.txt) |

!!! note "Fuente de Datos"
    Esta tabla de versiones está sincronizada con [GitHub Releases](https://github.com/billyrise/aimo-standard/releases). Cada tag de release (`vX.Y.Z`) corresponde a un snapshot congelado de la especificación.

## Fuente única de verdad (SSOT) para "latest"

La **definición autorizada de "latest"** es el tag **latest** de [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) (`releases/latest`). La ruta del sitio `/latest/` redirige siempre a ese release. No existe un "latest del sitio" separado: el flujo de release despliega la versión etiquetada y la establece como alias `latest` en un solo paso.

| Fuente | Rol |
|--------|-----|
| **Tag latest de GitHub Release** | SSOT — única definición de "release actual" |
| **Tabla de versiones** (esta página) | Sincronizada con releases vía flujo de release; debe coincidir con el tag antes del despliegue |
| **Changelog** | Historial de cambios normativo; las notas de release lo referencian |
| **Sitio `/latest/`** | Redirección a la misma versión que GitHub Release latest |

Para detalles del proceso de release, véase [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) y el [flujo de release](https://github.com/billyrise/aimo-standard/blob/main/.github/workflows/release.yml). La tabla de versiones y el Changelog se actualizan como parte de la preparación del release para que coincidan siempre con la versión desplegada.

## Avisos legales y de marcas

**English notice (key facts):** Only AIMOaaS has been filed for trademark registration by RISEby Inc. (pending). "AIMO" is a registered trademark owned by third parties; RISEby Inc. does not claim ownership. For full trademark status and usage, see [Governance → Marcas Comerciales](../../governance/trademarks/) and [TRADEMARKS.md](https://github.com/billyrise/aimo-standard/blob/main/TRADEMARKS.md).

## Para auditores: URL canónica y fijación de versión

Para citar una versión concreta en informes de auditoría y garantizar reproducibilidad:

1. **URL canónica**: Use la URL de documentación fija de esa versión, p. ej. `https://standard.aimoaas.com/0.0.3/` (sustituya `0.0.3` por la versión utilizada).
2. **Fijación de versión**: Registre el **tag de release** (p. ej. `v0.0.3`) y opcionalmente el **hash de commit** de la página [GitHub Release](https://github.com/billyrise/aimo-standard/releases). Así se puede verificar de forma independiente que el snapshot de la especificación coincide con los activos del release (PDF, ZIP, checksums).
3. **Alineación de evidencia**: Indique en su envío con qué versión de AIMO Standard (p. ej. `v0.0.3`) se alinea su evidence bundle, y obtenga el validador y los esquemas del mismo release.

## Capas de versión

AIMO Standard utiliza tres conceptos de versión. En el release actual están alineados; en releases futuros pueden versionarse de forma independiente.

| Capa | Descripción | Dónde aparece |
|------|-------------|--------------|
| **Versión Standard** (sitio/release) | El tag de release y el snapshot de documentación (p. ej. `v0.0.3`). | Tabla de versiones, GitHub Releases, URLs `/X.Y.Z/`. |
| **Versión del esquema Taxonomy** | Versión del sistema de códigos y definiciones taxonomy/esquema. | `taxonomy_version` en manifiestos; `$id` del esquema o docs. |
| **Versión del contenido Dictionary** | Versión de las entradas del diccionario (códigos y definiciones). | Metadatos del diccionario; igual que taxonomy en 0.0.x. |

Al citar "AIMO Standard vX.Y.Z", la **versión Standard** es la que define el snapshot canónico. El Validator y los Minimum Evidence Requirements se refieren a los artefactos y esquemas de ese release.

## Procedimiento de Verificación

Los auditores e implementadores deben verificar la integridad de descarga usando checksums SHA-256:

### 1. Descargar Activos de Release

=== "Linux / macOS"

    ```bash
    # Descargue todos los activos para una versión específica
    VERSION=v0.0.1
    BASE_URL="https://github.com/billyrise/aimo-standard/releases/download/${VERSION}"

    curl -LO "${BASE_URL}/trust_package.pdf"
    curl -LO "${BASE_URL}/trust_package.ja.pdf"
    curl -LO "${BASE_URL}/aimo-standard-artifacts.zip"
    curl -LO "${BASE_URL}/SHA256SUMS.txt"
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Descargue todos los activos para una versión específica
    $VERSION = "v0.0.1"
    $BASE_URL = "https://github.com/billyrise/aimo-standard/releases/download/$VERSION"

    Invoke-WebRequest -Uri "$BASE_URL/trust_package.pdf" -OutFile trust_package.pdf
    Invoke-WebRequest -Uri "$BASE_URL/trust_package.ja.pdf" -OutFile trust_package.ja.pdf
    Invoke-WebRequest -Uri "$BASE_URL/aimo-standard-artifacts.zip" -OutFile aimo-standard-artifacts.zip
    Invoke-WebRequest -Uri "$BASE_URL/SHA256SUMS.txt" -OutFile SHA256SUMS.txt
    ```

### 2. Verificar Checksums

=== "Linux"

    ```bash
    # Verifique todos los archivos descargados contra checksums
    sha256sum -c SHA256SUMS.txt

    # Salida esperada (todos deben mostrar "OK"):
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "macOS"

    ```bash
    # Verifique todos los archivos descargados contra checksums
    shasum -a 256 -c SHA256SUMS.txt

    # Salida esperada (todos deben mostrar "OK"):
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Verifique cada archivo
    Get-FileHash .\trust_package.pdf -Algorithm SHA256
    Get-FileHash .\trust_package.ja.pdf -Algorithm SHA256
    Get-FileHash .\aimo-standard-artifacts.zip -Algorithm SHA256

    # Compare salida Hash con SHA256SUMS.txt
    Get-Content .\SHA256SUMS.txt
    ```

### 3. Verificación Manual (Alternativa)

=== "Linux"

    ```bash
    # Calcule hash para un archivo específico
    sha256sum trust_package.pdf

    # Compare salida con SHA256SUMS.txt
    cat SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # Calcule hash para un archivo específico
    shasum -a 256 trust_package.pdf

    # Compare salida con SHA256SUMS.txt
    cat SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Calcule hash para un archivo específico
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # Vea archivo de checksums
    Get-Content .\SHA256SUMS.txt
    ```

!!! tip "Para Auditores"
    Siempre obtenga el archivo de checksums directamente del GitHub Release oficial, no de la parte que envía. Esto asegura verificación independiente.

### 4. Verificar Procedencia de Build (Atestación)

Todos los activos de release incluyen atestaciones de procedencia de build firmadas criptográficamente generadas por GitHub Actions. Esto le permite verificar que los activos fueron construidos en el repositorio oficial sin manipulación.

**Requisitos previos**: Instale [GitHub CLI](https://cli.github.com/) (`gh`)

```bash
# Descargue activos de release usando GitHub CLI
VERSION=v0.0.1
gh release download "$VERSION" --repo billyrise/aimo-standard

# Verifique atestación para cada activo
gh attestation verify trust_package.pdf --repo billyrise/aimo-standard
gh attestation verify trust_package.ja.pdf --repo billyrise/aimo-standard
gh attestation verify aimo-standard-artifacts.zip --repo billyrise/aimo-standard
gh attestation verify SHA256SUMS.txt --repo billyrise/aimo-standard
```

**Salida esperada** (éxito):

```
Loaded digest sha256:abc123... for file trust_package.pdf
Loaded 1 attestation from GitHub API
✓ Verification succeeded!
```

**Verificación offline** (entornos air-gapped):

```bash
# Primero, descargue la raíz de confianza (requiere red una vez)
gh attestation trusted-root > trusted-root.jsonl

# Luego verifique offline
gh attestation verify trust_package.pdf \
  --repo billyrise/aimo-standard \
  --custom-trusted-root trusted-root.jsonl
```

!!! info "Qué demuestra la atestación"
    La atestación de procedencia de build demuestra criptográficamente que los activos de release fueron:

    1. Construidos por GitHub Actions (no la máquina local de un desarrollador)
    2. Construidos desde el repositorio oficial `billyrise/aimo-standard`
    3. Construidos desde el commit exacto asociado con el tag de release
    4. No modificados después de que se completó el build

## Compatibilidad

AIMO Standard sigue [Semantic Versioning](https://semver.org/) (SemVer):

| Tipo de Cambio | Bump de Versión | Impacto |
| :---------- | :----------- | :----- |
| **MAJOR** | X.0.0 | Cambios disruptivos — migración requerida |
| **MINOR** | 0.X.0 | Adiciones compatibles hacia atrás |
| **PATCH** | 0.0.X | Correcciones y clarificaciones |

Para la política de versionado completa, consulte [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md).

## Migración

Al actualizar entre versiones con cambios disruptivos:

1. Verifique el [Registro de Cambios](../current/08-changelog/) para cambios disruptivos
2. Revise la [Guía de Migración](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) para rutas de actualización específicas
3. Actualice su Paquete de Evidencia para alinear con los nuevos requisitos de esquema
4. Re-ejecute el validador para verificar cumplimiento

!!! warning "Cambios Disruptivos"
    Las actualizaciones de versión MAJOR pueden requerir cambios a Paquetes de Evidencia existentes. Siempre revise la guía de migración antes de actualizar.

## Snapshots de Documentación Versionada

Cada release crea un snapshot de documentación congelado accesible en:

- Producción: `https://standard.aimoaas.com/{version}/` (ej., `/0.0.1/`)
- GitHub Pages: `https://billyrise.github.io/aimo-standard/{version}/`

### Tipos de URL y Su Significado

| Patrón de URL | Descripción | ¿Para Citaciones de Auditoría? |
|-------------|-------------|---------------------|
| `/X.Y.Z/` (ej., `/0.0.1/`) | **Release congelado** — snapshot inmutable | **Sí** (preferido) |
| `/latest/` | **Alias** — redirige al release más reciente | Sí (resuelve a `/X.Y.Z/`) |
| `/dev/` | **Preview** — contenido de rama main no publicado | **No** (no para citaciones) |

!!! warning "Entendiendo `/latest/` vs `/dev/`"
    - **`/latest/`** es un alias (redirección) a la versión **publicada** más reciente. Es seguro para citaciones ya que resuelve a un snapshot congelado.
    - **`/dev/`** refleja la rama `main` actual y puede contener **cambios no publicados**. Nunca cite `/dev/` en reportes de auditoría.

### FAQ

??? question "¿Por qué `/latest/` no es un número de versión?"
    `/latest/` es un alias de conveniencia que siempre redirige al release estable más reciente (ej., `/0.0.1/`). Esto permite a los usuarios guardar una sola URL mientras obtienen automáticamente la versión actual. Para auditorías formales que requieren inmutabilidad, cite la URL de versión explícita en su lugar.

??? question "¿Qué URL deben citar los auditores?"
    - **Auditorías formales (inmutabilidad requerida)**: Use `/X.Y.Z/` (ej., `https://standard.aimoaas.com/0.0.1/standard/current/`)
    - **Referencias generales**: `/latest/` es aceptable ya que redirige al release actual
    - **Nunca cite**: `/dev/` (no publicado, sujeto a cambios)

??? question "¿Qué pasa si `/latest/` muestra contenido diferente al esperado?"
    Esto sería un bug de despliegue. Si sospecha que `/latest/` difiere del [GitHub Release](https://github.com/billyrise/aimo-standard/releases) más reciente, por favor [reporte un issue](https://github.com/billyrise/aimo-standard/issues). El alias `/latest/` siempre debe redirigir al release etiquetado más reciente.

## Recursos

- **[Centro de Versiones](../../../releases/)** — Preparación de envío, verificación de auditor, declaración de no sobre-reclamación
- **[Paquete de Confianza](../../governance/trust-package/)** — Materiales de aseguramiento listos para auditores
- **[Registro de Cambios (detallado)](../current/08-changelog/)** — Historial completo de cambios con seguimiento de deprecación
- **[VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)** — Política de versionado completa
