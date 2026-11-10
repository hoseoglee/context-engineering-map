# 기타 데이터 측 벤더 — AI 에이전트용 기업 데이터 컨텍스트 (조사일 2026-11-11)

> 범위: Palantir·Snowflake·Databricks·Microsoft·Google·AWS를 **제외한** 회사 중, 기업 데이터 쪽에서 에이전트에 컨텍스트를 공급하는 곳(기업 앱, 시맨틱 레이어, 카탈로그·컨텍스트 플랫폼, 지식그래프).
> 근거는 공식 보도자료·문서·블로그를 1순위로 썼고, 2차 자료만 있으면 `secondary`로 표시했다. 조사 방법: 웹 검색 20회, 페이지 직접 확인 16회(그중 1회 403).

## 선정 회사 (13곳)

| 회사 | 카테고리 | 왜 관련 있나 |
|---|---|---|
| Salesforce (+Informatica, MuleSoft, Tableau) | enterprise_app | CRM 데이터(Data 360)·시맨틱(Tableau)·데이터 관리(Informatica)·에이전트 연결(MuleSoft)을 한 회사가 묶어 "에이전트용 컨텍스트"로 판매 |
| SAP | enterprise_app | ERP 업무 객체·프로세스를 Knowledge Graph·Ontology Manager로 에이전트(Joule)에 제공 |
| ServiceNow | enterprise_app | CMDB·워크플로우 이력을 Context Engine으로 묶고, data.world 인수로 카탈로그·용어집 확보 |
| Oracle | data_platform | DB 안에서 에이전트 실행(Select AI Agent)·DB별 MCP 서버, Fusion 앱 에이전트 스튜디오 |
| IBM | data_platform | watsonx.data(+Confluent 실시간 스트림)로 에이전트 데이터, watsonx Orchestrate로 에이전트·MCP 통제 |
| Fivetran + dbt Labs | semantic_catalog | 지표 정의(dbt Semantic Layer)와 계보를 MCP로 에이전트에 노출, 수집~변환을 한 회사로 통합 |
| Cube | semantic_catalog | 독립 시맨틱 레이어 위에서 분석 에이전트가 동작하는 구조 |
| AtScale | semantic_catalog | 오픈 시맨틱 모델 언어(SML)와 MCP 서버로 여러 클라우드 에이전트에 지표 제공 |
| Atlan | semantic_catalog | 스스로 "컨텍스트 레이어"를 표방, 컨텍스트를 만들고·시험하고·배포하는 수명주기 도구 |
| Collibra | semantic_catalog | 거버넌스 카탈로그 → AI 에이전트 통제면(AI Command Center), MCP 서버 |
| Alation | semantic_catalog | 카탈로그+컨텍스트+에이전트를 묶은 AIOS, 에이전트 SDK/MCP |
| DataHub (Acryl) | semantic_catalog | 오픈소스 메타데이터 그래프를 "컨텍스트 플랫폼"으로 재포지셔닝, MCP·Agent Context Kit |
| Neo4j | knowledge_graph | GraphRAG·Aura Agent·Context Engine(온톨로지+에이전트 기억) |

**제외/흡수 처리**: Informatica는 2025-11 Salesforce에 인수 완료 → Salesforce 항목에 포함. data.world는 ServiceNow 인수 → ServiceNow 항목에 포함. Stardog(Voicebox, MCP 베타)·TigerGraph·Teradata(Enterprise Vector Store, 2026-04 GA)는 관련은 있으나 2026년 공식 근거가 얇거나 영향력이 상대적으로 작아 이번 묶음에서는 뺐다(아래 "기타 후보" 참고).

---

## 1. Salesforce (+Informatica, MuleSoft, Tableau)

**한 줄 요약**: CRM 고객 데이터(Data 360), 지표·의미(Tableau Semantics/Knowledge), 전사 데이터 관리(Informatica), 에이전트·MCP 연결 관리(MuleSoft Agent Fabric)를 모두 사들여 묶은 뒤, "요청마다 허용된 정보만 골라 주는" 컨텍스트 서비스로 Agentforce와 외부 에이전트에 판다.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Data 360 MCP Server | 외부 에이전트(ChatGPT·Claude 등)가 Data 360 API 약 200개를 MCP로 호출 — 조회뿐 아니라 세그먼트 생성 같은 작업도 | GA (Dreamforce 2026, 2차 자료) / 2026-05 개발자 프리뷰 기록과 상충 | L1, L7, GOV◐ | infotech.com Dreamforce 2026 노트 |
| Agent Context Engine | 정형 데이터+지식 문서를 섞어, 요청마다 그 에이전트에 허용된 정보만 골라 조립 | 발표, GA 예정 2026-12 (2차) | L6, GOV | infotech.com |
| Data 360 Agent Memory / Salesforce Catalog | 에이전트 간 공유 기억 / 필드 의미·객체 관계·권한을 쉬운 말로 보여주는 카탈로그 | Winter '27 릴리스 항목(상태 표기 없음) | L5, L2 | trailhead Winter '27 |
| Tableau Semantics + Tableau Knowledge | 지표·차원·관계를 관리하는 시맨틱 레이어 + 이를 연결 그래프로 자동 구성해 에이전트 컨텍스트로 제공 | Semantics GA / Knowledge는 Winter '27 항목 | L2, L3◐ | trailhead, isg-one |
| Informatica Headless (Managed MCP) | IDMC의 데이터 품질·통합·MDM 기능을 에이전트용 헤드리스 서비스로 노출 | GA(2026 봄, 2차) | L1, L3◐(MDM), GOV | trailhead, intelligentcio 2026-06-03 |
| MuleSoft Agent Fabric (Registry·Scanner·Kill Switch) | 사내 모든 에이전트·MCP 서버를 자동 발견·등록, 정책 위반 시 개별 에이전트 정지, 비용 한도 | GA (2025-09 출시, MCP URL 등록 GA 2026-01) | L1, L6◐, GOV, OBS◐ | salesforce.com news |

**층 커버리지**: L1● L2● L3◐ L4◐ L5◐ L6◐ L7● GOV● OBS◐

**2026 주요 움직임**
- 2026 가을(Dreamforce 2026): Data 360 MCP GA, Agent Context Engine 발표(GA 2026-12 예정), Tableau Knowledge 공개.
- 2026-06: Informatica가 자율 데이터 관리 에이전트와 MCP 기반 "헤드리스" 데이터 관리 발표.
- 2026-01~03: MuleSoft Agent Fabric 확장 — 클라우드별 Agent Scanner GA, MCP 서버 URL 등록.
- (참고) 2025-11-18: Informatica 인수 완료(약 80억 달러).

**불확실**: Data 360 MCP의 정확한 GA 시점(GA vs 개발자 프리뷰 기록 상충), Dreamforce 2026 정확한 일자, Tableau Knowledge의 GA 여부는 공식 릴리스 노트로 재확인 필요. Tableau 시맨틱이 Salesforce 밖에서도 열린 시맨틱 레이어가 될지 미지수(분석가 지적).

---

## 2. SAP

