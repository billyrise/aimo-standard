---
description: Releases do AIMO Standard - Baixe PDFs versionados, artefatos e checksums. Changelog, guias de migração e atestações de proveniência de build.
---

# Releases

Esta seção é um hub para releases versionados, changelog, migração e artefatos de distribuição.

## Baixar Release Mais Recente

**[GitHub Releases](https://github.com/billyrise/aimo-standard/releases/latest)** — é a fonte única de verdade do release "latest". O caminho do site `/latest/` redireciona para a mesma versão.

## Procedimento de verificação (página permanente)

O **procedimento de verificação** completo (download de ativos, verificação de checksums, attestação de proveniência) está disponível como página permanente, não apenas em PDF:

- **[Standard → Versões → Procedimento de Verificação](../standard/versions/index.md)** — verificação passo a passo de checksums (Linux/macOS/Windows) e attestação de proveniência.

Use esta página quando precisar verificar ativos de release ou documentar os passos de verificação em entregas de auditoria.

## Ativos de Release

Cada release oficial (tag `vX.Y.Z`) inclui:

| Ativo | Descrição |
| --- | --- |
| `trust_package.pdf` | Trust Package em Inglês — materiais de garantia prontos para auditoria |
| `trust_package.ja.pdf` | Trust Package em Japonês |
| `aimo-standard-artifacts.zip` | Schemas, templates, exemplos, regras do validador |
| `SHA256SUMS.txt` | Checksums SHA-256 para todos os ativos |

### Verificando Downloads

Após baixar, verifique integridade dos arquivos usando checksums:

=== "Linux"

    ```bash
    # Baixe o arquivo de checksums
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # Verifique um arquivo específico
    sha256sum -c SHA256SUMS.txt --ignore-missing

    # Ou verifique manualmente:
    sha256sum trust_package.pdf
    # Compare saída com SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # Baixe o arquivo de checksums
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # Verifique um arquivo específico
    shasum -a 256 -c SHA256SUMS.txt

    # Ou verifique manualmente:
    shasum -a 256 trust_package.pdf
    # Compare saída com SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Baixe o arquivo de checksums
    Invoke-WebRequest -Uri "https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt" -OutFile SHA256SUMS.txt

    # Verifique um arquivo específico
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # Compare saída de Hash com SHA256SUMS.txt
    Get-Content .\SHA256SUMS.txt
    ```

## Conteúdo do Zip de Artefatos

O `aimo-standard-artifacts.zip` contém:

- `schemas/jsonschema/*` — JSON Schemas para validação
- `templates/ev/*` — Templates de evidências (JSON + Markdown)
- `examples/*` — Pacotes de evidências de amostra
- `coverage_map/coverage_map.yaml` — Mapeamento para padrões externos
- `validator/rules/*` — Definições de regras de validação
- `VERSIONING.md`, `GOVERNANCE.md`, `SECURITY.md`, etc.

## Recursos

- **Tabela de Histórico de Versões**: [Padrão > Versões](../standard/versions/index.md) — tabela de versões com links diretos para todos os ativos de release (PDF, ZIP, SHA256)
- **Changelog (spec)**: [Padrão > Atual > Changelog](../standard/current/08-changelog.md) — histórico de mudanças normativas e não-normativas.
- **Processo de release**: tagging `vX.Y.Z`, build CI, PDF sob `dist/`, checksums, ativos de GitHub Release. Veja [GOVERNANCE.md](https://github.com/billyrise/aimo-standard/blob/main/GOVERNANCE.md) e [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) no repositório.
- **Guia de migração**: [MIGRATION.md](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) — caminhos de upgrade para breaking changes.

Para governança e política de versionamento, veja [Governança](../governance/index.md).

## Preparando seu pacote de submissão

Ao preparar evidências para submissão de auditoria:

1. **Crie seu Pacote de Evidências**: Siga [Pacote de Evidências](../artifacts/evidence-bundle.md) e [Requisitos Mínimos de Evidências](../artifacts/minimum-evidence.md) para criar registros EV, Dicionário, Resumo e Log de Alterações.
2. **Execute o Validador**: Execute `python validator/src/validate.py bundle/root.json` para verificar consistência estrutural. Corrija todos os erros antes de prosseguir.
3. **Gere Checksums**: Crie checksums SHA-256 para verificação:

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
4. **Empacote**: Crie um arquivo zip do diretório do seu pacote.
5. **Documente alinhamento de versão**: Note qual release do AIMO Standard (ex: `v1.0.0`) suas evidências estão alinhadas.
6. **Entregue**: Forneça o pacote, checksums e referência de versão para seu auditor.

Para o guia de preparação completo, veja [Trust Package](../governance/trust-package.md).

## Para auditores: Procedimento de verificação

Auditores recebendo submissões de evidências devem verificar integridade e estrutura:

1. **Verifique checksums**: Execute verificação de checksum (Linux: `sha256sum -c`, macOS: `shasum -a 256 -c`, Windows: `Get-FileHash`) para confirmar integridade do arquivo
2. **Execute validador**: Execute `python validator/src/validate.py bundle/root.json` para verificar estrutura
3. **Confirme versão**: Verifique que a versão do AIMO Standard declarada existe em [GitHub Releases](https://github.com/billyrise/aimo-standard/releases)

!!! tip "Obtenha ferramentas independentemente"
    Auditores devem baixar o validador e schemas diretamente do release oficial do AIMO Standard, não da parte submissora.

Para o procedimento de verificação completo (checksums, attestação, passo a passo), veja **[Standard → Versões → Procedimento de Verificação](../standard/versions/index.md)**. Veja também [Trust Package](../governance/trust-package.md) para materiais prontos para auditores.

## Declaração de não-sobrereivindicação

!!! warning "Importante"
    O AIMO Standard suporta **explicabilidade e prontidão de evidências**. Ele **não** fornece aconselhamento jurídico, garante conformidade, nem certifica conformidade com qualquer regulamentação ou framework. Adotantes devem verificar reivindicações contra textos autoritativos e obter aconselhamento profissional conforme apropriado.

Veja [Limite de Responsabilidade](../governance/responsibility-boundary.md) para escopo, suposições e responsabilidades do adotante.
