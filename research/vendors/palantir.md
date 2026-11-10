# Palantir — 컨텍스트 엔지니어링 관련 솔루션 (조사일 2026-11-11)

## 한 줄 요약 (이 회사의 전략)
"온톨로지(업무 객체·관계·행동의 모델)가 곧 에이전트의 컨텍스트이자 손발"이라는 전략. 데이터를 객체·링크로 묶고, 그 위에 **액션(쓰기)·함수(결정론 계산)·권한(마킹)** 을 같은 모델에 붙여 둔 뒤, 사내 에이전트(Chatbot Studio·AI FDE·AIP Analyst)와 외부 에이전트(Ontology MCP·Claude/OpenAI/Google SDK 템플릿)가 모두 이 한 층을 통해서만 읽고 쓰게 만든다. 2026년에는 "에이전트를 만드는 에이전트"(AI FDE)와 "AI 시스템을 스스로 개선하는 에이전트 함대"(AIP Evolve)로 폐루프까지 확장했다.

## 솔루션 목록
| 제품 | 무엇을 하나(쉬운 말) | 상태(날짜) | 층 | 근거 URL |
|---|---|---|---|---|
| Foundry Ontology (object/link/action types, interfaces) | 회사 데이터를 "주문·설비·고객" 같은 객체와 그 관계로 묶고, 객체에 할 수 있는 행동(액션)까지 정의하는 운영 모델. 2026-10 Workshop 에서 인터페이스(공통 형태) GA, 2026-08 객체 타임라인으로 사람·에이전트 편집 이력 관측 | GA(장기 운영), 인터페이스 GA 2026-10-06 | L3●, L4◐, L5◐, L7●, GOV● | https://palantir.com/docs/foundry/ontology/why-ontology/ , https://www.palantir.com/docs/foundry/announcements/2026-10 , https://www.palantir.com/docs/foundry/announcements/2026-08 |
| AIP Logic + Functions (TS/Python) | 노코드 블록으로 LLM 호출·온톨로지 조회·계산을 엮은 함수. 쓰기는 반드시 액션 안에서 실행될 때만 반영되고, "staged writes"(베타)로 실행 끝에 한꺼번에 적용 | GA(Logic), staged writes 베타, TS/Python 함수 Global Branching GA 2026-10-13 | L4◐, L6◐, L7● | https://www.palantir.com/docs/foundry/logic/overview/ , https://palantir.com/docs/foundry/logic/staged-writes/ |
| AIP Chatbot Studio (구 AIP Agent Studio) | LLM + 온톨로지 + 문서 + 도구를 묶어 대화형 비서를 만드는 빌더. Workshop 내장·OSDK/API 외부 호출·AIP Assist/Threads 배포 가능. 2026-04 "Agent"→"Chatbot" 으로 이름 변경 | GA, 리브랜딩 2026-04-22 발표(4월 27일 주 적용) | L1◐, L3◐, L6●, L7●, GOV● | https://www.palantir.com/docs/foundry/chatbot-studio/overview/ , https://www.palantir.com/docs/foundry/announcements/2026-04 |
| Pro-code agents (Agent templates) + OSDK | Claude Agent SDK·OpenAI Agents SDK·Google ADK 템플릿으로 코드형 에이전트를 만들고, 선택한 객체·액션·함수로 OSDK와 Ontology MCP를 자동 생성해 붙임. 토큰 없이 스코프 권한으로 인증 | 발표 2026-07-09(상태 미표기), OSDK React GA 2026-05, Pilot(OSDK 앱 생성 AI) GA 2026-10-29 | L1●, L6●, L7●, GOV● | https://palantir.com/docs/foundry/agents/agent-templates/ , https://www.palantir.com/docs/foundry/announcements/2026-07 |
| Ontology MCP (OMCP) | 외부 에이전트(MCP 클라이언트)가 온톨로지 객체를 읽고, 액션·함수를 도구로 호출하게 하는 MCP 서버. OAuth 2.0 으로 사용자 권한 그대로 실행. Microsoft Copilot Studio 연동 | GA 2026-06-25 (6월 16일 주 롤아웃), Copilot Studio 연동 발표 2026-03-26 | L1●, L3◐, L7●, GOV● | https://palantir.com/docs/foundry/ontology-mcp/overview/ , https://www.palantir.com/docs/foundry/announcements/2026-06 |
| Palantir MCP (PMCP) | 코딩 에이전트가 Foundry 안에서 개발(파이프라인·온톨로지 구조 설정·OSDK 앱)을 하게 하는 빌더용 MCP. 구조는 바꿀 수 있지만 데이터는 못 씀. 필요할 때만 도구를 켜는 "tool search" 모드로 토큰 절약 | GA 2026-06-25, tool search 2026-06-30 | L1●, L3◐, L6◐, GOV◐ | https://www.palantir.com/docs/foundry/palantir-mcp/ , https://www.palantir.com/docs/foundry/announcements/2026-06 |
| AIP Analyst | 온톨로지 데이터를 대화로 탐색·분석하는 에이전트. 2026-08 재사용 지침 "Skills"와 과거 분석을 틀로 불러오는 "Analysis lookup", 2026-10 그룹 스킬·모델 등급(Fast/Balanced/Smart) 추가. 대화는 분석 리소스로 저장 | 베타 2025-11-17 주 → GA 2026-04-13 주 | L3◐, L4●, L5◐, L6● | https://palantir.com/docs/foundry/announcements/2026-03/ , https://www.palantir.com/docs/foundry/announcements/2026-08 , https://www.palantir.com/docs/foundry/announcements/2026-10 |
| AI FDE (AI Forward Deployed Engineer) | 자연어로 Foundry 를 직접 조작하는 에이전트(파이프라인·온톨로지·함수·OSDK 앱·권한 점검). 실행→결과 관찰→수정의 폐루프로 일하고, 변경은 기본적으로 브랜치 제안/PR 로 사람 검토. 2026-08 Automate 설정 도구 추가 | 베타 2025-11-17 주 → GA 2026-03-12 | L4◐, L6●, L7●, GOV●, OBS◐ | https://www.palantir.com/docs/foundry/ai-fde/overview , https://palantir.com/docs/foundry/announcements/2026-03/ |
| Automate (+ Autopilot) | "이 일이 생기면 저걸 하라" 업무 자동화. 시간·객체 변화·데이터셋 갱신 조건으로 액션·Logic·함수·알림 실행, 중요한 쓰기는 사람 검토용으로 단계화 권장. Autopilot 으로 실행 추적·디버깅 | GA(Automate), Autopilot 베타 2026-03-19, Global Branching 지원 2026-07-09 | L4●, L7●, GOV◐, OBS◐ | https://www.palantir.com/docs/foundry/automate/overview/ , https://palantir.com/docs/foundry/announcements/2026-03/ |
| AIP Evals + AIP Observability + Workflow Lineage | LLM 기반 함수용 테스트 스위트(내장/LLM-판사 평가자, 실패 원인 자동 묶음), 함수·액션·자동화·LLM 호출 트레이싱, 실행 흐름의 계보 그래프 | Evals GA(상세 상태 미표기), 결과 분석기 2025-11-18, Observability 2025-11-06, Python Model Evaluations 2026-07-07 | L5◐, OBS● | https://www.palantir.com/docs/foundry/aip-evals/overview , https://palantir.com/docs/foundry/announcements/2025-11/ |
| AIP Evolve | 목표·검증 기준·한도를 주면 AI FDE 에이전트 여러 개가 프롬프트 수정·모델 교체 후보를 만들고 평가로 검증해 브랜치 제안으로 올림 (AI 시스템의 자가 개선 루프) | 베타 2026-08-18 → GA 2026-09-08 | L4◐, L5◐, OBS● | https://palantir.com/docs/foundry/aip-evolve/overview/ , https://www.palantir.com/docs/foundry/announcements/2026-09 |
| 보안·거버넌스 (Markings/CBAC, LLM 마킹 허용목록, Global Branching, Registered models) | 데이터에 붙은 마킹이 파생물까지 따라가고, 관리자가 "어떤 마킹의 데이터가 어느 LLM 에 가도 되는지" 허용목록으로 제한. 모든 변경을 브랜치에서 시험 후 승인 병합. 자체 모델 등록(BYOM)과 모델별 정책 | Global Branching GA 2026-05-18 주, Registered models GA 2026-05-21, LLM 마킹 허용목록(에이전트 포함) 2026-10-12 | GOV●, L6◐ | https://palantir.com/docs/foundry/aip/control-llm-data-access-with-markings/ , https://www.palantir.com/docs/foundry/announcements/2026-05 , https://www.palantir.com/docs/foundry/announcements/2026-10 |

