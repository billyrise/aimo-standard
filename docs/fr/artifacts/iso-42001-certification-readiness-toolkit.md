---
description: Boîte à outils de préparation à la certification ISO/IEC 42001. Parcours le plus court vers des preuves prêtes pour l'audit alignées sur l'ISO 42001 avec les artefacts AIMO. Soutient uniquement la préparation ; ne confère pas de certification.
---
<!-- aimo:translation_status=translated -->

# Boîte à outils de préparation à la certification ISO/IEC 42001

Cette page est un guide **pratique et orienté adoption** pour produire des **preuves prêtes pour l'audit** alignées sur l'ISO/IEC 42001 en utilisant les artefacts AIMO. Elle **soutient la préparation** ; elle **ne confère pas** de certification. Les décisions de certification restent du ressort des **organismes de certification accrédités**.

## Objectif

Produire un Evidence Bundle structuré et vérifié par le validateur qui soutient les contrôles de type ISO/IEC 42001 (contexte, leadership, planification, soutien, exploitation, évaluation des performances, amélioration), afin que les auditeurs puissent localiser et vérifier les preuves efficacement.

## Workflow en 5 étapes

| Étape | Action |
| --- | --- |
| **1. Établir le périmètre et l'inventaire IA** | Définir le périmètre (scope_ref) ; classer les systèmes d'IA avec la [taxonomie](../../standard/current/03-taxonomy/) et le [dictionnaire](../../standard/current/05-dictionary/). |
| **2. Définir les artefacts du système de management** | Créer ou référencer des politiques, rôles et artefacts alignés PDCA. Utiliser [AIMO-MS / AIMO-Controls](../../conformance/) comme structure ; référencer le [modèle Evidence Pack](../../standard/current/06-ev-template/) (EP-01..EP-07). |
| **3. Produire l'Evidence Bundle et les preuves minimales** | Construire manifest, object_index, payload_index, hash_chain, signing selon la [structure du lot de preuves](../../standard/current/09-evidence-bundle-structure/). Inclure request, review, exception, renewal, change_log selon les [Exigences minimales de preuves](minimum-evidence.md). |
| **4. Exécuter le validateur + checksums + maîtrise des changements** | Exécuter `python validator/src/validate.py <bundle_path> --validate-profiles`. Consigner la version du validateur et la sortie. Générer les checksums SHA-256 ; maintenir les entrées du journal des modifications qui référencent les objets impactés. |
| **5. Préparer le pack d'audit** | Empaqueter le lot (zip ou équivalent) ; fournir les checksums. Joindre optionnellement la [sortie du rapport d'audit](../../standard/current/07-validator/) (audit-json / audit-html). Utiliser des URL versionnées (ex. `/0.1.2/`) pour citer la norme. Pour le niveau Audit-Ready, ajouter [Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index) et [External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is). |

## Liste de contrôle : famille de clauses ISO 42001 → artefacts AIMO → sorties de preuves

| Famille de clauses ISO 42001 | Artefacts AIMO | Sorties de preuves |
| --- | --- | --- |
| Contexte (4.1) | Summary, Dictionary, scope_ref | scope_ref du manifeste ; Summary ; Dictionary |
| Leadership / Politique (5.x) | Summary, review, dictionary | Enregistrements de revue ; références à la politique |
| Planification (6.x) | request, review, exception, EV, Dictionary | Demande/approbation ; risque/objectifs dans EV ou Dictionary |
| Soutien (7.x) | Summary, review, EV, change_log | Documentation ; preuves de compétence/sensibilisation |
| Exploitation (8.x) | EV, request, review, exception | Contrôles opérationnels ; applicabilité |
| Évaluation des performances (9.x) | EV, change_log, review, renewal | Surveillance ; audit interne ; revue de direction |
| Amélioration (10.x) | exception, renewal, change_log | Action corrective ; amélioration continue |

Voir [Coverage Map — ISO/IEC 42001](../../coverage-map/iso-42001/) et [ISO/IEC 42006](https://www.iso.org/standard/42006) pour les attentes des organismes d'audit.

## Formulation sûre

- **À utiliser :** « Nous utilisons les artefacts AIMO pour soutenir la préparation à l'ISO/IEC 42001 ; les décisions de certification restent du ressort des organismes de certification accrédités. »
- **À ne pas utiliser :** « ISO 42001 certifié par AIMO » ou « AIMO certifie la conformité ».

## Voir aussi

- [Conformité](../../conformance/) — Niveaux (Foundation, Operational, Audit-Ready) et libellé de déclaration
- [Trust Package](../../governance/trust-package/) — Documents prêts pour l'auditeur
- [Responsibility Boundary](../../governance/responsibility-boundary/) — Ce qu'AIMO fournit et ne fournit pas
