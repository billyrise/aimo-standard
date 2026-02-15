---
description: AIMO SEO 및 정식 URL 정책 - 검색 엔진, 감사자 및 외부 참조를 위한 URL 정식화 전략.
---
<!-- aimo:translation_status=translated -->

# SEO 및 정식 URL 정책

이 페이지는 AIMO 표준이 검색 엔진, 감사자 및 외부 참조를 위해 URL 정식화를 관리하는 방법을 문서화합니다.

## 프로덕션 vs 미러 사이트

| 환경 | URL | 역할 | 색인 가능 |
|-------------|-----|------|-----------|
| **프로덕션** | `https://standard.aimoaas.com/` | 모든 목적의 정식 사이트 | 예 |
| GitHub Pages | `https://billyrise.github.io/aimo-standard/` | 임시 미러 / CI 미리보기 | 아니요 (noindex) |

**핵심 원칙**: 프로덕션(`standard.aimoaas.com`)이 권위 있는 URL입니다. GitHub Pages는 임시 백업/미러 역할을 하며 감사 보고서나 외부 참조에 인용되어서는 안 됩니다.

## 정식 URL 전략

### 정식 URL 생성 방법

AIMO 표준은 다음 구성으로 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)을 사용합니다:

```yaml
# mkdocs.yml
site_url: https://standard.aimoaas.com/
```

이 `site_url` 설정은 다음을 보장합니다:

1. **`<link rel="canonical">`** — 생성된 각 HTML 페이지에 프로덕션 URL을 가리키는 정식 링크가 포함됩니다.
2. **`sitemap.xml`** — 사이트맵의 모든 URL이 프로덕션을 참조합니다.
3. **`robots.txt`** — 사이트맵 참조가 프로덕션을 가리킵니다.
4. **`hreflang` 대체** — 언어 대체가 프로덕션 URL을 사용합니다.

### 언어별 정식 URL

| 언어 | URL 패턴 | 예시 |
|----------|-------------|---------|
| 영어 (기본) | `https://standard.aimoaas.com/{X.Y.Z}/{path}` | `https://standard.aimoaas.com/{X.Y.Z}/governance/` |
| 일본어 | `https://standard.aimoaas.com/{X.Y.Z}/ja/{path}` | `https://standard.aimoaas.com/{X.Y.Z}/ja/governance/` |

각 언어 버전은 자체 정식이며 다른 언어에 대한 `hreflang` 대체와 영어 버전을 가리키는 `x-default`를 포함합니다.

### 버전화된 문서와 정식 URL

