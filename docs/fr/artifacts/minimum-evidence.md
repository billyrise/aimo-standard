---
description: Exigences minimales de preuves AIMO. Liste de contrôle MUST par cycle de vie (demande, revue, approbation, changement, renouvellement) pour la préparation des preuves en gouvernance de l'IA.
---
<!-- aimo:translation_status=translated -->

# Exigences minimales de preuves (Minimum Evidence Requirements)

Cette page est la liste de contrôle des **Exigences minimales de preuves** pour les auditeurs et les metteurs en œuvre. Elle définit les exigences minimales comme liste MUST par cycle de vie. Elle soutient l'explicabilité et la préparation des preuves ; elle ne constitue pas un avis juridique ni ne garantit la conformité.

Utilisez cette page avec le [Lot de preuves](../evidence-bundle/) et le [Validateur](../../standard/current/07-validator/) lors de la préparation ou de la revue des soumissions.

## 1) Demande (Request)

- **Champs MUST** : identifiant, horodatage(s), acteur/rôle, périmètre (ce qui est demandé), justification (rationale).
- **Liens MUST** : l'id de demande est référencé par la revue et par les éléments EV qui enregistrent l'utilisation.
- **Ce que cela prouve** : que l'utilisation a été demandée et délimitée avant approbation et utilisation.

## 2) Revue / Approbation (Review / Approval)

- **Champs MUST** : identifiant, horodatage(s), acteur/rôle, décision (approuvé/rejeté/conditionnel), périmètre, justification, référence à la demande.
- **Liens MUST** : l'id de revue est référencé par l'EV et par toute exception ou renouvellement qui suit.
- **Ce que cela prouve** : qu'une revue et une approbation définies ont eu lieu avant utilisation (ou exception).

## 3) Exception (Exception)

- **Champs MUST** : identifiant, horodatage(s), périmètre, expiration (ou échéance), contrôles compensatoires, justification, référence à la revue/demande.
- **Liens MUST** : exception → contrôles compensatoires ; exception → expiration ; exception → renouvellement (lorsque la réévaluation est due).
- **Ce que cela prouve** : que les écarts sont limités dans le temps, ont des contrôles compensatoires et sont liés au renouvellement.

## 4) Renouvellement / Réévaluation (Renewal / Re-evaluation)

- **Champs MUST** : identifiant, horodatage(s), acteur/rôle, décision (renouvelé/révoqué/conditionnel), références à l'exception/demande/revue/EV antérieurs.
- **Liens MUST** : le renouvellement référence l'exception ou l'approbation renouvelée ; les éléments EV peuvent référencer l'id de renouvellement.
- **Ce que cela prouve** : que les exceptions et approbations sont réévaluées et renouvelées ou révoquées sur une base définie.

## 5) Journal des modifications (Change Log)

- **Champs MUST** : identifiant, horodatage, acteur/rôle, description du changement, références (ex. aux EV, demande, revue, exception, renouvellement concernés).
- **Liens MUST** : les entrées du journal des modifications référencent les artefacts qu'elles modifient ou qui déclenchent le changement.
- **Ce que cela prouve** : que les changements apportés au lot ou à son contenu sont enregistrés et traçables.

## 6) Intégrité et accès (Integrity & Access)

L'intégrité des preuves et le contrôle d'accès sont essentiels pour la confiance dans l'audit. AIMO ne prescrit pas de contrôles techniques spécifiques ; les adoptants doivent documenter comment ces attentes sont satisfaites.

### Guide de contrôle d'accès

| Aspect | Guide |
| --- | --- |
| **Accès par rôle** | Définir les rôles (ex. créateur de preuves, réviseur, auditeur, admin) et documenter qui peut créer, lire, mettre à jour ou supprimer des preuves. |
| **Privilège minimum** | Accorder l'accès minimum nécessaire ; restreindre l'écriture au personnel autorisé. |
| **Journalisation des accès** | Enregistrer les événements d'accès (qui, quand, quoi) pour la traçabilité d'audit. |
| **Séparation des fonctions** | Lorsque c'est pratique, séparer la création de preuves des rôles d'approbation. |

### Guide de conservation

| Aspect | Guide |
| --- | --- |
| **Durée de conservation** | Définir et documenter les durées selon les exigences réglementaires et la politique de l'organisation (ex. 5–7 ans pour les audits financiers). |
| **Calendrier de conservation** | Maintenir un calendrier indiquant quelles preuves sont conservées, pour combien de temps et quand elles peuvent être éliminées. |
| **Conservation légale** | Soutenir les processus de conservation légale qui suspendent la conservation/suppression normale en cas de litige ou d'enquête. |

### Options d'immutabilité

| Option | Description |
| --- | --- |
| **Hachage cryptographique** | Générer des hachages SHA-256 (ou supérieurs) pour les fichiers de preuves ; stocker les hachages séparément pour vérification. |
| **Stockage WORM** | Utiliser un stockage à écriture unique et lecture multiple (WORM) pour les archives de preuves afin d'éviter la modification. |
| **Journaux en annexe seule** | Utiliser des journaux d'audit en annexe seule pour le suivi des changements. |
| **Signatures numériques** | Signer les lots de preuves pour prouver la paternité et détecter les altérations. |

### Attentes en matière de traçabilité d'audit

