---
description: AIMO 신뢰 패키지 - 감사자 준비 자료 번들. 감사자, 법무 및 IT 보안이 AI 거버넌스 채택 준비를 평가하는 데 필요한 최소 문서.
---

# 신뢰 패키지 (보증 패키지)

이 페이지는 감사자, 법무 및 IT 보안이 채택 준비를 평가하는 데 필요한 최소 자료를 번들로 제공합니다.
이것은 허브일 뿐이며; 상세한 증거 목차 및 커버리지 테이블은 각 섹션에서 유지됩니다.

## 다운로드

**[신뢰 패키지 PDF 다운로드 (최신 릴리스)](https://github.com/billyrise/aimo-standard/releases/latest)**

신뢰 패키지 PDF는 감사자 준비 자료를 단일 문서로 통합합니다. 각 GitHub 릴리스에는 다음이 포함됩니다:

- `trust_package.pdf` — 영어 신뢰 패키지
- `trust_package.ja.pdf` — 일본어 신뢰 패키지
- `aimo-standard-artifacts.zip` — 스키마, 템플릿, 예제, 검증기 규칙
- `SHA256SUMS.txt` — 검증용 체크섬

## 제공되는 것

- **적합성**: 컴플라이언스 주장 방법 및 각 수준의 의미 — [적합성](../../conformance/)
- **커버리지 맵**: 외부 표준에 대한 매핑 — [커버리지 맵 인덱스](../../coverage-map/), [커버리지 맵 방법론](../../coverage-map/methodology/)
- **표준**: 규범적 요구사항 및 정의 — [표준 (현재)](../../standard/current/)
- **분류체계**: AI 거버넌스를 위한 8차원 분류 시스템 — [분류체계](../../standard/current/03-taxonomy/), [코드](../../standard/current/04-codes/), [딕셔너리](../../standard/current/05-dictionary/)
- **증거 번들**: 구조, 목차, 추적성 — [증거 번들](../../artifacts/evidence-bundle/)
- **최소 증거 요구사항**: 생명주기별 MUST 수준 체크리스트 — [최소 증거 요구사항](../../artifacts/minimum-evidence/)
- **검증기**: 규칙 및 참조 검사 — [검증기](../../validator/)
- **예제**: 감사 준비 샘플 번들 — [예제](../../examples/)
- **릴리스**: 변경 이력 및 배포 — [릴리스](../../releases/)
- **거버넌스**: 정책, 보안, 라이선스 — [거버넌스](../../governance/)

## 감사 준비를 위한 최소 세트

| 항목 | 위치 | 결과 / 증명하는 것 |
| --- | --- | --- |
| 적합성 수준 | [적합성](../../conformance/) | 컴플라이언스 주장 방법 및 필요한 증거 범위 |
| 커버리지 매핑 | [커버리지 맵 인덱스](../../coverage-map/), [커버리지 맵 방법론](../../coverage-map/methodology/) | 외부 규정 및 표준에 대한 설명 가능성 |
| 분류체계 및 딕셔너리 | [분류체계](../../standard/current/03-taxonomy/), [코드](../../standard/current/04-codes/), [딕셔너리](../../standard/current/05-dictionary/) | AI 시스템 분류 시스템 (8차원, 91개 코드) |
| 증거 산출물 | [증거 번들](../../artifacts/evidence-bundle/), [최소 증거](../../artifacts/minimum-evidence/), [EV 템플릿](../../standard/current/06-ev-template/) | 추적성 지원을 위해 존재해야 하는 데이터 |
| 검증기 검사 | [검증기](../../validator/) | 내부 일관성 및 완전성 검증 방법 |
| 예제 번들 | [예제](../../examples/) | 실제 감사 준비 패키지의 모습 |
| 변경 통제 | [릴리스](../../releases/), [거버넌스](../../governance/) | 업데이트 관리 및 전달 방법 |
| 보안 / 라이선스 / 상표 | [거버넌스](../../governance/) | 채택 결정을 위한 법적 및 보안 태세 |

## 인용 방법

인용 지침 및 맥락은 저장소 README를 사용하세요; 거버넌스는 권위 있는 정책에 연결됩니다.
[README.md](https://github.com/billyrise/aimo-standard/blob/main/README.md) 및 [거버넌스](../../governance/)를 참조하세요.

## 산출물 zip 내용

`aimo-standard-artifacts.zip`에는 다음이 포함됩니다:

- **분류체계 (SSOT)**: `source_pack/03_taxonomy/` — 딕셔너리 CSV (91개 코드), YAML, 코드 시스템
- **JSON 스키마**: `schemas/jsonschema/` — 기계 판독 가능 검증 스키마
- **템플릿**: `templates/ev/` — 증거 레코드 템플릿 (JSON + Markdown)
- **예제**: `examples/` — 빠른 채택을 위한 최소 샘플 번들
- **커버리지 맵**: `coverage_map/coverage_map.yaml` — 외부 표준에 대한 매핑
- **검증기 규칙**: `validator/rules/` — 검증 규칙 정의
- **거버넌스 문서**: `VERSIONING.md`, `GOVERNANCE.md`, `SECURITY.md`, `LICENSE.txt` 등.

## 책임 경계

AIMO 표준은 구조화된 증거 형식 및 설명 가능성 프레임워크를 제공합니다. 법률 자문, 컴플라이언스 인증, 리스크 평가 또는 감사 실행은 제공하지 **않습니다**.

전체 범위 정의, 가정 및 채택자 책임은 [책임 경계](../responsibility-boundary/)를 참조하세요.

## 제출 패키지 준비 방법

감사 준비 제출을 준비하려면 다음 단계를 따르세요:

1. **증거 번들 생성**: [증거 번들](../../artifacts/evidence-bundle/) 및 [최소 증거 요구사항](../../artifacts/minimum-evidence/)에 따라 EV 레코드, 딕셔너리, 요약 및 변경 로그를 생성합니다.
2. **검증기 실행**: `python validator/src/validate.py bundle/root.json`을 실행하여 구조적 일관성을 확인합니다. 오류가 있으면 진행하기 전에 수정하세요.
3. **체크섬 생성**: 모든 제출 파일에 대해 SHA-256 체크섬을 생성합니다:

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
4. **산출물 패키지**: 증거 번들의 zip 아카이브를 생성합니다:
   ```bash
   zip -r evidence_bundle.zip bundle_directory/
   ```
5. **릴리스 버전 참조**: 번들이 정합하는 AIMO 표준 버전(예: `v1.0.0`)을 명시합니다.
6. **제출**: zip, 체크섬 및 버전 참조를 감사자 또는 컴플라이언스 기능에 제공합니다.

릴리스 자산 및 검증은 [릴리스](../../releases/)를 참조하세요.

## 과대 주장 금지 선언

!!! warning "중요"
    AIMO 표준은 **설명 가능성 및 증거 준비**를 지원합니다. 법률 자문을 제공하거나, 컴플라이언스를 보장하거나, 어떤 규정 또는 프레임워크에 대한 적합성을 인증하지 **않습니다**. 채택자는 권위 있는 텍스트와 대조하여 주장을 확인하고 적절한 전문 자문을 받아야 합니다.

범위, 가정 및 채택자 책임에 대한 자세한 내용은 [책임 경계](../responsibility-boundary/)를 참조하세요.

## 감사자용: 검증 절차

증거 제출을 받을 때 감사자는 다음 단계를 사용하여 무결성 및 구조를 검증해야 합니다:

!!! success "빌드 출처 이용 가능"
    모든 릴리스 자산에는 암호화 서명된 빌드 증명이 포함됩니다. 증명 검증 단계는 [검증 절차](../../standard/versions/#4-verify-build-provenance-attestation)를 참조하세요.

### 1단계: 체크섬 확인 (SHA-256)

=== "Linux"

    ```bash
    # 제출과 함께 SHA256SUMS.txt를 다운로드하거나 받음
    # 모든 파일이 기록된 체크섬과 일치하는지 확인
    sha256sum -c SHA256SUMS.txt

    # 또는 개별 파일을 수동으로 확인:
    sha256sum evidence_bundle.zip
    # 출력을 SHA256SUMS.txt의 값과 비교
    ```

=== "macOS"

    ```bash
    # 모든 파일이 기록된 체크섬과 일치하는지 확인
    shasum -a 256 -c SHA256SUMS.txt

    # 또는 개별 파일을 수동으로 확인:
    shasum -a 256 evidence_bundle.zip
    # 출력을 SHA256SUMS.txt의 값과 비교
    ```

=== "Windows (PowerShell)"

    ```powershell
    # 개별 파일 확인
    Get-FileHash .\evidence_bundle.zip -Algorithm SHA256

    # 해시 출력을 SHA256SUMS.txt와 비교
    Get-Content .\SHA256SUMS.txt
    ```

체크섬이 실패하면 제출을 거부하거나 재요청해야 합니다.

### 2단계: 번들 구조 확인 (검증기)

**전제 조건** (일회성 설정):

```bash
# 공식 AIMO 표준 릴리스 클론
git clone https://github.com/billyrise/aimo-standard.git
cd aimo-standard

# 중요: 제출에 명시된 정확한 버전 사용
# VERSION을 제출자가 선언한 버전으로 교체 (예: v0.0.1)
VERSION=v0.0.1  # ← 제출의 버전과 일치
git checkout "$VERSION"

# Python 환경 설정
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

!!! warning "버전 일치"
    항상 제출에 명시된 정확한 AIMO 표준 버전을 사용하세요. 다른 버전을 사용하면 버전 간의 스키마 또는 규칙 변경으로 인해 검증 불일치가 발생할 수 있습니다.

**검증 실행**:

```bash
# 제출된 번들 추출
unzip evidence_bundle.zip -d bundle/

# 번들의 root.json에 대해 검증기 실행
python validator/src/validate.py bundle/root.json

# 예상 출력: "validation OK" 또는 오류 목록
```

**예시** (내장 샘플 사용):

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

검증기가 확인하는 것:

- 필수 파일 존재 (EV 레코드, 딕셔너리)
- JSON 파일이 스키마에 부합
- 상호 참조(request_id, review_id 등)가 유효
- 타임스탬프가 존재하고 적절한 형식

### 3단계: 버전 정합 확인

제출이 공식 AIMO 표준 릴리스를 참조하는지 확인합니다:

1. 명시된 버전(예: `v0.0.1`)이 [GitHub Releases](https://github.com/billyrise/aimo-standard/releases)에 존재하는지 확인
2. 제출된 스키마를 릴리스 산출물과 비교
3. 공식 릴리스와의 편차 기록

### 확인 사항

| 확인 | 통과 기준 | 실패 조치 |
| --- | --- | --- |
| 체크섬 일치 | 모든 `sha256sum -c` 검사 통과 | 거부 또는 재요청 |
| 검증기 통과 | `validate.py`에서 오류 없음 | 수락 전 수정 요청 |
| 버전 존재 | GitHub에 릴리스 태그 존재 | 버전 정합 명확화 |
| 필수 필드 존재 | EV 레코드에 id, timestamp, source, summary 있음 | 완료 요청 |
| 추적성 유지 | 상호 참조가 올바르게 해결 | 연결 수정 요청 |

!!! info "감사자 독립성"
    감사자는 검증 독립성을 보장하기 위해 제출 당사자가 아닌 공식 AIMO 표준 릴리스에서 직접 검증기와 스키마를 획득해야 합니다.

## 감사 여정

이 페이지에서 권장되는 감사 여정:

1. **분류 시스템**: [분류체계](../../standard/current/03-taxonomy/) + [딕셔너리](../../standard/current/05-dictionary/) — 8차원 코드 시스템 이해
2. **증거 구조**: [증거 번들](../../artifacts/evidence-bundle/) — 번들 목차 및 추적성 이해
3. **필수 증거**: [최소 증거 요구사항](../../artifacts/minimum-evidence/) — 생명주기별 MUST 수준 체크리스트
4. **프레임워크 정합**: [커버리지 맵](../../coverage-map/) + [방법론](../../coverage-map/methodology/) — AIMO가 외부 프레임워크에 매핑되는 방법 확인
5. **검증**: [검증기](../../validator/) — 구조적 일관성 검사 실행
6. **다운로드**: [릴리스](../../releases/) — 릴리스 자산 획득 및 체크섬 확인
