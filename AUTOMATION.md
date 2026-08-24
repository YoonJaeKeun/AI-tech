---
title: "Automation Runbook"
status: active
---

# Automation Runbook

이 저장소는 세 개의 클라우드 routine이 자동으로 갱신합니다. 각 routine의 프롬프트는
"`AUTOMATION.md` 의 해당 절을 읽고 그대로 수행하라"만 지시하므로, 동작을 바꾸려면
routine이 아니라 **이 파일을 고치면 됩니다**.

`CLAUDE.md` 의 작성 규칙과 경계를 먼저 따릅니다. 충돌하면 `CLAUDE.md` 가 우선입니다.

## 실행 범위

각 실행은 **자기 절차만 수행하고 끝냅니다.** 다음은 하지 마세요.

- 새 routine, 예약 실행, self check-in, 후속 알림을 만들지 마세요.
  PR이 머지될 때까지 상태를 폴링하는 것도 포함합니다. 머지 판단은 사람이 하고,
  사람은 절차 마지막의 알림 하나로 충분히 압니다.
- PR 활동 구독처럼 이 실행 이후까지 남는 백그라운드 작업을 걸지 마세요.
- 다른 routine의 절차를 대신 수행하지 마세요.

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
2. 시간 창은 두 단계입니다.
   - **기본 창**: 지난 24시간(월요일 실행이면 지난 72시간).
   - **확장 창**: 지난 7일. 기본 창에 걸리지 않아도, 이번 주에 반향이 계속되고 있고
     아직 이 저장소에 기록된 적 없는 자료라면 포함합니다. 이때 `published` 는
     **원문 발행일**을 그대로 적고, `Why It Matters` 첫 줄에 왜 지금 기록하는지 한 줄로 씁니다.
   - 7일보다 오래된 자료는 기록하지 않습니다. 월간 리뷰에서 다룹니다.

3. 아래 10개 축을 각각 검색합니다. **각 축에 적힌 1차 출처를 이름으로 지정해서 찾습니다.**
   `"Anthropic announcement August 2026"` 같은 개방형 쿼리는 SEO 애그리게이터만 물어옵니다.
   `site:` 스코프나 출처 이름 + 제품명 + 날짜 조합을 쓰세요.

   | 축 | 1차 출처 | topic |
   |---|---|---|
   | 모델·제품 릴리스 | anthropic.com/news, openai.com/index, deepmind.google/discover/blog, ai.meta.com/blog, mistral.ai/news, qwenlm.github.io/blog, api-docs.deepseek.com/news | `models` |
   | 논문 | arxiv.org/list/cs.CL/recent, cs.AI/recent, cs.SE/recent, huggingface.co/papers | 내용에 따라 |
   | 에이전트·개발도구 | blog.modelcontextprotocol.io, github.com/modelcontextprotocol, github.com/anthropics, code.claude.com/docs/changelog, cursor.com/changelog, docs.devin.ai/release-notes | `agents` |
   | 평가 | metr.org/blog, tbench.ai, swebench.com, github.com/SWE-bench, scaleapi.github.io, epoch.ai | `evals-benchmarks` |
   | 임상·헬스케어 AI | fda.gov (AI-enabled device list, 510k), nature.com/nm, ai.nejm.org, journals.plos.org/digitalhealth, clinicaltrials.gov | `clinical-healthcare` |
   | 안전·거버넌스 | aisi.gov.uk, nist.gov/aisi, frontiermodelforum.org, incidentdatabase.ai, digital-strategy.ec.europa.eu (AI Act) | `safety-governance` |
   | 비용·인프라·서빙 | 벤더 pricing 페이지와 changelog, artificialanalysis.ai, github.com/vllm-project/vllm 릴리스, github.com/ggml-org/llama.cpp 릴리스 | `infra-cost` |
   | 국내 동향·규제 | 과기정통부, 식약처, 개인정보보호위원회 보도자료, 국가법령정보센터(인공지능 기본법 시행령), 국내 벤더 공식 발표 | `korea` |
   | LLM 파이프라인 | RAG·구조화 출력·프롬프트 기법 관련 arXiv, 벤더 엔지니어링 블로그, 주요 프레임워크 릴리스 노트 | `llm-pipeline` |
   | 오픈소스 생태계 | huggingface.co/blog, huggingface.co/models 트렌딩, 주요 프레임워크 GitHub 릴리스, 라이선스 변경 공지 | `open-source` |

   **다음 도메인은 출처로 쓰지 않습니다.** 1차 자료를 재가공한 SEO 애그리게이터입니다.
   releasebot.io, llmgateway.io, local-ai-zone.github.io, powerdrill.ai, blog.mean.ceo,
   clickup.com, promptlayer.com, 그 밖에 "AI news roundup", "월간 총정리" 류 페이지.
   검색 결과에 이런 페이지만 나오면, 거기서 **1차 출처 URL을 찾아내** 그 URL로 기록합니다.

