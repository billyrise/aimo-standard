---
description: Méthodologie de la carte de couverture - Comment AIMO correspond aux cadres externes. Utilisation dans les audits, relation avec le lot de preuves et approche de traçabilité.
---

# Méthodologie

> Note : Cette méthodologie soutient la traçabilité et la préparation des preuves. Elle ne garantit pas la conformité à une réglementation/norme spécifique.

Cette page explique ce qu'est et n'est pas la carte de couverture, comment l'utiliser en audit et comment elle se rapporte au lot de preuves et aux exigences minimales de preuves.

## Ce qu'est la correspondance

- Une correspondance **informative** entre les références de cadre/réglementation externes (par sujet) et les preuves AIMO, les éléments de la TDM du lot de preuves, les groupes de cycle de vie des preuves minimales, les artefacts et les vérifications du validateur.
- Un outil de support pour **l'explicabilité** : quelles preuves et artefacts AIMO peuvent aider à démontrer ou expliquer l'alignement avec une exigence externe donnée (sans prétendre à la conformité).

## Ce que la correspondance n'est pas

- **Pas** une garantie de conformité à un cadre ou une réglementation.
- **Pas** un avis juridique ou un substitut à la vérification par rapport aux textes faisant autorité.
- **Pas** exhaustif ; c'est un sous-ensemble pratique pour la préparation à l'audit et l'explicabilité.

## Comment l'utiliser en audit

Utilisez le flux : **exigence → preuve → artefact → validation**.

1. **Exigence** : Identifiez la référence du cadre externe et le sujet (ex. documentation ISO 42001, tenue de registres EU AI Act).
2. **Preuve** : Voyez quels éléments du lot de preuves AIMO et groupes de cycle de vie des preuves minimales (demande, revue, exception, renouvellement, change_log, intégrité) soutiennent l'explicabilité pour cette exigence.
3. **Artefact** : Localisez les artefacts (schémas, modèles, exemples) qui implémentent ou illustrent cette preuve.
4. **Validation** : Utilisez le validateur et les vérifications de schéma référencés pour vérifier la cohérence structurelle.

Les lecteurs doivent vérifier par rapport au texte faisant autorité de chaque cadre ou réglementation.

## Relation avec le lot de preuves et les exigences minimales de preuves

- **[Lot de preuves](../../artifacts/evidence-bundle/)** : Définit la structure du lot, la TDM et la traçabilité. Les lignes de la carte de couverture référencent les sections du lot de preuves (ex. EV, Dictionary, Summary, change_log, demande, revue, exception, renouvellement).
- **[Exigences minimales de preuves](../../artifacts/minimum-evidence/)** : Définit les groupes de cycle de vie OBLIGATOIRES (demande, revue, exception, renouvellement, change_log, intégrité). Les lignes de la carte de couverture référencent ces groupes dans `minimum_evidence_refs`.

Utilisez la carte de couverture pour voir quels éléments du lot de preuves et groupes de preuves minimales soutiennent l'explicabilité pour une exigence externe donnée.

## Déclaration de non-déclaration excessive

!!! warning "Important"
    Le standard AIMO soutient **l'explicabilité et la préparation des preuves**. Il ne fournit **pas** d'avis juridique, ne garantit pas la conformité et ne certifie pas la conformité à une réglementation ou un cadre. Les adopteurs doivent vérifier les déclarations par rapport aux textes faisant autorité et obtenir des conseils professionnels si nécessaire.

Voir [Périmètre de responsabilité](../../governance/responsibility-boundary/) pour le périmètre, les hypothèses et les responsabilités des adopteurs.

## Parcours d'audit

Depuis cette page, continuez vers :

1. **Correspondances de cadres** : [ISO 42001](../iso-42001/), [NIST AI RMF](../nist-ai-rmf/), [EU AI Act](../eu-ai-act/), [ISMS](../isms/)
2. **Valider** : [Validateur](../../validator/) — exécuter les vérifications structurelles
3. **Télécharger** : [Versions](../../releases/) — obtenir les actifs de version
