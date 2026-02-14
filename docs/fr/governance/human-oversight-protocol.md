---
description: Protocole de surveillance humaine AIMO - Limite entre validation automatisée et revue humaine. Responsabilités du jugement machine vs humain dans la gouvernance IA.
---

# Protocole de surveillance humaine

Cette page définit la limite entre ce que la validation automatisée (validateur) peut vérifier et ce qui nécessite une revue humaine (humain dans la boucle). Elle clarifie les responsabilités du jugement machine vs humain dans les processus de preuves de gouvernance IA.

## Objectif

Les outils de validation automatisée peuvent efficacement vérifier la correction structurelle et syntaxique, mais ne peuvent pas remplacer le jugement humain pour les décisions dépendantes du contexte. Ce protocole :

- Clarifie ce que le validateur peut et ne peut pas vérifier
- Définit le périmètre de la revue humaine requise pour une gouvernance efficace
- Soutient les explications d'audit en documentant le processus de surveillance humaine
- Fournit un cadre pour les organisations implémentant des flux de travail de gouvernance IA

## Ce que la validation automatisée peut faire (périmètre du validateur)

Le validateur AIMO et les outils automatisés similaires peuvent vérifier :

| Capacité | Description |
| --- | --- |
| **Complétude des champs/documents requis** | Vérifier que tous les champs obligatoires sont présents dans les manifestes, enregistrements EV et autres artefacts |
| **Cohérence structurelle** | Valider les références, ID et liens croisés entre artefacts (ex. request_id → review_id) |
| **Validation de schéma** | Vérifier que les artefacts JSON/YAML sont conformes aux schémas définis |
| **Validation du format de code** | Vérifier que les codes de taxonomie correspondent aux patterns attendus (ex. `UC-001`) |
| **Vérifications d'intégrité** | Valider le format et la présence du hash (pas le recalcul par rapport au contenu) |
| **Validation du dictionnaire** | Confirmer que les codes existent dans le dictionnaire de taxonomie |

Voir [Validateur](../../standard/current/07-validator/) pour les règles de validation détaillées et l'implémentation de référence.

## Ce qui nécessite une revue humaine (périmètre humain dans la boucle)

Les domaines suivants nécessitent un jugement humain et ne peuvent pas être automatisés :

| Capacité | Description |
| --- | --- |
| **Jugement de risque dépendant du contexte** | Évaluer les risques métier, éthiques et opérationnels basés sur le contexte organisationnel |
| **Justification d'approbation d'exception** | Évaluer si une exception est justifiée et si les contrôles compensatoires sont adéquats |
| **Prise de décision de remédiation** | Prioriser les corrections, allouer les ressources et déterminer les délais |
| **Arbitrages de politique** | Équilibrer les exigences concurrentes (ex. rapidité vs rigueur, coût vs risque) |
| **Acceptation du risque résiduel** | Décider si les risques restants sont acceptables après les contrôles |
| **Évaluation d'impact inter-domaines** | Évaluer les implications pour le juridique, les RH, les opérations et autres fonctions |
| **Vérification de l'exactitude du contenu** | Confirmer que le contenu des preuves est factuellement correct et complet |
| **Communication avec les parties prenantes** | Expliquer les décisions aux auditeurs, régulateurs et direction |

## Limite de responsabilité

| Aspect | Validateur (machine) | Réviseur humain |
| --- | --- | --- |
| **Structure** | ✓ Peut vérifier | Revoir si signalé |
| **Complétude** | ✓ Peut vérifier les champs | Vérifier l'adéquation du contenu |
| **Format** | ✓ Peut vérifier | — |
| **Jugement de risque** | ✗ Ne peut pas évaluer | ✓ Doit évaluer |
| **Approbation d'exception** | ✗ Ne peut pas décider | ✓ Doit décider |
| **Priorité de remédiation** | ✗ Ne peut pas prioriser | ✓ Doit prioriser |
| **Interprétation juridique** | ✗ Ne peut pas interpréter | ✓ Doit vérifier avec un conseil |
| **Conclusion d'audit** | ✗ Ne peut pas conclure | ✓ Responsabilité de l'auditeur |

!!! note "Rôles complémentaires"
    Le validateur et la revue humaine sont **complémentaires**, pas des alternatives. Le validateur assure la cohérence structurelle avant la revue humaine ; la revue humaine assure l'adéquation contextuelle.

## Attentes en matière de preuves

Les organisations implémentant la surveillance humaine doivent documenter :

| Type de preuve | Description |
| --- | --- |
| **Enregistrement de revue** | Qui a revu, quand et quelle décision a été prise |
| **Justification d'approbation** | Pourquoi la décision a été prise (surtout pour les exceptions) |
| **Enregistrement d'escalade** | Quand et pourquoi les problèmes ont été escaladés à une autorité supérieure |
| **Plan de remédiation** | Actions planifiées, responsables et délais pour traiter les problèmes |
| **Validation** | Attestation formelle que la revue a été complétée |

Ces enregistrements doivent être inclus dans le lot de preuves selon les [Exigences minimales de preuves](../../artifacts/minimum-evidence/).

## Non-déclaration excessive

!!! warning "Important"
    Ce protocole définit un **cadre pour documenter la surveillance humaine**. Il ne :

    - Fournit pas d'avis juridique ou d'interprétation réglementaire
    - Garantit pas la conformité à une réglementation ou norme
    - Remplace pas le jugement humain qualifié par des décisions automatisées
    - Prescrit pas de processus organisationnels spécifiques

    Les organisations doivent adapter ce cadre à leur contexte spécifique, profil de risque et exigences réglementaires.

## Pages connexes

- [Validateur](../../standard/current/07-validator/) — règles de validation automatisée et implémentation de référence
- [Périmètre de responsabilité](../responsibility-boundary/) — ce que fournit AIMO vs responsabilités des adopteurs
- [Exigences minimales de preuves](../../artifacts/minimum-evidence/) — liste de contrôle OBLIGATOIRE des preuves
- [Package de confiance](../trust-package/) — centre des matériaux prêts pour les auditeurs