4. 각 자료에 대해 원문을 WebFetch로 열어보되, **열리지 않아도 기록합니다.**

   이 실행 환경은 egress 정책으로 상당수 도메인이 `EGRESS_BLOCKED` 입니다.
   프록시를 우회하려 하지 마세요. 원문을 못 열었다는 사실을 기록에 남기고 넘어갑니다.

   | 확인 수준 | `confidence` | `status` |
   |---|---|---|
   | 원문을 열어 내용을 읽음 | `high` 또는 `medium` | `read` |
   | 원문은 못 열었지만, 서로 독립된 출처 2개 이상이 같은 사실을 말함 | `low` | `unverified` |
   | 출처가 하나뿐이거나 서로 어긋남 | 기록하지 않음 | — |

   - `source_url` 은 **언제나 1차 출처의 canonical URL** 을 적습니다. arXiv는 `abs` 링크,
     논문은 DOI 링크, 벤더 발표는 해당 글의 permalink. 2차 보도 URL로 대체하지 않습니다.
     원문을 못 열었어도 나중에 직접 눌러볼 수 있어야 하므로 이 항목이 가장 중요합니다.
   - `confidence: low` 항목은 `Limitations` 첫 줄에 **원문 미확인 사실과 막힌 도메인**,
     그리고 **무엇을 근거로 교차 확인했는지**를 적습니다.
     예: `- 원문 미확인(arxiv.org egress 차단). Hugging Face Papers와 저자 공개 스레드로 교차 확인.`
   - 숫자·날짜·고유명사는 2차 출처에서 옮길 때 특히 조심합니다. 서로 다르면 기록하지 않습니다.
   - **URL과 날짜를 추측해서 확정 값처럼 적지 마세요.** 그럴듯한 1차 URL을 지어내면
     실제로 존재하지 않는 링크가 확정 사실처럼 남습니다. 이게 이 저장소에서 가장 나쁜 오염입니다.
     - canonical URL을 특정하지 못했으면, 지어내지 말고 **실제로 확인한 2차 출처 URL**을
       `source_url` 에 적고 `Limitations` 에 `- canonical URL 미확정. 2차 출처 URL로 기록.` 을 남깁니다.
     - 발행일을 확정하지 못했으면 `published: unknown` 으로 적습니다. 추정 날짜를 쓰지 않습니다.
       추정 시점은 `Limitations` 에 문장으로 남깁니다.
   - 배제 도메인만으로 구성된 항목은 기록하지 않습니다. 애그리게이터가 1차 URL을 지목한다는
     이유만으로는 부족합니다. **독립된 비(非)애그리게이터 출처가 최소 하나** 있어야 합니다.

5. 선별 기준: 하루 **5~10개**. 원문을 연 자료를 우선하되, `confidence: low` 라는 이유만으로
   버리지 않습니다. 10개 축 전부에서 억지로 채우려 하지 말고, 축이 비는 날은 비워둡니다.
   아래에 해당하면 기록하지 않습니다.
   - 벤더 마케팅 문구뿐이고 검증 가능한 내용이 없는 것
   - 이미 기록한 자료의 재보도
   - Watchlist·기존 topic 어디에도 닿지 않는 단발성 뉴스
   - 위 배제 도메인에서만 나오고 1차 출처를 찾지 못한 것
