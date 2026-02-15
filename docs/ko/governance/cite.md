---
description: AIMO 표준 인용 가이드 - 학술 논문, 감사 보고서 및 제안서에서 인용하는 방법. CITATION.cff 및 BibTeX 형식.
---
<!-- aimo:translation_status=translated -->

# 인용 방법

이 페이지는 학술 논문, 감사 보고서 및 제안서에서 AIMO 표준을 인용하는 가이드를 제공합니다.

## CITATION.cff

저장소에는 Citation File Format 표준을 따르는 [CITATION.cff](https://github.com/billyrise/aimo-standard/blob/main/CITATION.cff) 파일이 포함되어 있습니다.

GitHub는 이 파일에서 인용 정보를 자동으로 표시합니다.

## 권장 인용

### 간략 형식 (인라인)

> AIMO Standard Contributors. (2026). AIMO Standard. https://standard.aimoaas.com/

### BibTeX

```bibtex
@software{aimo_standard,
  author = {{AIMO Standard Contributors}},
  title = {AIMO Standard},
  url = {https://standard.aimoaas.com/},
  version = {0.0.2},
  year = {2026}
}
```

### APA 스타일

> AIMO Standard Contributors. (2026). *AIMO Standard* (Version 0.0.2) [Software]. https://standard.aimoaas.com/

## 버전별 인용

특정 버전을 인용할 때:

> AIMO Standard Contributors. (2026). AIMO Standard v0.0.2. https://github.com/billyrise/aimo-standard/releases/tag/v0.0.2

## 감사 문서

감사 보고서 및 컴플라이언스 문서의 경우:

| 필드 | 값 |
| ----- | ----- |
| 표준 이름 | AIMO Standard |
| 버전 | (사용된 버전 지정, 예: v0.0.1) |
| 웹사이트 | https://standard.aimoaas.com/ |
| 저장소 | https://github.com/billyrise/aimo-standard |
| 릴리스 | https://github.com/billyrise/aimo-standard/releases |

## URL 지침

### 정식 URL

공식 문서에서 다음 URL을 사용하세요:

| 목적 | URL |
| ------- | --- |
| 최신 문서 | https://standard.aimoaas.com/latest/ |
| 특정 버전 | https://standard.aimoaas.com/0.0.2/ |
| GitHub 릴리스 | https://github.com/billyrise/aimo-standard/releases |

!!! note "사이트 경로 형식"
    사이트 경로는 `v` 접두사 없이 버전 번호를 사용합니다. 버전 `v0.0.1`의 경우 URL에서 `/0.0.1/`을 사용하세요.

### 피해야 할 것

- GitHub Pages 미러 URL (임시)
- 브랜치별 URL (변경될 수 있음)

## 관련 페이지

- [신뢰 패키지](../trust-package/) — 감사자 준비 자료
- [거버넌스](../) — 프로젝트 거버넌스
- [라이선스](../license/) — 라이선스 조건
