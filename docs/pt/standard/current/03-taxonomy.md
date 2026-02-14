---
description: Taxonomia AIMO - Sistema de classificação de 8 dimensões com 91 códigos para categorizar sistemas de IA. Cobre escopo funcional, casos de uso, tipos de dados, canais, integração, riscos, resultados e evidências.
---

# Taxonomia

A Taxonomia AIMO fornece um sistema de classificação estruturado para categorizar sistemas de IA, seus usos e requisitos de governança associados. Consiste em **8 dimensões** com **91 códigos** que permitem classificação consistente e gestão de evidências entre organizações.

## Propósito

A taxonomia serve três propósitos primários do ponto de vista de auditoria:

1. **Explicabilidade**: Fornece um vocabulário comum para descrever casos de uso de IA em toda a organização, suportando comunicação clara com auditores e stakeholders.

2. **Prontidão de Evidências**: Permite documentação sistemática de sistemas de IA usando uma classificação padronizada, tornando coleta e revisão de evidências mais eficientes.

3. **Comparabilidade**: Permite que organizações comparem casos de uso de IA em diferentes contextos usando terminologia consistente.

## O que Não É (Não-Sobrereivindicação)

!!! warning "Importante"
    O AIMO Standard suporta **explicabilidade e prontidão de evidências**. Ele **não** fornece aconselhamento jurídico, garante conformidade, nem certifica conformidade com qualquer regulamentação ou framework. Veja [Limite de Responsabilidade](../../governance/responsibility-boundary.md) para detalhes.

A taxonomia é apenas um sistema de classificação. Ela não:

- Garante conformidade com qualquer lei ou regulamentação
- Substitui aconselhamento jurídico, de segurança ou conformidade profissional
- Certifica conformidade com frameworks externos (ISO, NIST, EU AI Act, etc.)
- Fornece avaliações de risco ou recomendações de controle

## Exemplos de riscos específicos de IA/agênticos (por que um padrão específico de IA é necessário)

Controles de segurança tradicionais (ex: ISMS) sozinhos frequentemente falham em capturar modos de falha específicos de LLM/agente e desvios de agentes autônomos (ex: execução de ferramenta não intencional, loops recursivos) de maneira **explicável para auditoria**.
A Taxonomia AIMO fornece uma linguagem compartilhada para classificar esses riscos específicos de IA e conectá-los a requisitos de evidências e fluxos de trabalho de remediação.

!!! warning "Apenas exemplos de referência — não são códigos normativos"
    Os códigos abaixo são **placeholders ilustrativos** e **não** fazem parte do sistema de códigos normativo AIMO. Não os use em submissões; use as dimensões e códigos normativos em [Codes](./04-codes.md) e [Dictionary](./05-dictionary.md).

- **AG-01** Loop/Recursão Descontrolada
- **AG-02** Uso Não Autorizado de Ferramenta (uso indevido estilo confused deputy)
- **AG-03** Drift de Limite de Privilégio

Não use AG-* em submissões; use as dimensões e códigos normativos definidos em Codes/Dictionary.

## Visão Geral das Dimensões

AIMO usa 8 dimensões para classificar casos de uso de IA. Cada dimensão tem um prefixo único de 2 letras.

| ID | Nome | Contagem de Códigos | Descrição |
| --- | --- | --- | --- |
| **FS** | Escopo Funcional | 6 | Qual função de negócio é suportada |
| **UC** | Classe de Caso de Uso | 30 | Que tipo de tarefa é realizada |
| **DT** | Tipo de Dados | 10 | Quais classificações de dados estão envolvidas |
| **CH** | Canal | 8 | Como usuários acessam a IA |
| **IM** | Modo de Integração | 7 | Como IA conecta a sistemas empresariais |
| **RS** | Superfície de Risco | 8 | Quais riscos estão associados |
| **OB** | Resultado / Benefício | 7 | Quais benefícios são esperados |
| **LG** | Tipo de Log/Registro | 15 | Quais logs/registros são necessários |

**Total: 91 códigos em 8 dimensões**（**EV-** reservado para IDs de artefato Evidence; dimensão de log/registro da taxonomia usa **LG-**.)

### Regras de Uso

| Dimensão | Seleção | Implicação para Auditoria |
| --- | --- | --- |
| FS, IM | Exatamente 1 | Classificação primária para atribuição de responsabilidade |
| UC, DT, CH, RS, LG | 1 ou mais | Enumeração completa necessária para cobertura de risco |
| OB | 0 ou mais | Opcional; documenta valor de negócio esperado |

## Definições de Dimensão

### FS: Escopo Funcional

Categoriza uso de IA pela função de negócio que suporta. **Selecione exatamente um.**

