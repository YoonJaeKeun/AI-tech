---
title: "Clinical / Healthcare AI"
topic: clinical-healthcare
last_reviewed: 2026-11-01
---

# Clinical / Healthcare AI

임상 데이터, EDC, 의료 워크플로, 규제 환경, 의료 도메인에서의 AI 적용 가능성을 정리하는 주제 파일입니다.

## Current View

- 임상 AI는 "모델이 의학 지식을 얼마나 잘 맞히는가"에서 "실제 workflow에서 안전하고 검증 가능하게 작동하는가"로 초점이 이동 중입니다.
- 진단/치료 의사결정보다 문서화, 행정 업무, 데이터 추출, trial operation 보조가 먼저 안정적으로 적용될 가능성이 큽니다.
- patient-facing AI는 oversight를 환자에게 기대하면 안 되며, 결과 지표와 harm safeguard가 필요합니다.
- (2026-11-01 갱신) 기존 Use Cases(문서화·행정 업무·trial operation 보조)보다 한 걸음 더 나간 유형이 확인됐습니다: 전임상(preclinical) 단계의 분자·항체 설계 의사결정에 Claude가 직접 개입하는 사례입니다(Anthropic·제약/바이오 6개사 파트너십). 다만 이는 환자 대상 임상 의사결정이 아니라 연구실 단계 R&D이므로, Constraints의 "prospective evaluation 없이 임상 의사결정을 자동화하는 사용"을 경계하는 기존 판단과 충돌하지는 않습니다. 결과는 모두 Anthropic·파트너사 자체 발표이며 독립 동료 심사나 제3자 재현 검증은 거치지 않았다는 한계가 있습니다. (sources/2026-10/2026-10-28.md)

## Use Cases

- EHR/의무기록에서 구조화 데이터 추출.
- clinical trial query drafting과 source data review 보조.
- protocol, CRF, edit check, coding guideline 요약.
- 임상 문서 초안 작성과 번역.
- clinician-facing decision support의 근거 요약.
- patient-facing history taking, coaching, translation. 단, 안전장치와 escalation 정책이 필요합니다.
- (2026-11-01 추가) 전임상 R&D 보조: 분자/항체 설계 변이 탐색, 실험 데이터 분석, 규제 제조 문서 검토·초안 작성, 임상시험 계획의 성공 가능성 평가. 환자가 아니라 연구실 단계 대상입니다. (sources/2026-10/2026-10-28.md)
- (2026-11-01 추가) 기관·재단 단위의 기초 생명과학 연구 가속: 유전체학·생의학 연구기관(Wellcome Sanger Institute, Francis Crick Institute, Gladstone Institutes, gnomAD/Broad Institute, Centre for Population Genomics 등)과의 직접 파트너십. 다만 이 발표에 포함된 20개 파트너 중 상당수(천체물리·기후·수학·화학)는 생명과학 범위 밖이라, 이 항목은 발표의 일부만을 대표합니다. (sources/2026-10/2026-10-29.md)

## Constraints

- 개인정보/보안: PHI, PII, confidential study data는 공개 LLM에 직접 입력하지 않습니다.
- 규제: SaMD, clinical decision support, AI-enabled medical device 여부를 구분해야 합니다.
- 검증/감사: prospective evaluation, post-deployment monitoring, audit log, versioning이 필요합니다.
- 도메인 전문가 검토: 임상 맥락, endpoint, protocol deviation, query impact는 전문가 검토가 필요합니다.
- workflow design: 인간과 AI의 역할, escalation, override, training을 함께 설계해야 합니다.

## Relevant Technologies

- LLM 기반 문서 요약과 정보 추출.
- multimodal 모델을 활용한 이미지/텍스트 통합 검토.
- retrieval-augmented generation for protocol/guideline grounding.
- local/private deployment 또는 enterprise-controlled API.
- structured output, validation rules, traceable citation.

## Sources

- [FDA AI-Enabled Medical Devices](../sources/2026-07/2026-07-09.md#fda-ai-enabled-medical-devices)
- [State of Clinical AI Report 2026](../sources/2026-07/2026-07-09.md#state-of-clinical-ai-report-2026)
- [Stanford AI Index 2026](../sources/2026-07/2026-07-09.md#the-2026-ai-index-report)
- [Anthropic 생명과학 Guest Investigator 공개 모집](../sources/2026-10/2026-10-23.md#anthropic-생명과학-분야-guest-investigator-공개-모집)
- [Anthropic 신약개발 파트너십 6건 초기 결과](../sources/2026-10/2026-10-28.md#anthropic-신약개발-파트너십-6건의-초기-결과-공개--claude-보조-분자-설계규제문서-검토임상시험-계획-평가-모두-preclinical)
- [Anthropic AI for Science 재단·연구기관 파트너십 확장](../sources/2026-10/2026-10-29.md#anthropic-ai-for-science-프로그램을-개인-연구자-지원에서-재단연구기관-파트너십으로-확장--sloansimonsnsf-등-20개-기관-공개)

## Open Questions

- EDC/임상 데이터 업무에서 AI 적용의 첫 실험은 query drafting, coding support, 문서 요약 중 무엇이 가장 안전한가?
- prospective evaluation을 개인 또는 소규모 팀 수준에서 어떻게 설계할 수 있는가?
- 모델 output을 audit 가능한 evidence trail로 남기는 최소 양식은 무엇인가?
