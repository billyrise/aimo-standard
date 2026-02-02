---
description: Format et conventions de nommage du système de codes AIMO. Définit la structure des codes (XX-NNN), les états du cycle de vie, le versionnement et les politiques de dépréciation pour les codes de taxonomie.
---

# Codes

Cette page définit le format du système de codes AIMO, les conventions de nommage et la gestion du cycle de vie.

## Format de code

Tous les codes AIMO suivent le format : **`<PRÉFIXE>-<TOKEN>`**

| Composant | Description | Format | Exemple |
| --- | --- | --- | --- |
| `<PRÉFIXE>` | Identifiant de dimension | 2 lettres majuscules | FS, UC, DT |
| `-` | Séparateur | Tiret | - |
| `<TOKEN>` | Token unique dans la dimension | 3 chiffres (avec zéros) | 001, 002, 003 |

### Exemples

- `FS-001` - Périmètre fonctionnel : Productivité utilisateur final
- `UC-005` - Classe de cas d'usage : Génération de code
- `DT-004` - Type de données : Données personnelles
- `CH-003` - Canal : Plugin IDE
- `IM-002` - Mode d'intégration : SaaS intégré
- `RS-001` - Surface de risque : Fuite de données
- `OB-001` - Résultat/Bénéfice : Efficacité
- `EV-001` - Type de preuve : Enregistrement de demande

## Espaces de noms

La taxonomie AIMO utilise 8 espaces de noms de dimensions :

| ID | Nom | Préfixe | Nombre de codes |
| --- | --- | --- | --- |
| **FS** | Périmètre fonctionnel | `FS-` | 6 |
| **UC** | Classe de cas d'usage | `UC-` | 30 |
| **DT** | Type de données | `DT-` | 10 |
| **CH** | Canal | `CH-` | 8 |
| **IM** | Mode d'intégration | `IM-` | 7 |
| **RS** | Surface de risque | `RS-` | 8 |
| **OB** | Résultat / Bénéfice | `OB-` | 7 |
| **EV** | Type de preuve | `EV-` | 15 |

**Total : 91 codes sur 8 dimensions**

### Règles d'espace de noms

1. **Le préfixe est fixe** : Le préfixe de dimension à deux lettres (FS, UC, etc.) est permanent et ne changera jamais.
2. **Zéros de remplissage** : Les tokens sont toujours à 3 chiffres, avec zéros de remplissage (ex. `001` pas `1`).
3. **Attribution séquentielle** : Les nouveaux codes reçoivent le prochain numéro disponible dans une dimension.
4. **Pas de réutilisation** : Les codes supprimés ne sont jamais réattribués à des significations différentes.

## Règles de stabilité

La stabilité des codes est un principe critique pour la traçabilité d'audit.

### Immutabilité des ID

- **Les ID de code sont immutables** — une fois attribué, un ID de code ne change jamais de signification
- Un code comme `UC-001` signifiera toujours "Q&R général" pendant tout son cycle de vie
- Si la signification doit changer, un nouveau code est créé à la place

### Politique de non-réutilisation

- Les codes dépréciés ou supprimés ne sont **jamais réattribués** à des significations différentes
- Cela assure que les preuves historiques restent valides et traçables
- Exemple : Si `UC-010` est déprécié, un nouveau cas d'usage obtient `UC-031` (pas `UC-010`)

### Dépréciation avant suppression

