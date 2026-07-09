---
title: "Clinical / Healthcare AI"
topic: clinical-healthcare
last_reviewed: 2026-07-09
---

# Clinical / Healthcare AI

임상 데이터, EDC, 의료 워크플로, 규제 환경, 의료 도메인에서의 AI 적용 가능성을 정리하는 주제 파일입니다.

## Current View

- 임상 AI는 "모델이 의학 지식을 얼마나 잘 맞히는가"에서 "실제 workflow에서 안전하고 검증 가능하게 작동하는가"로 초점이 이동 중입니다.
- 진단/치료 의사결정보다 문서화, 행정 업무, 데이터 추출, trial operation 보조가 먼저 안정적으로 적용될 가능성이 큽니다.
- patient-facing AI는 oversight를 환자에게 기대하면 안 되며, 결과 지표와 harm safeguard가 필요합니다.

## Use Cases

- EHR/의무기록에서 구조화 데이터 추출.
- clinical trial query drafting과 source data review 보조.
- protocol, CRF, edit check, coding guideline 요약.
- 임상 문서 초안 작성과 번역.
- clinician-facing decision support의 근거 요약.
- patient-facing history taking, coaching, translation. 단, 안전장치와 escalation 정책이 필요합니다.

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

## Open Questions

- EDC/임상 데이터 업무에서 AI 적용의 첫 실험은 query drafting, coding support, 문서 요약 중 무엇이 가장 안전한가?
- prospective evaluation을 개인 또는 소규모 팀 수준에서 어떻게 설계할 수 있는가?
- 모델 output을 audit 가능한 evidence trail로 남기는 최소 양식은 무엇인가?
