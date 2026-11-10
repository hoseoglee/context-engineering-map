# Google Cloud — 컨텍스트 엔지니어링 관련 솔루션 (조사일 2026-11-11)

## 한 줄 요약 (이 회사의 전략)
Google은 2026년 4월 Next '26에서 데이터 플랫폼을 "Agentic Data Cloud", Vertex AI를 "Gemini Enterprise Agent Platform"으로 다시 묶었다. 핵심은 **Knowledge Catalog(구 Dataplex Universal Catalog)를 회사 전체의 "컨텍스트 그래프"로 키우고**, 그 위에 Looker 시맨틱 레이어(지표), BigQuery/Spanner 그래프(관계), Memory Bank(기억), Agent Gateway·Registry·Identity(거버넌스)를 얹어 **데이터에서 에이전트 실행까지 한 회사 안에서 수직으로 잇는 것**이다. 10월에는 에이전트 대화 기록을 보고 컨텍스트를 스스로 고쳐 제안하는 "self-learning enrichment"(프리뷰)를 내놓아 폐루프(L5)까지 손을 뻗었다. 표준 쪽에서는 A2A(리눅스재단 이관, v1.0)와 Open Knowledge Format(OKF)을 밀어 개방성도 챙긴다.

## 솔루션 목록
| 제품 | 무엇을 하나(쉬운 말) | 상태(날짜) | 층 | 근거 URL |
|---|---|---|---|---|
| Knowledge Catalog (구 Dataplex Universal Catalog) | 회사의 표·문서·코드·위키를 한 그래프로 묶고, 용어 정의·조인 관계·모범 쿼리를 붙여 에이전트가 찾아 쓰게 함. 대화 기록을 분석해 빠진 정의를 자동 제안(신뢰도 기준 이상은 자동 반영, 이하는 담당자 승인) | 이름 변경 2026-04-10, 카탈로그 자체는 기존 GA / self-learning enrichment·Knowledge Studio는 Preview(2026-10-23) | L1◐ L2● L3● L4◐ L5◐ L6◐ GOV● OBS◐ | https://cloud.google.com/blog/products/data-analytics/knowledge-catalog-self-learning-context-enrichment-for-ai-agents , https://docs.cloud.google.com/dataplex/docs/transition-dataplex-universal-catalog |
| Open Knowledge Format (OKF) | 지식·메타데이터를 "마크다운 파일 폴더 + frontmatter" 묶음으로 표현하는 공개 규격. Knowledge Catalog의 context set을 이 형식으로 가져오고 내보냄 | 공개 규격 v0.1(2026-06), v0.2에서 출처·신뢰 필드 추가(2026-07, 2차 보도) | L2◐ L4◐ L5◐ | https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing |
| Looker 시맨틱 레이어 (LookML) + Looker MCP | 지표·차원을 LookML로 한 번 정의해 대화형 분석·대시보드 에이전트·외부 MCP 클라이언트가 같은 정의로 답하게 함 | LookML GA / 관리형 MCP 서버 Preview / LookML 에이전트(VS Code) Preview / Knowledge Catalog 연동 Preview (2026-04-23) | L1◐ L2● L7◐ GOV● | https://cloud.google.com/blog/products/business-intelligence/looker-updates-for-agentic-bi-at-next26 , https://docs.cloud.google.com/looker/docs/2608/mcp |
| Conversational Analytics (BigQuery·Looker) + Conversational Analytics API (데이터 에이전트) | 자연어 질문을 SQL로 바꿔 답하는 데이터 에이전트. Knowledge Catalog·검증 쿼리(golden query)·사용자 지침으로 근거를 잡고, 결과를 Gemini Enterprise나 자체 앱에 게시 | BigQuery CA·API GA(2026-07-29), Looker CA GA, DB용 CA Preview | L2◐ L3◐ L6◐ L7● GOV● | https://cloud.google.com/blog/products/data-analytics/conversational-analytics-in-google-data-cloud-in-q326 |
| BigQuery Graph / Spanner Graph | 엔터티·관계·비즈니스 규칙을 그래프로 모델링해 에이전트가 여러 단계를 건너 추론(GraphRAG). BigQuery와 Spanner 그래프를 데이터 이동 없이 연합 질의 | Spanner Graph GA(기존), BigQuery Graph 기능 다수 Preview(2026-04) | L1◐ L3● | https://cloud.google.com/blog/products/databases/unify-analytical-and-operational-data-for-ai , https://docs.cloud.google.com/spanner/docs/graph/overview |
| Gemini Enterprise Agent Platform (구 Vertex AI Agent Builder/Agent Engine) — Agent Runtime·ADK·Agent Studio·Evaluation·Observability·Optimizer | 에이전트를 만들고(코드 ADK/로우코드 Studio) 며칠짜리 장기 실행·샌드박스 실행을 돌리고, 추적·평가·실패 묶음 분석으로 지시문 개선안을 받음 | 플랫폼 발표 2026-04-23, Runtime 등 GA 2026-07-30, Observability GA 2026-06-18 | L4◐ L6● L7● OBS● | https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform , https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform |
| Memory Bank + Sessions | 대화 이력을 세션으로 저장하고, 대화에서 장기 기억을 자동 추출·정리해 다음 대화에 불러옴. 2026년 memory profile(구조화 스키마), 이벤트 스트리밍 수집(IngestEvents) 추가 | Sessions·Memory Bank GA(2025-12-17, 2차 확인), memory profiles GA(2026-07-15), IngestEvents GA(2026-07-09) | L5● L6◐ | https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes , https://docs.cloud.google.com/agent-builder/agent-engine/memory-bank/overview |
| Agent Identity·Agent Registry·Agent Gateway + Model Armor | 에이전트마다 고유 ID, 에이전트·도구·MCP 서버 목록 등록, 에이전트↔도구↔에이전트 통신을 게이트웨이에서 정책·프롬프트 인젝션 방어(Model Armor)로 통제 | Gateway·Registry GA(2026-06-18, A2A 1.0 지원 포함), Model Armor on Gateway GA(2026-06-24), Identity API Preview(2026-06-18)→GA 발표(2026-07-30) | L1◐ L7● GOV● OBS◐ | https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes , https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform |
| Vertex AI Search / RAG Engine | 문서·웹·사내 데이터를 색인해 검색·랭킹 후 모델에 근거로 넣는 관리형 검색·RAG | GA(기존). Agent Platform 아래로 편입, "Agent Search" 개명설은 미확인 | L1● L6● GOV◐ | https://docs.cloud.google.com/architecture/rag-genai-agentspace-vertexai |
| Gemini Enterprise (구 Agentspace) | 직원용 에이전트 작업공간. 검증된 커넥터+BYO-MCP, 사람·에이전트가 공유 컨텍스트를 쌓는 Projects, 필요할 때만 로드되는 팀 Skills, 단계별 사람 승인 체크포인트가 있는 Agent Designer | 다수 기능 발표·순차 롤아웃(2026-04-23) | L1● L4● L5◐ L6◐ L7◐ GOV● | https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise |
| MCP Toolbox for Databases + Google 관리형 MCP 서버 | DB 질의를 에이전트 도구로 노출하는 오픈소스 MCP 서버(40+ DB) 및 Google이 운영하는 원격 MCP 서버 | Toolbox 1.0(2026-04), 관리형 MCP: AlloyDB·Bigtable·Cloud SQL·Firestore·Spanner GA, 일부 Preview(2026-04-23) | L1● L7◐ GOV◐ | https://cloud.google.com/blog/products/databases/whats-new-for-google-cloud-databases-at-next26 |
| Agent2Agent (A2A) 프로토콜 | 서로 다른 회사의 에이전트가 작업을 주고받는 통신 규격. 서명된 Agent Card, 다중 바인딩 | 리눅스재단 이관(2025-06), v1.0(2026-03, 2차) / Agent Registry에서 A2A 1.0 GA 지원(2026-06-18) | L1● GOV◐ | https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes , https://opensource.googleblog.com/search/label/A2April |

