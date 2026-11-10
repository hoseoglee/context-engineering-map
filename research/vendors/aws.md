# AWS — 컨텍스트 엔지니어링 관련 솔루션 (조사일 2026-11-11)

## 한 줄 요약 (이 회사의 전략)
AWS는 **에이전트 실행 인프라(Bedrock AgentCore)를 레고 블록처럼 잘게 나눠 파는 것**이 중심이다. Runtime·Memory·Gateway·Identity·Policy(Cedar)·Observability·Evaluations·Registry를 따로 고를 수 있고, 2026년 내내 거의 매주 기능이 붙었다. 데이터 쪽 컨텍스트는 늦게 출발했다. 2026-06 뉴욕 서밋에서 **AWS Context**(기존 데이터를 자동으로 지식그래프로 묶고, 에이전트가 쓰는 조인 경로를 학습하는 서비스, "coming soon")와 Glue Data Catalog 비즈니스 컨텍스트(Preview), S3 Annotations(GA)를 내놓으며 Google Knowledge Catalog·Snowflake·Databricks를 쫓기 시작했다. 같은 시기 1세대 제품(Amazon Q Business·Kendra·Bedrock Agents)은 2026-07-30부터 신규 고객을 받지 않는 유지보수 모드로 돌리고, 그 자리를 Amazon Quick·Bedrock Managed Knowledge Base·AgentCore로 옮겼다.

