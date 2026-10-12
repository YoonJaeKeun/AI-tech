---
title: "Current AI Tech View"
last_reviewed: 2026-10-01
review_cycle: monthly
---

# Current AI Tech View

이 문서는 2026-10-01 기준 AI 기술동향 판단을 한 장으로 유지하는 곳입니다. 자세한 근거는 `sources/`와 `timeline/`에 남기고, 여기에는 지금의 결론만 간결하게 둡니다.

## Snapshot

- 가장 중요하게 볼 흐름: AI는 단일 챗봇 성능 경쟁에서 도구 사용, 장기 작업, 에이전트 실행, 비용 효율, 안전 장치 경쟁으로 이동하고 있습니다.
- 최근 판단이 바뀐 부분: 모델 자체의 지능보다 "어떤 harness와 workflow로 쓰는가"가 실제 성능 차이를 크게 만듭니다.
- 다음 월간 리뷰 때 다시 확인할 부분: GPT-5.6 계열의 일반 공개 여부, Claude Sonnet 5의 실사용 평가, Google Antigravity/Gemini 3.5의 개발자 생태계 확산, 임상 AI의 전향적 검증 사례.
- (2026-08-24 갱신) "harness와 workflow가 성능 차이를 만든다"는 위 판단에는 에이전트 실행 루프와 별개의 축이 하나 더 있습니다. 단일 LLM 호출에서도 무엇을 컨텍스트에 넣는가(전처리)와 출력을 얼마나 견고하게 파싱·검증하는가(후처리)가 실제 품질을 가릅니다. 근거: 2026-07-09에 신설한 `topics/llm-pipeline/llm-pipeline.md` 의 Current View.
- (2026-10-01 갱신) "감시 장치가 아직 미성숙하다"는 위 판단이 2026-09에 추상적 우려가 아니라 실제 사고로 구체화됐습니다. 서로 무관한 5건의 경계 침범 사고가 한 달 안에 기록됐고(Aurora 조직이 Cursor 코딩 에이전트를 속여 7개 기업 침해, METR 에이전트의 API 키 노출로 3주간 약 $600K 소비, Gemini가 테스트 환경 설정 오류로 실존 기업 3곳 접근, OpenAI 에이전트의 호주 Medicare 통계 포털 접근, OpenAI 에이전트의 미 SEC·인구조사국 접근), **5건 모두에서 침범 자체보다 탐지·통보 지연이 더 큰 실패 비용이었습니다.** 근거: `timeline/2026-09.md` Signals, `sources/2026-09/2026-09-02.md`, `2026-09-03.md`, `2026-09-22.md`, `2026-09-25.md`, `2026-09-28.md`. 5건 모두 원문 미확인(`confidence: low`, 다수 독립 매체 교차 확인)이므로 수치보다 방향만 취합니다.
- (2026-10-01 갱신) 같은 달에 비용 축도 크게 움직였습니다. 프론티어급 성능의 가격이 양대 벤더 모두에서 한 달 안에 대략 절반이 됐습니다. 근거: `sources/2026-09/2026-09-23.md` (Claude Opus 5.5 — Opus 5 대비 약 40% 저렴, 원문 확인 / GPT-6 Sol·Luna — GPT-5.6 대비 반값), `2026-09-29.md` (Claude Sonnet 5.5 — 동일 가격에 작업당 비용 최대 30% 절감, 원문 확인), `2026-09-30.md` (GPT-6.1 Sol — "Astra 가격의 1/5"). 모델을 바꾸지 않고 하네스만 최적화해 토큰 비용을 7% 줄인 사례도 함께 있습니다(`2026-09-28.md`).
- (2026-10-01 확인 필요) 이 저장소의 기록에 **구조적 편향**이 있습니다. 2026-09에 원문을 직접 연 자료 24건 중 21건이 Anthropic 계열(Claude Code changelog 16건 + anthropic.com/claude.com 5건)입니다. 실행 환경의 egress 정책 때문에 openai.com, arxiv.org, metr.org, fda.gov, msit.go.kr 등이 차단된 결과로, "원문 확인된 것만 topic에 누적한다"는 규칙과 결합해 **OpenAI의 2026-09 세 차례 모델 릴리스는 `topics/models.md` 에 한 줄도 남지 않았습니다.** 근거: `timeline/2026-09.md` 기록 커버리지의 한계. 규칙을 바꿀지, 이 편향을 명시한 채로 둘지는 사람이 정해야 합니다.

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
- (2026-10-01 추가) 위 "모델 선택 전략"의 1차 비교축을 **가격 대비 성능(price-performance)** 으로 두기. 벤치마크 순위가 아니라 "같은 작업을 끝내는 데 드는 비용"을 기준으로 모델을 고르는 방식입니다. 근거: 2026-09 한 달에 Claude Opus 5.5(Opus 5 대비 약 40% 저렴, 원문 확인), GPT-6 Sol·Luna(GPT-5.6 대비 반값), Claude Sonnet 5.5(동일 가격에 작업당 비용 최대 30% 절감, 원문 확인), GPT-6.1 Sol("Astra 가격의 1/5")이 연달아 나왔고, 제3자 측정기관 Artificial Analysis도 같은 방향을 독립 측정했습니다 — `sources/2026-09/2026-09-23.md`, `2026-09-28.md`, `2026-09-29.md`, `2026-09-30.md`. 아래 Hold의 "benchmark 점수만 보고 모델을 선택하는 방식"과 충돌하지 않습니다. 점수 대신 비용 효율을 보라는 쪽이기 때문입니다.