**한 줄 요약**: SAP 업무 객체·프로세스 지식을 지식그래프와 온톨로지로 정리해 "ERP를 아는 에이전트(Joule)"를 만들고, BTP·Business Data Cloud·AI를 하나의 Business AI Platform으로 합쳤다. 핵심 그래프 기능 상당수는 2027년 초 일정.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| SAP Business AI Platform (BDC+BTP+AI 통합) | 컨텍스트·빌드·거버넌스 3층으로 에이전트를 만들고 통제하는 통합 플랫폼 | 발표 2026-05 | L1, L2, GOV | news.sap.com 2026-05 |
| SAP Business Data Cloud | SAP·비SAP 데이터를 데이터 제품(data product)으로 묶어 의미를 보존한 채 제공, zero-copy 공유 | GA (2025 출시) | L1, L2 | news.sap.com |
| SAP Knowledge Graph | 고객 SAP 환경의 업무 엔티티·프로세스·관계를 구조화한 지도, Joule에 연결 | 일부 Joule 통합 / 확장 기능 2027-Q1 예정 | L3 | itbrief.co.uk, futurumgroup |
| Ontology Manager | 비즈니스 개념·관계·제약 규칙(SHACL)을 정의하고 데이터 제품에 매핑, 질의 전 검증 | 발표, 2027-Q1 예정 | L3, L7◐ | architecture.learning.sap.com, erp.today |
| Joule Studio / Joule Agents | 노코드·프로코드로 에이전트 구축, 70+ 모델 선택 | GA (커스텀 에이전트 런타임 2026-12까지 일부 무료) | L4, L6, L7 | itbrief.co.uk |
| Joule Work | 사용자가 Joule을 1차 창구로 쓰는 새 업무 화면, MCP·A2A 지원 | 발표 2026-05 | L6, L7 | siliconangle 2026-05-12 |

**층 커버리지**: L1● L2● L3◐ L4● L5 L6● L7● GOV● OBS◐

**2026 주요 움직임**
- 2026-10(TechEd 2026): Ontology Manager 등 2027년까지의 롤아웃 일정 제시(2차).
- 2026-05-12(Sapphire): Business AI Platform·Autonomous Suite 발표, 파트너 에이전트 펀드 1억 유로, Joule Work 공개.

**불확실**: Knowledge Graph·Ontology Manager·Enterprise AI Gateway 가격과 정확한 GA 시점 미공개. BARC는 지식그래프-BDC-BTP 통합 구조가 아직 개발 중이라고 평가. Ontology Manager가 Sapphire인지 TechEd 발표인지 자료 간 차이.

---

## 3. ServiceNow

**한 줄 요약**: IT·업무 워크플로우 이력(CMDB, 정책, 결정 이력)이라는 "행동 데이터"를 Context Engine으로 묶고, data.world(카탈로그·용어집·지식그래프)와 Pyramid Analytics를 사서 데이터 측 공백을 메웠다. 강점은 실행·통제(AI Control Tower).

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Context Engine | 사람·역할·자산·서비스·정책 관계를 실시간 매핑하고 CMDB·워크플로우·외부 데이터에 시맨틱 레이어 적용, 활동으로 계속 학습 | 발표 2026-04/05 (가용 시점 미기재) | L2, L3, L5 | ServiceNow 보도자료 2026-05-06 |
| Workflow Data Fabric | 전사 데이터를 복사 없이 워크플로우·에이전트에 연결, 자연어로 데이터 자산 생성 | GA | L1, L7 | 보도자료, servicenow docs |
| ServiceNow Data Catalog (구 data.world) | 자동 발견·계보·공유 비즈니스 용어집, 지식그래프 아키텍처 | GA | L2, L3, L5 | 보도자료, servicenow docs |
| Autonomous Data Analytics | 사람·에이전트가 자연어로 전사 데이터를 질의 (Pyramid Analytics 기술) | 발표 2026-05 | L2◐, L6 | 보도자료 |
| MCP Registry + AI Control Tower/AI Gateway | 검증된 MCP 서버의 사내 카탈로그, 타사 AI까지 통제·관측 | MCP Registry: Innovation Lab(프리뷰), A2A Agent Card 연말 예정 | GOV, OBS | 보도자료 |
| Autonomous Data Governance | 데이터 품질·정책 위반을 상시 감시·집행 | 2026 하반기 예정 | GOV, OBS | 보도자료 |

**층 커버리지**: L1● L2● L3● L4● L5◐ L6● L7● GOV● OBS●

**2026 주요 움직임**
- 2026-05-06(Knowledge 2026): Context Engine·Autonomous Data Analytics·MCP Registry·RaptorDB Pro 발표.
- 2026-04-09: Context Engine 최초 공개(관련 보도자료).
- (참고) 2025-05: data.world 인수 발표 + Workflow Data Network(100+ 데이터 파트너).

**불확실**: Context Engine의 GA 여부·가격, Pyramid Analytics 인수 시점·조건은 확인하지 못함.

---

## 4. Oracle

**한 줄 요약**: "데이터가 있는 DB 안에서 에이전트를 돌린다" 전략. DB마다 MCP 서버를 붙이고 DB 권한(VPD)·감사 로그를 그대로 에이전트 통제에 재사용하며, 앱 쪽은 Fusion AI Agent Studio로 덮는다.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Oracle AI Database 26ai | 벡터 저장·유사도 검색·내장 RAG를 갖춘 DB | GA (2025-10) | L1 | infoworld(2차), oracle.com |
| Select AI / Select AI Agent | 자연어→SQL, RAG, DB 안에서 에이전트·도구·팀 정의 및 실행(DBMS_CLOUD_AI_AGENT) | GA (19.29+, 26ai 23.26+) | L1, L6, L7 | docs.oracle.com Select AI Agent |
| Autonomous AI Database MCP Server | DB별 관리형 MCP 엔드포인트, 커스텀 도구 노출, DB 역할·VPD·감사 로그 적용 | GA (문서 기준, 공개일 미표기) | L1, L7, GOV● | docs.oracle.com MCP |
| Fusion AI Agent Studio + Agent Marketplace | Fusion 앱(ERP·HCM) 업무용 에이전트 구축·파트너 에이전트 배포, 외부 LLM·MCP 지원 | GA/발표 2025-10-15 | L4, L7 | oracle.com 보도자료 2025-10-15 |
| Oracle AI Data Platform | 수집·시맨틱 보강·벡터 인덱싱·생성 AI 도구를 한 거버넌스 환경에 묶음 | 발표 2025-10 | L1, L2◐ | 2차(분석가 요약) |

**층 커버리지**: L1● L2◐ L3◐(그래프 기능은 확인 못함) L4◐ L5 L6◐ L7● GOV● OBS◐

**2026 주요 움직임**
- 2026: Autonomous AI Database MCP Server 문서화·공식 블로그 발표(정확한 일자 미확인), 19c까지 Select AI Agent 하위 지원.
- (참고) 2025-10 AI World: 26ai 발표, Fusion Agent Marketplace 개시.

**불확실**: MCP 서버의 정확한 GA 날짜, 2026 AI World(10월) 발표 내용은 이번 조사에서 확인하지 못함. 시맨틱 레이어 제품의 존재 여부 불명.

---

## 5. IBM

**한 줄 요약**: Confluent(약 110억 달러)를 사서 "실시간 이벤트 → watsonx.data(계보·정책 포함) → 에이전트" 경로를 만들고, watsonx Orchestrate를 타사 에이전트·모델·MCP 서버까지 관리하는 통제면으로 키우는 중.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| watsonx.data (+ intelligence) | 레이크하우스에 계보·정책·품질 통제를 얹어 에이전트용 데이터 제공 | GA | L1, L5◐, GOV | confluent.io 보도자료 2026-03-17 |
| Confluent (IBM) | 운영 이벤트를 실시간 스트리밍해 에이전트 컨텍스트를 계속 갱신 | 인수 완료 2026-03-17 | L1 | confluent.io |
| watsonx.data integration MCP server | 배치·스트리밍 파이프라인을 에이전트가 다루는 MCP 도구 | 1.0 (2026-06, 공개 프리뷰 2026-04) | L1, L7 | IBM community 2026-06-15 |
| Agentic Data Integration | 통합 엔진 위 자연어 계층, 외부 에이전트는 MCP로 접속 | 기술 프리뷰 2026-10 | L1, L7 | omdia 2026-10 |
| watsonx Orchestrate (+AI Gateway) | 에이전트 구축·조율, 타사 에이전트·모델·MCP 서버 발견·관리, 에이전트 카탈로그·트레이싱 | GA (Gateway 2026, 2차) | L4, L6, GOV, OBS | techstrong.ai, nand-research |
| Data Intelligence MCP server | 카탈로그·계보 등 데이터 인텔리전스를 MCP로 노출(오픈소스) | 공개(GitHub) | L1, L2◐, L5◐ | github.com/ibm/data-intelligence-mcp-server |

