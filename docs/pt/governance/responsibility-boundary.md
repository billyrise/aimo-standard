---
description: Limite de responsabilidade AIMO — Define o que a norma fornece vs. responsabilidades do adotante. Declaração de não sobreafirmação e limites de âmbito.
---
<!-- aimo:translation_status=translated -->

# Limite de responsabilidade（Responsibility Boundary）

Esta página define o que o AIMO Standard fornece e não fornece, as premissas que assume e as responsabilidades dos adotantes.

## Limite prova vs. asseguração (Proof vs assurance boundary)

| Limite | O que a AIMO oferece | Quem decide |
| --- | --- | --- |
| **Prova (evidência)** | Estrutura do Evidence Bundle, validadores, esquemas, modelos, mapeamentos de cobertura (informativos). A AIMO produz **pacotes de evidência** e **validadores** que verificam conformidade estrutural. | O adoptante produz a evidência; a AIMO define o formato e as regras. |
| **Asseguração / conformidade / certificação** | A AIMO **não** emite certificações, opiniões de asseguração nem decisões de conformidade. | **Externo:** o cliente, o auditor ou o **organismo de certificação acreditado** decide conformidade e certificação. |

A conformidade e a linguagem de declaração estão unificadas em [Conformidade](../../conformance/) e no [Kit de prontidão para certificação ISO 42001](../../artifacts/iso-42001-certification-readiness-toolkit/). A AIMO apoia a **preparação de evidência** e a **transferência para auditoria**; não certifica nem garante conformidade.

## O que o AIMO Standard fornece

- **Um formato de evidência estruturado**: esquemas, modelos e taxonomia para evidência de governação de IA.
- **Enquadramento de rastreabilidade**: ligação de evidência por ciclo de vida (pedido → revisão → exceção → renovação).
- **Suporte à explicabilidade**: mapeamento de cobertura para quadros externos para discussões de auditoria.
- **Ferramentas de validação**: validador de referência e regras para verificações de consistência estrutural.
- **Documentação**: especificação normativa, exemplos e orientação.

## O que o AIMO Standard NÃO fornece

| Fora do âmbito | Explicação |
| --- | --- |
| **Aconselhamento jurídico** | O AIMO não interpreta leis ou regulamentos. Consulte aconselhamento jurídico qualificado para conformidade regulamentar. |
| **Certificação de conformidade** | Usar o AIMO não certifica conformidade com qualquer regulamento ou quadro (ISO 42001, EU AI Act, NIST AI RMF, etc.). |
| **"Certificado ISO pelo AIMO"** | O AIMO não emite certificações. A certificação é realizada por organismos de certificação acreditados. |
| **"Conformidade EU AI Act devido ao AIMO"** | O AIMO estrutura evidência; não garante nem certifica conformidade regulamentar. |
| **Avaliação de riscos** | O AIMO estrutura evidência mas não realiza nem valida avaliações de risco de IA. |
| **Controlos técnicos** | O AIMO não implementa controlo de acesso, encriptação ou outros controlos de segurança; documenta expectativas. |
| **Execução de auditoria** | O AIMO fornece materiais a auditores mas não realiza auditorias. |
| **Avaliação de modelos de IA** | O AIMO não avalia desempenho, viés ou segurança de modelos. |

## Premissas

O AIMO Standard assume:

1. **Os adotantes têm processos de governação**: existem fluxos de pedido, revisão, aprovação e exceção.
2. **Os adotantes mantêm evidência**: a evidência é criada, armazenada e retida pelos sistemas do adotante.
3. **Os adotantes verificam face a textos autoritativos**: ao usar o Coverage Map, os adotantes verificam o quadro ou regulamento original.
4. **As ferramentas são opcionais**: o validador de referência é uma conveniência; os adotantes podem usar a sua própria validação.

## Responsabilidades do adotante