6. `sources/YYYY-MM/YYYY-MM-DD.md` 를 만듭니다. `templates/daily-sources.md` 를 그대로
   복사해 시작하고, 파일이 이미 있으면 Source Entries 아래에 이어 붙입니다.
   `entry_count` frontmatter를 실제 entry 수로 갱신합니다.
7. 각 entry의 `My Take` 에는 "이 저장소의 기존 판단과 같은가, 다른가"를 한 줄로 씁니다.
   기존 판단과 어긋나는 자료는 특히 명확히 표시합니다. 이것이 월간 리뷰의 재료입니다.
8. Daily Summary에 그날의 한 줄 요약과, 있다면 새 topic 슬러그 제안을 적습니다.
9. 기록할 자료가 없으면 파일을 만들지 않고 커밋도 하지 않습니다. 다만 이 경우에도 11번은 수행합니다.
10. `git add` 후 `Add YYYY-MM-DD source log` 로 커밋하고 main에 push합니다.
11. **마지막에 `PushNotification` 으로 요약을 반드시 보냅니다.** 결과가 어떻든 매번 보냅니다 —
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
8. 변경이 없으면 커밋하지 않습니다. 있으면 `Update topics from YYYY-MM-DD week` 로 커밋하고 push합니다.
9. **마지막에 `PushNotification` 으로 요약을 반드시 보냅니다.** 변경이 없었을 때도, 실패했을 때도
   예외 없이 보냅니다. 6줄 이내로 아래를 담습니다.
   - 갱신한 topic 문서와 각각 무엇이 추가됐는지 (한 줄로 압축)
   - 자료 부족으로 손대지 않은 topic
   - 승격 후보가 있으면 그 사실
   - 커밋 해시, 또는 변경 없음/실패 사유

   예시: `AI-tech 주간: agents·evals 갱신, clinical 자료부족으로 보류 / 승격후보 없음 / commit a1b2c3d`

## 3. 월간 timeline + CURRENT.md 제안

**주기**: 매월 1일 09:00 KST. 대상은 **직전 달**입니다.

### 절차

1. 공통 준비를 수행합니다. 대상 월을 `YYYY-MM` 으로 확정합니다.
2. 대상 월의 `sources/YYYY-MM/` 전체와, 그달에 바뀐 `topics/` 변경 이력
   (`git log --since` / `git diff`)을 읽습니다.
3. `timeline/YYYY-MM.md` 를 작성합니다.

   **이미 그 파일이 있으면 절대 덮어쓰지 않습니다.** 사람이 직접 쓴 내용일 수 있습니다.
   이 경우 기존 내용을 그대로 두고 파일 맨 아래에
   `## 자동 갱신 (YYYY-MM-DD)` 섹션을 새로 만들어 그 안에만 씁니다.
   기존 섹션의 문장을 고치거나 지우지 마세요.

   파일이 없을 때만 `templates/monthly-review.md` 로 새로 만듭니다.
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
9. **마지막에 `PushNotification` 으로 요약을 반드시 보냅니다.** 이 알림이 없으면 PR이 열린 것을
   모르고 지나갑니다. 성공·실패 무관하게 보내며, 6줄 이내로 아래를 담습니다.
   - **PR URL을 맨 앞에.** 사람이 눌러야 할 링크가 이 실행의 결과물입니다.
   - `CURRENT.md` 에서 바꾸자고 제안한 항목 수와, 그중 Radar 이동이 있으면 그 내용
   - 사람이 판단해야 할 열린 질문이 있으면 한 줄
   - PR을 열지 못했으면 그 사실과 브랜치 이름
   - timeline 커밋 해시

   예시:
   ```
   AI-tech 2026-08 월간 리뷰
   PR: https://github.com/YoonJaeKeun/AI-tech/pull/3
   Radar 이동 2건 제안 (subagent orchestration: Trial→Adopt 등), 열린 질문 1건
   timeline commit a1b2c3d
   ```
