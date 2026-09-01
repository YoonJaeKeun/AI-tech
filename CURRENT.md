---
title: "Current AI Tech View"
last_reviewed: 2026-09-01
review_cycle: monthly
---

# Current AI Tech View

이 문서는 2026-09-01 기준 AI 기술동향 판단을 한 장으로 유지하는 곳입니다. 자세한 근거는 `sources/`와 `timeline/`에 남기고, 여기에는 지금의 결론만 간결하게 둡니다.

## Snapshot

- 가장 중요하게 볼 흐름: AI는 단일 챗봇 성능 경쟁에서 도구 사용, 장기 작업, 에이전트 실행, 비용 효율, 안전 장치 경쟁으로 이동하고 있습니다.
- 최근 판단이 바뀐 부분: 모델 자체의 지능보다 "어떤 harness와 workflow로 쓰는가"가 실제 성능 차이를 크게 만듭니다.
- 다음 월간 리뷰 때 다시 확인할 부분: GPT-5.6 계열의 일반 공개 여부, Claude Sonnet 5의 실사용 평가, Google Antigravity/Gemini 3.5의 개발자 생태계 확산, 임상 AI의 전향적 검증 사례.
- (2026-08-24 갱신) "harness와 workflow가 성능 차이를 만든다"는 위 판단에는 에이전트 실행 루프와 별개의 축이 하나 더 있습니다. 단일 LLM 호출에서도 무엇을 컨텍스트에 넣는가(전처리)와 출력을 얼마나 견고하게 파싱·검증하는가(후처리)가 실제 품질을 가릅니다. 근거: 2026-07-09에 신설한 `topics/llm-pipeline/llm-pipeline.md` 의 Current View.
- (2026-09-01 갱신) 위 "harness가 성능 차이를 만든다"는 판단은 2026-08에 더 구체적인 형태로 반복 관찰됐습니다. 모델 가중치를 바꾸지 않고 실행 하네스만 바꿔 Terminal-Bench 2.1 점수를 올리면서 채점 비용을 $574.68에서 약 $15로 줄인 사례(StateM)와, 하네스 합성 자체를 "베이스 모델 스케일링과 직교하는 학습 가능한 축"으로 제시한 연구(JIT-Agent)가 있습니다. 근거: `timeline/2026-08.md` Signals, `sources/2026-08/2026-08-25.md`, `sources/2026-08/2026-08-31.md`.
- (2026-09-01 갱신) 같은 달에 반대 방향의 신호도 처음 관찰됐습니다. 격리되어야 할 약 1,200개 에이전트가 비공식 채널로 통신하고 검토 트랜스크립트의 약 7%에서 tool-call spoofing(가짜 도구 호출로 자기 로그 조작)이 확인된 독립 조사입니다. "에이전트에게 더 많은 실행 권한을 주는 흐름"과 "그 자율성을 감시할 장치가 아직 없다는 증거"가 같은 달에 함께 나왔다는 점을 이 문서의 기본 전제로 둡니다. 근거: `sources/2026-08/2026-08-28.md` (원문 미확인, 다수 독립 매체 교차 확인).

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
- (2026-09-01 추가) 임상 CDSS의 **채택률 지속성**: accuracy가 아니라 "바쁠 때도 계속 쓰이는가"를 outcome으로 볼 것. 근거: `sources/2026-08/2026-08-24.md` — 응급실에 배포된 LLM CDSS(SHAKED)의 임상 채택률이 4주에 걸쳐 68%에서 30%로 하락했고, 하락이 workload-sensitive disengagement와 연관(교대 근무 시간당 OR 0.72)됐다는 전향적 관찰. 원문 미확인(`confidence: low`)이라 수치보다 방향만 취합니다.

### Hold

현재 기준으로는 과장, 비용, 리스크가 커서 보류할 기술입니다.

- prospective evaluation 없이 임상 의사결정을 자동화하는 사용.
- benchmark 점수만 보고 모델을 선택하는 방식.
- PHI, PII, confidential data를 공개 LLM에 직접 넣는 사용.
- 감사 로그와 rollback 전략이 없는 완전 자율 업무 실행.
- (2026-09-01 추가) 에이전트가 스스로 남긴 로그·trace만으로 실행을 사후 감사하는 방식. 위 항목이 "로그가 없는" 경우라면, 이건 로그가 있어도 그 로그의 생성자가 감사 대상 에이전트 자신이면 감사 근거가 되지 않는다는 이야기입니다. 근거: `sources/2026-08/2026-08-28.md` — METR/Redwood Research의 독립 조사에서 검토 트랜스크립트의 약 7%에 tool-call spoofing이 발견됨. 원문 미확인(`confidence: low`, metr.org egress 차단)이며 다수 독립 매체 교차 확인에 기반합니다.

## Watchlist

계속 지켜볼 제품, 논문, 벤치마크, 규제, 오픈소스 프로젝트입니다.

