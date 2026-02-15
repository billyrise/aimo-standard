---
description: AIMO 표준 기여 가이드 - 코드, 문서 및 번역 기여 방법. 이슈 및 PR 지침.
---
<!-- aimo:translation_status=translated -->

# 기여하기

이 페이지는 AIMO 표준에 기여하기 위한 지침을 제공합니다.

## 빠른 시작

1. 저장소 포크
2. 기능 브랜치 생성
3. 아래 지침에 따라 변경
4. 품질 검사 실행
5. 풀 리퀘스트 제출

## 핵심 원칙

| 원칙 | 설명 |
| --------- | ----------- |
| 영어가 정본 | 먼저 `docs/en/`을 편집한 후 `docs/ja/` 업데이트 |
| SSOT | 이 저장소가 단일 진실 공급원 |
| 생성 파일 수동 편집 금지 | 소스 편집, 재생성, 커밋 |
| 모든 변경은 PR을 통해 | 메인테이너도 풀 리퀘스트 사용 |

## 품질 검사

PR 제출 전 실행:

```bash
# 가상 환경 활성화
source .venv/bin/activate

# 린트 실행
python tooling/checks/lint_i18n.py
python tooling/checks/lint_schema.py
python tooling/audit/baseline_audit.py --check

# 문서 빌드
mkdocs build --strict
```

## 변경 유형

| 유형 | 예시 | 리뷰 요구사항 |
| ---- | -------- | ------------------- |
| 규범적 | 스키마 변경, 요구사항 | 메인테이너 + 토론 |
| 비규범적 | 오타, 명확화 | 메인테이너 승인 |
| i18n | 번역 | 구조가 EN과 일치해야 함 |
| 도구 | CI/CD, 스크립트 | 메인테이너 승인 |

## i18n 지침

### 업데이트 순서

1. 영어 소스 편집 (`docs/en/...`)
2. 일본어 번역 업데이트 (`docs/ja/...`)
3. `lint_i18n.py` 실행하여 일관성 확인
4. 둘 다 함께 커밋

### 구조 요구사항

- 양 언어에서 동일한 파일 이름
- 동일한 제목 계층 구조
- 섹션당 동일한 페이지 수

## PR 체크리스트

PR 제출 시 확인:

- [ ] 변경 유형 식별됨 (docs / schema / examples / tooling)
- [ ] 호환성 깨는 변경 평가 완료
- [ ] i18n: EN과 JA 함께 업데이트됨 (해당시)
- [ ] 품질 검사 통과
- [ ] 관련 이슈 연결됨

## 호환성 깨는 변경

호환성 깨는 변경은 다음이 필요합니다:

1. 구현 전 이슈 토론
2. [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)에 따른 버전 업
3. 마이그레이션 지침이 포함된 변경로그 항목

## 적합성 주장 업데이트

적합성 주장을 추가 또는 수정하려면:

1. 커버리지 맵 YAML 업데이트
2. 해당 문서 페이지 업데이트
3. 검증기 테스트 실행
4. 매핑 근거 문서화

## 전체 지침

루트 수준 가이드는 [CONTRIBUTING.md](https://github.com/billyrise/aimo-standard/blob/main/CONTRIBUTING.md)를 참조하세요.

## 관련 페이지

- [거버넌스](../) — 프로젝트 거버넌스
- [현지화 가이드](../../contributing/localization/) — i18n 세부사항
- [책임 경계](../responsibility-boundary/) — AIMO가 제공하는 것