## 솔루션 목록
| 제품 | 무엇을 하나(쉬운 말) | 상태(날짜) | 층 | 근거 URL |
|---|---|---|---|---|
| AWS Context | 회사의 기존 데이터 사이 관계를 자동으로 찾아 지식그래프로 만들고 에이전트용 검색(API·MCP)을 제공. 데이터 담당자가 추론된 관계를 검토·승격하고 업무 규칙을 붙임. 에이전트가 실제로 쓰는 조인 경로·규칙을 추적해 조직 전체에 퍼뜨림. 호출자의 IAM·Lake Formation 권한을 그대로 상속하고 접근 기록을 남김 | Coming soon(2026-06-17 발표, 2026-11 시점에도 미출시로 보도) | L2◐ L3● L5◐ L6◐ GOV● | https://aws.amazon.com/blogs/machine-learning/context-intelligence-for-your-data-and-ai-agents-at-scale/ |
| Glue Data Catalog 비즈니스 컨텍스트·시맨틱 검색 + SageMaker Catalog (Unified Studio) | 표·열에 업무 설명·용어집·사용자 메타데이터를 붙이고 "의미로" 검색. AI 에이전트가 용어집 용어를 자동 추천, 필수 용어 없으면 게시 차단. 런북·가이드를 가리키는 "skill asset". SageMaker Data Agent가 이 비즈니스 컨텍스트로 SQL·Python 생성 | Glue 비즈니스 컨텍스트·skill asset Preview(2026-06-17), SageMaker Catalog 용어 자동분류(2025-11), IAM 도메인 지원(2026-05), Data Agent 연동(2026-06) | L2● L4◐ GOV● | https://aws.amazon.com/blogs/machine-learning/context-intelligence-for-your-data-and-ai-agents-at-scale/ , https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-sagemaker-data-agent-bdc/ , https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-sagemaker-catalog-automatic-data-classification-ai-agents |
| S3 Vectors + S3 Annotations | S3에 벡터를 직접 저장·검색(저비용 RAG 저장소). 객체마다 최대 1GB의 업무 맥락을 붙여 두고 Iceberg 표로 질의, S3 Tables MCP로 에이전트가 찾음 | S3 Vectors GA(2025-12-02), S3 Annotations GA(2026-06-17) | L1● L2◐ | https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-s3-vectors-generally-available , https://aws.amazon.com/blogs/machine-learning/context-intelligence-for-your-data-and-ai-agents-at-scale/ |
| Amazon Bedrock Knowledge Bases (Managed KB·GraphRAG·구조화 데이터) | 문서를 색인해 검색 근거로 제공. Neptune Analytics로 엔터티·관계 그래프를 자동 생성해 벡터+그래프 탐색(GraphRAG), Redshift 등에 자연어→SQL. 2026-06 완전관리형 Managed KB와 질의 계획·재랭킹을 하는 agentic retrieval 추가 | GraphRAG GA(2025-03-07), 구조화 데이터 출시(2024-12), Managed KB GA(2026-06-17) | L1● L3◐ L6● L7◐ GOV◐ | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-managed-knowledge-base/ , https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-bedrock-knowledge-bases-graphrag-generally-available , https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-bedrock-knowledge-bases-structured-data-retrieval |
| Amazon Neptune / Neptune Analytics | 그래프 DB(트랜잭션용 Database, 분석·벡터용 Analytics). Bedrock GraphRAG의 저장소 역할 | GA(기존). Analytics 리전 확대(2026-01·02) | L3● L1◐ | https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-graphs.html , https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-neptune-analytics-generally-available-additional-regions/ |
| AgentCore Runtime + Harness | 에이전트를 microVM에서 장시간·격리 실행. Harness는 메모리·스킬 카탈로그·도구 호출 전후 훅(before_tool_call 등)을 갖춘 관리형 에이전트 루프. Browser·Code Interpreter 내장 도구 | AgentCore GA(2025-10), Harness GA(2026-06), 훅(2026-09) | L4◐ L6● L7● OBS◐ | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html |
| AgentCore Memory | 단기(대화 이벤트)·장기 기억. 의미·선호·요약 전략에 더해 "에피소드" 전략은 끝난 작업을 묶고 여러 에피소드에서 교훈(reflection)을 뽑음. 2026년 메타데이터 필터, 직접 수집, JSON 이벤트, 기억 만료(TTL) 추가 | GA(2025-10), episodic(2025-12), 직접 수집(2026-08~09), TTL(2026-10) | L5● L6◐ | https://aws.amazon.com/about-aws/whats-new/2026/09/agentcore-memory-direct-ingest , https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html |
| AgentCore Gateway + Identity + AWS Agent Registry | 기존 API·Lambda·Step Functions를 MCP 도구로 바꿔 한 곳에서 노출, 모델 라우팅·폴백·속도 제한. Identity는 OAuth·대리 토큰(OBO)·사용자 동의. Registry는 조직 전체 에이전트·도구 목록 | Gateway·Identity GA(2025-10), Registry GA(2026-08), Gateway 모델 폴백(2026-10) | L1● L6◐ GOV● | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html |
| AgentCore Policy (Cedar) + Bedrock Guardrails + Automated Reasoning checks | 게이트웨이에서 모든 도구 호출을 Cedar 정책(자연어로 작성 가능)으로 실시간 허용/거부. Guardrails는 입·출력 필터, Automated Reasoning은 정형 논리로 답변이 규칙에 맞는지 검증 | Policy GA(2026-03-03), Policy+Guardrails(2026-06-17), Automated Reasoning GA(2025-08-06) | L7● GOV● | https://aws.amazon.com/about-aws/whats-new/2026/03/policy-amazon-bedrock-agentcore-generally-available , https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-policy-guardrails-generally-available , https://aws.amazon.com/about-aws/whats-new/2025/08/automated-reasoning-checks-amazon-bedrock-guardrails |
| AgentCore Observability + Evaluations (+ Recommendations·A/B·최적화 루프) | 실행 추적, 13개 내장 평가기·사용자 정의 LLM 판정·스킬 선택 정확도 평가, 실패 분석, 배치 평가·A/B 테스트, 개선 추천 | Evaluations GA(2026-03-31), Recommendations·Batch Eval·A/B GA(2026-06), 최적화 루프 Preview(2026-04) | L4◐ OBS● | https://aws.amazon.com/about-aws/whats-new/2026/03/agentcore-evaluations-generally-available , https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html |
| Amazon Quick (구 Quick Suite, Q Business 후속) | 직원용 에이전트 작업공간. 연결된 앱·폴더에서 사람·프로젝트·결정·용어를 뽑아 **사용자별 지식그래프**를 자동 구축, 대화에서 배운 사실·선호는 Memories로 저장. Quick Index·Flows·Automate·Research, 기존 Q Business 색인 연결(BYOI) | Quick Suite 출시(2025-10-09), Amazon Quick으로 개명(2026-02경, 2차), 지식그래프 문서 확인(2026-11) | L1● L2◐ L3● L4◐ L5● L7◐ GOV◐ | https://docs.aws.amazon.com/quick/latest/userguide/knowledge-graph-desktop.html , https://aws.amazon.com/blogs/business-intelligence/reimagine-business-intelligence-amazon-quicksight-evolves-to-amazon-quick-suite , https://docs.aws.amazon.com/quicksuite/latest/userguide/qbiz-indexes-overview.html |
| AWS MCP Server + Agent Toolkit for AWS | 원격 관리형 MCP 서버 하나로 15,000+ AWS API 호출(call_aws), 최신 문서 검색, IAM 권한 그대로의 샌드박스 스크립트 실행. 40+ AWS 관리 스킬(구 Agent SOP)과 플러그인. CloudTrail 감사, 사람·에이전트 권한 분리 | GA(2026-05-06), re:Invent 2025 프리뷰 | L1● L4● L7● GOV● OBS◐ | https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available , https://aws.amazon.com/about-aws/whats-new/2026/05/agent-toolkit |

