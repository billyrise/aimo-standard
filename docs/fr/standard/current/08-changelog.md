---
description: Changelog et politique de versionnement du standard AIMO. Documente l'historique des versions, les règles de versionnement sémantique et les conseils de migration entre versions.
---

# Changelog

Cette section documente la politique de versionnement et l'historique des changements pour le standard AIMO.

## Politique de versionnement

Le standard AIMO suit le [versionnement sémantique](https://semver.org/) (SemVer) :

### Format de version : MAJEUR.MINEUR.PATCH

| Type de changement | Incrément de version | Exemples |
| --- | --- | --- |
| **MAJEUR** | X.0.0 | Changements de schéma cassants, suppression de code, changements de champs requis |
| **MINEUR** | 0.X.0 | Nouveaux codes, nouveaux champs optionnels, nouvelles dimensions (optionnelles) |
| **PATCH** | 0.0.X | Corrections de documentation, clarifications de définitions, corrections de bugs du validateur |

### Changements cassants vs compatibles

**Changements cassants (MAJEUR) :**

- Suppression de codes (après période de dépréciation)
- Changements de champs requis dans les schémas
- Changements structurels qui invalident les documents existants
- Changements de patterns de format de code

**Changements rétrocompatibles (MINEUR) :**

- Ajout de nouveaux codes aux dimensions existantes
- Ajout de nouveaux champs optionnels aux schémas
- Ajout de nouvelles dimensions optionnelles
- Ajout de nouveaux modèles de preuves

**Changements non cassants (PATCH) :**

- Corrections de documentation
- Clarification de définitions existantes
- Améliorations de traduction
- Corrections de bugs du validateur

## Politique de dépréciation

### Processus de dépréciation

1. **Marquer comme déprécié** : Le code ou la fonctionnalité est marqué(e) avec `status: deprecated` et `deprecated_in: X.Y.Z`
2. **Période de dépréciation** : Au moins une version MINEURE doit passer avant la suppression
3. **Fournir un remplacement** : Si applicable, `replaced_by` indique le remplacement
4. **Supprimer en MAJEUR** : La suppression se produit dans la prochaine version MAJEURE

### Exemple de cycle de vie

```
v0.0.1: FS-007 introduit (status: active)
v0.1.0: FS-007 déprécié (status: deprecated, replaced_by: FS-008)
v0.2.0: FS-007 toujours disponible avec avertissement de dépréciation
v1.0.0: FS-007 supprimé (status: removed)
```

### Utilisation de codes dépréciés

- Les codes dépréciés restent valides pour la validation
- Le validateur DEVRAIT émettre un avertissement pour les codes dépréciés
- Les nouvelles implémentations DEVRAIENT utiliser les codes de remplacement
- Les documents existants PEUVENT continuer à utiliser les codes dépréciés jusqu'à la migration

## Artefacts de version

Chaque version officielle inclut :

| Artefact | Description |
| --- | --- |
| Instantané de site versionné | `https://standard.aimoaas.com/0.0.1/` |
| Spécification PDF | `trust_package.pdf` |
| Package d'actifs (ZIP) | Schémas, modèles, dictionnaire |
| Checksums | Hachages SHA-256 pour l'intégrité |
| Changelog | Ce document |

## Historique des changements

### Non publié (corrections namespace et normatif)

**Résumé :** Résolution de la collision des codes EV, clarification EV (index) vs Evidence Pack (payload), durcissement /dev contre la citation erronée en audit. Types de document Evidence Pack : EP-01..EP-07 ; Taxonomy EV reste pour les types d'événement. Relation normatif EV↔Evidence Pack documentée. Bannière et canonical pour /dev.

### Version 0.0.1 (2026-02-02)

**Résumé :** Version initiale du standard AIMO avec système de codes à 8 dimensions, modèles de pack de preuves et documentation complète de gouvernance.

#### Ajouté

**Système de codes (8 dimensions)**

| Dimension | Codes ajoutés | Description |
| --- | --- | --- |
| FS | FS-001 à FS-006 | Périmètre fonctionnel |
| UC | UC-001 à UC-010 | Classe de cas d'usage |
| DT | DT-001 à DT-008 | Type de données |
| CH | CH-001 à CH-006 | Canal |
| IM | IM-001 à IM-005 | Mode d'intégration |
| RS | RS-001 à RS-005 | Surface de risque |
| OB | OB-001 à OB-005 | Résultat / Bénéfice |
| LG | LG-001 à LG-015 | Type de log/registre |

**Schémas**

- `taxonomy_pack.schema.json` : Définition de pack de taxonomie
- `changelog.schema.json` : Entrées de changelog
- `evidence_pack_manifest.schema.json` : Manifestes de pack de preuves
- `shadow-ai-discovery.schema.json` : Preuves de découverte de Shadow AI
- `agent-activity.schema.json` : Preuves d'activité des agents

**Modèles de pack de preuves (MVP)**

- EV-01 : Vue d'ensemble système
- EV-02 : Flux de données
- EV-03 : Inventaire IA
- EV-04 : Évaluation des risques et impacts
- EV-05 : Contrôles et approbations
- EV-06 : Journalisation et surveillance
- EV-07 : Gestion des incidents et exceptions

**Documentation**

- Documentation de taxonomie avec définitions à 8 dimensions
- Spécification du format du système de codes
- Spécification du format CSV du dictionnaire
- Politique de versionnement et de changement
- Exigences MVP du validateur
- Protocole de surveillance humaine
- Carte de couverture (ISO 42001, NIST AI RMF, EU AI Act, ISMS)
- Package de confiance

#### Rétrocompatibilité

C'est la version initiale ; pas de préoccupations de rétrocompatibilité.

---

## Changelog lisible par machine

Un changelog lisible par machine est disponible :

- `changelog/changelog.json`

Ce fichier suit le schéma `changelog.schema.json` et peut être analysé programmatiquement.

## Références

- [Taxonomie](../03-taxonomy/) - Définitions des dimensions
- [Dictionnaire](../05-dictionary/) - Dictionnaire des codes
- [Politique de versionnement](../../../governance/) - Politique de versionnement (voir VERSIONING.md à la racine du dépôt)
