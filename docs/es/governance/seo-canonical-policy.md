---
description: Política SEO y URL canónica de AIMO - Estrategia de canonicalización de URLs para motores de búsqueda, auditores y referencias externas.
---

# Política SEO y Canónica

Esta página documenta cómo AIMO Standard gestiona la canonicalización de URLs para motores de búsqueda, auditores y referencias externas.

## Sitios de Producción vs Mirror

| Entorno | URL | Rol | Indexable |
|-------------|-----|------|-----------|
| **Producción** | `https://standard.aimoaas.com/` | Sitio canónico para todos los propósitos | Sí |
| GitHub Pages | `https://billyrise.github.io/aimo-standard/` | Mirror temporal / preview de CI | No (noindex) |

**Principio clave**: Producción (`standard.aimoaas.com`) es la URL autoritativa. GitHub Pages sirve como backup/mirror temporal y no debe citarse en reportes de auditoría ni referencias externas.

## Estrategia de URL Canónica

### Cómo se Generan las URLs Canónicas

AIMO Standard usa [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) con la siguiente configuración:

```yaml
# mkdocs.yml
site_url: https://standard.aimoaas.com/
```

Esta configuración `site_url` asegura:

1. **`<link rel="canonical">`** — Cada página HTML generada incluye un enlace canónico apuntando a la URL de Producción.
2. **`sitemap.xml`** — Todas las URLs en el sitemap referencian Producción.
3. **`robots.txt`** — Referencia del sitemap apunta a Producción.
4. **Alternativas `hreflang`** — Alternativas de idioma usan URLs de Producción.

### Canónicos Específicos por Idioma

| Idioma | Patrón de URL | Ejemplo |
|----------|-------------|---------|
| Inglés (predeterminado) | `https://standard.aimoaas.com/{X.Y.Z}/{path}` | `https://standard.aimoaas.com/{X.Y.Z}/governance/` |
| Japonés | `https://standard.aimoaas.com/{X.Y.Z}/ja/{path}` | `https://standard.aimoaas.com/{X.Y.Z}/ja/governance/` |

Cada versión de idioma es auto-canónica e incluye alternativas `hreflang` a otro(s) idioma(s) más `x-default` apuntando a la versión en inglés.

### Documentación Versionada y Canónicos

