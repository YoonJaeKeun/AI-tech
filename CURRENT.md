---
title: "Current AI Tech View"
last_reviewed: 2026-11-01
review_cycle: monthly
---

# Current AI Tech View

이 문서는 2026-08-24 기준 AI 기술동향 판단을 한 장으로 유지하는 곳입니다. 자세한 근거는 `sources/`와 `timeline/`에 남기고, 여기에는 지금의 결론만 간결하게 둡니다.

## Snapshot

- 가장 중요하게 볼 흐름: AI는 단일 챗봇 성능 경쟁에서 도구 사용, 장기 작업, 에이전트 실행, 비용 효율, 안전 장치 경쟁으로 이동하고 있습니다.
- 최근 판단이 바뀐 부분: 모델 자체의 지능보다 "어떤 harness와 workflow로 쓰는가"가 실제 성능 차이를 크게 만듭니다.
- 다음 월간 리뷰 때 다시 확인할 부분: GPT-5.6 계열의 일반 공개 여부, Claude Sonnet 5의 실사용 평가, Google Antigravity/Gemini 3.5의 개발자 생태계 확산, 임상 AI의 전향적 검증 사례.
- (2026-08-24 갱신) "harness와 workflow가 성능 차이를 만든다"는 위 판단에는 에이전트 실행 루프와 별개의 축이 하나 더 있습니다. 단일 LLM 호출에서도 무엇을 컨텍스트에 넣는가(전처리)와 출력을 얼마나 견고하게 파싱·검증하는가(후처리)가 실제 품질을 가릅니다. 근거: 2026-07-09에 신설한 `topics/llm-pipeline/llm-pipeline.md` 의 Current View.

- (2026-11-01 갱신) 2026-10은 **판단이 바뀐 달이 아니라 판단의 전제가 다듬어진 달**입니다. 44개 자료의 `My Take` 를 전수 확인한 결과 기존 판단과 정면으로 어긋난 자료는 한 건도 없었습니다. 대신 하네스 기능의 무게중심이 "무엇을 할 수 있는가"에서 **"무엇을 막고 무엇을 남기는가"** 로 분명히 옮겨갔습니다 — 강제 사람 승인(mod `tool.check`의 `decider: "person"`), 감사 이벤트(`claude_code.safety_event` OpenTelemetry), 역할 분리(Enterprise custom roles)가 한 달 안에 모두 나왔습니다. 근거: `timeline/2026-10.md` Signals(원문 확인 17건), `sources/2026-10/2026-10-20.md`, `2026-10-22.md`, `2026-10-26.md`.
- (2026-11-01 갱신) 위 "비용 효율 경쟁" 판단의 성격이 바뀌었습니다. 2026-09가 **플래그십 가격 인하 발표**의 달이었다면, 2026-10에는 그런 발표가 한 건도 없고 대신 **effort·정밀도·비용을 조절하는 장치가 모델·프레임워크·서빙·로컬 런타임 전 계층으로 내려왔습니다**(원문 확인 8건). 근거: `timeline/2026-10.md` Signals, `sources/2026-10/2026-10-08.md`(Haiku 5.5의 effort 조절), `2026-10-09.md`(LangChain의 OpenAI Decisions 미들웨어), `2026-10-16.md`(Opus 5.5 Fast mode 정식 출시), `2026-10-19.md`(Ollama decision model의 클라우드 확장).

## Tech Radar

### Adopt

지금 바로 활용하거나 학습 우선순위를 높일 만한 기술입니다.

- 제한된 범위의 코딩 에이전트: 테스트, diff review, 사람 승인 절차가 있는 저장소 작업.
- 소스 노트 기반 스터디 운영: `sources/`에 근거를 남기고 `CURRENT.md`에는 현재 판단만 유지.
- Terminal-Bench, SWE-bench, METR Time Horizon 같은 workflow 중심 평가 렌즈.
- (2026-08-24 추가) LLM 전처리·후처리 경계를 명시적으로 설계하기: 컨텍스트 조립·예산 관리·입력 가드레일과, 파싱·구조화 출력 검증·출력 가드레일을 프레임워크 기능이 아니라 아키텍처의 뼈대로 다루는 방식. 근거: `topics/llm-pipeline/llm-pipeline.md` (2026-07-09 신설) — 환각, 형식 깨짐, prompt injection, 비용 폭증 같은 실패 대부분이 이 두 경계에서 발생한다는 누적 판단.

