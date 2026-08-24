# AI Tech Study

AI 최신 기술동향을 꾸준히 따라가기 위한 개인 스터디 저장소입니다. 이 저장소는 "지금의 판단", "그때의 기록", "주제별 누적 지식", "읽은 자료"를 분리해서 관리합니다.

## 운영 원칙

1. 지금의 판단은 `CURRENT.md`에만 적습니다.
2. 과거 판단은 지우지 않고 `timeline/`에 남깁니다.
3. 자료는 읽을 때마다 `sources/`에 바로 기록합니다.
4. 주제는 처음에는 `topics/*.md` 파일로 시작하고, 커지면 폴더로 승격합니다.
5. 고정 리듬은 월간 리뷰 하나로 유지합니다.

## 구조

```text
AI-tech/
  README.md
  CLAUDE.md
  AUTOMATION.md
  CURRENT.md
  timeline/
    2026-07.md
  topics/
    agents/
      agents.md
      agent-loop.md
    llm-pipeline/
      llm-pipeline.md
      preprocessing.md
      postprocessing.md
    models.md
    clinical-healthcare.md
    evals-benchmarks.md
    safety-governance.md
    infra-cost.md
    korea.md
    open-source.md
  sources/
    README.md
    2026-07/
      2026-07-09.md
  scripts/
    check-promotion-candidates.py
  templates/
    daily-sources.md
    source-note.md
    monthly-review.md
```

## 어디에 쓰나

`CURRENT.md`
: 최신 요약, 기술 레이더, watchlist, 열린 질문을 한 곳에서 관리합니다.

`timeline/YYYY-MM.md`
: 해당 월에 어떤 일이 있었고, 그때 어떤 판단을 했는지 기록합니다.

`topics/*.md`
: 모델, 에이전트, 헬스케어/임상 데이터처럼 반복해서 보는 주제의 누적 정리입니다.

`sources/YYYY-MM/YYYY-MM-DD.md`
: 그날 읽은 논문, 제품 릴리스, 블로그, 벤치마크, 규제 문서 등 원자료를 하나의 일일 로그로 요약합니다. 각 자료의 유형과 주제는 해당 source entry의 `type`, `topics` 항목에 적습니다.

`templates/`
: 반복해서 쓰는 문서의 템플릿입니다.

## 파일 이름 규칙

소스 노트는 월 폴더 아래 날짜 파일로 씁니다.

```text
sources/2026-07/2026-07-09.md
sources/2026-08/2026-08-01.md
```

월간 리뷰는 월 단위로 씁니다.

```text
timeline/2026-07.md
```

## 리뷰 리듬

자료를 읽을 때마다 해당 날짜의 `sources/YYYY-MM/YYYY-MM-DD.md`에 source entry로 짧게 남깁니다.

월말에는 `templates/monthly-review.md`를 복사해 `timeline/YYYY-MM.md`를 갱신하고, 마지막 5분 동안 `CURRENT.md`를 업데이트합니다.

## 주제 파일 승격 기준

`topics/models.md` 같은 파일이 너무 길어지거나 하위 분류가 반복해서 필요해지면 폴더로 승격합니다.

승격은 자동으로 실행되지 않습니다. 기준에 도달하면 월간 리뷰 때 구조 변경 후보로 보고, 사람이 판단해서 나눕니다. 승격할 때는 기존 주제 파일을 같은 이름의 폴더 안으로 옮겨(예: `topics/agents.md` → `topics/agents/agents.md`) 그 폴더의 허브 파일이 되게 하고, 허브에는 요약과 목차만 남긴 뒤 세부 내용을 하위 파일로 분리하는 것을 기본 원칙으로 합니다.

승격 후보로 보는 기준은 다음과 같습니다.

- 주제 파일이 300줄 이상입니다.
- 주제 파일 안의 2~3단계 제목이 12개 이상입니다.
- 같은 topic을 참조하는 source entry가 30개 이상입니다.
- `sources/` 바로 아래에 예전 방식의 낱개 source 파일이 100개 이상입니다.
- 특정 월의 source entry가 30개 이상입니다.
- 특정 날짜 파일이 20개 이상의 source entry 또는 500줄 이상으로 커집니다.

```text
topics/models.md
```

가 커지면 다음처럼 같은 이름의 폴더로 옮기고 하위 파일을 추가합니다.

```text
topics/
  models/
    models.md
    <subtopic-a>.md
    <subtopic-b>.md
```

실제 예시는 `topics/agents/`와 `topics/llm-pipeline/`입니다.

```text
topics/
  agents/
    agents.md
    agent-loop.md
  llm-pipeline/
    llm-pipeline.md
    preprocessing.md
    postprocessing.md
```

허브 파일(`topics/agents/agents.md`, `topics/llm-pipeline/llm-pipeline.md`)에는 현재 판단, 목차, 대표 소스만 남기고 세부 내용은 하위 파일로 옮깁니다.

## 승격 후보 점검

다음 명령으로 승격 후보를 확인합니다.

```bash
python3 scripts/check-promotion-candidates.py
```

이 스크립트는 파일을 옮기거나 수정하지 않고 후보만 출력합니다. 기준을 바꾸고 싶으면 옵션을 사용합니다.

```bash
python3 scripts/check-promotion-candidates.py --topic-lines 250 --topic-sources 20 --daily-source-entries 15
```

CI나 자동 점검에서 후보가 있을 때 실패로 처리하고 싶으면 `--strict`를 붙입니다.

```bash
python3 scripts/check-promotion-candidates.py --strict
```