| Código | Rótulo | Definição |
| --- | --- | --- |
| FS-001 | Produtividade do Usuário Final | IA usada para melhorar produtividade de usuários finais internos (escrita, busca, sumarização, notas de reunião). |
| FS-002 | Funcionalidades Voltadas ao Cliente | IA incorporada em funcionalidades de produto/serviço fornecidas aos clientes. |
| FS-003 | Ferramentas de Desenvolvedor | IA usada para auxiliar desenvolvimento de software e tarefas de engenharia. |
| FS-004 | Operações de TI | IA usada para operações de TI e administração de sistemas (monitoramento, tratamento de incidentes). |
| FS-005 | Operações de Segurança | IA usada para monitoramento/resposta de segurança (SOC, detecção, triagem). |
| FS-006 | Governança e Conformidade | IA usada para suportar atividades de governança/conformidade (política, evidência de auditoria). |

### UC: Classe de Caso de Uso

Categoriza uso de IA pelo tipo de tarefa ou interação. **Selecione um ou mais.** Lista completa inclui 30 códigos; exemplos representativos abaixo.

| Código | Rótulo | Definição |
| --- | --- | --- |
| UC-001 | Q&A Geral | Resposta a perguntas gerais e uso conversacional. |
| UC-002 | Sumarização | Sumarizar documentos, reuniões ou mensagens. |
| UC-003 | Tradução | Tradução entre idiomas. |
| UC-004 | Rascunho de Conteúdo | Gerar rascunhos para emails, documentos ou relatórios. |
| UC-005 | Geração de Código | Gerar código ou scripts. |
| UC-006 | Revisão de Código | Revisar código para problemas e melhorias. |
| UC-009 | Busca/RAG | Recuperação e resposta a perguntas baseada em RAG. |
| UC-010 | Automação Agêntica | Agentes autônomos ou semi-autônomos executando ações. |

Veja [Dicionário](./05-dictionary.md) para a lista completa de 30 códigos UC.

### DT: Tipo de Dados

Categoriza a sensibilidade e classificação dos dados envolvidos. **Selecione um ou mais.**

| Código | Rótulo | Definição |
| --- | --- | --- |
| DT-001 | Público | Dados publicamente disponíveis e destinados a divulgação pública. |
| DT-002 | Interno | Dados de negócio internos não públicos. |
| DT-003 | Confidencial | Dados internos altamente sensíveis requerendo acesso restrito. |
| DT-004 | Dados Pessoais | Dados pessoais conforme definido por leis de privacidade aplicáveis. |
| DT-005 | Dados Pessoais Sensíveis | Dados pessoais de categoria especial/sensível. |
| DT-006 | Credenciais | Segredos de autenticação e credenciais. |
| DT-007 | Código Fonte | Código fonte e artefatos relacionados. |
| DT-008 | Dados de Cliente | Dados fornecidos pelo cliente ou relacionados ao cliente. |
| DT-009 | Logs Operacionais | Logs operacionais ou de sistema usados para monitoramento e troubleshooting. |
| DT-010 | Telemetria de Segurança | Telemetria de segurança como alertas e detecções. |

### CH: Canal

Categoriza como usuários acessam ou interagem com a IA. **Selecione um ou mais.**

| Código | Rótulo | Definição |
| --- | --- | --- |
| CH-001 | UI Web | Uso via interface de usuário web. |
| CH-002 | API | Uso via integração de API programática. |
| CH-003 | Plugin de IDE | Uso via plugin de IDE/editor. |
| CH-004 | ChatOps | Uso via integrações de plataformas de chat (Slack/Teams). |
| CH-005 | App Desktop | Uso via aplicação desktop nativa. |
| CH-006 | App Mobile | Uso via aplicação mobile nativa. |
| CH-007 | Email | Uso via interface de email ou automação baseada em email. |
| CH-008 | Linha de Comando | Uso via interface de linha de comando. |

### IM: Modo de Integração

Categoriza como IA é integrada em sistemas empresariais. **Selecione exatamente um.**

| Código | Rótulo | Definição |
| --- | --- | --- |
| IM-001 | Standalone | Usado standalone sem integração em sistemas empresariais. |
| IM-002 | SaaS Integrado | Aplicação SaaS integra funcionalidades de IA. |
| IM-003 | Incorporado em App Empresarial | IA incorporada em aplicações empresariais internas. |
| IM-004 | RPA/Workflow | IA invocada dentro de automação de workflow ou RPA. |
| IM-005 | On-prem / Privado | IA hospedada em ambiente privado/on-prem. |
| IM-006 | Serviço Gerenciado | Uso via serviço gerenciado com controles empresariais. |
| IM-007 | Shadow / Não Gerenciado | Uso fora de controles de governança aprovados. |

### RS: Superfície de Risco

Categoriza os tipos de riscos associados ao uso de IA. **Selecione um ou mais.**