## 회사 전체 층 커버리지
- **L1 연결·원천 ●**: 관리형 MCP 서버(DB·Looker·SecOps), MCP Toolbox 1.0, A2A, Vertex AI Search, Gemini Enterprise 커넥터, Smart Storage Object Context API(파일 적재 시 자동 태깅).
- **L2 의미 ●**: LookML(가장 성숙), Knowledge Catalog의 비즈니스 정의·글로서리·golden query.
- **L3 관계 ●**: Knowledge Catalog 컨텍스트 그래프, BigQuery Graph·Spanner Graph와 그래프 연합.
- **L4 절차 ◐**: Gemini Enterprise Skills·Agent Designer, ADK. Knowledge Catalog가 플레이북 문서에서 "에이전트 지시문"을 뽑아 제안. 업무 절차를 정식 모델로 다루는 기능은 약함.
- **L5 기억 ●**: Memory Bank·Sessions(GA), Gemini Enterprise Projects, Knowledge Catalog 변경 이력·출처 기록.
- **L6 런타임 창 ◐~●**: Agent Runtime·ADK 멀티에이전트, context set(에이전트별 컨텍스트 범위 지정), Vertex AI Search 랭킹. 토큰 예산·압축 제품은 별도로 확인 못함.
- **L7 실행·검증 ●**: Agent Sandbox, CA의 SQL 실행, Model Armor 출력·입력 검사.
- **GOV ●**: Agent Identity·Registry·Gateway, IAM Unified Access Policies(GA 2026-08-31), context set IAM, VPC-SC.
- **OBS ●**: Agent Observability(GA), Evaluation·Simulation, Gateway Cloud Trace(Preview).

