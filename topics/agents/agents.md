---
title: "Agents"
topic: agents
last_reviewed: 2026-07-09
---

# Agents

도구 사용, 계획, 메모리, 브라우징, 코딩 에이전트, 워크플로 자동화와 관련된 누적 정리입니다.

이 주제는 세부 노트가 늘어 폴더로 승격했습니다. 이 파일은 `topics/agents/` 폴더의 허브로, 현재 판단, 목차, 대표 소스만 유지하고, 세부 내용은 같은 폴더의 하위 파일에 있습니다.

## Current View

- 에이전트는 2026년 AI 흐름에서 가장 실용적이면서도 가장 위험 관리가 필요한 영역입니다.
- 현재 가장 강한 적용처는 coding, terminal workflow, research, 문서 기반 업무 자동화입니다.
- 실제 가치는 "모델이 무엇을 아는가"보다 "권한, 도구, sandbox, 검증 루프를 어떻게 설계했는가"에서 갈립니다.

## 세부 노트

- [Agent Loop](agent-loop.md): 추론-행동-관찰 반복 구조, ReAct, 종료 조건, 구성 요소, Reactive/Plan-and-Execute/Reflection 변형 비교.
- [LLM 전처리와 후처리](llm-pre-post-processing.md): 매 스텝 LLM 호출을 감싸는 입력 조립(전처리)과 출력 파싱·검증(후처리), 애플리케이션 레벨과 모델 내부 레벨 구분.

## Key Concepts

- Tool use: 브라우저, terminal, DB, API, 파일 시스템 같은 외부 도구 호출.
- Scaffolding: 모델을 둘러싼 planner, memory, tool router, verifier, retry loop 같은 실행 구조.
- Subagents: 하나의 큰 일을 조사, 구현, 검증, 리뷰 같은 하위 역할로 분해하는 방식.
- Computer use: UI나 OS 환경을 직접 조작하는 에이전트 패턴.
- Human-in-the-loop: 고위험 action 전에 사람이 승인하거나 review하는 통제 방식.

## Patterns

- Plan, act, observe, revise loop.
- 테스트를 먼저 만들고 실패를 재현한 뒤 수정하고 다시 테스트하는 coding loop.
- remote sandbox에서 실행하고 결과물만 검토하는 격리 실행.
- 여러 agent에게 다른 역할을 주고 최종 판단은 사람 또는 verifier가 하는 구조.
- 권한을 단계적으로 열어주는 progressive permission 방식.

## Failure Modes

- 장기 작업에서 목표를 잃거나 중간 실패를 숨깁니다.
- tool output을 잘못 해석하고 잘못된 다음 action을 수행합니다.
- benchmark에서는 성공하지만 실제 환경의 flaky test, 권한, 데이터 상태에서 무너집니다.
- prompt injection이나 hijack에 의해 외부 도구 사용이 오염될 수 있습니다.
- 비용과 token 사용량이 retry loop에서 폭증할 수 있습니다.

## Sources

- [Anthropic Claude Sonnet 5](../../sources/2026-07/2026-07-09.md#introducing-claude-sonnet-5)
- [Google I/O 2026 Developer Keynote](../../sources/2026-07/2026-07-09.md#google-io-2026-developer-keynote-agentic-workflow)
- [Terminal-Bench 2.0](../../sources/2026-07/2026-07-09.md#terminal-bench-20)
- [METR Frontier Risk Report](../../sources/2026-07/2026-07-09.md#metr-frontier-risk-report-february-to-march-2026)
- [International AI Safety Report 2026](../../sources/2026-07/2026-07-09.md#international-ai-safety-report-2026)

## Open Questions

- 어떤 작업부터 agent에게 맡기고 어떤 작업은 반드시 사람 검토를 거쳐야 하는가?
- long-horizon task에서 성공률보다 더 먼저 측정해야 하는 실패 유형은 무엇인가?
- local coding agent의 기본 sandbox, network, credential 정책은 어떻게 잡아야 하는가?