| Código | Rótulo | Definição |
| --- | --- | --- |
| RS-001 | Vazamento de Dados | Risco de divulgação não intencional de dados. |
| RS-002 | Abuso de Segurança | Risco de que o sistema seja abusado para propósitos maliciosos. |
| RS-003 | Violação de Conformidade | Risco de violar leis/regulamentações/políticas. |
| RS-004 | Violação de PI | Risco de infringir direitos autorais/patentes/segredos comerciais. |
| RS-005 | Uso Indevido de Modelo | Risco de uso inapropriado de modelo ou dependência excessiva. |
| RS-006 | Viés/Justiça | Risco de resultados injustos ou enviesados. |
| RS-007 | Segurança | Risco de conteúdo prejudicial ou recomendações inseguras. |
| RS-008 | Risco de Terceiros | Riscos de fornecedores, sub-processadores e provedores de modelo. |

### OB: Resultado / Benefício

Categoriza os resultados ou benefícios esperados do uso de IA. **Opcional; selecione zero ou mais.**

| Código | Rótulo | Definição |
| --- | --- | --- |
| OB-001 | Eficiência | Melhora eficiência de tempo/custo. |
| OB-002 | Qualidade | Melhora qualidade/precisão de outputs. |
| OB-003 | Receita | Contribui para crescimento de receita. |
| OB-004 | Redução de Risco | Reduz risco operacional/segurança/conformidade. |
| OB-005 | Inovação | Permite novas capacidades ou inovações. |
| OB-006 | Satisfação do Cliente | Melhora satisfação do cliente. |
| OB-007 | Experiência do Funcionário | Melhora experiência do funcionário. |

### LG: Tipo de Log/Registro

Categoriza os tipos de log/registro necessários ou coletados. **Selecione um ou mais.**（EV- reservado para IDs de artefato Evidence.)

| Código | Rótulo | Definição |
| --- | --- | --- |
| LG-001 | Registro de Solicitação | Evidência de que um uso/serviço de IA foi solicitado e descrito. |
| LG-002 | Registro de Revisão/Aprovação | Evidência de que uma revisão/aprovação foi realizada. |
| LG-003 | Registro de Exceção | Evidência de que uma exceção foi concedida e rastreada. |
| LG-004 | Registro de Renovação/Reavaliação | Evidência de que renovação ou reavaliação ocorreu. |
| LG-005 | Entrada de Log de Alterações | Evidência de alterações e suas aprovações. |
| LG-006 | Prova de Integridade | Evidência de integridade (hash, assinatura, WORM). |
| LG-007 | Log de Acesso | Evidência de controle de acesso e histórico de acesso. |
| LG-008 | Inventário de Modelo/Serviço | Registro de inventário de modelos/serviços usados. |
| LG-009 | Avaliação de Risco | Avaliação de risco documentada para o uso/serviço. |
| LG-010 | Mapeamento de Controles | Evidência de mapeamento de controles para frameworks externos. |
| LG-011 | Treinamento/Orientação | Evidência de treinamento ou orientação fornecida aos usuários. |
| LG-012 | Evidência de Monitoramento | Evidência de monitoramento e supervisão contínua. |
| LG-013 | Registro de Incidente | Evidência de tratamento de incidentes relacionados ao uso de IA. |
| LG-014 | Avaliação de Terceiros | Evidência de avaliação de fornecedor ou terceiros. |
| LG-015 | Atestação/Sign-off | Registro formal de atestação ou sign-off. |

## Como Usar

### Relação com Evidências

Cada documento de evidências referencia códigos de múltiplas dimensões para classificar o sistema ou caso de uso de IA sendo documentado. A classificação de 8 dimensões permite:

- **Categorização consistente** em toda a organização
- **Filtragem baseada em risco** por valores de dimensão
- **Mapeamento de framework** via Mapa de Cobertura

### Referenciando o Dicionário

Para definições completas de códigos incluindo notas de escopo e exemplos, consulte o [Dicionário](./05-dictionary.md).

### Exemplo de Classificação

```
FS: FS-001 (Produtividade do Usuário Final)
UC: UC-001 (Q&A Geral), UC-002 (Sumarização)
DT: DT-002 (Interno), DT-004 (Dados Pessoais)
CH: CH-001 (UI Web)
IM: IM-002 (SaaS Integrado)
RS: RS-001 (Vazamento de Dados), RS-003 (Violação de Conformidade)
OB: OB-001 (Eficiência)
LG: LG-001 (Registro de Solicitação), LG-002 (Registro de Revisão/Aprovação)
```

## Referência SSOT

!!! info "Fonte de Verdade"
    A definição autoritativa é `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv`. Esta página é explicativa. Veja [Guia de Localização](../../contributing/localization.md) para fluxos de trabalho de atualização.

## Páginas Relacionadas

- [Códigos](./04-codes.md) - Formato de código, convenções de nomenclatura e ciclo de vida
- [Dicionário](./05-dictionary.md) - Listagens completas de códigos e definições de colunas
- [Templates de Evidências](./06-ev-template.md) - Como usar códigos em evidências
- [Limite de Responsabilidade](../../governance/responsibility-boundary.md) - Declaração de não-sobrereivindicação
