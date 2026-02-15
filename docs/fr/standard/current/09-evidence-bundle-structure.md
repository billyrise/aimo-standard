---
description: Structure racine normative et manifest du Paquet de preuves (v0.1). Integrity MUST ; Custody est défini par l'implémentation.
---
<!-- aimo:translation_status=translated -->

# Structure racine du Paquet de preuves (v0.1)

Cette page définit la **structure racine normative** et le manifest d'un Paquet de preuves. Les validateurs DOIVENT rejeter les paquets qui ne satisfont pas à ces exigences avant toute validation de schéma.

## MUST normatif v0.1 (résumé)

- **manifest.json** à la racine du paquet est requis.
- **object_index** et **payload_index** : chaque entrée DOIT inclure **sha256** (64 hex en minuscules) ; les chemins DOIVENT être relatifs et NE DOIVENT PAS contenir `../` ni s'échapper de la racine du paquet.
- **signing.signatures** DOIT être un tableau non vide (tableau vide invalide).
- Chaque entrée de signature DOIT avoir : **path** sous `signatures/` (traversée de chemin interdite), **targets** (tableau, au moins un chemin), et au moins une signature dans le paquet DOIT lister **manifest.json** dans **targets** (signature du manifest obligatoire).
- **hash_chain** : v0.1 DOIT inclure **algorithm**, **head**, **path** (sous `hashes/`) et **covers** avec au moins **manifest.json** et **objects/index.json**.

Les validateurs DOIVENT appliquer ces règles avant d'accepter un paquet. Le JSON Schema et le validateur de référence implémentent les mêmes règles.

## Structure racine requise (MUST)

À la racine du paquet, les éléments suivants DOIVENT être présents :

| Élément | Type | Objectif |
| --- | --- | --- |
| **manifest.json** | Fichier | Manifest du paquet (voir ci-dessous). Descripteur canonique du paquet. |
| **objects/** | Répertoire | Objets énumérés (p. ex. métadonnées, index). Listés dans object_index de `manifest.json`. |
| **payloads/** | Répertoire | Fichiers de charge (p. ex. EV JSON racine, fichiers Evidence Pack). Listés dans payload_index de `manifest.json`. |
| **signatures/** | Répertoire | Signatures numériques. v0.1 DOIT contenir au moins un fichier de signature référençant le manifest (existence et référence de cible ; vérification cryptographique est une extension future). |
| **hashes/** | Répertoire | Chaîne de hachage ou enregistrements d'intégrité (selon hash_chain de `manifest.json`). |

Les implémenteurs NE DOIVENT PAS soumettre un paquet auquel il manque l'un de ces éléments. Le Validateur DOIT échouer avec un message clair lorsque la structure racine est incomplète.

## Integrity (normatif) vs. Custody (implémentation)

- **Integrity** est **normatif** en v0.1 : la norme exige que le paquet porte des métadonnées d'intégrité (manifest, sha256 des fichiers indexés, présence de signature du manifest). Les validateurs DOIVENT vérifier que : les répertoires et fichiers requis existent ; `manifest.json` est présent et valide (schéma et vérifications préalables) ; chaque fichier listé dans object_index et payload_index existe au chemin donné et son contenu correspond au `sha256` déclaré ; `signatures/` contient au moins une signature ciblant le manifest (v0.1 : existence et référence uniquement ; v0.1.1 : métadonnées de vérification RECOMMENDED ; v0.2 prévu : vérification cryptographique dans le périmètre).
- **Custody** (stockage, contrôle d'accès, rétention, WORM) est **défini par l'implémentation**. La norme ne prescrit pas comment les gardiens stockent ou protègent le paquet ; elle exige seulement que le paquet, lors de la soumission, satisfasse aux exigences d'Integrity ci-dessus.

## manifest.json (champs MUST)

Le manifest DOIT inclure au moins :

| Champ | Type | Description |
| --- | --- | --- |
| **bundle_id** | string (UUID) | Identifiant unique de ce paquet. |
| **bundle_version** | string (SemVer) | Version du paquet. |
| **created_at** | string (date-time) | Horodatage de création. |
| **scope_ref** | string | Référence de périmètre (p. ex. `SC-001`). Modèle `SC-*`. |
| **object_index** | array | Liste d'objets : `id`, `type`, `path`, `sha256`. Les chemins DOIVENT être relatifs, NE DOIVENT PAS contenir `../` ni commencer par `/`, et rester dans la racine du Paquet de preuves (les validateurs DOIVENT rejeter les chemins sortant de la racine). |
| **payload_index** | array | Liste des charges : `logical_id`, `path`, `sha256`, `mime`, `size`. Mêmes règles de chemin que object_index. |
| **hash_chain** | object | **Normatif (v0.1) :** DOIT inclure `algorithm` (sha256 \| merkle), `head` (64 hex minuscules), `path` (chemin relatif sous `hashes/`), `covers` (tableau, au moins un élément). v0.1 DOIT inclure `manifest.json` et `objects/index.json` dans `covers`. |
| **signing** | object | **Normatif (v0.1) :** DOIT inclure `signatures` (tableau, au moins une entrée). Chaque entrée : `signature_id`, `path` (relatif sous `signatures/`), `targets` (tableau, au moins un chemin ; v0.1 au moins une signature doit inclure `manifest.json` dans targets), `algorithm` (ed25519, rsa-pss, ecdsa, unspecified). `created_at` (date-time) est MAY. **Note :** La vérification cryptographique des signatures est hors périmètre en v0.1 ; la référence (quel fichier et quelle cible) est requise. |

**Métadonnées de signature optionnelles v0.1.1 (RECOMMENDED pour réexécution par un tiers) :** signer_identity, signed_at, verification_command, canonicalization.

Intégrité et vérification : **v0.1** — référence et existence uniquement. **v0.1.1** — métadonnées de vérification RECOMMENDED. **v0.2** (prévu) — vérification cryptographique dans le périmètre.

- Les valeurs **sha256** DOIVENT être 64 caractères hexadécimaux en minuscules.
- **path** DOIT être un chemin relatif ; NE PAS contenir `../` ni commencer par `/` ; rester dans la racine du Paquet de preuves.

Voir le JSON Schema : `schemas/jsonschema/evidence_bundle_manifest.schema.json`.

## Extensions futures (informatif)

- **Liaison Control/Requirement** : Une version future pourrait ajouter une méthode standard pour lier les éléments du Paquet de preuves aux identifiants Control ou Requirement (p. ex. pour l'export vers NIST OSCAL ou formats similaires). Non requis en v0.1 ni v0.1.1.

## Références

- [Paquet de preuves (aperçu de l'artefact)](../../../artifacts/evidence-bundle/) — objectif et table des matières
- [Modèle EV — Formulaires externes et index de transfert d'audit](../06-ev-template/#external-forms-official-templateschecklists-attached-as-is)
- [Feuille de route de vérification des signatures](../../../artifacts/signature-verification-roadmap/) — métadonnées v0.1.1 et plan de vérification v0.2
- [Validator](../../../validator/) — comment le validateur applique cette structure
- [Exigences minimales de preuves](../../../artifacts/minimum-evidence/) — liste de contrôle MUST
