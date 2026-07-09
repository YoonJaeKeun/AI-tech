---
title: "Evals / Benchmarks"
topic: evals-benchmarks
last_reviewed: 2026-07-09
---

# Evals / Benchmarks

AI 모델과 에이전트의 성능을 어떻게 측정할지 정리하는 주제 파일입니다.

## Current View

- 전통적인 QA, 시험, 단일 정답 benchmark는 빠르게 포화되고 있습니다.
- 2026년 현재 중요한 평가는 실제 업무에 가까운 coding, terminal, computer use, long-horizon task, clinical workflow 평가입니다.
- benchmark 점수는 모델 선택의 시작점일 뿐이며, 실제 업무에서는 failure mode, 비용, 복구 가능성, auditability가 더 중요할 수 있습니다.

## Benchmarks To Track

- SWE-bench Verified: 실제 GitHub issue 해결 능력을 보는 coding benchmark입니다.
- Terminal-Bench: terminal 환경에서 command-line workflow를 수행하는 agent benchmark입니다.
- METR Time Horizon: AI agent가 어느 정도 길이의 소프트웨어 작업을 성공적으로 수행하는지 측정합니다.
- OSWorld / OSWorld-Verified: 컴퓨터 사용과 GUI workflow 수행력을 보는 평가입니다.
- BrowseComp: agentic search와 정보 탐색 성능을 보는 평가입니다.
- Clinical workflow evals: prospective trial, post-deployment monitoring, real-world task 기반 평가가 중요합니다.

## Evaluation Questions

- 이 benchmark는 실제 업무와 얼마나 닮았는가?
- 모델이 실패할 때 실패를 감지할 수 있는가?
- 같은 비용으로 retry와 human review를 포함하면 어떤 모델이 나은가?
- 평가 대상이 model 자체인가, agent harness인가, 전체 workflow인가?
- 결과가 재현 가능하고 감사 가능한가?

## Sources

- [Terminal-Bench 2.0](../sources/2026-07/2026-07-09.md#terminal-bench-20)
- [METR Frontier Risk Report](../sources/2026-07/2026-07-09.md#metr-frontier-risk-report-february-to-march-2026)
- [Stanford AI Index 2026](../sources/2026-07/2026-07-09.md#the-2026-ai-index-report)
- [State of Clinical AI Report 2026](../sources/2026-07/2026-07-09.md#state-of-clinical-ai-report-2026)

## Open Questions

- 개인 스터디에서 매달 고정으로 확인할 benchmark는 무엇으로 제한할 것인가?
- 임상 데이터/EDC 업무에 맞는 작은 내부 benchmark를 만들 수 있는가?
- benchmark saturation 이후에는 어떤 qualitative evidence를 함께 기록해야 하는가?
