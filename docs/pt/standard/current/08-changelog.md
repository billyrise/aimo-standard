---
description: Changelog e política de versionamento do AIMO Standard. Documenta histórico de versões, regras de semantic versioning e orientação de migração entre releases.
---

# Changelog

Esta seção documenta a política de versionamento e histórico de mudanças do AIMO Standard.

## Política de Versionamento

AIMO Standard segue [Semantic Versioning](https://semver.org/) (SemVer):

### Formato de Versão: MAJOR.MINOR.PATCH

| Tipo de Mudança | Bump de Versão | Exemplos |
| --- | --- | --- |
| **MAJOR** | X.0.0 | Breaking changes de schema, remoção de código, mudanças de campos obrigatórios |
| **MINOR** | 0.X.0 | Novos códigos, novos campos opcionais, novas dimensões (opcionais) |
| **PATCH** | 0.0.X | Correções de documentação, esclarecimentos de definição, correções de bug do validador |

### Mudanças Breaking vs. Compatíveis

**Breaking Changes (MAJOR):**

- Remoção de códigos (após período de depreciação)
- Mudanças em campos obrigatórios em schemas
- Mudanças estruturais que invalidam documentos existentes
- Mudanças em padrões de formato de código

**Mudanças Backward Compatible (MINOR):**

- Adicionar novos códigos a dimensões existentes
- Adicionar novos campos opcionais a schemas
- Adicionar novas dimensões opcionais
- Adicionar novos templates de evidência

**Mudanças Non-breaking (PATCH):**

- Correções de documentação
- Esclarecimento de definições existentes
- Melhorias de tradução
- Correções de bug do validador

## Política de Depreciação

### Processo de Depreciação

1. **Marcar como Deprecated**: Código ou funcionalidade é marcado com `status: deprecated` e `deprecated_in: X.Y.Z`
2. **Período de Depreciação**: Pelo menos uma versão MINOR deve passar antes da remoção
3. **Fornecer Substituição**: Se aplicável, `replaced_by` indica a substituição
4. **Remover em MAJOR**: Remoção ocorre na próxima versão MAJOR

### Exemplo de Ciclo de Vida

```
v0.0.1: FS-007 introduzido (status: active)
v0.1.0: FS-007 deprecated (status: deprecated, replaced_by: FS-008)
v0.2.0: FS-007 ainda disponível com aviso de depreciação
v1.0.0: FS-007 removido (status: removed)
```

### Usando Códigos Deprecated

- Códigos deprecated permanecem válidos para validação
- Validador DEVERIA emitir aviso para códigos deprecated
- Novas implementações DEVERIAM usar códigos de substituição
- Documentos existentes PODEM continuar usando códigos deprecated até migração

## Artefatos de Release

Cada release oficial inclui:

| Artefato | Descrição |
| --- | --- |
| Snapshot do site versionado | `https://standard.aimoaas.com/0.0.1/` |
| Especificação PDF | `trust_package.pdf` |
| Pacote de ativos (ZIP) | Schemas, templates, dicionário |
| Checksums | Hashes SHA-256 para integridade |
| Changelog | Este documento |

## Histórico de Mudanças

### Não publicado (correções de namespace e normativa)

**Resumo:** Resolução da colisão de códigos EV, clarificação EV (índice) vs Evidence Pack (payload), endurecimento de /dev contra citação errônea em auditoria. Tipos de documento Evidence Pack: EP-01..EP-07; Taxonomy EV permanece para tipos de evento. Relação normativa EV↔Evidence Pack documentada. Banner e canonical para /dev.

### Versão 0.0.1 (2026-02-02)

**Resumo:** Release inicial do AIMO Standard com sistema de códigos de 8 dimensões, templates de Evidence Pack e documentação abrangente de governança.

#### Adicionado

**Sistema de Códigos (8 Dimensões)**

| Dimensão | Códigos Adicionados | Descrição |
| --- | --- | --- |
| FS | FS-001 a FS-006 | Escopo Funcional |
| UC | UC-001 a UC-010 | Classe de Caso de Uso |
| DT | DT-001 a DT-008 | Tipo de Dados |
| CH | CH-001 a CH-006 | Canal |
| IM | IM-001 a IM-005 | Modo de Integração |
| RS | RS-001 a RS-005 | Superfície de Risco |
| OB | OB-001 a OB-005 | Resultado / Benefício |
| LG | LG-001 a LG-015 | Tipo de Log/Registro |

**Schemas**

- `taxonomy_pack.schema.json`: Definição de pacote de taxonomia
- `changelog.schema.json`: Entradas de changelog
- `evidence_pack_manifest.schema.json`: Manifestos de Evidence Pack
- `shadow-ai-discovery.schema.json`: Evidência de descoberta de Shadow AI
- `agent-activity.schema.json`: Evidência de atividade de agente

**Templates de Evidence Pack (MVP)**

- EV-01: Visão Geral do Sistema
- EV-02: Fluxo de Dados
- EV-03: Inventário de IA
- EV-04: Avaliação de Risco e Impacto
- EV-05: Controles e Aprovações
- EV-06: Logging e Monitoramento
- EV-07: Tratamento de Incidentes e Exceções

**Documentação**

- Documentação de taxonomia com definições de 8 dimensões
- Especificação de formato do Sistema de Códigos
- Especificação de formato de CSV do Dicionário
- Política de versionamento e mudança
- Requisitos MVP do validador
- Protocolo de Supervisão Humana
- Mapa de Cobertura (ISO 42001, NIST AI RMF, EU AI Act, ISMS)
- Trust Package

#### Compatibilidade Retroativa

Este é o release inicial; sem preocupações de compatibilidade retroativa.

---

## Changelog Legível por Máquina

Um changelog legível por máquina está disponível:

- `changelog/changelog.json`

Este arquivo segue o schema `changelog.schema.json` e pode ser parseado programaticamente.

## Referências

- [Taxonomia](../03-taxonomy/) - Definições de dimensão
- [Dicionário](../05-dictionary/) - Dicionário de códigos
- [Política de Versionamento](../../../governance/) - Política de versionamento (veja VERSIONING.md na raiz do repositório)