**층 커버리지**: L1● L2◐ L3 L4● L5◐ L6● L7● GOV● OBS●

**2026 주요 움직임**
- 2026-10: Agentic Data Integration 프리뷰.
- 2026-06: watsonx.data integration MCP 서버 1.0.
- 2026-05: Think 2026 — 스트리밍+배치 통합으로 에이전트에 상시 갱신 컨텍스트 제공 강조.
- 2026-03-17: Confluent 인수 완료.

**불확실**: Orchestrate AI Gateway의 GA 시점, Confluent 통합 제품 가격·패키징 미공개. watsonx.data + Confluent 결합 실사용 사례는 분석가도 확인 권고.

---

## 6. Fivetran + dbt Labs

**한 줄 요약**: 수집(Fivetran)과 변환·지표 정의(dbt)가 2026-06 한 회사가 됐고, "지표 정의+계보를 에이전트에 공급하는 데이터 레이어"를 내세운다. dbt MCP 서버와 오픈 표준 Agents Schema가 에이전트 접점.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| dbt Semantic Layer (MetricFlow) | 지표를 한 번 정의하면 모든 도구·에이전트가 같은 값으로 계산 | GA | L2 | docs.getdbt.com |
| dbt MCP server (로컬/원격) | 메타데이터·계보 탐색, 시맨틱 레이어 질의, text-to-SQL, (로컬) dbt 명령 실행 | 원격 GA(2차) / 문서에는 상태 표기 없음 | L1, L2, L5◐, L7◐ | docs.getdbt.com about-mcp |
| Agents Schema | 웨어하우스의 한 스키마를 에이전트 공용 컨텍스트로 지정(지표 정의·시맨틱 모델·계보를 SQL 테이블로) — 오픈 표준 | 발표 2026-06 | L2, L5 | techzine 2026-06-01 |
| dbt Fusion / Core v2.0 | 새 엔진 런타임, Apache 2.0 오픈소스 | 알파 | L2◐ | techzine |
| Fivetran 커넥터 | 수백 개 원천에서 데이터 수집 | GA | L1 | techtarget |

**층 커버리지**: L1● L2● L3 L4 L5◐ L6 L7◐ GOV◐ OBS◐

**2026 주요 움직임**
- 2026-06-01: 합병 완료(CEO George Fraser, 사장 Tristan Handy), Agents Schema·dbt State(프리뷰)·dbt Wizard(베타) 발표.

**불확실**: MCP 서버 GA 정확한 날짜, 시맨틱 레이어 오픈소스화 범위는 이번에 확인 못함.

---

## 7. Cube

**한 줄 요약**: 특정 클라우드에 묶이지 않는 독립 시맨틱 레이어를 쥐고, 그 위에서 분석 에이전트(모델 작성·차트·대화형 분석)를 직접 제공한다. "text-to-SQL 대신 시맨틱 레이어 위의 에이전트"가 핵심 주장.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Cube 시맨틱 레이어 | 측정값·차원·조인을 코드로 정의, BI·스프레드시트·임베디드·에이전트에 동일하게 제공 | GA | L1, L2, GOV◐ | cube.dev |
| Semantic Model Agent | 웨어하우스 테이블·LookML에서 시맨틱 모델을 자동 작성·변환 | GA 2025-10-29 | L2 | cube.dev/blog/cube-agentic-analytics |
| Analytics Chat Agent | 여러 질의를 돌려 분석·요약, 결과를 워크북에 저장 | GA 2025-10-29 | L6, L7◐ | 같은 글 |
| Workbook/Dashboard Agents | 보고서·시각화 생성·수정 | GA 2025-10-29 | L7 | 같은 글 |

**층 커버리지**: L1● L2● L3 L4 L5 L6◐ L7◐ GOV◐ OBS

**2026 주요 움직임**
- 2026: Gartner Agentic Analytics 시장 가이드에 언급(2차, 미검증).
- (참고) 2025-06 D3로 프리뷰 → 2025-10 GA하며 D3 이름 폐기.

**불확실**: Cube MCP 서버 존재·상태, 2026년 신제품은 공식 자료로 확인하지 못함.

---

## 8. AtScale

**한 줄 요약**: 오픈 시맨틱 모델 언어(SML)와 MCP 서버로 "어느 클라우드 에이전트든 같은 지표"를 내세우는 중립 시맨틱 레이어. Databricks·AWS·Snowflake 생태계에 동시에 붙는다.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| AtScale 시맨틱 레이어 | 여러 웨어하우스 위 지표·차원 모델, 질의 가속 | GA | L2 | atscale.com |
| SML (Semantic Modeling Language) | YAML 기반·버전관리되는 오픈 시맨틱 모델 형식 | 공개 | L2 | aws blog 2026-10-20 |
| AtScale MCP Server | `/mcp` 엔드포인트로 시맨틱 모델을 에이전트에 노출, Databricks MCP 마켓플레이스 등록 | GA 2025-12-01 | L1, L2 | businesswire 2025-12-01 |
| Bedrock AgentCore 연동 | AgentCore Gateway가 자격증명을 맡고 에이전트가 AtScale MCP 호출 | 레퍼런스 아키텍처 2026-10-20 | L1, GOV◐ | aws.amazon.com blog |

**층 커버리지**: L1◐ L2● L3 L4 L5 L6 L7 GOV◐ OBS

**2026 주요 움직임**
- 2026-10-20: AWS 공식 블로그에 AtScale+Bedrock AgentCore 시맨틱 레이어 구성 게재.
- 2026-06~: ACE 엔진이 Snowflake Semantic Views 내부에서 비공개 프리뷰(경쟁사 Atlan 자료, 2차).

**불확실**: MCP 도구 목록, Snowflake 연동 GA·가격 미확인.

---

## 9. Atlan

**한 줄 요약**: 메타데이터 카탈로그에서 "에이전트 컨텍스트 레이어"로 가장 공격적으로 재포지셔닝한 회사. 컨텍스트를 AI가 초안 작성 → 시험(evals) → 사람 승인 → 배포 → 학습하는 소프트웨어 개발식 수명주기를 제품화.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Context Agents | 데이터 자산을 분석해 테이블 설명·선호 조인·필터·지표·온톨로지를 자동 생성 | 출시 2026-06 | L2, L3◐ | atlan.com Snowflake Summit 2026 |
| Context Engineering Studio | 컨텍스트 빌드·테스트·리뷰·승인·배포·학습 수명주기, 대시보드·SQL로 평가셋 생성, 결과는 버전관리되는 context repo(시맨틱 모델·스킬·soul.md) | 출시 2026-06 | L2, L4, OBS, GOV | atlan.com context-engineering-studio |
| Atlan MCP Server | 한 컨텍스트 레이어를 여러 에이전트 플랫폼에 MCP로 공급 | GA | L1, L6◐ | atlan.com |
| Data Graph / Context Lakehouse | 전사 메타데이터 그래프와 대량 읽기용 컨텍스트 저장소 | GA(자사 주장) | L3, L5 | atlan.com Activate 2026 |

**층 커버리지**: L1● L2● L3◐ L4◐ L5◐ L6◐ L7 GOV● OBS◐

