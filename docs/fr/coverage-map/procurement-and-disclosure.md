---
description: Superpositions d'approvisionnement et de divulgation (Royaume-Uni, Japon). ATRS UK, orientation d'approvisionnement UK, approvisionnement GenAI du gouvernement japonais et lignes directrices commerciales IA. Correspondance de référence uniquement.
---
<!-- aimo:translation_status=translated -->

# Superpositions d'approvisionnement et de divulgation (Royaume-Uni, Japon)

Cette page décrit les **correspondances de référence** entre les preuves AIMO et les cadres d'approvisionnement et de divulgation sélectionnés du **Royaume-Uni** et du **Japon**. Il s'agit **uniquement de correspondance de référence** ; AIMO ne remplace pas les listes de contrôle officielles ni l'orientation gouvernementale.

## Royaume-Uni : ATRS et approvisionnement en IA

| Thème | Preuves AIMO / correspondance | Notes |
| --- | --- | --- |
| **ATRS UK** (registre de transparence IA) | Summary, review (responsable de la responsabilité), evidence (description modèle/système), dictionary (considérations de risque). Profil : `coverage_map/profiles/uk_atrs_procurement.json`. | Joindre ou référencer un registre de transparence de type ATRS dans les formulaires externes ; lier aux objets du paquet par logical_id. |
| **Orientation d'approvisionnement UK** | Request, review, exception ; Paquet de preuves pour l'évaluation des fournisseurs. | Utiliser le paquet AIMO pour structurer les preuves pour l'évaluation d'approvisionnement ; l'orientation officielle UK reste l'autorité. |

## Japon : Approvisionnement GenAI du gouvernement et lignes directrices commerciales IA

| Thème | Preuves AIMO / correspondance | Notes |
| --- | --- | --- |
| **Liste de contrôle d'approvisionnement GenAI du gouvernement JP** | Joindre la liste comme formulaire externe (p. ex. payload : JP_PROCUREMENT_CHECKLIST) ; référencer dans le manifest. Profil : `coverage_map/profiles/jp_gov_genai_procurement.json`. | Correspondance de référence uniquement ; AIMO ne remplace pas les listes officielles. |
| **Lignes directrices commerciales IA** | Summary, dictionary ; mapper les éléments de la liste aux codes de taxonomie AIMO lorsque utile pour la traçabilité. | Utiliser pour l'explicabilité ; vérifier par rapport à l'orientation officielle japonaise. |

## Comment utiliser

- **Formulaires externes** : Joindre les modèles/listes officiels UK ou Japon **tels quels** (PDF, DOC, etc.), les hasher et les lister dans le [payload_index](../../standard/current/09-evidence-bundle-structure/) du Paquet de preuves ou dans la [section Formulaires externes du modèle EV](../../standard/current/06-ev-template/). Les référencer par logical_id dans le manifest et dans les correspondances de couverture.
- **Profils** : Les profils ci-dessus définissent des correspondances optionnelles lisibles par machine ; ils n'imposent pas d'obligations légales ou contractuelles.

Voir [Conformité](../../conformance/) pour les niveaux et [Exigences minimales de preuves — Superpositions réglementaires](../../artifacts/minimum-evidence/) pour le résumé des superpositions.
