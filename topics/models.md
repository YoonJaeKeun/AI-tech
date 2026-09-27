---
title: "Models"
topic: models
last_reviewed: 2026-09-27
---

# Models

기초 모델, 추론 모델, 멀티모달 모델, 오픈 모델, 모델 라우팅과 관련된 누적 정리입니다.

## Current View

- frontier 모델 경쟁은 "정답률 높은 챗봇"에서 "추론 effort, 긴 context, tool use, cost tier, safety layer를 조합한 시스템" 경쟁으로 이동하고 있습니다.
- 최신 발표들은 coding, biology, cybersecurity, agentic workflow 같은 실제 실행형 작업을 강하게 강조합니다.
- open-weight 모델은 접근성과 privacy 측면에서 중요해졌지만, release 이후 회수가 어렵고 safeguard 제거가 쉽다는 리스크가 있습니다.

## Key Concepts

- Inference scaling: 응답 시점에 더 많은 계산과 추론 단계를 쓰는 방식입니다.
- Reasoning effort: 사용자가 작업 난이도에 따라 모델의 사고 깊이와 비용을 조절하는 제품 패턴입니다.
- Model family: flagship, balanced, fast/cheap 모델을 함께 제공해 routing과 비용 최적화를 가능하게 하는 구성입니다.
- Open-weight vs open-source: weights 공개와 training data/code 공개는 다릅니다.
- System card: 모델의 capability, limitation, safety evaluation을 기록한 문서입니다.

## Notable Systems

- OpenAI GPT-5.6 Sol/Terra/Luna: Sol은 flagship preview, Terra는 균형형, Luna는 저비용형으로 소개되었습니다.
- Anthropic Claude Sonnet 5: Sonnet급 모델에서 agentic coding과 tool use 성능을 크게 끌어올린 사례입니다.
- Google Gemini 3.5 series: Antigravity와 Managed Agents 흐름에서 agent-first 개발 플랫폼과 함께 제시되었습니다.
- Llama, DeepSeek, Qwen 계열 open-weight 모델: 폐쇄형 frontier와의 격차 축소와 배포 리스크를 동시에 봐야 합니다.
- (2026-09-27 추가) Anthropic Claude Opus 5.5(2026-09-22 공개, 원문 확인): Claude Fable 5.1급 성능을 Opus 5 대비 약 40% 낮은 비용(입력 $4/출력 $20 per Mtok, 캐시 읽기 $0.20)에 제공하며 처리 속도는 30% 이상 빠릅니다. Terminal-Bench 4.0 66.4%, GDPval-AA v2.1 1846 Elo, OSWorld 2.0 81.8%를 제시했고, METR·Frontier Design 등 외부 평가자의 사전 검증을 거쳤다고 밝혔습니다. (sources/2026-09/2026-09-23.md)

## Key Concepts

- (2026-09-27 추가) Frontier science capability: 모델의 실행형 능력이 coding·agentic workflow를 넘어 기초과학 연구 자체로 확장되는 사례입니다. Anthropic이 2026-09-23 공개한 사례(원문 확인)에서는 Claude Science·Claude Code 기반 에이전트 파이프라인 약 950개가 21시간 동안 2억 1천만 토큰을 써서 DNA 서열 데이터베이스에서 CRISPR와 유사한 신규 효소계(ART)를 찾아냈고, 실제 습식 실험은 사람 과학자가 수행했습니다. CURRENT.md Assess의 "frontier science, biology, cyber capability 평가"가 지금까지 주로 오용 가능성 쪽에서 다뤄졌는데, 이번 사례는 유용성 쪽 구체 사례입니다. 이 축이 반복되면 `models`나 `clinical-healthcare`와 별개로 새 topic 슬러그(`frontier-science` 등) 신설을 검토할 근거로 남깁니다. (sources/2026-09/2026-09-24.md)

## Evaluation Notes

- 모델 선택은 단일 leaderboard보다 사용 목적별로 봐야 합니다: coding, terminal work, multimodal, clinical, safety, cost, latency.
- benchmark saturation 때문에 "잘 정의된 문제를 맞히는 능력"과 "실제 업무를 끝까지 수행하는 능력"을 분리해서 봐야 합니다.
- 비용 지표는 input/output token 가격뿐 아니라 retry, 실패 복구, human review 시간을 포함해야 합니다.

## Sources

- [Stanford AI Index 2026](../sources/2026-07/2026-07-09.md#the-2026-ai-index-report)
- [OpenAI GPT-5.6 Sol Preview](../sources/2026-07/2026-07-09.md#previewing-gpt-56-sol)
- [Anthropic Claude Sonnet 5](../sources/2026-07/2026-07-09.md#introducing-claude-sonnet-5)
- [Google I/O 2026 Developer Keynote](../sources/2026-07/2026-07-09.md#google-io-2026-developer-keynote-agentic-workflow)
- [International AI Safety Report 2026](../sources/2026-07/2026-07-09.md#international-ai-safety-report-2026)
- [Claude Opus 5.5](../sources/2026-09/2026-09-23.md#anthropic-claude-opus-55-공개--fable-51급-성능을-opus-5-대비-40-낮은-비용에)
- [Anthropic 생명과학 연구소, ART 효소계 발견](../sources/2026-09/2026-09-24.md#anthropic-새-생명과학-연구소-공개--claude-에이전트-950개가-crispr-유사-신규-효소계art-발견)

## Open Questions

- reasoning effort를 높이는 것이 어떤 업무에서 실제 ROI로 이어지는가?
- open-weight 모델을 임상 데이터 환경에서 local/private하게 쓰는 것이 안전성과 운영비 측면에서 실용적인가?
- 모델 routing을 사람이 직접 고르는 방식과 자동 router 중 어떤 방식이 검증 가능성이 높은가?
