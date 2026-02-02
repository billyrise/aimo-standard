---
description: Limite de Responsabilidade AIMO - Define o que o padrão fornece vs. responsabilidades do adotante. Declaração de não-sobrereivindicação e limitações de escopo.
---

# Limite de Responsabilidade

Esta página define o que o AIMO Standard fornece e não fornece, as suposições que faz, e as responsabilidades dos adotantes.

## O que o AIMO Standard fornece

- **Um formato de evidências estruturado**: schemas, templates e taxonomia para evidências de governança de IA.
- **Framework de rastreabilidade**: vinculação de evidências baseada em ciclo de vida (solicitação → revisão → exceção → renovação).
- **Suporte à explicabilidade**: mapeamento de cobertura para frameworks externos para discussões de auditoria.
- **Ferramentas de validação**: validador de referência e regras para verificações de consistência estrutural.
- **Documentação**: especificação normativa, exemplos e orientação.

## O que o AIMO Standard NÃO fornece

| Fora de escopo | Explicação |
| --- | --- |
| **Aconselhamento jurídico** | AIMO não interpreta leis ou regulamentações. Consulte assessoria jurídica qualificada para conformidade regulatória. |
| **Certificação de conformidade** | Usar AIMO não certifica conformidade com qualquer regulamentação ou framework (ISO 42001, EU AI Act, NIST AI RMF, etc.). |
| **Avaliação de riscos** | AIMO estrutura evidências mas não realiza nem valida avaliações de risco de IA. |
| **Controles técnicos** | AIMO não implementa controle de acesso, criptografia ou outros controles de segurança; documenta expectativas. |
| **Execução de auditoria** | AIMO fornece materiais para auditores mas não conduz auditorias. |
| **Avaliação de modelo de IA** | AIMO não avalia desempenho de modelo, viés ou segurança. |

## Suposições

O AIMO Standard assume:

1. **Adotantes têm processos de governança**: fluxos de trabalho de solicitação, revisão, aprovação e exceção existem.
2. **Adotantes mantêm evidências**: evidências são criadas, armazenadas e retidas pelos sistemas do adotante.
3. **Adotantes verificam contra textos autoritativos**: ao usar Mapa de Cobertura, adotantes verificam o framework ou regulamentação original.
4. **Ferramentas são opcionais**: o validador de referência é uma conveniência; adotantes podem usar sua própria validação.

## Responsabilidades do adotante

| Responsabilidade | Descrição |
| --- | --- |
| **Criação de evidências** | Gerar registros de evidências precisos e oportunos alinhados com schema EV. |
| **Armazenamento e retenção de evidências** | Armazenar evidências com segurança com controles de acesso e períodos de retenção apropriados. |
| **Integridade e controle de acesso** | Implementar controles (hashing, WORM, logs de auditoria) para preservar integridade de evidências. |
| **Verificação jurídica** | Verificar reivindicações de conformidade contra textos jurídicos autoritativos e obter aconselhamento jurídico conforme necessário. |
| **Alinhamento contínuo** | Atualizar evidências e mapeamentos conforme versões do AIMO Standard e frameworks externos evoluem. |
| **Preparação para auditoria** | Empacotar pacotes de evidências e executar validação antes de submissão a auditores. |

## Matriz RACI

A seguinte matriz RACI esclarece responsabilidades entre papéis AIMO Standard, Adotante e Auditor.

| Atividade | AIMO Standard | Adotante | Auditor |
| --- | :---: | :---: | :---: |
| **Definir schema e templates de evidências** | R/A | I | I |
| **Criar registros de evidências** | — | R/A | I |
| **Armazenar e reter evidências** | — | R/A | I |
| **Implementar controles de acesso** | — | R/A | I |
| **Implementar controles de integridade (hash, WORM)** | — | R/A | I |
| **Executar validador no pacote** | C | R/A | C |
| **Empacotar submissão (zip, checksums)** | C | R/A | I |
| **Verificar checksums (sha256)** | — | C | R/A |
| **Verificar estrutura do pacote (validador)** | — | C | R/A |
| **Interpretar requisitos regulatórios** | — | R/A | C |
| **Emitir conclusão de auditoria** | — | — | R/A |
| **Fornecer aconselhamento jurídico** | — | — | — |

**Legenda**: R = Responsável, A = Accountable, C = Consultado, I = Informado, — = Não aplicável

!!! note "Conclusão chave"
    AIMO Standard é responsável por **definir o formato**. Adotantes são responsáveis por **criar, armazenar e validar evidências**. Auditores são responsáveis por **verificar submissões e emitir conclusões de auditoria**.

!!! warning "Aviso de não-certificação"
    AIMO Standard é informativo; não certifica conformidade nem fornece aconselhamento jurídico. Conclusões de auditoria e avaliações de conformidade são responsabilidade exclusiva de auditores e profissionais jurídicos qualificados.

## Declaração de não-sobrereivindicação

!!! warning "Importante"
    O AIMO Standard suporta **explicabilidade e prontidão de evidências**. Ele **não** fornece aconselhamento jurídico, garante conformidade, nem certifica conformidade com qualquer regulamentação ou framework. Adotantes devem verificar reivindicações contra textos autoritativos e obter aconselhamento profissional conforme apropriado.

Esta declaração se aplica a toda documentação do AIMO Standard, incluindo Trust Package, Pacote de Evidências, Requisitos Mínimos de Evidências, Mapa de Cobertura e Releases.

## Páginas relacionadas

- [Trust Package](trust-package.md) — hub de materiais prontos para auditoria
- [Protocolo de Supervisão Humana](human-oversight-protocol.md) — limite de revisão máquina vs. humano
- [Requisitos Mínimos de Evidências](../artifacts/minimum-evidence.md) — checklist de ciclo de vida de nível DEVE
- [Metodologia do Mapa de Cobertura](../coverage-map/methodology.md) — o que o mapeamento é e não é