AIMO Standard usa [mike](https://github.com/jimporter/mike) para versionado de documentación con `alias_type: redirect`:

| Versión | Patrón de URL | Estado Canónico | Indexable |
|---------|-------------|------------------|-----------|
| Versionada (ej., `0.0.1`) | `https://standard.aimoaas.com/0.0.1/` | Canónica para esa versión específica | Sí |
| `latest` (alias) | `https://standard.aimoaas.com/latest/` | **Redirige** a release actual | Sí (vía target) |
| `dev` | `https://standard.aimoaas.com/dev/` | Solo preview | **No** (noindex aplicado) |

**Distinciones críticas:**

| Aspecto | `/X.Y.Z/` | `/latest/` | `/dev/` |
|--------|-----------|------------|---------|
| Contenido | Snapshot congelado | Redirección a `/X.Y.Z/` | Preview de rama main |
| Mutable | Nunca | Puntero actualiza en release | Continuo |
| Para auditorías | **Sí (preferido)** | Sí (resuelve a congelado) | **Nunca** |
| SEO | Indexado | Indexado vía target | noindex |

**Cómo funciona alias_type: redirect:**

En lugar de copiar archivos, `/latest/` contiene páginas de redirección apuntando al release actual:

```html
<!-- /latest/index.html -->
<meta http-equiv="refresh" content="0; url=../0.0.1/">
<link rel="canonical" href="https://standard.aimoaas.com/0.0.1/">
```

Esto asegura:

1. **Sin deriva de contenido** — `/latest/` no puede divergir del release al que apunta.
2. **Sin contenido duplicado** — Los motores de búsqueda ven una fuente canónica.
3. **Actualizaciones atómicas** — Cambiar el alias actualiza todas las páginas a la vez.

!!! info "Git Tag vs. Ruta del Sitio"
    Los tags de release de Git usan prefijo `v` (ej., `v0.0.1`), pero las rutas del sitio omiten el `v` (ej., `/0.0.1/`). Esta es práctica estándar para herramientas de versionado de documentación como mike.

## Guía para Auditores: Qué URL Citar

Al citar AIMO Standard en reportes de auditoría, documentación de cumplimiento o referencias externas:

### URLs de Citación Recomendadas

| Caso de Uso | URL Recomendada |
|----------|-----------------|
| Especificación estable actual | `https://standard.aimoaas.com/{X.Y.Z}/standard/current/` |
| Versión específica (para auditoría) | `https://standard.aimoaas.com/{X.Y.Z}/standard/current/` |
| Gobernanza y políticas | `https://standard.aimoaas.com/{X.Y.Z}/governance/` |
| Paquete de Confianza | `https://standard.aimoaas.com/{X.Y.Z}/governance/trust-package/` |

### NO Citar

- ~~`https://billyrise.github.io/aimo-standard/`~~ — Mirror temporal, no canónico
- ~~`https://standard.aimoaas.com/dev/`~~ — Versión de desarrollo, sujeta a cambios

### Citación Versionada para Inmutabilidad

Para auditorías formales que requieren referencias inmutables, use URLs de snapshot versionado:

```
https://standard.aimoaas.com/1.0.0/standard/current/01-overview/
```

Los snapshots versionados están congelados en el momento del release y no cambiarán.

!!! note "Formato de URL"
    Las rutas del sitio usan números de versión sin el prefijo `v`. Para la versión `v1.0.0`, use `/1.0.0/` en URLs.

## Implementación Técnica

### Ejemplo de HTML Generado

Cada página HTML generada incluye tags canónicos y hreflang en el `<head>`:

```html
<!-- Canonical (siempre apunta a Producción) -->
<link rel="canonical" href="https://standard.aimoaas.com/{X.Y.Z}/governance/">

<!-- Alternativas de idioma -->
<link rel="alternate" hreflang="en" href="https://standard.aimoaas.com/{X.Y.Z}/governance/">
<link rel="alternate" hreflang="ja" href="https://standard.aimoaas.com/{X.Y.Z}/ja/governance/">
<link rel="alternate" hreflang="x-default" href="https://standard.aimoaas.com/{X.Y.Z}/governance/">
```

### robots.txt

```
User-agent: *
Allow: /

Sitemap: https://standard.aimoaas.com/sitemap.xml
```

### Sitemap

El sitemap es generado por el plugin `mkdocs-static-i18n` e incluye:

- Todas las URLs de Producción
- Alternativas `hreflang` para cada idioma

## Configuración Noindex

### `/dev/` (Preview) — Noindex Obligatorio

La versión `/dev/` contiene contenido no publicado y DEBE tener noindex para prevenir:

- Que motores de búsqueda indexen contenido inestable
- Que usuarios encuentren `/dev/` vía búsqueda y lo citen en auditorías
- Confusión entre contenido publicado y no publicado

**Implementación:**

El workflow `deploy-dev.yml` inyecta un meta tag noindex en todas las páginas `/dev/` vía override de tema:

```html
<!-- Inyectado en páginas /dev/ solamente -->
<meta name="robots" content="noindex, nofollow">
```

### Mirror de GitHub Pages — Noindex

Al desplegar a GitHub Pages (el sitio mirror en `billyrise.github.io`), todas las páginas deben tener noindex para prevenir indexación duplicada:

```html
<meta name="robots" content="noindex, nofollow">
```

Esto asegura que los motores de búsqueda siempre prioricen las URLs canónicas de Producción en `standard.aimoaas.com`.

## Verificación

Después de cada build, puede verificar URLs canónicas:

1. **Inspeccionando HTML generado** — Verifique directorio `site/` después de `mkdocs build`
2. **Usando DevTools del navegador** — Inspeccione sección `<head>` en páginas desplegadas
3. **Google Search Console** — Monitoree qué URLs están indexadas

Comando de verificación de ejemplo:

```bash
mkdocs build
grep -r 'rel="canonical"' site/ | head -5
```

La salida esperada debe mostrar URLs de Producción, ej.:

```
site/index.html:<link rel="canonical" href="https://standard.aimoaas.com/">
site/governance/index.html:<link rel="canonical" href="https://standard.aimoaas.com/governance/">
```

## Documentación Relacionada

- [Paquete de Confianza](trust-package.md) — Materiales listos para auditores
- [Versiones](../../releases/) — Historial de versiones y changelog
- [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) — Política de versiones
