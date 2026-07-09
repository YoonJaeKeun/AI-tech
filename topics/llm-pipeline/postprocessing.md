---
title: "LLM 후처리 (Postprocessing)"
topic: llm-pipeline
last_reviewed: 2026-07-09
---

# 후처리 (Postprocessing)

후처리는 모델이 낸 raw 출력(로짓·토큰)을 사람이나 시스템이 실제로 쓸 수 있는 결과로 바꾸는 모든 단계입니다. 상위 요약은 [LLM Pipeline 허브](llm-pipeline.md)를 참고하세요.

모델 내부 레벨(로짓 → 토큰 → 텍스트)과 애플리케이션 레벨(파싱·검증·라우팅·가드레일)로 나뉩니다.

## 모델 내부 레벨

### 1. 로짓 산출 (Logits)

- 마지막 레이어가 다음 토큰 후보 전체(vocabulary 크기)에 대한 점수(logits)를 냅니다. 아직 확률도, 텍스트도 아닙니다.

### 2. 로짓 가공 (Logit processing)

- temperature scaling: 값이 높을수록 분포가 평탄해져 다양성이 커지고, 낮을수록 뾰족해져 결정적이 됩니다.
- repetition / frequency / presence penalty, `logit_bias`, bad-words 마스킹으로 특정 토큰을 억제·촉진합니다.
- top-k / top-p(nucleus) 필터로 후보를 축소합니다.
- 제약 디코딩(constrained / grammar decoding): JSON schema나 정규문법을 강제해 출력 형식이 항상 유효하도록 만듭니다.

### 3. 샘플링 (Sampling)

- greedy(항상 최고 확률) / temperature / top-p / top-k / beam search 중 선택합니다.
- 결정성: seed 고정 여부. temperature=0이라도 하드웨어·병렬 처리 때문에 완전히 결정적이지 않을 수 있습니다.

### 4. 자기회귀 디코딩 루프 (Autoregressive decoding)

- 토큰 하나 생성 → KV cache 갱신 → 다시 다음 토큰을 생성합니다. 출력 길이만큼 이 과정을 반복합니다.
- speculative decoding 등으로 이 루프를 가속합니다.

### 5. 정지 조건 (Stopping)

- EOS token, 사용자가 지정한 stop sequence, `max_tokens`, 시간 초과에서 멈춥니다.
- 정지 처리 실수는 답이 잘리거나(under-generation) 불필요하게 길어지는(over-generation) 문제로 이어집니다.

### 6. 디토큰화 (Detokenization)

- 토큰 ID를 다시 텍스트로 되돌립니다. special token 제거, subword 병합, 공백·대소문자 복원이 포함됩니다.

### 7. 스트리밍 (Streaming)

- 생성되는 델타 토큰을 즉시 전송합니다(SSE 등). 부분 출력에 대한 점진적 파싱이 필요해집니다.

## 애플리케이션 / 오케스트레이션 레벨

### 1. 파싱과 추출 (Parsing & extraction)

- reasoning/thinking 블록과 최종 답을 분리하고, tool call(함수명 + 인자)을 추출하며, 코드블록·마크다운 구조를 파싱합니다.
- 스트리밍 중이면 부분 파싱과 "언제 완결되었는지" 판단이 함께 필요합니다.

### 2. 구조화 출력 검증 (Structured output validation)

- JSON schema·타입 검증, 필수 필드 확인을 합니다.
- 어긋나면 재시도(repair prompt로 다시 요청)하거나, 애초에 모델 내부의 constrained decoding으로 폴백합니다.

### 3. 도구 라우팅과 실행 (Tool routing & dispatch)

- 추출한 호출을 실제 함수에 매핑하고, 인자 검증·권한 확인 후 실행하며, 결과를 정규화합니다.
- 실패는 숨기지 말고 관찰로 되돌려 모델이 스스로 재시도·수정하게 하는 것이 견고합니다.

### 4. 출력 가드레일 (Output guardrails)

- 유해성·안전성 필터, PII/PHI 유출 검사, grounding 검증(주장 vs 근거 대조로 환각 탐지), 정책·컴플라이언스 확인.

### 5. 후정렬과 포매팅 (Post-formatting)

- 사용자용 렌더링, 인용·각주 삽입, 단위·표기 정리, 민감정보 마스킹.

### 6. 평가와 로깅 (Eval & logging)

- 트레이싱, 토큰·비용 집계, 자동 품질 스코어링(LLM-as-judge 등), 사용자 피드백 수집으로 개선 루프를 만듭니다.

### 7. 종료 판정 (Termination — 에이전트 맥락)

- 도구 호출이 있으면 실행 후 그 결과를 다음 스텝의 전처리로 되돌리고, 없으면 최종 답으로 종료합니다. 이 판정이 [agent loop](../agents/agent-loop.md)를 돌립니다.

## 관련

- [전처리 (Preprocessing)](preprocessing.md): 반대편 절반. 모델 입력을 구성합니다.
- [LLM Pipeline 허브](llm-pipeline.md): 전체 파이프라인 다이어그램과 현재 판단.
- [Agent Loop](../agents/agent-loop.md): 이번 스텝의 후처리 결과(관찰)가 다음 스텝의 전처리 입력이 됩니다.
