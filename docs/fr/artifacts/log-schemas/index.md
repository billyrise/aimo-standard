---
description: Schémas de journaux AIMO - Formats de journaux neutres vis-à-vis des fournisseurs pour les preuves d'IA. Inclut les schémas de découverte de Shadow AI et de surveillance d'activité des agents.
---
<!-- aimo:translation_status=translated -->

# Schémas de journaux

## Ce que c'est

Cette section définit des **formats de journaux normalisés** pour les preuves pouvant être incluses dans un lot de preuves. Ces schémas fournissent une structure neutre vis-à-vis des fournisseurs pour les journaux liés à la surveillance de l'utilisation de l'IA et aux opérations agentiques.

## Quand utiliser

- **Visibilité du Shadow AI** : Documenter la détection, l'inventaire et la remédiation de l'utilisation non approuvée de l'IA.
- **Audits des opérations agentiques** : Expliquer l'exercice des privilèges d'agents autonomes, l'exécution d'outils et les opérations récursives.
- **Reproductibilité des incidents** : Fournir des preuves structurées pour l'investigation d'incidents et l'analyse des causes racines.

## Ce que ce n'est PAS

!!! warning "Important"
    Ces schémas définissent des **formats de journaux pour la soumission de preuves**. Ils ne :

    - Collectent PAS automatiquement les journaux de vos systèmes
    - Fournissent PAS d'outils d'agrégation ou de surveillance des journaux
    - Garantissent PAS la conformité à une réglementation ou norme
    - Remplacent PAS les implémentations de journalisation spécifiques aux fournisseurs

    Les organisations doivent implémenter leurs propres pipelines de collecte de journaux et normaliser les journaux selon ces schémas pour la soumission de preuves.

## Schémas

| Schéma | Objectif | Télécharger |
| --- | --- | --- |
| [Journal de découverte de Shadow AI](shadow-ai-discovery/) | Détection et inventaire de l'utilisation non approuvée de l'IA | [shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json) |
| [Journal d'activité des agents](agent-activity/) | Exercice des privilèges d'IA agentique et exécution d'outils | [agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json) |

## Pages connexes

- [Exigences minimales de preuves](../minimum-evidence/) — Liste de contrôle OBLIGATOIRE des preuves
- [Lot de preuves](../evidence-bundle/) — Structure du lot et TDM
- [Taxonomie](../../standard/current/03-taxonomy/) — Codes de classification (incluant UC-010 Automatisation agentique, IM-007 Shadow/Non géré)