| Élément | Ce qu'il faut documenter |
| --- | --- |
| **Journal des modifications** | Enregistrer qui a changé quoi, quand et pourquoi (voir le groupe de cycle de vie Change Log). |
| **Journal d'accès** | Enregistrer qui a accédé aux preuves, quand et dans quel but. |
| **Journaux système** | Conserver les journaux système pertinents (authentification, autorisation) qui étayent les affirmations d'intégrité. |
| **Enregistrements de vérification** | Documenter la vérification périodique de l'intégrité (vérifications de hachage, revues d'audit). |

### Ce que cela prouve

- **Les preuves sont préservées** : les mécanismes d'intégrité (hachage, WORM, signatures) démontrent que les preuves n'ont pas été altérées.
- **L'accès est contrôlé** : les journaux d'accès et les définitions de rôles montrent qui a eu accès et que le privilège minimum a été appliqué.
- **La confiance dans l'audit est soutenue** : ensemble, ces éléments donnent aux auditeurs confiance dans la fiabilité des preuves.

### Profils opérationnels recommandés

Choisissez un profil selon votre tolérance au risque et les exigences réglementaires. Ce sont des recommandations, pas des obligations.

| Aspect | Léger | Standard | Strict |
| --- | --- | --- | --- |
| **Cas d'usage** | Pilotes internes, IA à faible risque | Systèmes en production, risque modéré | Industries réglementées, IA à haut risque |
| **Durée de conservation** | 1–2 ans | 5–7 ans | 7–10+ ans ou minimum réglementaire |
| **Immutabilité** | Hachages SHA-256 | SHA-256 + journaux en annexe seule | Stockage WORM + signatures numériques |
| **Contrôle d'accès** | Par rôle (de base) | Par rôle + journalisation des accès | Séparation des fonctions + traçabilité complète |
| **Traçabilité d'audit** | Journal des modifications uniquement | Journal des modifications + journal d'accès | Journaux système complets + vérification périodique |
| **Fréquence de vérification** | À la demande | Trimestrielle | Mensuelle ou continue |
| **Utilisation du Validateur** | Optionnelle | Requise avant soumission | Requise + vérifications CI automatisées |

!!! note "Les durées de conservation sont des exemples"
    Les durées indiquées sont illustratives. Les organisations doivent déterminer la conservation selon les lois applicables, contrats, exigences sectorielles et politiques internes.

!!! tip "Comment choisir"
    - **Léger** : Adapté à l'expérimentation, aux outils internes ou aux applications à faible enjeu où un audit formel est peu probable.
    - **Standard** : Recommandé pour la plupart des déploiements en production où des audits peuvent avoir lieu mais pas en continu.
    - **Strict** : Requis pour les industries réglementées (finance, santé, gouvernement) ou les systèmes d'IA à impact de risque significatif.

## Note importante

Cet ensemble minimal soutient l'explicabilité et la préparation des preuves ; il ne constitue pas en soi un avis juridique ni ne garantit la conformité.

Voir le [Lot de preuves](../evidence-bundle/) pour la structure et la TDM du lot ; [Modèle EV](../../standard/current/06-ev-template/) et schémas pour l'alignement au niveau des champs.

Voir aussi : [Schémas de journal](../log-schemas/) — formats de journal normalisés pour la découverte Shadow AI et les preuves d'activité des agents.

## Superpositions réglementaires (informatif)

Les **superpositions** suivantes décrivent des preuves supplémentaires souvent attendues dans des contextes réglementaires ou d'achat spécifiques. Elles sont **informatives** ; joignez les modèles/listes de contrôle officiels tels quels dans la [section External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) du modèle EV et référencez-les par logical_id dans le manifeste.

| Superposition | Artefacts supplémentaires typiquement attendus | Où joindre | Profil (optionnel) |
| --- | --- | --- | --- |
| **EU haut risque** | Gestion des risques, documentation technique (Annexe IV), journalisation, supervision humaine, transparence (Art 50), signalement d'incidents | payload_index ; Lot de preuves + profil Annex IV | `eu_ai_act_annex_iv.json`, `eu_ai_act_high_risk.json` |
| **EU GPAI CoP** | Model Documentation Form (transparence, droits d'auteur, sécurité) | External Forms ; logical_id ex. GPAI_MODEL_DOC_FORM | `eu_gp_ai_cop.json` |
| **NIST GenAI** | Artefacts du profil GenAI (adaptation de modèle, évaluation, surveillance) | payload_index ; change_log ; External Forms / enregistrements GenAI | `nist_ai_600_1_genai.json` |
| **UK ATRS / marchés publics** | Enregistrement de transparence ATRS ; responsable de la responsabilité ; notes d'évaluation des marchés | External Forms ; Summary, review | `uk_atrs_procurement.json` |
| **JP marchés publics** | Liste de contrôle des marchés publics GenAI du gouvernement ; liste de contrôle AI Business Guidelines | External Forms ; logical_id ex. JP_PROCUREMENT_CHECKLIST | `jp_gov_genai_procurement.json` |

Les noms de fichiers de profil suivent le modèle `coverage_map/profiles/<target>_<purpose>.json` ; chacun inclut `target_version`. Voir [Coverage Map — Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/) pour le R.-U. et le Japon ; [EU AI Act](../../coverage-map/eu-ai-act/) et [NIST AI RMF](../../coverage-map/nist-ai-rmf/) pour l'UE et le NIST.
