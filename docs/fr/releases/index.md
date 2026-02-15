---
description: Versions du standard AIMO - Téléchargez les PDF versionnés, artefacts et checksums. Changelog, guides de migration et attestations de provenance de build.
---
<!-- aimo:translation_status=translated -->

# Versions

Cette section est un centre pour les versions versionnées, changelog, migration et artefacts de distribution.

## Télécharger la dernière version

**[GitHub Releases](https://github.com/billyrise/aimo-standard/releases/latest)** — c’est la source unique de vérité du release « latest ». Le chemin du site `/latest/` redirige vers la même version.

## Procédure de vérification (page permanente)

La **procédure de vérification** complète (téléchargement des actifs, vérification des checksums, attestation de provenance) est disponible en page permanente, pas seulement en PDF :

- **[Standard → Versions → Procédure de vérification](../standard/versions/)** — vérification pas à pas des checksums (Linux/macOS/Windows) et attestation de provenance.

Utilisez cette page lorsque vous devez vérifier les actifs de release ou documenter les étapes de vérification dans les livrables d’audit.

## Actifs de version

Chaque version officielle (tag `vX.Y.Z`) inclut :

| Actif | Description |
| --- | --- |
| `trust_package.pdf` | Package de confiance anglais — matériaux d'assurance prêts pour les auditeurs |
| `trust_package.ja.pdf` | Package de confiance japonais |
| `aimo-standard-artifacts.zip` | Schémas, modèles, exemples, règles du validateur |
| `SHA256SUMS.txt` | Checksums SHA-256 pour tous les actifs |

### Vérification des téléchargements

Après téléchargement, vérifiez l'intégrité des fichiers en utilisant les checksums :

=== "Linux"

    ```bash
    # Télécharger le fichier de checksums
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # Vérifier un fichier spécifique
    sha256sum -c SHA256SUMS.txt --ignore-missing

    # Ou vérifier manuellement :
    sha256sum trust_package.pdf
    # Comparer la sortie avec SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # Télécharger le fichier de checksums
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # Vérifier un fichier spécifique
    shasum -a 256 -c SHA256SUMS.txt

    # Ou vérifier manuellement :
    shasum -a 256 trust_package.pdf
    # Comparer la sortie avec SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Télécharger le fichier de checksums
    Invoke-WebRequest -Uri "https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt" -OutFile SHA256SUMS.txt

    # Vérifier un fichier spécifique
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # Comparer la sortie Hash avec SHA256SUMS.txt
    Get-Content .\SHA256SUMS.txt
    ```

## Contenu du zip d'artefacts

Le `aimo-standard-artifacts.zip` contient :

- `schemas/jsonschema/*` — Schémas JSON pour la validation
- `templates/ev/*` — Modèles de preuves (JSON + Markdown)
- `examples/*` — Lots de preuves d'échantillon
- `coverage_map/coverage_map.yaml` — Correspondance des standards externes
- `validator/rules/*` — Définitions des règles de validation
- `VERSIONING.md`, `GOVERNANCE.md`, `SECURITY.md`, etc.

## Ressources

- **Table d'historique des versions** : [Standard > Versions](../standard/versions/) — table des versions avec liens directs vers tous les actifs de version (PDF, ZIP, SHA256)
- **Changelog (spec)** : [Standard > Actuel > Changelog](../standard/current/08-changelog/) — historique des changements normatifs et non-normatifs.
- **Processus de release** : tagging `vX.Y.Z`, build CI, PDF sous `dist/`, checksums, actifs GitHub Release. Voir [GOVERNANCE.md](https://github.com/billyrise/aimo-standard/blob/main/GOVERNANCE.md) et [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) dans le dépôt.
- **Guide de migration** : [MIGRATION.md](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) — chemins de mise à niveau pour les changements cassants.

Pour la gouvernance et la politique de versionnement, voir [Gouvernance](../governance/).

## Préparer votre package de soumission

Lors de la préparation des preuves pour soumission d'audit :

1. **Créer votre lot de preuves** : Suivez [Lot de preuves](../artifacts/evidence-bundle/) et [Exigences minimales de preuves](../artifacts/minimum-evidence/) pour créer les enregistrements EV, dictionnaire, résumé et journal des modifications.
2. **Exécuter le validateur** : Exécutez `python validator/src/validate.py bundle/root.json` pour vérifier la cohérence structurelle. Corrigez toutes les erreurs avant de continuer.
3. **Générer les checksums** : Créez les checksums SHA-256 pour la vérification :

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
4. **Packager** : Créez une archive zip de votre répertoire de lot.
5. **Documenter l'alignement de version** : Notez quelle version du standard AIMO (ex. `v1.0.0`) vos preuves sont alignées.
6. **Livrer** : Fournissez le package, les checksums et la référence de version à votre auditeur.

Pour le guide de préparation complet, voir [Package de confiance](../governance/trust-package/).

## Pour les auditeurs : procédure de vérification

Les auditeurs recevant des soumissions de preuves doivent vérifier l'intégrité et la structure :

1. **Vérifier les checksums** : Exécutez la vérification des checksums (Linux : `sha256sum -c`, macOS : `shasum -a 256 -c`, Windows : `Get-FileHash`) pour confirmer l'intégrité des fichiers
2. **Exécuter le validateur** : Exécutez `python validator/src/validate.py bundle/root.json` pour vérifier la structure
3. **Confirmer la version** : Vérifiez que la version du standard AIMO indiquée existe sur [GitHub Releases](https://github.com/billyrise/aimo-standard/releases)

!!! tip "Obtenir les outils de manière indépendante"
    Les auditeurs doivent télécharger le validateur et les schémas directement de la version officielle du standard AIMO, pas de la partie soumettante.

Pour la procédure de vérification complète (checksums, attestation, pas à pas), voir **[Standard → Versions → Procédure de vérification](../standard/versions/)**. Voir aussi [Package de confiance](../governance/trust-package/) pour les matériaux prêts pour les auditeurs.

## Déclaration de non-déclaration excessive

!!! warning "Important"
    Le standard AIMO soutient **l'explicabilité et la préparation des preuves**. Il ne fournit **pas** d'avis juridique, ne garantit pas la conformité et ne certifie pas la conformité à une réglementation ou cadre. Les adopteurs doivent vérifier les déclarations par rapport aux textes faisant autorité et obtenir des conseils professionnels si nécessaire.

Voir [Périmètre de responsabilité](../governance/responsibility-boundary/) pour le périmètre, les hypothèses et les responsabilités des adopteurs.
