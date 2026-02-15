---
description: Estructura raíz normativa y manifest del Paquete de Evidencia (v0.1). Integrity MUST; Custody es definido por la implementación.
---
<!-- aimo:translation_status=translated -->

# Estructura raíz del Paquete de Evidencia (v0.1)

Esta página define el **layout raíz normativo** y el manifest de un Paquete de Evidencia. Los validadores DEBEN rechazar paquetes que no cumplan estos requisitos antes de cualquier validación de esquema.

## MUST normativo v0.1 (resumen)

- **manifest.json** en la raíz del paquete es obligatorio.
- **object_index** y **payload_index**: cada entrada DEBE incluir **sha256** (64 hex en minúsculas); las rutas DEBEN ser relativas y NO DEBEN contener `../` ni escapar de la raíz del paquete.
- **signing.signatures** DEBE ser un array no vacío (array vacío no válido).
- Cada entrada de firma DEBE tener: **path** bajo `signatures/` (traversión de ruta prohibida), **targets** (array, al menos una ruta), y al menos una firma en el paquete DEBE incluir **manifest.json** en **targets** (firma del manifest obligatoria).
- **hash_chain**: v0.1 DEBE incluir **algorithm**, **head**, **path** (bajo `hashes/`) y **covers** con al menos **manifest.json** y **objects/index.json**.

Los validadores DEBEN hacer cumplir esto antes de aceptar un paquete. El JSON Schema y el validador de referencia implementan las mismas reglas.

## Estructura raíz requerida (MUST)

En la raíz del paquete DEBEN estar presentes:

| Elemento | Tipo | Propósito |
| --- | --- | --- |
| **manifest.json** | Archivo | Manifest del paquete (véase abajo). Descriptor canónico del paquete. |
| **objects/** | Directorio | Objetos enumerados (p. ej. metadatos, índices). Listados en object_index de `manifest.json`. |
| **payloads/** | Directorio | Archivos de carga (p. ej. EV JSON raíz, archivos Evidence Pack). Listados en payload_index de `manifest.json`. |
| **signatures/** | Directorio | Firmas digitales. v0.1 DEBE contener al menos un archivo de firma que referencie el manifest (existencia y referencia de objetivo; verificación criptográfica es extensión futura). |
| **hashes/** | Directorio | Cadena de hashes o registros de integridad (según hash_chain de `manifest.json`). |

Los implementadores NO DEBEN enviar un paquete al que falte alguno. El Validador DEBE fallar con un mensaje claro cuando la estructura raíz esté incompleta.

## Integrity (normativo) vs. Custody (implementación)

- **Integrity** es **normativo** en v0.1: la norma exige que el paquete lleve metadatos de integridad (manifest, sha256 de archivos indexados, presencia de firma del manifest). Los validadores DEBEN comprobar que: existan los directorios y archivos requeridos; `manifest.json` esté presente y sea válido (esquema y comprobaciones previas); todo archivo listado en object_index y payload_index exista en la ruta dada y su contenido coincida con el `sha256` declarado; `signatures/` contenga al menos una firma que tenga como objetivo el manifest (v0.1: solo existencia y referencia; v0.1.1: metadatos de verificación RECOMMENDED; v0.2 previsto: verificación criptográfica en alcance).
- **Custody** (almacenamiento, control de acceso, retención, WORM) es **definido por la implementación**. La norma no prescribe cómo los custodios almacenan o protegen el paquete; solo exige que el paquete, al ser entregado, cumpla los requisitos de Integrity anteriores.

## manifest.json (campos MUST)

El manifest DEBE incluir al menos:

| Campo | Tipo | Descripción |
| --- | --- | --- |
| **bundle_id** | string (UUID) | Identificador único de este paquete. |
| **bundle_version** | string (SemVer) | Versión del paquete. |
| **created_at** | string (date-time) | Marca de tiempo de creación. |
| **scope_ref** | string | Referencia de alcance (p. ej. `SC-001`). Patrón `SC-*`. |
| **object_index** | array | Lista de objetos: `id`, `type`, `path`, `sha256`. Las rutas DEBEN ser relativas, NO contener `../` ni comenzar por `/`, y permanecer dentro de la raíz del Paquete de Evidencia (los validadores DEBEN rechazar rutas que salgan de la raíz). |
| **payload_index** | array | Lista de cargas: `logical_id`, `path`, `sha256`, `mime`, `size`. Mismas reglas de ruta que object_index. |
| **hash_chain** | object | **Normativo (v0.1):** DEBE incluir `algorithm` (sha256 \| merkle), `head` (64 hex minúsculas), `path` (ruta relativa bajo `hashes/`), `covers` (array, al menos un elemento). v0.1 DEBE incluir `manifest.json` y `objects/index.json` en `covers`. |
| **signing** | object | **Normativo (v0.1):** DEBE incluir `signatures` (array, al menos una entrada). Cada entrada: `signature_id`, `path` (relativo bajo `signatures/`), `targets` (array, al menos una ruta; v0.1 al menos una firma debe incluir `manifest.json` en targets), `algorithm` (ed25519, rsa-pss, ecdsa, unspecified). `created_at` (date-time) es MAY. **Nota:** La verificación criptográfica de firmas está fuera de alcance en v0.1; se requiere la referencia (qué archivo y qué objetivo). |

**Metadatos de firma opcionales v0.1.1 (RECOMMENDED para re-ejecución por terceros):** signer_identity, signed_at, verification_command, canonicalization.

Integrity y verificación: **v0.1** — solo referencia y existencia. **v0.1.1** — metadatos de verificación RECOMMENDED. **v0.2** (previsto) — verificación criptográfica en alcance.

- Los valores **sha256** DEBEN ser 64 caracteres hexadecimales en minúsculas.
- **path** DEBE ser ruta relativa; NO contener `../` ni comenzar por `/`; permanecer dentro de la raíz del Paquete de Evidencia.

Véase el JSON Schema: `schemas/jsonschema/evidence_bundle_manifest.schema.json`.

## Extensiones futuras (informativo)

- **Vinculación Control/Requirement**: Una versión futura podría añadir una forma estándar de vincular elementos del Paquete de Evidencia a identificadores Control o Requirement (p. ej. para exportar a NIST OSCAL u otros formatos de automatización de auditoría). No requerido en v0.1 ni v0.1.1.

## Referencias

- [Paquete de Evidencia (resumen del artefacto)](../../../artifacts/evidence-bundle/) — propósito e índice
- [Plantilla EV — Formularios externos e índice de traspaso a auditoría](../06-ev-template/#external-forms-official-templateschecklists-attached-as-is)
- [Hoja de ruta de verificación de firmas](../../../artifacts/signature-verification-roadmap/) — metadatos v0.1.1 y plan de verificación v0.2
- [Validador](../../../validator/) — cómo el validador hace cumplir esta estructura
- [Requisitos Mínimos de Evidencia](../../../artifacts/minimum-evidence/) — lista de comprobación MUST
