# Databricks — 컨텍스트 엔지니어링 관련 솔루션 (조사일 2026-11-11)

## 한 줄 요약 (이 회사의 전략)
Unity Catalog를 "데이터·AI 자산 + 의미 + 권한"의 단일 통제면으로 삼고, 그 위에 (1) 지표 정의(Metric Views, 2026-04 GA)와 (2) 사용 흔적에서 비즈니스 지식을 자동 추출해 인용까지 붙이는 **Genie Ontology**를 얹어, 업무 사용자용 Genie One·데이터팀용 Genie Code·개발자용 Agent Bricks에 같은 맥락을 공급한다. Snowflake보다 **자동 추출(y축 위쪽)과 실행·메모리(Lakebase)·런타임 거버넌스(Unity AI Gateway)** 쪽을 더 넓게 잡는 것이 특징이다.

## 솔루션 목록
| 제품 | 무엇을 하나(쉬운 말) | 상태 (날짜) | 층 | 근거 URL |
|---|---|---|---|---|
| Unity Catalog Business Semantics (Metric Views) | 지표·차원·매핑을 SQL/YAML로 한 번 정의해 Genie·대시보드·외부 BI가 같이 씀. 동의어·표시명 등 에이전트용 메타데이터 포함 | GA 2026-04-02 (Materialization Preview, 작성 UI 공개 프리뷰, 지표 뷰 간 관계 Beta) | L2 ●, L3 ◐, GOV ◐ | https://www.databricks.com/blog/redefining-semantics-data-layer-future-bi-and-ai , https://docs.databricks.com/aws/en/business-semantics/metric-views |
| Genie Ontology | 메트릭 뷰·대시보드·SQL 쿼리·dbt·Genie 에이전트에서 지표 정의·권위 소스·업무 규칙을 자동 추출해 "지식 스니펫"으로 만들고, 출처·작성자·계보를 답변에 인용 | 발표 2026-06-16, 공식 문서엔 외부 지식원만 Beta 표기(2차 출처는 Public Preview) | L2 ●, L3 ◐, L5 ◐, L6 ●, GOV ◐ | https://docs.databricks.com/en/genie/genie-ontology , https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team |
| Genie Agents (구 Genie Spaces) | 특정 데이터셋·지침·예시 쿼리를 묶은 큐레이션된 질의 에이전트. 대화를 재사용 에이전트로 저장 | GA (2026-07-08 개명) | L2 ◐, L4 ●, L5 ◐, L6 ● | https://docs.databricks.com/gcp/en/release-notes/product/2026/july |
| Genie One | 업무 사용자용 "에이전트 동료". 문서·리포트 생성, 알림·예약 작업, MCP 도구로 외부 앱에서 행동 | GA 2026-06-16 | L4 ◐, L5 ◐, L6 ●, L7 ● | https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team |
| Genie Code (+ ZeroOps) | 데이터 엔지니어링·ML·분석 작업을 계획·구현·실행하는 자율 에이전트, ZeroOps는 파이프라인 장애를 감시·조사·수정 제안 | Genie Code GA 2026-06-16 / ZeroOps 비공개 프리뷰 예정 | L6 ●, L7 ●, OBS ◐ | https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team |
| Agent Bricks (Mosaic AI Agent Framework 계승; Knowledge Assistant·Supervisor Agent·Sandbox) | 어떤 모델·하네스(LangGraph, Claude Code SDK 등)로든 에이전트를 만들어 배포하는 개발자 플랫폼. 문서 QA 에이전트, 멀티에이전트 감독자, 격리 실행 VM | Knowledge Assistant GA 2026-01-13, Supervisor Agent GA 2026-02-10, 플랫폼 확장·Sandbox 발표 2026-06-16 | L1 ◐, L6 ●, L7 ●, GOV ◐ | https://www.databricks.com/blog/agent-bricks-dais-2026 , https://www.databricks.com/blog/agent-bricks-supervisor-agent-now-ga-orchestrate-enterprise-agents |
| Agent Memory Service (Lakebase 기반) | 서버리스 Postgres(Lakebase)에 에이전트의 세션·세션 간 기억과 상태를 저장 | 메모리 서비스 "사용 가능" 2026-06-16, Lakebase GA 2026-02(AWS)·2026-03(Azure) | L5 ● | https://www.databricks.com/blog/agent-bricks-dais-2026 , https://databricks.com/blog/databricks-lakebase-generally-available |
| AI Search (구 Vector Search) | 벡터·하이브리드·전문(full-text) 검색 인덱스. 임베딩 없는 전문 인덱스 지원 | GA, 2026-06-01 개명 | L1 ●, L6 ◐ | https://docs.databricks.com/aws/en/ai-search/ai-search , https://learn.microsoft.com/azure/databricks/release-notes/product/2026/june |
| Managed MCP servers | Genie One·Genie Agent·AI Search·DBSQL·UC 함수·Slack/GitHub/Drive 등 외부 커넥터를 MCP로 노출, UC 권한 항상 적용 | Genie One MCP GA, 워크스페이스 엔드포인트 공개 프리뷰, Unity Gateway MCP(dbsql·sandbox·web_search) Beta | L1 ●, L7 ◐, GOV ● | https://docs.databricks.com/aws/generative-ai/mcp/managed-mcp |
| Unity AI Gateway (Unity Gateway) | 모델·에이전트·MCP·도구 호출을 런타임에 통제: 서비스 정책(누가 어떤 도구), LLM 가드레일(입출력 검사), MCP 페이로드 로깅, 비용 한도 | 4대 기능 Beta 2026-05-19, DAIS에서 확장 발표 | L7 ◐, GOV ●, OBS ◐ | https://databricks.com/blog/whats-new-unity-ai-gateway-service-policies-guardrails-observability-and-cost-controls-ai , https://docs.databricks.com/aws/en/ai-gateway/index/ |
| MLflow 3 GenAI (Tracing·Evaluation·Production monitoring) | 에이전트 실행 트레이스, LLM 판정자로 정답성·근거·안전성 평가, 운영 트레이스에 자동 채점 | MLflow 3.0 발표 2025-06, Databricks 상의 GA 여부 미확인 | OBS ●, L7 ◐ | https://www.databricks.com/blog/mlflow-30-unified-ai-experimentation-observability-and-governance , https://docs.databricks.com/aws/mlflow3/genai/eval-monitor/production-monitoring |

