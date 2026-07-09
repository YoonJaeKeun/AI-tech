---
title: "LLM 전처리 (Preprocessing)"
topic: llm-pipeline
last_reviewed: 2026-07-09
---

# 전처리 (Preprocessing)

전처리는 사용자 요청과 주변 맥락을 "모델이 실제로 받는 최종 입력(토큰 시퀀스)"으로 바꾸는 모든 단계입니다. 상위 요약은 [LLM Pipeline 허브](llm-pipeline.md)를 참고하세요.

크게 두 레벨로 나뉩니다. 앞쪽(애플리케이션/오케스트레이션 레벨)은 개발자가 설계·통제하는 영역이고, 뒤쪽(모델 내부 레벨)은 모델·서빙 스택이 담당하지만 비용·한계·품질에 직접 영향을 줍니다.

## 애플리케이션 / 오케스트레이션 레벨

### 1. 입력 수집과 정규화 (Input collection & normalization)

- 사용자 입력, system/developer 지시, 이전 대화, 도구 실행 결과, 첨부(이미지·문서)를 한데 모읍니다.
- 인코딩 정규화(UTF-8, 유니코드 NFC), 제어문자·과도한 공백 제거, 필요 시 언어 감지.
- 멀티모달 입력은 이 단계에서 참조(파일 핸들·URL)와 형식을 정리합니다.

### 2. 프롬프트 구성 (Prompt construction)

- system prompt(역할·정책·톤), developer instruction, few-shot 예시, 출력 형식 지시를 조립합니다.
- 도구 정의(tool/function schema): 이름, 설명, 파라미터 JSON schema를 함께 넣어 모델이 어떤 도구를 어떻게 부를지 알게 합니다.
- 프롬프트 템플릿에 변수 슬롯을 채워 렌더링하고, 프롬프트 버전을 관리합니다.

### 3. 컨텍스트 조립 (Context assembly)

- 대화 이력 + 최신 관찰 + 검색 결과를 하나의 입력으로 우선순위대로 배치합니다.
- 무엇을 앞/뒤에 둘지 결정합니다. 중요한 지시는 입력의 처음과 끝 경계에 두는 것이 일반적으로 더 잘 지켜집니다(중간에 묻히는 "lost in the middle" 문제).
- 중복·모순 정보를 정리합니다.

### 4. 검색 증강 (Retrieval / RAG)

- 쿼리 임베딩 → 벡터 검색(또는 키워드와의 하이브리드) → 리랭킹 → 상위 청크 선택.
- 청크 크기와 중복(overlap), 출처 메타데이터·인용 앵커를 부착해 컨텍스트에 주입합니다.
- 실패 모드: 관련 없는 청크가 컨텍스트를 오염시키면 오히려 환각·오답을 유발합니다. 정밀도(precision)가 재현율(recall)보다 중요할 때가 많습니다.

### 5. 메모리 주입 (Memory)

- 단기 메모리: 현재 세션의 스크래치패드, 중간 결론.
- 장기 메모리: 사용자 프로필, 과거 대화 요약, 지식 스토어. 무엇을 언제 로드할지와 신선도(오래된 사실의 갱신)가 관건입니다.

### 6. 컨텍스트 예산 관리 (Context window budgeting)

- 남은 토큰 예산을 계산합니다(입력 + 예상 출력 ≤ 모델 한계).
- 초과를 막는 기법: truncation(오래된 것부터 자르기), 요약·압축(compaction), sliding window, 우선순위 기반 드롭.
- 목적은 세 가지입니다. 한계 초과 방지, 비용·지연 최소화, 중요한 정보 보존. 이 셋의 균형이 설계 포인트입니다.

### 7. 입력 가드레일 (Input guardrails)

- prompt injection / jailbreak 패턴을 탐지·차단합니다. 특히 검색 문서나 도구 결과처럼 신뢰도가 낮은 출처에서 온 텍스트를 경계합니다.
- PII/PHI 마스킹·레닥션, 정책 위반 입력 필터링. 민감 데이터가 외부 모델로 나가지 않게 통제합니다.

### 8. 캐싱 준비 (Prompt / prefix caching)

- 고정 프리픽스(system prompt + 도구 정의 + 안정적인 컨텍스트)를 캐시 경계에 배치해 반복 호출의 비용·지연을 크게 줄입니다.
- 자주 바뀌는 부분은 뒤로 몰아 캐시 적중률을 높이는 방향으로 컨텍스트를 배열합니다.

### 9. 직렬화와 메시지 포매팅 (Serialization & message formatting)

- role 구조(system / user / assistant / tool)로 배열하고, 멀티모달 파트(예: base64 이미지)를 인코딩해 API 스키마에 맞게 직렬화합니다.

## 모델 내부 레벨

### 1. 채팅 템플릿 적용 (Chat template)

- 역할 경계와 turn 구분 special token을 삽입합니다(예: `<|im_start|>role … <|im_end|>`, `[INST] … [/INST]`), 그리고 BOS/EOS.
- 모델마다 템플릿이 다르며, 학습 때와 다른 템플릿을 쓰면 성능이 눈에 띄게 떨어집니다.

### 2. 토큰화 (Tokenization)

- 텍스트를 subword 토큰(BPE / Unigram / WordPiece)으로 분할하고 vocabulary ID로 매핑합니다.
- 비용과 컨텍스트 한계가 여기서 결정됩니다. 언어·형식에 따라 토큰 효율이 달라 비영어·비정형 텍스트나 특정 코드가 더 많은 토큰을 소모합니다.
- special token, 숫자·공백 처리 방식이 결과에 영향을 줍니다.

### 3. 임베딩 조회 (Embedding lookup)

- 토큰 ID를 dense vector로 변환합니다(embedding matrix). 이 벡터열이 트랜스포머의 입력이 됩니다.

### 4. 위치 인코딩 (Positional encoding)

- absolute / RoPE(rotary) / ALiBi 등으로 토큰의 순서와 상대 거리 정보를 부여합니다.
- 긴 컨텍스트 확장(길이 외삽)과 직접 관련된 부분입니다.

### 5. 어텐션 마스크와 패딩 (Attention mask & padding)

- causal mask로 미래 토큰을 가리고, 배치 처리 시 padding과 그에 대한 mask를 적용합니다. 서빙에서 KV cache 초기화와 연결됩니다.

## 관련

- [후처리 (Postprocessing)](postprocessing.md): 반대편 절반. 모델 출력을 해석·검증합니다.
- [LLM Pipeline 허브](llm-pipeline.md): 전체 파이프라인 다이어그램과 현재 판단.
- [Agent Loop](../agents/agent-loop.md): 에이전트는 매 스텝 이 전처리를 다시 수행합니다.