- (2026-11-01 추가) 위 "제한된 범위의 코딩 에이전트" 항목의 전제는 **기본 설정에서만 성립합니다.** 2026-10에 서로 반대 방향의 변경이 같은 주에 나왔습니다 — Claude Code v2.1.305가 `sandbox.allowNestedUserNamespaces` 를 추가해 Chromium·rootless podman 실행 같은 정당한 필요를 위해 **샌드박스 파일 보호를 우회하는 경로를 공식 옵션으로** 열었고(`sources/2026-10/2026-10-21.md`, 원문 확인), 바로 다음 릴리스가 `claude_code.safety_event` OpenTelemetry 이벤트를 추가해 그 사용을 감사 가능하게 만들었습니다(`sources/2026-10/2026-10-22.md`, 원문 확인). 즉 이 항목을 Adopt에 두는 근거는 "하네스가 안전하다"가 아니라 **"기본값이 안전하고, 그 기본값을 벗어난 사용이 로그에 남는다"** 입니다. 우회 옵션을 켠 설정에서는 이 전제가 느슨해집니다.

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

- (2026-11-01 추가) **전임상·기초연구 단계의 AI R&D 보조**: 분자 설계, 규제 문서 검토, 임상시험 계획 평가, 기초과학 연구 가속처럼 **환자에게 닿지 않는** 연구 단계의 보조. 위 Trial의 "비진단성 행정 업무 보조"와도, 바로 위 Assess의 "환자-facing agent와 clinical decision support의 outcome 개선"과도 층위가 다릅니다. 근거는 2026-10의 원문 확인 자료 3건입니다 — `sources/2026-10/2026-10-23.md`(생명과학 Guest Investigator 공개 모집), `2026-10-28.md`(제약·바이오 6곳과의 신약개발 협업 초기 결과, Anthropic 스스로 **전부 preclinical** 이며 "완전한 검증은 더 오래 걸린다"고 명시), `2026-10-29.md`(AI for Science를 Sloan·Simons·NSF 등 20개 재단·연구기관 파트너십으로 확장, 참여 기관 상당수가 천체물리·수학·화학 등 **생명과학 밖**). 두 개의 일일 로그가 독립적으로 "기존 4개 ring 어디에도 맞지 않는다"고 지적했습니다. **Assess에 둘지 Trial 하위 항목으로 둘지는 사람이 판단할 사안입니다.**

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
- (2026-08-24 추가) MCP 사양과 거버넌스: 2026-07-28 spec의 stateless 코어 전환, Client ID Metadata Documents와 Enterprise-Managed Authorization, Agentic AI Foundation 이관 이후의 SEP 심사 체계. 근거: `sources/2026-08/2026-08-24.md#the-new-mcp-roadmap` (원문 확인, confidence high). 위 Trial의 "원격 sandbox 또는 격리된 terminal 기반 에이전트 실행" 항목이 어떤 표준 위에서 굴러갈지를 결정합니다.

