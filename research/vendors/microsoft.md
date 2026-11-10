# Microsoft — 컨텍스트 엔지니어링 관련 솔루션 (조사일 2026-11-11)

## 한 줄 요약 (이 회사의 전략)
"Microsoft IQ" 라는 하나의 지붕 아래 **Work IQ(사람·협업 맥락) / Fabric IQ(비즈니스 데이터·온톨로지 맥락) / Foundry IQ(문서·정책 지식 맥락) / Web IQ(웹)** 를 나란히 세우고, 그 위의 에이전트(M365 Copilot·Copilot Studio·Foundry)가 같은 맥락을 나눠 쓰게 하며, 아래로는 OneLake·Graph·AI Search 가 원천을, 옆으로는 Entra Agent ID·Agent 365·Purview 가 권한·감사를 받친다. 즉 **스택 전 층을 자사 제품으로 수직 통합**하고, 바깥 에이전트와는 MCP 로 연결하는 전략이다.

## 솔루션 목록
| 제품 | 무엇을 하나(쉬운 말) | 상태(날짜) | 층 | 근거 URL |
|---|---|---|---|---|
| Fabric IQ — Ontology (+ Graph, 온톨로지 에이전트) | 고객·배송·설비 같은 업무 개념과 그 관계·규칙·지표·가능한 행동을 하나의 모델로 정의하고 OneLake 실데이터에 묶음. 시맨틱 모델에서 자동 생성, RDF/OWL 가져오기, 그래프 탐색 지원. Copilot Chat·Cowork 통합은 2026-09-28 GA | Fabric IQ 발표 2025-11(Ignite) → Build 2026(2026-06)에 Fabric IQ GA 보도, **Ontology 항목 자체는 Learn 기준 여전히 Preview**(문서 2026-07-08 갱신) | L3●, L2◐, L4◐, L7◐, L1◐ | https://learn.microsoft.com/en-us/fabric/iq/overview · https://blog.fabric.microsoft.com/en-US/blog/from-data-platform-to-intelligence-platform-introducing-microsoft-fabric-iq/ |
| Power BI 시맨틱 모델 (+ Modeling/Authoring MCP) | 측정값(DAX)·차원·계층으로 "매출" 같은 지표를 한 번 정의. Fabric IQ 의 지표 원천이 되며 MCP 로 에이전트가 스키마 조회·DAX 실행·모델 편집 | 시맨틱 모델 GA / Modeling MCP Server 는 GitHub 기준 Public Preview | L2●, L1◐ | https://learn.microsoft.com/en-us/power-bi/developer/agentic/power-bi-agentic-overview · https://github.com/microsoft/powerbi-modeling-mcp |
| Fabric data agent | 레이크하우스·웨어하우스·시맨틱 모델·KQL·온톨로지 위에서 자연어 질문에 답하는 "가상 분석가". M365·Foundry·Copilot Studio 에 게시, MCP 서버로 노출 | GA 2026-03(FabCon, 2차 자료만 확인) | L6◐, L2◐, L1◐, GOV◐ | https://learn.microsoft.com/en-us/fabric/iq/overview · https://learn.microsoft.com/en-ca/fabric/data-science/data-agent-mcp-server · https://pub.towardsai.net/fabric-data-agents-just-hit-ga-94f459c68dcc |
| Work IQ (API·MCP 서버·CLI) | 메일·회의·문서·Teams·사람 관계 등 "일하는 방식" 신호를 에이전트에 공급. MCP 서버로 외부 코딩 에이전트도 사용. M365 Copilot 의 개인 기억(맞춤 지침·저장 기억·대화 인사이트)을 에이전트가 읽는 경로 추가 예정 | 발표 2025-11(Ignite), CLI/MCP GA 2026-06-16; 메모리 읽기 GA 롤아웃 2026-12 예정(MC1539004, 2026-11-05 공지) | L1●, L5◐, L6◐, GOV◐ | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/cli · https://mc.merill.net/message/MC1539004 · https://learn.microsoft.com/en-us/microsoft-copilot-studio/use-work-iq |
| Copilot connectors (구 Graph connectors) | 외부 SaaS(Jira·Confluence·ServiceNow 등) 콘텐츠를 Microsoft Graph 에 색인(synced)하거나 MCP 로 실시간 조회(federated)해 Copilot 지식으로 편입 | GA(100+ 커넥터); federated 2026-03 출시(2차); Work IQ API 확장 2026-11 말 롤아웃 예정(MC1538999) | L1●, GOV◐ | https://mc.merill.net/message/MC1538999 · https://techcommunity.microsoft.com/t5/microsoft-365-copilot-blog/fueling-new-experiences-in-microsoft-365-copilot-with-expanded/ba-p/4493246 |
| Copilot Studio (knowledge·agent flows·Work IQ/Foundry IQ 연결) | 로우코드 에이전트 빌더. SharePoint·Dataverse·SQL 등 지식 원천 연결, 지식 원천 동적 필터, 결정론적 agent flow, Foundry IQ 지식베이스 연결 | GA(플랫폼); Work IQ 도구 Preview; SharePoint lists 지식 GA 2026-05(2차) | L1●, L4●, L7●, L6◐, GOV◐ | https://learn.microsoft.com/en-us/microsoft-copilot-studio/use-work-iq · https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq |
| Foundry IQ / Azure AI Search 에이전틱 검색 | 여러 원천(Blob·SharePoint·OneLake·웹·MCP·Work IQ)을 묶은 "지식베이스". LLM 이 질의를 쪼개 병렬 검색·재랭킹·인용 반환, 호출자 권한·Purview 레이블 반영 | 발표 2025-11, 지식베이스 GA 2026-06(REST 2026-04-01: searchIndex·azureBlob·indexedOneLake·web 소스 GA), 답변합성·다회차·Serverless·기타 소스 Preview | L1●, L6●, GOV●, L5◐ | https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq · https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-how-to-migrate · https://mc.merill.net/message/AZ563222 |
| Foundry Agent Service (Hosted agents·Memory·Toolboxes·평가/트레이싱·가드레일) | 에이전트 실행 런타임. 장기 기억(사용자 프로필·대화 요약·절차 기억), 도구·스킬·MCP 단일 엔드포인트(Toolbox), 루브릭 평가·트레이싱, 가드레일, 운영 트레이스 기반 개선 제안(Agent Optimizer) | Hosted agents GA 예정 2026-07; Memory·Toolbox·Tracing·Rubric Preview(2026-06-02); Agent Optimizer "곧 Preview" | L5●, L7●, L6◐, L4◐, OBS●, GOV◐ | https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-build-2026/ · https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-memory |
| Microsoft Agent Framework (Semantic Kernel·AutoGen 후속) | 오픈소스 에이전트 SDK. 스킬·메모리·미들웨어 하네스, Magentic-One 멀티에이전트 오케스트레이션, 절차 기억 | 하네스 Stable(Build 2026, 2026-06-02); 파일시스템·메모리 도구 Preview | L6●, L4◐, L5◐, L7◐, OBS◐ | https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-build-2026/ · https://mc.merill.net/message/AZ563561 |
| GraphRAG / LazyGraphRAG (오픈소스·MSR) | 문서에서 엔티티·관계 그래프와 커뮤니티 요약을 뽑아 질의에 활용. Lazy 버전은 색인 비용을 벡터 RAG 수준으로 낮춤 | OSS(1.0 이후 지속 릴리스); Azure 솔루션 가속기는 보관(archived), Microsoft Discovery 에 내장 | L3●, L6◐ | https://www.microsoft.com/en-us/research/blog/moving-to-graphrag-1-0-streamlining-ergonomics-for-developers-and-users/ · https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/ |
| Microsoft Purview (DSPM for AI·DLP·감사) | 에이전트를 1급 대상으로 보고 민감 데이터 노출·프롬프트 위험을 탐지, 감사·eDiscovery·보존, Copilot Studio 프롬프트 인라인 DLP | DSPM 통합 경험 GA 2026-05(2차), 인라인 DLP Preview(2026-03~) | GOV●, OBS◐, L5◐ | https://learn.microsoft.com/purview/ai-copilot-studio · https://techcommunity.microsoft.com/blog/microsoft-purview-blog/data-security-posture-management-for-ai/4484148 |
| Entra Agent ID + Agent 365 | 에이전트마다 고유 신원·후원자·수명주기 부여, 조건부 접근·위험 차단, 접근 패키지. Agent 365 는 전사 에이전트 레지스트리·통제판 | Agent ID 발표 2025-05(Build)·확대 Preview 2025-11, Agent ID·Agent 365 GA 2026-05-01; 에이전트용 CA/ID Protection 플랜 GA 2026-07~08 | GOV●, OBS◐ | https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id · https://mc.merill.net/message/MC1395007 |

