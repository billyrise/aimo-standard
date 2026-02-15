---
description: Périmètre de responsabilité AIMO — Définit ce que la norme fournit vs. responsabilités des adoptants. Déclaration de non-surévaluation et limites de périmètre.
---
<!-- aimo:translation_status=translated -->

# Périmètre de responsabilité（Responsibility Boundary）

Cette page définit ce que le AIMO Standard fournit et ne fournit pas, les hypothèses qu’il fait et les responsabilités des adoptants.

## Ce que le AIMO Standard fournit

- **Un format de preuve structuré** : schémas, modèles et taxonomie pour les preuves de gouvernance IA.
- **Cadre de traçabilité** : liaison des preuves par cycle de vie (demande → revue → exception → renouvellement).
- **Soutien à l’explicabilité** : mapping de couverture vers des cadres externes pour les discussions d’audit.
- **Outils de validation** : validateur de référence et règles pour les contrôles de cohérence structurelle.
- **Documentation** : spécification normative, exemples et guide.

## Ce que le AIMO Standard ne fournit pas

| Hors périmètre | Explication |
| --- | --- |
| **Conseil juridique** | AIMO n’interprète pas les lois ni les réglementations. Consultez un conseil juridique qualifié pour la conformité réglementaire. |
| **Certification de conformité** | Utiliser AIMO ne certifie pas la conformité à une réglementation ou un cadre (ISO 42001, EU AI Act, NIST AI RMF, etc.). |
| **« Certifié ISO par AIMO »** | AIMO ne délivre pas de certifications. La certification est effectuée par des organismes de certification accrédités. |
| **« Conforme EU AI Act grâce à AIMO »** | AIMO structure les preuves ; il ne garantit ni ne certifie la conformité réglementaire. |
| **Évaluation des risques** | AIMO structure les preuves mais ne réalise ni ne valide d’évaluations de risque IA. |
| **Contrôles techniques** | AIMO n’implémente pas le contrôle d’accès, le chiffrement ou d’autres contrôles de sécurité ; il documente les attentes. |
| **Exécution d’audit** | AIMO fournit des supports aux auditeurs mais ne réalise pas d’audits. |
| **Évaluation de modèles IA** | AIMO n’évalue pas les performances, biais ou sécurité des modèles. |

## Hypothèses

Le AIMO Standard suppose :

1. **Les adoptants ont des processus de gouvernance** : flux de demande, revue, approbation et exception existants.
2. **Les adoptants maintiennent les preuves** : les preuves sont créées, stockées et conservées par les systèmes de l’adoptant.
3. **Les adoptants vérifient auprès des textes de référence** : lors de l’utilisation de la Coverage Map, les adoptants vérifient le cadre ou la réglementation d’origine.
4. **Les outils sont optionnels** : le validateur de référence est un confort ; les adoptants peuvent utiliser leur propre validation.

## Responsabilités des adoptants

| Responsabilité | Description |
| --- | --- |
| **Création de preuves** | Générer des enregistrements de preuve précis et à jour conformes au schéma EV. |
| **Stockage et conservation des preuves** | Stocker les preuves de manière sécurisée avec contrôles d’accès et durées de conservation appropriés. |
| **Intégrité et contrôle d’accès** | Mettre en œuvre des contrôles (hachage, WORM, journaux d’audit) pour préserver l’intégrité des preuves. |
| **Vérification juridique** | Vérifier les affirmations de conformité auprès des textes juridiques de référence et obtenir un conseil juridique si besoin. |
| **Alignement continu** | Mettre à jour les preuves et les mappings au fil de l’évolution des versions du AIMO Standard et des cadres externes. |
| **Préparation à l’audit** | Empaqueter les Evidence Bundles et exécuter la validation avant remise aux auditeurs. |

## Matrice RACI

La matrice RACI suivante précise les responsabilités entre AIMO Standard, Adoptant et Auditeur.

| Activité | AIMO Standard | Adoptant | Auditeur |
| --- | :---: | :---: | :---: |
| **Définir schéma et modèles de preuve** | R/A | I | I |
| **Créer des enregistrements de preuve** | — | R/A | I |
| **Stocker et conserver les preuves** | — | R/A | I |
| **Mettre en œuvre les contrôles d’accès** | — | R/A | I |
| **Mettre en œuvre les contrôles d’intégrité (hash, WORM)** | — | R/A | I |
| **Exécuter le validateur sur le bundle** | C | R/A | C |
| **Empaqueter la remise (zip, checksums)** | C | R/A | I |
| **Vérifier les checksums (sha256)** | — | C | R/A |
| **Vérifier la structure du bundle (validateur)** | — | C | R/A |
| **Interpréter les exigences réglementaires** | — | R/A | C |
| **Émettre la conclusion d’audit** | — | — | R/A |
| **Fournir un conseil juridique** | — | — | — |

**Légende** : R = Responsable, A = Accountable, C = Consulté, I = Informé, — = Non applicable

!!! note "À retenir"
    Le AIMO Standard est responsable de **définir le format**. Les adoptants sont responsables de **créer, stocker et valider les preuves**. Les auditeurs sont responsables de **vérifier les remises et d’émettre les conclusions d’audit**.

!!! warning "Avis de non-certification"
    Le AIMO Standard est informatif ; il ne certifie pas la conformité ni ne fournit de conseil juridique. Les conclusions d’audit et les évaluations de conformité relèvent de la seule responsabilité des auditeurs et professionnels juridiques qualifiés.

## Politique d’affirmations

| Acceptable | Inacceptable |
| --- | --- |
| « Un Evidence Bundle a été produit selon le AIMO Standard v0.1.2 et validé structurellement par le AIMO Validator. » | « Conforme EU AI Act », « certifié ISO 42001 », « approuvé par le gouvernement », etc. |
| « Nous utilisons les artefacts AIMO pour soutenir la préparation ISO/IEC 42001 ; les décisions de certification restent aux organismes de certification accrédités. » | Prétendre que AIMO certifie la conformité ou fournit un conseil juridique. |

## Déclaration de non-surévaluation

!!! warning "Important"
    Le AIMO Standard soutient **l’explicabilité et la préparation des preuves**. Il **ne** fournit **pas** de conseil juridique, **ne** garantit **pas** la conformité et **ne** certifie **pas** la conformité à une réglementation ou un cadre. Les adoptants doivent vérifier les affirmations auprès des textes de référence et obtenir un avis professionnel le cas échéant.

Cette déclaration s’applique à toute la documentation du AIMO Standard, y compris Trust Package, Evidence Bundle, Minimum Evidence Requirements, Coverage Map et Releases.

## Pages connexes

- [Trust Package](../trust-package/) — hub de supports prêts pour l’audit
- [Human Oversight Protocol](../human-oversight-protocol/) — frontière revue machine vs. humaine
- [Minimum Evidence Requirements](../../artifacts/minimum-evidence/) — checklist MUST par cycle de vie
- [Coverage Map Methodology](../../coverage-map/methodology/) — ce qu’est et n’est pas le mapping
