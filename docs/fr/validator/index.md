---
description: Hub du validateur AIMO - Démarrage rapide de l'outillage de validation. Installer, exécuter et interpréter les résultats en 30 secondes. Validation de pack de preuves et vérifications de conformité.
---

# Validateur

Cette page est un hub pour l'outillage et les règles de validation. La spécification normative du validateur et de ses règles est dans le Standard.

## Démarrage rapide (30 secondes)

**1. Prérequis**

```bash
pip install jsonschema   # si pas déjà installé
```

**2. Exécuter la validation sur un lot d'échantillon**

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

**3. Lire le rapport et corriger les erreurs/avertissements**

Exemple de sortie (succès) :

```
OK
```

Exemple de sortie (échec) :

```
Schema validation failed:
<root>: 'version' is a required property
<root>: 'dictionary' is a required property
<root>: 'evidence' is a required property
```

Codes de sortie : `0` = succès, `1` = erreurs de validation, `2` = erreur d'utilisation.

---

## Ce qu'il vérifie

- **Validation de schéma** : l'objet root, le dictionnaire et les preuves sont conformes au schéma JSON
- **Cohérence du dictionnaire** : tous les codes existent dans le dictionnaire de taxonomie
- **Statut des codes** : avertit pour les codes dépréciés, erreur pour les codes supprimés

## Ce qu'il ne vérifie PAS

- **Exactitude du contenu** : le validateur vérifie la structure, pas la signification
- **Garantie de conformité** : passer la validation ne garantit pas la conformité réglementaire
- **Jugement humain** : les décisions dépendantes du contexte nécessitent une revue humaine (voir [Protocole de surveillance humaine](../governance/human-oversight-protocol.md))
- **Collecte automatique de journaux** : le validateur valide les preuves soumises ; il ne collecte pas les journaux

---

## Ressources

- **Spécification** : [Standard > Actuel > Validateur](../standard/current/07-validator.md) — règles, vérifications de référence et comment la validation se rapporte aux preuves.
- **Règles et implémentation** : dépôt `validator/rules/` (vérifications), `validator/src/` (implémentation de référence). L'exécution et l'utilisation CI sont décrites dans la spec.
- **Interprétation** : ce qu'un "échec" de validation signifie pour les auditeurs (expliqué dans la spec).

Pour la conformité et l'utilisation des artefacts, voir [Conformité](../conformance/index.md) et [Artefacts](../artifacts/index.md).