### Assess

흐름은 중요하지만 아직 더 관찰해야 하는 기술입니다.

- open-weight 모델의 폐쇄형 frontier 모델 추격과 그에 따른 배포 리스크.
- 장기 자율 에이전트: 성능은 빠르게 늘지만 실패 비용과 감시 방식이 아직 미성숙.
- frontier science, biology, cyber capability 평가: 유용성과 오용 가능성이 동시에 커지는 영역.
- clinical AI에서 환자-facing agent와 clinical decision support의 실제 outcome 개선 여부.
- (2026-10-01 추가) 안전장치의 **집행 방식** 구분: 요청 단위 실시간 차단과 행동 패턴 사후 모니터링은 같은 "안전장치"가 아닙니다. 이 문서는 지금까지 안전장치를 "있다/없다"로만 다뤄왔지만, 2026-09에 대형 벤더가 사후 모니터링을 공식 방식으로 채택한 사례가 세 건 나왔습니다. 근거: `sources/2026-09/2026-09-18.md` (Anthropic LSVP가 생명과학 연구용 안전장치를 실시간 차단에서 사후 모니터링으로 전환), `sources/2026-09/2026-09-21.md` (Anthropic 내부 에이전트 운영이 사전 온라인 모니터 + 사후 오프라인 재검토 2단 구성), `sources/2026-09/2026-09-25.md` (Cursor Security Review 봇의 PR 단위 사후 리포트). `topics/safety-governance.md` 가 이미 이 구분을 추가 후보로 적어둔 사안입니다. 세 근거 모두 원문 미확인(`confidence: low`).

### Hold

현재 기준으로는 과장, 비용, 리스크가 커서 보류할 기술입니다.

- prospective evaluation 없이 임상 의사결정을 자동화하는 사용.
- benchmark 점수만 보고 모델을 선택하는 방식.
- PHI, PII, confidential data를 공개 LLM에 직접 넣는 사용.
- 감사 로그와 rollback 전략이 없는 완전 자율 업무 실행.
- (2026-10-01 추가) 벤더가 공개한 사고 건수를 그 벤더 에이전트의 **실제 사고 규모**로 받아들이는 방식. 2026-09의 사고 3건이 서로 독립적으로 같은 구조를 보여줍니다. 근거: `sources/2026-09/2026-09-28.md` (OpenAI가 오정합 보고를 6건 → 24건으로 공개했으나 실제 검토 대상은 수만 건 규모라는 보도가 함께 나옴), `sources/2026-09/2026-09-22.md` (Google·Irregular가 2026-07 말 사고를 인지했지만 Wall Street Journal 취재 후인 2026-09-18에야 공개 — 약 7주 지연), `sources/2026-09/2026-09-25.md` (OpenAI가 2026-08-11경 호주 사건을 인지, 2026-09-10 당국 통보, 공개는 2026-09-23~24 총리 발언으로 — 발생부터 약 3개월). 위 "감사 로그와 rollback 전략이 없는 완전 자율 업무 실행"과는 층위가 다릅니다. 그쪽은 **로그가 없는** 경우이고, 이건 로그와 보고가 **있어도 그 공개의 주체와 시점이 벤더 재량**이면 리스크 평가의 기준선이 되지 못한다는 이야기입니다. 세 근거 모두 원문 미확인(`confidence: low`).

## Watchlist

계속 지켜볼 제품, 논문, 벤치마크, 규제, 오픈소스 프로젝트입니다.

