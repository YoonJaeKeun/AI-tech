---
title: "Safety / Governance"
topic: safety-governance
last_reviewed: 2026-08-30
---

# Safety / Governance

AI 안전성, 거버넌스, 규제, 배포 통제, 책임 있는 사용을 정리하는 주제 파일입니다.

## Current View

- capability는 빠르게 올라가지만 responsible AI benchmark, transparency, incident tracking, post-deployment monitoring은 뒤처지는 흐름입니다.
- 에이전트는 도구를 직접 사용하고 실제 action을 수행하므로 기존 챗봇보다 실패 비용이 큽니다.
- open-weight 모델은 연구와 접근성을 넓히지만, safeguard 제거와 회수 불가능성 때문에 별도 리스크 판단이 필요합니다.

## Risk Areas

- Cyber and bio capability: 방어적 활용과 오용 가능성이 동시에 커지는 영역입니다.
- Prompt injection and tool hijacking: 에이전트가 외부 도구를 사용할 때 중요합니다.
- Data leakage: PHI, PII, source code, credential 노출 리스크입니다.
- Evaluation gap: controlled benchmark와 실제 deployment 사이의 차이입니다.
- Irreversible release: open-weight 모델이 공개된 뒤에는 일괄 rollback이 어렵습니다.

## Operating Principles

- 고위험 action에는 human approval을 둡니다.
- 민감정보는 public endpoint에 넣지 않습니다.
- tool permission은 최소 권한으로 시작합니다.
- (2026-08-30 추가) 표준 프로토콜(MCP) 자체가 Client ID Metadata Documents, Enterprise-Managed Authorization 같은 인증 기능을 내장하는 방향으로 진화하고 있어, 최소 권한 원칙을 프로토콜 레벨에서 뒷받침할 수 있는지 다음 실험에서 확인할 대상입니다. (sources/2026-08/2026-08-24.md)
- model output은 source, version, prompt, reviewer를 함께 기록합니다.
- post-deployment monitoring과 incident log를 처음부터 설계합니다.

## Sources

- [International AI Safety Report 2026](../sources/2026-07/2026-07-09.md#international-ai-safety-report-2026)
- [METR Frontier Risk Report](../sources/2026-07/2026-07-09.md#metr-frontier-risk-report-february-to-march-2026)
- [OpenAI GPT-5.6 Sol Preview](../sources/2026-07/2026-07-09.md#previewing-gpt-56-sol)
- [FDA AI-Enabled Medical Devices](../sources/2026-07/2026-07-09.md#fda-ai-enabled-medical-devices)
- [The New MCP Roadmap](../sources/2026-08/2026-08-24.md#the-new-mcp-roadmap)

## Open Questions

- 개인/팀 수준에서 최소한의 AI incident log는 어떤 형태가 좋은가?
- agent tool permission 정책을 업무별로 어떻게 표준화할 것인가?
- open-weight 모델을 사용할 때 safety update와 model provenance를 어떻게 추적할 것인가?
