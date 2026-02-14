---
description: Structure du lot de preuves AIMO. Format de package d'audit avec table des matières, traçabilité et artefacts pour la conformité en gouvernance IA et la livraison aux auditeurs.
---

# Lot de preuves

Un **lot de preuves** est un package d'audit : un ensemble structuré d'artefacts qui soutient l'explicabilité et la traçabilité pour la gouvernance de l'IA. Ce n'est pas une fonctionnalité produit mais un format livrable pour les auditeurs et la conformité.

## Structure et nommage du lot

- **Nommage de la racine du lot** : utilisez un modèle cohérent tel que `{org}_{system}_{period}_{version}` (ex. `acme_ai-usage_2026-Q1_v1`).
- **Fichiers requis** : au moins un ensemble de preuves (EV) aligné avec le [modèle Evidence Pack (EP)](../standard/current/06-ev-template.md), un [dictionnaire](../standard/current/05-dictionary.md), un bref **résumé** (synthèse exécutive du lot), et un **journal des modifications** (ou référence à celui-ci) pour les changements apportés au lot ou à son contenu.
- **Pièces jointes optionnelles** : journaux, enregistrements de revue, approbations d'exceptions, enregistrements de renouvellement ; gardez un nommage cohérent et référençable depuis le document EV/dictionnaire principal.

## Table des matières (TDM)

| Section | Artefact | Requis ? | Objectif | Champs minimums | Validation |
| --- | --- | --- | --- | --- | --- |
| Preuve | Enregistrements EV (JSON/tableau) | Oui | Enregistrement de ce qui s'est passé ; lien vers demande/revue/exception/renouvellement | id, timestamp, source, summary ; refs lifecycle optionnelles | [Validateur](../validator/index.md), aimo-ev.schema.json |
| Dictionnaire | dictionary.json | Oui | Clés/libellés/descriptions pour les codes et dimensions | entries (key, label, description) | aimo-dictionary.schema.json |
| Résumé | summary (doc ou champ) | Oui | Aperçu d'une page pour les auditeurs | scope, period, key decisions, exceptions | — |
| Journal des modifications | change_log ou référence | Oui | Piste d'audit des modifications du lot/contenu | id, timestamp, actor, change description, references | — |
| Demande | enregistrement(s) de demande | Si applicable | Demande/requête d'utilisation | id, timestamp, actor/role, scope, rationale | — |
| Revue/Approbation | enregistrement(s) de revue | Si applicable | Résultat de la revue et de l'approbation | id, timestamp, actor/role, decision, references | — |
| Exception | enregistrement(s) d'exception | Si applicable | Exception avec contrôles compensatoires et expiration | id, timestamp, scope, expiry, compensating controls, renewal ref | — |
| Renouvellement | enregistrement(s) de renouvellement | Si applicable | Réévaluation et renouvellement | id, timestamp, actor/role, decision, references to prior exception/EV | — |

## Relation normative : enregistrements EV (index) et Evidence Pack (payload)

Pour éviter la double construction et l'ambiguïté en audit, ce qui suit est **normatif** : (1) Les enregistrements EV (JSON) sont l'**index/registre** (traçabilité vérifiable par machine). (2) Les fichiers Evidence Pack (EP-01..EP-07 et manifeste) sont le **payload**. (3) Les enregistrements EV DEVRAIENT référencer le payload par `evidence_file_ids` (ex. EP-01) et/ou hachages ; le [Validateur](../validator/index.md) vérifie l'intégrité référentielle. (4) **Ensemble minimal de soumission** : EV JSON + Dictionary + Summary + Change Log + Evidence Pack (zip). Voir [Modèle Evidence Pack](../standard/current/06-ev-template.md) pour les types de document EP-01..EP-07.

## Traçabilité

- **ID stables** : chaque enregistrement (EV, demande, revue, exception, renouvellement, entrée du journal des modifications) DOIT avoir un identifiant unique et stable.
- **Références croisées** : liez Demande → Revue → Exception (le cas échéant) → Renouvellement et liez les éléments EV à ceux-ci via des champs de référence (ex. `request_id`, `review_id`, `exception_id`, `renewal_id`).
- **Liaison** : assurez-vous que les auditeurs peuvent suivre une chaîne depuis une utilisation de l'IA (ou exception) jusqu'à la demande, l'approbation, toute exception et ses contrôles compensatoires et expiration, et le renouvellement.

## Comment les auditeurs utilisent ceci

Les auditeurs utilisent le lot de preuves pour vérifier que l'utilisation de l'IA est demandée, revue et approuvée ; que les exceptions sont limitées dans le temps et ont des contrôles compensatoires et un renouvellement ; et que les modifications sont journalisées. La TDM et les règles de traçabilité leur permettent de localiser les artefacts requis et de suivre les ID et références entre les enregistrements de demande, revue, exception, renouvellement et EV. Le résumé donne un aperçu rapide ; le journal des modifications soutient le contrôle des changements et la responsabilité.

Voir [Exigences minimales de preuves](minimum-evidence.md) pour les champs OBLIGATOIRES et les groupes de cycle de vie.

## Orientations opérationnelles

!!! info "Intégrité et contrôle d'accès"
    Bien que AIMO ne prescrive pas de contrôles spécifiques, les adopteurs doivent documenter :
    
    - **Rôles d'accès** : qui peut créer, lire, mettre à jour ou supprimer des preuves
    - **Politique de rétention** : combien de temps les preuves sont conservées et selon quel calendrier
    - **Mécanismes d'intégrité** : hachage, stockage WORM ou signatures numériques utilisés
    - **Piste d'audit** : journaux d'accès et de modifications du lot
    
    Voir [Exigences minimales de preuves > Intégrité et accès](minimum-evidence.md#6-integrity-access) pour des orientations détaillées.

## Parcours d'audit

Depuis cette page, le parcours d'audit typique continue :

1. **Suivant** : [Exigences minimales de preuves](minimum-evidence.md) — liste de contrôle OBLIGATOIRE par cycle de vie
2. **Ensuite** : [Carte de couverture](../coverage-map/index.md) — correspondance avec les cadres externes
3. **Valider** : [Validateur](../validator/index.md) — exécuter les vérifications structurelles
4. **Télécharger** : [Versions](../../releases/) — obtenir les actifs de version et vérifier les sommes de contrôle
