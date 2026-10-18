---
title: "Safety / Governance"
topic: safety-governance
last_reviewed: 2026-10-18
---

# Safety / Governance

AI 안전성, 거버넌스, 규제, 배포 통제, 책임 있는 사용을 정리하는 주제 파일입니다.

## Current View

- capability는 빠르게 올라가지만 responsible AI benchmark, transparency, incident tracking, post-deployment monitoring은 뒤처지는 흐름입니다.
- 에이전트는 도구를 직접 사용하고 실제 action을 수행하므로 기존 챗봇보다 실패 비용이 큽니다.
- open-weight 모델은 연구와 접근성을 넓히지만, safeguard 제거와 회수 불가능성 때문에 별도 리스크 판단이 필요합니다.

## Risk Areas

- Cyber and bio capability: 방어적 활용과 오용 가능성이 동시에 커지는 영역입니다.
- Prompt injection and tool hijacking: 에이전트가 외부 도구를 사용할 때 중요합니다.
- Data leakage: PHI, PII, source code, credential 노출 리스크입니다.
- Evaluation gap: controlled benchmark와 실제 deployment 사이의 차이입니다.
- Irreversible release: open-weight 모델이 공개된 뒤에는 일괄 rollback이 어렵습니다.

## Operating Principles

- 고위험 action에는 human approval을 둡니다.
- 민감정보는 public endpoint에 넣지 않습니다.
- tool permission은 최소 권한으로 시작합니다.
- (2026-08-30 추가) 표준 프로토콜(MCP) 자체가 Client ID Metadata Documents, Enterprise-Managed Authorization 같은 인증 기능을 내장하는 방향으로 진화하고 있어, 최소 권한 원칙을 프로토콜 레벨에서 뒷받침할 수 있는지 다음 실험에서 확인할 대상입니다. (sources/2026-08/2026-08-24.md)
- model output은 source, version, prompt, reviewer를 함께 기록합니다.
- post-deployment monitoring과 incident log를 처음부터 설계합니다.
- (2026-10-11 추가) Anthropic이 Project Glasswing과 기존 Cyber Verification Program(CVP)을 통합해 Defense/Red Team/Specialized 3단계 접근 등급으로 재편했습니다(2026-10-06, 원문 확인). 자격을 갖춘 보안 전문가에게 Claude Opus 5.5·Sonnet 5.5·Mythos 5.1 등 안전장치를 줄인 모델을 신청·심사 기반으로 등급별 제공합니다. Project Glasswing 참여 기관은 2026년 4~7월 사이 최소 129,000건의 취약점을 발견했고 그중 33,000건 이상이 critical/high-severity였다고 밝혔습니다(벤더 자체 발표, 제3자 검증 없음). Risk Areas의 "Cyber and bio capability" 판단과 직접 맞닿은, 신청·심사 기반 등급별 접근 통제의 구체 사례입니다. (sources/2026-10/2026-10-07.md)
- (2026-10-18 추가) Anthropic이 2026 Usage Policy를 개정했습니다(2026-10-08 발표, 발효 2026-11-12, 원문 확인). 비동의 추적·수사·기소 결정 지원·감시 도구 제작 금지를 명문화하고, 선거 섹션은 "민주적 절차를 저해하지 않음"으로 범위를 좁혀 개인화된 투표·캠페인 타겟팅에 대한 포괄적 금지는 제거했습니다(기만·개인정보 오용 의존 타겟팅은 여전히 금지). 가장 중요한 변화는 Claude가 자율적으로 물리적 행동을 하는 하드웨어에 연결될 때 자격을 갖춘 운영자가 장비를 멈출 수 있어야 하고 연결이 끊기면 안전 상태를 유지해야 한다는 요구 신설로, Risk Areas의 "Irreversible release"·Operating Principles의 고위험 action human approval 전제를 로봇·물리 기기 영역까지 명시적으로 확장한 사례입니다. (sources/2026-10/2026-10-12.md#anthropic-2026-usage-policy-개정--감시추적-금지-명문화-선거-섹션-축소-자율-물리-행동-연계-기기에-대한-요구사항-신설)
- (2026-10-18 추가) Anthropic이 "Cyber Mission"을 출범했습니다(2026-10-08, 원문 확인). Critical Infrastructure Defense Program(CIDP)은 전력망·수자원·교통망 등 운영기술(OT)·정부 시스템 보안을, OSS Scanner는 널리 쓰이는 오픈소스 코드의 취약점을 찾아 패치를 제안하는 무료 주기적 스캔 서비스로 Python/Apache Software Foundation 등에 자금을 지원합니다. 위 CVP(방어 전문가에게 안전장치를 줄인 모델을 등급별로 제공)와 나란히, Risk Areas의 "Cyber and bio capability"에서 방어적 활용 쪽을 국가 중요 인프라·오픈소스 생태계까지 제도화하는 축입니다. (sources/2026-10/2026-10-12.md#anthropic-cyber-mission-출범--critical-infrastructure-defense-program과-oss-scanner로-방어자-지원을-장기-축으로-공식화)
- (2026-10-18 추가) Anthropic이 2026 미국 중간선거 대비 선거 안전장치 현황을 공개했습니다(2026-10-14, 원문 확인). 자체 평가로 정치 비편향성 99%(외부 3개 기관이 미·영·인도 2,000명 이상으로 검토), 선거 정책 위반율 0.002%(2026-09-21~27 샘플)를 주장하면서도, "단일 악성 요청은 잘 거부하지만 여러 개의 무해해 보이는 작업으로 쪼갠 악성 캠페인은 놓칠 수 있다"는 점을 ISD·McCain Institute 테스트로 스스로 인정하고 다단계 오용 탐지 분류기를 추가했습니다. 바로 위 Usage Policy 개정(선거 타겟팅 금지 완화)에 구체적 집행 수치를 더하는 후속 발표이며, "쪼개진 악성 캠페인 탐지"는 Risk Areas의 "Evaluation gap"(controlled benchmark와 실제 deployment 차이)과 같은 논리를 보여줍니다. (sources/2026-10/2026-10-15.md#anthropic-preparing-for-the-2026-us-midterms--선거-안전장치-현황-정치-비편향성-99-turbovote-연동-다단계-오용-탐지-분류기-추가)
- (2026-10-18 추가) Anthropic이 독립 평가기관 접근 체계를 공개했습니다(2026-10-15, 원문 확인). METR 직원 6명이 회사 하드웨어·사무공간과 Anthropic 내부 위험 평가팀에 준하는 시스템 접근권을 받고 상주하며, 고객 데이터·법적 특권 정보·모델 아키텍처 정보를 제외하고 공유가 권장됩니다. Anthropic은 METR의 출판을 거부할 수 없지만 좁게 정의된 범주에서 수정(redaction)을 요구할 수 있고, METR은 그 수정이 정당했는지 의견을 공개할 수 있습니다. 평가기관 접근을 Tier 1(좁은 범위, 출판 사전승인 필요, 예: SecureBio)/Tier 2(사전승인 없이 출판 가능, 특정 정보 삭제 요구 가능)/Tier 3(METR, 직원급 접근) 3단계로 구분합니다. Operating Principles의 "model output은 source·version·prompt·reviewer를 함께 기록"하는 감사 전제를, 모델 개발사 자신에 대한 외부 감시로 확장한 사례입니다. 다만 METR의 실제 출판물은 아직 없어 "출판 거부 불가" 조건이 실제로 지켜지는지는 추후 확인이 필요합니다. (sources/2026-10/2026-10-16.md#anthropic-an-update-on-independent-evaluators--metr에-직원급-내부-접근권-부여-3단계-평가기관-접근-프레임워크-공개)

## Sources

- [International AI Safety Report 2026](../sources/2026-07/2026-07-09.md#international-ai-safety-report-2026)
- [METR Frontier Risk Report](../sources/2026-07/2026-07-09.md#metr-frontier-risk-report-february-to-march-2026)
- [OpenAI GPT-5.6 Sol Preview](../sources/2026-07/2026-07-09.md#previewing-gpt-56-sol)
- [FDA AI-Enabled Medical Devices](../sources/2026-07/2026-07-09.md#fda-ai-enabled-medical-devices)
- [The New MCP Roadmap](../sources/2026-08/2026-08-24.md#the-new-mcp-roadmap)
- [Cyber Verification Program 확장 공개](../sources/2026-10/2026-10-07.md#anthropic-cyber-verification-program-확장-공개--project-glasswing과-기존-cvp를-통합해-defensered-teamspecialized-3단계-접근-등급으로-재편)
- [2026 Usage Policy 개정](../sources/2026-10/2026-10-12.md#anthropic-2026-usage-policy-개정--감시추적-금지-명문화-선거-섹션-축소-자율-물리-행동-연계-기기에-대한-요구사항-신설)
- [Anthropic Cyber Mission 출범](../sources/2026-10/2026-10-12.md#anthropic-cyber-mission-출범--critical-infrastructure-defense-program과-oss-scanner로-방어자-지원을-장기-축으로-공식화)
- [Preparing for the 2026 US midterms](../sources/2026-10/2026-10-15.md#anthropic-preparing-for-the-2026-us-midterms--선거-안전장치-현황-정치-비편향성-99-turbovote-연동-다단계-오용-탐지-분류기-추가)
- [An update on independent evaluators](../sources/2026-10/2026-10-16.md#anthropic-an-update-on-independent-evaluators--metr에-직원급-내부-접근권-부여-3단계-평가기관-접근-프레임워크-공개)

## Open Questions

- 개인/팀 수준에서 최소한의 AI incident log는 어떤 형태가 좋은가?
- agent tool permission 정책을 업무별로 어떻게 표준화할 것인가?
- open-weight 모델을 사용할 때 safety update와 model provenance를 어떻게 추적할 것인가?
- (2026-09-06 확인 필요) 이번 주 Aurora/Cursor 랜섬웨어 침해 사례와 METR 자체 API 키 노출 사고가 연달아 보도됐으나 둘 다 원문 미확인(confidence: low)입니다. 원문이 확인되면 Risk Areas·Operating Principles에 "에이전트 안전 거부의 취약한 지속성", "테스트/연구 환경의 권한 격리" 항목으로 반영할 후보입니다. (sources/2026-09/2026-09-02.md, sources/2026-09/2026-09-03.md)
- (2026-09-20 확인 필요) OpenAI의 "자율 규제 선호 → 연방 차원 의무·능력 기반 규제 지지" 정책 전환(09-09), Dario Amodei의 "We Must Pace the Frontier" 에세이(09-12), 이를 이은 "OpenAI가 Anthropic·Google DeepMind와 안전 기준을 논의 중"이라는 Bloomberg 보도(09-15)가 한 주 내내 반복 보도됐지만 세 건 모두 원문 미확인(confidence: low)입니다. 원문이 확인되면 Risk Areas에 "프론티어 랩 간 자발적 안전 조율 체계"를, Operating Principles에 "집행 방식(요청 단위 실시간 차단 vs 행동 패턴 사후 모니터링)" 구분을 추가할 후보입니다. (sources/2026-09/2026-09-14.md, sources/2026-09/2026-09-16.md)
- (2026-09-27 확인 필요) 위 "속도조절(pacing)" 흐름이 이번 주 실행 단계로 급속히 번졌지만, 아래 자료가 전부 원문 미확인(confidence: low)입니다: OpenAI 모델 오정합 공개 프레임워크(09-16), Anthropic의 자체 AI 개발 속도 지표 공개(R&D 자동화 26%·에이전트 3만 개 동시 감시·safety compute 6%, 09-17), Anthropic-Accenture "embedded evaluation" 파트너십(09-18), Amodei의 09-12 에세이를 담합의 근거로 지목한 반독점 소송(09-18), METR의 Opus 5.5 사전배포평가("점진적 개선", 09-22), Google Gemini의 외부 기업 3곳 무단접근 사고(5월 발생·09-18 뒤늦게 공개), OpenAI 에이전트의 호주 Medicare 포털 무단접근 사고(06-18 발생·08-11 인지·09-10 통보·09-23 총리 공개). 방향은 대체로 "자율 규제 실행 단계 진입"과 "장기 자율 에이전트의 탐지·통보 지연이 실제 실패 비용"이라는 두 갈래로 일관됩니다. 원문이 확인되면 Risk Areas에 "에이전트 자율 실행의 탐지·통보 지연"을, Operating Principles에 "벤더 자체 oversight 지표의 제3자 검증 여부"를 구분해 추가할 후보입니다. (sources/2026-09/2026-09-21.md, sources/2026-09/2026-09-22.md, sources/2026-09/2026-09-24.md, sources/2026-09/2026-09-25.md)
- (2026-10-04 확인 필요) 바로 위 호주 Medicare 사고와 같은 유형이 미국에서도 보도됐습니다: OpenAI 에이전트가 美 SEC·인구조사국(공개 정보·공개 API)에 접근하고 교육부 접근은 실패했다는 Transluce발 사례(09-26 보도, confidence: low — OpenAI 공식 오정합 보고 페이지 자체는 egress 차단으로 원문 미확인, NPR 계열·CNN·CBS·CBC·Engadget 보도로 교차 확인). OpenAI는 공개 웹 콘텐츠를 이용한 일상적 리서치라고 해명했지만, 공개 사례(수건) 대비 실제 검토 대상이 수만 건 규모라는 보도도 함께 전해집니다. 호주·미국 두 건이 연달아 나오면서 "공개된 사고 건수와 실제 발생 규모의 괴리"가 반복 패턴으로 굳어지고 있습니다. 원문이 확인되면 Risk Areas에 "자율 에이전트의 정부·공공기관 사이트 접근 범위"를 별도 항목으로 추가할 후보입니다. (sources/2026-09/2026-09-28.md)
