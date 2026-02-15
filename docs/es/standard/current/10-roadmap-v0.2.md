---
description: Hoja de ruta informativa para v0.2. SSOT de objetos de auditoría, Evidence-as-Code, perfiles de salida, biblioteca de pruebas, ciclo de vida, JNC.
---
<!-- aimo:translation_status=translated -->

# Hoja de ruta v0.2 (informativa)

Esta página resume las direcciones previstas para una **futura versión principal** (v0.2). Es **solo informativa**; la especificación normativa de cada versión es el estándar y los esquemas de esa versión. Cronograma objetivo: 2026 Q4–2027.

## Temas previstos

| Tema | Resumen |
| --- | --- |
| **Modelo de objetos de auditoría (SSOT)** | Requirement, Control, Claim, Evidence, Test, Finding, Remediation, Approval, Scope, VersionChange como objetos normativos con IDs fijos e integridad referencial. |
| **Puente con marcos externos** | Perfiles de salida para Anexo IV UE, formulario GPAI, ISO 42001, NIST AI RMF; mapeo legible por máquina y exportación opcional en un clic. |
| **Evidence-as-Code** | Integridad normativa: verificación de firmas, procedencia (p. ej. estilo SLSA), reproducibilidad y seguimiento de cambios. |
| **Biblioteca de procedimientos de prueba** | Plantillas de prueba estándar por control; alineación con ISAE 3000, SOC 2, ISO 19011. |
| **Ciclo de vida operativo** | Proceso impulsado por eventos (Intake → Review → Exception → Renewal → Change → Decommission) con registros y evidencia requeridos. |
| **Perfiles por sector / jurisdicción** | Perfiles opcionales por sector y jurisdicción. |
| **No conformidad justificada (JNC)** | Mecanismo opcional para registrar y justificar la no conformidad intencional (informativo). |
| **Vinculación OSCAL** | Forma estándar de vincular el Paquete de Evidencia a Control/Requirement para exportar a NIST OSCAL o similar. |

## Referencias

- [Alcance del modelo de objetos v0.1](https://github.com/billyrise/aimo-standard/blob/main/source_pack/07_release/v0.1_object_model_scope.md) — MUST de v0.1 vs. reservado
- [Hoja de ruta de verificación de firmas](../../../artifacts/signature-verification-roadmap/) — evolución de firma y verificación
- [Releases](../../../releases/) — recursos de versión y registro de cambios
