---
description: AIMO 현지화 가이드 - 다국어 문서를 위한 i18n 구조, 유지보수 워크플로우 및 SSOT 원칙.
---
<!-- aimo:translation_status=translated -->

# 현지화 가이드

이 페이지는 AIMO 표준 문서의 현지화(i18n) 구조, 유지보수 워크플로우 및 SSOT(단일 진실 공급원) 원칙을 문서화합니다.

## 언어 순수성 정책

**각 언어 페이지는 해당 언어의 콘텐츠만 포함해야 합니다.**

| 규칙 | 설명 |
| --- | --- |
| **EN 페이지** | CJK 문자 또는 언어별 열 참조(예: `_ja` 접미사)를 포함하면 안 됨 |
| **JA 페이지** | EN 특정 용어를 정식 구조인 것처럼 설명하면 안 됨 |
| **예외** | `tooling/checks/lint_i18n.py`의 `MIXED_LANGUAGE_ALLOWLIST`에 나열됨 |

이 정책은 다음을 보장합니다:
1. 독자는 선택한 언어만 볼 수 있음
2. 새 언어 추가 시 기존 페이지 업데이트가 필요 없음
3. CI가 자동으로 위반 감지 가능

## 언어 구조

AIMO 표준 문서는 **폴더 기반 i18n 구조**를 사용합니다:

```
docs/
├── en/           # 영어 (정본)
├── ja/           # 일본어 (日本語)
├── es/           # 스페인어 (Español)
├── fr/           # 프랑스어 (Français)
├── de/           # 독일어 (Deutsch)
├── pt/           # 포르투갈어 (Português)
├── it/           # 이탈리아어 (Italiano)
├── zh/           # 간체 중국어 (简体中文)
├── zh-TW/        # 번체 중국어 (繁體中文)
└── ko/           # 한국어 (한국어)
```

- **영어가 정본**: `docs/en/` 폴더가 문서 콘텐츠의 권위 있는 소스입니다.
- **다른 언어는 구조를 미러링**: 각 언어 폴더(`ja/` 등)는 `en/`과 동일한 파일 구조를 유지합니다.
- **동일한 파일 이름**: 모든 언어는 `.md` 확장자를 사용합니다(파일 이름에 언어 접미사 없음).
- **영어로 폴백**: 번역이 없는 경우 자동으로 영어 콘텐츠로 폴백됩니다.

## 분류체계 데이터 모델

분류체계는 별도의 번역 팩과 함께 **언어 중립적 정본 구조**를 사용합니다:

```
data/
└── taxonomy/
    ├── canonical.yaml           # 언어 중립 (코드, 상태, 생명주기)
    └── i18n/
        ├── en.yaml              # 영어 레이블 및 정의
        ├── ja.yaml              # 일본어 레이블 및 정의
        └── {lang}.yaml          # 추가 언어 (빈 템플릿)
```

### 정본 구조 (`canonical.yaml`)

언어 중립 데이터를 포함합니다:

- 코드 식별자 (예: `FS-001`, `UC-001`)
- 상태 (`active`, `deprecated`, `removed`)
- 생명주기 메타데이터 (`introduced_in`, `deprecated_in`, `removed_in`, `replaced_by`)
- 범위 노트 및 예시 (기술적 참조로서 영어로)

### 번역 팩 (`i18n/*.yaml`)

각 언어 팩에 포함된 내용:

- 차원 이름 (예: "Functional Scope")
- 코드 레이블 (예: "End-user Productivity")
- 코드 정의

**폴백**: 번역이 없는 경우 시스템은 영어를 사용합니다.

## SSOT 원칙

AIMO는 분류체계 데이터에 **SSOT 우선 아키텍처**를 사용합니다:

