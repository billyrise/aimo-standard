---
description: Niveaux de conformité AIMO Standard. Comment les organisations déclarent la conformité, exigences de preuves et ce que chaque niveau signifie pour la gouvernance de l'IA.
---
<!-- aimo:translation_status=translated -->

# Conformité

!!! warning "Important : pas de certification, pas d'assurance, pas de déclaration de conformité juridique"
    AIMO Standard définit un **format d'empaquetage et de validation des preuves**. Il ne certifie pas la conformité aux lois ou normes.
    Les opinions d'audit et d'assurance restent la responsabilité des auditeurs indépendants et de l'organisation adoptante.
    **Déclaration appropriée :** « Un Paquet de preuves a été produit conformément à AIMO Standard v0.1.2 et validé structurellement par le Validateur AIMO. »
    <!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
    **Déclaration inappropriée :** « Conforme à la loi sur l'IA de l'UE », « ISO 42001 certifié », « approuvé par le gouvernement ».
    <!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

AIMO Standard se positionne comme **couche d'assurance / transmission aux auditeurs / preuves continues** : il fournit l'empaquetage des preuves, les validateurs et la traçabilité pour que les adoptants et les auditeurs travaillent avec des preuves structurées. AIMO **n'est pas** un certificateur ; les décisions de certification et de conformité relèvent des organismes de certification accrédités, des auditeurs et de l'organisation adoptante.

Ces niveaux sont des **niveaux internes de maturité des preuves** pour l'empaquetage et la traçabilité. Ce **ne sont pas** une certification, **ni** une opinion d'assurance, **ni** une conformité juridique ou réglementaire.

## Déclarations de compatibilité (ISO/NIST/Loi sur l'IA de l'UE)

Les **correspondances informatives** suivantes lient les preuves et artefacts AIMO aux cadres externes. Elles soutiennent l'explicabilité et la transmission aux auditeurs ; elles **ne confèrent pas** de certification ni ne garantissent la conformité. Vérifiez par rapport aux textes de référence de chaque cadre.

