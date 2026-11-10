# Snowflake — 컨텍스트 엔지니어링 관련 솔루션 (조사일 2026-11-11)

## 한 줄 요약 (이 회사의 전략)
"지표 의미(semantic views)를 한 번 정의해 모든 사람·에이전트가 재사용"하는 L2 중심 전략에서 출발해, 2026년에는 (1) 그 의미를 AI가 대신 만들어 주고(Semantic View Autopilot), (2) 모델링되지 않은 데이터의 맥락까지 사용 이력에서 자동으로 뽑아내며(Cortex Sense), (3) 이를 Horizon Catalog 아래 하나의 "통제된 컨텍스트 층"(Horizon Context)으로 묶어 자사 에이전트(CoWork·CoCo)와 외부 에이전트(MCP) 모두에 공급하는 방향으로 확장 중이다. 행동(쓰기) 쪽은 아직 약하고, MCP 거버넌스는 Natoma 인수로 보강하려 한다.

## 솔루션 목록
| 제품 | 무엇을 하나(쉬운 말) | 상태 (날짜) | 층 | 근거 URL |
|---|---|---|---|---|
| Semantic Views | "매출·NRR" 같은 지표·차원·테이블 관계를 DB 객체로 한 번 정의해 BI와 에이전트가 같이 쓰게 함 | GA (질의 2025-08-26, 공유 2025-11-04) | L2 ●, GOV ◐ | https://docs.snowflake.com/release-notes/2025/9_25 , https://docs.snowflake.com/release-notes/2025/other/2025-11-04-sharing-semantic-views |
| Semantic View Autopilot | 기존 SQL·Tableau·Power BI 파일과 쿼리 이력을 읽어 시맨틱 뷰 초안을 AI가 자동 생성 | GA (2026-02-03), Power BI 수집 GA 2026-08-18 | L2 ●, L5 ◐ | https://www.snowflake.com/en/news/press-releases/snowflake-delivers-semantic-view-autopilot-as-the-foundation-for-trusted-scalable-enterprise-ready-AI/ , https://docs.snowflake.com/release-notes/2026/other/2026-08-18-semantic-views-power-bi-ingestion-ga |
| Horizon Context (Semantic Studio·메타데이터 커넥터·리니지 포함) | 의미·메타데이터·계보·거버넌스를 사람과 AI가 함께 쓰는 하나의 "통제된 컨텍스트 층"으로 묶은 Horizon Catalog의 상위 개념 | 발표 2026-06-02 (Semantic Studio 비공개 프리뷰, 메타데이터 커넥터 Preview, OpenLineage API 공개 프리뷰) | L1 ◐, L2 ●, L5 ●, GOV ● | https://www.snowflake.com/en/blog/horizon-context-governed-context/ , https://docs.snowflake.com/en/user-guide/snowflake-horizon/horizon-context |
| Cortex Sense | 시맨틱 뷰가 없는 테이블에 대해서도 쿼리 이력·dbt 모델·BI 지표에서 맥락을 자동 학습하고, 충돌하는 신호를 권위·인기·신선도로 순위 매겨 에이전트에 공급 | 비공개 프리뷰 (2026-07 예정 발표 → 문서상 Private Preview) | L2 ◐, L5 ◐, L6 ●, OBS ◐ | https://www.snowflake.com/en/blog/enterprise-ai-agents-grounded-context/ , https://docs.snowflake.com/LIMITEDACCESS/cortex-sense-reference |
| Cortex Analyst | 시맨틱 뷰를 바탕으로 자연어 질문을 SQL로 바꿔 숫자 질문에 답함 | GA (GA 일자 미확인) | L2 ◐, L7 ◐ | https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp |
| Cortex Search | 문서·텍스트에 대한 하이브리드(키워드+벡터) 검색 인덱스를 관리형으로 제공 | GA (GA 일자 미확인) | L1 ●, L6 ◐ | https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp |
| Cortex Agents (+ Agent evaluations, Agent Sharing) | Analyst·Search·커스텀 도구를 엮어 계획→도구 호출→답변하는 에이전트 런타임. 평가 기능과 계정 간 공유 포함 | GA 2025-11-04 / 평가 GA 2026-03-13 / Sharing 공개 프리뷰 2026-06-02 | L6 ●, L7 ◐, GOV ◐, OBS ● | https://docs.snowflake.com/release-notes/2025/other/2025-11-04-cortex-agents , https://docs.snowflake.com/release-notes/2026/other/2026-03-13-cortex-agent-evaluations |
| Snowflake CoWork (구 Snowflake Intelligence) | 업무 사용자용 대화형 에이전트. 메모리·사용자 스킬·자동화·멀티에이전트·MCP 커넥터 액션 추가 중 | Intelligence GA 2025-11-04 → 2026-06-02 개명, 메모리·스킬 "곧 공개 프리뷰" | L4 ◐, L5 ◐, L6 ●, L7 ◐, GOV ◐ | https://snowflake.com/en/blog/snowflake-cowork-personal-work-agent/ |
| Snowflake CoCo (구 Cortex Code) | 데이터 엔지니어용 코딩 에이전트. 시맨틱 뷰를 자동으로 찾아 쓰고, 파이프라인·SQL·ML 작업을 수행. SAP용 스킬 등 | CLI GA 2026-02, Snowsight GA 2026-03-09, 2026-06-02 개명 | L4 ◐, L6 ●, L7 ● | https://docs.snowflake.com/en/release-notes/2026/other/2026-03-09-cortex-code-snowsight-ga |
| Snowflake-managed MCP server | Analyst·Search·Agents·SQL·커스텀 도구를 MCP로 외부 에이전트(Claude, Cursor 등)에 노출 | GA 2025-11-04 / Native App 내 MCP GA 2026-08-07 | L1 ●, GOV ◐ | https://docs.snowflake.com/release-notes/2025/other/2025-11-04-cortex-agents-mcp , https://docs.snowflake.com/en/release-notes/2026/other/2026-08-07-native-apps-agents-mcp-ga |
| Horizon Catalog 거버넌스 (Agent Identity, 데이터 보호 정책, 민감정보 분류) | 에이전트에 별도 신원을 부여하고, 마스킹·행 접근 정책을 외부 엔진까지 일관 적용 | Agent Identity GA 2026-06-02, Connected Audit Access 비공개 프리뷰 | GOV ● | https://investors.snowflake.com/news/news-details/2026/Snowflake-Advances-Trusted-AI-with-Snowflake-Horizon-Catalog-Centralizing-Governance-Context-and-Security-Across-the-Enterprise/default.aspx |
| AI Observability (TruLens 기반) | LLM 앱·에이전트의 트레이스 기록, LLM-as-judge 평가, 비교 | GA 2025-07-31 | OBS ● | https://docs.snowflake.com/release-notes/2025/other/2025-07-31-ai-observability-ga , https://docs.snowflake.com/user-guide/snowflake-cortex/ai-observability/evaluate-applications-trulens |

