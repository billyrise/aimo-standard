---
description: Politica SEO e URL canonici AIMO - Strategia di canonicalizzazione URL per motori di ricerca, auditor e riferimenti esterni.
---

# SEO & Politica Canonica

Questa pagina documenta come lo Standard AIMO gestisce la canonicalizzazione degli URL per motori di ricerca, auditor e riferimenti esterni.

## Siti di Produzione vs Mirror

| Ambiente | URL | Ruolo | Indicizzabile |
|-------------|-----|------|-----------|
| **Produzione** | `https://standard.aimoaas.com/` | Sito canonico per tutti gli scopi | Sì |
| GitHub Pages | `https://billyrise.github.io/aimo-standard/` | Mirror temporaneo / anteprima CI | No (noindex) |

**Principio chiave**: Produzione (`standard.aimoaas.com`) è l'URL autorevole. GitHub Pages serve come backup/mirror temporaneo e non dovrebbe essere citato in report di audit o riferimenti esterni.

## Strategia degli URL Canonici

### Come Vengono Generati gli URL Canonici

Lo Standard AIMO utilizza [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) con la seguente configurazione:

```yaml
# mkdocs.yml
site_url: https://standard.aimoaas.com/
```

Questa impostazione `site_url` assicura:

1. **`<link rel="canonical">`** — Ogni pagina HTML generata include un link canonico che punta all'URL di Produzione.
2. **`sitemap.xml`** — Tutti gli URL nella sitemap referenziano Produzione.
3. **`robots.txt`** — Il riferimento alla sitemap punta a Produzione.
4. **Alternate `hreflang`** — Le versioni linguistiche alternative usano URL di Produzione.

### Canonici Specifici per Lingua

| Lingua | Pattern URL | Esempio |
|----------|-------------|---------|
| Inglese (default) | `https://standard.aimoaas.com/{X.Y.Z}/{path}` | `https://standard.aimoaas.com/{X.Y.Z}/governance/` |
| Giapponese | `https://standard.aimoaas.com/{X.Y.Z}/ja/{path}` | `https://standard.aimoaas.com/{X.Y.Z}/ja/governance/` |

Ogni versione linguistica è self-canonical e include alternate `hreflang` verso le altre lingue più `x-default` che punta alla versione inglese.

### Documentazione Versionata e Canonici