**2026 주요 움직임**
- 2026-06-02(Snowflake Summit): Context Agents·Context Engineering Studio·MCP 서버 발표("이번 주 출시").
- 2026-04-29(Activate 2026): 컨텍스트 레이어 5단계(Data Graph→Context Agents→Knowledge Folders→Studio→Lakehouse) 제시.

**불확실**: 성과 수치(2주 만에 컨텍스트 부트스트랩, 90일 80억 회 읽기, MCP 호출 58배 증가)는 모두 자사 발표. 2026 투자 유치 소식은 확인 못함.

---

## 10. Collibra

**한 줄 요약**: 데이터 거버넌스 카탈로그를 "AI·에이전트 통제면"으로 확장. MCP로 거버넌스된 메타데이터를 에이전트에 주고, 인수(trail ML·Raito)로 런타임 통제·접근 관리를 보강.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Collibra MCP Server | 거버넌스된 메타데이터·비즈니스 맥락을 에이전트에 실시간 제공 | GA (고객 100+, Databricks 마켓플레이스) | L1, L2, GOV | collibra.com blog 2026-05-06 |
| AI Command Center | 운영 중인 에이전트·모델·유스케이스를 한 화면에서 소유·활동·결정·위험 신호로 관리 | 비공개 프리뷰(40+ 기업) 2026-05 | GOV, OBS | 같은 글, hpcwire |
| 비즈니스 용어집·계보·데이터 카탈로그 | 용어 정의, 데이터 계보 | GA | L2, L5 | collibra.com |
| Snowflake/Databricks 연동 | Horizon Catalog·Cortex Agents로 맥락 전달 / Agent Bricks 런치 파트너 | Snowflake 연동 프리뷰(Q3 2026 확대 예정) | L2, GOV | collibra 보도자료 |
| trail ML (인수) | AI 시스템에 적용 규정 판단·통제 평가·에이전트 동작 지점의 정책 집행 | 인수 2026-10-05 | GOV, OBS | cdomagazine 2026-10-06 |

**층 커버리지**: L1◐ L2● L3◐ L4 L5● L6 L7 GOV● OBS●

**2026 주요 움직임**
- 2026-10-05: trail ML 인수(AI 거버넌스 상시 평가·런타임 통제).
- 2026-06: Databricks 2026 거버넌스 파트너상, Agent Bricks 런치 파트너.
- 2026-05-06: AI Command Center 발표, MCP 서버 고객 100+ 공개.
- (참고) 2025-06 Raito(데이터 접근) 인수.

**불확실**: MCP 도구 목록·가격, AI Command Center GA 시점.

---

## 11. Alation

**한 줄 요약**: 카탈로그 회사에서 데이터·컨텍스트·에이전트를 한데 묶은 "AIOS"로 재정의. 에이전트를 평가로 검증한 뒤 운영하고, 교정 내용을 다시 데이터·컨텍스트에 되먹이는 순환을 강조.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| AIOS | 카탈로그(기록 시스템)+컨텍스트+에이전트+피드백 계층을 묶은 통합 플랫폼 이름 | 발표 2026-07-14 | L2, L5, GOV, OBS◐ | alation.com 보도자료, blocksandfiles |
| Agent Studio (SDK + Agent Builder) | 메타데이터를 아는 에이전트를 만들고 평가 후 배포 | GA(2025-11 통합) | L4, L6, OBS◐ | alation.com blog |
| AI Agent SDK / MCP Server | 카탈로그 검색·발견 기능을 에이전트에 노출(오픈소스 파이썬, stdio/HTTP) | 1.0 RC (2025-12) | L1, L2 | pypi alation-ai-agent-mcp |
| Ontologies·Data Products 모듈 | 온톨로지, 데이터 제품 정의 | GA(모듈 목록 기준) | L2, L3◐ | alation.com |

**층 커버리지**: L1◐ L2● L3◐ L4◐ L5● L6◐ L7 GOV● OBS◐

**2026 주요 움직임**
- 2026-07-14: AIOS 발표(새 제품이 아니라 기존 통합 시스템의 이름이라고 자사 설명).
- (참고) 2025-05 Numbers Station(구조화 데이터 에이전트) 인수, 2025-03 Agentic Platform 발표.

**불확실**: AIOS 보도자료에 MCP·evals 구체 기능 표기 없음. "OS" 명칭의 실체에 대한 비판(diginomica).

---

## 12. DataHub (Acryl Data)

**한 줄 요약**: 오픈소스 메타데이터 그래프(DataHub Core)를 "에이전트용 컨텍스트 플랫폼"으로 바꿔 부르고, 읽기뿐 아니라 쓰기(태그·설명·용어 갱신) 도구까지 MCP로 제공. 오픈소스+관리형 이중 구조.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| DataHub Context Platform (Cloud) | 기술 메타데이터·비즈니스 지식·문서를 묶은 에이전트용 컨텍스트 계층 | 2026-05-28 출시 / 공개 베타 2026-09 기록과 상충 | L2, L3, L5 | datahub.com |
| DataHub MCP Server | 검색·엔티티 상세·계보·쿼리·문서 검색 + 태그/설명/용어/소유자 쓰기, 호스티드·오픈소스 둘 다 | GA(호스티드 Cloud 기본 활성) | L1, L5, L7◐ | docs.datahub.com agent-context |
| Agent Context Kit | 에이전트 개발용 가이드·SDK(pip)·MCP 묶음 | 공개 | L1, L6◐ | docs.datahub.com |
| Ask DataHub | 메타데이터 대상 자연어 질의 | GA | L6◐ | datahub.com |
| DataHub Core (OSS) | Apache 2.0 메타데이터 그래프 | GA | L1, L3, L5 | datahub.com |

**층 커버리지**: L1● L2● L3● L4 L5● L6◐ L7◐ GOV◐ OBS◐

**2026 주요 움직임**
- 2026-09: Context Platform 공개 베타(일부 자료), Cloud v2.1에서 범위 지정 MCP 서버 기본 활성.
- 2026-05-28: Cloud 업데이트로 Context Management Platform 도입.

**불확실**: Context Platform의 정확한 단계(출시 vs 베타). 시장 수치(91% 등)는 자사 의뢰 조사.

---

## 13. Neo4j

**한 줄 요약**: 그래프 DB 회사가 "에이전트의 지식 계층"으로 이동 중. Aura Agent로 그래프 기반 에이전트를 MCP로 배포하고, Context Engine으로 사전 정의된 6층 비즈니스 온톨로지+에이전트 기억을 제공하려 한다.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Aura Agent | 그래프 스키마에서 에이전트 자동 초안, 벡터·질의 템플릿·Text2Cypher 3종 검색기, 원클릭으로 OAuth MCP 서버 배포 | GA 2026-02-03 ($0.35/에이전트·시간) | L1, L3, L6 | neo4j.com blog aura agent |
| Neo4j Context Engine | 6층 비즈니스 온톨로지, Databricks·Snowflake에서 온톨로지 구축, Context Studio(거버넌스·에이전트·MCP 설정), 단기·장기·추론 기억과 스킬 증류 | 비공개 프리뷰 2026-10-20 | L3, L4◐, L5, GOV◐ | neo4j.com 보도자료 2026-10-20 |
| Neo4j MCP Server | 그래프 질의를 MCP 도구로 노출 | 호스티드 지원 예정(완료 미확인) | L1 | neo4j.com |
| GraphRAG 검색기(+ Gemini Enterprise A2A 연동) | 지식그래프 기반 검색 증강, A2A로 Gemini Enterprise와 연결 | GA | L3, L6 | neo4j.com blog google cloud |

**층 커버리지**: L1● L2◐ L3● L4◐ L5◐ L6● L7◐ GOV◐ OBS

