---
description: Superpositions d'approvisionnement et de divulgation (Royaume-Uni, Japon). ATRS UK, orientation d'approvisionnement UK, approvisionnement GenAI du gouvernement japonais et lignes directrices commerciales IA. Correspondance de référence uniquement.
---
<!-- aimo:translation_status=translated -->

# Superpositions d'approvisionnement et de divulgation (Royaume-Uni, Japon)

Cette page décrit les **correspondances de référence** entre les preuves AIMO et les cadres d'approvisionnement et de divulgation sélectionnés du **Royaume-Uni** et du **Japon**. L'objectif est de **réduire la charge par la réutilisation des preuves AIMO**. Il s'agit d'une **correspondance informative uniquement** ; AIMO ne garantit pas la conformité complète aux exigences gouvernementales. Vérifiez par rapport aux sources officielles ci-dessous.

## Sources primaires

**Royaume-Uni**

- [Algorithmic Transparency Recording Standard (ATRS) Hub](https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub) — GOV.UK (modèle, orientation, registres publiés)
- [Modèle ATRS](https://www.gov.uk/government/publications/algorithmic-transparency-template) — Modèle officiel pour le secteur public
- [Orientation pour les organisations utilisant l'ATRS](https://www.gov.uk/government/publications/guidance-for-organisations-using-the-algorithmic-transparency-standard/algorithmic-transparency-recording-standard-guidance-for-public-sector-bodies) — GOV.UK

**Japon**

- [Digital Agency — GenAI procurement and utilisation guideline](https://www.digital.go.jp/news/3579c42d-b11c-4756-b66e-3d3e35175623) — Digital Agency (Cabinet Secretariat)
- [AI Business Guidelines](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/index.html) — METI / MIC (Ministry of Economy, Trade and Industry / Ministry of Internal Affairs and Communications)

## Table de correspondance (Royaume-Uni)

| Exigence gouvernementale (thème) | Artefacts AIMO | Où dans le Evidence Bundle | Couverture du validateur | Note |
| --- | --- | --- | --- | --- |
| ATRS — responsabilité / propriétaire | Summary, review | manifest ; objects/ (EV, Summary) ; payload_index | schema_validate_ev | Correspondance informative ; ne garantit pas la conformité complète. |
| ATRS — description système / modèle | Dictionary, EV | objects/ ; schemas/jsonschema/aimo-dictionary.schema.json | schema_validate_dictionary | Joindre le registre ATRS officiel dans External Forms ; lier par logical_id. |
| ATRS — considérations de risque | Dictionary, request, review, exception | objects/ ; templates/ev/ | schema_validate_ev | Profil : `coverage_map/profiles/uk_atrs_procurement.json`. |
| Approvisionnement — preuves fournisseur | request, review, exception ; Evidence Bundle | manifest, object_index, payload_index ; examples/evidence_bundle_minimal/ | schema_validate_ev | Utiliser le paquet pour structurer les preuves ; l'orientation UK reste l'autorité. |

## Table de correspondance (Japon)

| Exigence gouvernementale (thème) | Artefacts AIMO | Où dans le Evidence Bundle | Couverture du validateur | Note |
| --- | --- | --- | --- | --- |
| Liste de contrôle d'approvisionnement GenAI (Digital Agency) | External Form (liste telle quelle) ; Dictionary, Summary | payload_index ; section External Forms ; référence dans manifest | N/A (pièce jointe) | Correspondance informative ; ne garantit pas la conformité complète. Profil : `coverage_map/profiles/jp_gov_genai_procurement.json`. |
| AI Business Guidelines — gouvernance / traçabilité | Summary, dictionary, request, review, change_log | objects/ ; manifest ; templates/ev/ | schema_validate_dictionary, schema_validate_ev | Mapper les éléments de la liste à la taxonomie AIMO lorsque utile. |
| Documentation risque / responsabilité | Dictionary, EV, review, exception | objects/ ; schemas/jsonschema/ | schema_validate_ev | Vérifier par rapport à l'orientation officielle de Digital Agency et METI/MIC. |

## Royaume-Uni : ATRS et approvisionnement en IA (résumé)

| Thème | Preuves AIMO / correspondance | Notes |
| --- | --- | --- |
| **ATRS UK** (registre de transparence IA) | Summary, review (responsable de la responsabilité), evidence (description modèle/système), dictionary (considérations de risque). Profil : `coverage_map/profiles/uk_atrs_procurement.json`. | Joindre ou référencer un registre de transparence de type ATRS dans les formulaires externes ; lier aux objets du paquet par logical_id. |
| **Orientation d'approvisionnement UK** | Request, review, exception ; Paquet de preuves pour l'évaluation des fournisseurs. | Utiliser le paquet AIMO pour structurer les preuves pour l'évaluation d'approvisionnement ; l'orientation officielle UK reste l'autorité. |

## Japon : Approvisionnement GenAI du gouvernement et lignes directrices commerciales IA (résumé)

| Thème | Preuves AIMO / correspondance | Notes |
| --- | --- | --- |
| **Liste de contrôle d'approvisionnement GenAI du gouvernement JP** | Joindre la liste comme formulaire externe (p. ex. payload : JP_PROCUREMENT_CHECKLIST) ; référencer dans le manifest. Profil : `coverage_map/profiles/jp_gov_genai_procurement.json`. | Correspondance de référence uniquement ; AIMO ne remplace pas les listes officielles. |
| **Lignes directrices commerciales IA** | Summary, dictionary ; mapper les éléments de la liste aux codes de taxonomie AIMO lorsque utile pour la traçabilité. | Utiliser pour l'explicabilité ; vérifier par rapport à l'orientation officielle japonaise. |

## Comment utiliser

- **Formulaires externes** : Joindre les modèles/listes officiels UK ou Japon **tels quels** (PDF, DOC, etc.), les hasher et les lister dans le [payload_index](../../standard/current/09-evidence-bundle-structure/) du Paquet de preuves ou dans la [section Formulaires externes du modèle EV](../../standard/current/06-ev-template/). Les référencer par logical_id dans le manifest et dans les correspondances de couverture.
- **Profils** : Les profils ci-dessus définissent des correspondances optionnelles lisibles par machine ; ils n'imposent pas d'obligations légales ou contractuelles.

Voir [Conformité](../../conformance/) pour les niveaux et [Exigences minimales de preuves — Superpositions réglementaires](../../artifacts/minimum-evidence/) pour le résumé des superpositions.
