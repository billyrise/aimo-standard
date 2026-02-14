---
description: Package de confiance AIMO - Lot de matériaux prêts pour les auditeurs. Documentation minimale pour les auditeurs, le juridique et la sécurité IT afin d'évaluer la préparation à l'adoption de la gouvernance IA.
---

# Package de confiance (Package d'assurance)

Cette page regroupe les matériaux minimaux dont les auditeurs, le juridique et la sécurité IT ont besoin pour évaluer la préparation à l'adoption.
C'est uniquement un centre ; les tableaux détaillés de TDM de preuves et de couverture sont maintenus dans leurs sections respectives.

## Téléchargement

**[Télécharger le PDF du Package de confiance (dernière version)](https://github.com/billyrise/aimo-standard/releases/latest)**

Le PDF du package de confiance consolide les matériaux prêts pour les auditeurs dans un seul document. Chaque version GitHub inclut :

- `trust_package.pdf` — Package de confiance anglais
- `trust_package.ja.pdf` — Package de confiance japonais
- `aimo-standard-artifacts.zip` — Schémas, modèles, exemples, règles du validateur
- `SHA256SUMS.txt` — Checksums pour vérification

## Ce que vous obtenez

- **Conformité** : comment déclarer la conformité et ce que signifient les niveaux — [Conformité](../conformance/index.md)
- **Carte de couverture** : correspondance avec les standards externes — [Index carte de couverture](../coverage-map/index.md), [Méthodologie carte de couverture](../coverage-map/methodology.md)
- **Standard** : exigences et définitions normatives — [Standard (Actuel)](../standard/current/index.md)
- **Taxonomie** : système de classification à 8 dimensions pour la gouvernance IA — [Taxonomie](../standard/current/03-taxonomy.md), [Codes](../standard/current/04-codes.md), [Dictionnaire](../standard/current/05-dictionary.md)
- **Lot de preuves** : structure, TDM, traçabilité — [Lot de preuves](../artifacts/evidence-bundle.md)
- **Exigences minimales de preuves** : liste de contrôle OBLIGATOIRE par cycle de vie — [Exigences minimales de preuves](../artifacts/minimum-evidence.md)
- **Validateur** : règles et vérifications de référence — [Validateur](../validator/index.md)
- **Exemples** : lots d'échantillons prêts pour l'audit — [Exemples](../examples/index.md)
- **Versions** : historique des changements et distribution — [Versions](../../releases/)
- **Gouvernance** : politiques, sécurité, licences — [Gouvernance](../governance/index.md)

## Ensemble minimum pour la préparation à l'audit

| Élément | Où le trouver | Résultat / ce que cela prouve |
| --- | --- | --- |
| Niveaux de conformité | [Conformité](../conformance/index.md) | Comment déclarer la conformité et le périmètre des preuves requises |
| Correspondance de couverture | [Index carte de couverture](../coverage-map/index.md), [Méthodologie carte de couverture](../coverage-map/methodology.md) | Explicabilité par rapport aux réglementations et standards externes |
| Taxonomie et dictionnaire | [Taxonomie](../standard/current/03-taxonomy.md), [Codes](../standard/current/04-codes.md), [Dictionnaire](../standard/current/05-dictionary.md) | Système de classification pour les systèmes IA (8 dimensions, 91 codes) |
| Artefacts de preuves | [Lot de preuves](../artifacts/evidence-bundle.md), [Preuves minimales](../artifacts/minimum-evidence.md), [Modèle EV](../standard/current/06-ev-template.md) | Quelles données doivent exister pour soutenir la traçabilité |
| Vérifications du validateur | [Validateur](../validator/index.md) | Comment vérifier la cohérence et la complétude internes |
| Lot d'exemple | [Exemples](../examples/index.md) | À quoi ressemble un package prêt pour l'audit en pratique |
| Contrôle des changements | [Versions](../../releases/), [Gouvernance](../governance/index.md) | Comment les mises à jour sont gérées et communiquées |
| Sécurité / Licence / Marques | [Gouvernance](../governance/index.md) | Posture juridique et de sécurité pour les décisions d'adoption |

## Comment citer

Utilisez le README du dépôt pour les conseils de citation et le contexte ; la gouvernance renvoie aux politiques faisant autorité.
Voir [README.md](https://github.com/billyrise/aimo-standard/blob/main/README.md) et [Gouvernance](../governance/index.md).

## Contenu du zip d'artefacts

Le `aimo-standard-artifacts.zip` inclut :

- **Taxonomie (SSOT)** : `source_pack/03_taxonomy/` — CSV du dictionnaire (91 codes), YAML, système de codes
- **Schémas JSON** : `schemas/jsonschema/` — Schémas de validation lisibles par machine
- **Modèles** : `templates/ev/` — Modèles d'enregistrement de preuves (JSON + Markdown)
- **Exemples** : `examples/` — Lots d'échantillons minimaux pour adoption rapide
- **Carte de couverture** : `coverage_map/coverage_map.yaml` — Correspondance avec les standards externes
- **Règles du validateur** : `validator/rules/` — Définitions des règles de validation
- **Docs de gouvernance** : `VERSIONING.md`, `GOVERNANCE.md`, `SECURITY.md`, `LICENSE.txt`, etc.

## Périmètre de responsabilité

Le standard AIMO fournit un format de preuves structuré et un cadre d'explicabilité. Il ne fournit **pas** d'avis juridique, de certification de conformité, d'évaluation des risques ou d'exécution d'audit.

Pour la définition complète du périmètre, les hypothèses et les responsabilités des adopteurs, voir [Périmètre de responsabilité](responsibility-boundary.md).

## Comment préparer un package de soumission

Suivez ces étapes pour préparer une soumission prête pour l'audit :

1. **Générer le lot de preuves** : Créez les enregistrements EV, dictionnaire, résumé et journal des modifications selon [Lot de preuves](../artifacts/evidence-bundle.md) et [Exigences minimales de preuves](../artifacts/minimum-evidence.md).
2. **Exécuter le validateur** : Exécutez `python validator/src/validate.py bundle/root.json` pour vérifier la cohérence structurelle. Corrigez les erreurs avant de continuer.
3. **Créer les checksums** : Générez les checksums SHA-256 pour tous les fichiers de soumission :

    === "Linux"

        ```bash
        sha256sum *.json *.pdf > SHA256SUMS.txt
        ```

    === "macOS"

        ```bash
        shasum -a 256 *.json *.pdf > SHA256SUMS.txt
        ```

    === "Windows (PowerShell)"

        ```powershell
        Get-ChildItem *.json, *.pdf | ForEach-Object {
            $hash = (Get-FileHash $_.FullName -Algorithm SHA256).Hash.ToLower()
            "$hash  $($_.Name)"
        } | Out-File SHA256SUMS.txt -Encoding UTF8
        ```
4. **Packager les artefacts** : Créez une archive zip de votre lot de preuves :
   ```bash
   zip -r evidence_bundle.zip bundle_directory/
   ```
5. **Référencer la version** : Notez quelle version du standard AIMO (ex. `v1.0.0`) votre lot est aligné.
6. **Livrer** : Fournissez le zip, les checksums et la référence de version à votre auditeur ou fonction de conformité.

Pour les actifs de version et la vérification, voir [Versions](../../releases/).

## Déclaration de non-déclaration excessive

!!! warning "Important"
    Le standard AIMO soutient **l'explicabilité et la préparation des preuves**. Il ne fournit **pas** d'avis juridique, ne garantit pas la conformité et ne certifie pas la conformité à une réglementation ou cadre. Les adopteurs doivent vérifier les déclarations par rapport aux textes faisant autorité et obtenir des conseils professionnels si nécessaire.

Voir [Périmètre de responsabilité](responsibility-boundary.md) pour les détails sur le périmètre, les hypothèses et les responsabilités des adopteurs.

## Pour les auditeurs : procédure de vérification

Lors de la réception d'une soumission de preuves, les auditeurs doivent vérifier l'intégrité et la structure en utilisant les étapes suivantes :

!!! success "Provenance de build disponible"
    Tous les actifs de version incluent des attestations de provenance de build signées cryptographiquement. Voir [Procédure de vérification](../standard/versions/index.md#4-verify-build-provenance-attestation) pour les étapes de vérification d'attestation.

### Étape 1 : Vérifier les checksums (SHA-256)

=== "Linux"

    ```bash
    # Télécharger ou recevoir SHA256SUMS.txt avec la soumission
    # Vérifier que tous les fichiers correspondent à leurs checksums enregistrés
    sha256sum -c SHA256SUMS.txt

    # Ou vérifier manuellement les fichiers individuels :
    sha256sum evidence_bundle.zip
    # Comparer la sortie avec la valeur dans SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # Vérifier que tous les fichiers correspondent à leurs checksums enregistrés
    shasum -a 256 -c SHA256SUMS.txt

    # Ou vérifier manuellement les fichiers individuels :
    shasum -a 256 evidence_bundle.zip
    # Comparer la sortie avec la valeur dans SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Vérifier les fichiers individuels
    Get-FileHash .\evidence_bundle.zip -Algorithm SHA256

    # Comparer la sortie Hash avec SHA256SUMS.txt
    Get-Content .\SHA256SUMS.txt
    ```

Si un checksum échoue, la soumission doit être rejetée ou redemandée.

### Étape 2 : Vérifier la structure du lot (validateur)

**Prérequis** (configuration unique) :

```bash
# Cloner la version officielle du standard AIMO
git clone https://github.com/billyrise/aimo-standard.git
cd aimo-standard

# IMPORTANT : Utiliser la version exacte indiquée dans la soumission
# Remplacer VERSION par la version déclarée par le soumettant (ex. v0.0.1)
VERSION=v0.0.1  # ← Correspondre à la version dans la soumission
git checkout "$VERSION"

# Configurer l'environnement Python
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

!!! warning "Correspondance de version"
    Utilisez toujours la version exacte du standard AIMO indiquée dans la soumission. Utiliser une version différente peut causer des incompatibilités de validation dues aux changements de schéma ou de règles entre versions.

**Exécuter la validation** :

```bash
# Extraire le lot soumis
unzip evidence_bundle.zip -d bundle/

# Exécuter le validateur sur le root.json du lot
python validator/src/validate.py bundle/root.json

# Sortie attendue : "validation OK" ou liste d'erreurs
```

**Exemple** (utilisant l'échantillon intégré) :

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

Le validateur vérifie :

- Les fichiers requis existent (enregistrements EV, dictionnaire)
- Les fichiers JSON sont conformes au schéma
- Les références croisées (request_id, review_id, etc.) sont valides
- Les horodatages sont présents et correctement formatés

### Étape 3 : Vérifier l'alignement de version

Vérifiez que la soumission référence une version officielle du standard AIMO :

1. Confirmez que la version indiquée (ex. `v0.0.1`) existe sur [GitHub Releases](https://github.com/billyrise/aimo-standard/releases)
2. Comparez les schémas soumis avec les artefacts de la version
3. Notez toute déviation par rapport à la version officielle

### Ce qu'il faut rechercher

| Vérification | Critères de réussite | Action en cas d'échec |
| --- | --- | --- |
| Les checksums correspondent | Toutes les vérifications `sha256sum -c` passent | Rejeter ou redemander |
| Le validateur passe | Pas d'erreurs de `validate.py` | Demander des corrections avant acceptation |
| La version existe | Le tag de version existe sur GitHub | Clarifier l'alignement de version |
| Champs requis présents | Les enregistrements EV ont id, timestamp, source, summary | Demander la complétion |
| Traçabilité intacte | Les références croisées se résolvent correctement | Demander des corrections de liaison |

!!! info "Indépendance de l'auditeur"
    Les auditeurs doivent obtenir le validateur et les schémas directement de la version officielle du standard AIMO, pas de la partie soumettante, pour assurer l'indépendance de la vérification.

## Parcours d'audit

Depuis cette page, le parcours d'audit recommandé est :

1. **Système de classification** : [Taxonomie](../standard/current/03-taxonomy.md) + [Dictionnaire](../standard/current/05-dictionary.md) — comprendre le système de codes à 8 dimensions
2. **Structure des preuves** : [Lot de preuves](../artifacts/evidence-bundle.md) — comprendre la TDM du lot et la traçabilité
3. **Preuves requises** : [Exigences minimales de preuves](../artifacts/minimum-evidence.md) — liste de contrôle OBLIGATOIRE par cycle de vie
4. **Alignement des cadres** : [Carte de couverture](../coverage-map/index.md) + [Méthodologie](../coverage-map/methodology.md) — voir comment AIMO correspond aux cadres externes
5. **Validation** : [Validateur](../validator/index.md) — exécuter les vérifications de cohérence structurelle
6. **Téléchargement** : [Versions](../../releases/) — obtenir les actifs de version et vérifier les checksums