## 회사 전체 층 커버리지
- **L1 연결·원천 ●** — 관리형 MCP 서버(외부 SaaS 커넥터 포함), AI Search, Catalog Federation, Lakebase.
- **L2 의미(지표) ●** — Metric Views GA, Spark 오픈소스화 진행(SPARK-54119), Apache Ossie 참여.
- **L3 관계·정체성 ◐** — 메트릭 뷰 간 관계(Beta), Genie Ontology가 개념·지표·테이블·팀 간 관계를 다룬다고 하나 공식 문서엔 엔티티·관계 모델 설명이 없음. 엔티티 해석(ID 매핑) 제품 없음.
- **L4 절차·역할 ◐** — Genie Agents의 지침·큐레이션, 공유 가능한 에이전트 스킬. 승인 체인·플레이북 제품은 없음.
- **L5 기억·이력 ●** — Lakebase 기반 Agent Memory Service, Genie Ontology 스니펫의 출처·계보 인용, Unity Catalog 리니지.
- **L6 런타임 창 관리 ●** — Genie Ontology의 권위 점수(OntoRank)로 맥락 선별, Supervisor Agent 멀티에이전트, Genie One.
- **L7 실행·검증 ●** — Genie One MCP 액션, Genie Code 실행, Sandbox, LLM 가드레일(Beta).
- **GOV ●** — Unity Catalog 권한(MCP 포함 항상 적용), Unity AI Gateway 서비스 정책·on-behalf-of 실행.
- **OBS ●** — MLflow 3 트레이싱·평가·운영 모니터링, Gateway 페이로드 로깅, ZeroOps(예정).

