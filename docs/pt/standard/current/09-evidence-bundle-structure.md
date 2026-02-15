---
description: Estrutura raiz normativa e manifest do Pacote de Evidências (v0.1). Integrity MUST; Custody é definido pela implementação.
---
<!-- aimo:translation_status=translated -->

# Estrutura raiz do Pacote de Evidências (v0.1)

Esta página define o **layout raiz normativo** e o manifest de um Pacote de Evidências. Os validadores DEVEM rejeitar pacotes que não satisfaçam estes requisitos antes de qualquer validação de esquema.

## MUST normativo v0.1 (resumo)

- **manifest.json** na raiz do pacote é obrigatório.
- **object_index** e **payload_index**: cada entrada DEVE incluir **sha256** (64 hex em minúsculas); os caminhos DEVEM ser relativos e NÃO DEVEM conter `../` nem escapar da raiz do pacote.
- **signing.signatures** DEVE ser um array não vazio (array vazio inválido).
- Cada entrada de assinatura DEVE ter: **path** sob `signatures/` (varredura de caminho proibida), **targets** (array, pelo menos um caminho), e pelo menos uma assinatura no pacote DEVE listar **manifest.json** em **targets** (assinatura do manifest obrigatória).
- **hash_chain**: v0.1 DEVE incluir **algorithm**, **head**, **path** (sob `hashes/`) e **covers** com pelo menos **manifest.json** e **objects/index.json**.

Os validadores DEVEM aplicar estas regras antes de aceitar um pacote.

## Estrutura raiz necessária (MUST)

Na raiz do pacote DEVEM estar presentes: **manifest.json**, **objects/**, **payloads/**, **signatures/**, **hashes/** (descritos na norma). Os implementadores NÃO DEVEM submeter um pacote que omita qualquer um destes. O Validador DEVE falhar com mensagem clara quando a estrutura raiz estiver incompleta.

## Integrity (normativo) vs. Custody (implementação)

- **Integrity** é **normativo** em v0.1: a norma exige que o pacote transporte metadados de integridade (manifest, sha256 dos ficheiros indexados, presença de assinatura do manifest). Os validadores DEVEM verificar a existência e validade do manifest, a existência e correspondência sha256 dos ficheiros indexados e a presença de pelo menos uma assinatura que tenha como alvo o manifest.
- **Custody** (armazenamento, controlo de acesso, retenção, WORM) é **definido pela implementação**.

## manifest.json (campos MUST)

O manifest DEVE incluir pelo menos: **bundle_id** (UUID), **bundle_version** (SemVer), **created_at** (date-time), **scope_ref** (padrão SC-*), **object_index**, **payload_index**, **hash_chain**, **signing**. Regras de caminho: relativos, sem `../`, sem `/` inicial, dentro da raiz do Pacote de Evidências.

**Metadados de assinatura opcionais v0.1.1 (RECOMMENDED para reexecução por terceiros):** signer_identity, signed_at, verification_command, canonicalization.

## Extensões futuras (informativo)

- **Ligação Control/Requirement**: Uma versão futura pode adicionar uma forma padrão de ligar elementos do Pacote de Evidências a identificadores Control ou Requirement (ex.: para exportar para NIST OSCAL).

## Referências

- [Pacote de Evidências (resumo do artefacto)](../../../artifacts/evidence-bundle/) — objetivo e índice
- [Modelo EV — Formulários externos e índice de transferência de auditoria](../06-ev-template/#external-forms-official-templateschecklists-attached-as-is)
- [Roadmap de verificação de assinaturas](../../../artifacts/signature-verification-roadmap/) — metadados v0.1.1 e plano de verificação v0.2
- [Validador](../../../validator/) — como o validador aplica esta estrutura
- [Requisitos Mínimos de Evidências](../../../artifacts/minimum-evidence/) — lista de verificação MUST