- [Coverage Map — ISO/IEC 42001](../coverage-map/iso-42001/) — correspondance avec ISO/IEC 42001 (système de management de l'IA)
- [Coverage Map — NIST AI RMF](../coverage-map/nist-ai-rmf/) — correspondance avec le NIST AI Risk Management Framework
- [Coverage Map — Loi sur l'IA de l'UE](../coverage-map/eu-ai-act/) — correspondance avec les thèmes de la loi sur l'IA (haut niveau ; pas un conseil juridique)

Les sources primaires et le libellé des déclarations sont documentés sur chaque page Coverage Map et dans [Périmètre de responsabilité](../governance/responsibility-boundary/).

## Non-déclarations (ce qu'AIMO ne déclare pas)

- AIMO **ne** certifie **pas** la conformité à ISO/IEC 42001, NIST AI RMF, loi sur l'IA de l'UE ou tout autre cadre.
- AIMO **ne** garantit **pas** la conformité réglementaire ou juridique.
- AIMO **ne** fournit **pas** d'opinions d'assurance ni de conseil juridique.
- AIMO **ne** décide **pas** si une organisation satisfait aux exigences externes ; cela relève des adoptants, des auditeurs et des organismes de certification.

AIMO **fournit** : un format de preuves structuré, un validateur, des correspondances de couverture (informatifs) et des documents pour la transmission aux auditeurs. Voir [Périmètre de responsabilité](../governance/responsibility-boundary/) pour le périmètre complet.

!!! note "Alias du nom de niveau"
    Le niveau supérieur a été appelé « Gold » de manière informelle par le passé ; le **nom officiel du niveau est Audit-Ready**.

## Cadre de conformité AIMO (AIMO-MS / AIMO-Controls / AIMO-Audit)

| Composant | Description | Attentes en preuves |
| --- | --- | --- |
| **AIMO-MS** | Structure orientée système de management : politiques, rôles, artefacts alignés PDCA pouvant soutenir des contrôles de type ISO/IEC 42001. | Request, review, exception, renewal, change log ; Summary et Dictionary. |
| **AIMO-Controls** | Contrôles du cycle de vie et d'intégrité : request→review→exception→renewal, hachage, signature (selon [structure du Paquet de preuves](../../standard/current/09-evidence-bundle-structure/)). | Object_index, payload_index, hash_chain, signing ; enregistrements du cycle de vie. |
| **AIMO-Audit** | Préparation au transfert d'audit : validateur réussi, checksums, attestation optionnelle et index de transfert d'audit. | Sortie du validateur, bundle_id, identité du producteur, métadonnées de signature optionnelles et index de transfert. |

Les attentes en preuves sont décrites dans [Exigences minimales de preuves](../artifacts/minimum-evidence/) et [Paquet de preuves](../artifacts/evidence-bundle/).

## Niveaux de conformité (AIMO uniquement)

### Niveau 1 — Foundation

**Objectif :** Base traçable. Ensemble minimum pour que le paquet soit identifiable, vérifiable en intégrité et contrôlé par le validateur.

| Élément | Exigence |
| --- | --- |
| **Artefacts requis** | Structure du [Paquet de preuves](../artifacts/evidence-bundle/) (manifest.json, objects/, payload_index selon spec.) ; [Validateur](../validator/) réussi ; lien vers [Exigences minimales de preuves](../artifacts/minimum-evidence/). |
| **Questions d'audit typiques** | Qu'est-ce qui est dans le périmètre ? Qui a produit le paquet ? Les hashes peuvent-ils être vérifiés ? |
| **Lacunes typiques** | Métadonnées du manifest manquantes (bundle_id, created_at, producer) ; validateur non exécuté ou non joint. |

### Niveau 2 — Operational

**Objectif :** Preuves de contrôle opérationnel. S'appuie sur Foundation avec piste du cycle de vie et surveillance.

| Élément | Exigence |
| --- | --- |
| **Artefacts requis** | Tous les MUST Foundation ; piste de contrôle du cycle de vie (request/approbation, review, exception ou « aucune exception », planning renewal) ; au moins un artefact de surveillance (journal d'incidents ou contrôle périodique ou échantillonnage de surveillance humaine) ; change log avec lien d'intégrité ; déclaration de limite preuve vs. assurance. |
| **Questions d'audit typiques** | Qui a approuvé l'utilisation ? Comment les exceptions sont-elles suivies ? Quand a eu lieu la dernière revue ? |
| **Lacunes typiques** | Review/approbation non liée à request ; pas d'artefact de surveillance ; change log ne référence pas les objets impactés. |

### Niveau 3 — Audit-Ready

**Objectif :** Qualité du transfert d'audit. Attestation complète, reproductibilité et emplacement pour formulaires externes.

| Élément | Exigence |
| --- | --- |
| **Artefacts requis** | Tous les MUST Operational ; au moins une signature numérique couvrant le manifest (identité du signataire + algorithme) ; TSA ou déclaration « pas de TSA » ; paquet de reproductibilité (commande exacte du validateur, sorties attendues, métadonnées d'environnement) ; section Formulaires externes avec modèles/listes officiels joints tels quels et référencés entre eux ; déclaration d'exhaustivité bornée ; index de transfert d'audit d'une page (artefact → hash → producteur → date). |
| **Questions d'audit typiques** | Comment un auditeur peut-il réexécuter la validation ? Où sont les listes externes et comment sont-elles mappées au paquet ? |
| **Lacunes typiques** | Signature présente mais signataire/algorithme non documentés ; pas d'index de transfert ; formulaires externes non hashés ou non référencés dans le manifest. |

## Preuves minimales par niveau (résumé)

| Niveau | MUST (résumé) |
| --- | --- |
| **Foundation** | Structure du paquet (manifest, object_index, payload_index) ; sha256 pour les objets référencés ; bundle_id, created_at, producer ; exécution du validateur + version ; base du dictionnaire de preuves (nom du système, propriétaire, objectif, catégories de données, étape du cycle de vie) ; déclaration d'accès et de rétention (qui, durée, type de stockage, preuve d'altération). SHOULD : entrée minimale dans le change log. |
| **Operational** | Tous les MUST Foundation ; piste du cycle de vie (request/approbation, review, exception ou « aucune », renewal + dernière renewal) ; ≥1 artefact de surveillance ; entrées du change log référencent les objets impactés ; déclaration explicite de limite preuve vs. assurance. |
| **Audit-Ready** | Tous les MUST Operational ; ≥1 signature sur le manifest (identité du signataire + algorithme) ; TSA ou « pas de TSA » ; paquet de reproductibilité ; Formulaires externes listés et référencés entre eux ; déclaration d'exhaustivité bornée ; index de transfert d'audit. |

La **présence** d'au moins une signature (ciblant le manifest) est requise par la [structure du Paquet de preuves](../../standard/current/09-evidence-bundle-structure/) normative pour tous les paquets. **Audit-Ready** ajoute une **attestation cryptographique** plus stricte (identité du signataire, algorithme, déclaration TSA, instructions de revalidation) pour qu'un tiers puisse refaire les contrôles.

## Correspondance ISO/IEC 42001 (informatif)

Le tableau suivant montre comment les artefacts AIMO **soutiennent les preuves** pour les familles de clauses typiques d'ISO/IEC 42001. C'est informatif uniquement ; cela n'implique pas certification ni conformité.

| Famille de clauses ISO/IEC 42001 | Artefacts AIMO soutenant les preuves |
| --- | --- |
| Contexte de l'organisation | Summary, Dictionary, scope_ref |
| Leadership / Politique | Summary, review, dictionary |
| Planification (risques, objectifs) | request, review, exception, EV, Dictionary |
| Soutien (ressources, compétence, documentation) | Summary, review, EV, change_log |
| Exploitation | EV, request, review, exception ; contrôles opérationnels |
| Évaluation des performances (surveillance, audit interne, revue de direction) | EV, change_log, review, renewal |
| Amélioration | exception, renewal, change_log |

Voir [Coverage Map — ISO/IEC 42001](../coverage-map/iso-42001/) et [Boîte à outils de préparation à la certification ISO 42001](../artifacts/iso-42001-certification-readiness-toolkit/) pour plus de détails.

## Modèles de libellés de déclaration (anti-surdéclaration)

N'utiliser que des déclarations décrivant avec précision ce qui a été fait. La certification et la conformité juridique restent la responsabilité des adoptants et des organismes accrédités.

**Acceptables (exemples)**

- « Nous sommes conformes AIMO (Niveau 2) à AIMO Standard v0.1.2 ; cela n'implique pas certification ISO ni conformité juridique. »
- « Nous utilisons les artefacts AIMO pour soutenir la préparation à l'ISO/IEC 42001 ; les décisions de certification relèvent des organismes de certification accrédités. »
- « Un Paquet de preuves a été produit conformément à AIMO Standard v0.1.2 et validé structurellement par le Validateur AIMO. »

<!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
**Inacceptables (exemples)**

- « Conforme à la loi sur l'IA de l'UE » (AIMO ne certifie pas la conformité réglementaire.)
- « ISO 42001 certifié » (La certification est délivrée par les organismes de certification accrédités, pas AIMO.)
- « Approuvé par le gouvernement » (AIMO n'est pas un schéma d'approbation gouvernementale.)
<!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

## Pages connexes

- [Trust Package](../governance/trust-package/) — Point d'entrée consolidé pour les auditeurs
- [Responsibility Boundary](../governance/responsibility-boundary/) — Ce que AIMO fournit et ne fournit pas
- [Standard (Current)](../standard/current/) — Exigences normatives
- [Artifacts](../artifacts/) — Structure des preuves et exigences minimales
- [Validator](../validator/) — Validation structurelle