| 자산 유형 | SSOT 위치 | 설명 |
| --- | --- | --- |
| **분류체계 (구조)** | `data/taxonomy/canonical.yaml` | 언어 중립 구조 (SSOT) |
| **분류체계 (i18n)** | `data/taxonomy/i18n/*.yaml` | 언어별 번역 (SSOT) |
| **커버리지 맵** | `coverage_map/coverage_map.yaml` | 프레임워크-증거 매핑 |
| **스키마** | `schemas/jsonschema/` | JSON 검증 스키마 |

### 파생 파일

다음 파일들은 SSOT에서 **생성**되며 수동으로 편집하면 안 됩니다:

| 파일 | 생성 소스 | 생성기 |
| --- | --- | --- |
| `artifacts/taxonomy/{version}/{lang}/taxonomy_dictionary.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_en.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_ja.yaml` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/code_system.csv` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/dimensions_en_ja.md` | canonical + i18n | `build_artifacts.py` |
| `source_pack/03_taxonomy/taxonomy_dictionary.json` | canonical + i18n | `build_artifacts.py` |

### 언어 코드 (BCP47)

AIMO는 BCP47 언어 코드를 사용합니다:

| 코드 | 언어 | 상태 |
| --- | --- | --- |
| `en` | 영어 | 정본 (소스) |
| `ja` | 일본어 (日本語) | 활성 |
| `es` | 스페인어 (Español) | 활성 |
| `fr` | 프랑스어 (Français) | 활성 |
| `de` | 독일어 (Deutsch) | 활성 |
| `pt` | 포르투갈어 (Português) | 활성 |
| `it` | 이탈리아어 (Italiano) | 활성 |
| `zh` | 간체 중국어 (简体中文) | 활성 |
| `zh-TW` | 번체 중국어 (繁體中文) | 활성 |
| `ko` | 한국어 (한국어) | 활성 |

### 레거시 CSV 파일 (동결)

`source_pack/03_taxonomy/legacy/`의 레거시 EN/JA 혼합 CSV 파일은:

- **21개 열로 동결** — 새 언어 열은 추가되지 않음
- **이전 호환성 유지** — 기존 통합은 계속 사용 가능
- **CI 강제** — `label_es`, `definition_de` 등 추가 시 빌드 실패

새 언어의 경우 `artifacts/taxonomy/{version}/{lang}/`의 언어별 산출물을 사용하세요.

## 번역 최신성 추적

AIMO는 영어(소스)와 번역된 콘텐츠 간의 일관성을 유지하기 위해 **번역 최신성 추적** 시스템을 사용합니다.

### 작동 방식

1. 각 번역 파일에는 어떤 영어 소스 버전에서 번역되었는지 추적하는 메타데이터가 포함됨
2. 영어 콘텐츠가 업데이트되면 시스템이 오래된 번역을 감지
3. CI가 오래된 번역에 대해 경고하지만 차단하지 않음 (번역은 뒤처질 수 있음)

### 번역 메타데이터

번역 파일에는 프론트매터 메타데이터가 포함됩니다:

```yaml
---
# TRANSLATION METADATA - DO NOT REMOVE
source_file: en/standard/current/01-overview.md
source_hash: abc123def456
translation_date: 2026-02-02
translator: human|machine|hybrid
translation_status: current|outdated|needs_review
---
```

### 동기화 도구 사용

```bash
# 모든 번역의 최신성 확인
python tooling/i18n/sync_translations.py --check

# 특정 언어 확인
python tooling/i18n/sync_translations.py --check --lang ja

# 번역 보고서 생성
python tooling/i18n/sync_translations.py --report

# 새 언어 초기화 (EN을 기본으로 복사)
python tooling/i18n/sync_translations.py --init-lang es

# 번역 완료 후 메타데이터 업데이트
python tooling/i18n/sync_translations.py --update-meta docs/ja/index.md
```

자세한 기술 사양은 `tooling/i18n/TRANSLATION_SYNC_SPEC.md`를 참조하세요.

## 업데이트 워크플로우

### 분류체계 업데이트 (새 SSOT 우선 워크플로우)