## 회사 전체 층 커버리지
- **L1 연결·원천 ●** — Foundry 데이터 연결·파이프라인 + Ontology MCP/Palantir MCP(양방향 MCP), OSDK. 벡터 저장소는 별도 제품으로 내세우지 않음.
- **L2 의미(지표) ◐ 약함** — 지표·차원 전용 시맨틱 레이어 제품은 없음. 객체 속성·Insight/Quiver 분석으로 대신하며 "지표 정의 SSOT" 개념은 확인 못함.
- **L3 관계·정체성 ● 최강** — 온톨로지(객체·링크·인터페이스)가 플랫폼의 중심.
- **L4 절차·역할 ●** — 액션 타입(업무 행동 정의), Automate, AIP Analyst Skills·그룹 스킬.
- **L5 기억·이력 ◐** — 객체 편집 타임라인, Workflow/Data Lineage, 저장된 분석·Analysis lookup. 에이전트 장기 기억 전용 제품은 문서에서 확인 못함.
- **L6 런타임 창 관리 ●** — Chatbot Studio 컨텍스트 유형·애플리케이션 상태, AI FDE 모드/스킬, PMCP tool search, 모델 등급 라우팅.
- **L7 실행·검증 ● 최강** — 액션(검증 규칙 포함 쓰기), 결정론 함수, staged writes, 시뮬레이션 평가.
- **GOV ● 최강** — 마킹·CBAC·행/열 보안이 LLM·에이전트 호출까지 전파, 브랜치 기반 사람 승인, 사용자별 LLM 속도 제한.
- **OBS ●** — AIP Evals, AIP Observability, Autopilot, Workflow Lineage, Evolve.

