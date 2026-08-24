---
title: "Automation Runbook"
status: active
---

# Automation Runbook

이 저장소는 세 개의 클라우드 routine이 자동으로 갱신합니다. 각 routine의 프롬프트는
"`AUTOMATION.md` 의 해당 절을 읽고 그대로 수행하라"만 지시하므로, 동작을 바꾸려면
routine이 아니라 **이 파일을 고치면 됩니다**.

`CLAUDE.md` 의 작성 규칙과 경계를 먼저 따릅니다. 충돌하면 `CLAUDE.md` 가 우선입니다.

## 공통 준비

1. `date -u +%Y-%m-%d` 로 오늘 날짜(UTC)를 확인합니다. 대화 맥락에서 날짜를 추측하지 않습니다.
   저장소의 날짜 표기는 KST 기준이므로 UTC 시각이 15:00 이후면 다음 날로 계산합니다.
2. `CURRENT.md` 의 Watchlist와 Open Questions를 읽습니다. 이번 실행에서 무엇을 우선해서
   볼지 여기서 정합니다.
3. 최근 source 로그 2~3개를 읽어 이미 기록한 항목을 파악합니다. **중복 기록을 만들지 않습니다.**

## 1. 일간 sources 수집

**주기**: 평일 08:00 KST

### 절차

1. 공통 준비를 수행합니다.
2. 아래 축을 각각 웹 검색해 새 자료를 찾습니다. 시간 창은 두 단계입니다.
   - **기본 창**: 지난 24시간(월요일 실행이면 지난 72시간).
   - **확장 창**: 지난 7일. 기본 창에 걸리지 않아도, 이번 주에 반향이 계속되고 있고
     아직 이 저장소에 기록된 적 없는 자료라면 포함합니다. 이때 `published` 는
     **원문 발행일**을 그대로 적고, `Why It Matters` 첫 줄에 왜 지금 기록하는지 한 줄로 씁니다.
   - 7일보다 오래된 자료는 기록하지 않습니다. 월간 리뷰에서 다룹니다.
   - 모델/제품 릴리스: Anthropic, OpenAI, Google DeepMind, Meta, Mistral, Qwen, DeepSeek 공식 발표
   - 논문: arXiv cs.CL / cs.AI / cs.SE 중 반향이 있는 것
   - 에이전트·개발도구: coding agent, tool use, computer use, MCP, harness 관련
   - 평가: 새 벤치마크, 기존 벤치마크 포화·오염 논쟁, METR/Terminal-Bench/SWE-bench 계열
   - 임상·헬스케어 AI: 규제 승인, prospective trial, 배포 후 모니터링
   - 안전·거버넌스: system card, 규제 초안, incident 보고
3. 각 자료의 **원문**을 WebFetch로 열어 확인하려고 시도합니다.

   이 실행 환경은 네트워크 egress 정책 때문에 상당수 도메인이 `EGRESS_BLOCKED` 로 막혀 있습니다.
   프록시를 우회하려 하지 마세요. 대신 확인 수준을 그대로 기록에 남깁니다.

   | 확인 수준 | `confidence` | `status` |
   |---|---|---|
   | 원문을 열어 내용을 읽음 | `high` (내용이 명확할 때) 또는 `medium` | `read` |
   | 원문은 못 열었지만, 서로 독립된 출처 2개 이상이 같은 사실을 말함 | `low` | `unverified` |
   | 출처가 하나뿐이거나 서로 어긋남 | 기록하지 않음 | — |

   `confidence: low` 항목은 `Limitations` 첫 줄에 **원문 미확인 사실과 막힌 도메인**을 반드시 적습니다.
   예: `- 원문 미확인. arxiv.org 가 egress 정책으로 차단되어 검색 스니펫만으로 정리했습니다.`
   `source_url` 은 어느 경우든 **원문 URL**을 적습니다. 요약 기사 URL로 대체하지 않습니다.
4. 선별 기준: 하루 **3~7개**. 이 중 `confidence: low` 는 **최대 3개**까지만 허용합니다.
   원문을 연 자료를 항상 우선합니다. 아래에 해당하면 기록하지 않습니다.
   - 벤더 마케팅 문구뿐이고 검증 가능한 내용이 없는 것
   - 이미 기록한 자료의 재보도
   - Watchlist·기존 topic 어디에도 닿지 않는 단발성 뉴스
5. `sources/YYYY-MM/YYYY-MM-DD.md` 를 만듭니다. `templates/daily-sources.md` 를 그대로
   복사해 시작하고, 파일이 이미 있으면 Source Entries 아래에 이어 붙입니다.
   `entry_count` frontmatter를 실제 entry 수로 갱신합니다.
6. 각 entry의 `My Take` 에는 "이 저장소의 기존 판단과 같은가, 다른가"를 한 줄로 씁니다.
   기존 판단과 어긋나는 자료는 특히 명확히 표시합니다. 이것이 월간 리뷰의 재료입니다.