Lo Standard AIMO utilizza [mike](https://github.com/jimporter/mike) per il versionamento della documentazione con `alias_type: redirect`:

| Versione | Pattern URL | Stato Canonico | Indicizzabile |
|---------|-------------|------------------|-----------|
| Versionata (es. `0.0.1`) | `https://standard.aimoaas.com/0.0.1/` | Canonica per quella specifica versione | Sì |
| `latest` (alias) | `https://standard.aimoaas.com/latest/` | **Redirect** alla release corrente | Sì (tramite target) |
| `dev` | `https://standard.aimoaas.com/dev/` | Solo anteprima | **No** (noindex forzato) |

**Distinzioni critiche:**

| Aspetto | `/X.Y.Z/` | `/latest/` | `/dev/` |
|--------|-----------|------------|---------|
| Contenuto | Snapshot congelato | Redirect a `/X.Y.Z/` | Anteprima del branch main |
| Mutabile | Mai | Il puntatore si aggiorna al rilascio | Continuo |
| Per audit | **Sì (preferito)** | Sì (risolve a congelato) | **Mai** |
| SEO | Indicizzato | Indicizzato tramite target | noindex |

**Come funziona alias_type: redirect:**

Invece di copiare file, `/latest/` contiene pagine di redirect che puntano alla release corrente:

```html
<!-- /latest/index.html -->
<meta http-equiv="refresh" content="0; url=../0.0.1/">
<link rel="canonical" href="https://standard.aimoaas.com/0.0.1/">
```

Questo assicura:

1. **Nessuna deriva del contenuto** — `/latest/` non può divergere dalla release a cui punta.
2. **Nessun contenuto duplicato** — I motori di ricerca vedono una sola fonte canonica.
3. **Aggiornamenti atomici** — Cambiare l'alias aggiorna tutte le pagine contemporaneamente.

!!! info "Tag Git vs. Percorso Sito"
    I tag delle release Git usano il prefisso `v` (es. `v0.0.1`), ma i percorsi del sito omettono la `v` (es. `/0.0.1/`). Questa è una pratica standard per strumenti di versionamento della documentazione come mike.

## Guida per Auditor: Quale URL Citare

Quando si cita lo Standard AIMO in report di audit, documentazione di conformità o riferimenti esterni:

### URL di Citazione Raccomandati

| Caso d'Uso | URL Raccomandato |
|----------|-----------------|
| Specifica stabile corrente | `https://standard.aimoaas.com/{X.Y.Z}/standard/current/` |
| Versione specifica (per audit) | `https://standard.aimoaas.com/{X.Y.Z}/standard/current/` |
| Governance & politiche | `https://standard.aimoaas.com/{X.Y.Z}/governance/` |
| Trust Package | `https://standard.aimoaas.com/{X.Y.Z}/governance/trust-package/` |

### NON Citare

- ~~`https://billyrise.github.io/aimo-standard/`~~ — Mirror temporaneo, non canonico
- ~~`https://standard.aimoaas.com/dev/`~~ — Versione di sviluppo, soggetta a modifiche

### Citazione Versionata per Immutabilità

Per audit formali che richiedono riferimenti immutabili, usare URL di snapshot versionati:

```
https://standard.aimoaas.com/1.0.0/standard/current/01-overview/
```

Gli snapshot versionati sono congelati al momento del rilascio e non cambieranno.

!!! note "Formato URL"
    I percorsi del sito usano numeri di versione senza il prefisso `v`. Per la versione `v1.0.0`, usare `/1.0.0/` negli URL.

## Implementazione Tecnica

### Esempio HTML Generato

Ogni pagina HTML generata include tag canonici e hreflang nel `<head>`:

```html
<!-- Canonico (punta sempre a Produzione) -->
<link rel="canonical" href="https://standard.aimoaas.com/{X.Y.Z}/governance/">

<!-- Alternative linguistiche -->
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

La sitemap è generata dal plugin `mkdocs-static-i18n` e include:

- Tutti gli URL di Produzione
- Alternate `hreflang` per ogni lingua

## Configurazione Noindex

### `/dev/` (Anteprima) — Noindex Obbligatorio

La versione `/dev/` contiene contenuto non rilasciato e DEVE avere noindex per prevenire:

- Che i motori di ricerca indicizzino contenuto instabile
- Che gli utenti trovino `/dev/` tramite ricerca e lo citino negli audit
- Confusione tra contenuto rilasciato e non rilasciato

**Implementazione:**

Il workflow `deploy-dev.yml` inietta un meta tag noindex in tutte le pagine `/dev/` tramite override del tema:

```html
<!-- Iniettato solo nelle pagine /dev/ -->
<meta name="robots" content="noindex, nofollow">
```

### Mirror GitHub Pages — Noindex

Quando si deploy su GitHub Pages (il sito mirror su `billyrise.github.io`), tutte le pagine dovrebbero avere noindex per prevenire l'indicizzazione duplicata:

```html
<meta name="robots" content="noindex, nofollow">
```

Questo assicura che i motori di ricerca diano sempre priorità agli URL canonici di Produzione su `standard.aimoaas.com`.

## Verifica

Dopo ogni build, puoi verificare gli URL canonici:

1. **Ispezionando l'HTML generato** — Controllare la directory `site/` dopo `mkdocs build`
2. **Usando i DevTools del browser** — Ispezionare la sezione `<head>` sulle pagine deployate
3. **Google Search Console** — Monitorare quali URL sono indicizzati

Comando di verifica di esempio:

```bash
mkdocs build
grep -r 'rel="canonical"' site/ | head -5
```

L'output atteso dovrebbe mostrare URL di Produzione, es.:

```
site/index.html:<link rel="canonical" href="https://standard.aimoaas.com/">
site/governance/index.html:<link rel="canonical" href="https://standard.aimoaas.com/governance/">
```

## Documentazione Correlata

- [Trust Package](trust-package.md) — Materiali pronti per l'auditor
- [Release](../../releases/) — Cronologia delle versioni e changelog
- [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) — Politica di versionamento
