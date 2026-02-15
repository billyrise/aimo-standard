---
description: Correspondance AIMO Standard vers la loi sur l'IA de l'UE. Traçabilité entre les codes de taxonomie AIMO et les catégories de risque et exigences de la loi sur l'IA de l'UE.
---
<!-- aimo:translation_status=translated -->

# Correspondance loi sur l'IA de l'UE

> Raccourcis de traçabilité : Taxonomie → Exigences minimales de preuves → Validateur → Protocole de surveillance humaine.

- [Taxonomie](../../standard/current/03-taxonomy/)
- [Exigences minimales de preuves](../../artifacts/minimum-evidence/)
- [Schémas de journaux](../../artifacts/log-schemas/)
- [Validateur](../../validator/)
- [Protocole de surveillance humaine](../../governance/human-oversight-protocol/)

Cette page met en correspondance des thèmes sélectionnés de la loi sur l'IA de l'UE (documentation, tenue des dossiers, gestion des risques, surveillance humaine, transparence) avec les preuves et artefacts AIMO. Elle est uniquement de haut niveau et **ne constitue pas** un conseil juridique ni ne garantit la conformité. Vérifier par rapport au texte juridique officiel.

**Référence :** Règlement (UE) 2024/1689 (Loi sur l'intelligence artificielle). Tous les numéros d'article ci-dessous renvoient à ce règlement.

## Table de correspondance

| Référence du cadre / thème | Preuves AIMO / où dans AIMO | Paquet de preuves / Exigences minimales | Artefacts et validation | Notes |
| --- | --- | --- | --- | --- |
| Art. 4 – Littératie IA | [Périmètre](../../standard/current/02-scope/) | Summary, EV ; review | templates/ev/ | Transversal ; preuve de capacité/formation organisationnelle (haut niveau). Pas un conseil juridique. Vérifier contre le texte officiel. |
| Art. 9 – Système de gestion des risques | [Périmètre](../../standard/current/02-scope/) | request, review, exception, renewal | templates/ev/ | Systèmes d'IA à haut risque (Titre III). Pas un conseil juridique. Vérifier contre le texte officiel. |
| Art. 10 – Données et gouvernance des données | [Dictionnaire](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/ ; schema_validate_dictionary | Pas un conseil juridique. Vérifier contre le texte officiel. |
| Art. 11 – Documentation technique (haut risque) | [Modèle EV](../../standard/current/06-ev-template/), [Paquet de preuves](../../artifacts/evidence-bundle/) | EV, Dictionary, Summary ; request, review | schemas/jsonschema/, templates/ev/ ; **Annexe IV** : [Exemples > Échantillon Annexe IV UE](../../examples/) (`examples/evidence_bundle_v01_annex_iv_sample/`) ; profil : `coverage_map/profiles/eu_ai_act_annex_iv.json`. Paquet d'exemple conforme (signatures/, hashes/, payload avec documentation technique orientée Annexe IV). Voir Exemples (contenu supplémentaire dans une version future). | Haut niveau uniquement ; pas un conseil juridique. Vérifier contre le texte officiel. |
| Art. 12 – Tenue des dossiers | [Paquet de preuves](../../artifacts/evidence-bundle/), [Exigences minimales de preuves](../../artifacts/minimum-evidence/) | EV, change_log, request, review | examples/evidence_bundle_minimal/ ; schema_validate_ev | Pas un conseil juridique. Vérifier contre le texte officiel. |
| Art. 13 – Transparence et information aux déployeurs/utilisateurs | [Périmètre](../../standard/current/02-scope/) | Summary, EV ; review | templates/ev/ | Contexte à haut risque. Pas un conseil juridique. Vérifier contre le texte officiel. |
| Art. 14 – Surveillance humaine | [Exigences minimales de preuves](../../artifacts/minimum-evidence/) | review, exception | templates/ev/ev_template.md | Pas un conseil juridique. Vérifier contre le texte officiel. |
| Art. 15 – Exactitude, robustesse, cybersécurité | [Exigences minimales de preuves](../../artifacts/minimum-evidence/) | EV (codes de preuve/risque, haut niveau) | templates/ev/ | Correspondance haut niveau uniquement. Pas un conseil juridique. Vérifier contre le texte officiel. |
| Art. 17 – Système de management de la qualité | [Périmètre](../../standard/current/02-scope/) | Summary, review (processus organisationnel) | templates/ev/ | Distinct de l'art. 9 (système de gestion des risques). Pas un conseil juridique. Vérifier contre le texte officiel. |
| Obligations de transparence (selon le cas d'usage) | [Périmètre](../../standard/current/02-scope/), [Exigences minimales de preuves](../../artifacts/minimum-evidence/) | Summary, EV ; review | templates/ev/ | Les dispositions applicables dépendent du cas d'usage (p. ex. risque limité, obligations du déployeur). Pas un conseil juridique. Vérifier contre le texte officiel. |
| Obligations des modèles GPAI | [Modèle EV](../../standard/current/06-ev-template/), [Paquet de preuves](../../artifacts/evidence-bundle/) | Modèle EV, Paquet de preuves (cadre de structuration des preuves) | schemas/jsonschema/ ; schema_validate_ev | AIMO fournit un cadre pour organiser les preuves ; les obligations réelles sont définies par le règlement. Pas un conseil juridique. Vérifier contre le texte officiel. |
| Considérants – Responsabilité | [Paquet de preuves](../../artifacts/evidence-bundle/) | EV, request, review, change_log | examples/evidence_bundle_minimal/ ; schema_validate_ev | Pas un conseil juridique. Vérifier contre le texte officiel. |

## Dates d'application / applicabilité (haut niveau)

Ce qui suit s'aligne sur le **calendrier officiel de l'UE** (Service de la loi sur l'IA / Commission). Ce **n'est pas un conseil juridique** et ne garantit pas l'exactitude. Toujours confirmer avec le **texte juridique officiel** et les autorités compétentes.

| Phase | Date | Ce qui s'applique (haut niveau) |
| --- | --- | --- |
| Entrée en vigueur | Août 2024 | Règlement en vigueur ; la plupart des obligations substantielles pas encore applicables. |
| Dispositions générales et interdictions | 02 fév 2025 | Pratiques interdites (risque inacceptable) ; certaines dispositions liées à la littératie IA. |
| Règles GPAI et gouvernance | 02 août 2025 | Règles sur les organismes notifiés, GPAI, gouvernance, confidentialité, sanctions ; codes de conduite. |
| Règles principales + Annexe III haut risque + Art. 50 transparence | 02 août 2026 | Applicabilité complète pour les systèmes d'IA à haut risque (Annexe III), obligations de transparence de l'art. 50. |
| Haut risque intégré dans les produits réglementés | 02 août 2027 | Systèmes d'IA à haut risque intégrés dans des produits soumis à la législation européenne sur les produits. |

## Normes harmonisées et présomption de conformité (art. 40)

Lorsque des **normes harmonisées** sont publiées au Journal officiel de l'UE au titre de la loi sur l'IA, leur conformité peut conférer une **présomption de conformité** aux exigences correspondantes. La liste et les dates exactes dépendent des travaux de normalisation et de la publication au JO. Les correspondances AIMO sont informatives et ne confèrent pas de présomption de conformité. Pour l'état actuel, voir les sources de la Commission et du Bureau de l'IA dans **Références** ci-dessous.

## Lignes directrices 2026 du Bureau de l'IA (détail de mise en œuvre)

La Commission européenne a indiqué que le **Bureau de l'IA** préparera des **lignes directrices pratiques** en 2026, notamment sur :

- Classification des risques élevés
- Mise en œuvre de l'art. 50 (transparence)
- Signalement des incidents
- Éléments liés au SMQ

Ces lignes directrices sont des **déclencheurs de mise à jour** pour les profils et correspondances de couverture AIMO : une fois publiées, les adoptants doivent aligner les preuves et correspondances sur la dernière orientation officielle. AIMO n'interprète ni ne garantit la conformité à ces lignes directrices.

!!! warning "Pas un conseil juridique"
    Cette page est à usage explicatif uniquement. Vous devez vérifier l'applicabilité et les dates par rapport au règlement officiel et à tout acte d'exécution ou de modification. AIMO ne fournit pas de conseil juridique ni ne garantit la conformité.

## Références

- [Règlement (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689) (EUR-Lex) — Loi sur l'intelligence artificielle
- [Calendrier de mise en œuvre de la loi sur l'IA de l'UE](https://artificialintelligenceact.eu/implementation-timeline) (Service de la loi sur l'IA / aligné Commission ; informatif)
- Commission européenne / Bureau de l'IA — lignes directrices et calendrier (vérifier les actualités de la Commission et le Service de la loi sur l'IA pour les URL actuelles)
- [EPRS — Mise en œuvre de la loi sur l'IA de l'UE](https://www.europarl.europa.eu/thinktank/) — briefing du Parlement (informatif)
