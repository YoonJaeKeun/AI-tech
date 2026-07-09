# Sources

읽은 자료를 월 폴더 아래 날짜별 파일로 저장합니다. 하루에 읽은 여러 자료는 하나의 날짜 파일 안에서 source entry로 나눕니다.

## Naming

```text
YYYY-MM/YYYY-MM-DD.md
```

예시:

```text
2026-07/2026-07-09.md
2026-08/2026-08-01.md
```

## Entry Format

각 source entry는 `###` 제목으로 시작하고, 바로 아래에 최소 메타데이터를 적습니다.

```markdown
### Source Title

- source_url: https://example.com/source
- published: 2026-07-09
- type: report
- topics: agents, evals-benchmarks
- status: read
- confidence: medium
```

## Types

각 entry의 `type`에는 다음 중 하나를 우선 사용합니다.

- `paper`
- `report`
- `product-release`
- `benchmark`
- `blog`
- `talk`
- `regulation`
- `dataset`
- `other`

## Topics

각 entry의 `topics`에는 관련 주제를 쉼표로 구분해 적습니다.

예시:

```markdown
- topics: agents, models
```
