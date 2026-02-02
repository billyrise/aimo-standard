---
description: Guide de citation du standard AIMO - Comment citer dans les articles académiques, rapports d'audit et propositions. Formats CITATION.cff et BibTeX.
---

# Comment citer

Cette page fournit des conseils de citation pour le standard AIMO dans les articles académiques, rapports d'audit et propositions.

## CITATION.cff

Le dépôt inclut un fichier [CITATION.cff](https://github.com/billyrise/aimo-standard/blob/main/CITATION.cff) suivant le standard Citation File Format.

GitHub affiche automatiquement les informations de citation à partir de ce fichier.

## Citation recommandée

### Forme courte (en ligne)

> AIMO Standard Contributors. (2026). AIMO Standard. https://standard.aimoaas.com/

### BibTeX

```bibtex
@software{aimo_standard,
  author = {{AIMO Standard Contributors}},
  title = {AIMO Standard},
  url = {https://standard.aimoaas.com/},
  version = {0.0.2},
  year = {2026}
}
```

### Style APA

> AIMO Standard Contributors. (2026). *AIMO Standard* (Version 0.0.2) [Software]. https://standard.aimoaas.com/

## Citation spécifique à une version

Lors de la citation d'une version spécifique :

> AIMO Standard Contributors. (2026). AIMO Standard v0.0.2. https://github.com/billyrise/aimo-standard/releases/tag/v0.0.2

## Documentation d'audit

Pour les rapports d'audit et la documentation de conformité :

| Champ | Valeur |
| ----- | ----- |
| Nom du standard | AIMO Standard |
| Version | (spécifiez la version utilisée, ex. v0.0.1) |
| Site web | https://standard.aimoaas.com/ |
| Dépôt | https://github.com/billyrise/aimo-standard |
| Versions | https://github.com/billyrise/aimo-standard/releases |

## Orientation sur les URL

### URL canoniques

Utilisez ces URL dans la documentation officielle :

| Objectif | URL |
| ------- | --- |
| Documentation la plus récente | https://standard.aimoaas.com/latest/ |
| Version spécifique | https://standard.aimoaas.com/0.0.2/ |
| Versions GitHub | https://github.com/billyrise/aimo-standard/releases |

!!! note "Format du chemin du site"
    Les chemins du site utilisent les numéros de version sans le préfixe `v`. Pour la version `v0.0.1`, utilisez `/0.0.1/` dans les URL.

### À éviter

- URL miroir GitHub Pages (temporaire)
- URL spécifiques aux branches (peuvent changer)

## Pages connexes

- [Package de confiance](trust-package.md) — Matériaux prêts pour les auditeurs
- [Gouvernance](index.md) — Gouvernance du projet
- [Licence](license.md) — Termes de licence
