---
description: AIMO 표준과 NIST AI RMF 매핑. AIMO 분류체계 코드와 NIST AI 리스크 관리 프레임워크 기능 간의 추적성.
---
<!-- aimo:translation_status=translated -->

# NIST AI RMF 매핑

!!! note "1차 출처"
    **NIST AI Risk Management Framework (AI RMF 1.0)** — [NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework)(공식 NIST 출판물 및 자료). 매핑 및 적용 가능성은 이 1차 출처와 대조하여 확인하세요.

> 추적성 바로가기: 분류체계 → 최소 증거 → 검증기 → 인간 감독 프로토콜.

- [분류체계](../../standard/current/03-taxonomy/)
- [최소 증거 요구사항](../../artifacts/minimum-evidence/)
- [로그 스키마](../../artifacts/log-schemas/)
- [검증기](../../validator/)
- [인간 감독 프로토콜](../../governance/human-oversight-protocol/)

이 페이지는 선택된 NIST AI 리스크 관리 프레임워크(Govern, Map, Measure, Manage) 주제를 AIMO 증거 및 산출물에 매핑합니다. 이것은 설명 가능성을 위한 것이며; NIST AI RMF 적합성을 보장하지 않습니다. [NIST AI RMF 1.0 출판물](https://www.nist.gov/itl/ai-risk-management-framework)과 대조하여 확인하세요.


## 매핑 테이블

| 프레임워크 참조 / 주제 | AIMO 증거 / AIMO 내 위치 | 증거 번들 / 최소 증거 | 산출물 및 검증 | 참고사항 |
| --- | --- | --- | --- | --- |
| Govern 1.1 – 정책 | [범위](../../standard/current/02-scope/), [분류체계](../../standard/current/03-taxonomy/) | Dictionary, Summary, review; review | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | 참고용; NIST 출판물과 대조 확인. |
| Govern 1.2 – 역할 및 책임 | [최소 증거](../../artifacts/minimum-evidence/) | request, review | templates/ev/ev_template.md | 참고용; NIST 출판물과 대조 확인. |
| Govern 2.1 – 책임성 | [증거 번들](../../artifacts/evidence-bundle/) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | 참고용; NIST 출판물과 대조 확인. |
| Govern 3.1 – 리스크 관리 | [범위](../../standard/current/02-scope/) | request, review, exception | templates/ev/ | 참고용; NIST 출판물과 대조 확인. |
| Govern 4.1 – 문화 | [개요](../../standard/current/01-overview/) | Summary, review; review | — | 참고용; NIST 출판물과 대조 확인. |
| Map 1.1 – 맥락 매핑 | [범위](../../standard/current/02-scope/), [딕셔너리](../../standard/current/05-dictionary/) | Dictionary, Summary; request | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | 참고용; NIST 출판물과 대조 확인. |
| Map 2.1 – 데이터 및 문서화 | [EV 템플릿](../../standard/current/06-ev-template/) | EV, Dictionary, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | 참고용; NIST 출판물과 대조 확인. |
| Map 3.1 – 데이터 거버넌스 | [딕셔너리](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | 참고용; NIST 출판물과 대조 확인. |
| Measure 1.1 – 성능 및 영향 | [EV 템플릿](../../standard/current/06-ev-template/) | EV | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | 참고용; NIST 출판물과 대조 확인. |
| Measure 2.1 – 모니터링 | [최소 증거](../../artifacts/minimum-evidence/) | EV, change_log; change_log, integrity | templates/ev/ | 참고용; NIST 출판물과 대조 확인. |
| Measure 3.1 – 테스트 및 검증 | [검증기](../../standard/current/07-validator/) | EV | validator/rules/, validator/src/; schema_validate_ev | 참고용; NIST 출판물과 대조 확인. |
| Manage 1.1 – 자원 할당 | [개요](../../standard/current/01-overview/) | Summary, review; review | — | 참고용; NIST 출판물과 대조 확인. |
| Manage 2.1 – 인시던트 및 대응 | [최소 증거](../../artifacts/minimum-evidence/) | exception, renewal, change_log | templates/ev/ev_template.md | 참고용; NIST 출판물과 대조 확인. |
| Manage 3.1 – 변경 관리 | [증거 번들](../../artifacts/evidence-bundle/) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | 참고용; NIST 출판물과 대조 확인. |
| Manage 4.1 – 검토 및 업데이트 | [최소 증거](../../artifacts/minimum-evidence/) | renewal, review; review, renewal | templates/ev/ | 참고용; NIST 출판물과 대조 확인. |
| Manage 5.1 – 커뮤니케이션 | [증거 번들](../../artifacts/evidence-bundle/) | Summary, change_log; change_log | templates/ev/ | 참고용; NIST 출판물과 대조 확인. |