## 2026년 주요 움직임 (최신순)
- **2026-11-09** Genie Ontology 문서 갱신: 학습 지식(자동 스니펫) vs 모델링 지식(메트릭 뷰·도메인·Pages·인증 자산) 이원 구조, 충돌 시 모델링 지식 우선.
- **2026-10-16** Genie One·Genie Agents 파일 업로드 GA.
- **2026-08-03** Genie One·Genie Agents 무료 사용 2027-01-31까지 연장.
- **2026-07-08** Genie Spaces → **Genie Agents** 개명 (기능 동일). 7월 하순 Agent mode API Beta.
- **2026-06-16 (DAIS 2026, 6/15–18)** **Genie One** GA, **Genie Ontology** 발표, Genie Code GA, Genie App Builder·ZeroOps 비공개 프리뷰 예정. Agent Bricks를 "모든 모델·하네스" 개발자 플랫폼으로 확장, Databricks Sandbox, Unity Catalog의 MCP 지원(외부 SaaS 연결), Lakebase 기반 Agent Memory Service. 그 밖에 LTAP, Lakehouse//RT, Panther 인수(LakeWatch), OpenSharing.
- **2026-06-01** Vector Search → **AI Search** 개명, 임베딩 없는 전문 검색 인덱스 지원.
- **2026-05-19** Unity AI Gateway: 서비스 정책·LLM 가드레일·MCP 페이로드 로깅·비용 통제 Beta.
- **2026-04-02** Unity Catalog Business Semantics(Metric Views) GA, Apache Ossie 참여 명시, Spark 오픈소스화 예고.
- **2026-02** Lakebase GA(AWS 2/22 전후, Azure 3/2).
- **2026-02-10** Agent Bricks Supervisor Agent GA (2/5 Multi-Agent Supervisor에서 개명).
- **2026-01-13** Agent Bricks Knowledge Assistant GA.

## 경쟁·파트너 관계
- **Snowflake**: 정면 경쟁. Snowflake는 Horizon Context·Cortex Sense, Databricks는 Unity Catalog·Genie Ontology로 같은 "컨텍스트 층" 자리를 놓고 경쟁. 표준(Apache Ossie)에서는 양사 모두 기여.
- **Palantir**: "Ontology" 명칭을 정면으로 차용 — 다만 Genie Ontology는 객체·행동 모델이 아니라 분석 지식 스니펫 중심이라 성격이 다름.
- **Atlan·Timbr 등**: Genie Ontology 비교·연동 해설을 다수 발행(이해관계 있는 2차 출처).
- **에이전트 프레임워크(LangGraph, CrewAI, Agno, Claude Code SDK, OpenAI Agents SDK)**: Agent Bricks가 호스팅·거버넌스 대상으로 수용 — 프레임워크 경쟁 대신 통제면을 장악하는 전략.
- **Microsoft(Azure Databricks)·Google·AWS**: 클라우드 파트너. Azure 문서가 동일 기능을 재게시.
- **Slack·GitHub·Atlassian·Google·Microsoft 365**: 관리형 MCP 외부 커넥터 대상.

## 불확실·확인 못한 것
- **Genie Ontology 상태**: 공식 문서(2026-11-09 갱신)에 프리뷰 배너가 없고 외부 지식원만 Beta. 2차 출처는 Public Preview라고 함 → 미확정. 엔티티·관계(그래프) 구조는 공식 문서에 설명 없음, OntoRank는 2차 출처에만 등장. 커뮤니티에서 "그래프 전체 탐색·학습 변경 이력 diff는 아직 없음"이라는 직원 답변 보고(2차).
- **"Unity Catalog Metrics" 명칭**: 일부 2차 출처가 DAIS 2026 신제품으로 언급하나 공식 문서·보도자료에서는 Metric Views/Business Semantics만 확인. 별도 제품인지 미확인.
- **Unity AI Gateway vs Unity Gateway 명칭·GA 여부**: 블로그는 Beta, 일부 2차 출처는 "기반은 GA". 문서 제목은 "Unity Gateway".
- **MLflow 3 GenAI 기능의 Databricks GA 일자** 미확인.
- **Agent Bricks 자동 최적화(평가 기반 자기 개선)** 기능의 현재 상태 미확인 → 성숙도는 보수적으로 매김.
- **Ossie 지원**: Metric Views의 Ossie import/export 기능은 공식 문서로 확인 못 함(Atlan은 "아직 없음"이라 주장).
- **Lakebase GCP GA** 및 Agent Memory Service의 정식 상태(GA/Preview) 미확인.