## 회사 전체 층 커버리지
- **L1 연결·원천 ●** — 관리형 MCP 서버(GA), Cortex Search, Horizon 메타데이터 커넥터(Preview), SAP·Salesforce 제로카피 연동.
- **L2 의미(지표) ●** — 핵심 강점. Semantic Views + Autopilot + Semantic Studio + Ossie(OSI) 표준 주도.
- **L3 관계·정체성 ◐** — 시맨틱 뷰 안의 테이블 관계(조인)만. 독립 온톨로지/지식그래프 제품은 공식 문서에서 확인 안 됨. Ossie에 "Ontology" 작업그룹이 있어 표준 차원에서만 진행.
- **L4 절차·역할 ◐** — CoWork 사용자 스킬(곧 프리뷰), CoCo 스킬. 3월 블로그가 말한 "operational playbook(지침)"을 위한 독립 제품은 아직 없음.
- **L5 기억·이력 ◐** — 컬럼 리니지·OpenLineage(계보) ●, 에이전트 메모리는 CoWork "곧 프리뷰". 결정·이벤트 기억 제품은 없음.
- **L6 런타임 창 관리 ●** — Cortex Agents 오케스트레이션, Cortex Sense의 신호 순위·조립, CoWork 멀티에이전트(곧 프리뷰).
- **L7 실행·검증 ◐** — SQL 생성·코드 실행(CoCo, CoWork Code Execution), MCP 커넥터 액션. 출력 검증/근거 확인 전용 기능은 약함.
- **GOV ●** — Horizon RBAC·마스킹, Agent Identity GA, MCP OAuth, Natoma 인수(대기).
- **OBS ●** — AI Observability GA, Cortex Agent evaluations GA, Cortex Sense 자기 평가.

