---
description: Níveis de conformidade AIMO Standard. Como as organizações declaram conformidade, requisitos de evidências e o que cada nível significa para a governação da IA.
---
<!-- aimo:translation_status=translated -->

# Conformidade

!!! warning "Importante: Não é certificação, não é asseguração, não é declaração de conformidade legal"
    O AIMO Standard define um **formato de empacotamento e validação de evidências**. Não certifica conformidade com leis ou normas.
    As opiniões de auditoria e asseguração permanecem responsabilidade dos auditores independentes e da organização adoptante.
    **Declaração apropriada:** "Um Pacote de Evidências foi produzido de acordo com o AIMO Standard v0.1.2 e validado estruturalmente pelo Validador AIMO."
    <!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
    **Declaração inapropriada:** "Conforme à Lei de IA da UE", "ISO 42001 certificado", "aprovado pelo governo".
    <!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

Estes níveis são **níveis internos de maturidade de evidências** para empacotamento e rastreabilidade. **Não** são certificação, **não** são opinião de asseguração nem conformidade legal ou regulamentar.

!!! note "Alias do nome do nível"
    O nível superior foi referido informalmente como "Gold" no passado; o **nome oficial do nível é Audit-Ready**.

## Quadro de conformidade AIMO (AIMO-MS / AIMO-Controls / AIMO-Audit)

| Componente | Descrição | Expectativas de evidências |
| --- | --- | --- |
| **AIMO-MS** | Estrutura orientada ao sistema de gestão: políticas, funções, artefactos alinhados PDCA que podem apoiar controlos tipo ISO/IEC 42001. | Request, review, exception, renewal, change log; Summary e Dictionary. |
| **AIMO-Controls** | Controlos de ciclo de vida e integridade: request→review→exception→renewal, hashing, assinatura (conforme [estrutura do Pacote de Evidências](../../standard/current/09-evidence-bundle-structure/)). | Object_index, payload_index, hash_chain, signing; registos de ciclo de vida. |
| **AIMO-Audit** | Preparação para transferência de auditoria: validador aprovado, somas de verificação, attestation opcional e índice de transferência de auditoria. | Saída do validador, bundle_id, identidade do produtor, metadados de assinatura opcionais e índice de transferência. |

As expectativas de evidências são descritas em [Requisitos Mínimos de Evidências](../artifacts/minimum-evidence/) e [Pacote de Evidências](../artifacts/evidence-bundle/).

## Níveis de conformidade (apenas AIMO)

### Nível 1 — Foundation

**Objetivo:** Linha de base rastreável. Conjunto mínimo para que o pacote seja identificável, verificável em integridade e verificado pelo validador.

### Nível 2 — Operational

**Objetivo:** Evidências de controlo operacional. Constrói sobre Foundation com rasto de ciclo de vida e supervisão.

### Nível 3 — Audit-Ready

**Objetivo:** Qualidade da transferência de auditoria. Attestation completa, reprodutibilidade e ranhura para formulários externos.

## Evidência mínima por nível (resumo)

| Nível | MUST (resumo) |
| --- | --- |
| **Foundation** | Estrutura do pacote (manifest, object_index, payload_index); sha256 para objetos referenciados; bundle_id, created_at, producer; execução do validador + versão; linha de base do dicionário de evidências; declaração de acesso e retenção. SHOULD: entrada mínima no change log. |
| **Operational** | Todos os MUST Foundation; rasto de ciclo de vida; ≥1 artefacto de supervisão; entradas do change log referenciam objetos impactados; declaração explícita de limite prova vs. asseguração. |
| **Audit-Ready** | Todos os MUST Operational; ≥1 assinatura sobre o manifest; TSA ou "sem TSA"; pacote de reprodutibilidade; Formulários externos listados e referenciados; declaração de integridade limitada; índice de transferência de auditoria. |

A **presença** de pelo menos uma assinatura (que tenha como alvo o manifest) é exigida pela [estrutura do Pacote de Evidências](../../standard/current/09-evidence-bundle-structure/) normativa para todos os pacotes.

## Mapeamento ISO/IEC 42001 (informativo)

Consulte [Mapa de Cobertura — ISO/IEC 42001](../coverage-map/iso-42001/) e [Kit de preparação para certificação ISO 42001](../artifacts/iso-42001-certification-readiness-toolkit/) para detalhes.

## Modelos de redação de declarações (anti-sobredeclaração)

Utilize apenas declarações que descrevam com precisão o que foi feito. A certificação e a conformidade legal permanecem responsabilidade dos adoptantes e dos organismos acreditados.

**Aceitáveis (exemplos):** "Somos conformes AIMO (Nível 2) com o AIMO Standard v0.1.2; isto não implica certificação ISO nem conformidade legal." / "Um Pacote de Evidências foi produzido de acordo com o AIMO Standard v0.1.2 e validado estruturalmente pelo Validador AIMO."

**Inaceitáveis (exemplos):** "Conforme à Lei de IA da UE" / "ISO 42001 certificado" / "Aprovado pelo governo" (A AIMO não certifica conformidade regulamentar; a certificação é emitida por organismos acreditados.)

## Páginas relacionadas

- [Trust Package](../governance/trust-package/) — Ponto de entrada consolidado para auditores
- [Responsibility Boundary](../governance/responsibility-boundary/) — O que a AIMO fornece e não fornece
- [Standard (Current)](../standard/current/) — Requisitos normativos
- [Artifacts](../artifacts/) — Estrutura de evidências e requisitos mínimos
- [Validator](../validator/) — Validação estrutural