## 2026년 주요 움직임 (최신순)
- 2026-10-29 Pilot(OSDK React 앱 생성 AI) GA.
- 2026-10-13 TypeScript v2·Python 함수의 Global Branching GA.
- 2026-10-12 AIP 에서 LLM 으로 갈 수 있는 데이터를 마킹 허용목록으로 제한(AI FDE 같은 에이전트 포함).
- 2026-10-06 Workshop 에서 온톨로지 인터페이스 GA.
- 2026-10-01 AIP Analyst 조직 기본값·그룹 스킬·모델 등급(Fast/Balanced/Smart).
- 2026-09-29 OSDK React 컴포넌트 베타.
- 2026-09-08 AIP Evolve GA (8월 18일 베타).
- 2026-08-27 AI FDE 안에서 Automate 자동화 설정.
- 2026-08-18 AIP Analyst Skills·Analysis lookup.
- 2026-08-11 객체 타임라인: 에이전트·사람 편집 관측.
- 2026-07-09 Pro-code agents: Claude Agent SDK/OpenAI Agents SDK/Google ADK 템플릿, OSDK·OMCP·PMCP 스코프 인증 내장.
- 2026-07-07 Evals 용 Python Model Evaluations API.
- 2026-07-02 AIP Analyst 대화를 분석 리소스로 저장, 사용자별 LLM 속도 제한.
- 2026-06-30 Palantir MCP tool search 모드, 객체/속성 보안 정책 테스트 GA.
- 2026-06-25 Palantir MCP GA, Ontology MCP GA (OAuth 2.0, 사용자 권한으로 실행).
- 2026-05-21 Registered models(BYOM) GA, MCP Hub 에 OMCP 서버 노출, 온톨로지 리소스 CBAC.
- 2026-05-18 주 Global Branching GA.
- 2026-04-22 AIP Agent Studio → AIP Chatbot Studio, AIP Agents → AIP Chatbots 리브랜딩 (4월 27일 주 적용). "에이전트" 명칭은 AI FDE·pro-code agents 쪽으로 이동한 것으로 보임.
- 2026-04-13 주 AIP Analyst GA.
- 2026-03-26 Ontology MCP ↔ Microsoft Copilot Studio 연동(Teams·Outlook 에서 온톨로지 사용).
- 2026-03-19 Autopilot 베타. 2026-03-12 AI FDE GA.
- 2026-01-22(2차 출처 기준) 공식 블로그 "Securing Agents in Production (Agentic Runtime #1)" — Rubix 격리, 출처(provenance) 기반 도구 인가, 온톨로지 인지형 접근 제어.

