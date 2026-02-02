---
description: Taxonomie AIMO - Système de classification à 8 dimensions avec 91 codes pour catégoriser les systèmes IA. Couvre le périmètre fonctionnel, les cas d'usage, types de données, canaux, intégration, risques, résultats et preuves.
---

# Taxonomie

La taxonomie AIMO fournit un système de classification structuré pour catégoriser les systèmes IA, leurs utilisations et les exigences de gouvernance associées. Elle se compose de **8 dimensions** avec **91 codes** qui permettent une classification et une gestion des preuves cohérentes entre les organisations.

## Objectif

La taxonomie sert trois objectifs principaux du point de vue de l'audit :

1. **Explicabilité** : Fournit un vocabulaire commun pour décrire les cas d'usage de l'IA dans l'organisation, soutenant une communication claire avec les auditeurs et les parties prenantes.

2. **Préparation des preuves** : Permet une documentation systématique des systèmes IA utilisant une classification standardisée, rendant la collecte et la revue des preuves plus efficaces.

3. **Comparabilité** : Permet aux organisations de comparer les cas d'usage de l'IA dans différents contextes en utilisant une terminologie cohérente.

## Ce que ce n'est pas (non-déclaration excessive)

!!! warning "Important"
    Le standard AIMO soutient **l'explicabilité et la préparation des preuves**. Il ne fournit **pas** d'avis juridique, ne garantit pas la conformité et ne certifie pas la conformité à une réglementation ou cadre. Voir [Périmètre de responsabilité](../../governance/responsibility-boundary.md) pour les détails.

La taxonomie est uniquement un système de classification. Elle ne :

- Garantit pas la conformité à une loi ou réglementation
- Remplace pas les conseils professionnels juridiques, de sécurité ou de conformité
- Certifie pas la conformité aux cadres externes (ISO, NIST, EU AI Act, etc.)
- Fournit pas d'évaluations des risques ou de recommandations de contrôles

## Exemples de risques spécifiques à l'IA/agentique (pourquoi un standard spécifique à l'IA est nécessaire)

Les contrôles de sécurité traditionnels (ex. ISMS) seuls échouent souvent à capturer les modes de défaillance spécifiques aux LLM/agents et les déviations d'agents autonomes (ex. exécution d'outil non intentionnelle, boucles récursives) d'une manière **explicable pour l'audit**.
La taxonomie AIMO fournit un langage partagé pour classifier ces risques spécifiques à l'IA et les connecter aux exigences de preuves et flux de travail de remédiation.

(Exemples de référence pour la différenciation. Les codes ci-dessous sont des espaces réservés illustratifs ; le système de codes officiel suit les définitions du Standard.)
- AG-01 Boucle/récursion incontrôlée
- AG-02 Utilisation d'outil non autorisée (mauvais usage de type confused deputy)
- AG-03 Dérive des limites de privilèges

## Vue d'ensemble des dimensions

AIMO utilise 8 dimensions pour classifier les cas d'usage de l'IA. Chaque dimension a un préfixe unique de 2 lettres.

| ID | Nom | Nombre de codes | Description |
| --- | --- | --- | --- |
| **FS** | Périmètre fonctionnel | 6 | Quelle fonction métier est supportée |
| **UC** | Classe de cas d'usage | 30 | Quel type de tâche est effectuée |
| **DT** | Type de données | 10 | Quelles classifications de données sont impliquées |
| **CH** | Canal | 8 | Comment les utilisateurs accèdent à l'IA |
| **IM** | Mode d'intégration | 7 | Comment l'IA se connecte aux systèmes entreprise |
| **RS** | Surface de risque | 8 | Quels risques sont associés |
| **OB** | Résultat / Bénéfice | 7 | Quels bénéfices sont attendus |
| **EV** | Type de preuve | 15 | Quelles preuves sont requises |

**Total : 91 codes sur 8 dimensions**

### Règles d'utilisation

| Dimension | Sélection | Implication d'audit |
| --- | --- | --- |
| FS, IM | Exactement 1 | Classification primaire pour l'attribution des responsabilités |
| UC, DT, CH, RS, EV | 1 ou plus | Énumération complète requise pour la couverture des risques |
| OB | 0 ou plus | Optionnel ; documente la valeur métier attendue |

## Définitions des dimensions

### FS : Périmètre fonctionnel

Catégorise l'utilisation de l'IA par la fonction métier qu'elle supporte. **Sélectionnez exactement une.**

