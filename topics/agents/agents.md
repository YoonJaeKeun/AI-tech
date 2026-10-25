---
title: "Agents"
topic: agents
last_reviewed: 2026-10-25
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
- (2026-09-13 추가) 하네스 자기진단 기능 확장: 사용하지 않는 skill과 그 컨텍스트 비용을 진단하는 `/skill-doctor`, `/status`·`claude doctor`의 조직 정책 로드 실패 원인 표시, `/cost`·상태줄의 prompt cache miss 원인 표시(Claude Code v2.1.260/261). Adopt의 "LLM 전처리·후처리 경계를 명시적으로 설계하기" 판단과 맞닿아 있습니다 — 컨텍스트에 무엇이 들어가는지를 하네스 스스로 진단하게 만드는 기능입니다. (sources/2026-09/2026-09-07.md)
- (2026-09-13 추가) 실행 비용·컨텍스트 구성을 명시적으로 통제하는 옵션 확대: Bedrock/Vertex/Foundry 전반의 모델 effort 수준을 상한하는 `maxEffortLevel`, 매 요청마다 시스템 프롬프트를 새로 렌더링하는 `--system-prompt-snapshot off`(Claude Code v2.1.267). (sources/2026-09/2026-09-10.md)
- (2026-09-13 추가) Artifact 퍼블리시 시 커넥터가 실제로 노출하지 않는 도구 이름을 그냥 받아들이던 문제를 고쳐, 선언된 도구가 하나도 없으면 퍼블리시를 거부하고 일부만 없으면 경고하도록 바뀌었습니다(Claude Code v2.1.265). "출력을 얼마나 견고하게 파싱·검증하는가(후처리)" 판단과 정확히 맞닿는 사례로, 실행 전에 선언과 실제 능력의 불일치를 잡아내는 가드레일입니다. (sources/2026-09/2026-09-09.md)
- (2026-09-13 추가) 반복적으로 드러나는 경로·권한 검사 우회 패턴: 플러그인 경로에 백슬래시를 넣어 macOS·Linux의 symlink containment 검사를 우회하는 취약점(v2.1.265)에 이어, symlink된 디렉터리(`/etc`, `/tmp`, `/var`, `/bin` 등)의 deny/ask 권한 규칙이 실제 경로로 우회되는 문제와 마켓플레이스 항목 경로의 백슬래시 우회(v2.1.267/268)가 잇따라 발견·수정됐습니다. 하네스의 실행 격리를 신뢰할 때, 경로 정규화 관련 우회는 한 번 고쳐도 다른 진입점에서 반복해서 나타날 수 있다는 점을 보여줍니다. (sources/2026-09/2026-09-09.md, sources/2026-09/2026-09-11.md)
- (2026-09-20 추가) 도구 호출 단위 sandbox 세분화가 이어지고 있습니다: Bash·PowerShell·Monitor의 auto mode에 커맨드별 도메인 allowlist(`allowed_domains`)가 추가되고(v2.1.271, 09-14) v2.1.272/273(09-15)에서 정식화됐으며, `claude plugin install/update`의 `--accept-command <sha256>`로 플러그인 커맨드를 개별 승인할 수 있게 됐습니다(v2.1.271). Adopt의 "제한된 범위의 코딩 에이전트" 판단이 도구 호출 단위까지 정밀해지고 있습니다. (sources/2026-09/2026-09-14.md, sources/2026-09/2026-09-15.md, sources/2026-09/2026-09-16.md)
- (2026-09-20 추가) MCP 표준의 enterprise 인증 기능이 실제 SDK 구현으로 이어지고 있습니다: Rust SDK(rmcp) v3.3.0(09-10)에 enterprise refresh-token exchange와 ID-JAG(JWT Authorization Grant) exchange 지원이 추가됐습니다. 2026-08-30에 추가한 "MCP가 운영 인프라 표준으로 이동" 판단의 구체적 후속 사례입니다. (sources/2026-09/2026-09-15.md)
- (2026-09-27 추가) 실행 제어가 계속 벤더 인프라 레이어로 이동합니다: auto mode 분류기가 서버사이드 기본값으로 전환되며 과금되지 않고(Claude Code v2.1.278, 09-19), CLAUDE.md가 없는 프로젝트의 AGENTS.md 지원과 게이트웨이 egress boundary 옵션(`CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY`)이 함께 추가됐습니다(v2.1.277). (sources/2026-09/2026-09-21.md)
- (2026-09-27 추가) 신모델(Opus 5.5)이 발표 당일 Claude Code 기본 Opus 모델로 즉시 편입됐습니다(v2.1.280, 09-22, 1M 컨텍스트). 다음날에는 Bedrock `assume_role`/`guardrail` 설정과 세션 재개(resume) 안정성 관련 다수 버그(재개 시 API 대화 추론 붕괴, prompt cache 손실, 무한 재시도)가 한 번에 수정됐습니다(v2.1.281, 09-23). Trial의 "긴 context와 추론 effort를 조절하는 모델 선택 전략"이 실제로 오래 지속되는 세션에서 의미가 있으려면 이런 재개 안정성이 먼저 갖춰져야 한다는 점을 보여줍니다. (sources/2026-09/2026-09-23.md, sources/2026-09/2026-09-24.md)
- (2026-10-04 추가) "발표 당일 기본 모델 편입" 패턴이 다시 반복됐습니다: Claude Sonnet 5.5(2026-09-28 공개, 원문 확인)가 같은 날 Claude Code v2.1.284의 기본 Sonnet 모델로 편입됐습니다(1M 컨텍스트, 입력 $2/출력 $10). 같은 배치의 v2.1.283(09-25)은 LLM 게이트웨이 요청을 묶는 `x-claude-code-prompt-id` 헤더(옵트인), 허용 모델만 제한하는 `availableModelsMatch` 관리 설정, 오래된 모델을 겨냥한 프롬프트 패턴을 진단하는 `/doctor prompt-audit`을 추가했고, v2.1.282(09-24)는 세션 재개 안정성 버그 다수를 수정했습니다. (sources/2026-09/2026-09-29.md)
- (2026-10-04 추가) 세션·인증·MCP 안정성 개선이 거의 매일 단위로 이어졌습니다: v2.1.285(09-29)는 `claude plugin configure`·`claude --desktop`·`allowedProviders` 관리 설정을 추가했고, v2.1.286(09-30)은 여러 권한 요청이 쌓일 때 "2 of 5" 형태로 개수를 보여주는 권한 프롬프트 카운터를 추가했습니다. v2.1.287(10-01)은 플러그인이 더 깊은 동작까지 바꿀 수 있게 하는 "Claude Mods" 체계와 세션을 이름·태스크로 거르는 `n:<텍스트>` 필터를 changelog에 반영했습니다. Adopt의 "제한된 범위의 코딩 에이전트"·"LLM 전처리·후처리 경계" 판단과 맞물리는 안정성 개선이 계속되는 동시에, Trial의 "subagent orchestration" 판단과도 닿는 확장성(플러그인) 기능이 더해지고 있습니다. (sources/2026-09/2026-09-30.md, sources/2026-10/2026-10-01.md, sources/2026-10/2026-10-02.md)
- (2026-10-04 추가) Anthropic이 유료 Claude 플랜 개발자 대상 Claude Plugins 제출 포털을 공개했습니다(2026-09-25, 원문 확인). MCP 커넥터 단독 제출 또는 MCP 서버+Agent Skills를 묶은 GitHub 저장소 제출 두 방식을 지원하며, 제출 즉시 자동 안전성 검증(auto-validation)과 게시 후 설치·검색 분석을 제공합니다. 2026-07-28 MCP 2.0(stateless core) 사양과 MCP Apps, Enterprise Managed Auth를 지원한다고 밝혀, Watchlist의 MCP 사양·거버넌스 항목이 사양 문서 수준을 넘어 실제 유통 구조(마켓플레이스+제출 포털)로 구체화된 사례입니다. (sources/2026-09/2026-09-28.md)
- (2026-10-04 추가) Anthropic·Barclays가 Claude Code·Claude 모델 전사 확산 계약을 공개했습니다(2026-10-01, 원문 확인). 2026년 말까지 개발자 50%, 2027년에는 대다수가 Claude Code를 쓰도록 하는 목표를 밝혔고, 기존 Colleague Knowledge Assistant는 1.6만명 이상이 사용하며 검색 100만 건 이상을 처리했으며 Global Markets 부문은 하루 12만 건의 이메일을 처리한다고 밝혔습니다. 거버넌스·보안 통제를 명시한 전사 배포 사례로 Adopt의 "제한된 범위의 코딩 에이전트" 판단과 가까운 방향이지만, 구체적인 비용·시간 절감 수치는 이번 발표에 포함되지 않았습니다. (sources/2026-10/2026-10-02.md)
- (2026-10-11 추가) Claude Code v2.1.288~295가 거의 매일 단위로 배포되며 하네스 안정성·mod/plugin·subagent 기능이 계속 확장됐습니다. mod용 `$.ui.selection()`, MCP 재인증 프롬프트, `--marketplace` 지정 설치, Agent tool `effort` 파라미터, `agent.spawn` mod 훅의 workflow agent 지원, `$.tool.register`의 `isDeferred` 플래그, subagent 타입 구분 필드가 추가됐고, hook이 실제로 동작을 막지 못하던 버그를 고친 뒤(v2.1.294) hook 실패 시 동작을 막는 `onFailure:"block"` 옵션(v2.1.295)이 바로 뒤따랐습니다. 같은 날 Claude Agent SDK(Python/TS)도 parity 릴리스를 냈습니다. 특이하게 v2.1.290에서 고친 "컨테이너 재시작 후 클라우드 세션 미기동" 수정이 v2.1.293에서 다시 되돌려졌습니다. Adopt의 "제한된 범위의 코딩 에이전트"(사람 승인 절차) 판단은 hook·guardrail 계층 자체의 신뢰성에 의존하므로, 이번 주 hook 관련 수정 흐름이 그 전제를 직접 뒷받침합니다. (sources/2026-10/2026-10-05.md, sources/2026-10/2026-10-07.md, sources/2026-10/2026-10-08.md, sources/2026-10/2026-10-09.md)
- (2026-10-11 추가) Anthropic이 "Claude Frontier Academy"를 공개했습니다(2026-10-02, 원문 확인). $100M을 투입해 2027년 말까지 'Frontier Deployed Engineer' 1만 명을 양성하는 프로그램으로, 의료 레지던트 모델을 본떠 집중 교육 → 12주 레지던시 → 최종 평가 구조를 거칩니다. Accenture·Deloitte·McKinsey·Morgan Stanley 등이 초기 참여합니다. 2026-10-02 로그의 Barclays 사례와 나란히, Anthropic이 "모델 성능"보다 "그 모델을 실제 프로덕션에 배치할 수 있는 인력"을 병목으로 보고 있다는 신호입니다. (sources/2026-10/2026-10-05.md)
- (2026-10-18 추가) Claude Code v2.1.296(10-09)~v2.1.301(10-15)이 매일 단위로 이어지며, 백그라운드 전환 시 실행 중이던 turn·`!` 명령을 "보이지 않게 끝까지 실행"하지 않고 중단시키는 안전장치가 v2.1.296에서 도입된 뒤 v2.1.301에서 다시 보강됐습니다. 같은 구간에 OpenTelemetry `tool_decision` 이벤트가 분류기 결정(`classifier_verdict`/`classifier_category`)과 권한 규칙 결정(`permission_mode`)을 구분해 노출하도록 바뀌었고, 200K 토큰을 넘는 대화가 약 54분 idle 상태면 prompt cache 만료 전에 자동 압축되는 "idle compaction"이 추가됐습니다. Adopt의 "제한된 범위의 코딩 에이전트"(사람 승인 절차) 판단이 전제하는 "감시되지 않는 실행을 줄인다"는 방향이 백그라운드 실행·분류기 투명성 두 축에서 계속 구체화되고 있습니다. (sources/2026-10/2026-10-12.md#anthropic-claude-code-v21296-배포--sonnet-55-cache-read-가격-010m-반영-mcp-tool-설명-길이-제한-20484096자-백그라운드-전환-시-실행-중-명령-중단-처리, sources/2026-10/2026-10-15.md#anthropic-claude-code-v21299300-배포-claude-agent-sdkpython-v02166167-동시-parity--유휴-압축-gzip-요청-opentelemetry-cache-토큰-속성-추가, sources/2026-10/2026-10-16.md#anthropic-claude-code-v21301-배포--사용량-한도-임박-시-재시도-중단-opentelemetry-도구-분류기-속성-추가-백그라운드-실행-중-명령-중단-안전장치-강화)
- (2026-10-18 추가) Claude Code 저장소에 HIPAA 환경용 `managed-settings.json`/`managed-mcp.json` 예제(`hipaa-baseline.json`, `managed-mcp.lockdown.json`)가 추가됐습니다(커밋 2026-10-07, 원문 확인). Bash를 샌드박스 전용으로 제한하고 네트워크를 allowlist로 묶으며 자격증명·환경변수를 숨기고 OTel로 보내는 이벤트의 prompt/response/tool 내용을 `<REDACTED>`로 치환합니다. README는 스스로 "출발점일 뿐 컴플라이언스 보증이 아니다"라고 명시합니다. Hold의 "PHI, PII, confidential data를 공개 LLM에 직접 넣는 사용"을 막기 위한 실무적 템플릿이 벤더 쪽에서 나온 사례입니다. (sources/2026-10/2026-10-14.md#anthropic-claude-code-hipaa-환경용-managed-settings-예제-추가--examplesmanaged-settings에-hipaa-baselinejson--managed-mcplockdownjson--readme)
- (2026-10-18 추가) Claude Developer Platform에 Managed Agents "Dynamic workflows"(beta)가 공개됐습니다(2026-10-09, 원문 확인, anthropic-sdk-python v1.13.0과 교차 확인). `multiagent_20261001` 설정으로 활성화하며, 에이전트가 여러 에이전트를 단계(phase)로 나눠 실행하는 workflow를 스스로 작성하고 `workflow_run.*` 이벤트로 추적합니다. Trial의 "subagent orchestration" 실험이 애플리케이션 레이어(LangChain 미들웨어 등)에서 벤더 네이티브 API 레이어로 내려오는 흐름을 보여주지만, 베타 단계라 실패 처리·비용 관측의 투명성은 아직 확인되지 않았습니다. (sources/2026-10/2026-10-15.md#claude-developer-platform-managed-agents-dynamic-workflowsbeta-공개--다수-에이전트를-단계phase로-묶어-실행하는-멀티에이전트-오케스트레이션-api)
- (2026-10-25 추가) Claude Code v2.1.302~309(10-16~10-22)가 거의 매일 단위로 이어지며, 안전·격리 관련 변경이 두 방향으로 동시에 나타났습니다. 한편에는 우회 가능성을 넓히는 변경(fork subagent가 `claude -p`·Agent SDK·desktop app·VS Code에서 기본 활성화, `sandbox.allowNestedUserNamespaces`로 Linux 샌드박스 안 user namespace 생성 허용)이, 다른 한편에는 우회를 막거나 감사 가능하게 만드는 변경(mod `tool.check`의 `decider: "person"`, 권한·안전 점검·hook·샌드박스의 모든 차단/확인/반송 이벤트를 남기는 `claude_code.safety_event` OpenTelemetry 이벤트, 샌드박스 셸 시작 파일 격리·`--mcp-config` 설정 파일 변조 방지·`claude ultrareview`의 workspace trust 요구 등 v2.1.308~309의 보안 수정 다수)가 함께 나타났습니다. 조직 관리자가 전사 기본 Code Review 수준(Quick/Standard/Deep)을 고르고 저장소별로 재지정할 수 있게 된 것(v2.1.304)도 Adopt의 "사람 승인 절차가 있는 저장소 작업" 전제를 조직 레벨에서 구체화합니다. (sources/2026-10/2026-10-19.md, sources/2026-10/2026-10-20.md, sources/2026-10/2026-10-21.md, sources/2026-10/2026-10-22.md, sources/2026-10/2026-10-23.md)
- (2026-10-25 추가) Anthropic이 Agent Skills 표준(이름·로고·GitHub organization·agentskills.io 도메인)을 Agentic AI Foundation(AAIF)에 이관한다고 발표했습니다(2026-10-22, 원문 확인). 2026-08-24에 기록한 "MCP가 AAIF로 넘어갔다"는 관찰에 이어, 에이전트 생태계의 두 핵심 표준(MCP, Agent Skills)이 모두 같은 벤더 중립 거버넌스 아래로 수렴하는 패턴이 확인됐습니다. 발표 시점 기준 약 100만 개 skill 공개·약 2.8억 회 설치, 70개 이상 플랫폼 통합이라는 수치는 Anthropic 자체 발표로 독립 집계로는 교차 확인되지 않았습니다. (sources/2026-10/2026-10-23.md)

## Patterns

- Plan, act, observe, revise loop.
- 테스트를 먼저 만들고 실패를 재현한 뒤 수정하고 다시 테스트하는 coding loop.
- remote sandbox에서 실행하고 결과물만 검토하는 격리 실행.
- 여러 agent에게 다른 역할을 주고 최종 판단은 사람 또는 verifier가 하는 구조.
- 권한을 단계적으로 열어주는 progressive permission 방식.
- (2026-08-30 추가) subagent 결과가 실행 한도(예: maxTurns)에 도달해 잘렸을 때, 이를 완결된 결과와 구분해 명시적으로 "partial"로 표시하는 방식. 잘린 결과를 완결로 오인하는 실패를 줄입니다(Claude Code v2.1.246). (sources/2026-08/2026-08-26.md)
- (2026-09-06 추가) foreground subagent의 tool call을 Remote Control 클라이언트로 실시간 스트리밍해, 원격에서 실행 중인 subagent의 행동을 그대로 관찰하는 방식(Claude Code v2.1.251). Trial의 "원격 sandbox 또는 격리된 terminal 기반 에이전트 실행"을 실제로 감시 가능하게 만드는 진전입니다. (sources/2026-08/2026-08-31.md)
- (2026-09-20 추가) Claude Code v2.1.274/275(09-17)에서 `/code-review`가 다수의 리뷰 서브에이전트를 띄우는 방식 대신 인라인 리뷰 프롬프트를 쓰는 방식으로 바뀌었습니다. Open Questions의 "subagent orchestration은 언제 단일 강한 모델보다 비용 대비 효과가 좋은가?"에 벤더가 실무에서 내놓은 답 중 하나로, 반복적인 리뷰 작업에는 오케스트레이션 오버헤드가 항상 이득은 아니라는 신호입니다. (sources/2026-09/2026-09-18.md)

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
- [Claude Code v2.1.260/261/263](../../sources/2026-09/2026-09-07.md#claude-code-v21260261263--diff-전체화면-패널-skill-doctor-조직-정책-가시성)
- [Claude Code v2.1.265](../../sources/2026-09/2026-09-09.md#anthropic-claude-code-v21265-배포--플러그인-디렉터리-동적-로드-아티팩트-퍼블리시-도구-검증-prompt-cache-재사용-버그-다수-수정)
- [Claude Code v2.1.266/267](../../sources/2026-09/2026-09-10.md#anthropic-claude-code-v21266267-배포--maxeffortlevel-설정-시스템-프롬프트-스냅샷-무효화-옵션-prompt-cache-안정화-다수)
- [Claude Code v2.1.268](../../sources/2026-09/2026-09-11.md#anthropic-claude-code-v21268-배포--webfetch-무한대기-수정-서드파티-호환-엔드포인트-http-400-회귀-수정-symlink-권한-규칙플러그인-토큰-노출-등-보안-수정-다수)
- [Claude Code v2.1.269/270](../../sources/2026-09/2026-09-14.md#anthropic-claude-code-v21269270-배포--claude-plugin-eval-output-style-workflow-동시-실행-한도-상향-prompt-cache-회귀-수정)
- [Claude Code v2.1.271](../../sources/2026-09/2026-09-15.md#anthropic-claude-code-v21271-배포--remote-세션-fast-mode-per-command-도메인-allowlist-플러그인-커맨드-승인--accept-command)
- [MCP Rust SDK(rmcp) v3.3.0](../../sources/2026-09/2026-09-15.md#model-context-protocol-rust-sdkrmcp-v330-릴리스--enterprise-refresh-token·id-jagjwt-authorization-grant-exchange-지원-추가)
- [Claude Code v2.1.272/273](../../sources/2026-09/2026-09-16.md#anthropic-claude-code-v21272273-배포--llm-게이트웨이용-요청-헤더-remote-세션-포크-allowed_domains-샌드박싱-정식화)
- [Claude Code v2.1.274/275](../../sources/2026-09/2026-09-18.md#anthropic-claude-code-v21274275-배포--mcp-streamable-http-타임아웃-설정-code-review-인라인-프롬프트-전환-claudeai-skillplugin-자동-동기화)
- [Claude Code v2.1.276~278](../../sources/2026-09/2026-09-21.md#anthropic-claude-code-v21276278-배포--서버사이드-auto-mode-분류기-기본값-전환-agentsmd-지원-gateway-egress-boundary-옵션)
- [Claude Code v2.1.280](../../sources/2026-09/2026-09-23.md#anthropic-claude-code-v21280-배포--claude-opus-55를-기본-opus-모델로-편입-1m-컨텍스트)
- [Claude Code v2.1.281](../../sources/2026-09/2026-09-24.md#anthropic-claude-code-v21281-배포--bedrock-guardrailassume_role-세션-재개-안정성-대규모-수정)
- [Claude Plugins 제출 포털](../../sources/2026-09/2026-09-28.md#anthropic-claude-plugins-디렉터리-제출-포털-공개--mcp-20stateless-coremcp-appsenterprise-managed-auth-지원)
- [Claude Code v2.1.282~284](../../sources/2026-09/2026-09-29.md#anthropic-claude-code-v21282284-배포--sonnet-55-기본-모델-편입-세션-재개프롬프트-캐시-안정성-다수-수정)
- [Claude Code v2.1.285](../../sources/2026-09/2026-09-30.md#anthropic-claude-code-v21285-배포--claude-plugin-configure---desktop-다수-세션-안정성-수정)
- [Claude Code v2.1.286](../../sources/2026-10/2026-10-01.md#anthropic-claude-code-v21286-배포--권한-프롬프트-카운터-다수-자격증명세션mcp-안정성-수정)
- [Claude Code v2.1.287](../../sources/2026-10/2026-10-02.md#anthropic-claude-code-v21287-배포--claude-mods-플러그인-체계-에이전트-뷰-필터-다수-mcpremote-control-안정성-수정)
- [Anthropic·Barclays 전사 확산 계약](../../sources/2026-10/2026-10-02.md#anthropicbarclays-claude-codeclaude-모델-전사-확산-계약-공개--2026년-말-개발자-50-claude-code-도입-목표-기존-colleague-knowledge-assistant-16만명-사용검색-100만건)
- [Claude Code v2.1.288~289](../../sources/2026-10/2026-10-05.md#anthropic-claude-code-v21288289-배포--모드플러그인-설정-기능-확장-다수-플러그인세션-안정성-수정)
- [Claude Frontier Academy](../../sources/2026-10/2026-10-05.md#anthropic-claude-frontier-academy-공개--100m-투자로-2027년-말까지-frontier-deployed-engineer-1만-명-양성-accenturedeloittemckinseymorgan-stanley-등-초기-참여)
- [Claude Code v2.1.290~292](../../sources/2026-10/2026-10-07.md#anthropic-claude-code-v21290292-배포--mod-훅-확장캐싱워크플로-에이전트-spawn-claude-plugin-install-마켓플레이스-지정-agent-tool-effort-파라미터-두-차례-회귀-수정)
- [Claude Code v2.1.293](../../sources/2026-10/2026-10-08.md#anthropic-claude-code-v21293-배포--mod-isdeferred-도구-등록-플래그-subagent-타입-구분-필드-추가-다수-안정성-수정과-21290-수정-1건-되돌림)
- [Claude Code v2.1.294~295 / Agent SDK parity](../../sources/2026-10/2026-10-09.md#anthropic-claude-code-v21294295-배포--instruction-기반-hook-우회-버그-수정-hook-onfailureblock-추가-claude-agent-sdkpythonts도-동시-parity-릴리스)
- [Claude Code v2.1.296](../../sources/2026-10/2026-10-12.md#anthropic-claude-code-v21296-배포--sonnet-55-cache-read-가격-010m-반영-mcp-tool-설명-길이-제한-20484096자-백그라운드-전환-시-실행-중-명령-중단-처리)
- [Claude Code HIPAA managed-settings 예제](../../sources/2026-10/2026-10-14.md#anthropic-claude-code-hipaa-환경용-managed-settings-예제-추가--examplesmanaged-settings에-hipaa-baselinejson--managed-mcplockdownjson--readme)
- [Claude Code v2.1.299~300 / Agent SDK parity](../../sources/2026-10/2026-10-15.md#anthropic-claude-code-v21299300-배포-claude-agent-sdkpython-v02166167-동시-parity--유휴-압축-gzip-요청-opentelemetry-cache-토큰-속성-추가)
- [Managed Agents Dynamic workflows(beta)](../../sources/2026-10/2026-10-15.md#claude-developer-platform-managed-agents-dynamic-workflowsbeta-공개--다수-에이전트를-단계phase로-묶어-실행하는-멀티에이전트-오케스트레이션-api)
- [Claude Code v2.1.301](../../sources/2026-10/2026-10-16.md#anthropic-claude-code-v21301-배포--사용량-한도-임박-시-재시도-중단-opentelemetry-도구-분류기-속성-추가-백그라운드-실행-중-명령-중단-안전장치-강화)
- [Claude Code v2.1.302~303](../../sources/2026-10/2026-10-19.md#anthropic-claude-code-v21302303-배포--fork-subagent-기본-활성화-auto-mode-분류기-모델-분리-설정-read-도구-128mb-이미지-상한)
- [Claude Code v2.1.304](../../sources/2026-10/2026-10-20.md#anthropic-claude-code-v21304-배포--code-review-레벨quickstandarddeep-mod-toolcheck의-decider-person-auto-mode-setup-전-플랫폼-확대)
- [Claude Code v2.1.305](../../sources/2026-10/2026-10-21.md#anthropic-claude-code-v21305-배포--sandboxallownestedusernamespaces-retry-watchdog의-usage-limit-재확인-toolsearch-미지원-게이트웨이-회귀-수정)
- [Claude Code v2.1.306~307](../../sources/2026-10/2026-10-22.md#anthropic-claude-code-v21306307-배포--claude_codesafety_event-opentelemetry-이벤트-claude-api-api-version-고정-mcp-중복-호출-수정)
- [Agent Skills를 AAIF에 이관](../../sources/2026-10/2026-10-23.md#anthropic-agent-skills-표준을-agentic-ai-foundationaaif에-이관-발표)
- [Claude Code v2.1.308~309](../../sources/2026-10/2026-10-23.md#anthropic-claude-code-v21308309-배포--샌드박스-우회-경로-다수-수정-ultrareview-workspace-trust-요구-github-멘션-오발송-수정)

## Open Questions

- 어떤 작업부터 agent에게 맡기고 어떤 작업은 반드시 사람 검토를 거쳐야 하는가?
- long-horizon task에서 성공률보다 더 먼저 측정해야 하는 실패 유형은 무엇인가?
- local coding agent의 기본 sandbox, network, credential 정책은 어떻게 잡아야 하는가?
