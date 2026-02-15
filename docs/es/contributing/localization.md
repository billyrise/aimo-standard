---
description: Guía de localización de AIMO - estructura i18n, flujo de trabajo de mantenimiento y principios SSOT para documentación multilingüe.
---
<!-- aimo:translation_status=translated -->

# Guía de Localización

Esta página documenta la estructura de localización (i18n), flujo de trabajo de mantenimiento y principios SSOT (Single Source of Truth) para la documentación del AIMO Standard.

## Política de Pureza de Idioma

**Cada página de idioma debe contener solo el contenido de ese idioma.**

| Regla | Descripción |
| --- | --- |
| **Páginas EN** | No deben contener caracteres CJK ni referencias a columnas específicas de idioma (ej., sufijos `_ja`) |
| **Páginas JA** | No deben explicar terminología específica de EN como si fuera la estructura canónica |
| **Excepciones** | Listadas en `MIXED_LANGUAGE_ALLOWLIST` en `tooling/checks/lint_i18n.py` |

Esta política asegura:
1. Los lectores ven solo su idioma seleccionado
2. Agregar nuevos idiomas no requiere actualizar páginas existentes
3. CI puede detectar automáticamente violaciones

## Estructura de Idiomas

La documentación del AIMO Standard usa una **estructura i18n basada en carpetas**:

```
docs/
├── en/           # Inglés (canónico)
├── ja/           # Japonés (日本語)
├── es/           # Español (Español)
├── fr/           # Francés (Français)
├── de/           # Alemán (Deutsch)
├── pt/           # Portugués (Português)
├── it/           # Italiano (Italiano)
├── zh/           # Chino Simplificado (简体中文)
├── zh-TW/        # Chino Tradicional (繁體中文)
└── ko/           # Coreano (한국어)
```

- **El inglés es canónico**: La carpeta `docs/en/` es la fuente autoritativa para el contenido de documentación.
- **Otros idiomas reflejan la estructura**: Cada carpeta de idioma (`ja/`, etc.) mantiene la misma estructura de archivos que `en/`.
- **Mismos nombres de archivo**: Todos los idiomas usan extensión `.md` (sin sufijo de idioma en nombres de archivo).
- **Fallback a inglés**: Las traducciones faltantes automáticamente recurren al contenido en inglés.

## Modelo de Datos de Taxonomía

La taxonomía usa una **estructura canónica neutral al idioma** con paquetes de traducción separados:

```
data/
└── taxonomy/
    ├── canonical.yaml           # Neutral al idioma (códigos, estado, ciclo de vida)
    └── i18n/
        ├── en.yaml              # Etiquetas y definiciones en inglés
        ├── ja.yaml              # Etiquetas y definiciones en japonés
        └── {lang}.yaml          # Idiomas adicionales (plantilla vacía)
```

### Estructura Canónica (`canonical.yaml`)

Contiene datos neutrales al idioma:

- Identificadores de código (ej., `FS-001`, `UC-001`)
- Estado (`active`, `deprecated`, `removed`)
- Metadatos de ciclo de vida (`introduced_in`, `deprecated_in`, `removed_in`, `replaced_by`)
- Notas de alcance y ejemplos (en inglés, como referencias técnicas)

### Paquetes de Traducción (`i18n/*.yaml`)

Cada paquete de idioma contiene:

- Nombres de dimensión (ej., "Functional Scope")
- Etiquetas de código (ej., "End-user Productivity")
- Definiciones de código

**Fallback**: Si falta una traducción, el sistema usa inglés.

## Principio SSOT

AIMO usa una **arquitectura SSOT-first** para datos de taxonomía:

| Tipo de Activo | Ubicación SSOT | Descripción |
| --- | --- | --- |
| **Taxonomía (estructura)** | `data/taxonomy/canonical.yaml` | Estructura neutral al idioma (SSOT) |
| **Taxonomía (i18n)** | `data/taxonomy/i18n/*.yaml` | Traducciones por idioma (SSOT) |
| **Mapa de Cobertura** | `coverage_map/coverage_map.yaml` | Mapeo de framework a evidencia |
| **Esquemas** | `schemas/jsonschema/` | Esquemas de validación JSON |

### Archivos Derivados

Los siguientes archivos son **generados** desde el SSOT y NO deben editarse manualmente:

| Archivo | Generado Desde | Generador |
| --- | --- | --- |
| `artifacts/taxonomy/{version}/{lang}/taxonomy_dictionary.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_en.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_ja.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/code_system.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/dimensions_en_ja.md` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_dictionary.json` | canonical + i18n | `build_artifacts.py` |

### Códigos de Idioma (BCP47)

AIMO usa códigos de idioma BCP47:

| Código | Idioma | Estado |
| --- | --- | --- |
| `en` | Inglés | Canónico (fuente) |
| `ja` | Japonés (日本語) | Activo |
| `es` | Español (Español) | Activo |
| `fr` | Francés (Français) | Activo |
| `de` | Alemán (Deutsch) | Activo |
| `pt` | Portugués (Português) | Activo |
| `it` | Italiano (Italiano) | Activo |
| `zh` | Chino Simplificado (简体中文) | Activo |
| `zh-TW` | Chino Tradicional (繁體中文) | Activo |
| `ko` | Coreano (한국어) | Activo |

### Archivos CSV Legacy (Congelados)

Los archivos CSV legacy mixtos EN/JA en `source_pack/03_taxonomy/legacy/` están:

- **Congelados en 21 columnas** — no se agregarán nuevas columnas de idioma
- **Mantenidos para compatibilidad hacia atrás** — integraciones existentes pueden continuar usándolos
- **Aplicado por CI** — agregar `label_es`, `definition_de`, etc. fallará el build

Para nuevos idiomas, use los artefactos por idioma en `artifacts/taxonomy/{version}/{lang}/`.

## Seguimiento de Frescura de Traducción

AIMO usa un sistema de **Seguimiento de Frescura de Traducción** para mantener consistencia entre inglés (fuente) y contenido traducido.

### Cómo Funciona

1. Cada archivo traducido contiene metadatos que rastrean de qué versión de la fuente en inglés fue traducido
2. Cuando el contenido en inglés se actualiza, el sistema detecta traducciones desactualizadas
3. CI advierte sobre traducciones desactualizadas pero no bloquea (las traducciones pueden quedar atrás)

### Metadatos de Traducción

Los archivos traducidos incluyen metadatos en frontmatter:

```yaml
---
# TRANSLATION METADATA - DO NOT REMOVE
source_file: en/standard/current/01-overview.md
source_hash: abc123def456
translation_date: 2026-02-02
translator: human|machine|hybrid
translation_status: current|outdated|needs_review
---
```

### Usando la Herramienta de Sincronización

```bash
# Verificar todas las traducciones para frescura
python tooling/i18n/sync_translations.py --check

