---
description: Validateur AIMO - Assure que les packs de preuves sont conformes aux schémas du standard AIMO. Règles de validation, gestion des erreurs et implémentation de référence pour les vérifications de conformité.
---

# Validateur

Le validateur AIMO assure que les packs de preuves et artefacts associés sont conformes aux schémas et exigences du standard AIMO.

Voir aussi : [Protocole de surveillance humaine](../../governance/human-oversight-protocol.md) — limite de responsabilité pour la revue machine vs humaine.

## Le validateur en pratique

Pour un démarrage rapide en 30 secondes (installer, exécuter, interpréter la sortie), voir [Hub validateur](../../validator/index.md).

## Exigences MVP du validateur

Le validateur minimum viable DOIT effectuer les vérifications suivantes :

### 1. Validation des champs requis

Vérifier que tous les champs obligatoires sont présents :

| Artefact | Champs requis |
| --- | --- |
| Manifeste du pack de preuves | pack_id, pack_version, taxonomy_version, created_date, last_updated, codes, evidence_files |
| Objet codes | FS, UC, DT, CH, IM, RS, EV (OB optionnel) |
| Entrée de fichier de preuve | file_id (EP-01..EP-07), filename, title (ev_type / ev_codes optionnel) |

### 2. Validation des codes de dimension

Vérifier que chaque dimension requise a au moins un code :

| Dimension | Exigence |
| --- | --- |
| FS (Périmètre fonctionnel) | Exactement 1 code |
| UC (Classe de cas d'usage) | Au moins 1 code |
| DT (Type de données) | Au moins 1 code |
| CH (Canal) | Au moins 1 code |
| IM (Mode d'intégration) | Exactement 1 code |
| RS (Surface de risque) | Au moins 1 code |
| OB (Résultat / Bénéfice) | Optionnel (0 ou plus) |
| EV (Type de preuve) | Au moins 1 code |

### 3. Vérification d'existence dans le dictionnaire

Valider que tous les codes existent dans le dictionnaire de taxonomie :

- Charger le dictionnaire de taxonomie pour la `taxonomy_version` spécifiée
- Vérifier que chaque code dans le manifeste existe dans le dictionnaire
- Signaler les codes invalides avec leur dimension et valeur

### 4. Validation du format de code

Vérifier que tous les codes correspondent au format attendu :

```regex
^(FS|UC|DT|CH|IM|RS|OB|LG)-\d{3}$
```

### 5. Validation de schéma

Valider par rapport aux schémas JSON :

| Schéma | Objectif |
| --- | --- |
| `evidence_pack_manifest.schema.json` | Manifestes de pack de preuves |
| `taxonomy_pack.schema.json` | Définitions de pack de taxonomie |
| `changelog.schema.json` | Entrées de changelog |

## Règles de validation

### Règle : Dimensions requises

```yaml
rule_id: required_dimensions
description: Toutes les dimensions requises doivent avoir au moins un code
severity: error
check: |
  - FS: exactement 1
  - UC: au moins 1
  - DT: au moins 1
  - CH: au moins 1
  - IM: exactement 1
  - RS: au moins 1
  - EV: au moins 1
```

### Règle : Codes valides

```yaml
rule_id: valid_codes
description: Tous les codes doivent exister dans le dictionnaire de taxonomie
severity: error
check: |
  Pour chaque code dans manifest.codes:
    - Le code existe dans le dictionnaire pour la taxonomy_version spécifiée
    - Le statut du code est 'active' (avertir si 'deprecated')
```

### Règle : Format de code

```yaml
rule_id: code_format
description: Tous les codes doivent correspondre au format standard
severity: error
pattern: "^(FS|UC|DT|CH|IM|RS|OB|LG)-\\d{3}$"
```

### Règle : Format de version

```yaml
rule_id: version_format
description: Les versions doivent être du SemVer valide
severity: error
pattern: "^\\d+\\.\\d+\\.\\d+$"
fields:
  - pack_version
  - taxonomy_version
```

## Format de sortie des erreurs

Les erreurs de validation sont signalées dans le format suivant :

```
<chemin>: <sévérité>: <message>
```

**Exemples :**

```
codes.FS: error: La dimension requise 'FS' n'a pas de codes
codes.UC[0]: error: Le code 'UC-999' n'existe pas dans le dictionnaire v0.1.0
pack_version: error: Format de version invalide 'v1.0' (SemVer attendu)
codes.RS[1]: warning: Le code 'RS-002' est déprécié en v0.2.0
```

## Ce que le validateur ne vérifie PAS

Le validateur se concentre sur la conformité structurelle, pas la qualité du contenu :

| Aspect | Raison |
| --- | --- |
| Exactitude du contenu | Le validateur vérifie la structure, pas la signification |
| Complétude des preuves | Les modèles sont des guides, pas des formats imposés |
| Résolution des références croisées | L'existence des fichiers n'est pas vérifiée |
| Validité des horodatages | ISO-8601 n'est pas strictement validé |
| Unicité des ID | Pas actuellement imposé |
| Hachages d'intégrité | Responsabilité de l'adopteur |

## Implémentation de référence

Une implémentation de référence est fournie en Python :

```
validator/src/validate.py
```

### Utilisation

```bash
python validator/src/validate.py <manifest.json>
```

### Exemple de sortie

```
Validating: evidence_pack_manifest.json
Taxonomy version: 0.1.0

Checking required dimensions...
  FS: OK (1 code)
  UC: OK (3 codes)
  DT: OK (1 code)
  CH: OK (1 code)
  IM: OK (1 code)
  RS: OK (3 codes)
  OB: OK (2 codes)
  EV: OK (7 codes)

Checking code validity...
  All codes valid.

Validation: PASSED
```

## Politique de versionnement

Les règles du validateur suivent SemVer :

- **MAJEUR** : Changements de règles cassants (nouvelles vérifications requises qui échouent sur des packs existants valides)
- **MINEUR** : Nouvelles vérifications optionnelles, avertissements ou messages informatifs
- **PATCH** : Corrections de bugs qui ne changent pas les résultats de validation

## Références de schémas

| Schéma | Emplacement |
| --- | --- |
| Manifeste de pack de preuves | `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json` |
| Pack de taxonomie | `source_pack/03_taxonomy/schemas/taxonomy_pack.schema.json` |
| Changelog | `source_pack/03_taxonomy/schemas/changelog.schema.json` |

## Références

- [Taxonomie](./03-taxonomy.md) - Définitions des dimensions
- [Codes](./04-codes.md) - Format des codes
- [Dictionnaire](./05-dictionary.md) - Dictionnaire des codes
- [Règles du validateur](../../validator/index.md) - Documentation complète des règles