**2026 주요 움직임**
- 2026-10-20: Context Engine 발표(비공개 프리뷰, 디자인 파트너 모집).
- 2026-07: AI 제품 키노트에서 Document Intelligence 등 로드맵 공개.
- 2026-02-03: Aura Agent GA.

**불확실**: Context Engine 상태는 자료 간 상충(보도자료=비공개 프리뷰, TechTarget=초기 버전 GA) → 1차 자료 따라 프리뷰. 분석가는 현재 읽기 전용 지식 계층이라고 지적. Aura Agent GA 게시일과 페이지 메타데이터 날짜 불일치.

---

## 기타 후보 (이번 묶음에서 제외)
- **Stardog**: Voicebox(지식그래프+LLM 답변 엔진), 공식 MCP 서버(원격, 베타). 2026 "Semantic Control Plane" 리브랜딩은 경쟁사 자료로만 확인.
- **TigerGraph**: 2026년 에이전트·MCP 공식 발표 확인 못함.
- **Teradata**: Enterprise Vector Store 에이전트·멀티모달 기능 2026-04 GA, MCP로 벡터 연산 노출, AgentStack(2026-01). 데이터 플랫폼 성격이 강해 다음 확장 시 포함 검토.

---

## 데이터 블록

```yaml
vendors:
  - vendor: salesforce
    name: Salesforce (Data 360 / Tableau / Informatica / MuleSoft)
    category: enterprise_app
    products:
      - id: salesforce-data360-mcp
        name: Data 360 MCP Server
        status: GA
        status_date: 2026-10
        layers: {L1: ●, L7: ●, GOV: ◐}
        x: 1
        y: 0
        xy_reason: "고객 데이터 조회와 세그먼트 생성 같은 쓰기 작업을 함께 노출, 컨텍스트는 Data 360에 사람이 구성한 모델 기반"
        maturity: 2
        evidence:
          - {url: "https://www.infotech.com/software-reviews/vendor-technology-notes/dreamforce-2026-data-360-tableau-informatica", kind: secondary, date: 2026-11-11}
      - id: salesforce-agent-context-engine
        name: Agent Context Engine
        status: announced
        status_date: 2026-12
        layers: {L6: ●, GOV: ●}
        x: 1
        y: 1
        xy_reason: "요청마다 허용된 정형·비정형 정보를 런타임에 골라 조립"
        maturity: 2
        evidence:
          - {url: "https://www.infotech.com/software-reviews/vendor-technology-notes/dreamforce-2026-data-360-tableau-informatica", kind: secondary, date: 2026-11-11}
      - id: salesforce-data360-agent-memory-catalog
        name: Data 360 Agent Memory / Salesforce Catalog
        status: announced
        status_date: 2026-10
        layers: {L5: ●, L2: ◐}
        x: 1
        y: 1
        xy_reason: "에이전트 상호작용을 공유 기억으로 축적, 카탈로그는 필드 의미·권한 설명"
        maturity: 1
        evidence:
          - {url: "https://trailhead.salesforce.com/content/learn/modules/winter-27-release-highlights/see-whats-new-data360-mulesoft-tableau-informatica", kind: official, date: 2026-11-11}
      - id: salesforce-tableau-semantics-knowledge
        name: Tableau Semantics + Tableau Knowledge
        status: preview
        status_date: 2026-10
        layers: {L2: ●, L3: ◐}
        x: -2
        y: -1
        xy_reason: "지표·차원 정의가 중심, 지식그래프는 자동 구성 보조"
        maturity: 1
        evidence:
          - {url: "https://trailhead.salesforce.com/content/learn/modules/winter-27-release-highlights/see-whats-new-data360-mulesoft-tableau-informatica", kind: official, date: 2026-11-11}
          - {url: "https://research.isg-one.com/analyst-perspectives/salesforce-adds-knowledge-to-tableau-for-agentic-analytics", kind: secondary, date: 2026-11-11}
      - id: salesforce-informatica-headless
        name: Informatica Headless (Managed MCP)
        status: GA
        status_date: 2026-05
        layers: {L1: ●, L3: ◐, GOV: ●}
        x: -1
        y: -1
        xy_reason: "데이터 품질·통합·MDM 같은 사전 관리된 데이터 서비스를 에이전트에 노출"
        maturity: 2
        evidence:
          - {url: "https://trailhead.salesforce.com/content/learn/modules/winter-27-release-highlights/see-whats-new-data360-mulesoft-tableau-informatica", kind: official, date: 2026-11-11}
          - {url: "https://www.intelligentcio.com/me/2026/06/03/informatica-launches-autonomous-data-management-agents/", kind: secondary, date: 2026-06-03}
          - {url: "https://investor.salesforce.com/news/news-details/2025/Salesforce-Completes-Acquisition-of-Informatica/", kind: official, date: 2025-11-18}
      - id: salesforce-mulesoft-agent-fabric
        name: MuleSoft Agent Fabric (Registry, Scanners, Kill Switch)
        status: GA
        status_date: 2026-01
        layers: {L1: ●, L6: ◐, GOV: ●, OBS: ◐}
        x: 1
        y: 1
        xy_reason: "사내 에이전트·MCP 서버를 자동 발견해 등록하고 실행 단계에서 정지·비용 통제"
        maturity: 3
        evidence:
          - {url: "https://www.salesforce.com/news/stories/mulesoft-agent-fabric-automated-agent-discovery", kind: official, date: 2026-11-11}

  - vendor: sap
    name: SAP
    category: enterprise_app
    products:
      - id: sap-business-ai-platform
        name: SAP Business AI Platform
        status: announced
        status_date: 2026-05
        layers: {L1: ●, L2: ●, GOV: ●}
        x: 1
        y: -1
        xy_reason: "ERP 프로세스·데이터 제품 위에 에이전트를 만들고 통제하는 통합 플랫폼"
        maturity: 2
        evidence:
          - {url: "https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/", kind: official, date: 2026-05-12}
      - id: sap-business-data-cloud
        name: SAP Business Data Cloud
        status: GA
        status_date: 2025-02
        layers: {L1: ●, L2: ●}
        x: -1
        y: -1
        xy_reason: "의미가 보존된 데이터 제품을 사전에 큐레이션해 제공"
        maturity: 1
        evidence:
          - {url: "https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/", kind: official, date: 2026-05-12}
      - id: sap-knowledge-graph
        name: SAP Knowledge Graph
        status: announced
        status_date: 2027-03
        layers: {L3: ●}
        x: 1
        y: -1
        xy_reason: "업무 엔티티·프로세스·관계 지도, SAP가 미리 모델링"
        maturity: 1
        evidence:
          - {url: "https://itbrief.co.uk/story/sap-launches-business-ai-platform-autonomous-suite", kind: secondary, date: 2026-05-12}
          - {url: "https://futurumgroup.com/insights/precision-over-prose-why-sap-knowledge-graph-is-the-secret-to-production-ready-ai/", kind: secondary, date: 2026-11-11}
      - id: sap-ontology-manager
        name: SAP Ontology Manager
        status: announced
        status_date: 2027-03
        layers: {L3: ●, L7: ◐}
        x: 1
        y: -2
        xy_reason: "개념·관계·SHACL 제약을 사람이 정의하고 질의 전 검증"
        maturity: 4
        evidence:
          - {url: "https://architecture.learning.sap.com/docs/ref-arch/e15602", kind: official, date: 2026-11-11}
          - {url: "https://erp.today/sap-teched-2026-whats-rolling-out-and-whats-planned-through-2027/", kind: secondary, date: 2026-11-11}
      - id: sap-joule-studio
        name: Joule Studio / Joule Agents
        status: GA
        status_date: 2026-05
        layers: {L4: ●, L6: ●, L7: ●}
        x: 2
        y: 0
        xy_reason: "HR·구매·공급망 등 업무 실행 에이전트 구축"
        maturity: 3
        evidence:
          - {url: "https://itbrief.co.uk/story/sap-launches-business-ai-platform-autonomous-suite", kind: secondary, date: 2026-05-12}
      - id: sap-joule-work
        name: Joule Work
        status: announced
        status_date: 2026-05
        layers: {L6: ●, L7: ●}
        x: 2
        y: 1
        xy_reason: "사용자 의도를 받아 SAP·비SAP 시스템 행동으로 연결, MCP·A2A 지원"
        maturity: 2
        evidence:
          - {url: "https://siliconangle.com/2026/05/12/sap-recasts-joule-front-door-autonomous-enterprise-ai", kind: secondary, date: 2026-05-12}

  - vendor: servicenow
    name: ServiceNow
    category: enterprise_app
    products:
      - id: servicenow-context-engine
        name: Context Engine
        status: announced
        status_date: 2026-05
        layers: {L2: ●, L3: ●, L5: ●}
        x: 2
        y: 1
        xy_reason: "사람·자산·정책·결정 이력을 실시간 매핑하고 시스템 활동으로 계속 학습"
        maturity: 2
        evidence:
          - {url: "https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-launches-the-real-time-data-foundation-that-puts-autonomous-AI-to-work-across-the-enterprise/default.aspx", kind: official, date: 2026-05-06}
      - id: servicenow-workflow-data-fabric
        name: Workflow Data Fabric
        status: GA
        status_date: 2026-05
        layers: {L1: ●, L7: ●}
        x: 2
        y: 0
        xy_reason: "전사 데이터를 워크플로우 실행 계층에 연결"
        maturity: 2
        evidence:
          - {url: "https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-launches-the-real-time-data-foundation-that-puts-autonomous-AI-to-work-across-the-enterprise/default.aspx", kind: official, date: 2026-05-06}
          - {url: "https://www.servicenow.com/docs/r/zurich/integrate-applications/create-integrations-applications.html", kind: official, date: 2026-11-11}
      - id: servicenow-data-catalog
        name: ServiceNow Data Catalog (formerly data.world)
        status: GA
        status_date: 2026-05
        layers: {L2: ●, L3: ●, L5: ●}
        x: -1
        y: -1
        xy_reason: "용어집·계보를 사람이 관리, 지식그래프 기반 카탈로그"
        maturity: 1
        evidence:
          - {url: "https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-launches-the-real-time-data-foundation-that-puts-autonomous-AI-to-work-across-the-enterprise/default.aspx", kind: official, date: 2026-05-06}
          - {url: "https://www.constellationr.com/insights/news/servicenow-launches-workflow-data-network-acquires-dataworld", kind: secondary, date: 2025-05-07}
      - id: servicenow-autonomous-data-analytics
        name: Autonomous Data Analytics
        status: announced
        status_date: 2026-05
        layers: {L2: ◐, L6: ●}
        x: -2
        y: 1
        xy_reason: "사람·에이전트가 자연어로 전사 데이터에 숫자 질문"
        maturity: 1
        evidence:
          - {url: "https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-launches-the-real-time-data-foundation-that-puts-autonomous-AI-to-work-across-the-enterprise/default.aspx", kind: official, date: 2026-05-06}
      - id: servicenow-mcp-registry-control-tower
        name: MCP Registry + AI Control Tower / AI Gateway
        status: preview
        status_date: 2026-05
        layers: {L1: ◐, GOV: ●, OBS: ●}
        x: 1
        y: 0
        xy_reason: "검증된 MCP 서버 카탈로그와 타사 AI까지 통제·관측"
        maturity: 3
        evidence:
          - {url: "https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-launches-the-real-time-data-foundation-that-puts-autonomous-AI-to-work-across-the-enterprise/default.aspx", kind: official, date: 2026-05-06}

  - vendor: oracle
    name: Oracle
    category: data_platform
    products:
      - id: oracle-ai-database-26ai
        name: Oracle AI Database 26ai
        status: GA
        status_date: 2025-10
        layers: {L1: ●}
        x: -1
        y: -1
        xy_reason: "벡터·RAG 내장 DB, 데이터 원천 역할"
        maturity: 1
        evidence:
          - {url: "https://www.oracle.com/autonomous-database/select-ai/", kind: official, date: 2026-11-11}
      - id: oracle-select-ai-agent
        name: Select AI / Select AI Agent
        status: GA
        status_date: 2026-01
        layers: {L1: ●, L6: ◐, L7: ●}
        x: 0
        y: 0
        xy_reason: "NL2SQL 분석과 DB 내부 도구 실행을 모두 지원"
        maturity: 2
        evidence:
          - {url: "https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/byysy/", kind: official, date: 2026-11-11}
      - id: oracle-adb-mcp-server
        name: Autonomous AI Database MCP Server
        status: GA
        status_date: null
        layers: {L1: ●, L7: ●, GOV: ●}
        x: 0
        y: -1
        xy_reason: "DBA가 정의한 도구만 노출, DB 역할·VPD·감사로 통제"
        maturity: 2
        evidence:
          - {url: "https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/about-mcp-server.html", kind: official, date: 2026-11-11}
      - id: oracle-fusion-ai-agent-studio
        name: Fusion AI Agent Studio + Agent Marketplace
        status: GA
        status_date: 2025-10
        layers: {L4: ●, L7: ●}
        x: 2
        y: -1
        xy_reason: "ERP·HCM 업무 에이전트를 템플릿으로 구축·배포"
        maturity: 3
        evidence:
          - {url: "https://www.oracle.com/uk/news/announcement/ai-world-oracle-expands-ai-agent-studio-for-fusion-applications-with-new-marketplace-llms-and-vast-partner-network-2025-10-15/", kind: official, date: 2025-10-15}

  - vendor: ibm
    name: IBM
    category: data_platform
    products:
      - id: ibm-watsonx-data-confluent
        name: watsonx.data + Confluent streaming
        status: GA
        status_date: 2026-03
        layers: {L1: ●, L5: ◐, GOV: ●}
        x: -1
        y: 0
        xy_reason: "실시간 이벤트를 계보·정책과 함께 에이전트용 데이터로 공급"
        maturity: 1
        evidence:
          - {url: "https://confluent.io/press-release/ibm-completes-acquisition-of-confluent/", kind: official, date: 2026-03-17}
      - id: ibm-watsonx-data-integration-mcp
        name: watsonx.data integration MCP server
        status: GA
        status_date: 2026-06
        layers: {L1: ●, L7: ●}
        x: 0
        y: 0
        xy_reason: "에이전트가 데이터 파이프라인 자체를 다루는 도구"
        maturity: 2
        evidence:
          - {url: "https://community.ibm.com/community/user/blogs/john-wen/2026/06/15/agentic-data-integration-is-here-with-the-watsonxd", kind: official, date: 2026-06-15}
      - id: ibm-agentic-data-integration
        name: Agentic Data Integration
        status: preview
        status_date: 2026-10
        layers: {L1: ●, L7: ●}
        x: 0
        y: 1
        xy_reason: "자연어로 통합 작업 지시, 외부 에이전트는 MCP로 접속"
        maturity: 2
        evidence:
          - {url: "https://omdia.tech.informa.com/blogs/2026/oct/ibm-previews-agentic-data-integration-for-watsonx-data", kind: secondary, date: 2026-10-20}
      - id: ibm-watsonx-orchestrate
        name: watsonx Orchestrate (+ AI Gateway)
        status: GA
        status_date: 2026-05
        layers: {L4: ●, L6: ●, GOV: ●, OBS: ●}
        x: 2
        y: 0
        xy_reason: "업무 에이전트 조율과 타사 에이전트·MCP 통제"
        maturity: 3
        evidence:
          - {url: "https://techstrong.ai/?p=74824", kind: secondary, date: 2026-11-11}
          - {url: "https://nand-research.com/research-note-ibm-orchestrate-for-enterprise-agentic-ai/", kind: secondary, date: 2026-11-11}
      - id: ibm-data-intelligence-mcp
        name: Data Intelligence MCP server
        status: GA
        status_date: null
        layers: {L1: ●, L2: ◐, L5: ◐}
        x: -1
        y: -1
        xy_reason: "카탈로그·계보 메타데이터 조회"
        maturity: 1
        evidence:
          - {url: "https://github.com/ibm/data-intelligence-mcp-server", kind: official, date: 2026-11-11}

  - vendor: fivetran-dbt
    name: Fivetran + dbt Labs
    category: semantic_catalog
    products:
      - id: dbt-semantic-layer
        name: dbt Semantic Layer (MetricFlow)
        status: GA
        status_date: 2024-01
        layers: {L2: ●}
        x: -2
        y: -2
        xy_reason: "분석 엔지니어가 코드로 지표를 미리 정의"
        maturity: 1
        evidence:
          - {url: "https://docs.getdbt.com/docs/dbt-ai/about-mcp", kind: official, date: 2026-11-11}
      - id: dbt-mcp-server
        name: dbt MCP server (local/remote)
        status: GA
        status_date: 2025-10
        layers: {L1: ●, L2: ●, L5: ◐, L7: ◐}
        x: -1
        y: -1
        xy_reason: "지표·계보 메타데이터 조회 중심, 로컬은 dbt 명령 실행"
        maturity: 2
        evidence:
          - {url: "https://docs.getdbt.com/docs/dbt-ai/about-mcp", kind: official, date: 2026-11-11}
          - {url: "https://www.selectstar.com/resources/dbt-coalesce-2025", kind: secondary, date: 2025-10-15}
      - id: dbt-agents-schema
        name: Agents Schema (open standard)
        status: announced
        status_date: 2026-06
        layers: {L2: ●, L5: ◐}
        x: -2
        y: -1
        xy_reason: "지표·시맨틱 모델·계보를 웨어하우스 스키마로 에이전트에 공개"
        maturity: 1
        evidence:
          - {url: "https://www.techzine.eu/news/analytics/141758/fivetran-and-dbt-labs-complete-merger-data-infrastructure-for-reliable-agentic-ai/", kind: secondary, date: 2026-06-01}
      - id: fivetran-connectors
        name: Fivetran connectors
        status: GA
        status_date: 2026-06
        layers: {L1: ●}
        x: -1
        y: -2
        xy_reason: "원천 데이터를 미리 적재"
        maturity: 0
        evidence:
          - {url: "https://www.techtarget.com/searchdatamanagement/news/366643590/Fivetran-DBT-Labs-complete-merger-to-form-data-layer-for-AI", kind: secondary, date: 2026-06-01}

  - vendor: cube
    name: Cube
    category: semantic_catalog
    products:
      - id: cube-semantic-layer
        name: Cube semantic layer
        status: GA
        status_date: 2025-10
        layers: {L1: ●, L2: ●, GOV: ◐}
        x: -2
        y: -2
        xy_reason: "측정값·차원을 코드로 미리 정의하는 독립 시맨틱 레이어"
        maturity: 1
        evidence:
          - {url: "https://cube.dev/blog/cube-agentic-analytics", kind: official, date: 2025-10-29}
      - id: cube-semantic-model-agent
        name: Semantic Model Agent
        status: GA
        status_date: 2025-10
        layers: {L2: ●}
        x: -2
        y: 0
        xy_reason: "에이전트가 시맨틱 모델 초안을 만들고 사람이 다듬음"
        maturity: 1
        evidence:
          - {url: "https://cube.dev/blog/cube-agentic-analytics", kind: official, date: 2025-10-29}
      - id: cube-analytics-chat
        name: Analytics Chat / Workbook agents
        status: GA
        status_date: 2025-10
        layers: {L6: ◐, L7: ◐}
        x: -2
        y: 1
        xy_reason: "여러 질의를 스스로 돌려 숫자 질문에 답함"
        maturity: 2
        evidence:
          - {url: "https://cube.dev/blog/cube-agentic-analytics", kind: official, date: 2025-10-29}
          - {url: "https://cube.dev/blog/announcing-cube-d3", kind: official, date: 2025-06-02}

  - vendor: atscale
    name: AtScale
    category: semantic_catalog
    products:
      - id: atscale-semantic-layer-sml
        name: AtScale semantic layer + SML
        status: GA
        status_date: null
        layers: {L2: ●}
        x: -2
        y: -2
        xy_reason: "YAML·버전관리 시맨틱 모델을 사람이 정의"
        maturity: 1
        evidence:
          - {url: "https://aws.amazon.com/blogs/machine-learning/build-a-semantic-layer-for-agentic-ai-on-aws-with-atscale-and-amazon-bedrock-agentcore", kind: official, date: 2026-10-20}
      - id: atscale-mcp-server
        name: AtScale MCP Server
        status: GA
        status_date: 2025-12
        layers: {L1: ●, L2: ●, GOV: ◐}
        x: -2
        y: -1
        xy_reason: "정의된 지표를 여러 클라우드 에이전트에 질의 도구로 제공"
        maturity: 2
        evidence:
          - {url: "https://www.businesswire.com/news/home/20251201005442/en/AtScale-Delivers-Semantic-Intelligence-to-Databricks-MCP-Marketplace/", kind: official, date: 2025-12-01}
          - {url: "https://atlan.com/know/ai-agent/semantic-layer/atscale-vs-context-layer/", kind: secondary, date: 2026-09-01}

  - vendor: atlan
    name: Atlan
    category: semantic_catalog
    products:
      - id: atlan-context-agents
        name: Context Agents
        status: GA
        status_date: 2026-06
        layers: {L2: ●, L3: ◐}
        x: -1
        y: 1
        xy_reason: "에이전트가 데이터 자산을 분석해 설명·조인·지표·온톨로지를 자동 생성"
        maturity: 2
        evidence:
          - {url: "https://atlan.com/snowflake-summit-2026-announcements/", kind: official, date: 2026-06-02}
      - id: atlan-context-engineering-studio
        name: Context Engineering Studio
        status: GA
        status_date: 2026-06
        layers: {L2: ●, L4: ◐, GOV: ●, OBS: ●}
        x: -1
        y: 0
        xy_reason: "AI 초안 + 사람 승인, 평가셋으로 시험 후 배포하고 학습"
        maturity: 5
        evidence:
          - {url: "https://atlan.com/context-engineering-studio.md", kind: official, date: 2026-11-11}
          - {url: "https://atlan.com/snowflake-summit-2026-announcements/", kind: official, date: 2026-06-02}
      - id: atlan-mcp-server
        name: Atlan MCP Server
        status: GA
        status_date: 2026-06
        layers: {L1: ●, L6: ◐}
        x: -1
        y: 0
        xy_reason: "한 컨텍스트 레이어를 여러 에이전트 플랫폼에 공급"
        maturity: 2
        evidence:
          - {url: "https://atlan.com/snowflake-summit-2026-announcements/", kind: official, date: 2026-06-02}
      - id: atlan-data-graph-context-lakehouse
        name: Data Graph / Context Lakehouse
        status: GA
        status_date: 2026-04
        layers: {L3: ●, L5: ●}
        x: -1
        y: -1
        xy_reason: "전사 메타데이터 그래프·컨텍스트 저장소"
        maturity: 1
        evidence:
          - {url: "https://atlan.com/know/context-layer-stopped-being-theoretical-activate-2026/", kind: official, date: 2026-04-29}

  - vendor: collibra
    name: Collibra
    category: semantic_catalog
    products:
      - id: collibra-mcp-server
        name: Collibra MCP Server
        status: GA
        status_date: 2026-05
        layers: {L1: ●, L2: ●, GOV: ●}
        x: -1
        y: -2
        xy_reason: "스튜어드가 관리한 메타데이터·용어를 에이전트에 제공"
        maturity: 2
        evidence:
          - {url: "https://www.collibra.com/blog/the-end-to-end-control-plane-for-ai-has-arrived", kind: official, date: 2026-05-06}
      - id: collibra-ai-command-center
        name: AI Command Center
        status: preview
        status_date: 2026-05
        layers: {GOV: ●, OBS: ●}
        x: 1
        y: 0
        xy_reason: "운영 중인 에이전트의 활동·결정·위험을 통제"
        maturity: 3
        evidence:
          - {url: "https://www.collibra.com/blog/the-end-to-end-control-plane-for-ai-has-arrived", kind: official, date: 2026-05-06}
          - {url: "https://www.hpcwire.com/bigdatawire/this-just-in/collibra-launches-ai-command-center-to-scale-agentic-ai-with-real-time-oversight-and-continuous-control", kind: secondary, date: 2026-05-06}
      - id: collibra-glossary-lineage
        name: Business glossary / lineage / catalog
        status: GA
        status_date: null
        layers: {L2: ●, L5: ●}
        x: -1
        y: -2
        xy_reason: "용어·계보를 사람이 큐레이션"
        maturity: 1
        evidence:
          - {url: "https://collibra.com/company/newsroom/press-releases/snowflake-and-collibra-expand-partnership-to-bring-governed-business-context-and-semantics", kind: official, date: 2026-11-11}
      - id: collibra-trail-ml
        name: trail ML (acquired) — continuous AI governance
        status: announced
        status_date: 2026-10
        layers: {GOV: ●, OBS: ◐}
        x: 1
        y: 0
        xy_reason: "에이전트 동작 지점에서 통제를 재확인·집행"
        maturity: 3
        evidence:
          - {url: "https://www.cdomagazine.tech/aiml/collibra-acquisition-pushes-ai-governance-toward-continuous-control", kind: secondary, date: 2026-10-06}

  - vendor: alation
    name: Alation
    category: semantic_catalog
    products:
      - id: alation-aios
        name: AIOS (Alation Intelligence Operating System)
        status: announced
        status_date: 2026-07
        layers: {L2: ●, L5: ●, GOV: ●, OBS: ◐}
        x: -1
        y: 0
        xy_reason: "카탈로그+컨텍스트+에이전트, 교정을 되먹이는 피드백 계층"
        maturity: 5
        evidence:
          - {url: "https://www.alation.com/news-and-press/alation-launches-aios-intelligence-operating-system/", kind: official, date: 2026-07-14}
          - {url: "https://www.blocksandfiles.com/ai-ml/2026/07/14/alation-builds-ai-agent-operating-system/5271050", kind: secondary, date: 2026-07-14}
      - id: alation-agent-studio
        name: Agent Studio (SDK + Agent Builder)
        status: GA
        status_date: 2025-11
        layers: {L4: ◐, L6: ◐, OBS: ◐}
        x: 0
        y: 0
        xy_reason: "메타데이터 기반 에이전트를 만들고 평가 후 운영"
        maturity: 4
        evidence:
          - {url: "https://www.alation.com/blog/alation-ai-agent-sdk-smarter-ai-models/", kind: official, date: 2026-11-11}
      - id: alation-mcp-server
        name: Alation AI Agent SDK / MCP server
        status: preview
        status_date: 2025-12
        layers: {L1: ●, L2: ●}
        x: -1
        y: -1
        xy_reason: "카탈로그 검색·발견 기능을 도구로 노출"
        maturity: 2
        evidence:
          - {url: "https://pypi.org/project/alation-ai-agent-mcp/", kind: official, date: 2026-11-11}

  - vendor: datahub
    name: DataHub (Acryl Data)
    category: semantic_catalog
    products:
      - id: datahub-context-platform
        name: DataHub Context Platform (Cloud)
        status: preview
        status_date: 2026-09
        layers: {L2: ●, L3: ●, L5: ●}
        x: -1
        y: 0
        xy_reason: "메타데이터·비즈니스 지식·문서를 에이전트용으로 통합, 에이전트 쓰기 반영"
        maturity: 2
        evidence:
          - {url: "https://datahub.com/?p=14496", kind: official, date: 2026-11-11}
          - {url: "https://futurumgroup.com/insights/curing-agentic-hallucinations-datahubs-answer-to-the-ai-context-gap/", kind: secondary, date: 2026-11-11}
      - id: datahub-mcp-server
        name: DataHub MCP Server
        status: GA
        status_date: 2026-05
        layers: {L1: ●, L5: ●, L7: ◐}
        x: -1
        y: 1
        xy_reason: "에이전트가 검색·계보 조회에 더해 태그·설명·용어를 직접 갱신"
        maturity: 2
        evidence:
          - {url: "https://docs.datahub.com/docs/dev-guides/agent-context/agent-context", kind: official, date: 2026-11-11}
      - id: datahub-agent-context-kit
        name: Agent Context Kit
        status: GA
        status_date: 2026-05
        layers: {L1: ●, L6: ◐}
        x: -1
        y: 0
        xy_reason: "에이전트 개발용 SDK·가이드 묶음"
        maturity: 1
        evidence:
          - {url: "https://docs.datahub.com/docs/dev-guides/agent-context/agent-context", kind: official, date: 2026-11-11}
      - id: datahub-core
        name: DataHub Core (OSS)
        status: GA
        status_date: null
        layers: {L1: ●, L3: ●, L5: ●}
        x: -1
        y: -1
        xy_reason: "오픈소스 메타데이터 그래프, 수집기로 자동 적재"
        maturity: 1
        evidence:
          - {url: "https://docs.datahub.com/docs/dev-guides/agent-context/agent-context", kind: official, date: 2026-11-11}

  - vendor: neo4j
    name: Neo4j
    category: knowledge_graph
    products:
      - id: neo4j-aura-agent
        name: Aura Agent
        status: GA
        status_date: 2026-02
        layers: {L1: ●, L3: ●, L6: ●}
        x: 1
        y: 0
        xy_reason: "그래프 스키마로 에이전트 자동 초안, 3종 검색기로 런타임 조회, MCP 배포"
        maturity: 2
        evidence:
          - {url: "https://neo4j.com/blog/agentic-ai/neo4j-launches-aura-agent/", kind: official, date: 2026-02-03}
      - id: neo4j-context-engine
        name: Neo4j Context Engine
        status: preview
        status_date: 2026-10
        layers: {L3: ●, L4: ◐, L5: ●, GOV: ◐}
        x: 1
        y: 1
        xy_reason: "6층 온톨로지(사전 모델) + 에이전트 결정 추적·스킬 증류 기억"
        maturity: 5
        evidence:
          - {url: "https://neo4j.com/?p=433599", kind: official, date: 2026-10-20}
          - {url: "https://www.techtarget.com/data-technologies/news/366652383/Neo4j-joins-the-context-cavalcade-with-suite-for-informing-AI-agents", kind: secondary, date: 2026-10-20}
      - id: neo4j-graphrag-a2a
        name: GraphRAG retrievers + Gemini Enterprise A2A
        status: GA
        status_date: null
        layers: {L3: ●, L6: ●}
        x: 0
        y: 1
        xy_reason: "질의마다 그래프에서 관련 서브그래프를 찾아 조립"
        maturity: 1
        evidence:
          - {url: "https://neo4j.com/blog/news/knowledge-layer-agentic-systems-google-cloud/", kind: official, date: 2026-11-11}
```
