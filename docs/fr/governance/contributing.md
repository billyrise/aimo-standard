---
description: Guide de contribution au standard AIMO - Comment contribuer au code, à la documentation et aux traductions. Directives pour les issues et PR.
---

# Contribuer

Cette page fournit des directives pour contribuer au standard AIMO.

## Démarrage rapide

1. Forkez le dépôt
2. Créez une branche de fonctionnalité
3. Effectuez les modifications en suivant les directives ci-dessous
4. Exécutez les vérifications de qualité
5. Soumettez une pull request

## Principes clés

| Principe | Description |
| --------- | ----------- |
| L'anglais est canonique | Éditez d'abord `docs/en/`, puis mettez à jour `docs/ja/` |
| SSOT | Ce dépôt est la source unique de vérité |
| Pas de modifications manuelles des fichiers générés | Éditez les sources, régénérez, committez |
| Tous les changements via PR | Même les mainteneurs utilisent les pull requests |

## Vérifications de qualité

Avant de soumettre une PR, exécutez :

```bash
# Activez l'environnement virtuel
source .venv/bin/activate

# Exécutez les lints
python tooling/checks/lint_i18n.py
python tooling/checks/lint_schema.py
python tooling/audit/baseline_audit.py --check

# Construisez la documentation
mkdocs build --strict
```

## Types de changements

| Type | Exemples | Exigences de revue |
| ---- | -------- | ------------------- |
| Normatif | Changements de schéma, exigences | Mainteneur + discussion |
| Non-normatif | Fautes de frappe, clarifications | Approbation du mainteneur |
| i18n | Traductions | La structure doit correspondre à EN |
| Outillage | CI/CD, scripts | Approbation du mainteneur |

## Directives i18n

### Ordre de mise à jour

1. Éditez la source anglaise (`docs/en/...`)
2. Mettez à jour la traduction japonaise (`docs/ja/...`)
3. Exécutez `lint_i18n.py` pour vérifier la cohérence
4. Committez les deux ensemble

### Exigences de structure

- Mêmes noms de fichiers dans les deux langues
- Même hiérarchie de titres
- Même nombre de pages par section

## Liste de contrôle PR

Lors de la soumission d'une PR, vérifiez :

- [ ] Type de changement identifié (docs / schéma / exemples / outillage)
- [ ] Évaluation des changements cassants complétée
- [ ] i18n : EN et JA mis à jour ensemble (si applicable)
- [ ] Vérifications de qualité passées
- [ ] Issues liées référencées

## Changements cassants

Les changements cassants nécessitent :

1. Discussion dans une issue avant implémentation
2. Incrément de version selon [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)
3. Entrée de changelog avec guide de migration

## Mises à jour des déclarations de conformité

Pour ajouter ou modifier des déclarations de conformité :

1. Mettez à jour le YAML de la carte de couverture
2. Mettez à jour les pages de documentation correspondantes
3. Exécutez les tests du validateur
4. Documentez la justification de la correspondance

## Directives complètes

Voir [CONTRIBUTING.md](https://github.com/billyrise/aimo-standard/blob/main/CONTRIBUTING.md) pour le guide de niveau racine.

## Pages connexes

- [Gouvernance](index.md) — Gouvernance du projet
- [Guide de localisation](../contributing/localization.md) — Détails i18n
- [Périmètre de responsabilité](responsibility-boundary.md) — Ce que fournit AIMO
