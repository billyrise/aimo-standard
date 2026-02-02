---
description: Correspondance du standard AIMO avec l'EU AI Act. Traçabilité entre les codes de taxonomie AIMO et les catégories de risque et exigences de l'EU AI Act.
---

# Correspondance EU AI Act

> Raccourcis de traçabilité : Taxonomie → Exigences minimales de preuves → Validateur → Protocole de surveillance humaine.

- [Taxonomie](../standard/current/03-taxonomy.md)
- [Exigences minimales de preuves](../artifacts/minimum-evidence.md)
- [Schémas de journaux](../artifacts/log-schemas/index.md)
- [Validateur](../validator/index.md)
- [Protocole de surveillance humaine](../governance/human-oversight-protocol.md)

Cette page met en correspondance des thèmes sélectionnés de l'EU AI Act (documentation, tenue de registres, gestion des risques, surveillance humaine, transparence) avec les preuves et artefacts AIMO. C'est uniquement de haut niveau et ne constitue **pas** un avis juridique ni ne garantit la conformité. Vérifiez par rapport au texte juridique officiel.


## Table de correspondance

| Référence du cadre / sujet | Preuve AIMO / où dans AIMO | Lot de preuves / Preuves minimales | Artefacts et validation | Notes |
| --- | --- | --- | --- | --- |
| Art 9 – Gestion des risques (obligations) | [Périmètre](../standard/current/02-scope.md) | demande, revue, exception | templates/ev/ | Haut niveau uniquement ; pas d'avis juridique. Vérifiez par rapport au texte officiel. |
| Art 10 – Gouvernance des données | [Dictionnaire](../standard/current/05-dictionary.md) | Dictionary, EV | schemas/jsonschema/; schema_validate_dictionary | Haut niveau uniquement ; pas d'avis juridique. Vérifiez par rapport au texte officiel. |
| Art 11 – Documentation (haut risque) | [Modèle EV](../standard/current/06-ev-template.md), [Lot de preuves](../artifacts/evidence-bundle.md) | EV, Dictionary, Summary; demande, revue | schemas/jsonschema/, templates/ev/; schema_validate_ev | Haut niveau uniquement ; pas d'avis juridique. Vérifiez par rapport au texte officiel. |
| Art 12 – Tenue de registres | [Lot de preuves](../artifacts/evidence-bundle.md), [Preuves minimales](../artifacts/minimum-evidence.md) | EV, change_log, demande, revue | examples/evidence_bundle_minimal/; schema_validate_ev | Haut niveau uniquement ; pas d'avis juridique. Vérifiez par rapport au texte officiel. |
| Art 13 – Transparence (information utilisateur) | [Périmètre](../standard/current/02-scope.md) | Summary, EV; revue | templates/ev/ | Haut niveau uniquement ; pas d'avis juridique. Vérifiez par rapport au texte officiel. |
| Art 14 – Surveillance humaine | [Preuves minimales](../artifacts/minimum-evidence.md) | revue, exception; revue, exception | templates/ev/ev_template.md | Haut niveau uniquement ; pas d'avis juridique. Vérifiez par rapport au texte officiel. |
| Art 17 – Gestion des risques (haut risque) | [Périmètre](../standard/current/02-scope.md) | demande, revue, exception, renouvellement | templates/ev/ | Haut niveau uniquement ; pas d'avis juridique. Vérifiez par rapport au texte officiel. |
| Art 26 – Transparence (risque limité) | [Périmètre](../standard/current/02-scope.md) | Summary, EV; revue | templates/ev/ | Haut niveau uniquement ; pas d'avis juridique. Vérifiez par rapport au texte officiel. |
| Art 29 – Documentation (IA à usage général) | [Modèle EV](../standard/current/06-ev-template.md) | EV, Dictionary, Summary; demande, revue | schemas/jsonschema/; schema_validate_ev | Haut niveau uniquement ; pas d'avis juridique. Vérifiez par rapport au texte officiel. |
| Art 52 – Transparence (déployeur) | [Preuves minimales](../artifacts/minimum-evidence.md) | EV, Summary; revue | templates/ev/ | Haut niveau uniquement ; pas d'avis juridique. Vérifiez par rapport au texte officiel. |
| Considérants – Responsabilité | [Lot de preuves](../artifacts/evidence-bundle.md) | EV, demande, revue, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | Haut niveau uniquement ; pas d'avis juridique. Vérifiez par rapport au texte officiel. |