AIMO 표준은 `alias_type: redirect`로 문서 버전화를 위해 [mike](https://github.com/jimporter/mike)를 사용합니다:

| 버전 | URL 패턴 | 정식 상태 | 색인 가능 |
|---------|-------------|------------------|-----------|
| 버전화됨 (예: `0.0.1`) | `https://standard.aimoaas.com/0.0.1/` | 해당 특정 버전의 정식 | 예 |
| `latest` (별칭) | `https://standard.aimoaas.com/latest/` | 현재 릴리스로 **리디렉션** | 예 (대상을 통해) |
| `dev` | `https://standard.aimoaas.com/dev/` | 미리보기 전용 | **아니요** (noindex 강제) |

**중요한 구분:**

| 측면 | `/X.Y.Z/` | `/latest/` | `/dev/` |
|--------|-----------|------------|---------|
| 내용 | 고정된 스냅샷 | `/X.Y.Z/`로 리디렉션 | main 브랜치 미리보기 |
| 변경 가능 | 절대 안 됨 | 릴리스 시 포인터 업데이트 | 지속적 |
| 감사용 | **예 (선호)** | 예 (고정으로 해결) | **절대 안 됨** |
| SEO | 색인됨 | 대상을 통해 색인 | noindex |

**alias_type: redirect 작동 방식:**

파일을 복사하는 대신 `/latest/`에는 현재 릴리스를 가리키는 리디렉션 페이지가 포함됩니다:

```html
<!-- /latest/index.html -->
<!-- Latest alias (redirect stub); canonical points to versioned snapshot -->
<meta http-equiv="refresh" content="0; url=../{X.Y.Z}/">
<link rel="canonical" href="https://standard.aimoaas.com/{X.Y.Z}/">
```

이것은 다음을 보장합니다:

1. **내용 드리프트 없음** — `/latest/`가 가리키는 릴리스에서 분기될 수 없습니다.
2. **중복 콘텐츠 없음** — 검색 엔진은 하나의 정식 소스를 봅니다.
3. **원자적 업데이트** — 별칭 변경이 모든 페이지를 한 번에 업데이트합니다.

!!! info "Git 태그 vs. 사이트 경로"
    Git 릴리스 태그는 `v` 접두사를 사용하지만 (예: `v0.0.1`), 사이트 경로는 `v`를 생략합니다 (예: `/0.0.1/`). 이것은 mike와 같은 문서 버전화 도구의 표준 관행입니다.

## 감사자 지침: 인용할 URL

감사 보고서, 컴플라이언스 문서 또는 외부 참조에서 AIMO 표준을 인용할 때:

### 권장 인용 URL

| 사용 사례 | 권장 URL |
|----------|-----------------|
| 현재 안정 사양 | `https://standard.aimoaas.com/{X.Y.Z}/standard/current/` |
| 특정 버전 (감사용) | `https://standard.aimoaas.com/{X.Y.Z}/standard/current/` |
| 거버넌스 및 정책 | `https://standard.aimoaas.com/{X.Y.Z}/governance/` |
| 신뢰 패키지 | `https://standard.aimoaas.com/{X.Y.Z}/governance/trust-package/` |

### 인용하지 말아야 할 것

- ~~`https://billyrise.github.io/aimo-standard/`~~ — 임시 미러, 정식 아님
- ~~`https://standard.aimoaas.com/dev/`~~ — 개발 버전, 변경될 수 있음

### 불변성을 위한 버전화된 인용

불변 참조가 필요한 공식 감사의 경우 버전화된 스냅샷 URL을 사용하세요:

```
https://standard.aimoaas.com/1.0.0/standard/current/01-overview/
```

버전화된 스냅샷은 릴리스 시점에 고정되며 변경되지 않습니다.

!!! note "URL 형식"
    사이트 경로는 `v` 접두사 없이 버전 번호를 사용합니다. 버전 `v1.0.0`의 경우 URL에서 `/1.0.0/`을 사용하세요.

## 기술 구현

### 생성된 HTML 예시

생성된 모든 HTML 페이지는 `<head>`에 정식 및 hreflang 태그를 포함합니다:

```html
<!-- 정식 (항상 프로덕션을 가리킴) -->
<link rel="canonical" href="https://standard.aimoaas.com/{X.Y.Z}/governance/">

<!-- 언어 대체 -->
<link rel="alternate" hreflang="en" href="https://standard.aimoaas.com/{X.Y.Z}/governance/">
<link rel="alternate" hreflang="ja" href="https://standard.aimoaas.com/{X.Y.Z}/ja/governance/">
<link rel="alternate" hreflang="x-default" href="https://standard.aimoaas.com/{X.Y.Z}/governance/">
```

### robots.txt

```
User-agent: *
Allow: /

Sitemap: https://standard.aimoaas.com/sitemap.xml
```

### 사이트맵

사이트맵은 `mkdocs-static-i18n` 플러그인에 의해 생성되며 다음을 포함합니다:

- 모든 프로덕션 URL
- 각 언어에 대한 `hreflang` 대체

## Noindex 구성

### `/dev/` (미리보기) — 필수 Noindex

`/dev/` 버전은 릴리스되지 않은 콘텐츠를 포함하며 다음을 방지하기 위해 noindex가 반드시 있어야 합니다:

- 검색 엔진이 불안정한 콘텐츠를 색인
- 사용자가 검색을 통해 `/dev/`를 찾고 감사에 인용
- 릴리스된 콘텐츠와 릴리스되지 않은 콘텐츠 간의 혼동

**구현:**

`deploy-dev.yml` 워크플로우는 테마 오버라이드를 통해 모든 `/dev/` 페이지에 noindex 메타 태그를 삽입합니다:

```html
<!-- /dev/ 페이지에만 삽입 -->
<meta name="robots" content="noindex, nofollow">
```

### GitHub Pages 미러 — Noindex

GitHub Pages (미러 사이트 `billyrise.github.io`)에 배포할 때 중복 색인을 방지하기 위해 모든 페이지에 noindex가 있어야 합니다:

```html
<meta name="robots" content="noindex, nofollow">
```

이것은 검색 엔진이 항상 `standard.aimoaas.com`의 프로덕션 정식 URL을 우선시하도록 보장합니다.

## 검증

각 빌드 후 다음을 통해 정식 URL을 확인할 수 있습니다:

1. **생성된 HTML 검사** — `mkdocs build` 후 `site/` 디렉토리 확인
2. **브라우저 DevTools 사용** — 배포된 페이지의 `<head>` 섹션 검사
3. **Google Search Console** — 어떤 URL이 색인되는지 모니터링

예시 검증 명령:

```bash
mkdocs build
grep -r 'rel="canonical"' site/ | head -5
```

예상 출력은 프로덕션 URL을 표시해야 합니다, 예:

```
site/index.html:<link rel="canonical" href="https://standard.aimoaas.com/">
site/governance/index.html:<link rel="canonical" href="https://standard.aimoaas.com/governance/">
```

## 관련 문서

- [신뢰 패키지](../trust-package/) — 감사자 준비 자료
- [릴리스](../../releases/) — 버전 이력 및 변경로그
- [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) — 버전 정책
