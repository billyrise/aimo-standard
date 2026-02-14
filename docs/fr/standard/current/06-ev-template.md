---
description: Modèles et guide d'utilisation des packs de preuves AIMO. Structure pour documenter les preuves de gouvernance IA avec gestion d'index et formatage prêt pour l'audit.
---

# Modèle Evidence Pack (EP)

Cette section définit les modèles de pack de preuves et leur utilisation. Un pack de preuves est une collection de documentation qui démontre la gouvernance et la conformité pour un système IA.

## Espace de noms : types de document Evidence Pack (EP) vs Taxonomy Log/Event Type (LG)

> **Important** : **EP-01..EP-07** identifient les *types de document* (types de fichier Evidence Pack). **LG-001, LG-002, …** dans la [Taxonomie](./03-taxonomy.md) identifient les *types de log/registre* (Enregistrement de demande, Enregistrement de revue/approbation, etc.). **EV-** réservé aux ID d'artefacts Evidence. Utiliser EP pour la structure du pack et LG pour la classification des preuves du cycle de vie.

## Principe clé : Gestion d'index et de diff

Ce qui compte n'est pas seulement le contenu des soumissions individuelles, mais l'**index** et la **gestion de diff** entre les éléments de preuves.

Un pack de preuves sert d'index liant les systèmes IA à leurs artefacts de gouvernance. La valeur réside dans :

1. **Traçabilité** : Lier les décisions, approbations et changements dans le temps
2. **Auditabilité** : Permettre aux auditeurs de naviguer dans la structure des preuves
3. **Maintenabilité** : Suivre ce qui a changé, quand et pourquoi

## Ensemble de preuves MVP (EP-01 à EP-07)

Les sept **types de document Evidence Pack** (EP) suivants forment l'**ensemble minimum viable** pour démontrer la gouvernance IA. Chacun est un modèle de document ; les codes **LG** de taxonomie (Enregistrement de demande, Revue/approbation, etc.) sont utilisés ailleurs dans le bundle et dans `codes.LG` pour classer les preuves de *log/registre*.

| ID | Type de document | Objectif |
| --- | --- | --- |
| EP-01 | Vue d'ensemble système | Documenter le système IA et son objectif |
| EP-02 | Flux de données | Cartographier le mouvement des données dans le système |
| EP-03 | Inventaire | Maintenir le catalogue des actifs IA |
| EP-04 | Évaluation des risques et impacts | Évaluer et documenter les risques |
| EP-05 | Contrôles et approbations | Documenter les contrôles et enregistrements d'approbation |
| EP-06 | Journalisation et surveillance | Définir la configuration de journalisation et surveillance |
| EP-07 | Incident et exception | Suivre les incidents et exceptions |

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

Chaque pack de preuves DOIT inclure des codes des 8 dimensions. La dimension **LG** liste les types de log/registre *taxonomie* (ex. Enregistrement de demande, Revue/approbation) applicables à ce pack—pas les codes de type de document. Le type de document est donné par `evidence_files[].file_id` (EP-01..EP-07).

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
    "LG": ["LG-001", "LG-002", "LG-008", "LG-009"]
  }
}
```

### Liste des fichiers de preuves

Chaque entrée identifie un document du pack par **file_id** (EP-01..EP-07). Optionnellement **ev_codes** peut lister les codes LG de taxonomie (LG-xxx) que le document supporte.

```json
{
  "evidence_files": [
    {
      "file_id": "EP-01",
      "filename": "EP-01_system_overview.md",
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
# EP-01: Vue d'ensemble système

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
| **LG** | `LG-001`, `LG-002` | Enregistrement de demande, Enregistrement de revue/approbation |
```

## Téléchargements

### Modèles

Les modèles Evidence Pack sont disponibles dans le dépôt. Utilisez **file_id** EP-01..EP-07 dans le manifeste ; les noms de fichier peuvent être EP-01_... ou legacy EV-01_... pour compatibilité.

- `source_pack/04_evidence_pack/templates/EV-01_system_overview.md` → file_id **EP-01**
- `source_pack/04_evidence_pack/templates/EV-02_data_flow.md` → file_id **EP-02**
- `source_pack/04_evidence_pack/templates/EV-03_inventory.md` → file_id **EP-03**
- `source_pack/04_evidence_pack/templates/EV-04_risk_impact.md` → file_id **EP-04**
- `source_pack/04_evidence_pack/templates/EV-05_controls_approvals.md` → file_id **EP-05**
- `source_pack/04_evidence_pack/templates/EV-06_logging_monitoring.md` → file_id **EP-06**
- `source_pack/04_evidence_pack/templates/EV-07_incident_exception.md` → file_id **EP-07**

### Schémas et exemples

- Schéma : `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json`
- Exemple : `source_pack/04_evidence_pack/examples/evidence_pack_manifest.example.json`

Voir [Versions](../../../releases/) pour les packages téléchargeables.

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
