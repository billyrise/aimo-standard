---
description: AIMO 표준과 EU AI Act 매핑. AIMO 분류체계 코드와 EU AI Act 리스크 범주 및 요구사항 간의 추적성.
---

# EU AI Act 매핑

> 추적성 바로가기: 분류체계 → 최소 증거 → 검증기 → 인간 감독 프로토콜.

- [분류체계](../standard/current/03-taxonomy.md)
- [최소 증거 요구사항](../artifacts/minimum-evidence.md)
- [로그 스키마](../artifacts/log-schemas/index.md)
- [검증기](../validator/index.md)
- [인간 감독 프로토콜](../governance/human-oversight-protocol.md)

이 페이지는 선택된 EU AI Act 주제(문서화, 기록 보존, 리스크 관리, 인간 감독, 투명성)를 AIMO 증거 및 산출물에 매핑합니다. 이것은 고수준 개요일 뿐이며 법률 자문을 구성하거나 적합성을 보장하지 **않습니다**. 공식 법률 문서와 대조하여 확인하세요.


## 매핑 테이블

| 프레임워크 참조 / 주제 | AIMO 증거 / AIMO 내 위치 | 증거 번들 / 최소 증거 | 산출물 및 검증 | 참고사항 |
| --- | --- | --- | --- | --- |
| Art 9 – 리스크 관리 (의무) | [범위](../standard/current/02-scope.md) | request, review, exception | templates/ev/ | 고수준 개요; 법률 자문 아님. 공식 문서와 대조 확인. |
| Art 10 – 데이터 거버넌스 | [딕셔너리](../standard/current/05-dictionary.md) | Dictionary, EV | schemas/jsonschema/; schema_validate_dictionary | 고수준 개요; 법률 자문 아님. 공식 문서와 대조 확인. |
| Art 11 – 문서화 (고위험) | [EV 템플릿](../standard/current/06-ev-template.md), [증거 번들](../artifacts/evidence-bundle.md) | EV, Dictionary, Summary; request, review | schemas/jsonschema/, templates/ev/; schema_validate_ev | 고수준 개요; 법률 자문 아님. 공식 문서와 대조 확인. |
| Art 12 – 기록 보존 | [증거 번들](../artifacts/evidence-bundle.md), [최소 증거](../artifacts/minimum-evidence.md) | EV, change_log, request, review | examples/evidence_bundle_minimal/; schema_validate_ev | 고수준 개요; 법률 자문 아님. 공식 문서와 대조 확인. |
| Art 13 – 투명성 (사용자 정보) | [범위](../standard/current/02-scope.md) | Summary, EV; review | templates/ev/ | 고수준 개요; 법률 자문 아님. 공식 문서와 대조 확인. |
| Art 14 – 인간 감독 | [최소 증거](../artifacts/minimum-evidence.md) | review, exception; review, exception | templates/ev/ev_template.md | 고수준 개요; 법률 자문 아님. 공식 문서와 대조 확인. |
| Art 17 – 리스크 관리 (고위험) | [범위](../standard/current/02-scope.md) | request, review, exception, renewal | templates/ev/ | 고수준 개요; 법률 자문 아님. 공식 문서와 대조 확인. |
| Art 26 – 투명성 (제한된 리스크) | [범위](../standard/current/02-scope.md) | Summary, EV; review | templates/ev/ | 고수준 개요; 법률 자문 아님. 공식 문서와 대조 확인. |
| Art 29 – 문서화 (범용 AI) | [EV 템플릿](../standard/current/06-ev-template.md) | EV, Dictionary, Summary; request, review | schemas/jsonschema/; schema_validate_ev | 고수준 개요; 법률 자문 아님. 공식 문서와 대조 확인. |
| Art 52 – 투명성 (배포자) | [최소 증거](../artifacts/minimum-evidence.md) | EV, Summary; review | templates/ev/ | 고수준 개요; 법률 자문 아님. 공식 문서와 대조 확인. |
| 서문 – 책임성 | [증거 번들](../artifacts/evidence-bundle.md) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | 고수준 개요; 법률 자문 아님. 공식 문서와 대조 확인. |