- (2026-11-01 추가) Managed Agents **"Dynamic workflows"(beta)의 beta 졸업 여부**와, 실패 시 디버깅·비용 관측이 실제로 얼마나 투명한지. 다수 에이전트를 phase로 묶어 실행하는 벤더 네이티브 오케스트레이션 API입니다. **이것이 위 Trial의 "subagent orchestration"을 Adopt로 올릴지 가를 자료입니다.** 근거: `sources/2026-10/2026-10-15.md` (원문 확인).
- (2026-11-01 추가) **METR 상주 평가의 첫 출판물.** Anthropic이 METR 직원 6명에게 직원급 내부 접근권을 부여하는 3단계 평가기관 프레임워크를 공개했습니다. "Anthropic이 출판을 거부할 수 없다"는 조건과 "모델 아키텍처 정보는 공유 범위에서 기본 제외"라는 한계가 실제로 어떻게 작동하는지는 **첫 출판물이 나와야 검증됩니다.** 근거: `sources/2026-10/2026-10-16.md` (원문 확인).
- (2026-11-01 추가) **민감 데이터 환경용 기본 설정이 벤더 측에서 제공되는 흐름.** Claude Code 저장소에 HIPAA용 `hipaa-baseline.json` + `managed-mcp.lockdown.json` 예제가 추가됐습니다(네트워크 샌드박싱·자격증명 격리·로그 레댁션). 위 Hold의 "PHI, PII, confidential data를 공개 LLM에 직접 넣는 사용" 경계에 대한 실무적 답이 벤더에서 나온 첫 사례로, clinical-healthcare 축과 agents 축을 잇습니다. 근거: `sources/2026-10/2026-10-14.md` (원문 확인). **단일 자료이므로 신호가 아니라 관찰 대상으로만 둡니다.**
- (2026-11-01 갱신) 위 "MCP 사양과 거버넌스" 항목은 이제 **"MCP와 Agent Skills — 에이전트 생태계 표준의 AAIF 거버넌스 이관"** 으로 읽습니다. Anthropic이 Agent Skills 표준도 Agentic AI Foundation에 이관한다고 발표했습니다(2026-10-22). 2026-08의 MCP 이관에 이은 **두 번째 사례**이므로 "한 번의 사건"이 아니라 "경로"로 다룰 수 있습니다. 근거: `sources/2026-10/2026-10-23.md` (원문 확인).

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

- (2026-11-01 추가) **`company-business` 슬러그를 신설할 것인가?** 2026-10에 기존 9개 topic 슬러그 어디에도 맞지 않아 기록을 포기한 자료가 연이어 나왔습니다 — Anthropic의 SEC Form S-1 공식 제출(2026-10-26, **원문을 직접 열어 확인했는데도** 맞는 슬러그가 없어 기록하지 않음)과 GSA 파트너십 확대입니다. 두 개의 일일 로그가 독립적으로 같은 슬러그를 제안했습니다. `CLAUDE.md` 는 에이전트가 임의로 슬러그를 만드는 것을 금지하므로 **사람만 결정할 수 있습니다.** 신설하지 않는다면, 원문 확인된 자료를 슬러그가 없어서 버리는 상황을 그대로 둘지도 함께 정해야 합니다. 근거: `sources/2026-10/2026-10-27.md`, `2026-10-28.md`.
- (2026-11-01 추가) **기초과학 연구 축의 공백을 `clinical-healthcare` 로 덮을 수 있는가?** 위 `company-business` 와는 성격이 다른 공백입니다. AI for Science 확장의 참여 기관 상당수가 천체물리·수학·화학이어서 `clinical-healthcare` 에 넣는 것이 정확하지 않습니다. 2026-10에 이 축의 자료가 3건으로 늘었으므로 단발성이 아닙니다. 근거: `sources/2026-10/2026-10-29.md` (원문 확인).
- (2026-11-01 추가) **하네스 릴리스를 어느 수준까지 기록할 것인가?** 2026-10의 44개 자료 중 17건(39%)이 Claude Code 릴리스 한 축입니다. 전부 원문 확인이라 품질은 가장 높지만, 하루 5~10건이라는 선별 기준 안에서 **이 축이 다른 축을 밀어내고 있는지** 판단이 필요합니다. 개별 패치 버전을 매일 기록하는 대신 주간으로 묶는 선택지도 있습니다. 이 질문은 `AUTOMATION.md` 의 선별 기준을 고칠지와 직결됩니다. 근거: `sources/2026-10/` 전체, `timeline/2026-10.md` Signals.
- (2026-11-01 추가) **선거·시민 활동 관련 사용을 어디까지 허용하는 것이 맞는가?** 2026 Usage Policy 개정이 비동의 감시·추적 금지를 **명문화하면서 동시에** 선거 섹션을 축소해 타겟팅 금지를 완화했습니다(발효 2026-11-12). "시민 활동 지원"과 "개인화된 선거 조작"을 같은 기능이 가르는 구조이고, 이 문서의 기존 판단에는 이 긴장을 다루는 항목이 없습니다. 같은 달 중간선거 대비 발표가 "쪼개진 악성 캠페인은 놓칠 수 있다"고 자체 인정한 것과 함께 보아야 합니다. 근거: `sources/2026-10/2026-10-12.md`, `2026-10-15.md` (둘 다 원문 확인).
- (2026-11-01 추가) **"harness·workflow 설계 역량"을 무엇으로 측정하고 무엇으로 늘릴 것인가?** 벤더가 모델 성능이 아니라 **배치할 수 있는 사람**을 병목으로 보고 있다는 신호가 2026-10에 두 건 나왔습니다 — Barclays 전사 확산 계약(2026년 말 개발자 50% 목표)과 Claude Frontier Academy($100M, 2027년까지 'Frontier Deployed Engineer' 1만 명). 위 Snapshot의 "harness와 workflow가 성능 차이를 만든다"는 판단이 맞다면 이것이 다음 질문입니다. 두 발표 모두 **구체적인 비용·시간 절감 수치는 비어 있습니다.** 근거: `sources/2026-10/2026-10-02.md`, `2026-10-05.md` (둘 다 원문 확인).

