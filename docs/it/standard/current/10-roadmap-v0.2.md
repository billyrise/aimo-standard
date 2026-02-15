---
description: Roadmap informativa per v0.2. SSOT oggetti di audit, Evidence-as-Code, profili di output, libreria di test, ciclo di vita, JNC.
---
<!-- aimo:translation_status=translated -->

# Roadmap v0.2 (informativa)

Questa pagina riassume le direzioni pianificate per una **futura versione principale** (v0.2). È **solo informativa**; la specifica normativa di ogni release è lo standard e gli schemi di quella versione. Timeline obiettivo: 2026 Q4–2027.

## Temi pianificati

| Tema | Riepilogo |
| --- | --- |
| **Modello di oggetti di audit (SSOT)** | Requirement, Control, Claim, Evidence, Test, Finding, Remediation, Approval, Scope, VersionChange come oggetti normativi con ID fissi e integrità referenziale. |
| **Ponte verso quadri esterni** | Profili di output per Allegato IV UE, modulo GPAI, ISO 42001, NIST AI RMF; mappatura leggibile da macchina ed export opzionale in un clic. |
| **Evidence-as-Code** | Integrità normativa: verifica delle firme, provenienza (es. stile SLSA), riproducibilità e tracciamento delle modifiche. |
| **Libreria di procedure di test** | Modelli di test standard per controllo; allineamento con ISAE 3000, SOC 2, ISO 19011. |
| **Ciclo di vita operativo** | Processo guidato da eventi (Intake → Review → Exception → Renewal → Change → Decommission) con log e evidence richiesti. |
| **Profili per settore / giurisdizione** | Profili opzionali per settore e giurisdizione. |
| **Non conformità giustificata (JNC)** | Meccanismo opzionale per registrare e giustificare la non conformità intenzionale (informativo). |
| **Collegamento OSCAL** | Modo standard per collegare l'Evidence Bundle a Control/Requirement per l'export verso NIST OSCAL o simile. |

## Riferimenti

- [Ambito del modello di oggetti v0.1](https://github.com/billyrise/aimo-standard/blob/main/source_pack/07_release/v0.1_object_model_scope.md) — MUST v0.1 vs. riservato
- [Roadmap verifica firme](../../../artifacts/signature-verification-roadmap/) — evoluzione di firma e verifica
- [Releases](../../../releases/) — risorse di release e changelog
