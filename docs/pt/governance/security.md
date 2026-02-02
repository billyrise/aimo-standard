---
description: Política de segurança do AIMO Standard - Relatório de vulnerabilidades, procedimentos de divulgação e considerações de segurança para implementações de governança de IA.
---

# Segurança

Esta página documenta a política de segurança do AIMO Standard, incluindo relatório de vulnerabilidades e procedimentos de divulgação.

## Escopo

### Em Escopo

- Implementação de referência do Validador (`validator/`)
- Ferramentas de build e release (`tooling/`)
- JSON schemas (`schemas/`)
- Infraestrutura do website de documentação

### Fora de Escopo

- Conteúdo da especificação (texto normativo não é artefato de segurança)
- Implementações de adotantes usando AIMO Standard
- Dependências externas (reporte aos mantenedores upstream)

## Versões Suportadas

| Versão | Suportada |
| ------- | --------- |
| latest (dev) | Sim |
| Releases com tag (vX.Y.Z) | Sim (últimas 2 versões minor) |
| Releases mais antigas | Não (upgrade recomendado) |

## Reportando uma Vulnerabilidade

**Não** abra uma issue pública no GitHub para vulnerabilidades de segurança.

### Processo

1. Reporte privadamente via relatório de vulnerabilidade privado do GitHub
2. Inclua: descrição, passos de reprodução, versões afetadas, impacto
3. Permita tempo para avaliação e desenvolvimento de correção

### Cronograma

| Fase | Cronograma |
| ----- | -------- |
| Confirmação | 72 horas |
| Avaliação inicial | 7 dias |
| Divulgação coordenada | 90 dias máx |

## Política de Divulgação

1. Vulnerabilidades são reportadas privadamente
2. Correções são desenvolvidas antes da divulgação pública
3. Avisos de segurança são publicados após correções estarem disponíveis
4. Reportantes são creditados (a menos que anonimato seja solicitado)

## Medidas de Segurança

- Verificações de CI/CD em todas as alterações
- Releases assinados com checksums SHA-256
- Revisão de PR obrigatória antes de merge

## Política Completa

Veja [SECURITY.md](https://github.com/billyrise/aimo-standard/blob/main/SECURITY.md) para a política de segurança completa.

## Páginas Relacionadas

- [Trust Package](trust-package.md) — Materiais prontos para auditoria
- [Governança](index.md) — Governança do projeto