## 회사 전체 층 커버리지
- **L1 연결·원천 ●** — OneLake(shortcut·mirroring), Graph+Copilot connectors(synced/federated MCP), AI Search 색인, Work IQ MCP, 제품 대부분이 MCP 서버/클라이언트 제공.
- **L2 의미(지표) ●** — Power BI 시맨틱 모델이 사실상 업계 최대 설치 기반의 지표 층. 온톨로지가 DAX 측정값을 그대로 지표로 가져감.
- **L3 관계·정체성 ●** — Fabric IQ Ontology + Graph(Preview 위주), GraphRAG(OSS). 엔티티 해석(ID 매핑) 전용 기능은 문서상 약함.
- **L4 절차·역할 ◐** — 온톨로지 규칙(자연어), Copilot Studio agent flow, Agent Framework 스킬, Foundry 절차 기억. 전사 플레이북 저장소 같은 독립 제품은 없음.
- **L5 기억·이력 ●** — Foundry Memory(3종), Copilot Memory, Work IQ 메모리 읽기. 계보는 Purview 쪽.
- **L6 런타임 창 관리 ●** — 에이전틱 검색(질의 분해·병렬·재랭킹·추론 강도), Agent Framework 오케스트레이션, Toolbox 도구 검색.
- **L7 실행·검증 ●** — Foundry hosted agents, Copilot Studio 액션·flow, Operations agent·Activator 연동 행동, 가드레일(ACS).
- **GOV ●** — Entra Agent ID, Agent 365, Purview, 질의시점 ACL·레이블 집행. 5대 벤더 중 가장 두꺼움.
- **OBS ●** — Foundry 트레이싱·루브릭 평가·ASSERT(OSS), Agent Optimizer(예정), Purview 감사. 데이터 신선도 감시는 freshness-aware 검색(Preview) 수준.

