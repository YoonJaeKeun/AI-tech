# CLAUDE.md

이 저장소는 AI 기술동향 개인 스터디 노트입니다. 코드 프로젝트가 아니라 마크다운 지식 저장소입니다.
자동화된 클라우드 에이전트와 사람이 함께 쓰므로, 아래 규칙을 반드시 지킵니다.

## 가장 중요한 경계

`CURRENT.md` 는 **사람의 판단**을 적는 곳입니다. 에이전트는 이 파일을 main에 직접 커밋하지 않습니다.
변경이 필요하면 브랜치를 만들어 PR로 제안만 하고, 머지는 사람이 합니다.

나머지(`sources/`, `topics/`, `timeline/`)는 기록이므로 에이전트가 main에 직접 커밋해도 됩니다.

## 문서별 역할

| 경로 | 역할 | 에이전트 쓰기 |
|---|---|---|
| `CURRENT.md` | 지금의 판단, Tech Radar, watchlist, 열린 질문 | PR로만 |
| `timeline/YYYY-MM.md` | 그달에 무슨 일이 있었고 어떤 판단을 했는지 | 직접 커밋 |
| `topics/*.md` | 주제별 누적 정리 | 직접 커밋 |
| `sources/YYYY-MM/YYYY-MM-DD.md` | 그날 읽은 원자료 일일 로그 | 직접 커밋 |
| `templates/` | 문서 템플릿 | 사람만 |
| `scripts/` | 보조 스크립트 | 사람만 |

## 작성 규칙

- 모든 본문은 한국어로 씁니다. 고유명사, 모델명, 벤치마크명은 원문 표기를 유지합니다.
- 새 문서는 반드시 `templates/` 의 해당 템플릿에서 시작하고 frontmatter를 채웁니다.
- 날짜는 항상 `YYYY-MM-DD` 절대 표기를 씁니다. "지난주", "최근" 같은 상대 표현을 쓰지 않습니다.
- source entry의 `topics` 값은 `topics/` 에 실제로 존재하는 슬러그만 씁니다.
  현재 슬러그: `models`, `agents`, `llm-pipeline`, `clinical-healthcare`, `evals-benchmarks`, `safety-governance`.
  새 주제가 필요하면 임의로 만들지 말고 해당 일일 로그의 Daily Summary에 제안만 남깁니다.
- 근거 없는 단정을 쓰지 않습니다. 확실하지 않으면 `confidence: low` 로 표시하고 Limitations에 이유를 적습니다.
- 원문을 열지 못한 채 검색 결과만으로 정리한 자료는 `confidence: low` + `status: unverified` 로 표시하고,
  Limitations 첫 줄에 그 사실을 적습니다. 이런 항목은 topic 문서로 누적하지 않습니다.
- 원문 링크가 없는 항목은 기록하지 않습니다. `source_url` 은 반드시 채웁니다.
- 기존 내용을 덮어쓰지 않습니다. 판단이 바뀌었으면 지우지 말고 새로 덧붙이고 날짜를 남깁니다.

## 커밋 규칙

- 커밋 메시지는 영어 한 줄, 명령형으로 씁니다. 예: `Add 2026-08-24 source log`
- 한 커밋에 한 종류의 변경만 담습니다.
- 자동 실행에서 반영할 내용이 없으면 **빈 커밋을 만들지 않고 그냥 종료**합니다.

## 승격 판단

`python scripts/check-promotion-candidates.py` 는 자문용입니다. 이 스크립트 결과만으로
파일을 옮기거나 폴더로 승격하지 않습니다. 후보는 월간 리뷰에 보고만 합니다.