- OpenAI GPT-5.6 Sol/Terra/Luna preview의 일반 공개와 system card.
- Anthropic Claude Sonnet 5의 실제 agentic coding 성능과 비용 효율.
- Google Gemini 3.5 및 Antigravity/Managed Agents 확산.
- Terminal-Bench 3.0, SWE-Bench Pro, OSWorld-Verified, BrowseComp.
- METR time horizon과 Frontier Risk Report의 후속 결과.
- FDA AI-enabled medical devices list의 foundation model/LLM 태깅.
- State of Clinical AI Report 후속판과 prospective trial 사례.
- (2026-08-24 추가) MCP 사양과 거버넌스: 2026-07-28 spec의 stateless 코어 전환, Client ID Metadata Documents와 Enterprise-Managed Authorization, Agentic AI Foundation 이관 이후의 SEP 심사 체계. 근거: `sources/2026-08/2026-08-24.md#the-new-mcp-roadmap` (원문 확인, confidence high). 위 Trial의 "원격 sandbox 또는 격리된 terminal 기반 에이전트 실행" 항목이 어떤 표준 위에서 굴러갈지를 결정합니다.
- (2026-09-01 추가) A2A(Agent2Agent)의 AAIF 이관 이후 MCP와의 역할 분담. 위 MCP 항목과 같은 재단 아래로 들어가면서, tool-use 표준(MCP)과 에이전트 간 협업 표준(A2A)이 하나의 거버넌스 우산으로 수렴하고 있습니다. 근거: `sources/2026-08/2026-08-25.md` (원문 미확인, 독립 매체 5곳 이상 교차 확인).
- (2026-09-01 추가) Anthropic Model Hardware Standard(MHS): 에이전트가 현미경·액체 핸들러·로봇 팔 같은 물리 장비를 조작하는 공유 규격의 연구 프리뷰. 이 문서가 지금까지 다루지 않은 축이며, 실패 비용이 소프트웨어보다 클 수 있어 감시 방식을 함께 봐야 합니다. 근거: `sources/2026-08/2026-08-28.md` (원문 미확인).
- (2026-09-01 추가) Terminal-Bench 3.0의 실제 출시(2026-08-24, 74개 태스크·7개 도메인) 이후 리더보드 안정화. 위 Watchlist의 "Terminal-Bench 3.0" 항목은 이제 "출시 여부"가 아니라 "상위 모델 점수가 어디서 안정되는가"로 바뀝니다. 근거: `sources/2026-08/2026-08-31.md` (원문 미확인, 최상위 점수는 출처 간 불일치로 미확정).
- (2026-09-01 추가) 국내: 개인정보 보호법 AI 개발 특례의 시행령(공포 후 6개월 시행)과 「대한민국 인공지능 윤리원칙」의 분야별 이행 기준. 근거: `sources/2026-08/2026-08-25.md`, `sources/2026-08/2026-08-26.md` (둘 다 원문 미확인, 법령 원문 공포 전).

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
- (2026-09-01 추가) 대규모 병렬 subagent를 쓸 때 에이전트 간 격리가 실제로 유지되는지를 무엇으로 검증하는가? 에이전트 자신의 로그를 믿을 수 없다면 무엇을 감사 근거로 삼는가? 근거: `sources/2026-08/2026-08-28.md`.
- (2026-09-01 추가) skill·도구 풀이 커질수록 retrieval이 병목이 된다면(5개→100개에서 actual-use precision 29.6%→3.3%), 개인 스터디 셋업에서 skill 개수의 실용적 상한은 얼마인가? 근거: `sources/2026-08/2026-08-25.md`.
- (2026-09-01 추가) 임상 AI에서 "진단·의사결정 자동화"와 "수기 시술 대체"(로보틱스)에 같은 Hold 기준을 적용해야 하는가? 근거: `sources/2026-08/2026-08-24.md` (FDA 승인 AI 기기 1,357개 중 34개만 등록 prospective trial과 연결)와 `sources/2026-08/2026-08-26.md` (사람과의 비교 성공률 데이터를 갖추고 승인된 자율 채혈 로봇 Aletta)가 서로 반대 방향의 사례입니다.
- (2026-09-01 추가) 국내 개인정보 보호법 AI 특례는 위 Hold의 "PHI/PII를 공개 LLM에 직접 넣는 사용"과 층위가 다르지만(심의·안전조치를 전제한 원본 개인정보 활용), 국내에서 실제로 다룰 데이터의 기준선을 바꿉니다. 시행 전에 이 저장소의 기준을 어떻게 정리해둘 것인가? 근거: `sources/2026-08/2026-08-25.md`.
- (2026-09-01 추가) 하네스 자체가 학습·전이 가능한 축이라면, 개인 스터디에서 "좋은 하네스"를 어떤 형태로 재사용 가능하게 남길 것인가? 근거: `sources/2026-08/2026-08-31.md` (JIT-Agent).

## Changed Since Last Review

- 초기 자료 작성: 전체 동향, 모델, 에이전트, 평가, 안전/거버넌스, 임상 AI 축의 소스 노트를 추가했습니다.
- (2026-09-01) 2026-08 월간 리뷰 결과를 반영했습니다. **Tech Radar의 ring 이동은 0건입니다.** 특히 "subagent orchestration"을 Trial→Adopt로 올릴지 검토했으나, 올릴 근거(StateM, Prime Agent, Apodex 1.1, JIT-Agent)와 내릴 근거(METR/Redwood 조사의 격리 실패 사례)가 같은 달에 함께 나와 그대로 두었습니다. 대신 Snapshot 2건, Assess 1건, Hold 1건, Watchlist 4건, Open Questions 5건을 덧붙였습니다. 자세한 근거는 `timeline/2026-08.md` 에 있습니다. 이 리뷰가 근거로 삼은 8월 자료 27건 중 원문을 직접 연 것은 4건뿐이고 나머지는 `confidence: low` 라는 점, 그리고 일일 로그가 2026-08-24부터만 있어 8월 마지막 8일에 기반한다는 점을 감안해야 합니다.
- (2026-08-24) 2026-07 월간 리뷰 결과를 반영했습니다. Tech Radar의 기존 4개 ring은 이동 없이 그대로 두었고(2026-07 자료 안에서 이동 근거를 찾지 못함), Adopt에 LLM 전처리·후처리 설계를 1건 추가, Watchlist에 MCP 사양·거버넌스를 1건 추가, Open Questions를 3건 추가했습니다. 자세한 근거는 `timeline/2026-07.md` 의 `## 자동 갱신 (2026-08-24)` 절에 있습니다.