## 2026년 주요 움직임 (최신순)
- **2026-11-17~20 (예정)** Ignite 2026(샌프란시스코). 조사일 기준 미개최 — 발표 내용 없음.
- **2026-11-05** MC1539004: Work IQ MCP 에 사용자 Copilot 기억 읽기 전용 경로(`/memory/me/coreMemories`) 추가, 2026-12 GA 롤아웃 예정. MC1538999: Copilot connectors 를 Work IQ API 로 확장(11월 말).
- **2026-10** Copilot connectors 관리가 Agent 365 의 "허용 에이전트 유형" 설정으로 통합(2차), Copilot Studio 내 Foundry IQ 연결 GA 보도(Redmond, 2차).
- **2026-09-28** Fabric IQ 의 Copilot Chat·Cowork 통합 GA, IQ Sharing Preview (Microsoft 공식 블로그).
- **2026-08** AI Search `2026-08-01-preview`: Work IQ 지식 원천 인증 변경, MCP 서버 지식 원천 결과 처리 옵션.
- **2026-06-16** Work IQ CLI/MCP GA.
- **2026-06-02~04 (Build 2026)** Foundry IQ 지식베이스 GA, Foundry Memory 에 절차 기억 추가, Toolboxes·Routines Preview, Agent Framework 하네스 Stable, 트레이싱·평가를 타 프레임워크로 확장, Agent Control Specification·ASSERT 오픈소스. Fabric IQ GA 보도(온톨로지는 Preview 유지).
- **2026-05-01** Entra Agent ID GA, Agent 365 GA. Purview DSPM 통합 경험 GA(2차).
- **2026-04** AI Search REST `2026-04-01` 로 에이전틱 검색 일부 GA.
- **2026-03** FabCon: Fabric data agent GA, 온톨로지 규칙의 Activator 연동(2차). Federated Copilot connectors(MCP 기반) 출시(2차).
- (기준점) **2025-11-18 Ignite 2025**: Work IQ·Fabric IQ·Foundry IQ 세 IQ 와 Agent 365 첫 발표.

