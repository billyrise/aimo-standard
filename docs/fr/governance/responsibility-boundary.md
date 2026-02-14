---
description: Périmètre de responsabilité AIMO - Définit ce que le standard fournit vs les responsabilités des adopteurs. Déclaration de non-déclaration excessive et limitations du périmètre.
---

# Périmètre de responsabilité

Cette page définit ce que le standard AIMO fournit et ne fournit pas, les hypothèses qu'il fait et les responsabilités des adopteurs.

## Ce que le standard AIMO fournit

- **Un format de preuves structuré** : schémas, modèles et taxonomie pour les preuves de gouvernance IA.
- **Cadre de traçabilité** : liaison de preuves basée sur le cycle de vie (demande → revue → exception → renouvellement).
- **Support d'explicabilité** : correspondance de couverture avec les cadres externes pour les discussions d'audit.
- **Outillage de validation** : validateur de référence et règles pour les vérifications de cohérence structurelle.
- **Documentation** : spécification normative, exemples et conseils.

## Ce que le standard AIMO ne fournit PAS

| Hors périmètre | Explication |
| --- | --- |
| **Avis juridique** | AIMO n'interprète pas les lois ou réglementations. Consultez un conseil juridique qualifié pour la conformité réglementaire. |
| **Certification de conformité** | Utiliser AIMO ne certifie pas la conformité à une réglementation ou cadre (ISO 42001, EU AI Act, NIST AI RMF, etc.). |
| **Évaluation des risques** | AIMO structure les preuves mais n'effectue pas ou ne valide pas les évaluations de risques IA. |
| **Contrôles techniques** | AIMO n'implémente pas le contrôle d'accès, le chiffrement ou autres contrôles de sécurité ; il documente les attentes. |
| **Exécution d'audit** | AIMO fournit des matériaux pour les auditeurs mais ne conduit pas d'audits. |
| **Évaluation de modèle IA** | AIMO n'évalue pas la performance, les biais ou la sécurité des modèles. |

## Hypothèses

Le standard AIMO suppose :

1. **Les adopteurs ont des processus de gouvernance** : les flux de travail de demande, revue, approbation et exception existent.
2. **Les adopteurs maintiennent les preuves** : les preuves sont créées, stockées et conservées par les systèmes de l'adopteur.
3. **Les adopteurs vérifient par rapport aux textes faisant autorité** : lors de l'utilisation de la carte de couverture, les adopteurs vérifient le cadre ou la réglementation original.
4. **L'outillage est optionnel** : le validateur de référence est une commodité ; les adopteurs peuvent utiliser leur propre validation.

## Responsabilités des adopteurs

| Responsabilité | Description |
| --- | --- |
| **Création de preuves** | Générer des enregistrements de preuves précis et opportuns alignés avec le schéma EV. |
| **Stockage et rétention des preuves** | Stocker les preuves de manière sécurisée avec des contrôles d'accès et des périodes de rétention appropriés. |
| **Intégrité et contrôle d'accès** | Implémenter des contrôles (hachage, WORM, journaux d'audit) pour préserver l'intégrité des preuves. |
| **Vérification juridique** | Vérifier les déclarations de conformité par rapport aux textes juridiques faisant autorité et obtenir un avis juridique si nécessaire. |
| **Alignement continu** | Mettre à jour les preuves et correspondances au fur et à mesure que les versions du standard AIMO et les cadres externes évoluent. |
| **Préparation d'audit** | Packager les lots de preuves et exécuter la validation avant soumission aux auditeurs. |

## Matrice RACI

La matrice RACI suivante clarifie les responsabilités entre les rôles Standard AIMO, Adopteur et Auditeur.

| Activité | Standard AIMO | Adopteur | Auditeur |
| --- | :---: | :---: | :---: |
| **Définir le schéma et les modèles de preuves** | R/A | I | I |
| **Créer les enregistrements de preuves** | — | R/A | I |
| **Stocker et conserver les preuves** | — | R/A | I |
| **Implémenter les contrôles d'accès** | — | R/A | I |
| **Implémenter les contrôles d'intégrité (hash, WORM)** | — | R/A | I |
| **Exécuter le validateur sur le lot** | C | R/A | C |
| **Packager la soumission (zip, checksums)** | C | R/A | I |
| **Vérifier les checksums (sha256)** | — | C | R/A |
| **Vérifier la structure du lot (validateur)** | — | C | R/A |
| **Interpréter les exigences réglementaires** | — | R/A | C |
| **Émettre une conclusion d'audit** | — | — | R/A |
| **Fournir un avis juridique** | — | — | — |

**Légende** : R = Responsable, A = Accountable (redevable), C = Consulté, I = Informé, — = Non applicable

!!! note "Point clé"
    Le standard AIMO est responsable de **définir le format**. Les adopteurs sont responsables de **créer, stocker et valider les preuves**. Les auditeurs sont responsables de **vérifier les soumissions et émettre les conclusions d'audit**.

!!! warning "Avis de non-certification"
    Le standard AIMO est informatif ; il ne certifie pas la conformité et ne fournit pas d'avis juridique. Les conclusions d'audit et les évaluations de conformité sont la responsabilité exclusive des auditeurs qualifiés et des professionnels du droit.

## Déclaration de non-déclaration excessive

!!! warning "Important"
    Le standard AIMO soutient **l'explicabilité et la préparation des preuves**. Il ne fournit **pas** d'avis juridique, ne garantit pas la conformité et ne certifie pas la conformité à une réglementation ou cadre. Les adopteurs doivent vérifier les déclarations par rapport aux textes faisant autorité et obtenir des conseils professionnels si nécessaire.

Cette déclaration s'applique à toute la documentation du standard AIMO, y compris le package de confiance, le lot de preuves, les exigences minimales de preuves, la carte de couverture et les versions.

## Pages connexes

- [Package de confiance](../trust-package/) — centre des matériaux prêts pour les auditeurs
- [Protocole de surveillance humaine](../human-oversight-protocol/) — limite entre revue machine et humaine
- [Exigences minimales de preuves](../../artifacts/minimum-evidence/) — liste de contrôle OBLIGATOIRE du cycle de vie
- [Méthodologie de la carte de couverture](../../coverage-map/methodology/) — ce qu'est et n'est pas la correspondance
