---
description: Dictionnaire AIMO - Liste faisant autorité de 91 codes de taxonomie sur 8 dimensions. Définitions complètes, libellés et informations de cycle de vie pour la classification IA.
---

# Dictionnaire

Le dictionnaire AIMO est la liste faisant autorité de tous les codes valides dans la taxonomie. Il fournit les définitions complètes pour chaque code incluant les libellés, descriptions et informations de cycle de vie.

## Qu'est-ce que le dictionnaire

Le dictionnaire fournit un ensemble complet et lisible par machine de tous les codes de taxonomie AIMO. Il contient :

- Tous les 91 codes sur 8 dimensions
- Libellés et définitions (avec traductions dans les packs de langue)
- Métadonnées de cycle de vie (statut, version d'introduction, dépréciation, suppression)
- Notes de portée et exemples d'utilisation des codes

Le dictionnaire permet :

1. **Modèles de preuves** : Les codes sont utilisés dans les modèles EV pour classifier les systèmes IA
2. **Validateur** : Le validateur vérifie que tous les codes existent dans le dictionnaire
3. **Carte de couverture** : Les codes permettent la correspondance avec les cadres et réglementations externes

!!! info "Source unique de vérité (SSOT)"
    Le SSOT pour le dictionnaire est :

    - **Structure** : `data/taxonomy/canonical.yaml` (codes, statut, cycle de vie)
    - **Traductions** : `data/taxonomy/i18n/*.yaml` (libellés, définitions par langue)

    Les fichiers CSV sont des **artefacts générés** pour la distribution. Voir [Versions](../../../releases/) pour les téléchargements.

## Schéma de colonnes

Le dictionnaire canonique utilise **18 colonnes** (structure neutre linguistiquement) :

### Colonnes d'identification (5)

| # | Colonne | Requis | Description | Exemple |
| --- | --- | --- | --- | --- |
| 1 | `standard_id` | Oui | Identifiant du standard | `AIMO-STD` |
| 2 | `standard_version` | Oui | Format SemVer | `0.1.0` |
| 3 | `dimension_id` | Oui | ID de dimension à deux lettres | `FS`, `UC`, `DT` |
| 4 | `dimension_name` | Oui | Nom de dimension | `Functional Scope` |
| 5 | `code` | Oui | Code complet | `UC-001` |

### Colonnes de libellé et définition (4)

| # | Colonne | Requis | Description | Exemple |
| --- | --- | --- | --- | --- |
| 6 | `label` | Oui | Libellé du code (max 50 car.) | `General Q&A` |
| 7 | `definition` | Oui | Définition du code (1-2 phrases) | `General question answering...` |
| 8 | `scope_notes` | Non | Clarification de portée d'usage | `Low to medium risk...` |
| 9 | `examples` | Non | Exemples séparés par pipe | `chatbot\|recommendation` |

!!! note "Traductions"
    Le modèle de données canonique sépare les traductions dans des packs de langue (`data/taxonomy/i18n/*.yaml`). Chaque pack de langue fournit des valeurs localisées `dimension_name`, `label` et `definition`. Voir [Guide de localisation](../../../contributing/localization/) pour les détails.

### Colonnes de cycle de vie (6)

| # | Colonne | Requis | Description | Exemple |
| --- | --- | --- | --- | --- |
| 10 | `status` | Oui | `active`, `deprecated`, `removed` | `active` |
| 11 | `introduced_in` | Oui | Version lors de l'ajout | `0.1.0` |
| 12 | `deprecated_in` | Non | Version lors de la dépréciation | `1.2.0` |
| 13 | `removed_in` | Non | Version lors de la suppression | `2.0.0` |
| 14 | `replaced_by` | Non | Code de remplacement | `UC-015` |
| 15 | `backward_compatible` | Oui | `true` ou `false` | `true` |

### Colonnes de gouvernance (3)

| # | Colonne | Requis | Description | Exemple |
| --- | --- | --- | --- | --- |
| 16 | `references` | Non | Références externes | ISO/IEC 42001 |
| 17 | `owner` | Non | Partie responsable | `AIMO WG` |
| 18 | `last_reviewed_date` | Non | Dernière revue (AAAA-MM-JJ) | `2026-01-19` |

## Entrées initiales

La version actuelle du dictionnaire est **v0.1.0** et contient :

| Dimension | Nom | Codes actifs | Dépréciés | Total |
| --- | --- | --- | --- | --- |
| FS | Périmètre fonctionnel | 6 | 0 | 6 |
| UC | Classe de cas d'usage | 30 | 0 | 30 |
| DT | Type de données | 10 | 0 | 10 |
| CH | Canal | 8 | 0 | 8 |
| IM | Mode d'intégration | 7 | 0 | 7 |
| RS | Surface de risque | 8 | 0 | 8 |
| OB | Résultat / Bénéfice | 7 | 0 | 7 |
| LG | Type Log/Événement | 15 | 0 | 15 |
| **Total** | | **91** | **0** | **91** |

!!! note "Listes complètes de codes"
    La liste complète des 91 codes est disponible dans les artefacts CSV générés. Cette page de documentation fournit les définitions de colonnes et les conseils d'utilisation. Pour les définitions détaillées des codes :

    - **Téléchargement** : Voir [Versions](../../../releases/) pour les fichiers CSV par langue
    - **CSV par langue** : `artifacts/taxonomy/current/{lang}/taxonomy_dictionary.csv`
    - **CSV hérité mixte EN/JA** : `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` (figé, pour rétrocompatibilité uniquement)

## Politique de mise à jour

### Ajout de nouveaux codes

1. Attribuez le prochain numéro disponible dans la dimension (ex. `UC-031` après `UC-030`)
2. Définissez `status` à `active`
3. Définissez `introduced_in` à la version actuelle
4. Définissez `backward_compatible` à `true`
5. Fournissez libellé et définition (ajoutez les traductions aux packs de langue)

### Modification de codes existants

| Type de changement | Autorisé | Impact de version |
| --- | --- | --- |
| Clarification de définition | Oui | PATCH |
| Mise à jour de notes de portée | Oui | PATCH |
| Changement de libellé (signification préservée) | Oui | MINEUR |
| Changement de signification | Non | Créer un nouveau code à la place |

### Dépréciation de codes

1. Définissez `status` à `deprecated`
2. Définissez `deprecated_in` à la version actuelle
3. Définissez `replaced_by` au nouveau code (si applicable)
4. Le code reste fonctionnel pour la rétrocompatibilité
5. Documentez la raison dans scope_notes

### Suppression de codes

1. Dépréciez pendant au moins une version MINEURE d'abord
2. Définissez `status` à `removed`
3. Définissez `removed_in` à la version MAJEURE actuelle
4. Le code n'est plus valide pour les nouvelles preuves

### Politique de compatibilité

| Action | Impact de version | Rétrocompatible |
| --- | --- | --- |
| Ajouter un nouveau code | MINEUR | Oui |
| Déprécier un code | MINEUR | Oui |
| Clarifier une définition | PATCH | Oui |
| Supprimer un code | MAJEUR | Non |
| Changer la signification d'un code | Non autorisé | - |

## Comment utiliser

### Dans les modèles de preuves

Chaque modèle EV inclut un tableau de codes à 8 dimensions :

```markdown
## Codes AIMO (8 dimensions)

| Dimension | Code(s) | Libellé |
| --- | --- | --- |
| **FS** | `FS-001` | Productivité utilisateur final |
| **UC** | `UC-001`, `UC-002` | Q&R général, Résumé |
| **DT** | `DT-002`, `DT-004` | Interne, Données personnelles |
| **CH** | `CH-001` | Interface web |
| **IM** | `IM-002` | SaaS intégré |
| **RS** | `RS-001`, `RS-003` | Fuite de données, Violation de conformité |
| **OB** | `OB-001` | Efficacité |
| **LG** | `LG-001`, `LG-002` | Enregistrement de demande, Enregistrement de revue/approbation |
```

### Dans le validateur

Le validateur vérifie :

1. Tous les codes référencés dans les preuves existent dans le dictionnaire
2. Le format de code correspond au pattern attendu (`PRÉFIXE-###`)
3. Les codes dépréciés déclenchent des avertissements
4. Les codes supprimés sont rejetés

### Directives d'extension

Les organisations PEUVENT étendre le dictionnaire avec des codes personnalisés :

**Préfixe d'extension :**

```
X-<ORG>-<DIM>-<TOKEN>
```

Exemple : `X-ACME-UC-901` pour le code de cas d'usage personnalisé d'ACME Corporation.

**Règles d'extension :**

1. Les codes personnalisés ne DOIVENT PAS entrer en conflit avec les codes standard
2. Les codes personnalisés DEVRAIENT être documentés dans un dictionnaire d'extension local
3. Lors de l'échange de preuves avec des parties externes, utilisez uniquement les codes standard

## Téléchargements

Voir [Versions](../../../releases/) pour les packages téléchargeables contenant le dictionnaire et les fichiers associés.

## Pages connexes

- [Taxonomie](../03-taxonomy/) - Définitions de dimensions et tableaux de codes
- [Codes](../04-codes/) - Format de code, nommage et cycle de vie
- [Modèles de preuves](../06-ev-template/) - Comment les codes sont utilisés dans les modèles
- [Validateur](../07-validator/) - Règles de validation des codes
- [Changelog](../08-changelog/) - Historique des versions
