---
title: "Agents"
topic: agents
last_reviewed: 2026-09-06
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

## 관련 주제

- [LLM Pipeline (전처리·후처리)](../llm-pipeline/llm-pipeline.md): 에이전트가 매 스텝 반복 실행하는 LLM 입력·출력 처리 파이프라인. 원래 이 폴더 아래 있었으나, 에이전트에 국한되지 않는 기반 주제라 별도 주제로 분리했습니다.

## Key Concepts

- Tool use: 브라우저, terminal, DB, API, 파일 시스템 같은 외부 도구 호출.
- (2026-08-30 추가) Tool-use/agent 통신 표준의 거버넌스 재단화: MCP(도구 통합)가 Agentic AI Foundation(Linux Foundation 산하) 아래에서 stateless 코어(세션·핸드셰이크 제거, Multi Round-Trip Requests)와 Client ID Metadata Documents, Enterprise-Managed Authorization 같은 엔터프라이즈 인증 기능을 갖춰가는 흐름입니다. 개인 실험 도구에서 운영 인프라 표준으로 이동하는 신호로 봅니다. (sources/2026-08/2026-08-24.md)
- Scaffolding: 모델을 둘러싼 planner, memory, tool router, verifier, retry loop 같은 실행 구조.
- Subagents: 하나의 큰 일을 조사, 구현, 검증, 리뷰 같은 하위 역할로 분해하는 방식.
- Computer use: UI나 OS 환경을 직접 조작하는 에이전트 패턴.
- Human-in-the-loop: 고위험 action 전에 사람이 승인하거나 review하는 통제 방식.
- (2026-09-06 추가) Auto mode의 Containment Escape 규칙: 클라우드 메타데이터 자격증명 조회, egress 우회, 테넌트 간 접근 시도가 환경에서 명시적으로 허용하지 않는 한 더 이상 자동 승인되지 않습니다. 작업 디렉터리 밖 파일을 처음 읽을 때도 auto mode에서 1회성 확인을 거치도록 바뀌었습니다(Claude Code v2.1.257). Open Questions의 "local coding agent의 기본 sandbox, network, credential 정책" 질문에 하네스 쪽에서 나온 구체적인 답 하나입니다. (sources/2026-09/2026-09-03.md)
- (2026-09-06 추가) 조직이 모든 사용자에게 HTTP/SSE MCP 서버를 배포하는 `managedMcpServers` 관리 설정과, 무인 headless 실행에서 프롬프트가 필요한 작업을 자동 거부하는 `--permission-prompts none` 옵션(Claude Code v2.1.259). 하네스가 조직 단위 관리·무인 실행 통제 쪽으로 계속 이동하고 있음을 보여줍니다. (sources/2026-09/2026-09-04.md)

## Patterns

- Plan, act, observe, revise loop.
- 테스트를 먼저 만들고 실패를 재현한 뒤 수정하고 다시 테스트하는 coding loop.
- remote sandbox에서 실행하고 결과물만 검토하는 격리 실행.
- 여러 agent에게 다른 역할을 주고 최종 판단은 사람 또는 verifier가 하는 구조.
- 권한을 단계적으로 열어주는 progressive permission 방식.
- (2026-08-30 추가) subagent 결과가 실행 한도(예: maxTurns)에 도달해 잘렸을 때, 이를 완결된 결과와 구분해 명시적으로 "partial"로 표시하는 방식. 잘린 결과를 완결로 오인하는 실패를 줄입니다(Claude Code v2.1.246). (sources/2026-08/2026-08-26.md)
- (2026-09-06 추가) foreground subagent의 tool call을 Remote Control 클라이언트로 실시간 스트리밍해, 원격에서 실행 중인 subagent의 행동을 그대로 관찰하는 방식(Claude Code v2.1.251). Trial의 "원격 sandbox 또는 격리된 terminal 기반 에이전트 실행"을 실제로 감시 가능하게 만드는 진전입니다. (sources/2026-08/2026-08-31.md)

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
- [The New MCP Roadmap](../../sources/2026-08/2026-08-24.md#the-new-mcp-roadmap)
- [Claude Code v2.1.246](../../sources/2026-08/2026-08-26.md#claude-code-v21246-auto-mode-확장-subagent-결과-처리-개선)
- [Claude Code v2.1.251](../../sources/2026-08/2026-08-31.md#claude-code-v21251-premodelswitchpostmodelswitch-훅-remote-control-서브에이전트-실시간-스트리밍)
- [Claude Code v2.1.257/v2.1.258](../../sources/2026-09/2026-09-03.md#claude-code-v21257v21258--fable-51-기본-모델-전환-auto-mode-containment-escape-규칙-추가)
- [Claude Code v2.1.259](../../sources/2026-09/2026-09-04.md#claude-code-v21259--managedmcpservers---permission-prompts-none-동시-세션-설정-덮어쓰기-버그-수정)

## Open Questions

- 어떤 작업부터 agent에게 맡기고 어떤 작업은 반드시 사람 검토를 거쳐야 하는가?
- long-horizon task에서 성공률보다 더 먼저 측정해야 하는 실패 유형은 무엇인가?
- local coding agent의 기본 sandbox, network, credential 정책은 어떻게 잡아야 하는가?