## 2026년 주요 움직임 (최신순)
- **2026-08-18** Semantic View Autopilot의 Power BI 수집 GA.
- **2026-08-07** Native App 안에 Cortex Agent·MCP 서버를 담아 배포하는 기능 GA (컨텍스트를 Marketplace로 유통).
- **2026-07-08** Open Semantic Interchange(OSI)가 Apache Incubator에 들어가며 **Apache Ossie**로 개명 확인. 시맨틱 레이어 + 온톨로지 공통 스펙, 참여 조직 50곳 이상, Snowflake 엔지니어가 초기 커미터.
- **2026-06-30** Cortex Sense 공개 블로그: 사내 테스트에서 어려운 질문 정확도 24.1%→86.3%, 질의당 비용 $1.76→$0.59 주장(자체 벤치마크).
- **2026-06-02 (Summit 2026, 6/1–4)** Cortex Code→**CoCo**, Snowflake Intelligence→**CoWork** 개명. Horizon Context·Cortex Sense 공개, Semantic Studio·Advanced Semantics 비공개 프리뷰, Agent Identity GA, Cortex Agent Sharing·데이터 공유용 자동 생성 에이전트 공개 프리뷰.
- **2026-05-27** Natoma(엔터프라이즈 MCP 게이트웨이·신원 거버넌스) 인수 의향 발표 — 거래 종결 조건부.
- **2026-03-19** "Agent Context Layer" 관점 블로그(의미·정체성·플레이북·출처·결정 기억·권한 6요소) — 이후 제품 로드맵의 설계 문서 역할.
- **2026-03-13** Cortex Agent evaluations GA.
- **2026-03-09** Cortex Code Snowsight GA (CLI는 2월 GA).
- **2026-02-03** Semantic View Autopilot GA.

## 경쟁·파트너 관계
- **Databricks**: 정면 경쟁. Snowflake는 "사람이 승인하는 시맨틱 뷰 + 자동 초안", Databricks는 Genie Ontology로 "자동 추출 지식 + 인용"을 앞세움. 단, 양사 모두 Apache Ossie에 기여(Snowflake 블로그가 Databricks의 커밋을 언급).
- **Atlan·Collibra 등 카탈로그 벤더**: Horizon Context와 겹치면서도 파트너(Atlan은 자사 컨텍스트 층과 Horizon Context 연동 해설 다수 발행 — 이해관계 있는 2차 출처).
- **dbt Labs, Looker, Sigma, ThoughtSpot, Tableau, Power BI**: Autopilot 연동 대상이자 Ossie 동반자.
- **Anthropic·Cursor 등 외부 에이전트**: MCP로 시맨틱 뷰를 소비하는 쪽. Snowflake는 "외부 에이전트에도 같은 의미를 공급"을 차별점으로 내세움.
- **SAP·Salesforce·Workday·AVEVA·IBM**: 제로카피 통합 파트너(원천 확장).
- **AWS**: Summit 직전 5년 60억 달러 협약 보도(2차 출처, 미검증).

## 불확실·확인 못한 것
- **Cortex Sense 상태**: 공식 문서는 "Private Preview" 레퍼런스가 있으나, 2026-09 도쿄 행사 보고(Classmethod)는 "곧 비공개 프리뷰"라고 해 시점이 엇갈림. 정확도 수치는 Snowflake 내부 테스트뿐.
- **Horizon Context 자체의 GA 여부**: 보도자료에 상태 각주 없음. 구성요소별로만 상태가 다름(일부 문서가 LIMITEDACCESS 경로).
- **CoWork 메모리·스킬·멀티에이전트**: 2026-06 시점 "곧 공개 프리뷰" — 이후 실제 프리뷰 개시일 미확인.
- **Cortex Analyst·Cortex Search GA 일자**: 이번 조사에서 공식 릴리스 노트로 재확인하지 못함(GA 상태 자체는 MCP 문서에서 도구로 사용 중임으로 간접 확인).
- **Cortex AISQL GA**: TechTarget(2차)만 2025-11 GA 보도. 공식 릴리스 노트 미확인 → 목록에서 제외.
- **Natoma 인수 종결 여부·가격** 미확인.
- **L3 온톨로지**: Snowflake 자체 온톨로지 제품은 확인 못 함. Ossie Ontology WG 외에는 근거 없음.