## 경쟁·파트너 관계
- **모델 파트너(중립 모델 허브)**: Anthropic(Claude Opus 5.5 등), OpenAI(GPT-6 계열), Google(Gemini), xAI, Meta 계열 오픈 모델, DeepSeek·Kimi·GLM 등을 Bedrock/Vertex/Azure/Fireworks 경유로 제공. 모델은 상품으로 취급하고 온톨로지·거버넌스를 차별점으로 둠.
- **에이전트 프레임워크 파트너**: Claude Agent SDK, OpenAI Agents SDK, Google ADK 를 1급 템플릿으로 수용 → 프레임워크 경쟁이 아니라 "어떤 에이전트든 온톨로지에 붙인다"는 위치.
- **Microsoft**: Copilot Studio 가 Ontology MCP 를 소비(Teams/Outlook).
- **경쟁**: Snowflake·Databricks(시맨틱 뷰/메트릭 뷰 중심의 L2 강자 vs Palantir 의 L3·L7), Microsoft Fabric IQ 온톨로지, ServiceNow·Salesforce(업무 객체+에이전트), 에이전트 런타임 업체(Agno 등)가 Palantir 의 "Agentic Runtime" 서술을 직접 언급.
- **NVIDIA**: 2026-03 "Sovereign AI OS" 레퍼런스 아키텍처 보도가 있으나 단일 2차 출처라 미확인.

## 불확실·확인 못한 것
- **Apollo**: 자율 배포 플랫폼으로 소개되나 2026년 에이전트·컨텍스트 관련 신규 발표는 공식 출처에서 찾지 못해 목록에서 제외(L0/운영 기반에 가까움).
- **AIP Assist / AIP Threads**: Threads 문서는 존재하나 상태(베타 여부) 표기가 페이지마다 다르고(검색 제목은 "[Beta]", 본문엔 미표기) 출시일 미확인. 그래서 Chatbot Studio 배포 채널로만 기재.
- **에이전트 장기 기억**: 공식 블로그가 "memory taxonomy"를 다룬다는 2차 언급만 있고, blog.palantir.com 원문은 WebFetch 403 으로 직접 확인 못함. 블로그 게시일(2026-01-22)도 집계 사이트 기준.
- **AIP Evals 의 GA 날짜**, **pro-code agents 의 정식 상태(베타/GA)**, **Ontology MCP 의 구체 도구 이름**은 문서에 미표기.
- **L2 시맨틱(지표) 계층**: 전용 제품 부재로 판단했으나, Insight/Quiver·Ontology SQL 함수(베타)가 일부 역할을 할 수 있어 ◐ 로 둠.
- AIP Analyst Skills 세부 동작(대화를 스킬로 내보내기 등)은 2차 출처(BestHub/DataFunTalk) 내용이며, 공식은 2026-08-18 공지 제목 수준만 확인.

