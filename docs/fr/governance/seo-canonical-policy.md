---
description: Politique SEO et URL canoniques AIMO - Stratégie de canonicalisation des URL pour les moteurs de recherche, auditeurs et références externes.
---
<!-- aimo:translation_status=translated -->

# Politique SEO et canonique

Cette page documente comment le standard AIMO gère la canonicalisation des URL pour les moteurs de recherche, auditeurs et références externes.

## Sites de production vs miroir

| Environnement | URL | Rôle | Indexable |
|-------------|-----|------|-----------|
| **Production** | `https://standard.aimoaas.com/` | Site canonique pour tous les usages | Oui |
| GitHub Pages | `https://billyrise.github.io/aimo-standard/` | Miroir temporaire / aperçu CI | Non (noindex) |

**Principe clé** : Production (`standard.aimoaas.com`) est l'URL faisant autorité. GitHub Pages sert de backup/miroir temporaire et ne doit pas être cité dans les rapports d'audit ou références externes.

## Stratégie d'URL canoniques

### Comment les URL canoniques sont générées

Le standard AIMO utilise [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) avec la configuration suivante :

```yaml
# mkdocs.yml
site_url: https://standard.aimoaas.com/
```

Ce paramètre `site_url` assure :

1. **`<link rel="canonical">`** — Chaque page HTML générée inclut un lien canonique pointant vers l'URL de production.
2. **`sitemap.xml`** — Toutes les URL dans le sitemap référencent Production.
3. **`robots.txt`** — La référence sitemap pointe vers Production.
4. **Alternates `hreflang`** — Les alternates de langue utilisent les URL de Production.

### Canoniques spécifiques aux langues

| Langue | Pattern d'URL | Exemple |
|----------|-------------|---------|
| Anglais (défaut) | `https://standard.aimoaas.com/{X.Y.Z}/{path}` | `https://standard.aimoaas.com/{X.Y.Z}/governance/` |
| Japonais | `https://standard.aimoaas.com/{X.Y.Z}/ja/{path}` | `https://standard.aimoaas.com/{X.Y.Z}/ja/governance/` |

Chaque version de langue est auto-canonique et inclut des alternates `hreflang` vers les autres langues plus `x-default` pointant vers la version anglaise.

### Documentation versionnée et canoniques

