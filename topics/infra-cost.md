---
title: "Infra / Cost"
topic: infra-cost
last_reviewed: 2026-10-04
---

# Infra / Cost

추론 비용, 가격 정책, 서빙 최적화, 하드웨어와 관련된 누적 정리입니다.
`CURRENT.md` Snapshot이 "비용 효율 경쟁"을 핵심 흐름으로 보고 있어 별도 주제로 분리했습니다.

## Current View

- 아직 자료가 쌓이지 않았습니다. 이 축은 2026-08-24에 수집 대상으로 추가했습니다.
- (2026-08-30 갱신) 첫 원문 확인 자료가 들어왔습니다: 오픈소스 서빙 엔진(vLLM)이 최신 open-weight 모델(Kimi-K3, DeepSeek V4)용 최적화를 계속 추가하며, 모델 가격 인하·전용 추론 칩과 나란히 "서빙 소프트웨어" 축에서도 비용 효율 경쟁이 진행 중입니다. (sources/2026-08/2026-08-27.md)
- (2026-09-20 갱신) 위 흐름이 이어집니다. vLLM v0.29.0은 Model Runner V2를 모든 모델의 기본값으로 승격하고 CUDA graph 메모리 프로파일링으로 KV cache 크기를 자동 산정하며, 특정 아키텍처의 decode 커널에 deterministic matmul을 적용해 약 3배 성능 향상을 보고합니다. 서빙 엔진 자체의 개선이 벤더 가격 인하 못지않게 실제 운영 비용에 직접 영향을 준다는 판단을 뒷받침합니다. (sources/2026-09/2026-09-14.md)
- (2026-09-27 갱신) 벤더 가격 인하 축에서 새 사례가 나왔습니다. Anthropic Claude Opus 5.5(2026-09-22, 원문 확인)는 Opus 5 대비 약 40% 낮은 비용(입력 $4/출력 $20, 캐시 읽기 $0.20 per Mtok, 60% 인하)에 유사 성능을 제공한다고 밝혔습니다. Snapshot의 "비용 효율 경쟁"이 flagship 모델 라인에서도 계속되고 있다는 근거입니다. (sources/2026-09/2026-09-23.md)
- (2026-10-04 갱신) Anthropic·Barclays의 전사 확산 계약(2026-10-01, 원문 확인)은 Colleague Knowledge Assistant 1.6만명 이상 사용·검색 100만 건+, Global Markets 일일 이메일 12만 건 처리 같은 사용 규모 수치를 공개했지만, 구체적인 비용 절감액이나 절감 시간 수치는 포함하지 않았습니다. Evaluation Questions의 "같은 작업을 같은 품질로 끝내는 데 드는 총비용은 얼마인가"에 대해, 벤더 발표가 사용 규모는 보여주면서도 ROI 수치는 비워두는 패턴이 반복되고 있다는 점을 보여줍니다. (sources/2026-10/2026-10-02.md)

## Notable Systems

- vLLM v0.28.0 (2026-08-26 태그): Kimi-K3용 Decode Context Parallel·fused FlashKDA 커널·shared-expert 메모리 절감, DeepSeek V4용 end-to-end Sparse MLA, Model Runner V2의 E/P/D disaggregation·weight offloading. 원문(GitHub 릴리스 페이지)을 직접 확인했습니다. (sources/2026-08/2026-08-27.md)
- vLLM v0.29.0 (2026-09-09 태그): Model Runner V2 기본화, CUDA graph 메모리 프로파일링 기반 KV cache 자동 산정, batch-sharded sampling으로 스텝당 logits 메모리를 텐서 병렬(TP) 비율의 1/TP로 절감, 일부 아키텍처 decode 커널에 deterministic matmul 적용으로 약 3배 성능 향상. Model Runner V1은 deprecated 상태로 v0.32에서 제거 예정입니다. 원문(GitHub 릴리스 페이지)을 직접 확인했습니다. (sources/2026-09/2026-09-14.md)
- llama.cpp v0.4.1 (2026-09-14 태그): Maple 20B-A1B·Tencent Hy 4·Spark2.5 모델 지원 추가, 내부 ggml 라이브러리를 v0.24.0으로 갱신, 구조화된 JSONL 로깅과 서버 자식 프로세스 관리 개선. 원문(GitHub 릴리스 페이지)을 직접 확인했습니다. (sources/2026-09/2026-09-15.md)

## Watch Items

- frontier 모델 가격 인하와 tier 재편 (flagship / balanced / fast).
- prompt caching, batch API, context 압축 등 비용 절감 기능.
- 추론 최적화: speculative decoding, quantization, KV cache, serving 스택.
- GPU/가속기 공급과 가격, 클라우드 리전별 가용성.
- self-host vs API의 손익분기, open-weight 모델의 실제 운영 비용.

## Evaluation Questions

- 같은 작업을 같은 품질로 끝내는 데 드는 총비용은 얼마인가? (retry와 human review 포함)
- 가격 인하가 실제 사용 패턴을 바꾸는 임계점은 어디인가?
- reasoning effort와 context 길이를 조절할 때 비용 대비 품질 곡선은 어떤 모양인가?

## Sources

- [vLLM v0.28.0 릴리스](../sources/2026-08/2026-08-27.md#vllm-v0280-릴리스-kimi-k3deepseek-v4-최적화-model-runner-v2-성숙)
- [vLLM v0.29.0 릴리스](../sources/2026-09/2026-09-14.md#vllm-v0290-릴리스--model-runner-v2-기본화-deterministic-matmul로-decode-커널-약-3배-성능-향상)
- [llama.cpp v0.4.1 릴리스](../sources/2026-09/2026-09-15.md#ggml-org-llamacpp-v041-릴리스--maple-20b-a1b·tencent-hy-4·spark25-모델-지원-ggml-v0240으로-갱신)
- [Claude Opus 5.5](../sources/2026-09/2026-09-23.md#anthropic-claude-opus-55-공개--fable-51급-성능을-opus-5-대비-40-낮은-비용에)
- [Anthropic·Barclays 전사 확산 계약](../sources/2026-10/2026-10-02.md#anthropicbarclays-claude-codeclaude-모델-전사-확산-계약-공개--2026년-말-개발자-50-claude-code-도입-목표-기존-colleague-knowledge-assistant-16만명-사용검색-100만건)

## Open Questions

- 개인 스터디 수준에서 비용을 어떻게 재현 가능하게 측정할 것인가?
- 에이전트 workflow의 비용은 모델 단가보다 harness 설계에 더 좌우되는가?
