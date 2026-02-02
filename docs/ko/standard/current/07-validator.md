---
description: AIMO 검증기 - 증거 팩이 AIMO 표준 스키마에 부합하는지 확인합니다. 컴플라이언스 검사를 위한 검증 규칙, 오류 처리 및 참조 구현.
---

# 검증기

AIMO 검증기는 증거 팩 및 관련 산출물이 AIMO 표준 스키마 및 요구사항에 부합하는지 확인합니다.

참조: [인간 감독 프로토콜](../../governance/human-oversight-protocol.md) — 기계 vs. 인간 검토의 책임 경계.

## 실제 검증기

30초 빠른 시작(설치, 실행, 출력 해석)은 [검증기 허브](../../validator/index.md)를 참조하세요.

## 검증기 MVP 요구사항

최소 실행 가능 검증기는 다음 검사를 수행해야 합니다(MUST):

### 1. 필수 필드 검증

모든 필수 필드가 존재하는지 확인:

| 산출물 | 필수 필드 |
| --- | --- |
| 증거 팩 매니페스트 | pack_id, pack_version, taxonomy_version, created_date, last_updated, codes, evidence_files |
| 코드 객체 | FS, UC, DT, CH, IM, RS, EV (OB 선택적) |
| 증거 파일 항목 | file_id (EP-01..EP-07), filename, title (ev_type / ev_codes 선택) |

### 2. 차원 코드 검증

각 필수 차원에 최소 하나의 코드가 있는지 확인:

| 차원 | 요구사항 |
| --- | --- |
| FS (기능 범위) | 정확히 1개 코드 |
| UC (사용 사례 분류) | 최소 1개 코드 |
| DT (데이터 유형) | 최소 1개 코드 |
| CH (채널) | 최소 1개 코드 |
| IM (통합 모드) | 정확히 1개 코드 |
| RS (리스크 표면) | 최소 1개 코드 |
| OB (결과 / 혜택) | 선택적 (0개 이상) |
| EV (증거 유형) | 최소 1개 코드 |

### 3. 딕셔너리 존재 확인

모든 코드가 분류체계 딕셔너리에 존재하는지 검증:

- 지정된 `taxonomy_version`의 분류체계 딕셔너리 로드
- 매니페스트의 각 코드가 딕셔너리에 존재하는지 확인
- 차원 및 값과 함께 유효하지 않은 코드 보고

### 4. 코드 형식 검증

모든 코드가 예상 형식과 일치하는지 확인:

```regex
^(FS|UC|DT|CH|IM|RS|OB|EV)-\d{3}$
```

### 5. 스키마 검증

JSON 스키마에 대해 검증:

| 스키마 | 목적 |
| --- | --- |
| `evidence_pack_manifest.schema.json` | 증거 팩 매니페스트 |
| `taxonomy_pack.schema.json` | 분류체계 팩 정의 |
| `changelog.schema.json` | 변경로그 항목 |

## 검증 규칙

### 규칙: 필수 차원

```yaml
rule_id: required_dimensions
description: 모든 필수 차원에 최소 하나의 코드가 있어야 함
severity: error
check: |
  - FS: 정확히 1개
  - UC: 최소 1개
  - DT: 최소 1개
  - CH: 최소 1개
  - IM: 정확히 1개
  - RS: 최소 1개
  - EV: 최소 1개
```

### 규칙: 유효한 코드

```yaml
rule_id: valid_codes
description: 모든 코드가 분류체계 딕셔너리에 존재해야 함
severity: error
check: |
  manifest.codes의 각 코드에 대해:
    - 코드가 지정된 taxonomy_version의 딕셔너리에 존재
    - 코드 상태가 'active' ('deprecated'인 경우 경고)
```

### 규칙: 코드 형식

```yaml
rule_id: code_format
description: 모든 코드가 표준 형식과 일치해야 함
severity: error
pattern: "^(FS|UC|DT|CH|IM|RS|OB|EV)-\\d{3}$"
```

### 규칙: 버전 형식

```yaml
rule_id: version_format
description: 버전이 유효한 SemVer이어야 함
severity: error
pattern: "^\\d+\\.\\d+\\.\\d+$"
fields:
  - pack_version
  - taxonomy_version
```

## 오류 출력 형식

검증 오류는 다음 형식으로 보고됩니다:

```
<path>: <severity>: <message>
```

**예시:**

```
codes.FS: error: 필수 차원 'FS'에 코드가 없음
codes.UC[0]: error: 코드 'UC-999'가 딕셔너리 v0.1.0에 존재하지 않음
pack_version: error: 유효하지 않은 버전 형식 'v1.0' (SemVer 기대됨)
codes.RS[1]: warning: 코드 'RS-002'가 v0.2.0에서 폐기됨
```

## 검증기가 확인하지 않는 것

검증기는 콘텐츠 품질이 아닌 구조적 적합성에 초점을 맞춥니다:

| 측면 | 이유 |
| --- | --- |
| 내용 정확성 | 검증기는 구조를 확인하며, 의미가 아님 |
| 증거 완전성 | 템플릿은 가이드이며, 강제 형식이 아님 |
| 상호 참조 해결 | 파일 존재가 확인되지 않음 |
| 타임스탬프 유효성 | ISO-8601이 엄격히 검증되지 않음 |
| ID 고유성 | 현재 강제되지 않음 |
| 무결성 해시 | 채택자 책임 |

## 참조 구현

Python에서 참조 구현이 제공됩니다:

```
validator/src/validate.py
```

### 사용

```bash
python validator/src/validate.py <manifest.json>
```

### 예시 출력

```
Validating: evidence_pack_manifest.json
Taxonomy version: 0.1.0

Checking required dimensions...
  FS: OK (1 code)
  UC: OK (3 codes)
  DT: OK (1 code)
  CH: OK (1 code)
  IM: OK (1 code)
  RS: OK (3 codes)
  OB: OK (2 codes)
  EV: OK (7 codes)

Checking code validity...
  All codes valid.

Validation: PASSED
```

## 버전 관리 정책

검증기 규칙은 SemVer를 따릅니다:

- **MAJOR**: 호환성 깨는 규칙 변경 (기존 유효 팩을 실패시키는 새 필수 검사)
- **MINOR**: 새 선택적 검사, 경고 또는 정보 메시지
- **PATCH**: 검증 결과를 변경하지 않는 버그 수정

## 스키마 참조

| 스키마 | 위치 |
| --- | --- |
| 증거 팩 매니페스트 | `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json` |
| 분류체계 팩 | `source_pack/03_taxonomy/schemas/taxonomy_pack.schema.json` |
| 변경로그 | `source_pack/03_taxonomy/schemas/changelog.schema.json` |

## 참조

- [분류체계](./03-taxonomy.md) - 차원 정의
- [코드](./04-codes.md) - 코드 형식
- [딕셔너리](./05-dictionary.md) - 코드 딕셔너리
- [검증기 규칙](../../validator/index.md) - 전체 규칙 문서