1. `data/taxonomy/`의 SSOT 편집:
   - 구조 변경 → `canonical.yaml`
   - 영어 번역 → `i18n/en.yaml`
   - 일본어 번역 → `i18n/ja.yaml`
2. 검증 실행: `python tooling/checks/lint_taxonomy_ssot.py`
3. 모든 파생 파일 재생성: `python tooling/taxonomy/build_artifacts.py --version current --langs en ja`
4. 필요에 따라 문서 페이지 업데이트
5. 모든 변경 사항을 함께 커밋

### 커버리지 맵 업데이트

1. `coverage_map/coverage_map.yaml` (SSOT) 편집
2. 해당 프레임워크 페이지 테이블 업데이트 (`docs/en/coverage-map/*.md`)
3. 일본어 번역 업데이트 (`docs/ja/coverage-map/*.md`)
4. 모든 변경 사항을 함께 커밋

### 문서 업데이트

1. 영어 소스 편집 (`docs/en/...`)
2. 필요에 따라 번역 업데이트 (또는 나중 업데이트를 위해 표시)
3. `python tooling/i18n/sync_translations.py --check`를 실행하여 오래된 번역 확인
4. `python tooling/checks/lint_i18n.py`를 실행하여 제목 일관성 확인
5. `mkdocs build --strict`를 실행하여 빌드 확인
6. 모든 변경 사항을 함께 커밋

!!! note "번역 우선순위"
    모든 번역이 즉시 업데이트될 필요는 없습니다. Tier 1 (중요) 페이지를 우선시해야 합니다:
    
    - `index.md`
    - `standard/current/*.md`
    - `governance/index.md`
    - `releases/`

## 새 언어 추가 (5단계)

새 언어를 추가하려면 (예: 스페인어):

### 1단계: 분류체계 팩 생성

```bash
python tooling/taxonomy/build_i18n_taxonomy.py --add-lang es --lang-name "Español"
```

`data/taxonomy/i18n/es.yaml`을 영어 참조를 주석으로 포함하여 생성합니다.

### 2단계: 문서 폴더 생성

```bash
mkdir -p docs/es && cp -r docs/en/* docs/es/
```

### 3단계: mkdocs.yml 업데이트

```yaml
plugins:
  - i18n:
      languages:
        - locale: es
          name: Español
          build: true
```

### 4단계: 번역

- `data/taxonomy/i18n/es.yaml` 번역
- `docs/es/`의 파일 번역

### 5단계: 확인

```bash
python tooling/checks/lint_i18n.py && mkdocs build --strict
```

!!! success "완료"
    새 언어는 이제 `/dev/es/`에서 사용 가능합니다

## 파일 명명 규칙

| 패턴 | 예시 | 설명 |
| --- | --- | --- |
| `index.md` | `docs/en/governance/index.md` | 섹션 랜딩 페이지 |
| `{topic}.md` | `docs/en/governance/trust-package.md` | 주제 페이지 |
| `{NN}-{topic}.md` | `docs/en/standard/current/03-taxonomy.md` | 번호가 매겨진 사양 페이지 |

## 품질 검사

커밋 전에 다음 검사를 실행하세요:

```bash
# i18n 구조, 제목 일관성 및 더 이상 사용되지 않는 문구 감지
python tooling/checks/lint_i18n.py

# 스키마 및 매니페스트 린트
python tooling/checks/lint_schema.py
python tooling/checks/lint_manifest.py

# 분류체계 SSOT 린트
python tooling/checks/lint_taxonomy_ssot.py --required-langs en
python tooling/checks/lint_legacy_csv.py
python tooling/checks/lint_taxonomy_dictionary.py
python tooling/checks/lint_taxonomy_json.py

# 분류체계 산출물 최신 상태
python tooling/taxonomy/build_artifacts.py --check

# 빌드 확인
mkdocs build --strict
```

## 관련 페이지

- [릴리스](../../releases/) — 다운로드 가능 패키지
- [거버넌스](../../governance/) — 프로젝트 거버넌스