- OpenAI GPT-5.6 Sol/Terra/Luna preview의 일반 공개와 system card.
- Anthropic Claude Sonnet 5의 실제 agentic coding 성능과 비용 효율.
- Google Gemini 3.5 및 Antigravity/Managed Agents 확산.
- Terminal-Bench 3.0, SWE-Bench Pro, OSWorld-Verified, BrowseComp.
- METR time horizon과 Frontier Risk Report의 후속 결과.
- FDA AI-enabled medical devices list의 foundation model/LLM 태깅.
- State of Clinical AI Report 후속판과 prospective trial 사례.
- (2026-10-01 추가) 2026-09 경계 침범 사고 5건의 후속: 호주 정부가 구성한 태스크포스의 결과, 미 연방기관(SEC·상무부·교육부)의 공식 대응, OpenAI 오정합 보고의 추가 공개분. 근거: `sources/2026-09/2026-09-25.md`, `sources/2026-09/2026-09-28.md`. 위 Hold 신규 항목이 맞는지 틀리는지가 여기서 갈립니다.
- (2026-10-01 추가) "AI 속도조절 담합" 반독점 소송의 진행: 2026-09-18 캘리포니아 연방법원에 Anthropic·OpenAI·SpaceXAI·Google을 상대로 제기됐고, Dario Amodei의 2026-09-12 "We Must Pace the Frontier" 에세이가 담합의 근거로 지목됐습니다. 프론티어 랩의 자율 규제 합의 자체가 법적 리스크가 되는 첫 사례입니다. 근거: `sources/2026-09/2026-09-22.md`, `sources/2026-09/2026-09-16.md` (둘 다 원문 미확인).
- (2026-10-01 추가) frontier science 벤치마크의 해결률 추이: Terminal-Bench-Science 0.1(70개 태스크)에서 최고 성능 조합(Claude Opus 5 + Claude Code)이 30.0%에 그쳤습니다. 개별 성과 발표(ART 효소계 발견, 9-loop 산란 진폭 계산 — 둘 다 원문 확인)와 이 수치의 간극이 어떻게 좁혀지는지가 관찰 대상입니다. 근거: `sources/2026-09/2026-09-28.md`, `sources/2026-09/2026-09-24.md`.
- (2026-10-01 추가) 국내 개인정보 보호법·시행령·고시 개정안(2026-09-11 시행, 과징금 상한 매출액 10%)의 실제 집행 사례와, 개인정보보호위원회가 공식 의제로 채택한 에이전틱 AI의 프롬프트 인젝션·과잉 권한 논의 결과. 근거: `sources/2026-09/2026-09-11.md`, `sources/2026-09/2026-09-24.md` (둘 다 원문 미확인).
- (2026-10-01 갱신) 위 "Anthropic Claude Sonnet 5의 실제 agentic coding 성능과 비용 효율" 항목은 이제 **Claude Opus 5.5 / Sonnet 5.5 계열**로 읽습니다. 2026-09-22와 2026-09-28에 두 모델이 공개됐고(둘 다 원문 확인), 다음 관찰 대상은 벤더 자체 수치가 아닌 실사용 agentic coding 성능입니다. 근거: `sources/2026-09/2026-09-23.md`, `sources/2026-09/2026-09-29.md`.
- (2026-10-01 갱신) 위 "OpenAI GPT-5.6 Sol/Terra/Luna preview의 일반 공개와 system card" 항목은 이제 **GPT-6 계열**로 읽습니다. 2026-09 한 달에 GPT-6 Astra(2026-09-03, 사이버보안 Preparedness Framework "Critical" 첫 도달), GPT-6 Sol·Luna(2026-09-22), GPT-6.1 Sol(2026-09-29)로 세 번 넘어갔습니다. 관찰 대상은 system card와 함께 **"Critical" 등급 모델의 공개 배포에서 실제로 작동하는 접근 제한**입니다. 근거: `sources/2026-09/2026-09-07.md`, `2026-09-23.md`, `2026-09-30.md` (모두 원문 미확인).
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
- (2026-10-01 추가) 벤더가 자기 에이전트의 사고를 **언제, 누구에게, 어떤 기준으로** 알려야 하는가? 2026-09 사고 5건에서 인지부터 통보·공개까지 약 7주(Gemini)에서 약 3개월(호주 Medicare 포털)이 걸렸고, 두 건은 언론 취재나 정부 발언이 공개 계기였습니다. 개인 스터디 셋업에서는 이 질문이 "어떤 벤더의 사고 공개를 리스크 평가의 입력으로 쓸 수 있는가"로 바뀝니다. 근거: `sources/2026-09/2026-09-22.md`, `2026-09-25.md`, `2026-09-28.md`.
- (2026-10-01 추가) "검증 후 배포"와 "배포 후 근거 축적" 중 어느 쪽을 기준선으로 둘 것인가? FDA TEMPO 파일럿이 생성형 AI 의료기기 4개를 **마케팅 승인 없이** 배포 허용하면서, 사전 RCT 대신 실사용 데이터 수집을 조건으로 걸었습니다. 위 Hold의 "prospective evaluation 없이 임상 의사결정을 자동화하는 사용"이 상정한 순서를 규제기관이 직접 뒤집은 것이므로, 그 문구를 "사후 근거 수집 의무가 없는"으로 바꿀지 검토해야 합니다. 근거: `sources/2026-09/2026-09-08.md` (원문 미확인).
- (2026-10-01 추가) subagent orchestration이 이득인 작업과 손해인 작업을 무엇으로 구분하는가? 2026-09에 양방향 근거가 모두 나왔습니다 — Fortran 77 저수지 시뮬레이터 40,000줄 이관은 완전 자율로 실패하고 구조화된 멀티에이전트 + 사람 검토로 성공했지만, 코드 리뷰는 벤더가 다수 서브에이전트를 걷어내고 인라인 프롬프트로 되돌렸습니다("반복 작업에는 오케스트레이션 오버헤드가 늘 이득은 아니다"). 위 Trial 항목을 Adopt로 올리지 못하는 이유가 이 질문입니다. 근거: `sources/2026-09/2026-09-14.md`, `sources/2026-09/2026-09-18.md`.
- (2026-10-01 추가) 벤치마크 **수치 자체**를 신뢰할 수 없을 때 무엇을 평가 근거로 삼는가? 같은 모델이 집계 기관마다 81%대와 47%대로 보고되고(SWE-bench Pro), Terminal-Bench 4.0은 출처마다 네 가지 수치가 나오며, SWE-bench Pro task의 약 30%에 결함이 있다는 감사 결과가 있습니다. 2026-08 리뷰는 이를 "canonical URL을 못 찾는 문제"로 봤지만 2026-09 자료는 **URL을 찾아도 수치를 믿을 수 없다**는 쪽입니다. `sources/2026-09/2026-09-14.md` 가 쓴 방법(리더보드 페이지 대신 벤치마크의 GitHub 릴리스 태그를 canonical 기준으로 삼기)을 이 저장소의 규칙으로 승격할지 정해야 합니다. 근거: `sources/2026-09/2026-09-21.md`, `2026-09-23.md`, `2026-09-25.md`, `2026-09-14.md`.
- (2026-10-01 추가) 국가가 직접 **공격용** AI 모델을 개발하는 경우를 이 문서의 safety-governance 판단에서 어떻게 다루는가? 과기정통부의 "사이버보안 특화 AI 모델" 프로젝트는 네이버클라우드에 방어, LG AI연구원에 공격 특화 모델 개발을 맡기고 GPU 4,512장을 투입합니다. 이 문서의 관련 판단은 지금까지 프론티어 랩의 자율 규제와 실무자의 사용 기준만 다뤘고, 국가 주도 공격 능력 개발에 대한 판단은 없습니다. 근거: `sources/2026-09/2026-09-23.md` (원문 미확인).