- Les codes doivent être marqués `deprecated` pendant au moins une version MINEURE avant suppression
- La suppression ne se produit que lors d'incréments de version MAJEURE
- Voir la section [Cycle de vie](#cycle-de-vie) pour les détails

## Utilisation

### Dimensions requises

Pour chaque système IA ou cas d'usage, vous DEVEZ spécifier au moins un code de chaque dimension requise :

| Dimension | Sélection | Notes |
| --- | --- | --- |
| FS | Exactement 1 | Fonction métier primaire |
| UC | 1 ou plus | Types de tâches effectuées |
| DT | 1 ou plus | Classifications de données |
| CH | 1 ou plus | Canaux d'accès |
| IM | Exactement 1 | Mode d'intégration |
| RS | 1 ou plus | Catégories de risques |
| EV | 1 ou plus | Types de preuves |

### Dimensions optionnelles

| Dimension | Sélection | Notes |
| --- | --- | --- |
| OB | 0 ou plus | Bénéfices attendus (optionnel) |

### Composition de codes

Lors de la documentation d'un système IA, les codes de plusieurs dimensions sont combinés. La **priorité de composition** détermine l'ordre lors de la liste des codes :

1. FS (Périmètre fonctionnel)
2. UC (Classe de cas d'usage)
3. DT (Type de données)
4. CH (Canal)
5. IM (Mode d'intégration)
6. RS (Surface de risque)
7. OB (Résultat / Bénéfice)
8. EV (Type de preuve)

**Exemple de composition :**

```
FS: FS-001
UC: UC-001, UC-002
DT: DT-002, DT-004
CH: CH-001
IM: IM-002
RS: RS-001, RS-003
OB: OB-001
EV: EV-001, EV-002
```

## Cycle de vie

### Valeurs de statut

| Statut | Description | Comportement du validateur |
| --- | --- | --- |
| `active` | Actuellement valide et en usage | Accepté |
| `deprecated` | Toujours valide mais prévu pour suppression | Accepté avec avertissement |
| `removed` | Plus valide ; ne pas utiliser | Rejeté |

### Champs de métadonnées de cycle de vie

Le dictionnaire suit le cycle de vie avec ces champs :

| Champ | Requis | Description | Exemple |
| --- | --- | --- | --- |
| `status` | Oui | Statut actuel | `active` |
| `introduced_in` | Oui | Version quand le code a été ajouté | `0.1.0` |
| `deprecated_in` | Non | Version quand marqué déprécié | `1.2.0` |
| `removed_in` | Non | Version quand supprimé | `2.0.0` |
| `replaced_by` | Non | Code(s) de remplacement | `UC-015` |
| `backward_compatible` | Oui | Si le changement casse l'usage existant | `true` |

### Règles de dépréciation

1. Les codes DOIVENT être marqués `deprecated` pendant au moins une version MINEURE avant suppression
2. Les codes dépréciés incluent la version `deprecated_in` et `replaced_by` si applicable
3. La suppression ne se produit que lors d'incréments de version MAJEURE
4. Les codes dépréciés restent valides pour la rétrocompatibilité pendant la période de dépréciation

**Exemple de chronologie :**

| Version | Statut | Action |
| --- | --- | --- |
| 0.1.0 | `active` | Code `UC-010` introduit |
| 1.2.0 | `deprecated` | Marqué déprécié, `replaced_by: UC-031` |
| 2.0.0 | `removed` | Plus accepté par le validateur |

### Versionnement

Les changements de codes suivent le [versionnement sémantique](./08-changelog.md) :

- **MAJEUR** : Suppression de code ou changements cassants
- **MINEUR** : Nouveaux codes ajoutés, codes dépréciés
- **PATCH** : Clarifications de définition uniquement (pas de changements structurels)

### Rétrocompatibilité

Le champ `backward_compatible` indique si un changement casse l'usage existant :

| Valeur | Signification |
| --- | --- |
| `true` | Les preuves existantes utilisant ce code restent valides |
| `false` | Les preuves existantes peuvent nécessiter des mises à jour (changement de version MAJEURE) |

## Validation

Le validateur vérifie :

1. Toutes les dimensions requises ont au moins un code
2. Les dimensions à sélection unique ont exactement un code
3. Tous les codes existent dans le dictionnaire de taxonomie actuel
4. Le format de code correspond au pattern `<PRÉFIXE>-<TOKEN>` (ex. `UC-001`)
5. Les codes dépréciés sont signalés avec des avertissements

Voir [Validateur](./07-validator.md) pour les détails d'implémentation.

## Référence SSOT

!!! info "Source de vérité"
    La définition faisant autorité est `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv`. Cette page est explicative. Voir [Guide de localisation](../../contributing/localization.md) pour les flux de travail de mise à jour.

## Pages connexes

- [Taxonomie](./03-taxonomy.md) - Définitions complètes des dimensions
- [Dictionnaire](./05-dictionary.md) - Listes complètes de codes et définitions de colonnes
- [Validateur](./07-validator.md) - Règles de validation
- [Changelog](./08-changelog.md) - Historique des versions
