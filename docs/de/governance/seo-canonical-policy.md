---
description: AIMO SEO und Canonical-URL-Richtlinie - URL-Kanonisierungsstrategie für Suchmaschinen, Prüfer und externe Verweise.
---
<!-- aimo:translation_status=translated -->

# SEO & Canonical Policy

Diese Seite dokumentiert, wie der AIMO Standard URL-Kanonisierung für Suchmaschinen, Prüfer und externe Verweise verwaltet.

## Produktions- vs. Mirror-Sites

| Umgebung | URL | Rolle | Indexierbar |
|-------------|-----|------|-----------|
| **Produktion** | `https://standard.aimoaas.com/` | Kanonische Site für alle Zwecke | Ja |
| GitHub Pages | `https://billyrise.github.io/aimo-standard/` | Temporärer Mirror / CI-Vorschau | Nein (noindex) |

**Grundprinzip**: Produktion (`standard.aimoaas.com`) ist die maßgebliche URL. GitHub Pages dient als temporäres Backup/Mirror und sollte nicht in Auditberichten oder externen Verweisen zitiert werden.

## Canonical-URL-Strategie

### Wie Canonical URLs generiert werden

Der AIMO Standard verwendet [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) mit der folgenden Konfiguration:

```yaml
# mkdocs.yml
site_url: https://standard.aimoaas.com/
```

Diese `site_url`-Einstellung stellt sicher:

1. **`<link rel="canonical">`** — Jede generierte HTML-Seite enthält einen Canonical-Link zur Produktions-URL.
2. **`sitemap.xml`** — Alle URLs in der Sitemap verweisen auf Produktion.
3. **`robots.txt`** — Sitemap-Verweis zeigt auf Produktion.
4. **`hreflang`-Alternativen** — Sprachalternativen verwenden Produktions-URLs.

### Sprachspezifische Canonicals

| Sprache | URL-Muster | Beispiel |
|----------|-------------|---------|
| Englisch (Standard) | `https://standard.aimoaas.com/{X.Y.Z}/{path}` | `https://standard.aimoaas.com/{X.Y.Z}/governance/` |
| Japanisch | `https://standard.aimoaas.com/{X.Y.Z}/ja/{path}` | `https://standard.aimoaas.com/{X.Y.Z}/ja/governance/` |

Jede Sprachversion ist selbst-kanonisch und enthält `hreflang`-Alternativen zur anderen Sprache(n) plus `x-default` auf die englische Version zeigend.

### Versionierte Dokumentation und Canonicals