# Verificar idioma específico
python tooling/i18n/sync_translations.py --check --lang ja

# Generar reporte de traducción
python tooling/i18n/sync_translations.py --report

# Inicializar nuevo idioma (copiar EN como base)
python tooling/i18n/sync_translations.py --init-lang es

# Actualizar metadatos después de completar traducción
python tooling/i18n/sync_translations.py --update-meta docs/ja/index.md
```

Para especificación técnica detallada, consulte `tooling/i18n/TRANSLATION_SYNC_SPEC.md`.

## Flujos de Trabajo de Actualización

### Actualizaciones de Taxonomía (Nuevo Flujo de Trabajo SSOT-First)

1. Edite el SSOT en `data/taxonomy/`:
   - Cambios de estructura → `canonical.yaml`
   - Traducciones en inglés → `i18n/en.yaml`
   - Traducciones en japonés → `i18n/ja.yaml`
2. Ejecute validación: `python tooling/checks/lint_taxonomy_ssot.py`
3. Regenere todos los archivos derivados: `python tooling/taxonomy/build_artifacts.py --version current --langs en ja`
4. Actualice páginas de documentación según sea necesario
5. Haga commit de todos los cambios juntos

### Actualizaciones del Mapa de Cobertura

1. Edite `coverage_map/coverage_map.yaml` (el SSOT)
2. Actualice las tablas de página de framework correspondientes (`docs/en/coverage-map/*.md`)
3. Actualice traducciones al japonés (`docs/ja/coverage-map/*.md`)
4. Haga commit de todos los cambios juntos

### Actualizaciones de Documentación

1. Edite la fuente en inglés (`docs/en/...`)
2. Actualice traducciones según sea necesario (o márquelas para actualización posterior)
3. Ejecute `python tooling/i18n/sync_translations.py --check` para ver traducciones desactualizadas
4. Ejecute `python tooling/checks/lint_i18n.py` para verificar consistencia de encabezados
5. Ejecute `mkdocs build --strict` para verificar el build
6. Haga commit de todos los cambios juntos

!!! note "Prioridad de Traducción"
    No todas las traducciones necesitan actualizarse inmediatamente. Las páginas Nivel 1 (críticas) deben priorizarse:
    
    - `index.md`
    - `standard/current/*.md`
    - `governance/index.md`
    - `releases/`

## Agregar un Nuevo Idioma (5 Pasos)

Para agregar un nuevo idioma (ej., Español):

### Paso 1: Generar Paquete de Taxonomía

```bash
python tooling/taxonomy/build_i18n_taxonomy.py --add-lang es --lang-name "Español"
```

Crea `data/taxonomy/i18n/es.yaml` con referencias en inglés como comentarios.

### Paso 2: Crear Carpeta de Docs

```bash
mkdir -p docs/es && cp -r docs/en/* docs/es/
```

### Paso 3: Actualizar mkdocs.yml

```yaml
plugins:
  - i18n:
      languages:
        - locale: es
          name: Español
          build: true
```

### Paso 4: Traducir

- Traduzca `data/taxonomy/i18n/es.yaml`
- Traduzca archivos en `docs/es/`

### Paso 5: Verificar

```bash
python tooling/checks/lint_i18n.py && mkdocs build --strict
```

!!! success "Listo"
    El nuevo idioma está ahora disponible en `/dev/es/`

## Convenciones de Nomenclatura de Archivos

| Patrón | Ejemplo | Descripción |
| --- | --- | --- |
| `index.md` | `docs/en/governance/index.md` | Página de inicio de sección |
| `{tema}.md` | `docs/en/governance/trust-package.md` | Página de tema |
| `{NN}-{tema}.md` | `docs/en/standard/current/03-taxonomy.md` | Página de especificación numerada |

## Verificaciones de Calidad

Ejecute estas verificaciones antes de hacer commit:

```bash
# Estructura i18n, consistencia de encabezados y detección de frases obsoletas
python tooling/checks/lint_i18n.py

# Lints de esquema y manifiesto
python tooling/checks/lint_schema.py
python tooling/checks/lint_manifest.py

# Lints de SSOT de taxonomía
python tooling/checks/lint_taxonomy_ssot.py --required-langs en
python tooling/checks/lint_legacy_csv.py
python tooling/checks/lint_taxonomy_dictionary.py
python tooling/checks/lint_taxonomy_json.py

# Artefactos de taxonomía actualizados
python tooling/taxonomy/build_artifacts.py --check

# Verificación de build
mkdocs build --strict
```

## Páginas Relacionadas

- [Versiones](../../releases/) — Paquetes descargables
- [Gobernanza](../../governance/) — Gobernanza del proyecto