## Changed Since Last Review

- 초기 자료 작성: 전체 동향, 모델, 에이전트, 평가, 안전/거버넌스, 임상 AI 축의 소스 노트를 추가했습니다.
- (2026-08-24) 2026-07 월간 리뷰 결과를 반영했습니다. Tech Radar의 기존 4개 ring은 이동 없이 그대로 두었고(2026-07 자료 안에서 이동 근거를 찾지 못함), Adopt에 LLM 전처리·후처리 설계를 1건 추가, Watchlist에 MCP 사양·거버넌스를 1건 추가, Open Questions를 3건 추가했습니다. 자세한 근거는 `timeline/2026-07.md` 의 `## 자동 갱신 (2026-08-24)` 절에 있습니다.
- (2026-11-01) 2026-10 월간 리뷰 결과를 반영했습니다. **Tech Radar의 ring 이동은 0건입니다.** 2026-08·2026-09 리뷰와 같은 결론이지만 이유가 다릅니다 — 2026-09에는 *같은 달 안에 반대 방향 근거가 함께 나와서* 옮기지 못했고, 2026-10에는 **이동을 뒷받침할 근거 자체가 한쪽 축에만 몰려 있어서** 옮기지 않았습니다. 특히 "subagent orchestration"은 올릴 근거가 또 한 단계 강해졌지만(벤더 네이티브 오케스트레이션 API 등장, 하네스의 fork subagent 기본 활성화) **"언제 단일 강한 모델보다 이득인가"에 답하는 2026-10 자료가 0건**이라 Trial에 그대로 두었습니다. 대신 Snapshot 2건, Adopt 전제 1건, Assess 1건, Watchlist 3건 추가 + 1건 문구 갱신, Open Questions 5건을 덧붙였습니다. 자세한 근거는 `timeline/2026-10.md` 에 있습니다.
- (2026-11-01 확인 필요) 이 리뷰가 근거로 삼은 2026-10 자료 44건 중 **41건(93%)이 원문 확인**으로 이 저장소 최고 검증률이지만, 동시에 **기록의 폭은 역대 가장 좁습니다** — 출처가 5개 도메인뿐이고(github.com 15, www.anthropic.com 13, code.claude.com 11, arxiv.org 3, platform.claude.com 2) **33건(75%)이 Anthropic 계열**입니다. `korea` 축은 0건으로 **3개월 연속 공백**이고(`topics/korea.md` 는 2026-08-24 이후 갱신 없음), `models` 축은 1건, `evals-benchmarks` 축은 1건(원문 미확인)뿐입니다. PR #4가 제안한 "구조적 편향" 항목과 같은 사안이라 중복 추가하지 않았습니다. 2026-09에는 *검증할 수 있는 것*이 기울었고, 2026-10에는 **기록된 것 자체**가 기울었습니다.