## 경쟁·파트너 관계
- **경쟁**: 온톨로지+행동(Fabric IQ Ontology·Operations agent)은 Palantir Foundry Ontology 와 정면 경쟁. 지표 층은 Snowflake Semantic Views·Databricks Metric Views·dbt/OSI 진영과 경쟁. Foundry IQ·Memory 는 AWS Bedrock Knowledge Bases/AgentCore Memory, Google Vertex/Agentspace 와 같은 자리. Work IQ 는 Google Workspace·Glean 의 "업무 그래프"와 경쟁.
- **파트너/개방**: Agent Framework 가 Claude Agent SDK·GitHub Copilot SDK 를 통합, Foundry hosted agents 는 LangGraph 등 타 프레임워크 수용. Entra Agent ID 는 AWS Bedrock·n8n 에이전트에도 신원 부여 가이드 제공. 온톨로지 RDF/OWL 가져오기, 전 제품 MCP 지원으로 바깥 에이전트 접속 허용. OpenAI 모델이 에이전틱 검색의 질의 계획·답변 합성에 쓰임.

## 불확실·확인 못한 것
- **Fabric IQ "GA" 범위**: 2차 자료는 Build 2026 GA 라 하지만 Learn 은 Ontology·IQ 워크로드를 여전히 Preview 로 표기. Microsoft 원 공지(블로그) 미확인.
- **Fabric data agent GA(2026-03)**, Graph·Operations agent GA(2026-06) — 2차 자료/로드맵 사이트만 확인.
- **온톨로지 MCP 엔드포인트** 상태(Preview/예정) 자료 간 충돌.
- **Hosted agents GA** 실제 도달 여부(7월 예정만 공식 확인).
- **Agent Framework 1.0 정확한 날짜**, Semantic Kernel 의 공식 지위(유지보수 모드 여부) 미확인.
- **Purview DSPM 통합 GA(2026-05)** 날짜는 2차 자료.
- **Copilot connectors federated(MCP) 출시 시점** 2차 자료.
- **GraphRAG 2026 최신 버전**(3.x 보도) GitHub 릴리스 직접 확인 실패.
- Ignite 2026 발표는 조사일 이후라 반영 불가.