Der AIMO Standard verwendet [mike](https://github.com/jimporter/mike) für Dokumentationsversionierung mit `alias_type: redirect`:

| Version | URL-Muster | Canonical-Status | Indexierbar |
|---------|-------------|------------------|-----------|
| Versioniert (z.B. `0.0.1`) | `https://standard.aimoaas.com/0.0.1/` | Kanonisch für diese spezifische Version | Ja |
| `latest` (Alias) | `https://standard.aimoaas.com/latest/` | **Leitet weiter** zum aktuellen Release | Ja (über Ziel) |
| `dev` | `https://standard.aimoaas.com/dev/` | Nur Vorschau | **Nein** (noindex erzwungen) |

**Kritische Unterscheidungen:**

| Aspekt | `/X.Y.Z/` | `/latest/` | `/dev/` |
|--------|-----------|------------|---------|
| Inhalt | Eingefrorener Snapshot | Weiterleitung zu `/X.Y.Z/` | Main-Branch-Vorschau |
| Veränderlich | Nie | Zeiger wird bei Release aktualisiert | Kontinuierlich |
| Für Audits | **Ja (bevorzugt)** | Ja (löst zu eingefroren auf) | **Nie** |
| SEO | Indexiert | Indexiert über Ziel | noindex |

**Wie alias_type: redirect funktioniert:**

Anstatt Dateien zu kopieren, enthält `/latest/` Weiterleitungsseiten, die auf das aktuelle Release zeigen:

```html
<!-- /latest/index.html -->
<!-- Latest alias (redirect stub); canonical points to versioned snapshot -->
<meta http-equiv="refresh" content="0; url=../{X.Y.Z}/">
<link rel="canonical" href="https://standard.aimoaas.com/{X.Y.Z}/">
```

Dies stellt sicher:

1. **Keine Inhaltsabweichung** — `/latest/` kann nicht vom Release abweichen, auf das es zeigt.
2. **Kein doppelter Inhalt** — Suchmaschinen sehen eine kanonische Quelle.
3. **Atomare Updates** — Das Ändern des Alias aktualisiert alle Seiten gleichzeitig.

!!! info "Git-Tag vs. Site-Pfad"
    Git-Release-Tags verwenden das `v`-Präfix (z.B. `v0.0.1`), aber Site-Pfade lassen das `v` weg (z.B. `/0.0.1/`). Dies ist Standardpraxis für Dokumentationsversionierungstools wie mike.

## Prüferhinweise: Welche URL zitieren

Bei Zitierung des AIMO Standards in Auditberichten, Compliance-Dokumentation oder externen Verweisen:

### Empfohlene Zitierungs-URLs

| Anwendungsfall | Empfohlene URL |
|----------|-----------------|
| Aktuelle stabile Spezifikation | `https://standard.aimoaas.com/{X.Y.Z}/standard/current/` |
| Bestimmte Version (für Audit) | `https://standard.aimoaas.com/{X.Y.Z}/standard/current/` |
| Governance & Richtlinien | `https://standard.aimoaas.com/{X.Y.Z}/governance/` |
| Trust Package | `https://standard.aimoaas.com/{X.Y.Z}/governance/trust-package/` |

### NICHT zitieren

- ~~`https://billyrise.github.io/aimo-standard/`~~ — Temporärer Mirror, nicht kanonisch
- ~~`https://standard.aimoaas.com/dev/`~~ — Entwicklungsversion, änderbar

### Versionierte Zitierung für Unveränderlichkeit

Für formelle Audits, die unveränderliche Verweise erfordern, verwenden Sie versionierte Snapshot-URLs:

```
https://standard.aimoaas.com/1.0.0/standard/current/01-overview/
```

Versionierte Snapshots sind zum Release-Zeitpunkt eingefroren und ändern sich nicht.

!!! note "URL-Format"
    Site-Pfade verwenden Versionsnummern ohne das `v`-Präfix. Für Version `v1.0.0` verwenden Sie `/1.0.0/` in URLs.

## Technische Implementierung

### Generiertes HTML-Beispiel

Jede generierte HTML-Seite enthält Canonical- und hreflang-Tags im `<head>`:

```html
<!-- Canonical (zeigt immer auf Produktion) -->
<link rel="canonical" href="https://standard.aimoaas.com/{X.Y.Z}/governance/">

<!-- Sprachalternativen -->
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

Die Sitemap wird vom `mkdocs-static-i18n`-Plugin generiert und enthält:

- Alle Produktions-URLs
- `hreflang`-Alternativen für jede Sprache

## Noindex-Konfiguration

### `/dev/` (Vorschau) — Obligatorisches Noindex

Die `/dev/`-Version enthält unveröffentlichte Inhalte und MUSS noindex haben, um zu verhindern, dass:

- Suchmaschinen instabile Inhalte indexieren
- Benutzer `/dev/` über Suche finden und in Audits zitieren
- Verwirrung zwischen veröffentlichten und unveröffentlichten Inhalten entsteht

**Implementierung:**

Der `deploy-dev.yml`-Workflow injiziert ein noindex-Meta-Tag über Theme-Override in alle `/dev/`-Seiten:

```html
<!-- Nur in /dev/-Seiten injiziert -->
<meta name="robots" content="noindex, nofollow">
```

### GitHub Pages Mirror — Noindex

Bei Deployment auf GitHub Pages (die Mirror-Site unter `billyrise.github.io`) sollten alle Seiten noindex haben, um doppelte Indexierung zu verhindern:

```html
<meta name="robots" content="noindex, nofollow">
```

Dies stellt sicher, dass Suchmaschinen immer die Produktions-Canonical-URLs unter `standard.aimoaas.com` priorisieren.

## Verifizierung

Nach jedem Build können Sie Canonical-URLs verifizieren durch:

1. **Generiertes HTML inspizieren** — `site/`-Verzeichnis nach `mkdocs build` prüfen
2. **Browser DevTools verwenden** — `<head>`-Abschnitt auf deployen Seiten inspizieren
3. **Google Search Console** — Überwachen, welche URLs indexiert werden

Beispiel-Verifizierungsbefehl:

```bash
mkdocs build
grep -r 'rel="canonical"' site/ | head -5
```

Erwartete Ausgabe sollte Produktions-URLs zeigen, z.B.:

```
site/index.html:<link rel="canonical" href="https://standard.aimoaas.com/">
site/governance/index.html:<link rel="canonical" href="https://standard.aimoaas.com/governance/">
```

## Verwandte Dokumentation

- [Trust Package](../trust-package/) — Prüfungsbereite Materialien
- [Releases](../../releases/) — Versionshistorie und Changelog
- [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) — Versionsrichtlinie
