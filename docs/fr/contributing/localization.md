---
description: Guide de localisation AIMO - Structure i18n, flux de travail de maintenance et principes SSOT pour la documentation multilingue.
---
<!-- aimo:translation_status=translated -->

# Guide de localisation

Cette page documente la structure de localisation (i18n), le flux de travail de maintenance et les principes SSOT (Source Unique de Vérité) pour la documentation du standard AIMO.

## Politique de pureté linguistique

**Chaque page de langue ne doit contenir que le contenu de cette langue.**

| Règle | Description |
| --- | --- |
| **Pages EN** | Ne doivent pas contenir de caractères CJK ou de références à des colonnes spécifiques à une langue (ex. suffixes `_ja`) |
| **Pages JA** | Ne doivent pas expliquer la terminologie spécifique à l'EN comme si c'était la structure canonique |
| **Exceptions** | Listées dans `MIXED_LANGUAGE_ALLOWLIST` dans `tooling/checks/lint_i18n.py` |

Cette politique assure :
1. Les lecteurs ne voient que leur langue sélectionnée
2. L'ajout de nouvelles langues ne nécessite pas de mettre à jour les pages existantes
3. La CI peut automatiquement détecter les violations

## Structure linguistique

La documentation du standard AIMO utilise une **structure i18n basée sur les dossiers** :

```
docs/
├── en/           # Anglais (canonique)
├── ja/           # Japonais (日本語)
├── es/           # Espagnol (Español)
├── fr/           # Français (Français)
├── de/           # Allemand (Deutsch)
├── pt/           # Portugais (Português)
├── it/           # Italien (Italiano)
├── zh/           # Chinois simplifié (简体中文)
├── zh-TW/        # Chinois traditionnel (繁體中文)
└── ko/           # Coréen (한국어)
```

- **L'anglais est canonique** : Le dossier `docs/en/` est la source faisant autorité pour le contenu de la documentation.
- **Les autres langues reflètent la structure** : Chaque dossier de langue (`ja/`, etc.) maintient la même structure de fichiers que `en/`.
- **Mêmes noms de fichiers** : Toutes les langues utilisent l'extension `.md` (pas de suffixe de langue dans les noms de fichiers).
- **Repli vers l'anglais** : Les traductions manquantes retombent automatiquement sur le contenu anglais.

## Modèle de données taxonomique

La taxonomie utilise une **structure canonique neutre linguistiquement** avec des packs de traduction séparés :

```
data/
└── taxonomy/
    ├── canonical.yaml           # Neutre linguistiquement (codes, statut, cycle de vie)
    └── i18n/
        ├── en.yaml              # Libellés et définitions anglais
        ├── ja.yaml              # Libellés et définitions japonais
        └── {lang}.yaml          # Langues supplémentaires (modèle vide)
```

### Structure canonique (`canonical.yaml`)

Contient les données neutres linguistiquement :

- Identifiants de code (ex. `FS-001`, `UC-001`)
- Statut (`active`, `deprecated`, `removed`)
- Métadonnées de cycle de vie (`introduced_in`, `deprecated_in`, `removed_in`, `replaced_by`)
- Notes de portée et exemples (en anglais, comme références techniques)

### Packs de traduction (`i18n/*.yaml`)

Chaque pack de langue contient :

- Noms de dimensions (ex. "Functional Scope")
- Libellés de codes (ex. "End-user Productivity")
- Définitions de codes

**Repli** : Si une traduction est manquante, le système utilise l'anglais.

## Principe SSOT

AIMO utilise une **architecture SSOT-first** pour les données taxonomiques :

| Type d'actif | Emplacement SSOT | Description |
| --- | --- | --- |
| **Taxonomie (structure)** | `data/taxonomy/canonical.yaml` | Structure neutre linguistiquement (SSOT) |
| **Taxonomie (i18n)** | `data/taxonomy/i18n/*.yaml` | Traductions par langue (SSOT) |
| **Carte de couverture** | `coverage_map/coverage_map.yaml` | Correspondance cadre-preuve |
| **Schémas** | `schemas/jsonschema/` | Schémas de validation JSON |

### Fichiers dérivés

Les fichiers suivants sont **générés** à partir du SSOT et ne doivent PAS être édités manuellement :

| Fichier | Généré depuis | Générateur |
| --- | --- | --- |
| `artifacts/taxonomy/{version}/{lang}/taxonomy_dictionary.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_en.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_ja.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/code_system.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/dimensions_en_ja.md` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_dictionary.json` | canonical + i18n | `build_artifacts.py` |

### Codes de langue (BCP47)

AIMO utilise les codes de langue BCP47 :

| Code | Langue | Statut |
| --- | --- | --- |
| `en` | Anglais | Canonique (source) |
| `ja` | Japonais (日本語) | Actif |
| `es` | Espagnol (Español) | Actif |
| `fr` | Français (Français) | Actif |
| `de` | Allemand (Deutsch) | Actif |
| `pt` | Portugais (Português) | Actif |
| `it` | Italien (Italiano) | Actif |
| `zh` | Chinois simplifié (简体中文) | Actif |
| `zh-TW` | Chinois traditionnel (繁體中文) | Actif |
| `ko` | Coréen (한국어) | Actif |

### Fichiers CSV hérités (figés)

Les fichiers CSV mixtes EN/JA hérités dans `source_pack/03_taxonomy/legacy/` sont :

- **Figés à 21 colonnes** — aucune nouvelle colonne de langue ne sera ajoutée
- **Maintenus pour la rétrocompatibilité** — les intégrations existantes peuvent continuer à les utiliser
- **Appliqués par CI** — l'ajout de `label_es`, `definition_de`, etc. fera échouer le build

Pour les nouvelles langues, utilisez les artefacts par langue dans `artifacts/taxonomy/{version}/{lang}/`.

## Suivi de la fraîcheur des traductions

AIMO utilise un système de **suivi de la fraîcheur des traductions** pour maintenir la cohérence entre l'anglais (source) et le contenu traduit.

### Comment ça fonctionne

1. Chaque fichier traduit contient des métadonnées suivant quelle version de la source anglaise a été traduite
2. Quand le contenu anglais est mis à jour, le système détecte les traductions obsolètes
3. La CI avertit des traductions obsolètes mais ne bloque pas (les traductions peuvent être en retard)

### Métadonnées de traduction

Les fichiers traduits incluent des métadonnées frontmatter :

```yaml
---
# TRANSLATION METADATA - DO NOT REMOVE
source_file: en/standard/current/01-overview.md
source_hash: abc123def456
translation_date: 2026-02-02
translator: human|machine|hybrid
translation_status: current|outdated|needs_review
---
```

### Utilisation de l'outil de synchronisation

```bash
# Vérifier toutes les traductions pour la fraîcheur
python tooling/i18n/sync_translations.py --check

