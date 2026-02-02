---
description: Correspondance du standard AIMO avec NIST AI RMF. Traçabilité entre les codes de taxonomie AIMO et les fonctions du cadre de gestion des risques IA du NIST.
---

# Correspondance NIST AI RMF

> Raccourcis de traçabilité : Taxonomie → Exigences minimales de preuves → Validateur → Protocole de surveillance humaine.

- [Taxonomie](../standard/current/03-taxonomy.md)
- [Exigences minimales de preuves](../artifacts/minimum-evidence.md)
- [Schémas de journaux](../artifacts/log-schemas/index.md)
- [Validateur](../validator/index.md)
- [Protocole de surveillance humaine](../governance/human-oversight-protocol.md)

Cette page met en correspondance des thèmes sélectionnés du NIST AI Risk Management Framework (Govern, Map, Measure, Manage) avec les preuves et artefacts AIMO. C'est uniquement pour l'explicabilité ; cela ne garantit pas la conformité au NIST AI RMF. Vérifiez par rapport à la publication NIST.


## Table de correspondance

| Référence du cadre / sujet | Preuve AIMO / où dans AIMO | Lot de preuves / Preuves minimales | Artefacts et validation | Notes |
| --- | --- | --- | --- | --- |
| Govern 1.1 – Politiques | [Périmètre](../standard/current/02-scope.md), [Taxonomie](../standard/current/03-taxonomy.md) | Dictionary, Summary, revue; revue | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informatif ; vérifiez par rapport à la publication NIST. |
| Govern 1.2 – Rôles et responsabilités | [Preuves minimales](../artifacts/minimum-evidence.md) | demande, revue | templates/ev/ev_template.md | Informatif ; vérifiez par rapport à la publication NIST. |
| Govern 2.1 – Responsabilité | [Lot de preuves](../artifacts/evidence-bundle.md) | EV, demande, revue, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | Informatif ; vérifiez par rapport à la publication NIST. |
| Govern 3.1 – Gestion des risques | [Périmètre](../standard/current/02-scope.md) | demande, revue, exception | templates/ev/ | Informatif ; vérifiez par rapport à la publication NIST. |
| Govern 4.1 – Culture | [Vue d'ensemble](../standard/current/01-overview.md) | Summary, revue; revue | — | Informatif ; vérifiez par rapport à la publication NIST. |
| Map 1.1 – Cartographie du contexte | [Périmètre](../standard/current/02-scope.md), [Dictionnaire](../standard/current/05-dictionary.md) | Dictionary, Summary; demande | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informatif ; vérifiez par rapport à la publication NIST. |
| Map 2.1 – Données et documentation | [Modèle EV](../standard/current/06-ev-template.md) | EV, Dictionary, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informatif ; vérifiez par rapport à la publication NIST. |
| Map 3.1 – Gouvernance des données | [Dictionnaire](../standard/current/05-dictionary.md) | Dictionary, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informatif ; vérifiez par rapport à la publication NIST. |
| Measure 1.1 – Performance et impact | [Modèle EV](../standard/current/06-ev-template.md) | EV | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informatif ; vérifiez par rapport à la publication NIST. |
| Measure 2.1 – Surveillance | [Preuves minimales](../artifacts/minimum-evidence.md) | EV, change_log; change_log, intégrité | templates/ev/ | Informatif ; vérifiez par rapport à la publication NIST. |
| Measure 3.1 – Tests et validation | [Validateur](../standard/current/07-validator.md) | EV | validator/rules/, validator/src/; schema_validate_ev | Informatif ; vérifiez par rapport à la publication NIST. |
| Manage 1.1 – Allocation des ressources | [Vue d'ensemble](../standard/current/01-overview.md) | Summary, revue; revue | — | Informatif ; vérifiez par rapport à la publication NIST. |
| Manage 2.1 – Incidents et réponses | [Preuves minimales](../artifacts/minimum-evidence.md) | exception, renouvellement, change_log | templates/ev/ev_template.md | Informatif ; vérifiez par rapport à la publication NIST. |
| Manage 3.1 – Gestion des changements | [Lot de preuves](../artifacts/evidence-bundle.md) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | Informatif ; vérifiez par rapport à la publication NIST. |
| Manage 4.1 – Revue et mise à jour | [Preuves minimales](../artifacts/minimum-evidence.md) | renouvellement, revue; revue, renouvellement | templates/ev/ | Informatif ; vérifiez par rapport à la publication NIST. |
| Manage 5.1 – Communication | [Lot de preuves](../artifacts/evidence-bundle.md) | Summary, change_log; change_log | templates/ev/ | Informatif ; vérifiez par rapport à la publication NIST. |
