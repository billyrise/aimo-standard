---
description: Correspondance du standard AIMO avec NIST AI RMF. Traçabilité entre les codes de taxonomie AIMO et les fonctions du cadre de gestion des risques IA du NIST.
---
<!-- aimo:translation_status=translated -->

# Correspondance NIST AI RMF

> Raccourcis de traçabilité : Taxonomie → Exigences minimales de preuves → Validateur → Protocole de surveillance humaine.

- [Taxonomie](../../standard/current/03-taxonomy/)
- [Exigences minimales de preuves](../../artifacts/minimum-evidence/)
- [Schémas de journaux](../../artifacts/log-schemas/)
- [Validateur](../../validator/)
- [Protocole de surveillance humaine](../../governance/human-oversight-protocol/)

Cette page met en correspondance des thèmes sélectionnés du NIST AI Risk Management Framework (Govern, Map, Measure, Manage) avec les preuves et artefacts AIMO. C'est uniquement pour l'explicabilité ; cela ne garantit pas la conformité au NIST AI RMF. Vérifiez par rapport à la publication NIST.


## Table de correspondance

| Référence du cadre / sujet | Preuve AIMO / où dans AIMO | Lot de preuves / Preuves minimales | Artefacts et validation | Notes |
| --- | --- | --- | --- | --- |
| Govern 1.1 – Politiques | [Périmètre](../../standard/current/02-scope/), [Taxonomie](../../standard/current/03-taxonomy/) | Dictionary, Summary, revue; revue | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informatif ; vérifiez par rapport à la publication NIST. |
| Govern 1.2 – Rôles et responsabilités | [Preuves minimales](../../artifacts/minimum-evidence/) | demande, revue | templates/ev/ev_template.md | Informatif ; vérifiez par rapport à la publication NIST. |
| Govern 2.1 – Responsabilité | [Lot de preuves](../../artifacts/evidence-bundle/) | EV, demande, revue, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | Informatif ; vérifiez par rapport à la publication NIST. |
| Govern 3.1 – Gestion des risques | [Périmètre](../../standard/current/02-scope/) | demande, revue, exception | templates/ev/ | Informatif ; vérifiez par rapport à la publication NIST. |
| Govern 4.1 – Culture | [Vue d'ensemble](../../standard/current/01-overview/) | Summary, revue; revue | — | Informatif ; vérifiez par rapport à la publication NIST. |
| Map 1.1 – Cartographie du contexte | [Périmètre](../../standard/current/02-scope/), [Dictionnaire](../../standard/current/05-dictionary/) | Dictionary, Summary; demande | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informatif ; vérifiez par rapport à la publication NIST. |
| Map 2.1 – Données et documentation | [Modèle EV](../../standard/current/06-ev-template/) | EV, Dictionary, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informatif ; vérifiez par rapport à la publication NIST. |
| Map 3.1 – Gouvernance des données | [Dictionnaire](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informatif ; vérifiez par rapport à la publication NIST. |
| Measure 1.1 – Performance et impact | [Modèle EV](../../standard/current/06-ev-template/) | EV | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informatif ; vérifiez par rapport à la publication NIST. |
| Measure 2.1 – Surveillance | [Preuves minimales](../../artifacts/minimum-evidence/) | EV, change_log; change_log, intégrité | templates/ev/ | Informatif ; vérifiez par rapport à la publication NIST. |
| Measure 3.1 – Tests et validation | [Validateur](../../standard/current/07-validator/) | EV | validator/rules/, validator/src/; schema_validate_ev | Informatif ; vérifiez par rapport à la publication NIST. |
| Manage 1.1 – Allocation des ressources | [Vue d'ensemble](../../standard/current/01-overview/) | Summary, revue; revue | — | Informatif ; vérifiez par rapport à la publication NIST. |
| Manage 2.1 – Incidents et réponses | [Preuves minimales](../../artifacts/minimum-evidence/) | exception, renouvellement, change_log | templates/ev/ev_template.md | Informatif ; vérifiez par rapport à la publication NIST. |
| Manage 3.1 – Gestion des changements | [Lot de preuves](../../artifacts/evidence-bundle/) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | Informatif ; vérifiez par rapport à la publication NIST. |
| Manage 4.1 – Revue et mise à jour | [Preuves minimales](../../artifacts/minimum-evidence/) | renouvellement, revue; revue, renouvellement | templates/ev/ | Informatif ; vérifiez par rapport à la publication NIST. |
| Manage 5.1 – Communication | [Lot de preuves](../../artifacts/evidence-bundle/) | Summary, change_log; change_log | templates/ev/ | Informatif ; vérifiez par rapport à la publication NIST. |
