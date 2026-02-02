---
description: Modèles et guide d'utilisation des packs de preuves AIMO. Structure pour documenter les preuves de gouvernance IA avec gestion d'index et formatage prêt pour l'audit.
---

# Modèle EV

Cette section définit les modèles de pack de preuves et leur utilisation. Un pack de preuves est une collection de documentation qui démontre la gouvernance et la conformité pour un système IA.

## Principe clé : Gestion d'index et de diff

> **Important** : Ce qui compte n'est pas le contenu des soumissions individuelles, mais la **gestion d'index** et de **diff** entre les éléments de preuves.

Un pack de preuves sert d'index liant les systèmes IA à leurs artefacts de gouvernance. La valeur réside dans :

1. **Traçabilité** : Lier les décisions, approbations et changements dans le temps
2. **Auditabilité** : Permettre aux auditeurs de naviguer dans la structure des preuves
3. **Maintenabilité** : Suivre ce qui a changé, quand et pourquoi

## Ensemble de preuves MVP (EV-01 à EV-07)

Les sept types de preuves suivants forment l'**ensemble minimum viable** pour démontrer la gouvernance IA :

| ID | Type de preuve | Code | Objectif |
| --- | --- | --- | --- |
| EV-01 | Vue d'ensemble système | EV-001 | Documenter le système IA et son objectif |
| EV-02 | Flux de données | EV-002 | Cartographier le mouvement des données dans le système |
| EV-03 | Inventaire | EV-003 | Maintenir le catalogue des actifs IA |
| EV-04 | Évaluation des risques et impacts | EV-004 | Évaluer et documenter les risques |
| EV-05 | Contrôles et approbations | EV-005 | Documenter les contrôles et enregistrements d'approbation |
| EV-06 | Journalisation et surveillance | EV-006 | Définir la configuration de journalisation et surveillance |
| EV-07 | Incident et exception | EV-007 | Suivre les incidents et exceptions |

## Manifeste du pack de preuves

Chaque pack de preuves DOIT inclure un fichier manifeste contenant :

### Métadonnées obligatoires

| Champ | Description | Requis |
| --- | --- | --- |
| `pack_id` | Identifiant unique (ex. EP-EXAMPLE-001) | Oui |
| `pack_version` | Version SemVer du pack | Oui |
| `taxonomy_version` | Version de la taxonomie AIMO utilisée | Oui |
| `created_date` | Date de création du pack | Oui |
| `last_updated` | Date de dernière mise à jour | Oui |
| `owner` | Partie responsable | Oui |

### Codes AIMO (8 dimensions)

Chaque pack de preuves DOIT inclure des codes des 8 dimensions :

```json
{
  "codes": {
    "FS": ["FS-001"],
    "UC": ["UC-001", "UC-002"],
    "DT": ["DT-002"],
    "CH": ["CH-001"],
    "IM": ["IM-001"],
    "RS": ["RS-001", "RS-003"],
    "OB": ["OB-001"],
    "EV": ["EV-001", "EV-002", "EV-003", "EV-004", "EV-005", "EV-006", "EV-007"]
  }
}
```

### Liste des fichiers de preuves

```json
{
  "evidence_files": [
    {
      "file_id": "EV-01",
      "filename": "EV-01_system_overview.md",
      "ev_type": "EV-001",
      "title": "System Overview",
      "required": true
    }
  ]
}
```

## Structure du modèle

Chaque modèle de preuve inclut :

1. **Bloc de métadonnées obligatoires** - pack_id, version, taxonomy_version, dates, owner
2. **Tableau de codes AIMO** - Les 8 dimensions avec les codes applicables
3. **Sections de contenu** - Sections de documentation spécifiques au domaine
4. **Références** - Liens vers les preuves connexes
5. **Historique des révisions** - Suivi des changements

### Exemple d'en-tête de modèle

```markdown
# EV-01: Vue d'ensemble système

---

## Métadonnées obligatoires

| Champ | Valeur |
| --- | --- |
| **pack_id** | `EP-EXAMPLE-001` |
| **pack_version** | `0.1.0` |
| **taxonomy_version** | `0.1.0` |
| **created_date** | `2026-01-31` |
| **last_updated** | `2026-01-31` |
| **owner** | `AI Governance Team` |

---

## Codes AIMO (8 dimensions)

| Dimension | Code(s) | Libellé |
| --- | --- | --- |
| **FS** | `FS-001` | Productivité utilisateur final |
| **UC** | `UC-001` | Q&R général |
| **DT** | `DT-002` | Interne |
| **CH** | `CH-001` | Interface web |
| **IM** | `IM-001` | Autonome |
| **RS** | `RS-001` | Fuite de données |
| **OB** | `OB-001` | Efficacité |
| **EV** | `EV-001` | Vue d'ensemble système |
```

## Téléchargements

### Modèles

Les modèles de pack de preuves sont disponibles dans :

- `source_pack/04_evidence_pack/templates/EV-01_system_overview.md`
- `source_pack/04_evidence_pack/templates/EV-02_data_flow.md`
- `source_pack/04_evidence_pack/templates/EV-03_inventory.md`
- `source_pack/04_evidence_pack/templates/EV-04_risk_impact.md`
- `source_pack/04_evidence_pack/templates/EV-05_controls_approvals.md`
- `source_pack/04_evidence_pack/templates/EV-06_logging_monitoring.md`
- `source_pack/04_evidence_pack/templates/EV-07_incident_exception.md`

### Schémas et exemples

- Schéma : `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json`
- Exemple : `source_pack/04_evidence_pack/examples/evidence_pack_manifest.example.json`

Voir [Versions](../../releases/index.md) pour les packages téléchargeables.

## Modèle de distribution

> **Note** : Les cibles principales de distribution sont les **cabinets d'audit et intégrateurs système** (distributeurs de modèles), pas les entreprises individuelles.

Les modèles sont conçus pour être :

1. Adoptés par les auditeurs et consultants comme artefacts standard
2. Distribués aux entreprises avec attribution de source préservée
3. Versionnés avec le standard AIMO

Les entreprises reçoivent les modèles via leurs auditeurs, consultants ou équipes de gouvernance internes qui maintiennent le lien avec la version du standard.

## Références

- [Taxonomie](./03-taxonomy.md) - Définitions des dimensions
- [Codes](./04-codes.md) - Format des codes
- [Validateur](./07-validator.md) - Règles de validation
- [Lot de preuves](../../artifacts/evidence-bundle.md) - Structure du lot
