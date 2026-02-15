---
description: Correspondance du standard AIMO avec ISMS (ISO 27001/27002). Traçabilité entre la taxonomie AIMO et les contrôles du système de management de la sécurité de l'information.
---
<!-- aimo:translation_status=translated -->

# Vue ISMS (ISO/IEC 27001/27002) - Correspondance

> Raccourcis de traçabilité : Taxonomie → Exigences minimales de preuves → Validateur → Protocole de surveillance humaine.

- [Taxonomie](../../standard/current/03-taxonomy/)
- [Exigences minimales de preuves](../../artifacts/minimum-evidence/)
- [Schémas de journaux](../../artifacts/log-schemas/)
- [Validateur](../../validator/)
- [Protocole de surveillance humaine](../../governance/human-oversight-protocol/)

Cette page met en correspondance des thèmes sélectionnés ISO/IEC 27001/27002 (gestion des changements, contrôle d'accès, journalisation, intégrité des preuves) avec les preuves et artefacts AIMO. C'est uniquement pour l'explicabilité ; cela ne garantit pas la conformité à ISO/IEC 27001 ou 27002. Vérifiez par rapport aux normes publiées.


## Table de correspondance

| Référence du cadre / sujet | Preuve AIMO / où dans AIMO | Lot de preuves / Preuves minimales | Artefacts et validation | Notes |
| --- | --- | --- | --- | --- |
| A.5.24 – Sécurité de l'information dans la gestion de projet | [Périmètre](../../standard/current/02-scope/) | demande, revue | templates/ev/ | Informatif ; vérifiez par rapport au texte officiel. |
| A.5.29 – Sécurité de l'information pendant les perturbations | [Preuves minimales](../../artifacts/minimum-evidence/) | exception, renouvellement | templates/ev/ev_template.md | Informatif ; vérifiez par rapport au texte officiel. |
| A.5.30 – Préparation des TIC pour la continuité d'activité | [Vue d'ensemble](../../standard/current/01-overview/) | Summary; intégrité | — | Informatif ; vérifiez par rapport au texte officiel. |
| A.8.1 – Inventaire des actifs | [Dictionnaire](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informatif ; vérifiez par rapport au texte officiel. |
| A.8.2 – Classification de l'information | [Taxonomie](../../standard/current/03-taxonomy/) | Dictionary; revue | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informatif ; vérifiez par rapport au texte officiel. |
| A.8.3 – Contrôle d'accès | [Preuves minimales](../../artifacts/minimum-evidence/) | —; intégrité | — | Informatif ; vérifiez par rapport au texte officiel. |
| A.8.15 – Journalisation | [Modèle EV](../../standard/current/06-ev-template/) | EV, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informatif ; vérifiez par rapport au texte officiel. |
| A.8.16 – Activités de surveillance | [Preuves minimales](../../artifacts/minimum-evidence/) | EV, change_log; change_log, intégrité | templates/ev/ | Informatif ; vérifiez par rapport au texte officiel. |
| A.8.32 – Gestion des changements | [Lot de preuves](../../artifacts/evidence-bundle/) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | Informatif ; vérifiez par rapport au texte officiel. |
| A.8.33 – Informations de test | [Validateur](../../standard/current/07-validator/) | EV | validator/rules/, validator/src/; schema_validate_ev | Informatif ; vérifiez par rapport au texte officiel. |