| Code | Libellé | Définition |
| --- | --- | --- |
| FS-001 | Productivité utilisateur final | IA utilisée pour améliorer la productivité des utilisateurs finaux internes (écriture, recherche, résumé, notes de réunion). |
| FS-002 | Fonctionnalités orientées client | IA intégrée dans les fonctionnalités produit/service fournies aux clients. |
| FS-003 | Outillage développeur | IA utilisée pour assister le développement logiciel et les tâches d'ingénierie. |
| FS-004 | Opérations IT | IA utilisée pour les opérations IT et l'administration système (surveillance, gestion d'incidents). |
| FS-005 | Opérations de sécurité | IA utilisée pour la surveillance/réponse de sécurité (SOC, détection, triage). |
| FS-006 | Gouvernance et conformité | IA utilisée pour soutenir les activités de gouvernance/conformité (politique, preuves d'audit). |

### UC : Classe de cas d'usage

Catégorise l'utilisation de l'IA par le type de tâche ou d'interaction. **Sélectionnez une ou plusieurs.** La liste complète inclut 30 codes ; exemples représentatifs ci-dessous.

| Code | Libellé | Définition |
| --- | --- | --- |
| UC-001 | Q&R général | Questions-réponses générales et utilisation conversationnelle. |
| UC-002 | Résumé | Résumer des documents, réunions ou messages. |
| UC-003 | Traduction | Traduction entre langues. |
| UC-004 | Rédaction de contenu | Générer des brouillons d'emails, documents ou rapports. |
| UC-005 | Génération de code | Générer du code ou des scripts. |
| UC-006 | Revue de code | Revoir le code pour les problèmes et améliorations. |
| UC-009 | Recherche/RAG | Récupération et questions-réponses basées sur RAG. |
| UC-010 | Automatisation agentique | Agents autonomes ou semi-autonomes exécutant des actions. |

Voir [Dictionnaire](./05-dictionary.md) pour la liste complète des 30 codes UC.

### DT : Type de données

Catégorise la sensibilité et la classification des données impliquées. **Sélectionnez une ou plusieurs.**

| Code | Libellé | Définition |
| --- | --- | --- |
| DT-001 | Public | Données publiquement disponibles et destinées à la divulgation publique. |
| DT-002 | Interne | Données métier internes non publiques. |
| DT-003 | Confidentiel | Données internes hautement sensibles nécessitant un accès restreint. |
| DT-004 | Données personnelles | Données personnelles telles que définies par les lois de confidentialité applicables. |
| DT-005 | Données personnelles sensibles | Catégorie spéciale/données personnelles sensibles. |
| DT-006 | Identifiants | Secrets d'authentification et identifiants. |
| DT-007 | Code source | Code source et artefacts associés. |
| DT-008 | Données client | Données fournies par ou liées au client. |
| DT-009 | Journaux opérationnels | Journaux opérationnels ou système utilisés pour la surveillance et le dépannage. |
| DT-010 | Télémétrie de sécurité | Télémétrie de sécurité comme les alertes et détections. |

### CH : Canal

Catégorise comment les utilisateurs accèdent ou interagissent avec l'IA. **Sélectionnez une ou plusieurs.**

| Code | Libellé | Définition |
| --- | --- | --- |
| CH-001 | Interface web | Utilisation via une interface utilisateur web. |
| CH-002 | API | Utilisation via intégration API programmatique. |
| CH-003 | Plugin IDE | Utilisation via plugin IDE/éditeur. |
| CH-004 | ChatOps | Utilisation via intégrations de plateformes de chat (Slack/Teams). |
| CH-005 | Application bureau | Utilisation via application bureau native. |
| CH-006 | Application mobile | Utilisation via application mobile native. |
| CH-007 | Email | Utilisation via interface email ou automatisation basée sur email. |
| CH-008 | Ligne de commande | Utilisation via interface en ligne de commande. |

### IM : Mode d'intégration

Catégorise comment l'IA est intégrée dans les systèmes entreprise. **Sélectionnez exactement une.**

| Code | Libellé | Définition |
| --- | --- | --- |
| IM-001 | Autonome | Utilisé de manière autonome sans intégration dans les systèmes entreprise. |
| IM-002 | SaaS intégré | Application SaaS intégrant des fonctionnalités IA. |
| IM-003 | Intégré app entreprise | IA intégrée dans les applications entreprise internes. |
| IM-004 | RPA/Workflow | IA invoquée dans l'automatisation de workflow ou RPA. |
| IM-005 | On-prem / Privé | IA hébergée dans un environnement privé/on-prem. |
| IM-006 | Service géré | Utilisation via service géré avec contrôles entreprise. |
| IM-007 | Shadow / Non géré | Utilisation en dehors des contrôles de gouvernance approuvés. |

### RS : Surface de risque

Catégorise les types de risques associés à l'utilisation de l'IA. **Sélectionnez une ou plusieurs.**

| Code | Libellé | Définition |
| --- | --- | --- |
| RS-001 | Fuite de données | Risque de divulgation non intentionnelle de données. |
| RS-002 | Abus de sécurité | Risque que le système soit abusé à des fins malveillantes. |
| RS-003 | Violation de conformité | Risque de violation des lois/réglementations/politiques. |
| RS-004 | Violation de PI | Risque de violation de droits d'auteur/brevets/secrets commerciaux. |
| RS-005 | Mauvaise utilisation de modèle | Risque d'utilisation inappropriée du modèle ou de dépendance excessive. |
| RS-006 | Biais/équité | Risque de résultats injustes ou biaisés. |
| RS-007 | Sécurité | Risque de contenu nuisible ou de recommandations dangereuses. |
| RS-008 | Risque tiers | Risques des fournisseurs, sous-traitants et fournisseurs de modèles. |

### OB : Résultat / Bénéfice

Catégorise les résultats ou bénéfices attendus de l'utilisation de l'IA. **Optionnel ; sélectionnez zéro ou plus.**

| Code | Libellé | Définition |
| --- | --- | --- |
| OB-001 | Efficacité | Améliore l'efficacité temps/coût. |
| OB-002 | Qualité | Améliore la qualité/précision des sorties. |
| OB-003 | Revenus | Contribue à la croissance des revenus. |
| OB-004 | Réduction des risques | Réduit les risques opérationnels/sécurité/conformité. |
| OB-005 | Innovation | Permet de nouvelles capacités ou innovations. |
| OB-006 | Satisfaction client | Améliore la satisfaction client. |
| OB-007 | Expérience employé | Améliore l'expérience employé. |

### EV : Type de preuve

Catégorise les types de preuves requises ou collectées. **Sélectionnez une ou plusieurs.**

| Code | Libellé | Définition |
| --- | --- | --- |
| EV-001 | Enregistrement de demande | Preuve qu'une utilisation/service IA a été demandé(e) et décrit(e). |
| EV-002 | Enregistrement de revue/approbation | Preuve qu'une revue/approbation a été effectuée. |
| EV-003 | Enregistrement d'exception | Preuve qu'une exception a été accordée et suivie. |
| EV-004 | Enregistrement de renouvellement/réévaluation | Preuve qu'un renouvellement ou une réévaluation a eu lieu. |
| EV-005 | Entrée de journal des modifications | Preuve des modifications et de leurs approbations. |
| EV-006 | Preuve d'intégrité | Preuve d'intégrité (hash, signature, WORM). |
| EV-007 | Journal des accès | Preuve de contrôle d'accès et d'historique des accès. |
| EV-008 | Inventaire de modèles/services | Enregistrement d'inventaire des modèles/services utilisés. |
| EV-009 | Évaluation des risques | Évaluation des risques documentée pour l'utilisation/service. |
| EV-010 | Correspondance de contrôles | Preuve de correspondance des contrôles avec les cadres externes. |
| EV-011 | Formation/orientation | Preuve de formation ou d'orientation fournie aux utilisateurs. |
| EV-012 | Preuve de surveillance | Preuve de surveillance et de supervision continue. |
| EV-013 | Enregistrement d'incident | Preuve de gestion d'incident liée à l'utilisation de l'IA. |
| EV-014 | Évaluation tierce | Preuve d'évaluation fournisseur ou tierce. |
| EV-015 | Attestation/validation | Enregistrement d'attestation formelle ou de validation. |

## Comment utiliser

### Relation avec les preuves

Chaque document de preuve (EV) référence des codes de plusieurs dimensions pour classifier le système IA ou le cas d'usage documenté. La classification à 8 dimensions permet :

- **Catégorisation cohérente** dans l'organisation
- **Filtrage basé sur le risque** par valeurs de dimension
- **Correspondance de cadres** via la carte de couverture

### Référence au dictionnaire

Pour les définitions complètes des codes incluant les notes de portée et exemples, référez-vous au [Dictionnaire](./05-dictionary.md).

### Exemple de classification

```
FS: FS-001 (Productivité utilisateur final)
UC: UC-001 (Q&R général), UC-002 (Résumé)
DT: DT-002 (Interne), DT-004 (Données personnelles)
CH: CH-001 (Interface web)
IM: IM-002 (SaaS intégré)
RS: RS-001 (Fuite de données), RS-003 (Violation de conformité)
OB: OB-001 (Efficacité)
EV: EV-001 (Enregistrement de demande), EV-002 (Enregistrement de revue/approbation)
```

## Référence SSOT

!!! info "Source de vérité"
    La définition faisant autorité est `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv`. Cette page est explicative. Voir [Guide de localisation](../../contributing/localization.md) pour les flux de travail de mise à jour.

## Pages connexes

- [Codes](./04-codes.md) - Format de code, conventions de nommage et cycle de vie
- [Dictionnaire](./05-dictionary.md) - Listes complètes de codes et définitions de colonnes
- [Modèles de preuves](./06-ev-template.md) - Comment utiliser les codes dans les preuves
- [Périmètre de responsabilité](../../governance/responsibility-boundary.md) - Déclaration de non-déclaration excessive
