---
description: Exigences minimales de preuves AIMO. Liste de contrôle OBLIGATOIRE par cycle de vie (demande, revue, approbation, modification, renouvellement) pour la préparation des preuves de gouvernance IA.
---

# Exigences minimales de preuves

Cette page définit les exigences minimales de preuves sous forme de liste de contrôle OBLIGATOIRE, groupée par cycle de vie. Elle soutient l'explicabilité et la préparation des preuves ; elle ne fournit pas de conseils juridiques et ne garantit pas la conformité.

## 1) Demande

- **Champs OBLIGATOIRES** : identifiant, horodatage(s), acteur/rôle, périmètre (ce qui est demandé), justification (pourquoi).
- **Liaisons OBLIGATOIRES** : l'ID de demande est référencé par la revue et par les éléments EV qui enregistrent l'utilisation.
- **Ce que cela prouve** : que l'utilisation a été demandée et délimitée avant l'approbation et l'utilisation.

## 2) Revue / Approbation

- **Champs OBLIGATOIRES** : identifiant, horodatage(s), acteur/rôle, décision (approuvé/rejeté/conditionnel), périmètre, justification, référence à la demande.
- **Liaisons OBLIGATOIRES** : l'ID de revue est référencé par EV et par toute exception ou renouvellement qui suit.
- **Ce que cela prouve** : qu'une revue et une approbation définies ont eu lieu avant l'utilisation (ou l'exception).

## 3) Exception

- **Champs OBLIGATOIRES** : identifiant, horodatage(s), périmètre, expiration (ou échéance), contrôles compensatoires, justification, référence à la revue/demande.
- **Liaisons OBLIGATOIRES** : exception → contrôles compensatoires ; exception → expiration ; exception → renouvellement (quand la réévaluation est due).
- **Ce que cela prouve** : que les déviations sont limitées dans le temps, ont des contrôles compensatoires et sont liées au renouvellement.

## 4) Renouvellement / Réévaluation

- **Champs OBLIGATOIRES** : identifiant, horodatage(s), acteur/rôle, décision (renouvelé/révoqué/conditionnel), références à l'exception/demande/revue/EV antérieur(e).
- **Liaisons OBLIGATOIRES** : le renouvellement référence l'exception ou l'approbation en cours de renouvellement ; les éléments EV peuvent référencer l'ID de renouvellement.
- **Ce que cela prouve** : que les exceptions et approbations sont réévaluées et renouvelées ou révoquées sur une base définie.

## 5) Journal des modifications

- **Champs OBLIGATOIRES** : identifiant, horodatage, acteur/rôle, description de la modification, références (ex. aux EV, demande, revue, exception, renouvellement affectés).
- **Liaisons OBLIGATOIRES** : les entrées du journal des modifications référencent les artefacts qu'elles modifient ou qui déclenchent la modification.
- **Ce que cela prouve** : que les modifications du lot ou de son contenu sont enregistrées et traçables.

## 6) Intégrité et accès

L'intégrité des preuves et le contrôle d'accès sont essentiels pour la confiance de l'audit. Bien que AIMO ne prescrive pas de contrôles techniques spécifiques, les adopteurs doivent documenter comment ces attentes sont satisfaites.

### Orientations sur le contrôle d'accès

| Aspect | Orientation |
| --- | --- |
| **Accès basé sur les rôles** | Définissez les rôles (ex. créateur de preuves, réviseur, auditeur, admin) et documentez qui peut créer, lire, mettre à jour ou supprimer des preuves. |
| **Moindre privilège** | Accordez l'accès minimum nécessaire ; restreignez l'accès en écriture au personnel autorisé. |
| **Journalisation des accès** | Journalisez les événements d'accès (qui, quand, quoi) pour la piste d'audit. |
| **Séparation des fonctions** | Lorsque c'est pratique, séparez la création de preuves des rôles d'approbation. |

### Orientations sur la rétention

| Aspect | Orientation |
| --- | --- |
| **Période de rétention** | Définissez et documentez les périodes de rétention basées sur les exigences réglementaires et la politique organisationnelle (ex. 5-7 ans pour les audits financiers). |
| **Calendrier de rétention** | Maintenez un calendrier montrant quelles preuves sont conservées, pour combien de temps et quand elles peuvent être éliminées. |
| **Conservation juridique** | Soutenez les processus de conservation juridique qui suspendent la rétention/suppression normale pour les litiges ou investigations. |

### Options d'immutabilité

| Option | Description |
| --- | --- |
| **Hachage cryptographique** | Générez des hachages SHA-256 (ou plus forts) pour les fichiers de preuves ; stockez les hachages séparément pour vérification. |
| **Stockage WORM** | Utilisez un stockage Write-Once-Read-Many pour les archives de preuves afin de prévenir les modifications. |
| **Journaux en ajout seul** | Utilisez des journaux d'audit en ajout seul pour le suivi des modifications. |
| **Signatures numériques** | Signez les lots de preuves pour prouver la paternité et détecter les altérations. |

### Attentes de piste d'audit

| Élément | Ce qu'il faut documenter |
| --- | --- |
| **Journal des modifications** | Enregistrez qui a modifié quoi, quand et pourquoi (voir le groupe cycle de vie Journal des modifications). |
| **Journal des accès** | Enregistrez qui a accédé aux preuves, quand et dans quel but. |
| **Journaux système** | Conservez les journaux système pertinents (authentification, autorisation) qui soutiennent les affirmations d'intégrité des preuves. |
| **Enregistrements de vérification** | Documentez la vérification périodique de l'intégrité (vérifications de hash, revues d'audit). |

