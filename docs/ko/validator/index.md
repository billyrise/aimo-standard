---
description: AIMO 검증기 허브 - 검증 도구 빠른 시작. 30초 안에 설치, 실행 및 결과 해석. 증거 팩 검증 및 컴플라이언스 검사.
---
<!-- aimo:translation_status=translated -->

# 검증기

이 페이지는 검증 도구 및 규칙의 허브입니다. 검증기와 그 규칙에 대한 규범적 사양은 표준에 있습니다.

## 빠른 시작 (30초)

**1. 전제 조건**

```bash
pip install jsonschema   # 아직 설치되지 않은 경우
```

**2. 샘플 번들에 대해 검증 실행**

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

**3. 보고서 읽기 및 오류/경고 수정**

예시 출력 (성공):

```
OK
```

예시 출력 (실패):

```
Schema validation failed:
<root>: 'version' is a required property
<root>: 'dictionary' is a required property
<root>: 'evidence' is a required property
```

종료 코드: `0` = 성공, `1` = 검증 오류, `2` = 사용 오류.

---

## 확인하는 것

- **스키마 검증**: 루트 객체, 딕셔너리 및 증거가 JSON Schema에 부합
- **딕셔너리 일관성**: 모든 코드가 분류체계 딕셔너리에 존재
- **코드 상태**: 더 이상 사용되지 않는 코드에 대해 경고, 제거된 코드에 대해 오류

## 확인하지 않는 것

- **내용 정확성**: 검증기는 구조를 확인하며, 의미가 아님
- **컴플라이언스 보장**: 검증 통과가 규제 컴플라이언스를 보장하지 않음
- **인간 판단**: 맥락 의존적 결정은 인간 검토가 필요 ([인간 감독 프로토콜](../governance/human-oversight-protocol/) 참조)
- **자동 로그 수집**: 검증기는 제출된 증거를 검증하며; 로그를 수집하지 않음

---

## 리소스

- **사양**: [표준 > 현재 > 검증기](../standard/current/07-validator/) — 규칙, 참조 검사 및 검증이 증거와 어떻게 관련되는지.
- **규칙 및 구현**: 저장소 `validator/rules/` (검사), `validator/src/` (참조 구현). 실행 및 CI 사용은 사양에 설명되어 있습니다.
- **해석**: 감사자에게 검증 "실패"가 의미하는 것 (사양에서 설명됨).

적합성 및 산출물 사용에 대해서는 [적합성](../conformance/) 및 [산출물](../artifacts/)을 참조하세요.
