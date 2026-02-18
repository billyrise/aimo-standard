---
description: Kit de prontidão para certificação ISO/IEC 42001. Caminho mais curto para evidência pronta para auditoria alinhada à ISO 42001 usando artefatos AIMO. Apoia apenas a prontidão; não confere certificação.
---
<!-- aimo:translation_status=translated -->

# Kit de prontidão para certificação ISO/IEC 42001

Esta página é um guia **prático e orientado à adoção** para produzir **evidência pronta para auditoria** alinhada à ISO/IEC 42001 usando artefatos AIMO. **Apoia a prontidão**; **não** confere certificação. As decisões de certificação permanecem com **organismos de certificação acreditados**.

## Objetivo

Produzir um Evidence Bundle estruturado e verificado pelo validador que apoie controles do tipo ISO/IEC 42001 (contexto, liderança, planejamento, suporte, operação, avaliação de desempenho, melhoria), para que os auditores possam localizar e verificar evidências com eficiência.

## Fluxo de trabalho em 5 passos

| Passo | Ação |
| --- | --- |
| **1. Estabelecer escopo e inventário de IA** | Definir escopo (scope_ref); classificar sistemas de IA usando a [taxonomia](../../standard/current/03-taxonomy/) e o [dicionário](../../standard/current/05-dictionary/). |
| **2. Definir artefatos do sistema de gestão** | Criar ou referenciar políticas, papéis e artefatos alinhados ao PDCA. Usar [AIMO-MS / AIMO-Controls](../../conformance/) como estrutura; referenciar [Modelo Evidence Pack](../../standard/current/06-ev-template/) (EP-01..EP-07). |
| **3. Produzir Evidence Bundle e evidência mínima** | Construir manifest, object_index, payload_index, hash_chain, signing conforme [estrutura do Pacote de Evidências](../../standard/current/09-evidence-bundle-structure/). Incluir request, review, exception, renewal, change_log conforme [Requisitos mínimos de evidência](minimum-evidence.md). |
| **4. Executar validador + checksums + controle de alterações** | Executar `python validator/src/validate.py <bundle_path> --validate-profiles`. Registar versão do validador e saída. Gerar checksums SHA-256; manter entradas do registro de alterações que referenciem os objetos impactados. |
| **5. Preparar pacote de auditoria** | Empacotar o pacote (zip ou equivalente); fornecer checksums. Opcionalmente anexar [saída do relatório de auditoria](../../standard/current/07-validator/) (audit-json / audit-html). Usar URLs versionadas (ex. `/0.1.2/`) ao citar o padrão. Para nível Audit-Ready, adicionar [Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index) e [External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is). |

## Lista de verificação: família de cláusulas ISO 42001 → artefatos AIMO → saídas de evidência

| Família de cláusulas ISO 42001 | Artefatos AIMO | Saídas de evidência |
| --- | --- | --- |
| Contexto (4.1) | Summary, Dictionary, scope_ref | scope_ref do manifesto; Summary; Dictionary |
| Liderança / Política (5.x) | Summary, review, dictionary | Registros de revisão; referências à política |
| Planejamento (6.x) | request, review, exception, EV, Dictionary | Solicitação/aprovação; risco/objetivos em EV ou Dictionary |
| Suporte (7.x) | Summary, review, EV, change_log | Documentação; evidência de competência/consciencialização |
| Operação (8.x) | EV, request, review, exception | Controles operacionais; aplicabilidade |
| Avaliação de desempenho (9.x) | EV, change_log, review, renewal | Monitorização; auditoria interna; revisão pela gestão |
| Melhoria (10.x) | exception, renewal, change_log | Ação corretiva; melhoria contínua |

Consulte [Coverage Map — ISO/IEC 42001](../../coverage-map/iso-42001/) e [ISO/IEC 42006](https://www.iso.org/standard/42006) para expectativas de organismos de auditoria.

## Linguagem segura

- **Usar:** "Utilizamos artefatos AIMO para apoiar a prontidão para ISO/IEC 42001; as decisões de certificação permanecem com organismos de certificação acreditados."
- **Não usar:** "ISO 42001 certificado pela AIMO" ou "AIMO certifica conformidade."

Padrão oficial (fonte primária): [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) (ISO). Este kit está alinhado com [Conformidade](../../conformance/) e [Limite de responsabilidade](../../governance/responsibility-boundary/) — a AIMO não certifica nem garante conformidade.

## Relacionado

- [Conformidade](../../conformance/) — Níveis (Foundation, Operational, Audit-Ready) e linguagem de declaração
- [Trust Package](../../governance/trust-package/) — Materiais prontos para auditor
- [Responsibility Boundary](../../governance/responsibility-boundary/) — O que a AIMO fornece e não fornece