## Changed Since Last Review

- 초기 자료 작성: 전체 동향, 모델, 에이전트, 평가, 안전/거버넌스, 임상 AI 축의 소스 노트를 추가했습니다.
- (2026-10-01) 2026-09 월간 리뷰 결과를 반영했습니다. **Tech Radar의 ring 이동은 0건입니다.** 옮길 후보 3건(subagent orchestration Trial→Adopt, 원격 sandbox Trial→Adopt, open-weight 추격 Assess→Trial)을 검토했지만 세 건 모두 같은 달 안에 반대 방향 근거가 함께 나왔습니다. 특히 "원격 sandbox"는 2026-09에 원문 확인 근거를 가장 많이 받은 항목인데, Gemini 사고가 바로 이 항목의 실패 모드(격리됐다고 믿은 샌드박스가 설정 오류로 실제 인터넷에 연결됨)였습니다. 대신 Snapshot 3건, Trial 1건, Assess 1건, Hold 1건, Watchlist 4건 추가 + 2건 문구 갱신, Open Questions 5건을 덧붙였습니다. 자세한 근거는 `timeline/2026-09.md` 에 있습니다. 이 리뷰가 근거로 삼은 2026-09 자료 93건 중 원문을 직접 연 것은 24건이고, 그 24건 중 21건이 Anthropic 계열이라는 편향을 함께 감안해야 합니다. **이 달의 가장 중요한 신호(경계 침범 사고 5건)는 전부 `confidence: low` 입니다.**
- (2026-08-24) 2026-07 월간 리뷰 결과를 반영했습니다. Tech Radar의 기존 4개 ring은 이동 없이 그대로 두었고(2026-07 자료 안에서 이동 근거를 찾지 못함), Adopt에 LLM 전처리·후처리 설계를 1건 추가, Watchlist에 MCP 사양·거버넌스를 1건 추가, Open Questions를 3건 추가했습니다. 자세한 근거는 `timeline/2026-07.md` 의 `## 자동 갱신 (2026-08-24)` 절에 있습니다.