## 데이터 블록
```yaml
vendor: snowflake
name: Snowflake
category: data_platform
products:
  - id: snowflake-semantic-views
    name: Semantic Views
    status: GA
    status_date: 2025-08
    layers: {L2: ●, GOV: ◐}
    x: -2
    y: -2
    xy_reason: "지표·차원 정의로 숫자 질문에 답하고, 사람이 직접 작성·검토하는 객체"
    maturity: 1
    evidence:
      - {url: https://docs.snowflake.com/release-notes/2025/9_25, kind: official, date: 2025-08-26}
      - {url: https://docs.snowflake.com/release-notes/2025/other/2025-11-04-sharing-semantic-views, kind: official, date: 2025-11-04}
  - id: snowflake-semantic-view-autopilot
    name: Semantic View Autopilot
    status: GA
    status_date: 2026-02
    layers: {L2: ●, L5: ◐}
    x: -2
    y: 0
    xy_reason: "지표 정의 생성 도구. AI가 기존 SQL·BI 파일·쿼리 이력으로 초안을 만들고 사람이 확정"
    maturity: 1
    evidence:
      - {url: https://www.snowflake.com/en/news/press-releases/snowflake-delivers-semantic-view-autopilot-as-the-foundation-for-trusted-scalable-enterprise-ready-AI/, kind: official, date: 2026-02-03}
      - {url: https://docs.snowflake.com/release-notes/2026/other/2026-08-18-semantic-views-power-bi-ingestion-ga, kind: official, date: 2026-08-18}
  - id: snowflake-horizon-context
    name: Horizon Context (Semantic Studio, metadata connectors, lineage)
    status: announced
    status_date: 2026-06
    layers: {L1: ◐, L2: ●, L5: ●, GOV: ●}
    x: -1
    y: -1
    xy_reason: "분석용 의미·메타데이터·계보 중심. 사람이 Studio로 큐레이션하되 커넥터·리니지는 자동 수집"
    maturity: 1
    evidence:
      - {url: https://www.snowflake.com/en/blog/horizon-context-governed-context/, kind: official, date: 2026-06-02}
      - {url: https://docs.snowflake.com/en/user-guide/snowflake-horizon/horizon-context, kind: official, date: 2026-11-11}
  - id: snowflake-cortex-sense
    name: Cortex Sense
    status: preview
    status_date: 2026-07
    layers: {L2: ◐, L5: ◐, L6: ●, OBS: ◐}
    x: -1
    y: 1
    xy_reason: "여전히 데이터 질문용이지만, 쿼리 이력·BI 지표에서 맥락을 자동 학습하고 충돌만 사람이 해소"
    maturity: 5
    evidence:
      - {url: https://www.snowflake.com/en/blog/enterprise-ai-agents-grounded-context/, kind: official, date: 2026-06-30}
      - {url: https://docs.snowflake.com/LIMITEDACCESS/cortex-sense-reference, kind: official, date: 2026-11-11}
  - id: snowflake-cortex-analyst
    name: Cortex Analyst
    status: GA
    status_date: null  # GA 일자 미확인
    layers: {L2: ◐, L7: ◐}
    x: -2
    y: -1
    xy_reason: "시맨틱 뷰 기반 text-to-SQL로 숫자 질문 전용, 맥락은 사전 정의된 뷰에 의존"
    maturity: 1
    evidence:
      - {url: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp, kind: official, date: 2026-11-11}
  - id: snowflake-cortex-search
    name: Cortex Search
    status: GA
    status_date: null  # GA 일자 미확인
    layers: {L1: ●, L6: ◐}
    x: -1
    y: 0
    xy_reason: "문서 검색 인덱스. 인덱스 대상은 사람이 정하고 질의 시 런타임 검색"
    maturity: 1
    evidence:
      - {url: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp, kind: official, date: 2026-11-11}
  - id: snowflake-cortex-agents
    name: Cortex Agents (evaluations, Agent Sharing)
    status: GA
    status_date: 2025-11
    layers: {L6: ●, L7: ◐, GOV: ◐, OBS: ●}
    x: 0
    y: 0
    xy_reason: "분석 도구와 커스텀 도구를 런타임에 고르는 오케스트레이터. 도구 목록은 사람이 구성"
    maturity: 2
    evidence:
      - {url: https://docs.snowflake.com/release-notes/2025/other/2025-11-04-cortex-agents, kind: official, date: 2025-11-04}
      - {url: https://docs.snowflake.com/release-notes/2026/other/2026-03-13-cortex-agent-evaluations, kind: official, date: 2026-03-13}
      - {url: https://investors.snowflake.com/news/news-details/2026/Snowflake-Pioneers-New-Open-Framework-for-Interoperable-Enterprise-Data-and-AI/default.aspx, kind: official, date: 2026-06-02}
  - id: snowflake-cowork
    name: Snowflake CoWork (formerly Snowflake Intelligence)
    status: GA
    status_date: 2026-06
    layers: {L4: ◐, L5: ◐, L6: ●, L7: ◐, GOV: ◐}
    x: 1
    y: 1
    xy_reason: "분석 답변에서 업무 자동화·커넥터 액션으로 이동 중, 메모리·스킬로 런타임 축적(프리뷰 예정)"
    maturity: 3
    evidence:
      - {url: https://snowflake.com/en/blog/snowflake-cowork-personal-work-agent/, kind: official, date: 2026-06-02}
      - {url: https://www.cio.com/article/4179715/snowflake-recasts-its-ai-strategy-around-action-not-answers-with-cowork.html, kind: secondary, date: 2026-06-02}
  - id: snowflake-coco
    name: Snowflake CoCo (formerly Cortex Code)
    status: GA
    status_date: 2026-03
    layers: {L4: ◐, L6: ●, L7: ●}
    x: 1
    y: 1
    xy_reason: "코드·파이프라인을 실제로 쓰는 에이전트, 필요한 시맨틱 뷰를 스스로 검색"
    maturity: 2
    evidence:
      - {url: https://docs.snowflake.com/en/release-notes/2026/other/2026-03-09-cortex-code-snowsight-ga, kind: official, date: 2026-03-09}
      - {url: https://snowflake.com/en/blog/snowflake-coco-ai-coding-agent-modern-data-stack/, kind: official, date: 2026-06-02}
  - id: snowflake-managed-mcp
    name: Snowflake-managed MCP server
    status: GA
    status_date: 2025-11
    layers: {L1: ●, GOV: ◐}
    x: -1
    y: -1
    xy_reason: "주로 분석 도구(Analyst·Search)를 노출하는 전송 계층, 노출 도구는 관리자가 지정"
    maturity: 2
    evidence:
      - {url: https://docs.snowflake.com/release-notes/2025/other/2025-11-04-cortex-agents-mcp, kind: official, date: 2025-11-04}
      - {url: https://docs.snowflake.com/en/release-notes/2026/other/2026-08-07-native-apps-agents-mcp-ga, kind: official, date: 2026-08-07}
  - id: snowflake-horizon-governance
    name: Horizon Catalog governance (Agent Identity, data protection policies)
    status: GA
    status_date: 2026-06
    layers: {GOV: ●}
    x: 0
    y: -2
    xy_reason: "데이터·에이전트 공통 권한 기반. 정책은 사람이 사전 정의"
    maturity: 2
    evidence:
      - {url: https://investors.snowflake.com/news/news-details/2026/Snowflake-Advances-Trusted-AI-with-Snowflake-Horizon-Catalog-Centralizing-Governance-Context-and-Security-Across-the-Enterprise/default.aspx, kind: official, date: 2026-06-02}
      - {url: https://www.businesswire.com/news/home/20260527677399/en/snowflake-announces-intent-to-acquire-natoma-providing-secure-connectivity-for-the-agentic-enterprise/, kind: official, date: 2026-05-27}
  - id: snowflake-ai-observability
    name: AI Observability (TruLens)
    status: GA
    status_date: 2025-07
    layers: {OBS: ●}
    x: 0
    y: 0
    xy_reason: "용도 중립 평가·트레이싱 도구"
    maturity: 4
    evidence:
      - {url: https://docs.snowflake.com/release-notes/2025/other/2025-07-31-ai-observability-ga, kind: official, date: 2025-07-31}
      - {url: https://docs.snowflake.com/user-guide/snowflake-cortex/ai-observability/evaluate-applications-trulens, kind: official, date: 2026-11-11}
notes:
  standard: "Apache Ossie (incubating, 구 Open Semantic Interchange) — Snowflake 창립·커미터 주도, 시맨틱 레이어+온톨로지 YAML 스펙. https://snowflake.com/en/blog/apache-ossie-open-semantic-interchange-incubator (2026-07-08)"
  acquisition: "Natoma(MCP 게이트웨이) 인수 의향 2026-05-27, 종결 미확인"
```

## 참고자료 (References)
- Snowflake Summit 2026 보도자료(2026-06-02): https://investors.snowflake.com/news/news-details/2026/Snowflake-Pioneers-New-Open-Framework-for-Interoperable-Enterprise-Data-and-AI/default.aspx
- Constellation Research Summit 2026 분석(2차): https://www.constellationr.com/index%2ephp/research/blog/snowflake-summit-2026-redrawing-boundary-between-data-context-and-action
- Apache Ossie 공식: https://ossie.apache.org/updates/ossie-enters-apache-incubator/
- Atlan Summit 2026 정리(2차, 이해관계 있음): https://atlan.com/know/snowflake/summit-2026-announcements/