## 데이터 블록
```yaml
vendor: microsoft
name: Microsoft
category: hyperscaler
products:
  - id: microsoft-fabric-iq-ontology
    name: Fabric IQ Ontology (+ Graph, ontology agent)
    status: preview
    status_date: 2026-07
    layers: {L1: ◐, L2: ◐, L3: ●, L4: ◐, L7: ◐, GOV: ◐}
    x: 1
    y: -1
    xy_reason: "엔티티·관계·규칙·행동을 모델링해 운영 행동까지 잇지만, 온톨로지 자체는 사람이 정의·승인(proposal-first)하는 큐레이션형"
    maturity: 3
    evidence:
      - {url: "https://learn.microsoft.com/en-us/fabric/iq/overview", kind: official, date: 2026-07-08}
      - {url: "https://blog.fabric.microsoft.com/en-US/blog/from-data-platform-to-intelligence-platform-introducing-microsoft-fabric-iq/", kind: official, date: 2025-11-18}
      - {url: "https://pub.towardsai.net/fabric-iq-is-ga-mostly-46bedac669d8", kind: secondary, date: 2026-06}
  - id: microsoft-powerbi-semantic-model
    name: Power BI semantic model (+ Modeling/Authoring MCP)
    status: GA
    status_date: 2026-06
    layers: {L1: ◐, L2: ●}
    x: -2
    y: -2
    xy_reason: "측정값·차원을 모델러가 미리 정의하는 전형적 지표 층"
    maturity: 1
    evidence:
      - {url: "https://learn.microsoft.com/en-us/power-bi/developer/agentic/power-bi-agentic-overview", kind: official, date: 2026-11-11}
      - {url: "https://github.com/microsoft/powerbi-modeling-mcp", kind: official, date: 2026-11-11}
  - id: microsoft-fabric-data-agent
    name: Fabric data agent
    status: GA
    status_date: 2026-03
    layers: {L1: ◐, L2: ◐, L6: ◐, GOV: ◐}
    x: -1
    y: 0
    xy_reason: "주로 숫자 질문에 답하는 분석 에이전트, 사람이 지정한 원천·지침 위에서 런타임 질의 생성"
    maturity: 2
    evidence:
      - {url: "https://learn.microsoft.com/en-ca/fabric/data-science/data-agent-mcp-server", kind: official, date: 2026-11-11}
      - {url: "https://pub.towardsai.net/fabric-data-agents-just-hit-ga-94f459c68dcc", kind: secondary, date: 2026-03}
  - id: microsoft-work-iq
    name: Work IQ (API / MCP / CLI)
    status: GA
    status_date: 2026-06
    layers: {L1: ●, L5: ◐, L6: ◐, GOV: ◐}
    x: 1
    y: 1
    xy_reason: "메일·회의·문서 등 업무 활동 신호를 런타임에 자동 수집해 제공, 사람의 사전 큐레이션 거의 없음"
    maturity: 1
    evidence:
      - {url: "https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/cli", kind: official, date: 2026-09-25}
      - {url: "https://mc.merill.net/message/MC1539004", kind: secondary, date: 2026-11-05}
  - id: microsoft-copilot-connectors
    name: Copilot connectors (synced / federated MCP)
    status: GA
    status_date: 2026-03
    layers: {L1: ●, GOV: ◐}
    x: 0
    y: 0
    xy_reason: "원천 연결 배관으로 성격 중립, 관리자가 커넥터를 켜면 이후 색인·실시간 조회는 자동"
    maturity: 1
    evidence:
      - {url: "https://techcommunity.microsoft.com/t5/microsoft-365-copilot-blog/fueling-new-experiences-in-microsoft-365-copilot-with-expanded/ba-p/4493246", kind: official, date: 2026-02}
      - {url: "https://mc.merill.net/message/MC1538999", kind: secondary, date: 2026-11}
      - {url: "https://blog-en.topedia.com/2026/09/self-serve-sync-connectors-in-microsoft-365-copilot-chat-preview/", kind: secondary, date: 2026-09}
  - id: microsoft-copilot-studio
    name: Copilot Studio (knowledge, agent flows, Work IQ / Foundry IQ tools)
    status: GA
    status_date: 2026-10
    layers: {L1: ●, L4: ●, L6: ◐, L7: ●, GOV: ◐}
    x: 1
    y: -1
    xy_reason: "메이커가 지식 원천·흐름·승인을 미리 구성하는 업무 실행형 빌더"
    maturity: 3
    evidence:
      - {url: "https://learn.microsoft.com/en-us/microsoft-copilot-studio/use-work-iq", kind: official, date: 2026-11-11}
      - {url: "https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq", kind: official, date: 2026-07-31}
      - {url: "https://redmondmag.com/blogs/redmond-dispatch/2026/10/microsoft-makes-foundry-iq-available.aspx", kind: secondary, date: 2026-10}
  - id: microsoft-foundry-iq
    name: Foundry IQ / Azure AI Search agentic retrieval
    status: GA
    status_date: 2026-06
    layers: {L1: ●, L5: ◐, L6: ●, GOV: ●}
    x: 0
    y: 1
    xy_reason: "문서·정책 지식 대상, 원천은 사람이 지정하나 LLM 이 런타임에 질의 분해·원천 선택·재랭킹"
    maturity: 2
    evidence:
      - {url: "https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq", kind: official, date: 2026-07-31}
      - {url: "https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-how-to-migrate", kind: official, date: 2026-08-20}
      - {url: "https://mc.merill.net/message/AZ563222", kind: secondary, date: 2026-06-04}
  - id: microsoft-foundry-agent-service
    name: Foundry Agent Service (hosted agents, Memory, Toolboxes, evals, guardrails)
    status: preview
    status_date: 2026-06
    layers: {L4: ◐, L5: ●, L6: ◐, L7: ●, GOV: ◐, OBS: ●}
    x: 1
    y: 2
    xy_reason: "도구 실행 런타임 + 대화에서 사용자·절차 기억을 자동 추출·통합"
    maturity: 5
    evidence:
      - {url: "https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-build-2026/", kind: official, date: 2026-06-02}
      - {url: "https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-memory", kind: official, date: 2026-06-02}
  - id: microsoft-agent-framework
    name: Microsoft Agent Framework (successor to Semantic Kernel / AutoGen)
    status: GA
    status_date: 2026-06
    layers: {L4: ◐, L5: ◐, L6: ●, L7: ◐, OBS: ◐}
    x: 1
    y: 1
    xy_reason: "개발자용 오케스트레이션 SDK, 스킬·메모리·미들웨어로 런타임 조립"
    maturity: 3
    evidence:
      - {url: "https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-build-2026/", kind: official, date: 2026-06-02}
      - {url: "https://mc.merill.net/message/AZ563561", kind: secondary, date: 2026-06}
  - id: microsoft-graphrag
    name: GraphRAG / LazyGraphRAG (open source)
    status: GA
    status_date: 2024-12
    layers: {L3: ●, L6: ◐}
    x: -1
    y: 1
    xy_reason: "문서에서 그래프·커뮤니티 요약을 자동 추출해 질의 시 활용, 분석·이해용"
    maturity: 1
    evidence:
      - {url: "https://www.microsoft.com/en-us/research/blog/moving-to-graphrag-1-0-streamlining-ergonomics-for-developers-and-users/", kind: official, date: 2024-12}
      - {url: "https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/", kind: official, date: 2024-11}
  - id: microsoft-purview-ai
    name: Microsoft Purview (DSPM for AI, DLP, audit)
    status: GA
    status_date: 2026-05
    layers: {L5: ◐, GOV: ●, OBS: ◐}
    x: 0
    y: -1
    xy_reason: "보안 관리자가 정책을 미리 정의하고 에이전트 상호작용을 감시"
    maturity: 3
    evidence:
      - {url: "https://learn.microsoft.com/purview/ai-copilot-studio", kind: official, date: 2026-11-11}
      - {url: "https://techcommunity.microsoft.com/blog/microsoft-purview-blog/data-security-posture-management-for-ai/4484148", kind: official, date: 2026}
      - {url: "https://blog.admindroid.com/new-data-security-posture-management-experience-in-microsoft-purview/", kind: secondary, date: 2026}
  - id: microsoft-entra-agent-id
    name: Entra Agent ID + Agent 365
    status: GA
    status_date: 2026-05
    layers: {GOV: ●, OBS: ◐}
    x: 1
    y: -1
    xy_reason: "행동하는 에이전트의 신원·권한·후원자를 사전에 정의·집행"
    maturity: 3
    evidence:
      - {url: "https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id", kind: official, date: 2026-05-01}
      - {url: "https://mc.merill.net/message/MC1395007", kind: secondary, date: 2026}
```