## 데이터 블록
```yaml
vendor: databricks
name: Databricks
category: data_platform
products:
  - id: databricks-metric-views
    name: Unity Catalog Business Semantics (Metric Views)
    status: GA
    status_date: 2026-04
    layers: {L2: ●, L3: ◐, GOV: ◐}
    x: -2
    y: -2
    xy_reason: "지표·차원을 사람이 SQL/YAML로 정의해 숫자 질문에 재사용"
    maturity: 1
    evidence:
      - {url: https://www.databricks.com/blog/redefining-semantics-data-layer-future-bi-and-ai, kind: official, date: 2026-04-02}
      - {url: https://docs.databricks.com/aws/en/business-semantics/metric-views, kind: official, date: 2026-11-11}
  - id: databricks-genie-ontology
    name: Genie Ontology
    status: preview
    status_date: 2026-06
    layers: {L2: ●, L3: ◐, L5: ◐, L6: ●, GOV: ◐}
    x: -1
    y: 2
    xy_reason: "분석용 업무 지식이지만, 쿼리·대시보드 사용 흔적에서 자동 추출·갱신하고 권위 점수로 선별"
    maturity: 5
    evidence:
      - {url: https://docs.databricks.com/en/genie/genie-ontology, kind: official, date: 2026-11-09}
      - {url: https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team, kind: official, date: 2026-06-16}
      - {url: https://www.cio.com/article/4186154/from-rag-to-ontology-databricks-bets-on-context-as-the-key-to-trusted-ai-agents-2.html, kind: secondary, date: 2026-06}
  - id: databricks-genie-agents
    name: Genie Agents (formerly Genie Spaces)
    status: GA
    status_date: 2026-07
    layers: {L2: ◐, L4: ●, L5: ◐, L6: ●}
    x: -2
    y: -1
    xy_reason: "데이터 질문용, 대상 테이블·지침·예시 쿼리를 사람이 큐레이션"
    maturity: 2
    evidence:
      - {url: https://docs.databricks.com/gcp/en/release-notes/product/2026/july, kind: official, date: 2026-07-08}
  - id: databricks-genie-one
    name: Genie One
    status: GA
    status_date: 2026-06
    layers: {L4: ◐, L5: ◐, L6: ●, L7: ●}
    x: 1
    y: 1
    xy_reason: "리포트 작성·예약 작업·MCP 액션까지 하는 업무 에이전트, Ontology로 런타임 맥락 획득"
    maturity: 2
    evidence:
      - {url: https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team, kind: official, date: 2026-06-16}
      - {url: https://docs.databricks.com/aws/generative-ai/mcp/managed-mcp, kind: official, date: 2026-11-11}
  - id: databricks-genie-code
    name: Genie Code (+ ZeroOps)
    status: GA
    status_date: 2026-06
    layers: {L6: ●, L7: ●, OBS: ◐}
    x: 1
    y: 1
    xy_reason: "파이프라인·ML 작업을 직접 구현·실행하는 자율 에이전트"
    maturity: 2
    evidence:
      - {url: https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team, kind: official, date: 2026-06-16}
  - id: databricks-agent-bricks
    name: Agent Bricks (Knowledge Assistant, Supervisor Agent, Sandbox)
    status: GA
    status_date: 2026-02
    layers: {L1: ◐, L6: ●, L7: ●, GOV: ◐}
    x: 1
    y: 0
    xy_reason: "범용 에이전트 개발·실행 플랫폼, 도구·하위 에이전트는 개발자가 구성하고 런타임에 라우팅"
    maturity: 3
    evidence:
      - {url: https://www.databricks.com/blog/agent-bricks-dais-2026, kind: official, date: 2026-06-16}
      - {url: https://www.databricks.com/blog/agent-bricks-supervisor-agent-now-ga-orchestrate-enterprise-agents, kind: official, date: 2026-02-10}
      - {url: https://learn.microsoft.com/en-us/azure/databricks/release-notes/product/2026/march, kind: official, date: 2026-03}
  - id: databricks-agent-memory-lakebase
    name: Agent Memory Service (Lakebase)
    status: GA
    status_date: 2026-06
    layers: {L5: ●}
    x: 1
    y: 2
    xy_reason: "에이전트가 실행 중 상태·기억을 스스로 쓰고 다시 읽는 운영 DB"
    maturity: 1
    evidence:
      - {url: https://www.databricks.com/blog/agent-bricks-dais-2026, kind: official, date: 2026-06-16}
      - {url: https://databricks.com/blog/databricks-lakebase-generally-available, kind: official, date: 2026-02}
  - id: databricks-ai-search
    name: AI Search (formerly Vector Search)
    status: GA
    status_date: 2026-06
    layers: {L1: ●, L6: ◐}
    x: -1
    y: 0
    xy_reason: "문서·벡터 검색 인덱스, 인덱스 대상은 사람이 정하고 질의 시 런타임 검색"
    maturity: 1
    evidence:
      - {url: https://docs.databricks.com/aws/en/ai-search/ai-search, kind: official, date: 2026-11-11}
      - {url: https://learn.microsoft.com/azure/databricks/release-notes/product/2026/june, kind: official, date: 2026-06-01}
  - id: databricks-managed-mcp
    name: Managed MCP servers
    status: preview
    status_date: 2026-06
    layers: {L1: ●, L7: ◐, GOV: ●}
    x: 0
    y: -1
    xy_reason: "Genie·SQL 같은 분석 도구와 Slack·GitHub 쓰기 커넥터를 함께 노출, 활성화는 관리자가 결정"
    maturity: 2
    evidence:
      - {url: https://docs.databricks.com/aws/generative-ai/mcp/managed-mcp, kind: official, date: 2026-11-11}
  - id: databricks-unity-ai-gateway
    name: Unity AI Gateway (Unity Gateway)
    status: preview
    status_date: 2026-05
    layers: {L7: ◐, GOV: ●, OBS: ◐}
    x: 1
    y: -1
    xy_reason: "에이전트의 도구 호출·행동을 통제하는 런타임 정책, 정책은 사람이 사전 정의"
    maturity: 4
    evidence:
      - {url: https://databricks.com/blog/whats-new-unity-ai-gateway-service-policies-guardrails-observability-and-cost-controls-ai, kind: official, date: 2026-05-19}
      - {url: https://docs.databricks.com/aws/en/ai-gateway/index/, kind: official, date: 2026-11-11}
  - id: databricks-mlflow3-genai
    name: MLflow 3 GenAI (Tracing, Evaluation, Production monitoring)
    status: GA
    status_date: 2025-06
    layers: {OBS: ●, L7: ◐}
    x: 0
    y: 0
    xy_reason: "용도 중립 관측·평가 도구"
    maturity: 4
    evidence:
      - {url: https://www.databricks.com/blog/mlflow-30-unified-ai-experimentation-observability-and-governance, kind: official, date: 2025-06}
      - {url: https://docs.databricks.com/aws/mlflow3/genai/eval-monitor/production-monitoring, kind: official, date: 2026-11-11}
notes:
  standard: "Apache Ossie(구 OSI) 참여 — 2026-04-02 블로그에서 명시, Metric View 코어를 Apache Spark로 오픈소스화 예정(SPARK-54119)"
  naming: "Genie Spaces→Genie Agents(2026-07-08), Vector Search→AI Search(2026-06-01), Multi-Agent Supervisor→Supervisor Agent(2026-02-05)"
```

## 참고자료 (References)
- DAIS 2026 Genie One 보도자료(2026-06-16): https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team
- Agent Bricks DAIS 2026 블로그: https://www.databricks.com/blog/agent-bricks-dais-2026
- Atlan DAIS 2026 정리(2차, 이해관계 있음): https://atlan.com/know/ai-agent/databricks/databricks-data-ai-summit-2026-announcements/
- Bain DAIS 분석(2차): https://www.bain.com/insights/databricks-data-ai-summit-the-lakehouse-becomes-the-agentic-enterprise-control-plane/