## 회사 전체 층 커버리지
- **L1 연결·원천 ●**: AWS MCP Server, AgentCore Gateway(API→MCP), Bedrock KB 커넥터, S3 Vectors, Quick 통합. 가장 두텁다.
- **L2 의미 ◐**: Glue/SageMaker Catalog 용어집·비즈니스 메타데이터(대부분 Preview). Looker·LookML급 지표 시맨틱 레이어는 없음(Quick Sight topics 정도).
- **L3 관계 ●(발표 기준) / ◐(출시 기준)**: Neptune·GraphRAG는 GA지만 기업 전체 그래프인 AWS Context는 coming soon. Quick의 사용자별 그래프는 출시.
- **L4 절차 ◐~●**: Agent Toolkit 스킬, Glue skill asset(Preview), Harness 스킬 카탈로그. 업무 절차·승인 체인 모델링은 약함.
- **L5 기억 ●**: AgentCore Memory(episodic·reflection), Quick Memories. 결정/출처 이력은 AWS Context 감사 기록(미출시).
- **L6 런타임 창 ◐~●**: Managed KB agentic retrieval·재랭킹, Gateway 모델 라우팅, Runtime 세션. 토큰 예산·압축 전용 기능은 확인 못함.
- **L7 실행·검증 ●**: Runtime·Code Interpreter·Browser, call_aws/run_script, Guardrails, Automated Reasoning(정형 검증은 경쟁사에 드문 강점).
- **GOV ●**: Cedar Policy, Identity(OBO·동의), Registry, IAM·Lake Formation 상속, CloudTrail.
- **OBS ●**: AgentCore Observability·Evaluations·A/B·Recommendations.

