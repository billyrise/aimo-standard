---
description: AIMO 표준 릴리스 - 버전화된 PDF, 산출물 및 체크섬 다운로드. 변경로그, 마이그레이션 가이드 및 빌드 출처 증명.
---
<!-- aimo:translation_status=translated -->

# 릴리스

이 섹션은 버전화된 릴리스, 변경로그, 마이그레이션 및 배포 산출물의 허브입니다.

## 최신 릴리스 다운로드

**[GitHub Releases](https://github.com/billyrise/aimo-standard/releases/latest)** — "latest" 릴리스의 단일 정보원입니다. 사이트 경로 `/latest/`는 동일한 버전으로 리디렉션됩니다.

## 검증 절차 (영구 웹 페이지)

전체 **검증 절차**(자산 다운로드, 체크섬 검증, 빌드 출처 증명)는 PDF뿐만 아니라 영구 웹 페이지로도 제공됩니다:

- **[Standard → 버전 → 검증 절차](../standard/versions/)** — 단계별 체크섬 검증(Linux/macOS/Windows) 및 출처 증명.

릴리스 자산을 검증하거나 감사 산출물에 검증 단계를 문서화할 때 이 페이지를 사용하세요.

## 릴리스 자산

각 공식 릴리스(`vX.Y.Z` 태그)에는 다음이 포함됩니다:

| 자산 | 설명 |
| --- | --- |
| `trust_package.pdf` | 영어 신뢰 패키지 — 감사자 준비 보증 자료 |
| `trust_package.ja.pdf` | 일본어 신뢰 패키지 |
| `aimo-standard-artifacts.zip` | 스키마, 템플릿, 예제, 검증기 규칙 |
| `SHA256SUMS.txt` | 모든 자산의 SHA-256 체크섬 |

### 다운로드 확인

다운로드 후 체크섬을 사용하여 파일 무결성을 확인하세요:

=== "Linux"

    ```bash
    # 체크섬 파일 다운로드
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # 특정 파일 확인
    sha256sum -c SHA256SUMS.txt --ignore-missing

    # 또는 수동으로 확인:
    sha256sum trust_package.pdf
    # 출력을 SHA256SUMS.txt와 비교
    ```

=== "macOS"

    ```bash
    # 체크섬 파일 다운로드
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # 특정 파일 확인
    shasum -a 256 -c SHA256SUMS.txt

    # 또는 수동으로 확인:
    shasum -a 256 trust_package.pdf
    # 출력을 SHA256SUMS.txt와 비교
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 체크섬 파일 다운로드
    Invoke-WebRequest -Uri "https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt" -OutFile SHA256SUMS.txt

    # 특정 파일 확인
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # 해시 출력을 SHA256SUMS.txt와 비교
    Get-Content .\SHA256SUMS.txt
    ```

## 산출물 Zip 내용

`aimo-standard-artifacts.zip`에는 다음이 포함됩니다:

- `schemas/jsonschema/*` — 검증용 JSON 스키마
- `templates/ev/*` — 증거 템플릿 (JSON + Markdown)
- `examples/*` — 샘플 증거 번들
- `coverage_map/coverage_map.yaml` — 외부 표준 매핑
- `validator/rules/*` — 검증 규칙 정의
- `VERSIONING.md`, `GOVERNANCE.md`, `SECURITY.md` 등.

## 리소스

- **버전 이력 테이블**: [표준 > 버전](../standard/versions/) — 모든 릴리스 자산(PDF, ZIP, SHA256)에 대한 직접 링크가 있는 버전 테이블
- **변경로그 (사양)**: [표준 > 현재 > 변경로그](../standard/current/08-changelog/) — 규범적 및 비규범적 변경 이력.
- **릴리스 프로세스**: `vX.Y.Z` 태그, CI 빌드, `dist/` 아래 PDF, 체크섬, GitHub Release 자산. 저장소의 [GOVERNANCE.md](https://github.com/billyrise/aimo-standard/blob/main/GOVERNANCE.md) 및 [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) 참조.
- **마이그레이션 가이드**: [MIGRATION.md](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) — 호환성 깨는 변경에 대한 업그레이드 경로.

거버넌스 및 버전 정책은 [거버넌스](../governance/)를 참조하세요.

## 제출 패키지 준비

감사 제출을 위해 증거를 준비할 때:

1. **증거 번들 생성**: [증거 번들](../artifacts/evidence-bundle/) 및 [최소 증거 요구사항](../artifacts/minimum-evidence/)에 따라 EV 레코드, 딕셔너리, 요약 및 변경 로그를 생성합니다.
2. **검증기 실행**: `python validator/src/validate.py bundle/root.json`을 실행하여 구조적 일관성을 확인합니다. 진행하기 전에 모든 오류를 수정하세요.
3. **체크섬 생성**: 검증용 SHA-256 체크섬을 생성합니다:

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
4. **패키지**: 번들 디렉토리의 zip 아카이브를 생성합니다.
5. **버전 정합 문서화**: 증거가 정합하는 AIMO 표준 릴리스(예: `v1.0.0`)를 명시합니다.
6. **제출**: 패키지, 체크섬 및 버전 참조를 감사자에게 제공합니다.

전체 준비 가이드는 [신뢰 패키지](../governance/trust-package/)를 참조하세요.

## 감사자용: 검증 절차

증거 제출을 받는 감사자는 무결성 및 구조를 확인해야 합니다:

1. **체크섬 확인**: 체크섬 검증(Linux: `sha256sum -c`, macOS: `shasum -a 256 -c`, Windows: `Get-FileHash`)을 실행하여 파일 무결성 확인
2. **검증기 실행**: `python validator/src/validate.py bundle/root.json`을 실행하여 구조 확인
3. **버전 확인**: 명시된 AIMO 표준 버전이 [GitHub Releases](https://github.com/billyrise/aimo-standard/releases)에 존재하는지 확인

!!! tip "독립적으로 도구 획득"
    감사자는 검증기와 스키마를 제출 당사자가 아닌 공식 AIMO 표준 릴리스에서 직접 다운로드해야 합니다.

전체 검증 절차(체크섬, 증명, 단계별)는 **[Standard → 버전 → 검증 절차](../standard/versions/)**를 참조하세요. 감사자 준비 자료는 [신뢰 패키지](../governance/trust-package/)도 참조하세요.

## 과대 주장 금지 선언

!!! warning "중요"
    AIMO 표준은 **설명 가능성 및 증거 준비**를 지원합니다. 법률 자문을 제공하거나, 컴플라이언스를 보장하거나, 어떤 규정 또는 프레임워크에 대한 적합성을 인증하지 **않습니다**. 채택자는 권위 있는 텍스트와 대조하여 주장을 확인하고 적절한 전문 자문을 받아야 합니다.

범위, 가정 및 채택자 책임은 [책임 경계](../governance/responsibility-boundary/)를 참조하세요.
