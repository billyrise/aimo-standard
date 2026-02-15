---
description: AIMO Standard 개요. AI 거버넌스 감사를 위한 공유 분류체계, 코드 체계, 사전, 증거 템플릿 및 검증기 검사 정의.
---
<!-- aimo:translation_status=translated -->

# 개요（Overview）

**AIMO**는 **AI Management Office**를 의미합니다. AIMO Standard는 다음을 정의합니다:
- 공유 분류체계
- 코드 체계
- 초기 사전
- EV 템플릿
- 검증기 검사(사양 + 최소 참조 구현)

본 저장소는 다음을 게시합니다:
- 사람이 읽을 수 있는 사양(HTML)
- 기계가 읽을 수 있는 산출물(스키마/템플릿/예제)
- 공식 PDF 릴리스

## 포지셔닝: ISO/IEC 42001(AIMS) 동반

AIMO Standard는 **증거 준비 및 설명 가능성을 위한 구현 가속기**로, ISO/IEC 42001에 정렬된 AI 관리 시스템(AIMS)을 지원하고 감사 가능한 증거를 구조화하는 데 사용할 수 있습니다. ISO/IEC 42001 또는 기타 관리 시스템 표준을 **대체하지 않으며**; 분류체계, Evidence Bundle 구조, Coverage Map을 추가하여 해당 통제의 운영화 및 증거화를 지원합니다.

**AIMO가 제공하는 것**

- AI 거버넌스 분류를 위한 분류체계 및 코드 체계
- Evidence Bundle 구조(manifest, object_index, payload_index, 무결성)
- 추적 가능성을 위한 검증기 및 Coverage Map
- 적합성 수준(Foundation, Operational, Audit-Ready) — 증거 패키징을 위한 AIMO 전용 성숙도 단계

**AIMO가 제공하지 않는 것**

- 법적 자문
- ISO 인증 또는 인증 대체
- 규제 준수 보장
- 감사인 판단 또는 인정 인증 기관의 대체

**왜 지금인가**

- **ISO/IEC 42006**(2025-07 발행)은 ISO/IEC 42001에 따른 AI 관리 시스템의 감사 및 인증을 수행하는 기관에 대한 요구사항을 규정하여 감사 가능한 증거 및 추적 가능성에 대한 기대를 높입니다.
- **EU AI Act**는 단계적 적용 중(2025–2027); 공보에 게시된 조화 표준은 적합성 추정을 제공합니다. EU AI Office는 2026년 동안 실무 가이드라인(고위험 분류, 제50조 투명성, 사고, QMS 요소) 준비를 진행 중입니다.
- 채택자와 인증 기관이 AI 거버넌스의 시스템 계층으로 ISO/IEC 42001을 점점 더 사용하고 있으며, AIMO는 인증을 주장하지 않고 해당 계층을 지원하는 증거 구조화를 돕습니다.

## 참고 자료

- [ISO/IEC 42006](https://www.iso.org/standard/42006) — AI 관리 시스템 감사 및 인증 기관 요구사항
- [EU AI Act 시행 일정](https://artificialintelligenceact.eu/implementation-timeline)(AI Act Service Desk / 위원회 정렬; 참고)
- [European Commission — Clear guidelines for AI (2025년 12월 4일)](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_xxxx) — AI Office 가이드라인 준비(현재 URL은 위원회 뉴스 확인)
- [EPRS — EU AI Act implementation timeline (2025년 6월)](https://www.europarl.europa.eu/thinktank/en/document/EPRS_BRI) — 의회 브리핑(참고)