## 2026년 주요 움직임 (최신순)
- 2026-11-06: Memory Bank 전용 콘솔 페이지(기억 조회·설정) 추가 (release notes).
- 2026-10-23: Knowledge Catalog self-learning context enrichment·Knowledge Studio Preview. 에이전트 trace를 분석해 정의·조인·지시문을 출처·신뢰도와 함께 제안, 임계값 이상 자동 반영. 내부 벤치 "정확도 약 4배, 토큰 최대 75% 절감"(벤더 수치).
- 2026-09-30: Agent Registry App Topology API GA, Gateway Cloud Trace Preview.
- 2026-08-31: IAM Unified Access Policies GA(Agent Gateway 접근 제어 기반).
- 2026-07-30: Agent Runtime·Memory Bank·Agent Identity 등 "모두에게 제공(GA)" 발표.
- 2026-07-29: BigQuery Conversational Analytics 및 API GA.
- 2026-07: OKF v0.2(출처·신뢰 필드) — 2차 보도.
- 2026-06-18~24: Agent Gateway·Agent Registry(A2A 1.0·MCP 서버 카탈로그)·Agent Observability GA, Model Armor on Gateway GA.
- 2026-06-12(2차 보도): Open Knowledge Format v0.1 공개.
- 2026-04-22~23 (Next '26): Vertex AI → Gemini Enterprise Agent Platform, 데이터 플랫폼 → Agentic Data Cloud, Dataplex → Knowledge Catalog, Looker 관리형 MCP·Dashboard Agents, MCP Toolbox 1.0, 관리형 DB MCP GA, BigQuery Graph·그래프 연합, Workspace Intelligence(Workspace 전반의 시맨틱 레이어) 발표.
- 2026-04-10: Dataplex Universal Catalog → Knowledge Catalog 이름 변경(API·IAM 이름 유지).
- 2026-03 (2차): A2A v1.0 안정판.

## 경쟁·파트너 관계
- **경쟁**: Knowledge Catalog는 Snowflake(Horizon/semantic views), Databricks(Unity Catalog·metric views), AWS Context, Microsoft(Fabric IQ 계열)와 "에이전트용 컨텍스트 레이어" 자리를 다툰다. Looker는 dbt·Cube·AtScale 등 시맨틱 레이어와 경쟁. Memory Bank는 AWS AgentCore Memory, Mem0·Zep 등과 겹친다.
- **파트너/개방**: Model Garden에서 Anthropic Claude 제공, Agent Marketplace에 Accenture·Oracle·ServiceNow 에이전트, Gemini Enterprise가 Microsoft 365 권한을 존중하는 커넥터 제공. A2A는 AWS·Microsoft·Salesforce·SAP·ServiceNow 등과 리눅스재단에서 공동 운영. Cross-Cloud Lakehouse(Iceberg)로 AWS·Azure 데이터를 복사 없이 질의.

## 불확실·확인 못한 것
- Knowledge Catalog "제품 자체"의 GA/Preview 표기가 문서마다 다름(DB 블로그는 Preview로 표기, 카탈로그 기능은 Dataplex 시절부터 GA). self-learning enrichment는 확실히 Preview.
- Memory Bank GA 시점(2025-12-17)은 검색 스니펫으로만 확인, 원문 미열람.
- "BigQuery knowledge engine"이라는 공식 명칭은 찾지 못함. 가장 가까운 것은 Conversational Analytics + Knowledge Catalog + BigQuery Graph 조합.
- Vertex AI Search의 "Agent Search" 개명, RAG Engine의 2026년 상태는 공식 근거 없음.
- OKF 날짜·v0.2 내용, A2A v1.0 날짜는 2차 출처 위주.
- Agent Evaluation·Agent Simulation·Agent Optimizer의 GA 여부 미확인.
- Gemini Enterprise Projects·Skills·Agent Designer의 롤아웃 완료 여부 미확인.

## 데이터 블록
> evidence의 date는 원문 게시일. 게시일을 못 찾은 문서 페이지는 열람일(2026-11-11)로 적었다.

```yaml
vendor: google
name: Google Cloud
category: hyperscaler
products:
  - id: google-knowledge-catalog
    name: Knowledge Catalog (구 Dataplex Universal Catalog)
    status: GA
    status_date: 2026-04
    layers: {L1: ◐, L2: ●, L3: ●, L4: ◐, L5: ◐, L6: ◐, GOV: ●, OBS: ◐}
    x: -1
    y: 1
    xy_reason: "정의·조인·지표 같은 분석 컨텍스트 중심이지만, 에이전트 trace에서 정의를 스스로 찾아 제안·자동 반영(임계값)하므로 런타임 축적 쪽"
    maturity: 5
    notes: "maturity 5는 self-learning enrichment(Preview, 2026-10) 기준"
    evidence:
      - {url: https://cloud.google.com/blog/products/data-analytics/knowledge-catalog-self-learning-context-enrichment-for-ai-agents, kind: official, date: 2026-10-23}
      - {url: https://docs.cloud.google.com/dataplex/docs/transition-dataplex-universal-catalog, kind: official, date: 2026-04-10}
      - {url: https://cloud.google.com/blog/products/data-analytics/whats-new-in-the-agentic-data-cloud, kind: official, date: 2026-04-23}
  - id: google-okf
    name: Open Knowledge Format (OKF)
    status: announced
    status_date: 2026-06
    layers: {L2: ◐, L4: ◐, L5: ◐}
    x: -1
    y: -2
    xy_reason: "사람이 작성·검토하는 마크다운 지식 묶음의 이식 규격"
    maturity: 1
    evidence:
      - {url: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing, kind: official, date: 2026-06-12}
      - {url: https://www.implicator.ai/google-open-sources-a-knowledge-format-and-wires-it-into-its-catalog/, kind: secondary, date: 2026-06-12}
  - id: google-looker-semantic
    name: Looker 시맨틱 레이어 (LookML) + Looker MCP
    status: GA
    status_date: 2026-04
    layers: {L1: ◐, L2: ●, L7: ◐, GOV: ●}
    x: -2
    y: -2
    xy_reason: "숫자 질문용 지표 정의를 사람이 LookML로 미리 큐레이션. MCP 서버는 Preview"
    maturity: 2
    evidence:
      - {url: https://cloud.google.com/blog/products/business-intelligence/looker-updates-for-agentic-bi-at-next26, kind: official, date: 2026-04-23}
      - {url: https://docs.cloud.google.com/looker/docs/2608/mcp, kind: official, date: 2026-11-11}
  - id: google-conversational-analytics
    name: Conversational Analytics (BigQuery/Looker) + CA API
    status: GA
    status_date: 2026-07
    layers: {L2: ◐, L3: ◐, L6: ◐, L7: ●, GOV: ●}
    x: -2
    y: -1
    xy_reason: "자연어→SQL 데이터 에이전트. golden query·지침 등 큐레이션된 근거를 주로 씀"
    maturity: 2
    evidence:
      - {url: https://cloud.google.com/blog/products/data-analytics/conversational-analytics-in-google-data-cloud-in-q326, kind: official, date: 2026-07-29}
  - id: google-bigquery-spanner-graph
    name: BigQuery Graph / Spanner Graph
    status: preview
    status_date: 2026-04
    layers: {L1: ◐, L3: ●}
    x: -1
    y: -2
    xy_reason: "사람이 엔터티·관계를 모델링하는 그래프 DB. 분석·운영 데이터 모두. Spanner Graph는 GA, BigQuery Graph 다수 기능 Preview"
    maturity: 1
    evidence:
      - {url: https://cloud.google.com/blog/products/databases/unify-analytical-and-operational-data-for-ai, kind: official, date: 2026-04-22}
      - {url: https://docs.cloud.google.com/spanner/docs/graph/overview, kind: official, date: 2026-11-11}
  - id: google-agent-platform
    name: Gemini Enterprise Agent Platform (Agent Runtime·ADK·Studio·Evaluation·Observability)
    status: GA
    status_date: 2026-07
    layers: {L4: ◐, L6: ●, L7: ●, OBS: ●}
    x: 1
    y: 1
    xy_reason: "장기 실행 에이전트와 도구 실행이 중심. Optimizer가 실패를 묶어 지시문 개선을 제안"
    maturity: 4
    evidence:
      - {url: https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform, kind: official, date: 2026-04-23}
      - {url: https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform, kind: official, date: 2026-07-30}
  - id: google-memory-bank
    name: Memory Bank + Sessions
    status: GA
    status_date: 2025-12
    layers: {L5: ●, L6: ◐}
    x: 1
    y: 2
    xy_reason: "대화에서 에이전트가 기억을 자동 생성·갱신"
    maturity: 5
    evidence:
      - {url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes, kind: official, date: 2026-11-06}
      - {url: https://docs.cloud.google.com/agent-builder/agent-engine/memory-bank/overview, kind: official, date: 2026-11-11}
      - {url: https://docs.cloud.google.com/agent-builder/release-notes, kind: official, date: 2025-12-17}
  - id: google-agent-governance
    name: Agent Identity / Agent Registry / Agent Gateway + Model Armor
    status: GA
    status_date: 2026-06
    layers: {L1: ◐, L7: ●, GOV: ●, OBS: ◐}
    x: 1
    y: -1
    xy_reason: "에이전트 행동·도구 호출 통제. 정책은 관리자가 사전 정의"
    maturity: 4
    evidence:
      - {url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes, kind: official, date: 2026-06-24}
      - {url: https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform, kind: official, date: 2026-07-30}
  - id: google-vertex-search-rag
    name: Vertex AI Search / RAG Engine
    status: GA
    status_date: null
    layers: {L1: ●, L6: ●, GOV: ◐}
    x: 0
    y: 0
    xy_reason: "문서 색인은 사전 구성, 질의별 검색·랭킹은 런타임"
    maturity: 1
    notes: "기존 GA 제품이나 GA 월은 미확인이라 비움"
    evidence:
      - {url: https://docs.cloud.google.com/architecture/rag-genai-agentspace-vertexai, kind: official, date: 2026-11-11}
  - id: google-gemini-enterprise
    name: Gemini Enterprise (구 Agentspace)
    status: announced
    status_date: 2026-04
    layers: {L1: ●, L4: ●, L5: ◐, L6: ◐, L7: ◐, GOV: ●}
    x: 1
    y: 0
    xy_reason: "업무 실행형 직원 에이전트. Skills·Agent Designer는 사람이 정의, Projects는 사용 중 컨텍스트 축적"
    maturity: 3
    evidence:
      - {url: https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise, kind: official, date: 2026-04-23}
  - id: google-mcp-toolbox
    name: MCP Toolbox for Databases + 관리형 MCP 서버
    status: GA
    status_date: 2026-04
    layers: {L1: ●, L7: ◐, GOV: ◐}
    x: 0
    y: -1
    xy_reason: "DB 읽기·쓰기를 도구로 노출. 도구는 설정 파일로 사전 정의"
    maturity: 2
    evidence:
      - {url: https://cloud.google.com/blog/products/databases/whats-new-for-google-cloud-databases-at-next26, kind: official, date: 2026-04-23}
  - id: google-a2a
    name: Agent2Agent (A2A) 프로토콜
    status: GA
    status_date: 2026-03
    layers: {L1: ●, GOV: ◐}
    x: 1
    y: 0
    xy_reason: "에이전트 간 작업 위임 전송 규격, 컨텍스트 내용 자체에는 중립"
    maturity: 1
    evidence:
      - {url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes, kind: official, date: 2026-06-18}
      - {url: https://opensource.googleblog.com/search/label/A2April, kind: secondary, date: 2026-11-11}
```