Le standard AIMO utilise [mike](https://github.com/jimporter/mike) pour le versionnement de la documentation avec `alias_type: redirect` :

| Version | Pattern d'URL | Statut canonique | Indexable |
|---------|-------------|------------------|-----------|
| Versionnée (ex. `0.0.1`) | `https://standard.aimoaas.com/0.0.1/` | Canonique pour cette version spécifique | Oui |
| `latest` (alias) | `https://standard.aimoaas.com/latest/` | **Redirige** vers la version actuelle | Oui (via cible) |
| `dev` | `https://standard.aimoaas.com/dev/` | Aperçu uniquement | **Non** (noindex forcé) |

**Distinctions critiques :**

| Aspect | `/X.Y.Z/` | `/latest/` | `/dev/` |
|--------|-----------|------------|---------|
| Contenu | Instantané figé | Redirection vers `/X.Y.Z/` | Aperçu branche main |
| Mutable | Jamais | Le pointeur se met à jour lors des releases | Continu |
| Pour audits | **Oui (préféré)** | Oui (résout vers figé) | **Jamais** |
| SEO | Indexé | Indexé via cible | noindex |

**Comment fonctionne alias_type: redirect :**

Au lieu de copier les fichiers, `/latest/` contient des pages de redirection pointant vers la version actuelle :

```html
<!-- /latest/index.html -->
<!-- Latest alias (redirect stub); canonical points to versioned snapshot -->
<meta http-equiv="refresh" content="0; url=../{X.Y.Z}/">
<link rel="canonical" href="https://standard.aimoaas.com/{X.Y.Z}/">
```

Cela assure :

1. **Pas de dérive de contenu** — `/latest/` ne peut pas diverger de la version vers laquelle elle pointe.
2. **Pas de contenu dupliqué** — Les moteurs de recherche voient une source canonique.
3. **Mises à jour atomiques** — Changer l'alias met à jour toutes les pages d'un coup.

!!! info "Tag Git vs chemin du site"
    Les tags de release Git utilisent le préfixe `v` (ex. `v0.0.1`), mais les chemins du site omettent le `v` (ex. `/0.0.1/`). C'est une pratique standard pour les outils de versionnement de documentation comme mike.

## Conseils aux auditeurs : quelle URL citer

Lors de la citation du standard AIMO dans les rapports d'audit, documentation de conformité ou références externes :

### URL de citation recommandées

| Cas d'usage | URL recommandée |
|----------|-----------------|
| Spécification stable actuelle | `https://standard.aimoaas.com/{X.Y.Z}/standard/current/` |
| Version spécifique (pour audit) | `https://standard.aimoaas.com/{X.Y.Z}/standard/current/` |
| Gouvernance et politiques | `https://standard.aimoaas.com/{X.Y.Z}/governance/` |
| Package de confiance | `https://standard.aimoaas.com/{X.Y.Z}/governance/trust-package/` |

### Ne PAS citer

- ~~`https://billyrise.github.io/aimo-standard/`~~ — Miroir temporaire, non canonique
- ~~`https://standard.aimoaas.com/dev/`~~ — Version de développement, susceptible de changer

### Citation versionnée pour l'immutabilité

Pour les audits formels nécessitant des références immutables, utilisez les URL d'instantanés versionnés :

```
https://standard.aimoaas.com/1.0.0/standard/current/01-overview/
```

Les instantanés versionnés sont figés au moment de la release et ne changeront pas.

!!! note "Format d'URL"
    Les chemins du site utilisent les numéros de version sans le préfixe `v`. Pour la version `v1.0.0`, utilisez `/1.0.0/` dans les URL.

## Implémentation technique

### Exemple HTML généré

Chaque page HTML générée inclut des tags canoniques et hreflang dans le `<head>` :

```html
<!-- Canonique (pointe toujours vers Production) -->
<link rel="canonical" href="https://standard.aimoaas.com/{X.Y.Z}/governance/">

<!-- Alternates de langue -->
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

Le sitemap est généré par le plugin `mkdocs-static-i18n` et inclut :

- Toutes les URL de Production
- Alternates `hreflang` pour chaque langue

## Configuration noindex

### `/dev/` (aperçu) — Noindex obligatoire

La version `/dev/` contient du contenu non publié et DOIT avoir noindex pour empêcher :

- Les moteurs de recherche d'indexer du contenu instable
- Les utilisateurs de trouver `/dev/` via la recherche et de le citer dans des audits
- La confusion entre contenu publié et non publié

**Implémentation :**

Le workflow `deploy-dev.yml` injecte un meta tag noindex dans toutes les pages `/dev/` via le override de thème :

```html
<!-- Injecté dans les pages /dev/ uniquement -->
<meta name="robots" content="noindex, nofollow">
```

### Miroir GitHub Pages — Noindex

Lors du déploiement sur GitHub Pages (le site miroir à `billyrise.github.io`), toutes les pages doivent avoir noindex pour empêcher l'indexation dupliquée :

```html
<meta name="robots" content="noindex, nofollow">
```

Cela assure que les moteurs de recherche priorisent toujours les URL canoniques de Production à `standard.aimoaas.com`.

## Vérification

Après chaque build, vous pouvez vérifier les URL canoniques en :

1. **Inspectant le HTML généré** — Vérifiez le répertoire `site/` après `mkdocs build`
2. **Utilisant les DevTools du navigateur** — Inspectez la section `<head>` sur les pages déployées
3. **Google Search Console** — Surveillez quelles URL sont indexées

Exemple de commande de vérification :

```bash
mkdocs build
grep -r 'rel="canonical"' site/ | head -5
```

La sortie attendue devrait montrer les URL de Production, ex. :

```
site/index.html:<link rel="canonical" href="https://standard.aimoaas.com/">
site/governance/index.html:<link rel="canonical" href="https://standard.aimoaas.com/governance/">
```

## Documentation connexe

- [Package de confiance](../trust-package/) — Matériaux prêts pour les auditeurs
- [Versions](../../releases/) — Historique des versions et changelog
- [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) — Politique de versionnement
