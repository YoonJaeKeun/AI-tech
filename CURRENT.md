---
title: "Current AI Tech View"
last_reviewed: 2026-07-09
review_cycle: monthly
---

# Current AI Tech View

이 문서는 2026-07-09 기준 AI 기술동향 판단을 한 장으로 유지하는 곳입니다. 자세한 근거는 `sources/`와 `timeline/`에 남기고, 여기에는 지금의 결론만 간결하게 둡니다.

## Snapshot

- 가장 중요하게 볼 흐름: AI는 단일 챗봇 성능 경쟁에서 도구 사용, 장기 작업, 에이전트 실행, 비용 효율, 안전 장치 경쟁으로 이동하고 있습니다.
- 최근 판단이 바뀐 부분: 모델 자체의 지능보다 "어떤 harness와 workflow로 쓰는가"가 실제 성능 차이를 크게 만듭니다.
- 다음 월간 리뷰 때 다시 확인할 부분: GPT-5.6 계열의 일반 공개 여부, Claude Sonnet 5의 실사용 평가, Google Antigravity/Gemini 3.5의 개발자 생태계 확산, 임상 AI의 전향적 검증 사례.

## Tech Radar

### Adopt

지금 바로 활용하거나 학습 우선순위를 높일 만한 기술입니다.

- 제한된 범위의 코딩 에이전트: 테스트, diff review, 사람 승인 절차가 있는 저장소 작업.
- 소스 노트 기반 스터디 운영: `sources/`에 근거를 남기고 `CURRENT.md`에는 현재 판단만 유지.
- Terminal-Bench, SWE-bench, METR Time Horizon 같은 workflow 중심 평가 렌즈.

### Trial

작게 실험해보고 적용 가능성을 확인할 기술입니다.

- subagent orchestration: 큰 작업을 조사, 구현, 검증 역할로 나누는 방식.
- 원격 sandbox 또는 격리된 terminal 기반 에이전트 실행.
- 임상/헬스케어의 비진단성 행정 업무 보조: 문서 요약, 질의 초안, 코딩/분류 보조.
- 긴 context와 추론 effort를 조절하는 모델 선택 전략.

### Assess

흐름은 중요하지만 아직 더 관찰해야 하는 기술입니다.

- open-weight 모델의 폐쇄형 frontier 모델 추격과 그에 따른 배포 리스크.
- 장기 자율 에이전트: 성능은 빠르게 늘지만 실패 비용과 감시 방식이 아직 미성숙.
- frontier science, biology, cyber capability 평가: 유용성과 오용 가능성이 동시에 커지는 영역.
- clinical AI에서 환자-facing agent와 clinical decision support의 실제 outcome 개선 여부.

### Hold

현재 기준으로는 과장, 비용, 리스크가 커서 보류할 기술입니다.

- prospective evaluation 없이 임상 의사결정을 자동화하는 사용.
- benchmark 점수만 보고 모델을 선택하는 방식.
- PHI, PII, confidential data를 공개 LLM에 직접 넣는 사용.
- 감사 로그와 rollback 전략이 없는 완전 자율 업무 실행.

## Watchlist

계속 지켜볼 제품, 논문, 벤치마크, 규제, 오픈소스 프로젝트입니다.

- OpenAI GPT-5.6 Sol/Terra/Luna preview의 일반 공개와 system card.
- Anthropic Claude Sonnet 5의 실제 agentic coding 성능과 비용 효율.
- Google Gemini 3.5 및 Antigravity/Managed Agents 확산.
- Terminal-Bench 3.0, SWE-Bench Pro, OSWorld-Verified, BrowseComp.
- METR time horizon과 Frontier Risk Report의 후속 결과.
- FDA AI-enabled medical devices list의 foundation model/LLM 태깅.
- State of Clinical AI Report 후속판과 prospective trial 사례.

## Open Questions

아직 답이 없거나 판단을 유보한 질문입니다.

- 에이전트가 실제 업무에서 "성공률"보다 중요한 오류 유형은 무엇인가?
- subagent orchestration은 언제 단일 강한 모델보다 비용 대비 효과가 좋은가?
- 임상 데이터/EDC 업무에서 AI가 가장 먼저 안정적으로 줄일 수 있는 병목은 무엇인가?
- open-weight 모델의 장점인 privacy/local control과 안전 장치 제거 가능성을 어떻게 균형 잡을 것인가?
- benchmark saturation이 심해질수록 개인 스터디에서는 어떤 평가 기준을 써야 하나?

## Changed Since Last Review

- 초기 자료 작성: 전체 동향, 모델, 에이전트, 평가, 안전/거버넌스, 임상 AI 축의 소스 노트를 추가했습니다.