7. Daily Summary에 그날의 한 줄 요약과, 있다면 새 topic 슬러그 제안을 적습니다.
8. 기록할 자료가 없으면 파일을 만들지 않고 커밋도 하지 않습니다. 다만 이 경우에도 10번은 수행합니다.
9. `git add` 후 `Add YYYY-MM-DD source log` 로 커밋하고 main에 push합니다.
10. **마지막에 `PushNotification` 으로 요약을 반드시 보냅니다.** 결과가 어떻든 매번 보냅니다 —
    성공했을 때도, 기록할 자료가 0건일 때도, 중간에 실패했을 때도 예외 없이 보냅니다.
    실행 도중 어떤 단계에서 막히더라도, 종료 전에 그 사실을 담아 보내는 것을 잊지 마세요.

    분량은 휴대폰 알림에서 읽히도록 **6줄 이내**로 유지하고, 아래를 담습니다.
    - 기록한 자료 수. `confidence: high`/`medium` 과 `low` 를 나눠서 셉니다.
    - 각 자료의 제목을 짧게. 긴 제목은 줄입니다.
    - **기존 판단과 어긋나는 자료가 있었다면 그것을 맨 앞에 둡니다.** 이게 가장 알 가치가 있습니다.
    - 커밋 해시, 또는 push 실패 시 그 사실과 원인.
    - 0건이면 왜 0건인지 한 줄. 예: `자료 없음 — 검색 창에 새 자료 없음` /
      `자료 없음 — egress 차단으로 원문·교차 확인 모두 실패`

    예시:
    ```
    AI-tech 08-25: 4건 기록 (검증 2, 미검증 2)
    ⚠ 기존 판단과 충돌: "open-weight 성능 격차 축소" 반박 자료 1건
    MCP Roadmap / SWE-bench Pro 리더보드 / FDA AI 기기 outcome 연구 / Gemini 3.7 Flash
    commit a1b2c3d, push 완료
    ```

## 2. 주간 topics 누적

**주기**: 일요일 21:00 KST

### 절차

1. 공통 준비를 수행합니다.
2. 지난 7일치 `sources/` 일일 로그를 모두 읽습니다.
3. entry의 `topics` 값으로 묶어, 건드릴 topic 문서를 정합니다.
4. `confidence: low` / `status: unverified` 인 entry는 topic 문서에 **누적하지 않습니다.**
   검증되지 않은 내용이 누적 지식으로 굳는 것을 막기 위해서입니다. 다만 그런 항목이
   반복해서 나타나면 해당 topic의 `Open Questions` 나 커밋 메시지에 "확인 필요"로만 남깁니다.
5. 각 topic 문서에 대해:
   - `Current View` 는 이번 주 자료로 실제로 관점이 바뀐 경우에만 고칩니다.
     고칠 때는 기존 문장을 지우지 말고 아래에 `- (2026-08-24 갱신) ...` 형태로 덧붙입니다.
   - 새로 알게 된 개념은 `Key Concepts` 에, 구체 시스템·제품은 `Notable Systems` 에 추가합니다.
   - 각 추가 항목 끝에 근거가 된 source 로그를 `(sources/2026-08/2026-08-21.md)` 처럼 표기합니다.
   - frontmatter의 `last_reviewed` 를 오늘 날짜로 갱신합니다.
6. **자료가 뒷받침하지 않는 내용을 쓰지 않습니다.** 이번 주 자료로 할 말이 없는 topic은
   손대지 않습니다. 모든 topic을 매주 갱신할 필요가 없습니다.
7. `python scripts/check-promotion-candidates.py` 를 실행하고 출력을 확인합니다.
   후보가 있으면 파일을 옮기지 말고, 커밋 메시지 본문에 후보 목록만 남깁니다.
8. 변경이 없으면 종료합니다. 있으면 `Update topics from YYYY-MM-DD week` 로 커밋하고 push합니다.

## 3. 월간 timeline + CURRENT.md 제안

**주기**: 매월 1일 09:00 KST. 대상은 **직전 달**입니다.

### 절차

1. 공통 준비를 수행합니다. 대상 월을 `YYYY-MM` 으로 확정합니다.
2. 대상 월의 `sources/YYYY-MM/` 전체와, 그달에 바뀐 `topics/` 변경 이력
   (`git log --since` / `git diff`)을 읽습니다.
3. `templates/monthly-review.md` 로 `timeline/YYYY-MM.md` 를 작성합니다.
   - `Sources Reviewed` 에는 그달의 대표 자료를 링크와 함께 나열합니다.
   - `Signals` 에는 **한 번이 아니라 반복해서** 관찰된 것만 씁니다.
   - `Radar Changes` 와 `Decisions` 는 근거가 된 source를 함께 적습니다.
   - `status` 는 `draft` 로 둡니다. 사람이 확정합니다.
4. `timeline/YYYY-MM.md` 를 **main에 직접 커밋하고 push**합니다.
   커밋 메시지는 `Add YYYY-MM monthly review draft`.
5. 이어서 `CURRENT.md` 제안을 만듭니다. 여기서부터는 main을 건드리지 않습니다.
   - `git switch -c current-update-YYYY-MM` 으로 브랜치를 만듭니다.
   - Snapshot, Tech Radar, Watchlist, Open Questions, `last_reviewed` 를 갱신합니다.
   - Radar 이동은 **항상 근거를 함께** 적습니다. 어떤 자료 때문에 Assess에서 Trial로
     옮기는지 쓸 수 없으면 옮기지 않습니다.
   - 판단이 바뀌지 않았으면 그대로 둡니다. 변화를 지어내지 않습니다.
6. 브랜치를 push하고 `gh pr create` 로 PR을 엽니다. 제목은 `Propose CURRENT.md update for YYYY-MM`.
   PR 본문에는 다음을 반드시 담습니다.
   - 바꾼 항목과 각각의 근거 source
   - 바꾸지 않기로 한 것 중 논쟁 여지가 있는 항목
   - 사람이 판단해야 할 열린 질문
   - 승격 후보 스크립트 출력
7. `gh` 를 쓸 수 없으면 브랜치만 push하고, PR을 열지 못한 사실과 브랜치 이름을 결과에 남깁니다.
8. **어떤 경우에도 `CURRENT.md` 를 main에 직접 커밋하지 않습니다.**