## 데이터 블록
```yaml
vendor: palantir
name: Palantir
category: data_platform
products:
  - id: palantir-ontology
    name: Foundry Ontology (object/link/action types, interfaces)
    status: GA
    status_date: 2026-10
    layers: {L3: ●, L4: ◐, L5: ◐, L7: ●, GOV: ●}
    x: 2
    y: -2
    xy_reason: "업무 객체와 그에 대한 행동(액션)을 사람이 모델링해 두는 운영 계층 — 쓰기 중심, 사전 큐레이션"
    maturity: 3
    evidence:
      - {url: https://palantir.com/docs/foundry/ontology/why-ontology/, kind: official, date: 2026-11-11}
      - {url: https://www.palantir.com/docs/foundry/announcements/2026-10, kind: official, date: 2026-10-06}
      - {url: https://www.palantir.com/docs/foundry/announcements/2026-08, kind: official, date: 2026-08-11}
  - id: palantir-aip-logic
    name: AIP Logic + Functions
    status: GA
    status_date: 2026-10
    layers: {L4: ◐, L6: ◐, L7: ●}
    x: 1
    y: -1
    xy_reason: "개발자가 정의한 LLM+결정론 함수, 쓰기는 액션 경유로만 반영"
    maturity: 4
    evidence:
      - {url: https://www.palantir.com/docs/foundry/logic/overview/, kind: official, date: 2026-11-11}
      - {url: https://palantir.com/docs/foundry/logic/staged-writes/, kind: official, date: 2026-11-11}
      - {url: https://www.palantir.com/docs/foundry/announcements/2026-10, kind: official, date: 2026-10-13}
  - id: palantir-chatbot-studio
    name: AIP Chatbot Studio (formerly AIP Agent Studio)
    status: GA
    status_date: 2026-04
    layers: {L1: ◐, L3: ◐, L6: ●, L7: ●, GOV: ●}
    x: 1
    y: 0
    xy_reason: "빌더가 컨텍스트 유형(온톨로지·문서·앱 변수)과 도구를 지정하고, 런타임에 LLM 이 그 범위 안에서 검색·실행"
    maturity: 3
    evidence:
      - {url: https://www.palantir.com/docs/foundry/chatbot-studio/overview/, kind: official, date: 2026-11-11}
      - {url: https://www.palantir.com/docs/foundry/announcements/2026-04, kind: official, date: 2026-04-22}
  - id: palantir-procode-agents
    name: Pro-code agents (Agent templates) + OSDK
    status: announced
    status_date: 2026-07
    layers: {L1: ●, L6: ●, L7: ●, GOV: ●}
    x: 1
    y: 1
    xy_reason: "외부 SDK 에이전트 루프가 생성된 OSDK/OMCP 도구로 런타임에 온톨로지를 탐색·조작"
    maturity: 3
    evidence:
      - {url: https://palantir.com/docs/foundry/agents/agent-templates/, kind: official, date: 2026-11-11}
      - {url: https://www.palantir.com/docs/foundry/announcements/2026-07, kind: official, date: 2026-07-09}
      - {url: https://www.palantir.com/docs/foundry/announcements/2026-10, kind: official, date: 2026-10-29}
  - id: palantir-ontology-mcp
    name: Ontology MCP (OMCP)
    status: GA
    status_date: 2026-06
    layers: {L1: ●, L3: ◐, L7: ●, GOV: ●}
    x: 2
    y: 1
    xy_reason: "외부 에이전트가 객체 읽기와 액션 실행(쓰기)을 사용자 권한으로 런타임 호출"
    maturity: 3
    evidence:
      - {url: https://palantir.com/docs/foundry/ontology-mcp/overview/, kind: official, date: 2026-11-11}
      - {url: https://www.palantir.com/docs/foundry/announcements/2026-06, kind: official, date: 2026-06-25}
      - {url: https://palantir.com/docs/foundry/announcements/2026-03/, kind: official, date: 2026-03-26}
  - id: palantir-mcp
    name: Palantir MCP (PMCP)
    status: GA
    status_date: 2026-06
    layers: {L1: ●, L3: ◐, L6: ◐, GOV: ◐}
    x: 1
    y: 1
    xy_reason: "코딩 에이전트가 플랫폼 구조(온톨로지 타입·파이프라인)를 만드는 빌더용 — 데이터는 못 씀, tool search 로 런타임 도구 발견"
    maturity: 2
    evidence:
      - {url: https://www.palantir.com/docs/foundry/palantir-mcp/, kind: official, date: 2026-11-11}
      - {url: https://www.palantir.com/docs/foundry/announcements/2026-06, kind: official, date: 2026-06-30}
  - id: palantir-aip-analyst
    name: AIP Analyst
    status: GA
    status_date: 2026-04
    layers: {L3: ◐, L4: ●, L5: ◐, L6: ●}
    x: -1
    y: 1
    xy_reason: "온톨로지 데이터에 대한 질의·분석 에이전트(읽기 중심), Skills·과거 분석 재사용으로 런타임 축적"
    maturity: 2
    evidence:
      - {url: https://palantir.com/docs/foundry/announcements/2026-03/, kind: official, date: 2026-03-31}
      - {url: https://www.palantir.com/docs/foundry/announcements/2026-08, kind: official, date: 2026-08-18}
      - {url: https://www.palantir.com/docs/foundry/announcements/2026-10, kind: official, date: 2026-10-01}
      - {url: https://www.besthub.dev/articles/palantir-adds-skills-to-aip-analyst-enterprise-ai-gains-reusable-analysis-methods-d273ae25511d, kind: secondary, date: 2026-08-18}
  - id: palantir-ai-fde
    name: AI FDE (AI Forward Deployed Engineer)
    status: GA
    status_date: 2026-03
    layers: {L4: ◐, L6: ●, L7: ●, GOV: ●, OBS: ◐}
    x: 1
    y: 2
    xy_reason: "최소 컨텍스트로 시작해 사용자가 넘긴 자료와 실행 결과를 관찰하며 스스로 플랫폼을 조작·수정"
    maturity: 4
    evidence:
      - {url: https://www.palantir.com/docs/foundry/ai-fde/overview, kind: official, date: 2026-11-11}
      - {url: https://palantir.com/docs/foundry/announcements/2026-03/, kind: official, date: 2026-03-12}
      - {url: https://palantir.com/docs/foundry/announcements/2025-11/, kind: official, date: 2025-11-18}
  - id: palantir-automate
    name: Automate (+ Autopilot)
    status: GA
    status_date: 2026-07
    layers: {L4: ●, L7: ●, GOV: ◐, OBS: ◐}
    x: 2
    y: -1
    xy_reason: "사람이 정의한 조건→효과 규칙으로 액션·Logic 을 자동 실행(쓰기), 단계화된 사람 검토 지원"
    maturity: 3
    evidence:
      - {url: https://www.palantir.com/docs/foundry/automate/overview/, kind: official, date: 2026-11-11}
      - {url: https://palantir.com/docs/foundry/announcements/2026-03/, kind: official, date: 2026-03-19}
      - {url: https://www.palantir.com/docs/foundry/announcements/2026-07, kind: official, date: 2026-07-09}
  - id: palantir-aip-evals-observability
    name: AIP Evals + AIP Observability + Workflow Lineage
    status: GA
    status_date: 2026-07
    layers: {L5: ◐, OBS: ●}
    x: 0
    y: -1
    xy_reason: "사람이 만든 테스트 스위트·평가자로 LLM 함수를 검증하고 실행을 추적하는 관측 기둥"
    maturity: 4
    evidence:
      - {url: https://www.palantir.com/docs/foundry/aip-evals/overview, kind: official, date: 2026-11-11}
      - {url: https://palantir.com/docs/foundry/announcements/2025-11/, kind: official, date: 2025-11-06}
      - {url: https://www.palantir.com/docs/foundry/announcements/2026-07, kind: official, date: 2026-07-07}
  - id: palantir-aip-evolve
    name: AIP Evolve
    status: GA
    status_date: 2026-09
    layers: {L4: ◐, L5: ◐, OBS: ●}
    x: 0
    y: 2
    xy_reason: "AI FDE 에이전트 함대가 프롬프트·모델 후보를 스스로 만들고 평가로 검증해 개선안을 제안"
    maturity: 5
    evidence:
      - {url: https://palantir.com/docs/foundry/aip-evolve/overview/, kind: official, date: 2026-11-11}
      - {url: https://www.palantir.com/docs/foundry/announcements/2026-09, kind: official, date: 2026-09-08}
      - {url: https://www.palantir.com/docs/foundry/announcements/2026-08, kind: official, date: 2026-08-18}
  - id: palantir-governance
    name: Security & governance (Markings/CBAC, LLM marking allowlist, Global Branching, Registered models)
    status: GA
    status_date: 2026-10
    layers: {L6: ◐, GOV: ●}
    x: 1
    y: -2
    xy_reason: "관리자가 사전에 정한 마킹·정책·브랜치 승인이 모든 LLM·에이전트 호출에 강제됨"
    maturity: 3
    evidence:
      - {url: https://palantir.com/docs/foundry/aip/control-llm-data-access-with-markings/, kind: official, date: 2026-11-11}
      - {url: https://www.palantir.com/docs/foundry/announcements/2026-10, kind: official, date: 2026-10-12}
      - {url: https://www.palantir.com/docs/foundry/announcements/2026-05, kind: official, date: 2026-05-21}
      - {url: https://engineered.at/articles/securing-agents-in-production-agentic-runtime-1, kind: secondary, date: 2026-01-22}
```

## 참고자료 (References)
- Palantir Foundry 월간 공지: 2025-11, 2026-03, 2026-04, 2026-05, 2026-06, 2026-07, 2026-08, 2026-09, 2026-10 (https://www.palantir.com/docs/foundry/announcements/YYYY-MM)
- 제품 문서: Ontology MCP, Palantir MCP, Chatbot Studio, Agent templates, AI FDE, AIP Logic, Automate, AIP Evals, AIP Evolve, AIP Threads, LLM 마킹 제어 (위 표 URL)
- 2차: engineered.at (Palantir 블로그 Agentic Runtime #1 요약), BestHub (AIP Analyst Skills 해설)