# Vérifier une langue spécifique
python tooling/i18n/sync_translations.py --check --lang ja

# Générer un rapport de traduction
python tooling/i18n/sync_translations.py --report

# Initialiser une nouvelle langue (copier EN comme base)
python tooling/i18n/sync_translations.py --init-lang es

# Mettre à jour les métadonnées après avoir terminé la traduction
python tooling/i18n/sync_translations.py --update-meta docs/ja/index.md
```

Pour les spécifications techniques détaillées, voir `tooling/i18n/TRANSLATION_SYNC_SPEC.md`.

## Flux de travail de mise à jour

### Mises à jour de taxonomie (nouveau flux SSOT-First)

1. Éditez le SSOT dans `data/taxonomy/` :
   - Changements de structure → `canonical.yaml`
   - Traductions anglaises → `i18n/en.yaml`
   - Traductions japonaises → `i18n/ja.yaml`
2. Exécutez la validation : `python tooling/checks/lint_taxonomy_ssot.py`
3. Régénérez tous les fichiers dérivés : `python tooling/taxonomy/build_artifacts.py --version current --langs en ja`
4. Mettez à jour les pages de documentation si nécessaire
5. Committez tous les changements ensemble

### Mises à jour de la carte de couverture

1. Éditez `coverage_map/coverage_map.yaml` (le SSOT)
2. Mettez à jour les tables de pages de cadre correspondantes (`docs/en/coverage-map/*.md`)
3. Mettez à jour les traductions japonaises (`docs/ja/coverage-map/*.md`)
4. Committez tous les changements ensemble

### Mises à jour de documentation

1. Éditez la source anglaise (`docs/en/...`)
2. Mettez à jour les traductions si nécessaire (ou marquez-les pour mise à jour ultérieure)
3. Exécutez `python tooling/i18n/sync_translations.py --check` pour voir les traductions obsolètes
4. Exécutez `python tooling/checks/lint_i18n.py` pour vérifier la cohérence des titres
5. Exécutez `mkdocs build --strict` pour vérifier le build
6. Committez tous les changements ensemble

!!! note "Priorité de traduction"
    Toutes les traductions n'ont pas besoin d'être mises à jour immédiatement. Les pages de niveau 1 (critiques) doivent être priorisées :
    
    - `index.md`
    - `standard/current/*.md`
    - `governance/index.md`
    - `releases/`

## Ajouter une nouvelle langue (5 étapes)

Pour ajouter une nouvelle langue (ex. espagnol) :

### Étape 1 : Générer le pack taxonomique

```bash
python tooling/taxonomy/build_i18n_taxonomy.py --add-lang es --lang-name "Español"
```

Crée `data/taxonomy/i18n/es.yaml` avec les références anglaises en commentaires.

### Étape 2 : Créer le dossier docs

```bash
mkdir -p docs/es && cp -r docs/en/* docs/es/
```

### Étape 3 : Mettre à jour mkdocs.yml

```yaml
plugins:
  - i18n:
      languages:
        - locale: es
          name: Español
          build: true
```

### Étape 4 : Traduire

- Traduisez `data/taxonomy/i18n/es.yaml`
- Traduisez les fichiers dans `docs/es/`

### Étape 5 : Vérifier

```bash
python tooling/checks/lint_i18n.py && mkdocs build --strict
```

!!! success "Terminé"
    La nouvelle langue est maintenant disponible à `/dev/es/`

## Conventions de nommage des fichiers

| Modèle | Exemple | Description |
| --- | --- | --- |
| `index.md` | `docs/en/governance/index.md` | Page d'accueil de section |
| `{topic}.md` | `docs/en/governance/trust-package.md` | Page de sujet |
| `{NN}-{topic}.md` | `docs/en/standard/current/03-taxonomy.md` | Page de spécification numérotée |

## Vérifications de qualité

Exécutez ces vérifications avant de committer :

```bash
# structure i18n, cohérence des titres et détection de phrases obsolètes
python tooling/checks/lint_i18n.py

# lints de schéma et de manifeste
python tooling/checks/lint_schema.py
python tooling/checks/lint_manifest.py

# lints SSOT de taxonomie
python tooling/checks/lint_taxonomy_ssot.py --required-langs en
python tooling/checks/lint_legacy_csv.py
python tooling/checks/lint_taxonomy_dictionary.py
python tooling/checks/lint_taxonomy_json.py

# artefacts de taxonomie à jour
python tooling/taxonomy/build_artifacts.py --check

# vérification du build
mkdocs build --strict
```

## Pages connexes

- [Versions](../../releases/) — Packages téléchargeables
- [Gouvernance](../../governance/) — Gouvernance du projet
