---
title: "Current AI Tech View"
last_reviewed: 2026-09-07
review_cycle: monthly
---

# Current AI Tech View

이 문서는 2026-08-24 기준 AI 기술동향 판단을 한 장으로 유지하는 곳입니다. 자세한 근거는 `sources/`와 `timeline/`에 남기고, 여기에는 지금의 결론만 간결하게 둡니다.

## Snapshot

- 가장 중요하게 볼 흐름: AI는 단일 챗봇 성능 경쟁에서 도구 사용, 장기 작업, 에이전트 실행, 비용 효율, 안전 장치 경쟁으로 이동하고 있습니다.
- 최근 판단이 바뀐 부분: 모델 자체의 지능보다 "어떤 harness와 workflow로 쓰는가"가 실제 성능 차이를 크게 만듭니다.
- 다음 월간 리뷰 때 다시 확인할 부분: GPT-5.6 계열의 일반 공개 여부, Claude Sonnet 5의 실사용 평가, Google Antigravity/Gemini 3.5의 개발자 생태계 확산, 임상 AI의 전향적 검증 사례.
- (2026-08-24 갱신) "harness와 workflow가 성능 차이를 만든다"는 위 판단에는 에이전트 실행 루프와 별개의 축이 하나 더 있습니다. 단일 LLM 호출에서도 무엇을 컨텍스트에 넣는가(전처리)와 출력을 얼마나 견고하게 파싱·검증하는가(후처리)가 실제 품질을 가릅니다. 근거: 2026-07-09에 신설한 `topics/llm-pipeline/llm-pipeline.md` 의 Current View.

## Tech Radar

### Adopt

지금 바로 활용하거나 학습 우선순위를 높일 만한 기술입니다.

- 제한된 범위의 코딩 에이전트: 테스트, diff review, 사람 승인 절차가 있는 저장소 작업.
- 소스 노트 기반 스터디 운영: `sources/`에 근거를 남기고 `CURRENT.md`에는 현재 판단만 유지.
- Terminal-Bench, SWE-bench, METR Time Horizon 같은 workflow 중심 평가 렌즈.
- (2026-08-24 추가) LLM 전처리·후처리 경계를 명시적으로 설계하기: 컨텍스트 조립·예산 관리·입력 가드레일과, 파싱·구조화 출력 검증·출력 가드레일을 프레임워크 기능이 아니라 아키텍처의 뼈대로 다루는 방식. 근거: `topics/llm-pipeline/llm-pipeline.md` (2026-07-09 신설) — 환각, 형식 깨짐, prompt injection, 비용 폭증 같은 실패 대부분이 이 두 경계에서 발생한다는 누적 판단.

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
- (2026-09-07 추가) OpenAI GPT-6 Astra(2026-09-03 발표): Preparedness Framework 기준 사이버보안 역량이 처음 "Critical" 등급에 도달했다고 보도됨. 위 GPT-5.6 라인업의 사실상 후속 세대. 원문 미확인(openai.com egress 차단), 복수 매체 교차확인 기반이라 `confidence: low`. 근거: `sources/2026-09/2026-09-07.md#openai-gpt-6-astra-출시--사이버보안-preparedness-framework-critical-등급-첫-도달`.
- Anthropic Claude Sonnet 5의 실제 agentic coding 성능과 비용 효율.
- Google Gemini 3.5 및 Antigravity/Managed Agents 확산.
- Terminal-Bench 3.0, SWE-Bench Pro, OSWorld-Verified, BrowseComp.
- METR time horizon과 Frontier Risk Report의 후속 결과.
- FDA AI-enabled medical devices list의 foundation model/LLM 태깅.
- State of Clinical AI Report 후속판과 prospective trial 사례.
- (2026-08-24 추가) MCP 사양과 거버넌스: 2026-07-28 spec의 stateless 코어 전환, Client ID Metadata Documents와 Enterprise-Managed Authorization, Agentic AI Foundation 이관 이후의 SEP 심사 체계. 근거: `sources/2026-08/2026-08-24.md#the-new-mcp-roadmap` (원문 확인, confidence high). 위 Trial의 "원격 sandbox 또는 격리된 terminal 기반 에이전트 실행" 항목이 어떤 표준 위에서 굴러갈지를 결정합니다.