## 2026년 주요 움직임 (최신순)
- 2026-11: AgentCore Gateway Web Answer 커넥터 GA, Runtime이 MCP 2026-07-28 사양 지원.
- 2026-10: Gateway 모델 폴백·속도 제한, Step Functions를 MCP 도구로, Memory 기억 TTL, AgentCore CLI 1.0, Evaluations 실패 분석.
- 2026-09: Memory 장기기억 직접 수집 GA(What's New 2026-09), Harness 수명주기 훅, Identity 동의 포털.
- 2026-08: AWS Agent Registry GA, Memory JSON 이벤트 추출, 스킬 평가기.
- 2026-07-30: Amazon Q Business·Amazon Kendra·Bedrock Agents(→"Agents Classic") 신규 고객 차단(유지보수 모드).
- 2026-06-17 (뉴욕 서밋): AWS Context 발표(coming soon), Glue 비즈니스 컨텍스트·시맨틱 검색 Preview, S3 Annotations GA, Bedrock Managed Knowledge Base GA, AgentCore Policy에 Guardrails 통합, Harness·Recommendations·A/B GA.
- 2026-05-06: AWS MCP Server·Agent Toolkit for AWS GA.
- 2026-04: AgentCore Registry·Harness Preview, OBO 토큰 교환, Memory 메타데이터 필터.
- 2026-03: AgentCore Policy GA(03-03), Evaluations GA(03-31).
- 2026-02경: Quick Suite → Amazon Quick 개명(2차 보도).
- 참고: re:Invent 2025(2025-12-02)에 Policy·Evaluations Preview, episodic memory, S3 Vectors GA 발표. **re:Invent 2026은 조사일(11-11) 기준 아직 열리지 않음.**

## 경쟁·파트너 관계
- **경쟁**: AWS Context ↔ Google Knowledge Catalog·Snowflake·Databricks·Microsoft 컨텍스트 레이어(TechTarget는 이들을 같은 범주로 묶음). AgentCore ↔ Google Agent Platform·Azure AI Foundry. Quick ↔ Gemini Enterprise·Microsoft 365 Copilot.
- **파트너/개방**: AgentCore Evaluations가 Google ADK·Claude Agent SDK·OpenAI Agents·LangGraph 등 타사 프레임워크 지원, DeepEval 등 외부 평가기. AWS MCP Server는 Claude Code·Cursor·Kiro·Codex와 호환. SageMaker Catalog는 Alation과 메타데이터 동기화. A2A 리눅스재단 프로젝트 창립 멤버(2차).

## 불확실·확인 못한 것
- AWS Context의 정확한 상태: AWS 공식 블로그는 "Coming soon", 일부 분석사(Futurum)는 "preview"로 표기. 가격·리전·출시일 없음. 자기학습 효과는 벤더 주장.
- Bedrock KB 구조화 데이터(Redshift) 기능의 공식 "GA" 표기 미발견(2024-12 출시 공지만).
- Amazon Quick 개명의 공식 공지 미발견(파트너 블로그·문서 변경으로만 확인). Quick 지식그래프 기능의 출시일 미확인.
- AgentCore Memory episodic 전략의 GA 시점 미확인.
- "Graphs for AI"(Neptune이 에이전트 장기기억 제공) 표현은 2차 출처만.
- Kendra GenAI Index의 2026년 위치(유지보수 모드 대상인 Kendra에 포함되는지) 불명.

## 데이터 블록
> evidence의 date는 원문 게시일. 게시일을 못 찾은 문서 페이지는 열람일(2026-11-11)로 적었다.

```yaml
vendor: aws
name: Amazon Web Services
category: hyperscaler
products:
  - id: aws-context
    name: AWS Context
    status: announced
    status_date: 2026-06
    layers: {L2: ◐, L3: ●, L5: ◐, L6: ◐, GOV: ●}
    x: -1
    y: 1
    xy_reason: "데이터 관계·업무 규칙 중심. 관계를 자동 추론하고 에이전트 사용 패턴으로 학습하되 담당자 검토로 승격"
    maturity: 5
    notes: "maturity 5는 발표된 자기학습 기능 기준(미출시)"
    evidence:
      - {url: https://aws.amazon.com/blogs/machine-learning/context-intelligence-for-your-data-and-ai-agents-at-scale/, kind: official, date: 2026-06-17}
      - {url: https://www.techtarget.com/searchdatamanagement/news/366644853/AWS-latest-to-introduce-context-layer-for-agentic-AI, kind: secondary, date: 2026-06-17}
  - id: aws-glue-sagemaker-catalog
    name: Glue Data Catalog 비즈니스 컨텍스트 + SageMaker Catalog
    status: preview
    status_date: 2026-06
    layers: {L2: ●, L4: ◐, GOV: ●}
    x: -1
    y: -1
    xy_reason: "용어집·비즈니스 메타데이터를 사람이 관리하고 AI가 추천을 보조"
    maturity: 2
    evidence:
      - {url: https://aws.amazon.com/blogs/machine-learning/context-intelligence-for-your-data-and-ai-agents-at-scale/, kind: official, date: 2026-06-17}
      - {url: https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-sagemaker-data-agent-bdc/, kind: official, date: 2026-11-11}
      - {url: https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-sagemaker-catalog-automatic-data-classification-ai-agents, kind: official, date: 2026-11-11}
      - {url: https://aws.amazon.com/about-aws/whats-new/2026/05/sagemaker-catalog-iam-domains/, kind: official, date: 2026-11-11}
  - id: aws-s3-vectors-annotations
    name: S3 Vectors + S3 Annotations
    status: GA
    status_date: 2026-06
    layers: {L1: ●, L2: ◐}
    x: -1
    y: -2
    xy_reason: "저장소 원자재. 맥락은 사람이 객체에 붙임"
    maturity: 1
    evidence:
      - {url: https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-s3-vectors-generally-available, kind: official, date: 2025-12-02}
      - {url: https://aws.amazon.com/blogs/machine-learning/context-intelligence-for-your-data-and-ai-agents-at-scale/, kind: official, date: 2026-06-17}
  - id: aws-bedrock-knowledge-bases
    name: Amazon Bedrock Knowledge Bases (Managed KB, GraphRAG, 구조화 데이터)
    status: GA
    status_date: 2026-06
    layers: {L1: ●, L3: ◐, L6: ●, L7: ◐, GOV: ◐}
    x: -1
    y: 0
    xy_reason: "문서·표 검색 근거 제공. 색인은 사전 구성, agentic retrieval은 질의 시 계획·재랭킹"
    maturity: 1
    evidence:
      - {url: https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-managed-knowledge-base/, kind: official, date: 2026-06-17}
      - {url: https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-bedrock-knowledge-bases-graphrag-generally-available, kind: official, date: 2025-03-07}
      - {url: https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-bedrock-knowledge-bases-structured-data-retrieval, kind: official, date: 2024-12-04}
  - id: aws-neptune
    name: Amazon Neptune / Neptune Analytics
    status: GA
    status_date: null
    layers: {L1: ◐, L3: ●}
    x: 0
    y: -2
    xy_reason: "그래프 저장·질의 엔진. 모델링은 사람(또는 Bedrock GraphRAG 자동 추출)"
    maturity: 1
    notes: "오래된 GA 제품, GA 월은 조사 범위 밖이라 비움"
    evidence:
      - {url: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-graphs.html, kind: official, date: 2026-11-11}
      - {url: https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-neptune-analytics-generally-available-additional-regions/, kind: official, date: 2026-11-11}
  - id: aws-agentcore-runtime
    name: AgentCore Runtime + Harness
    status: GA
    status_date: 2026-06
    layers: {L4: ◐, L6: ●, L7: ●, OBS: ◐}
    x: 2
    y: 1
    xy_reason: "도구 실행·장기 실행 에이전트 인프라. 런타임에 에이전트가 스스로 도구를 고름"
    maturity: 3
    notes: "도구 호출 전 훅(before_tool_call)으로 승인 게이트 구성 가능"
    evidence:
      - {url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html, kind: official, date: 2026-11-11}
  - id: aws-agentcore-memory
    name: AgentCore Memory
    status: GA
    status_date: 2025-10
    layers: {L5: ●, L6: ◐}
    x: 1
    y: 2
    xy_reason: "대화·이벤트에서 기억을 자동 추출, episodic 전략은 여러 에피소드에서 교훈을 생성"
    maturity: 5
    evidence:
      - {url: https://aws.amazon.com/about-aws/whats-new/2026/09/agentcore-memory-direct-ingest, kind: official, date: 2026-09-08}
      - {url: https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-bedrock-agentcore-policy-evaluations-preview, kind: official, date: 2025-12-02}
      - {url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html, kind: official, date: 2026-11-11}
  - id: aws-agentcore-gateway-identity-registry
    name: AgentCore Gateway + Identity + AWS Agent Registry
    status: GA
    status_date: 2026-08
    layers: {L1: ●, L6: ◐, GOV: ●}
    x: 1
    y: -1
    xy_reason: "도구 연결·권한 위임 인프라. 도구 목록과 권한은 관리자가 사전 정의"
    maturity: 2
    evidence:
      - {url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html, kind: official, date: 2026-11-11}
  - id: aws-policy-guardrails
    name: AgentCore Policy (Cedar) + Bedrock Guardrails + Automated Reasoning checks
    status: GA
    status_date: 2026-03
    layers: {L7: ●, GOV: ●}
    x: 1
    y: -2
    xy_reason: "행동(도구 호출)과 출력 검증 규칙을 사람이 사전에 정책으로 작성"
    maturity: 4
    evidence:
      - {url: https://aws.amazon.com/about-aws/whats-new/2026/03/policy-amazon-bedrock-agentcore-generally-available, kind: official, date: 2026-03-03}
      - {url: https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-policy-guardrails-generally-available, kind: official, date: 2026-06-17}
      - {url: https://aws.amazon.com/about-aws/whats-new/2025/08/automated-reasoning-checks-amazon-bedrock-guardrails, kind: official, date: 2025-08-06}
  - id: aws-agentcore-obs-evals
    name: AgentCore Observability + Evaluations (Recommendations, A/B)
    status: GA
    status_date: 2026-03
    layers: {L4: ◐, OBS: ●}
    x: 1
    y: 0
    xy_reason: "에이전트 행동 품질 측정. 평가 기준은 사람, 실패 분석·추천은 자동"
    maturity: 4
    evidence:
      - {url: https://aws.amazon.com/about-aws/whats-new/2026/03/agentcore-evaluations-generally-available, kind: official, date: 2026-03-31}
      - {url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html, kind: official, date: 2026-11-11}
  - id: aws-quick
    name: Amazon Quick (구 Quick Suite / Q Business 후속)
    status: GA
    status_date: 2025-10
    layers: {L1: ●, L2: ◐, L3: ●, L4: ◐, L5: ●, L7: ◐, GOV: ◐}
    x: 1
    y: 1
    xy_reason: "직원 업무 실행형 비서. 연결 앱에서 사용자별 지식그래프·기억을 자동 축적"
    maturity: 5
    evidence:
      - {url: https://docs.aws.amazon.com/quick/latest/userguide/knowledge-graph-desktop.html, kind: official, date: 2026-11-11}
      - {url: https://aws.amazon.com/blogs/business-intelligence/reimagine-business-intelligence-amazon-quicksight-evolves-to-amazon-quick-suite, kind: official, date: 2025-10-09}
      - {url: https://docs.aws.amazon.com/quicksuite/latest/userguide/qbiz-indexes-overview.html, kind: official, date: 2026-11-11}
      - {url: https://aws.amazon.com/about-aws/whats-new/2026/06/aws-service-availability/, kind: official, date: 2026-11-11}
  - id: aws-mcp-server
    name: AWS MCP Server + Agent Toolkit for AWS
    status: GA
    status_date: 2026-05
    layers: {L1: ●, L4: ●, L7: ●, GOV: ●, OBS: ◐}
    x: 2
    y: -1
    xy_reason: "AWS 자원을 직접 조작(쓰기)하는 도구. 스킬은 AWS가 사전 큐레이션"
    maturity: 2
    evidence:
      - {url: https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available, kind: official, date: 2026-05-06}
      - {url: https://aws.amazon.com/about-aws/whats-new/2026/05/agent-toolkit, kind: official, date: 2026-05-06}
```
