---
description: Historique des versions du standard AIMO. Versions officielles figées avec PDF prêts pour les auditeurs, artefacts lisibles par machine, checksums et attestations de provenance de build.
---

# Versions

Les versions officielles sont des instantanés figés publiés avec des PDF prêts pour les auditeurs et des artefacts lisibles par machine.

## Dernière version

!!! success "Version actuelle"
    **v0.0.2** (2026-02-02) — [Voir la documentation](../current/) | [Version GitHub](https://github.com/billyrise/aimo-standard/releases/tag/v0.0.2)

## Historique des versions

| Version | Date | Notes de version | PDF (EN) | PDF (JA) | Artefacts | Checksums |
| :------ | :--- | :------------ | :------- | :------- | :-------- | :-------- |
| **v0.0.2** | 2026-02-02 | [Changelog](../current/08-changelog/) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/SHA256SUMS.txt) |
| **v0.0.1** | 2026-02-02 | [Changelog](../current/08-changelog/) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/SHA256SUMS.txt) |

!!! note "Source de données"
    Ce tableau des versions est synchronisé avec [GitHub Releases](https://github.com/billyrise/aimo-standard/releases). Chaque tag de version (`vX.Y.Z`) correspond à un instantané figé de la spécification.

## Source unique de vérité (SSOT) pour « latest »

La **définition faisant autorité de « latest »** est le tag **latest** des [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) (`releases/latest`). Le chemin du site `/latest/` redirige toujours vers ce release. Il n’y a pas de « latest site » séparé : le workflow de release déploie la version taguée et la définit comme alias `latest` en une seule étape.

| Source | Rôle |
|--------|------|
| **Tag latest de GitHub Release** | SSOT — seule définition du « release actuel » |
| **Tableau des versions** (cette page) | Synchronisé avec les releases via le workflow ; doit correspondre au tag avant déploiement |
| **Changelog** | Historique des changements normatif ; les notes de release s’y réfèrent |
| **Site `/latest/`** | Redirection vers la même version que GitHub Release latest |

Pour les détails du processus de release, voir [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) et le [workflow release](https://github.com/billyrise/aimo-standard/blob/main/.github/workflows/release.yml). Le tableau des versions et le Changelog sont mis à jour dans le cadre de la préparation du release pour qu’ils correspondent toujours à la version déployée.

## Avis juridiques et marques

**English notice (key facts):** Only AIMOaaS has been filed for trademark registration by RISEby Inc. (pending). "AIMO" is a registered trademark owned by third parties; RISEby Inc. does not claim ownership. For full trademark status and usage, see [Governance → Marques](../../governance/trademarks/) and [TRADEMARKS.md](https://github.com/billyrise/aimo-standard/blob/main/TRADEMARKS.md).

## Pour les auditeurs : URL canonique et épinglage de version

Pour citer une version précise dans les rapports d’audit et assurer la reproductibilité :

1. **URL canonique** : Utilisez l’URL de documentation figée pour cette version, ex. `https://standard.aimoaas.com/0.0.3/` (remplacez `0.0.3` par la version utilisée).
2. **Épinglage de version** : Enregistrez le **tag de release** (ex. `v0.0.3`) et éventuellement le **hash de commit** depuis la page [GitHub Release](https://github.com/billyrise/aimo-standard/releases). Cela permet de vérifier de manière indépendante que le snapshot de spécification correspond aux artefacts du release (PDF, ZIP, checksums).
3. **Alignement des preuves** : Indiquez dans votre soumission avec quelle version d’AIMO Standard (ex. `v0.0.3`) votre evidence bundle est aligné, et obtenez le validateur et les schémas depuis ce même release.

## Couches de version

AIMO Standard utilise trois concepts de version. Pour le release actuel ils sont alignés ; dans les releases futurs ils pourront être versionnés indépendamment.

| Couche | Description | Où cela apparaît |
|--------|-------------|------------------|
| **Version Standard** (site/release) | Le tag de release et le snapshot de documentation (ex. `v0.0.3`). | Tableau des versions, GitHub Releases, URLs `/X.Y.Z/`. |
| **Version du schéma Taxonomy** | Version du système de codes et des définitions taxonomy/schéma. | `taxonomy_version` dans les manifestes ; `$id` du schéma ou docs. |
| **Version du contenu Dictionary** | Version des entrées du dictionnaire (codes et définitions). | Métadonnées du dictionnaire ; identique à taxonomy pour 0.0.x. |

Lorsqu’on cite « AIMO Standard vX.Y.Z », la **version Standard** est celle qui définit le snapshot canonique. Le Validator et les Minimum Evidence Requirements se réfèrent aux artefacts et schémas de ce release.

## Procédure de vérification

Les auditeurs et implémenteurs doivent vérifier l'intégrité des téléchargements en utilisant les checksums SHA-256 :

### 1. Télécharger les actifs de version

=== "Linux / macOS"

    ```bash
    # Télécharger tous les actifs pour une version spécifique
    VERSION=v0.0.1
    BASE_URL="https://github.com/billyrise/aimo-standard/releases/download/${VERSION}"

    curl -LO "${BASE_URL}/trust_package.pdf"
    curl -LO "${BASE_URL}/trust_package.ja.pdf"
    curl -LO "${BASE_URL}/aimo-standard-artifacts.zip"
    curl -LO "${BASE_URL}/SHA256SUMS.txt"
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Télécharger tous les actifs pour une version spécifique
    $VERSION = "v0.0.1"
    $BASE_URL = "https://github.com/billyrise/aimo-standard/releases/download/$VERSION"

    Invoke-WebRequest -Uri "$BASE_URL/trust_package.pdf" -OutFile trust_package.pdf
    Invoke-WebRequest -Uri "$BASE_URL/trust_package.ja.pdf" -OutFile trust_package.ja.pdf
    Invoke-WebRequest -Uri "$BASE_URL/aimo-standard-artifacts.zip" -OutFile aimo-standard-artifacts.zip
    Invoke-WebRequest -Uri "$BASE_URL/SHA256SUMS.txt" -OutFile SHA256SUMS.txt
    ```

### 2. Vérifier les checksums

=== "Linux"

    ```bash
    # Vérifier tous les fichiers téléchargés par rapport aux checksums
    sha256sum -c SHA256SUMS.txt

    # Sortie attendue (tous doivent afficher "OK") :
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "macOS"

    ```bash
    # Vérifier tous les fichiers téléchargés par rapport aux checksums
    shasum -a 256 -c SHA256SUMS.txt

    # Sortie attendue (tous doivent afficher "OK") :
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Vérifier chaque fichier
    Get-FileHash .\trust_package.pdf -Algorithm SHA256
    Get-FileHash .\trust_package.ja.pdf -Algorithm SHA256
    Get-FileHash .\aimo-standard-artifacts.zip -Algorithm SHA256

    # Comparer la sortie Hash avec SHA256SUMS.txt
    Get-Content .\SHA256SUMS.txt
    ```

### 3. Vérification manuelle (alternative)

=== "Linux"

    ```bash
    # Calculer le hash pour un fichier spécifique
    sha256sum trust_package.pdf

    # Comparer la sortie avec SHA256SUMS.txt
    cat SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # Calculer le hash pour un fichier spécifique
    shasum -a 256 trust_package.pdf

    # Comparer la sortie avec SHA256SUMS.txt
    cat SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Calculer le hash pour un fichier spécifique
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # Voir le fichier de checksums
    Get-Content .\SHA256SUMS.txt
    ```

!!! tip "Pour les auditeurs"
    Obtenez toujours le fichier de checksums directement depuis la version officielle GitHub, pas de la partie soumettante. Cela assure une vérification indépendante.

### 4. Vérifier la provenance de build (attestation)

Tous les actifs de version incluent des attestations de provenance de build signées cryptographiquement générées par GitHub Actions. Cela vous permet de vérifier que les actifs ont été construits dans le dépôt officiel sans altération.

**Prérequis** : Installer [GitHub CLI](https://cli.github.com/) (`gh`)

```bash
# Télécharger les actifs de version en utilisant GitHub CLI
VERSION=v0.0.1
gh release download "$VERSION" --repo billyrise/aimo-standard

# Vérifier l'attestation pour chaque actif
gh attestation verify trust_package.pdf --repo billyrise/aimo-standard
gh attestation verify trust_package.ja.pdf --repo billyrise/aimo-standard
gh attestation verify aimo-standard-artifacts.zip --repo billyrise/aimo-standard
gh attestation verify SHA256SUMS.txt --repo billyrise/aimo-standard
```

**Sortie attendue** (succès) :

```
Loaded digest sha256:abc123... for file trust_package.pdf
Loaded 1 attestation from GitHub API
✓ Verification succeeded!
```

**Vérification hors ligne** (environnements air-gapped) :

```bash
# D'abord, télécharger la racine de confiance (nécessite le réseau une fois)
gh attestation trusted-root > trusted-root.jsonl

# Puis vérifier hors ligne
gh attestation verify trust_package.pdf \
  --repo billyrise/aimo-standard \
  --custom-trusted-root trusted-root.jsonl
```

!!! info "Ce que l'attestation prouve"
    L'attestation de provenance de build prouve cryptographiquement que les actifs de version ont été :

    1. Construits par GitHub Actions (pas la machine locale d'un développeur)
    2. Construits depuis le dépôt officiel `billyrise/aimo-standard`
    3. Construits depuis le commit exact associé au tag de version
    4. Non modifiés après la fin du build

## Compatibilité

Le standard AIMO suit le [versionnement sémantique](https://semver.org/) (SemVer) :

| Type de changement | Incrément de version | Impact |
| :---------- | :----------- | :----- |
| **MAJEUR** | X.0.0 | Changements cassants — migration requise |
| **MINEUR** | 0.X.0 | Ajouts rétrocompatibles |
| **PATCH** | 0.0.X | Corrections et clarifications |

Pour la politique de versionnement complète, voir [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md).

## Migration

Lors de la mise à niveau entre versions avec des changements cassants :

1. Consultez le [Changelog](../current/08-changelog/) pour les changements cassants
2. Revoyez le [Guide de migration](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) pour les chemins de mise à niveau spécifiques
3. Mettez à jour votre lot de preuves pour vous aligner aux nouvelles exigences de schéma
4. Ré-exécutez le validateur pour vérifier la conformité

!!! warning "Changements cassants"
    Les mises à jour de version MAJEURE peuvent nécessiter des modifications aux lots de preuves existants. Revoyez toujours le guide de migration avant la mise à niveau.

## Instantanés de documentation versionnée

Chaque version crée un instantané de documentation figée accessible à :

- Production : `https://standard.aimoaas.com/{version}/` (ex. `/0.0.1/`)
- GitHub Pages : `https://billyrise.github.io/aimo-standard/{version}/`

### Types d'URL et leur signification

| Pattern d'URL | Description | Pour citations d'audit ? |
|-------------|-------------|---------------------|
| `/X.Y.Z/` (ex. `/0.0.1/`) | **Version figée** — instantané immutable | **Oui** (préféré) |
| `/latest/` | **Alias** — redirige vers la version la plus récente | Oui (résout vers `/X.Y.Z/`) |
| `/dev/` | **Aperçu** — contenu non publié de la branche main | **Non** (pas pour citations) |

!!! warning "Comprendre `/latest/` vs `/dev/`"
    - **`/latest/`** est un alias (redirection) vers la version **publiée** la plus récente. C'est sûr pour les citations car cela résout vers un instantané figé.
    - **`/dev/`** reflète la branche `main` actuelle et peut contenir des **changements non publiés**. Ne jamais citer `/dev/` dans les rapports d'audit.

### FAQ

??? question "Pourquoi `/latest/` n'est-il pas un numéro de version ?"
    `/latest/` est un alias de commodité qui redirige toujours vers la version stable la plus récente (ex. `/0.0.1/`). Cela permet aux utilisateurs de mettre en favoris une seule URL tout en obtenant automatiquement la version actuelle. Pour les audits formels nécessitant l'immutabilité, citez l'URL de version explicite à la place.

??? question "Quelle URL les auditeurs doivent-ils citer ?"
    - **Audits formels (immutabilité requise)** : Utilisez `/X.Y.Z/` (ex. `https://standard.aimoaas.com/0.0.1/standard/current/`)
    - **Références générales** : `/latest/` est acceptable car cela redirige vers la version actuelle
    - **Ne jamais citer** : `/dev/` (non publié, sujet à changement)

??? question "Et si `/latest/` affiche un contenu différent de celui attendu ?"
    Ce serait un bug de déploiement. Si vous suspectez que `/latest/` diffère de la [version GitHub](https://github.com/billyrise/aimo-standard/releases) la plus récente, veuillez [signaler un problème](https://github.com/billyrise/aimo-standard/issues). L'alias `/latest/` doit toujours rediriger vers la version taguée la plus récente.

## Ressources

- **[Hub des versions](../../../releases/)** — Préparation de soumission, vérification par l'auditeur, déclaration de non-déclaration excessive
- **[Package de confiance](../../governance/trust-package/)** — Matériaux d'assurance prêts pour les auditeurs
- **[Changelog (détaillé)](../current/08-changelog/)** — Historique complet des changements avec suivi des dépréciations
- **[VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)** — Politique de versionnement complète