## Open Questions

아직 답이 없거나 판단을 유보한 질문입니다.

- 에이전트가 실제 업무에서 "성공률"보다 중요한 오류 유형은 무엇인가?
- subagent orchestration은 언제 단일 강한 모델보다 비용 대비 효과가 좋은가?
- 임상 데이터/EDC 업무에서 AI가 가장 먼저 안정적으로 줄일 수 있는 병목은 무엇인가?
- open-weight 모델의 장점인 privacy/local control과 안전 장치 제거 가능성을 어떻게 균형 잡을 것인가?
- benchmark saturation이 심해질수록 개인 스터디에서는 어떤 평가 기준을 써야 하나?
- (2026-08-24 추가) 매월 고정적으로 확인할 benchmark를 3개 정도로 줄일 수 있는가? 근거: `timeline/2026-07.md` Open Questions — 2026-07 리뷰에서 제기됐지만 이 문서에 옮겨지지 않았습니다.
- (2026-08-24 추가) agent workflow를 실험한다면 어떤 local sandbox와 권한 정책을 기본값으로 둘 것인가? 근거: `timeline/2026-07.md` Open Questions. MCP의 enterprise auth 강화(`sources/2026-08/2026-08-24.md#the-new-mcp-roadmap`)로 답을 잡을 재료가 생겼습니다.
- (2026-08-24 추가) 구조화 출력을 보장할 때 constrained decoding(모델 내부)과 검증-재시도(애플리케이션) 중 어디에서 처리하는 것이 견고한가? 근거: `topics/llm-pipeline/llm-pipeline.md` Open Questions.
- (2026-09-07 추가) "Critical" 등급(Preparedness Framework 기준) 모델의 공개 배포에서 실제로 어떤 접근 제한이 작동하는가? 근거: `sources/2026-09/2026-09-07.md` GPT-6 Astra 항목 — 원문 미확인 상태라 이번 자료만으로는 답을 확인하지 못했습니다.
- (2026-09-07 추가) 저비용 모델의 출시 주기가 빨라질수록(72시간 내 3사 릴리스 사례) "어떤 모델을 언제 쓸지 결정하는 비용" 자체가 커지는 것은 아닌가? 근거: `sources/2026-09/2026-09-07.md` Gemini 3.8 Flash 항목.

## Changed Since Last Review

- 초기 자료 작성: 전체 동향, 모델, 에이전트, 평가, 안전/거버넌스, 임상 AI 축의 소스 노트를 추가했습니다.
- (2026-08-24) 2026-07 월간 리뷰 결과를 반영했습니다. Tech Radar의 기존 4개 ring은 이동 없이 그대로 두었고(2026-07 자료 안에서 이동 근거를 찾지 못함), Adopt에 LLM 전처리·후처리 설계를 1건 추가, Watchlist에 MCP 사양·거버넌스를 1건 추가, Open Questions를 3건 추가했습니다. 자세한 근거는 `timeline/2026-07.md` 의 `## 자동 갱신 (2026-08-24)` 절에 있습니다.
- (2026-09-07) 지난 1주(2026-08-31~2026-09-07) 소스 노트를 반영했습니다. 72시간 안에 OpenAI/Google/Meta가 연달아 프론티어 모델을 출시한 점을 Watchlist에 1건 추가했고, Open Questions를 2건 추가했습니다. 이번 주 신규 항목 다수가 egress 차단으로 원문 미확인 상태(`status: unverified`, `confidence: low`)라 Tech Radar ring 이동은 하지 않았습니다. 자세한 근거는 `sources/2026-09/2026-09-07.md` 참고.
