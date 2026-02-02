---
description: AIMO 표준 버전 이력. 감사자 준비 PDF, 기계 판독 가능 산출물, 체크섬 및 빌드 출처 증명이 포함된 공식 고정 릴리스.
---

# 버전

공식 릴리스는 감사자 준비 PDF 및 기계 판독 가능 산출물과 함께 게시된 고정 스냅샷입니다.

## 최신 릴리스

!!! success "현재 버전"
    **v0.0.2** (2026-02-02) — [문서 보기](../current/index.md) | [GitHub 릴리스](https://github.com/billyrise/aimo-standard/releases/tag/v0.0.2)

## 버전 이력

| 버전 | 날짜 | 릴리스 노트 | PDF (EN) | PDF (JA) | 산출물 | 체크섬 |
| :------ | :--- | :------------ | :------- | :------- | :-------- | :-------- |
| **v0.0.2** | 2026-02-02 | [변경로그](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/SHA256SUMS.txt) |
| **v0.0.1** | 2026-02-02 | [변경로그](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/SHA256SUMS.txt) |

!!! note "데이터 소스"
    이 버전 테이블은 [GitHub Releases](https://github.com/billyrise/aimo-standard/releases)와 동기화됩니다. 각 릴리스 태그(`vX.Y.Z`)는 사양의 고정 스냅샷에 해당합니다.

## 검증 절차

감사자 및 구현자는 SHA-256 체크섬을 사용하여 다운로드 무결성을 확인해야 합니다:

### 1. 릴리스 자산 다운로드

=== "Linux / macOS"

    ```bash
    # 특정 버전의 모든 자산 다운로드
    VERSION=v0.0.1
    BASE_URL="https://github.com/billyrise/aimo-standard/releases/download/${VERSION}"

    curl -LO "${BASE_URL}/trust_package.pdf"
    curl -LO "${BASE_URL}/trust_package.ja.pdf"
    curl -LO "${BASE_URL}/aimo-standard-artifacts.zip"
    curl -LO "${BASE_URL}/SHA256SUMS.txt"
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 특정 버전의 모든 자산 다운로드
    $VERSION = "v0.0.1"
    $BASE_URL = "https://github.com/billyrise/aimo-standard/releases/download/$VERSION"

    Invoke-WebRequest -Uri "$BASE_URL/trust_package.pdf" -OutFile trust_package.pdf
    Invoke-WebRequest -Uri "$BASE_URL/trust_package.ja.pdf" -OutFile trust_package.ja.pdf
    Invoke-WebRequest -Uri "$BASE_URL/aimo-standard-artifacts.zip" -OutFile aimo-standard-artifacts.zip
    Invoke-WebRequest -Uri "$BASE_URL/SHA256SUMS.txt" -OutFile SHA256SUMS.txt
    ```

### 2. 체크섬 확인

=== "Linux"

    ```bash
    # 다운로드된 모든 파일을 체크섬과 비교하여 확인
    sha256sum -c SHA256SUMS.txt

    # 예상 출력 (모두 "OK" 표시):
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "macOS"

    ```bash
    # 다운로드된 모든 파일을 체크섬과 비교하여 확인
    shasum -a 256 -c SHA256SUMS.txt

    # 예상 출력 (모두 "OK" 표시):
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 각 파일 확인
    Get-FileHash .\trust_package.pdf -Algorithm SHA256
    Get-FileHash .\trust_package.ja.pdf -Algorithm SHA256
    Get-FileHash .\aimo-standard-artifacts.zip -Algorithm SHA256

    # 해시 출력을 SHA256SUMS.txt와 비교
    Get-Content .\SHA256SUMS.txt
    ```

### 3. 수동 확인 (대안)

=== "Linux"

    ```bash
    # 특정 파일의 해시 계산
    sha256sum trust_package.pdf

    # 출력을 SHA256SUMS.txt와 비교
    cat SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # 특정 파일의 해시 계산
    shasum -a 256 trust_package.pdf

    # 출력을 SHA256SUMS.txt와 비교
    cat SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 특정 파일의 해시 계산
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # 체크섬 파일 보기
    Get-Content .\SHA256SUMS.txt
    ```

!!! tip "감사자용"
    항상 제출 당사자가 아닌 공식 GitHub 릴리스에서 직접 체크섬 파일을 획득하세요. 이것은 독립적인 검증을 보장합니다.

### 4. 빌드 출처 확인 (증명)

모든 릴리스 자산에는 GitHub Actions에서 생성된 암호화 서명된 빌드 출처 증명이 포함됩니다. 이를 통해 자산이 변조 없이 공식 저장소에서 빌드되었는지 확인할 수 있습니다.

**전제 조건**: [GitHub CLI](https://cli.github.com/) (`gh`) 설치

```bash
# GitHub CLI를 사용하여 릴리스 자산 다운로드
VERSION=v0.0.1
gh release download "$VERSION" --repo billyrise/aimo-standard

# 각 자산에 대한 증명 확인
gh attestation verify trust_package.pdf --repo billyrise/aimo-standard
gh attestation verify trust_package.ja.pdf --repo billyrise/aimo-standard
gh attestation verify aimo-standard-artifacts.zip --repo billyrise/aimo-standard
gh attestation verify SHA256SUMS.txt --repo billyrise/aimo-standard
```

**예상 출력** (성공):

```
Loaded digest sha256:abc123... for file trust_package.pdf
Loaded 1 attestation from GitHub API
✓ Verification succeeded!
```

**오프라인 확인** (에어갭 환경):

```bash
# 먼저 신뢰할 수 있는 루트 다운로드 (한 번 네트워크 필요)
gh attestation trusted-root > trusted-root.jsonl

# 그런 다음 오프라인으로 확인
gh attestation verify trust_package.pdf \
  --repo billyrise/aimo-standard \
  --custom-trusted-root trusted-root.jsonl
```

!!! info "증명이 증명하는 것"
    빌드 출처 증명은 릴리스 자산이 다음임을 암호화로 증명합니다:

    1. 개발자의 로컬 머신이 아닌 GitHub Actions에서 빌드됨
    2. 공식 `billyrise/aimo-standard` 저장소에서 빌드됨
    3. 릴리스 태그와 연결된 정확한 커밋에서 빌드됨
    4. 빌드 완료 후 수정되지 않음

## 호환성

AIMO 표준은 [시맨틱 버전 관리](https://semver.org/) (SemVer)를 따릅니다:

| 변경 유형 | 버전 범프 | 영향 |
| :---------- | :----------- | :----- |
| **MAJOR** | X.0.0 | 호환성 깨는 변경 — 마이그레이션 필요 |
| **MINOR** | 0.X.0 | 이전 호환 추가 |
| **PATCH** | 0.0.X | 수정 및 명확화 |

완전한 버전 관리 정책은 [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)를 참조하세요.

## 마이그레이션

호환성 깨는 변경이 있는 버전 간 업그레이드 시:

1. [변경로그](../current/08-changelog.md)에서 호환성 깨는 변경 확인
2. 특정 업그레이드 경로에 대해 [마이그레이션 가이드](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) 검토
3. 새 스키마 요구사항에 맞게 증거 번들 업데이트
4. 컴플라이언스 확인을 위해 검증기 재실행

!!! warning "호환성 깨는 변경"
    MAJOR 버전 업데이트는 기존 증거 번들에 대한 변경이 필요할 수 있습니다. 업그레이드 전에 항상 마이그레이션 가이드를 검토하세요.

## 버전화된 문서 스냅샷

각 릴리스는 다음에서 접근 가능한 고정 문서 스냅샷을 생성합니다:

- 프로덕션: `https://standard.aimoaas.com/{version}/` (예: `/0.0.1/`)
- GitHub Pages: `https://billyrise.github.io/aimo-standard/{version}/`

### URL 유형 및 의미

| URL 패턴 | 설명 | 감사 인용용? |
|-------------|-------------|---------------------|
| `/X.Y.Z/` (예: `/0.0.1/`) | **고정 릴리스** — 불변 스냅샷 | **예** (선호) |
| `/latest/` | **별칭** — 가장 최근 릴리스로 리디렉션 | 예 (`/X.Y.Z/`로 해결) |
| `/dev/` | **미리보기** — 릴리스되지 않은 main 브랜치 콘텐츠 | **아니요** (인용용 아님) |

!!! warning "`/latest/` vs `/dev/` 이해"
    - **`/latest/`**는 가장 최근 **릴리스된** 버전으로의 별칭(리디렉션)입니다. 고정 스냅샷으로 해결되므로 인용에 안전합니다.
    - **`/dev/`**는 현재 `main` 브랜치를 반영하며 **릴리스되지 않은 변경**을 포함할 수 있습니다. 감사 보고서에서 `/dev/`를 절대 인용하지 마세요.

### FAQ

??? question "왜 `/latest/`가 버전 번호가 아닌가요?"
    `/latest/`는 항상 가장 최근 안정 릴리스(예: `/0.0.1/`)로 리디렉션하는 편의 별칭입니다. 이를 통해 사용자는 자동으로 현재 버전을 받으면서 단일 URL을 북마크할 수 있습니다. 불변성이 필요한 공식 감사의 경우 대신 명시적 버전 URL을 인용하세요.

??? question "감사자는 어떤 URL을 인용해야 하나요?"
    - **공식 감사 (불변성 필요)**: `/X.Y.Z/` 사용 (예: `https://standard.aimoaas.com/0.0.1/standard/current/`)
    - **일반 참조**: `/latest/`는 현재 릴리스로 리디렉션되므로 허용 가능
    - **절대 인용하지 마세요**: `/dev/` (릴리스되지 않음, 변경될 수 있음)

??? question "`/latest/`가 예상과 다른 콘텐츠를 표시하면?"
    이것은 배포 버그입니다. `/latest/`가 가장 최근 [GitHub 릴리스](https://github.com/billyrise/aimo-standard/releases)와 다르다고 의심되면 [이슈를 보고](https://github.com/billyrise/aimo-standard/issues)해 주세요. `/latest/` 별칭은 항상 가장 최근 태그된 릴리스로 리디렉션되어야 합니다.

## 리소스

- **[릴리스 허브](../../releases/index.md)** — 제출 준비, 감사자 검증, 과대 주장 금지 선언
- **[신뢰 패키지](../../governance/trust-package.md)** — 감사자 준비 보증 자료
- **[변경로그 (상세)](../current/08-changelog.md)** — 폐기 추적이 있는 전체 변경 이력
- **[VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)** — 완전한 버전 관리 정책
