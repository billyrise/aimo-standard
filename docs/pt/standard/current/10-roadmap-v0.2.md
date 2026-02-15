---
description: Roadmap informativa para v0.2. SSOT de objetos de auditoria, Evidence-as-Code, perfis de saída, biblioteca de testes, ciclo de vida, JNC.
---
<!-- aimo:translation_status=translated -->

# Roadmap v0.2 (informativa)

Esta página resume as direções planeadas para uma **futura versão principal** (v0.2). É **apenas informativa**; a especificação normativa de cada versão é a norma e os esquemas dessa versão. Cronograma alvo: 2026 Q4–2027.

## Temas planeados

| Tema | Resumo |
| --- | --- |
| **Modelo de objetos de auditoria (SSOT)** | Requirement, Control, Claim, Evidence, Test, Finding, Remediation, Approval, Scope, VersionChange como objetos normativos com IDs fixos e integridade referencial. |
| **Ponte para quadros externos** | Perfis de saída para Anexo IV UE, formulário GPAI, ISO 42001, NIST AI RMF; mapeamento legível por máquina e exportação opcional em um clique. |
| **Evidence-as-Code** | Integridade normativa: verificação de assinaturas, proveniência (ex.: estilo SLSA), reprodutibilidade e rastreio de alterações. |
| **Biblioteca de procedimentos de teste** | Modelos de teste padrão por controlo; alinhamento com ISAE 3000, SOC 2, ISO 19011. |
| **Ciclo de vida operacional** | Processo orientado a eventos (Intake → Review → Exception → Renewal → Change → Decommission) com registos e evidências necessários. |
| **Perfis por setor / jurisdição** | Perfis opcionais por setor e jurisdição. |
| **Não conformidade justificada (JNC)** | Mecanismo opcional para registar e justificar não conformidade intencional (informativo). |
| **Ligação OSCAL** | Forma padrão de ligar o Pacote de Evidências a Control/Requirement para exportar para NIST OSCAL ou similar. |

## Referências

- [Âmbito do modelo de objetos v0.1](https://github.com/billyrise/aimo-standard/blob/main/source_pack/07_release/v0.1_object_model_scope.md) — MUST v0.1 vs. reservado
- [Roadmap de verificação de assinaturas](../../../artifacts/signature-verification-roadmap/) — evolução da assinatura e verificação
- [Releases](../../../releases/) — recursos de versão e registo de alterações
