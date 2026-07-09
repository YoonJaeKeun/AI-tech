---
title: "LLM 전처리와 후처리"
topic: agents
last_reviewed: 2026-07-09
---

# LLM 전처리와 후처리

전처리와 후처리는 [agent loop](agent-loop.md) 안에서 매 스텝 LLM 호출을 감싸는 양쪽 절반입니다. 전처리는 "모델에 넣을 입력을 만드는 과정", 후처리는 "모델 출력을 루프가 쓸 수 있게 바꾸는 과정"입니다. 각각 애플리케이션(에이전트) 레벨과 모델 내부 레벨로 나눠 보면 정리가 쉽습니다.

## 전처리 (Preprocessing) — 입력을 만든다

애플리케이션/에이전트 레벨 (루프가 매 스텝 실제로 하는 일):

- Context assembly: system prompt + 도구 정의(tool schema) + 대화 이력 + 직전 관찰 결과를 하나의 입력으로 조립합니다.
- Context window 관리: 길어진 이력을 truncation, 요약, sliding window, compaction으로 예산 안에 맞춥니다.
- Retrieval(RAG): 질의에 맞는 문서를 검색해 컨텍스트에 주입합니다.
- Memory 주입: 장기 memory, scratchpad, 이전 세션 요약을 끌어옵니다.
- Message formatting: system / user / assistant / tool 역할 구조로 배치하고 chat template을 적용합니다.
- Input guardrail: prompt injection 필터링, PII 마스킹, 민감 입력 차단.
- Few-shot / instruction: 예시와 출력 형식 지시를 덧붙입니다.

모델 내부 레벨 (호출이 실제로 모델에 들어갈 때):

- Tokenization: 텍스트를 토큰으로 분할합니다(BPE 등). 비용과 context 한계가 여기서 결정됩니다.
- Special token / chat template: 역할 경계와 turn 구분 토큰을 삽입합니다.
- Embedding: 토큰을 벡터로 변환합니다.
- Positional encoding: 토큰 순서 정보를 더합니다.

## 후처리 (Postprocessing) — 출력을 해석한다

모델 내부 레벨 (출력이 나오는 순간):

- Sampling: logits에서 실제 토큰을 고릅니다. temperature, top-p, top-k, greedy 등이 여기서 작동합니다.
- Detokenization: 토큰을 다시 텍스트로 되돌립니다.
- Stop 처리: stop token이나 stop sequence를 만나면 생성을 멈춥니다.
- Streaming: 토큰을 나오는 대로 흘려보냅니다.

애플리케이션/에이전트 레벨 (루프가 출력을 받아 하는 일):

- Parsing: 출력에서 tool call을 추출하고, thinking/reasoning과 최종 답변을 분리합니다.
- Structured output 검증: JSON schema 등에 맞는지 확인하고, 어긋나면 재시도(모델에게 다시 요청)합니다.
- Tool routing: 추출한 tool call을 실제 함수로 dispatch합니다.
- Output guardrail: 안전성 필터링, grounding/hallucination 점검, content moderation.
- Termination 판정: 도구 호출이 없으면 종료로 보고 최종 답을 사용자에게 전달합니다.

## 루프와의 연결

정리하면 agent loop의 한 스텝은 이렇게 펼쳐집니다.

```text
[전처리: 컨텍스트 조립 → 토큰화]
      → [LLM 추론]
      → [후처리: 샘플링/디토큰화 → tool call 파싱 → 검증]
      → 도구 실행 → 관찰 → (다음 스텝의 전처리로 관찰 결과가 다시 들어감)
```

즉 이번 스텝의 후처리 결과(관찰)가 다음 스텝의 전처리 입력이 되면서 루프가 돕니다. 에이전트 품질은 대부분 이 전처리(무엇을 컨텍스트에 넣는가)와 후처리(출력을 얼마나 견고하게 파싱·검증하는가)의 설계에서 갈립니다.

## 관련

- [Agent Loop](agent-loop.md): 추론-행동-관찰 반복 구조와 변형.
- [Agents 허브](agents.md): 현재 판단, 목차, 대표 소스.