### Ce que cela prouve

- **Les preuves sont préservées** : les mécanismes d'intégrité (hachage, WORM, signatures) démontrent que les preuves n'ont pas été altérées.
- **L'accès est contrôlé** : les journaux d'accès et les définitions de rôles montrent qui avait accès et que le moindre privilège a été appliqué.
- **La confiance de l'audit est soutenue** : ensemble, ces éléments donnent aux auditeurs confiance dans la fiabilité des preuves.

### Profils opérationnels recommandés

Choisissez un profil basé sur votre tolérance au risque et vos exigences réglementaires. Ce sont des recommandations, pas des obligations.

| Aspect | Léger | Standard | Strict |
| --- | --- | --- | --- |
| **Cas d'usage** | Pilotes internes, IA à faible risque | Systèmes de production, risque modéré | Industries réglementées, IA à haut risque |
| **Période de rétention** | 1-2 ans | 5-7 ans | 7-10+ ans ou minimum réglementaire |
| **Immutabilité** | Hachages SHA-256 | SHA-256 + journaux en ajout seul | Stockage WORM + signatures numériques |
| **Contrôle d'accès** | Basé sur les rôles (basique) | Basé sur les rôles + journalisation des accès | Séparation des fonctions + piste d'audit complète |
| **Piste d'audit** | Journal des modifications uniquement | Journal des modifications + journal des accès | Journaux système complets + vérification périodique |
| **Fréquence de vérification** | À la demande | Trimestrielle | Mensuelle ou continue |
| **Utilisation du validateur** | Optionnel | Requis avant soumission | Requis + vérifications CI automatisées |

!!! note "Les périodes de rétention sont des exemples"
    Les périodes de rétention indiquées sont illustratives. Les organisations doivent déterminer la rétention en fonction des lois applicables, contrats, exigences sectorielles et politiques internes.

!!! tip "Comment choisir"
    - **Léger** : Adapté à l'expérimentation, aux outils internes ou aux applications à faibles enjeux où des audits formels sont peu probables.
    - **Standard** : Recommandé pour la plupart des déploiements de production où des audits peuvent survenir mais ne sont pas continus.
    - **Strict** : Requis pour les industries réglementées (finance, santé, gouvernement) ou les systèmes d'IA à impact de risque significatif.

## Note importante

Cet ensemble minimum soutient l'explicabilité et la préparation des preuves ; il ne fournit pas en lui-même de conseils juridiques et ne garantit pas la conformité.

Voir [Lot de preuves](../evidence-bundle/) pour la structure du lot et la TDM ; voir [Modèle EV](../../standard/current/06-ev-template/) et les schémas pour l'alignement au niveau des champs.

Voir aussi : [Schémas de journaux](../log-schemas/) — formats de journaux normalisés pour les preuves de découverte de Shadow AI et d'activité des agents.
