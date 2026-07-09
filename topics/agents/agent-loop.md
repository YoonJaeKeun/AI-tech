---
title: "Agent Loop"
topic: agents
last_reviewed: 2026-07-09
---

# Agent Loop

에이전트의 핵심 제어 구조에 대한 세부 노트입니다. 상위 요약은 [Agents 허브](agents.md)를 참고하세요.

## 한 줄 정의

Agent loop는 LLM이 "추론 → 행동(도구 호출) → 관찰"을 목표가 끝날 때까지 반복하는 제어 구조입니다. LLM을 한 번 호출하고 끝내는 single-shot과 달리, 도구 실행 결과를 다시 입력으로 넣어 모델이 스스로 다음 수를 정하게 하는 while loop가 핵심입니다.

- single-shot: 프롬프트 → 답변. 끝.
- agent loop: 목표 → (모델 판단) → 도구 실행 → 결과 관찰 → 다시 모델 판단 → … → 종료.

## 한 사이클의 흐름

```text
┌─────────────────────────────────────────────┐
│ 1. 추론    "지금 상황에서 뭘 해야 하지?"      │
│      ↓                                        │
│ 2. 행동 결정  도구를 호출할지 / 끝낼지 판단   │
│      ↓  (도구 호출을 택하면)                  │
│ 3. 도구 실행  파일 읽기, 검색, 코드 실행 등   │
│      ↓                                        │
│ 4. 관찰    실행 결과를 컨텍스트에 추가         │
│      └──────────── 다시 1번으로 ──────────────┘
└─────────────────────────────────────────────┘
       종료 조건 충족 시 루프 탈출 → 최종 답변
```

의사코드로 보면 실체는 단순합니다.

```python
messages = [{"role": "user", "content": goal}]

while True:
    response = llm(messages, tools=available_tools)   # 1. 추론 (호출 앞뒤로 전처리/후처리)
    messages.append(response)

    if not response.tool_calls:                        # 2. 도구 호출이 없으면
        return response.text                           #    = 끝났다는 신호

    for call in response.tool_calls:                   # 3. 도구 실행
        result = execute(call)
        messages.append({"role": "tool", "content": result})  # 4. 관찰
    # 루프 반복
```

Claude Code, Cursor, 자율 리서치 에이전트도 본질은 이 구조의 확장판입니다.

## 왜 루프여야 하는가

모델은 미리 계획을 다 세울 수 없습니다. 파일을 열기 전엔 내용을 모르고, 검색을 돌리기 전엔 결과를 모릅니다. 그래서 "한 걸음 두고 → 결과 보고 → 다음 걸음 정하기"를 반복해야 합니다. 이렇게 추론과 행동을 번갈아 하는 방식을 ReAct(Reasoning + Acting) 패턴이라고 부릅니다. 루프의 본질은 모델에게 자기 행동의 결과를 관찰하고 경로를 수정할 피드백을 주는 것입니다.

## 구성 요소

- Model: 매 스텝 무엇을 할지 판단. 없으면 아무 결정도 못 함.
- Tools: 외부 세계에 실제로 작용. 없으면 생각만 하고 행동 불가.
- Context/Memory: 지금까지의 대화와 관찰 누적. 없으면 매 스텝 처음부터 시작.
- Termination: 언제 멈출지. 없으면 무한 루프.

## 실무에서 까다로운 지점

- Termination: 모델이 "끝났다"를 어떻게 아는가. 보통 도구 호출 없이 최종 답을 내면 종료로 봅니다. 못 멈추는 경우를 막는 max-steps 상한도 필수입니다.
- Context 관리: 루프가 길어지면 관찰이 쌓여 context window를 넘칩니다. 요약, 압축(compaction), 외부 memory가 필요해지는 지점입니다.
- Error 처리: 도구 실패 시 그 에러를 관찰로 넣어주면 모델이 스스로 재시도하고 수정합니다. 견고함의 큰 부분입니다.
- 병렬 도구 호출: 한 스텝에서 독립적인 도구 여러 개를 동시에 부를지.
- Planning: 단순 반응형 루프에 "먼저 계획을 세우고 시작"을 얹는 변형(Plan-and-Execute)과, 중간에 스스로 점검하는 Reflection 변형이 있습니다.

## 변형 비교

- Reactive loop: 매 스텝 즉흥 판단. 단순하지만 long-horizon에서 목표를 잃기 쉬움.
- Plan-and-Execute: 먼저 전체 계획을 세우고 단계별 실행. 계획이 틀리면 경직될 수 있어 재계획(replan) 단계가 필요.
- Reflection: 행동 후 스스로 결과를 비평하고 다음 행동을 교정. 품질은 오르지만 token과 latency 비용 증가.

## 관련

- [LLM 전처리와 후처리](llm-pre-post-processing.md): 매 스텝 LLM 호출을 감싸는 입력 조립과 출력 파싱·검증.
- [Agents 허브](agents.md): 현재 판단, 목차, 대표 소스.
