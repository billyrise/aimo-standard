---
description: AIMO 표준과 ISMS (ISO 27001/27002) 매핑. AIMO 분류체계와 정보보안 관리 시스템 통제 간의 추적성.
---

# ISMS 뷰 (ISO/IEC 27001/27002) 매핑

> 추적성 바로가기: 분류체계 → 최소 증거 → 검증기 → 인간 감독 프로토콜.

- [분류체계](../standard/current/03-taxonomy.md)
- [최소 증거 요구사항](../artifacts/minimum-evidence.md)
- [로그 스키마](../artifacts/log-schemas/index.md)
- [검증기](../validator/index.md)
- [인간 감독 프로토콜](../governance/human-oversight-protocol.md)

이 페이지는 선택된 ISO/IEC 27001/27002 주제(변경 관리, 접근 통제, 로깅, 증거 무결성)를 AIMO 증거 및 산출물에 매핑합니다. 이것은 설명 가능성을 위한 것이며; ISO/IEC 27001 또는 27002 적합성을 보장하지 않습니다. 출판된 표준과 대조하여 확인하세요.


## 매핑 테이블

| 프레임워크 참조 / 주제 | AIMO 증거 / AIMO 내 위치 | 증거 번들 / 최소 증거 | 산출물 및 검증 | 참고사항 |
| --- | --- | --- | --- | --- |
| A.5.24 – 프로젝트 관리에서의 정보보안 | [범위](../standard/current/02-scope.md) | request, review | templates/ev/ | 참고용; 공식 문서와 대조 확인. |
| A.5.29 – 중단 시 정보보안 | [최소 증거](../artifacts/minimum-evidence.md) | exception, renewal | templates/ev/ev_template.md | 참고용; 공식 문서와 대조 확인. |
| A.5.30 – 비즈니스 연속성을 위한 ICT 준비 | [개요](../standard/current/01-overview.md) | Summary; integrity | — | 참고용; 공식 문서와 대조 확인. |
| A.8.1 – 자산 인벤토리 | [딕셔너리](../standard/current/05-dictionary.md) | Dictionary, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | 참고용; 공식 문서와 대조 확인. |
| A.8.2 – 정보 분류 | [분류체계](../standard/current/03-taxonomy.md) | Dictionary; review | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | 참고용; 공식 문서와 대조 확인. |
| A.8.3 – 접근 통제 | [최소 증거](../artifacts/minimum-evidence.md) | —; integrity | — | 참고용; 공식 문서와 대조 확인. |
| A.8.15 – 로깅 | [EV 템플릿](../standard/current/06-ev-template.md) | EV, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | 참고용; 공식 문서와 대조 확인. |
| A.8.16 – 모니터링 활동 | [최소 증거](../artifacts/minimum-evidence.md) | EV, change_log; change_log, integrity | templates/ev/ | 참고용; 공식 문서와 대조 확인. |
| A.8.32 – 변경 관리 | [증거 번들](../artifacts/evidence-bundle.md) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | 참고용; 공식 문서와 대조 확인. |
| A.8.33 – 테스트 정보 | [검증기](../standard/current/07-validator.md) | EV | validator/rules/, validator/src/; schema_validate_ev | 참고용; 공식 문서와 대조 확인. |
