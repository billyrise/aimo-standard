---
description: Trust Package AIMO - Pacote de materiais prontos para auditoria. Documentação mínima para auditores, jurídico e segurança de TI avaliarem prontidão de adoção de governança de IA.
---

# Trust Package (Pacote de Garantia)

Esta página agrupa os materiais mínimos que auditores, jurídico e segurança de TI precisam para avaliar prontidão de adoção.
É apenas um hub; TOC de Evidências detalhado e tabelas de Cobertura são mantidos em suas respectivas seções.

## Download

**[Baixar Trust Package PDF (Release Mais Recente)](https://github.com/billyrise/aimo-standard/releases/latest)**

O Trust Package PDF consolida materiais prontos para auditoria em um único documento. Cada Release do GitHub inclui:

- `trust_package.pdf` — Trust Package em Inglês
- `trust_package.ja.pdf` — Trust Package em Japonês
- `aimo-standard-artifacts.zip` — Schemas, templates, exemplos, regras do validador
- `SHA256SUMS.txt` — Checksums para verificação

## O que você recebe

- **Conformidade**: como reivindicar conformidade e o que os níveis significam — [Conformidade](../../conformance/)
- **Mapa de Cobertura**: mapeamento para padrões externos — [Índice Mapa de Cobertura](../../coverage-map/), [Metodologia do Mapa de Cobertura](../../coverage-map/methodology/)
- **Padrão**: requisitos e definições normativas — [Padrão (Atual)](../../standard/current/)
- **Taxonomia**: sistema de classificação de 8 dimensões para governança de IA — [Taxonomia](../../standard/current/03-taxonomy/), [Códigos](../../standard/current/04-codes/), [Dicionário](../../standard/current/05-dictionary/)
- **Pacote de Evidências**: estrutura, TOC, rastreabilidade — [Pacote de Evidências](../../artifacts/evidence-bundle/)
- **Requisitos Mínimos de Evidências**: checklist de nível DEVE por ciclo de vida — [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/)
- **Validador**: regras e verificações de referência — [Validador](../../validator/)
- **Exemplos**: pacotes de amostra prontos para auditoria — [Exemplos](../../examples/)
- **Releases**: histórico de mudanças e distribuição — [Releases](../../releases/)
- **Governança**: políticas, segurança, licenciamento — [Governança](../../governance/)

## Conjunto mínimo para prontidão de auditoria

| Item | Onde encontrar | Resultado / o que prova |
| --- | --- | --- |
| Níveis de conformidade | [Conformidade](../../conformance/) | Como reivindicar conformidade e o escopo de evidências necessárias |
| Mapeamento de cobertura | [Índice Mapa de Cobertura](../../coverage-map/), [Metodologia do Mapa de Cobertura](../../coverage-map/methodology/) | Explicabilidade contra regulamentações e padrões externos |
| Taxonomia e Dicionário | [Taxonomia](../../standard/current/03-taxonomy/), [Códigos](../../standard/current/04-codes/), [Dicionário](../../standard/current/05-dictionary/) | Sistema de classificação para sistemas de IA (8 dimensões, 91 códigos) |
| Artefatos de evidências | [Pacote de Evidências](../../artifacts/evidence-bundle/), [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/), [Template EV](../../standard/current/06-ev-template/) | Quais dados devem existir para suportar rastreabilidade |
| Verificações do validador | [Validador](../../validator/) | Como verificar consistência e completude interna |
| Pacote exemplo | [Exemplos](../../examples/) | Como um pacote pronto para auditoria se parece na prática |
| Controle de mudanças | [Releases](../../releases/), [Governança](../../governance/) | Como atualizações são gerenciadas e comunicadas |
| Segurança / Licença / Marcas | [Governança](../../governance/) | Postura jurídica e de segurança para decisões de adoção |

## Como citar

Use o README do repositório para orientação e contexto de citação; links de governança para as políticas autoritativas.
Veja [README.md](https://github.com/billyrise/aimo-standard/blob/main/README.md) e [Governança](../../governance/).

## Conteúdo do zip de artefatos

O `aimo-standard-artifacts.zip` inclui:

- **Taxonomia (SSOT)**: `source_pack/03_taxonomy/` — CSV do Dicionário (91 códigos), YAML, sistema de códigos
- **JSON Schemas**: `schemas/jsonschema/` — Schemas de validação legíveis por máquina
- **Templates**: `templates/ev/` — Templates de registro de evidências (JSON + Markdown)
- **Exemplos**: `examples/` — Pacotes de amostra mínimos para adoção rápida
- **Mapa de Cobertura**: `coverage_map/coverage_map.yaml` — Mapeamento para padrões externos
- **Regras do Validador**: `validator/rules/` — Definições de regras de validação
- **Docs de governança**: `VERSIONING.md`, `GOVERNANCE.md`, `SECURITY.md`, `LICENSE.txt`, etc.

## Limite de responsabilidade

O AIMO Standard fornece um formato de evidências estruturado e framework de explicabilidade. Ele **não** fornece aconselhamento jurídico, certificação de conformidade, avaliação de riscos ou execução de auditoria.

Para a definição completa de escopo, suposições e responsabilidades do adotante, veja [Limite de Responsabilidade](../responsibility-boundary/).

## Como preparar um pacote de submissão

Siga estes passos para preparar uma submissão pronta para auditoria:

1. **Gerar Pacote de Evidências**: Crie registros EV, Dicionário, Resumo e Log de Alterações conforme [Pacote de Evidências](../../artifacts/evidence-bundle/) e [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/).
2. **Executar Validador**: Execute `python validator/src/validate.py bundle/root.json` para verificar consistência estrutural. Corrija quaisquer erros antes de prosseguir.
3. **Criar Checksums**: Gere checksums SHA-256 para todos os arquivos de submissão:

    === "Linux"

        ```bash
        sha256sum *.json *.pdf > SHA256SUMS.txt
        ```

    === "macOS"

        ```bash
        shasum -a 256 *.json *.pdf > SHA256SUMS.txt
        ```

    === "Windows (PowerShell)"

        ```powershell
        Get-ChildItem *.json, *.pdf | ForEach-Object {
            $hash = (Get-FileHash $_.FullName -Algorithm SHA256).Hash.ToLower()
            "$hash  $($_.Name)"
        } | Out-File SHA256SUMS.txt -Encoding UTF8
        ```
4. **Empacotar Artefatos**: Crie um arquivo zip do seu pacote de evidências:
   ```bash
   zip -r evidence_bundle.zip bundle_directory/
   ```
5. **Referenciar Versão do Release**: Note qual versão do AIMO Standard (ex: `v1.0.0`) seu pacote está alinhado.
6. **Entregar**: Forneça o zip, checksums e referência de versão para seu auditor ou função de conformidade.

Para ativos de release e verificação, veja [Releases](../../releases/).

## Declaração de não-sobrereivindicação

!!! warning "Importante"
    O AIMO Standard suporta **explicabilidade e prontidão de evidências**. Ele **não** fornece aconselhamento jurídico, garante conformidade, nem certifica conformidade com qualquer regulamentação ou framework. Adotantes devem verificar reivindicações contra textos autoritativos e obter aconselhamento profissional conforme apropriado.

Veja [Limite de Responsabilidade](../responsibility-boundary/) para detalhes sobre escopo, suposições e responsabilidades do adotante.

## Para auditores: Procedimento de verificação

Ao receber uma submissão de evidências, auditores devem verificar integridade e estrutura usando os seguintes passos:

!!! success "Proveniência de Build Disponível"
    Todos os ativos de release incluem atestações de proveniência de build assinadas criptograficamente. Veja [Procedimento de Verificação](../../standard/versions/#4-verify-build-provenance-attestation) para passos de verificação de atestação.

### Passo 1: Verificar checksums (SHA-256)

=== "Linux"

    ```bash
    # Baixe ou receba SHA256SUMS.txt com a submissão
    # Verifique que todos os arquivos correspondem aos checksums registrados
    sha256sum -c SHA256SUMS.txt

    # Ou verifique arquivos individuais manualmente:
    sha256sum evidence_bundle.zip
    # Compare saída com o valor em SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # Verifique que todos os arquivos correspondem aos checksums registrados
    shasum -a 256 -c SHA256SUMS.txt

    # Ou verifique arquivos individuais manualmente:
    shasum -a 256 evidence_bundle.zip
    # Compare saída com o valor em SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Verifique arquivos individuais
    Get-FileHash .\evidence_bundle.zip -Algorithm SHA256

    # Compare saída de Hash com SHA256SUMS.txt
    Get-Content .\SHA256SUMS.txt
    ```

Se qualquer checksum falhar, a submissão deve ser rejeitada ou re-solicitada.

### Passo 2: Verificar estrutura do pacote (Validador)

**Pré-requisitos** (configuração única):

```bash
# Clone o release oficial do AIMO Standard
git clone https://github.com/billyrise/aimo-standard.git
cd aimo-standard

# IMPORTANTE: Use a versão exata declarada na submissão
# Substitua VERSION pela versão declarada do submissor (ex: v0.0.1)
VERSION=v0.0.1  # ← Corresponda à versão na submissão
git checkout "$VERSION"

# Configure ambiente Python
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

!!! warning "Correspondência de Versão"
    Sempre use a versão exata do AIMO Standard declarada na submissão. Usar versão diferente pode causar incompatibilidades de validação devido a mudanças de schema ou regras entre versões.

**Execute validação**:

```bash
# Extraia o pacote submetido
unzip evidence_bundle.zip -d bundle/

# Execute validador contra o root.json do pacote
python validator/src/validate.py bundle/root.json

# Saída esperada: "validation OK" ou lista de erros
```

**Exemplo** (usando amostra embutida):

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

O validador verifica:

- Arquivos obrigatórios existem (registros EV, Dicionário)
- Arquivos JSON conformam ao schema
- Referências cruzadas (request_id, review_id, etc.) são válidas
- Timestamps estão presentes e formatados corretamente

### Passo 3: Verificar alinhamento de versão

Verifique que a submissão referencia um release oficial do AIMO Standard:

1. Confirme que a versão declarada (ex: `v0.0.1`) existe em [GitHub Releases](https://github.com/billyrise/aimo-standard/releases)
2. Compare schemas submetidos contra os artefatos do release
3. Note quaisquer desvios do release oficial

### O que procurar

| Verificação | Critério de Aprovação | Ação de Falha |
| --- | --- | --- |
| Checksums correspondem | Todas verificações `sha256sum -c` passam | Rejeitar ou re-solicitar |
| Validador passa | Sem erros de `validate.py` | Solicitar correções antes de aceitar |
| Versão existe | Tag de release existe no GitHub | Esclarecer alinhamento de versão |
| Campos obrigatórios presentes | Registros EV têm id, timestamp, source, summary | Solicitar completude |
| Rastreabilidade intacta | Referências cruzadas resolvem corretamente | Solicitar correções de vinculação |

!!! info "Independência do auditor"
    Auditores devem obter o validador e schemas diretamente do release oficial do AIMO Standard, não da parte submissora, para garantir independência de verificação.

## Jornada de auditoria

A partir desta página, a jornada de auditoria recomendada é:

1. **Sistema de classificação**: [Taxonomia](../../standard/current/03-taxonomy/) + [Dicionário](../../standard/current/05-dictionary/) — entenda o sistema de códigos de 8 dimensões
2. **Estrutura de evidências**: [Pacote de Evidências](../../artifacts/evidence-bundle/) — entenda TOC do pacote e rastreabilidade
3. **Evidências necessárias**: [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/) — checklist de nível DEVE por ciclo de vida
4. **Alinhamento de framework**: [Mapa de Cobertura](../../coverage-map/) + [Metodologia](../../coverage-map/methodology/) — veja como AIMO mapeia para frameworks externos
5. **Validação**: [Validador](../../validator/) — execute verificações de consistência estrutural
6. **Download**: [Releases](../../releases/) — obtenha ativos de release e verifique checksums