| Responsabilidade | Descrição |
| --- | --- |
| **Criação de evidência** | Gerar registos de evidência precisos e atempados alinhados com o esquema EV. |
| **Armazenamento e retenção de evidência** | Armazenar evidência de forma segura com controlos de acesso e períodos de retenção adequados. |
| **Integridade e controlo de acesso** | Implementar controlos (hashing, WORM, registos de auditoria) para preservar a integridade da evidência. |
| **Verificação jurídica** | Verificar alegações de conformidade face a textos legais autoritativos e obter aconselhamento jurídico conforme necessário. |
| **Alinhamento contínuo** | Atualizar evidência e mapeamentos à medida que as versões do AIMO Standard e quadros externos evoluem. |
| **Preparação para auditoria** | Empacotar Evidence Bundles e executar validação antes da submissão aos auditores. |

## Matriz RACI

A seguinte matriz RACI esclarece responsabilidades entre AIMO Standard, Adotante e Auditor.

| Atividade | AIMO Standard | Adotante | Auditor |
| --- | :---: | :---: | :---: |
| **Definir esquema e modelos de evidência** | R/A | I | I |
| **Criar registos de evidência** | — | R/A | I |
| **Armazenar e reter evidência** | — | R/A | I |
| **Implementar controlos de acesso** | — | R/A | I |
| **Implementar controlos de integridade (hash, WORM)** | — | R/A | I |
| **Executar validador no bundle** | C | R/A | C |
| **Empacotar submissão (zip, checksums)** | C | R/A | I |
| **Verificar checksums (sha256)** | — | C | R/A |
| **Verificar estrutura do bundle (validador)** | — | C | R/A |
| **Interpretar requisitos regulamentares** | — | R/A | C |
| **Emitir conclusão de auditoria** | — | — | R/A |
| **Prestar aconselhamento jurídico** | — | — | — |

**Legenda**: R = Responsável, A = Accountable, C = Consultado, I = Informado, — = Não aplicável

!!! note "Conclusão chave"
    O AIMO Standard é responsável por **definir o formato**. Os adotantes são responsáveis por **criar, armazenar e validar evidência**. Os auditores são responsáveis por **verificar submissões e emitir conclusões de auditoria**.

!!! warning "Aviso de não certificação"
    O AIMO Standard é informativo; não certifica conformidade nem presta aconselhamento jurídico. Conclusões de auditoria e avaliações de conformidade são da exclusiva responsabilidade de auditores e profissionais jurídicos qualificados.

## Política de alegações

| Aceitável | Inaceitável |
| --- | --- |
| "Um Evidence Bundle foi produzido de acordo com o AIMO Standard v0.1.2 e validado estruturalmente pelo AIMO Validator." | "Conformidade EU AI Act", "certificado ISO 42001", "aprovado pelo governo", etc. |
| "Usamos artefactos AIMO para apoiar a preparação ISO/IEC 42001; as decisões de certificação cabem aos organismos de certificação acreditados." | Alegar que o AIMO certifica conformidade ou presta aconselhamento jurídico. |

## Declaração de não sobreafirmação

!!! warning "Importante"
    O AIMO Standard apoia **explicabilidade e preparação de evidência**. **Não** presta aconselhamento jurídico, **não** garante conformidade nem **não** certifica conformidade com qualquer regulamento ou quadro. Os adotantes devem verificar alegações face a textos autoritativos e obter aconselhamento profissional conforme apropriado.

Esta declaração aplica-se a toda a documentação do AIMO Standard, incluindo Trust Package, Evidence Bundle, Minimum Evidence Requirements, Coverage Map e Releases.

## Páginas relacionadas

- [Trust Package](../trust-package/) — centro de materiais prontos para auditoria
- [Human Oversight Protocol](../human-oversight-protocol/) — fronteira revisão máquina vs. humana
- [Minimum Evidence Requirements](../../artifacts/minimum-evidence/) — checklist MUST por ciclo de vida
- [Coverage Map Methodology](../../coverage-map/methodology/) — o que é e o que não é o mapeamento
