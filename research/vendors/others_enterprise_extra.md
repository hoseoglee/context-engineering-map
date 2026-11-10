# 기타 전사(enterprise) 규모 컨텍스트 플랫폼 — 추가 조사 (조사일 2026-11-11)

범위: 회사 전체의 데이터·의미·지식·권한을 여러 에이전트와 사용자에게 **만들어 주고, 저장하고, 제공하고, 통제하는** 제품만 다룬다. 에이전트 SDK, 에이전트 하나의 기억, 프롬프트·컨텍스트 창 관리, 에이전트 추적 도구는 뺐다. 다른 파일에서 다룬 회사도 뺐다.

| 회사 | 분류 | 전사 규모 컨텍스트인 이유 |
|---|---|---|
| Denodo | data_platform (논리 데이터 계층) | 데이터를 옮기지 않고 회사 전체 원천을 가상화하고, 같은 의미와 정책을 MCP로 모든 에이전트에 공유 서비스로 제공 |
| Starburst | data_platform (페더레이션 레이크하우스) | 여러 클라우드에 흩어진 데이터를 연합 질의하고, 규칙이 담긴 "AI-Ready 데이터 제품"을 공통 컨텍스트 계층으로 둠 |
| Teradata | data_platform | 전사 분석 DB 위에 벡터 저장소·MCP·에이전트 런타임과 의미·계보를 묶은 "Autonomous Knowledge" 계층을 얹음 |
| Cloudera | data_platform (하이브리드 데이터 패브릭) | 온프레미스와 클라우드를 SDX 하나로 통합 거버넌스하고, 페더레이션·계보(Octopai)·에이전트를 데이터 옆에서 실행 |
| Qlik (Talend 포함) | data_platform + 분석 | 분석 엔진·시맨틱 계층·데이터 제품을 MCP로 외부 어시스턴트에 공개하고, Automate Agent로 하위 시스템에 실행까지 연결 |
| Stardog | knowledge_graph | 가상 그래프로 원천을 연결한 전사 지식그래프·온톨로지를 시맨틱 계층으로 쓰고 Voicebox MCP로 에이전트에 제공 |
| Graphwise (Ontotext + Semantic Web Company) | knowledge_graph | GraphDB·Graph Modeling(구 PoolParty)·GraphRAG를 묶어 "AI 컨텍스트 플랫폼"으로 재포지셔닝, Gartner AI Context Platforms 대표 벤더로 거론 |
| Coveo | memory_retrieval (엔터프라이즈 검색) | 권한을 반영한 전사 통합 색인과 관련도 로직을 호스팅 MCP로 ChatGPT·Claude 등에 제공 |
| Sinequa (ChapsVision) | memory_retrieval (엔터프라이즈 검색) | 200개 이상 원천의 권한 반영 하이브리드 색인을 검색 전용 MCP로 공개하고, 그 위에 전사 에이전트 운영 플랫폼 ChapsAgents |
| Workato | agent_platform (통합·실행 계층) | 수천 개 업무 앱(기록 시스템)에 대한 쓰기 행동을 사용자 신원·RBAC·감사 로그가 붙은 MCP 서버로 전사 공급 |

조사 중 제외한 후보: Dremio(SAP에 인수됨 — SAP 파일 영역), Reltio(2026-03-27 SAP 인수 합의, 2026년 Q2~Q3 종결 예정 — SAP 영역으로 넘김), TigerGraph(공식 MCP는 커뮤니티 패키지 위주라 근거 약함), C3 AI(전사 통합 데이터 모델은 있으나 2026 발표가 앱 개발 도구 C3 Code 중심), Pryon·Squirro(Gartner Impact Radar의 AI 컨텍스트 플랫폼 샘플 벤더이나 이번 조사 범위 밖 — 후속 후보).

---

## Denodo

**한 줄 요약**: 데이터 가상화(논리 데이터 계층)를 "에이전트가 공유하는 통제된 데이터 접근 서비스"로 바꾸는 전략. 에이전트별로 연결을 만들지 말고 플랫폼 하나에서 의미와 정책을 집행하자는 입장.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Denodo Platform 9.4 내장 MCP | 어떤 MCP 클라이언트든 승인된 의미·정책 아래 실시간 데이터를 찾고 질의 | GA, 2026-03 | L1, L2, GOV | https://www.denodo.com/en/press-release/2026-03-10/denodo-platform-94-accelerates-path-successful-agentic-ai-production |
| Data Marketplace 대화형 에이전트 | 업무 사용자가 데이터 제품을 놓고 여러 턴 대화, 추론 단계를 설명하고 모호하면 되물음 | GA, 2026-03 | L2, L6 | 같은 보도자료 |
| 벡터 DB 연동 | 정형·비정형(문서·임베딩)을 같은 논리 계층으로 통합 | GA, 2026-03 | L1 | 같은 보도자료 |
| Denodo AI SDK (MCP 서버 포함) | RAG 에이전트용 API·구성요소, 세션 단위 보안, 오픈소스 | GA(2024~), MCP 2025-07 | L1, L6, GOV | https://www.datamanagementblog.com/denodo-ushers-in-the-age-of-agentic-ai-with-mcp-server-support |
| DeepQuery | 시맨틱 계층을 이용해 필요한 데이터를 스스로 정해 가져오는 심층 분석 | GA(9.3), 2025-09 | L6, L7 | https://www.denodo.com/en/press-release/2025-09-16/denodo-platform-93-now-available-breakthrough-support-ai-innovation |

**2026 움직임**: 2026-03-10 Platform 9.4 — MCP를 SDK에서 플랫폼 핵심으로 옮김, Velox 기반 Lakehouse Accelerator, AI 상호작용 거버넌스.
**불확실**: 9.4 보도자료에 AI SDK·DeepQuery 언급 없음 → 9.4 안에서의 포장 방식 미확인. "시맨틱 계층"이 독립 기능명인지는 보도자료에서 불명확.

## Starburst

**한 줄 요약**: Trino 기반 페더레이션 위에 "AI-Ready 데이터 제품"이라는 컨텍스트 계층과 에이전트형 인터페이스 AIDA를 얹어, 데이터를 옮기지 않는 전사 컨텍스트 평면을 지향.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| AIDA (AI Data Assistant) | 전사 데이터 전체를 놓고 추론하는 대화형 분석이자 에이전트 제어 평면, MCP로 외부 앱·비정형 소스 연결 | 발표 2026-04, GA 2026-05 | L1, L6, GOV | https://www.businesswire.com/news/home/20260413879669/en/ , https://futurumgroup.com/insights/starbursts-intelligence-platform-sets-out-to-tame-the-multi-cloud-ai-wilderness/ |
| AI-Ready Data Products | 데이터·메타데이터·업무 규칙을 묶은 재사용 자산, YAML 코드로 정의해 CI/CD 배포 | GA 2026-05 (일부 자료는 공개 프리뷰로 기재) | L2, L4, GOV | 같은 Futurum 분석 |
| Starburst MCP 서버 + 에이전트 API | 내외부 에이전트가 Galaxy에 표준 방식으로 접근, 다중 에이전트 관리 | 발표 2025-10 | L1, L6 | https://siliconangle.com/?p=714821 |
| Enterprise Intelligence Platform (BYOC 포함) | 페더레이션·분석 엔진·컨텍스트 계층·AIDA 4계층 통합, 고객 클라우드 배포 | 발표 2026-05 | L1, L2, GOV | 같은 Futurum 분석 |

**2026 움직임**: 2026-04-14 AIDA 발표 → 2026-05-28 Enterprise Intelligence Platform, AIDA·데이터 제품·Managed Icehouse GA.
**불확실**: 공식 보도자료 원문(403)은 직접 확인 못 함 — 상세는 Futurum 등 2차 자료. 데이터 제품 정의 기능의 GA/프리뷰 상태가 자료마다 다름.

## Teradata

**한 줄 요약**: 2026년에 "에이전트 도구 묶음(AgentStack)"에서 "자율 지식 플랫폼"으로 브랜드를 옮기며, 전사 데이터·벡터·의미·계보를 에이전트용 지식 계층으로 묶음.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Autonomous Knowledge Platform (Tera, AI Studio, Tera Agents) | 데이터·분석·AI를 한 시스템으로, 통제된 컨텍스트·의미·계보를 에이전트에 제공 | 발표 2026-05, GA 2026-07 | L2, L5, L6, GOV | https://www.teradata.com/press-releases/2026/introducing-the-autonomous-knowledge-platform |
| Enterprise Vector Store | 문서·이미지·음성을 자동 처리해 정형 데이터와 하이브리드 검색, MCP로 노출 | 에이전트·멀티모달 기능 GA 2026-04 | L1 | https://kr.teradata.com/press-releases/2026/teradata-enables-ai-agents |
| Enterprise MCP | 에이전트가 Teradata 데이터를 질의·시맨틱 검색·SQL 생성하는 기성 도구 | 발표 2026-01, 클라우드 Q2 | L1, L7 | https://www.teradata.com/press-releases/2026/teradata-unveils-enterprise-agentstack |
| AgentEngine / AgentOps | 에이전트 실행 런타임(IAM·관측), 전사 에이전트 목록·정책·평가·사람 개입 | 발표 2026-01 | GOV, OBS, L7 | 같은 보도자료 |
| AgentBuilder | 노코드·프로코드 에이전트 제작(Flowise, LangGraph 등 연동) | 발표 2026-01 | L4 | 같은 보도자료 |

**2026 움직임**: 2026-01-27 Enterprise AgentStack → 2026-03 Vector Store 멀티모달(2026-04 GA) → 2026-05-07 Autonomous Knowledge Platform 발표 → 2026-07 GA(AWS 기반 Teradata Cloud 우선).
**불확실**: AgentStack 구성요소가 새 플랫폼 안에서 어떻게 이름이 바뀌었는지 공식 대응표 없음. AgentBuilder는 에이전트 제작 도구라 범위 경계 — 전사 런타임·거버넌스 부분 위주로 기록.

## Cloudera

**한 줄 요약**: "AI를 데이터로 가져간다" — 온프레미스·클라우드 어디든 SDX 공통 거버넌스와 계보 위에서 에이전트를 실행하는 하이브리드 데이터 패브릭 전략.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| SDX + Octopai 계보 + Trino 페더레이션 | 환경 전체의 메타데이터·접근 통제 통합, 외부 원천까지 끝-끝 계보, 데이터 이동 없는 연합 질의 | 발표 2025-11 | L1, L5, GOV | https://www.aap.com.au/aapreleases/globenewswire9578741/ |
| Agent Studio 3.0 | 시각 워크플로와 파이썬 코드가 같은 런타임, 샌드박스·가드레일·감사 로그 | 블로그 2026-08 | L4, L7, GOV | https://www.cloudera.com/blog/business/eliminating-the-enterprise-ai-governance-bottleneck-with-cloudera-agent-studio-3-0.html |
| Cloudera MCP 서버 | 플랫폼 안에서 돌아가는 통제된 데이터 게이트웨이 | 발표(시기 미확인) | L1, GOV | https://www.cloudera.com/blog/technical/bringing-context-to-genai-with-cloudera-mpc-servers |
| Workflow Data Fabric Zero Copy Connector for ServiceNow | ServiceNow의 AI 행동을 원천 데이터와 복사 없이 연결 | 발표 2026-05 | L1, L7 | https://www.storagenewsletter.com/2026/06/01/servicenow-knowledge26-cloudera-launches-workflow-data-fabric-zero-copy-connector-for-servicenow/ |

**2026 움직임**: 2026-02 Agent Studio 2.2(RBAC·평가) → 2026-05 2.3(평가 UI·트레이싱) → 2026-05-05 ServiceNow 제로카피 커넥터 → 2026-08 Agent Studio 3.0.
**불확실**: MCP 서버의 GA 여부·날짜 미확인. Agent Studio는 에이전트 제작 도구 성격이 강해 범위 경계(거버넌스·감사 부분 때문에 포함).

## Qlik (Talend 포함)

**한 줄 요약**: 분석 엔진·시맨틱 계층·데이터 제품을 MCP로 외부 어시스턴트에 열고, 질문(Answers)에서 행동(Automate Agent)까지 잇는 "분석의 에이전트화".

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Qlik MCP Server | 엔진·도구·에이전트 수준에서 Qlik을 Claude 등 외부 어시스턴트에 노출 | GA 2026-02 | L1, L2, GOV | https://www.qlik.com/us/news/company/press-room/press-releases/qlik-brings-agentic-analytics-to-general-availability-and-launches-mcp-server-for-third-party-assistants |
| Semantic Layer / Data Products for Analytics | 측정값·차원·관계 정의를 공유, 품질 신호가 붙은 큐레이션 데이터셋 | 발표 2026-04 (데이터 제품은 2026-02 이후 순차) | L2, GOV | https://www.qlik.com/us/news/company/press-room/press-releases/qlik-extends-analytics-from-answers-to-agentic-action |
| Qlik Answers | 정형 분석과 비정형 문서를 한 경험으로, 인용·추론 설명 포함 | GA 2026-02 | L1, L6, L7 | 같은 두 보도자료 |
| Discovery / Predict / Analytics Agent | 이상 탐지 신호, 예측 모델, 분석 개발 보조 | Discovery GA 2026-02, 나머지 발표 2026-04 | L5, L7 | 같은 보도자료 |
| Automate Agent | 자연어 요청으로 하위 시스템 워크플로 실행 | 발표 2026-04 | L7 | 같은 보도자료 |

**2026 움직임**: 2025-12 에이전트 기능 프리뷰 → 2026-02 Answers 강화·MCP GA → 2026-04-14 Qlik Connect에서 Discovery/Predict/Automate/Analytics Agent·시맨틱 계층·Open Lakehouse 스트리밍.
**불확실**: Talend 데이터 패브릭이 에이전트 컨텍스트와 어떻게 연결되는지 공식 문서 미확인. Agent 4종 각각의 GA 여부 불명.

## Stardog

**한 줄 요약**: 원천 데이터를 가상 그래프로 연결한 전사 지식그래프를 "시맨틱 계층"으로 내세우고, Voicebox(다중 에이전트 질의층)와 MCP로 에이전트에 근거 있는 답을 공급.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Stardog Semantic AI Platform (가상 그래프, 추론 엔진, SHACL 품질) | 데이터를 복사하거나 그 자리에서 질의, 질의 시점에 업무 규칙으로 정의 충돌 조정 | GA | L1, L2, L3, L7 | https://www.stardog.com/product/ |
| Voicebox + Voicebox MCP Server | 자연어 질의·모델 작성 보조, Think Mode로 다중 에이전트 계획, MCP로 외부 에이전트에 지식 제공(읽기 전용) | MCP 발표 2025-11 (11.2) | L3, L6 | https://community.stardog.com/t/whats-new-in-stardog-11-2/5512 |
| Stardog Designer | 노코드 온톨로지 설계, 역량 질문 기반 자동 제안 | GA | L3 | https://www.stardog.com/product/ |
| Stardog Cloud MCP | Voicebox API를 감싼 클라우드 MCP, Bedrock AgentCore 연동 사례 | 2026-07 사례 | L1, L3 | https://aws-news.com/article/2026-07-10-build-a-semantic-layer-for-agentic-ai-on-aws-with-stardog-and-amazon-bedrock-agentcore |

**2026 움직임**: 2026-07 AWS와 Bedrock AgentCore 시맨틱 계층 레퍼런스. 2026년 리브랜드로 "Semantic Control Plane" 포지셔닝(경쟁사 Atlan 자료 — 2차).
**불확실**: 리브랜드·CEO 교체는 경쟁사 글로만 확인. Voicebox는 쓰기 불가(읽기 전용)라는 공식 블로그 서술 이후 변화 미확인.

## Graphwise (Ontotext + Semantic Web Company)

**한 줄 요약**: 그래프 DB·택소노미·GraphRAG를 하나의 "AI 컨텍스트 플랫폼"으로 묶어, 지식그래프를 에이전트의 시맨틱 백본으로 판다. 2026-08 Oakley Capital이 과반 지분 확보.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| GraphDB 11.x (MCP) | RDF 그래프 DB, MCP로 에이전트·Copilot Studio가 지식에 접근 | 11.0 2025-07, 11.3 2026-02 | L1, L3 | https://graphwise.ai/news/ |
| Graph Modeling (구 PoolParty 10.x) | 택소노미·온톨로지 관리, AI 택소노미 빌더, 거버넌스 | 10.1 2026-02, 10.2 2026-03 | L2, L3, GOV | 같은 뉴스 페이지 |
| Graphwise GraphRAG | 지식그래프를 시맨틱 계층으로 쓰는 RAG, 벡터 검색도 MCP 도구로 | GA 2026-02, 1.2.0 2026-05 | L3, L6 | https://www.techtarget.com/searchDataManagement/news/366639196/Graphwise-aims-to-boost-AI-accuracy-with-GraphRAG-launch |
| Graphwise Platform (AI Context Platform) | 통합 라이선스, 평가 도구, n8n 자동화, 다국어 택소노미 검색 | 발표 2026-09 | L3, L4, OBS | https://aithority.com/machine-learning/graphwise-upgrades-its-ai-context-platform-to-help-enterprises-build-seamless-context-layers-and-unlock-smarter-multilingual-ai/ |

**2026 움직임**: 2026-02-17 GraphRAG → 2026-02-24 GraphDB 11.3 → 2026-08-19 Oakley Capital 과반 투자 → 2026-09-02 Gartner "Market Overview for AI Context Platforms"(2026-08-13) 대표 벤더 → 2026-09-30 플랫폼 업그레이드.
**불확실**: Gartner 보고서 전체 벤더 목록은 유료라 미확인. 9월 업그레이드는 보도자료 재배포만 확인.

## Coveo

**한 줄 요약**: 권한을 반영한 전사 통합 색인과 관련도 엔진을 호스팅 MCP로 ChatGPT·Claude 같은 범용 어시스턴트에 빌려주는 "관련도 계층" 전략.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Coveo Hosted MCP Server | 추가 인프라 없이 LLM 앱이 통합 색인에서 근거 검색, 소비량 기반 과금 | GA 2026-02 | L1, L6, GOV | https://ir.coveo.com/en/news-events/press-releases/detail/474/coveo-announces-hosted-mcp-server-to-expand-enterprise-ai |
| AI-Relevance Platform (통합 색인) | 여러 원천을 권한과 함께 색인하고 행동 신호로 관련도 학습 | GA | L1, L6, GOV | 같은 보도자료 |
| Relevance Generative Answering (RGA) | 사용자가 볼 권한이 있는 문서에서만 답 생성 | GA | L6, L7, GOV | https://docs.coveo.com/en/pboe0358/ (2차 요약 경유) |
| RAG-as-a-Service for AWS | AWS 에이전트 서비스에 Coveo 검색을 MCP로 공급 | 발표 2025-12 | L1, L6 | https://www.coveo.com/en/company/news-releases/2025/coveo-introduces-rag-as-a-service-for-aws-agentic-ai-services |

**2026 움직임**: 2026-02-10 Hosted MCP Server GA, ChatGPT Enterprise 앱 디렉터리 등재, Claude 연동 고객 10곳.
**불확실**: MCP 도구 목록 문서 페이지 접속 실패(503) — 도구 이름은 검색 요약으로만 확인. 커뮤니티 GitHub 버전과 혼동 주의.

## Sinequa (ChapsVision)

**한 줄 요약**: 하이브리드 검색 색인을 "추론하지 않는 검색 전용 MCP"로 모든 LLM에 공개하고, 그 위에 전사 에이전트 운영 플랫폼 ChapsAgents를 얹는 주권형(on-prem 가능) 전략.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Sinequa MCP Server | 검색·필터 정의·필터 검증·사내 용어 해석 등 5개 도구, 원천 권한 그대로 적용, LLM 호출 없음 | 공개(날짜 미확인) | L1, L2, L6, GOV | https://www.sinequa.com/wp-content/uploads/Sinequa-MCP-Server-Overview.html |
| Sinequa 엔터프라이즈 AI 검색 | 200개 이상 원천 커넥터, 통계·의미·멀티모달 하이브리드 검색 | GA | L1 | https://ressources.chapsvision.com/en-us/sinequa-by-chapsvision-trusted-enterprise-ai-search |
| ChapsAgents | 전사 에이전트를 구성·배포·조율·통제하는 플랫폼(Agentic RAG 기반) | GA 2026-04 | L4, L6, GOV, OBS | https://www.sinequa.com/resources/blog/scaling-ai-you-can-actually-trust-introducing-chapsagents/ |

**2026 움직임**: 2026-04-22 VisionCast에서 ChapsAgents GA. MCP 서버를 Claude·ChatGPT·Copilot·Gemini 공용 어댑터로 포지셔닝.
**불확실**: MCP 서버 출시일·GA 여부 공식 표기 없음. 사내 용어 해석 도구가 글로서리(L2)를 얼마나 관리하는지는 미확인(◐ 처리).

## Workato (추가 선정)

**한 줄 요약**: 통합·자동화 플랫폼을 "기록 시스템에 대한 행동 계층"으로 바꿔, 에이전트의 쓰기 작업을 사용자 신원·권한·감사가 붙은 MCP 서버로 전사 공급.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Workato Enterprise MCP | 기존 레시피·스킬을 노코드로 MCP 서버화, 사용자 신원 상속·RBAC·전수 감사 로그 | 발표 2025-10, 상태 표기 없음 | L1, L7, GOV, OBS | https://www.workato.com/de-DE/agentic/mcp |
| Production-ready MCP 서버 묶음 | 고객 컨텍스트 조회부터 기록 시스템 갱신까지 여러 시스템을 엮은 기성 서버 | 발표 2026-02 | L4, L7 | https://www.businesswire.com/news/home/20260205680021/en/Workato-Accelerates-Enterprise-AI-Adoption-with-Launch-of-Production-Ready-Model-Context-Protocol-Servers |
| Enterprise MCP Registry | 회사 안 모든 MCP 서버(자사·외부·내부 제작)의 통제된 목록 | 발표(날짜 미확인) | GOV | https://www.webull.com/news/15237139180315648 |
| Workato ONE Agent Hub | 지식 원천과 전사 스킬 목록, 오케스트레이션을 API로 노출 | GA(2025) | L4, L6 | https://www.businesswire.com/news/home/20250819305476/en/Workato-Supercharges-ONE-The-Agentic-Core-for-AI-Ready-Enterprises |

**2026 움직임**: 2026-02-05 기성 MCP 서버 묶음 발표, MCP Registry 발표(2차 경유), Gartner Peer Insights 2026 Customers' Choice.
**불확실**: 보도자료 원문(403)·Registry 출시일 직접 확인 못 함. 연결 앱 수(12,000+)는 2차 요약 수치.

---

```yaml
vendors:
  - vendor: denodo
    name: Denodo
    category: data_platform
    products:
      - id: denodo-platform-mcp
        name: Denodo Platform 9.4 내장 MCP
        scope: enterprise_context
        status: GA
        status_date: 2026-03
        layers: {L1: ●, L2: ●, GOV: ●}
        x: -1
        y: 0
        xy_reason: "가상화된 데이터·지표 질의 중심, 의미는 사람이 정의하고 에이전트가 런타임에 탐색·질의"
        maturity: 2
        evidence:
          - {url: "https://www.denodo.com/en/press-release/2026-03-10/denodo-platform-94-accelerates-path-successful-agentic-ai-production", kind: official, date: 2026-03-10}
      - id: denodo-marketplace-agent
        name: Data Marketplace 대화형 에이전트
        scope: enterprise_agent_app
        status: GA
        status_date: 2026-03
        layers: {L2: ●, L6: ●, GOV: ◐}
        x: -2
        y: 1
        xy_reason: "데이터 제품에 대한 분석 질문 응답, 모호하면 되묻고 단계별로 데이터 탐색"
        maturity: 1
        evidence:
          - {url: "https://www.denodo.com/en/press-release/2026-03-10/denodo-platform-94-accelerates-path-successful-agentic-ai-production", kind: official, date: 2026-03-10}
      - id: denodo-vector-integration
        name: 벡터 DB 연동
        scope: enterprise_context
        status: GA
        status_date: 2026-03
        layers: {L1: ●, GOV: ◐}
        x: -1
        y: -1
        xy_reason: "정형·비정형을 논리 계층에 등록하는 사전 구성 방식"
        maturity: 1
        evidence:
          - {url: "https://www.denodo.com/en/press-release/2026-03-10/denodo-platform-94-accelerates-path-successful-agentic-ai-production", kind: official, date: 2026-03-10}
      - id: denodo-ai-sdk
        name: Denodo AI SDK (MCP 서버 포함)
        scope: enterprise_context
        status: GA
        status_date: 2025-07
        layers: {L1: ●, L6: ◐, GOV: ●}
        x: -1
        y: 0
        xy_reason: "RAG 에이전트에 가상화 데이터와 세션 보안을 제공하는 API 묶음"
        maturity: 1
        evidence:
          - {url: "https://www.datamanagementblog.com/denodo-ushers-in-the-age-of-agentic-ai-with-mcp-server-support", kind: official, date: 2025-07}
      - id: denodo-deepquery
        name: Denodo DeepQuery
        scope: enterprise_agent_app
        status: GA
        status_date: 2025-09
        layers: {L2: ◐, L6: ●, L7: ◐}
        x: -2
        y: 2
        xy_reason: "필요한 데이터를 스스로 결정해 가져오는 심층 분석, 숫자 질문 중심"
        maturity: 1
        evidence:
          - {url: "https://www.denodo.com/en/press-release/2025-09-16/denodo-platform-93-now-available-breakthrough-support-ai-innovation", kind: official, date: 2025-09-16}

  - vendor: starburst
    name: Starburst
    category: data_platform
    products:
      - id: starburst-aida
        name: AIDA (AI Data Assistant)
        scope: enterprise_agent_app
        status: GA
        status_date: 2026-05
        layers: {L1: ◐, L6: ●, GOV: ◐}
        x: -1
        y: 1
        xy_reason: "전사 데이터에 대한 분석 질문을 추론하고 MCP로 외부 앱 컨텍스트를 끌어옴"
        maturity: 2
        evidence:
          - {url: "https://www.businesswire.com/news/home/20260413879669/en/", kind: official, date: 2026-04-14}
          - {url: "https://futurumgroup.com/insights/starbursts-intelligence-platform-sets-out-to-tame-the-multi-cloud-ai-wilderness/", kind: secondary, date: 2026-06-02}
      - id: starburst-ai-ready-data-products
        name: AI-Ready Data Products
        scope: enterprise_context
        status: GA
        status_date: 2026-05
        layers: {L2: ●, L4: ◐, GOV: ●}
        x: -1
        y: -2
        xy_reason: "업무 규칙·메타데이터를 YAML 코드로 사람이 정의·배포"
        maturity: 2
        evidence:
          - {url: "https://futurumgroup.com/insights/starbursts-intelligence-platform-sets-out-to-tame-the-multi-cloud-ai-wilderness/", kind: secondary, date: 2026-06-02}
      - id: starburst-mcp-agent-api
        name: Starburst MCP Server + Agent API
        scope: enterprise_context
        status: announced
        status_date: 2025-10
        layers: {L1: ●, L6: ◐, GOV: ◐}
        x: -1
        y: 0
        xy_reason: "내외부 에이전트가 페더레이션 데이터에 접근하는 표준 관문"
        maturity: 2
        evidence:
          - {url: "https://siliconangle.com/?p=714821", kind: secondary, date: 2025-10-09}
      - id: starburst-enterprise-intelligence-platform
        name: Starburst Enterprise Intelligence Platform
        scope: enterprise_context
        status: announced
        status_date: 2026-05
        layers: {L1: ●, L2: ●, L6: ◐, GOV: ●}
        x: -1
        y: 0
        xy_reason: "페더레이션+데이터 제품 컨텍스트 계층+에이전트 인터페이스의 통합 구조"
        maturity: 2
        evidence:
          - {url: "https://futurumgroup.com/insights/starbursts-intelligence-platform-sets-out-to-tame-the-multi-cloud-ai-wilderness/", kind: secondary, date: 2026-06-02}

  - vendor: teradata
    name: Teradata
    category: data_platform
    products:
      - id: teradata-autonomous-knowledge-platform
        name: Teradata Autonomous Knowledge Platform (Tera, AI Studio, Tera Agents)
        scope: enterprise_context
        status: GA
        status_date: 2026-07
        layers: {L2: ●, L5: ◐, L6: ◐, L7: ◐, GOV: ●}
        x: -1
        y: 0
        xy_reason: "통제된 의미·계보를 에이전트에 주는 분석 중심 플랫폼, 운영 에이전트도 포함"
        maturity: 3
        evidence:
          - {url: "https://www.teradata.com/press-releases/2026/introducing-the-autonomous-knowledge-platform", kind: official, date: 2026-05-07}
          - {url: "https://www.barchart.com/story/news/3296080/teradata-autonomous-knowledge-platform-reaches-general-availability-across-cloud-and-on-premises", kind: secondary, date: 2026-07-15}
      - id: teradata-enterprise-vector-store
        name: Teradata Enterprise Vector Store
        scope: enterprise_context
        status: GA
        status_date: 2026-04
        layers: {L1: ●, GOV: ◐}
        x: 0
        y: 0
        xy_reason: "문서·이미지·음성을 자동 처리해 색인, 에이전트가 MCP로 검색"
        maturity: 1
        evidence:
          - {url: "https://kr.teradata.com/press-releases/2026/teradata-enables-ai-agents", kind: official, date: 2026-03}
      - id: teradata-enterprise-mcp
        name: Teradata Enterprise MCP
        scope: enterprise_context
        status: announced
        status_date: 2026-01
        layers: {L1: ●, L7: ◐, GOV: ◐}
        x: -1
        y: 0
        xy_reason: "질의·시맨틱 검색·SQL 생성 도구를 에이전트에 제공"
        maturity: 2
        evidence:
          - {url: "https://www.teradata.com/press-releases/2026/teradata-unveils-enterprise-agentstack", kind: official, date: 2026-01-27}
      - id: teradata-agentengine-agentops
        name: AgentEngine / AgentOps
        scope: enterprise_context
        status: announced
        status_date: 2026-01
        layers: {L7: ●, GOV: ●, OBS: ●}
        x: 1
        y: 0
        xy_reason: "전사 에이전트 실행·정책·평가·사람 개입 관리"
        maturity: 4
        evidence:
          - {url: "https://www.teradata.com/press-releases/2026/teradata-unveils-enterprise-agentstack", kind: official, date: 2026-01-27}

  - vendor: cloudera
    name: Cloudera
    category: data_platform
    products:
      - id: cloudera-sdx-lineage-federation
        name: SDX + Octopai Lineage + Trino Federation
        scope: enterprise_context
        status: announced
        status_date: 2025-11
        layers: {L1: ●, L5: ●, GOV: ●}
        x: -1
        y: -1
        xy_reason: "하이브리드 전체 메타데이터·접근 정책·계보를 관리자가 통합 관리"
        maturity: 1
        evidence:
          - {url: "https://www.aap.com.au/aapreleases/globenewswire9578741/", kind: official, date: 2025-11-20}
      - id: cloudera-agent-studio
        name: Cloudera Agent Studio 3.0
        scope: enterprise_agent_app
        status: GA
        status_date: 2026-08
        layers: {L4: ●, L7: ●, GOV: ●, OBS: ◐}
        x: 1
        y: 0
        xy_reason: "데이터 옆에서 에이전트 워크플로 실행, 가드레일·LLM 판정·감사 로그"
        maturity: 4
        evidence:
          - {url: "https://www.cloudera.com/blog/business/eliminating-the-enterprise-ai-governance-bottleneck-with-cloudera-agent-studio-3-0.html", kind: official, date: 2026-08-19}
          - {url: "https://docs.cloudera.com/cdp-public-cloud/cloud/release-summaries/topics/announcement-202605.html", kind: official, date: 2026-05}
      - id: cloudera-mcp-servers
        name: Cloudera MCP Servers
        scope: enterprise_context
        status: announced
        status_date: null  # 블로그 날짜 미확인
        layers: {L1: ●, GOV: ◐}
        x: -1
        y: 0
        xy_reason: "플랫폼 내부의 통제된 데이터 게이트웨이"
        maturity: 1
        evidence:
          - {url: "https://www.cloudera.com/blog/technical/bringing-context-to-genai-with-cloudera-mpc-servers", kind: official, date: null}
      - id: cloudera-zero-copy-servicenow
        name: Workflow Data Fabric Zero Copy Connector for ServiceNow
        scope: enterprise_context
        status: announced
        status_date: 2026-05
        layers: {L1: ●, L7: ◐}
        x: 1
        y: -1
        xy_reason: "업무 워크플로 행동을 원천 데이터와 복사 없이 연결"
        maturity: 1
        evidence:
          - {url: "https://www.storagenewsletter.com/2026/06/01/servicenow-knowledge26-cloudera-launches-workflow-data-fabric-zero-copy-connector-for-servicenow/", kind: secondary, date: 2026-06-01}

  - vendor: qlik
    name: Qlik
    category: data_platform
    products:
      - id: qlik-mcp-server
        name: Qlik MCP Server
        scope: enterprise_context
        status: GA
        status_date: 2026-02
        layers: {L1: ●, L2: ●, GOV: ◐}
        x: -2
        y: 0
        xy_reason: "분석 엔진 계산과 통제된 데이터를 외부 어시스턴트에 노출"
        maturity: 2
        evidence:
          - {url: "https://www.qlik.com/us/news/company/press-room/press-releases/qlik-brings-agentic-analytics-to-general-availability-and-launches-mcp-server-for-third-party-assistants", kind: official, date: 2026-02}
      - id: qlik-semantic-data-products
        name: Qlik Semantic Layer / Data Products for Analytics
        scope: enterprise_context
        status: announced
        status_date: 2026-04
        layers: {L2: ●, GOV: ●, OBS: ◐}
        x: -2
        y: -2
        xy_reason: "측정값·차원·관계와 품질 신호를 사람이 큐레이션"
        maturity: 1
        evidence:
          - {url: "https://www.qlik.com/us/news/company/press-room/press-releases/qlik-extends-analytics-from-answers-to-agentic-action", kind: official, date: 2026-04-14}
      - id: qlik-answers
        name: Qlik Answers
        scope: enterprise_agent_app
        status: GA
        status_date: 2026-02
        layers: {L1: ◐, L6: ●, L7: ◐}
        x: -2
        y: 1
        xy_reason: "정형 분석과 문서를 묶어 인용 포함 답을 조립"
        maturity: 4
        evidence:
          - {url: "https://www.qlik.com/us/news/company/press-room/press-releases/qlik-brings-agentic-analytics-to-general-availability-and-launches-mcp-server-for-third-party-assistants", kind: official, date: 2026-02}
      - id: qlik-discovery-predict-analytics-agents
        name: Discovery / Predict / Analytics Agent
        scope: enterprise_agent_app
        status: GA
        status_date: 2026-02
        layers: {L5: ◐, L7: ●, OBS: ◐}
        x: -1
        y: 2
        xy_reason: "핵심 지표를 스스로 감시해 이상 신호를 찾아냄"
        maturity: 2
        evidence:
          - {url: "https://www.qlik.com/us/news/company/press-room/press-releases/qlik-extends-analytics-from-answers-to-agentic-action", kind: official, date: 2026-04-14}
      - id: qlik-automate-agent
        name: Qlik Automate Agent
        scope: enterprise_agent_app
        status: announced
        status_date: 2026-04
        layers: {L4: ◐, L7: ●}
        x: 2
        y: 0
        xy_reason: "자연어 요청으로 하위 시스템 워크플로·행동 실행"
        maturity: 2
        evidence:
          - {url: "https://www.qlik.com/us/news/company/press-room/press-releases/qlik-extends-analytics-from-answers-to-agentic-action", kind: official, date: 2026-04-14}

  - vendor: stardog
    name: Stardog
    category: knowledge_graph
    products:
      - id: stardog-semantic-ai-platform
        name: Stardog Semantic AI Platform (Virtual Graphs, Inference, SHACL)
        scope: enterprise_context
        status: GA
        status_date: 2025-11
        layers: {L1: ●, L2: ●, L3: ●, L7: ◐}
        x: 0
        y: -2
        xy_reason: "사람이 설계한 온톨로지·규칙으로 원천을 연결하고 질의 시점에 추론"
        maturity: 4
        evidence:
          - {url: "https://www.stardog.com/product/", kind: official, date: 2026-11-11}
      - id: stardog-voicebox-mcp
        name: Stardog Voicebox + Voicebox MCP Server
        scope: enterprise_context
        status: GA
        status_date: 2025-11
        layers: {L3: ●, L6: ●, GOV: ◐}
        x: 0
        y: 1
        xy_reason: "자연어를 그래프 질의로 바꿔 다중 에이전트가 계획·응답, 읽기 전용"
        maturity: 2
        evidence:
          - {url: "https://community.stardog.com/t/whats-new-in-stardog-11-2/5512", kind: official, date: 2025-11-04}
      - id: stardog-designer
        name: Stardog Designer
        scope: enterprise_context
        status: GA
        status_date: 2025-11
        layers: {L2: ◐, L3: ●}
        x: 0
        y: -1
        xy_reason: "사람이 온톨로지를 설계하되 AI 제안 보조"
        maturity: 1
        evidence:
          - {url: "https://community.stardog.com/t/whats-new-in-stardog-11-2/5512", kind: official, date: 2025-11-04}
      - id: stardog-cloud-mcp
        name: Stardog Cloud MCP (Bedrock AgentCore 연동)
        scope: enterprise_context
        status: GA
        status_date: 2026-07
        layers: {L1: ●, L3: ●}
        x: 0
        y: 0
        xy_reason: "외부 에이전트가 지식그래프를 시맨틱 계층으로 질의"
        maturity: 1
        evidence:
          - {url: "https://aws-news.com/article/2026-07-10-build-a-semantic-layer-for-agentic-ai-on-aws-with-stardog-and-amazon-bedrock-agentcore", kind: secondary, date: 2026-07-10}

  - vendor: graphwise
    name: Graphwise
    category: knowledge_graph
    products:
      - id: graphwise-graphdb
        name: GraphDB 11.x (MCP)
        scope: enterprise_context
        status: GA
        status_date: 2026-02
        layers: {L1: ●, L3: ●}
        x: 0
        y: -1
        xy_reason: "큐레이션된 RDF 지식그래프를 에이전트가 MCP로 조회"
        maturity: 1
        evidence:
          - {url: "https://graphwise.ai/news/", kind: official, date: 2026-02-24}
      - id: graphwise-graph-modeling
        name: Graph Modeling (구 PoolParty 10.x)
        scope: enterprise_context
        status: GA
        status_date: 2026-03
        layers: {L2: ●, L3: ●, GOV: ◐}
        x: 0
        y: -2
        xy_reason: "택소노미·온톨로지를 사람이 관리, AI 빌더가 보조"
        maturity: 1
        evidence:
          - {url: "https://graphwise.ai/news/", kind: official, date: 2026-03-19}
      - id: graphwise-graphrag
        name: Graphwise GraphRAG
        scope: enterprise_context
        status: GA
        status_date: 2026-05
        layers: {L1: ◐, L3: ●, L6: ●}
        x: 0
        y: 0
        xy_reason: "지식그래프+벡터 검색을 MCP 도구로 묶어 질의별 근거 조립"
        maturity: 2
        evidence:
          - {url: "https://www.techtarget.com/searchDataManagement/news/366639196/Graphwise-aims-to-boost-AI-accuracy-with-GraphRAG-launch", kind: secondary, date: 2026-02}
          - {url: "https://help.graphwise.ai/en/graphrag/release-notes/graphrag-1-2-0-release-notes.html", kind: official, date: 2026-05-06}
      - id: graphwise-ai-context-platform
        name: Graphwise Platform (AI Context Platform)
        scope: enterprise_context
        status: announced
        status_date: 2026-09
        layers: {L2: ●, L3: ●, L4: ◐, OBS: ◐}
        x: 0
        y: -1
        xy_reason: "그래프 기반 컨텍스트 계층에 평가 도구·n8n 자동화 추가"
        maturity: 4
        evidence:
          - {url: "https://aithority.com/machine-learning/graphwise-upgrades-its-ai-context-platform-to-help-enterprises-build-seamless-context-layers-and-unlock-smarter-multilingual-ai/", kind: secondary, date: 2026-09-30}

  - vendor: coveo
    name: Coveo
    category: memory_retrieval
    products:
      - id: coveo-hosted-mcp
        name: Coveo Hosted MCP Server
        scope: enterprise_context
        status: GA
        status_date: 2026-02
        layers: {L1: ●, L6: ●, GOV: ◐}
        x: 0
        y: 1
        xy_reason: "통합 색인에서 질의별로 관련 근거를 골라 외부 LLM 앱에 제공"
        maturity: 1
        evidence:
          - {url: "https://ir.coveo.com/en/news-events/press-releases/detail/474/coveo-announces-hosted-mcp-server-to-expand-enterprise-ai", kind: official, date: 2026-02-10}
      - id: coveo-ai-relevance-platform
        name: Coveo AI-Relevance Platform (통합 색인)
        scope: enterprise_context
        status: GA
        status_date: 2026-02
        layers: {L1: ●, L6: ●, GOV: ●, OBS: ◐}
        x: 0
        y: 1
        xy_reason: "권한 반영 색인, 사용 신호로 관련도가 자동 개선"
        maturity: 5
        evidence:
          - {url: "https://ir.coveo.com/en/news-events/press-releases/detail/474/coveo-announces-hosted-mcp-server-to-expand-enterprise-ai", kind: official, date: 2026-02-10}
      - id: coveo-rga
        name: Relevance Generative Answering
        scope: enterprise_agent_app
        status: GA
        status_date: 2026-02
        layers: {L6: ●, L7: ◐, GOV: ●}
        x: 0
        y: 1
        xy_reason: "사용자 권한 내 문서만으로 근거 답 생성"
        maturity: 4
        evidence:
          - {url: "https://docs.coveo.com/en/pboe0358/", kind: official, date: 2026-02}
      - id: coveo-rag-as-a-service-aws
        name: Coveo RAG-as-a-Service for AWS
        scope: enterprise_context
        status: announced
        status_date: 2025-12
        layers: {L1: ●, L6: ●}
        x: 0
        y: 1
        xy_reason: "AWS 에이전트 서비스에 검색 근거 공급"
        maturity: 1
        evidence:
          - {url: "https://www.coveo.com/en/company/news-releases/2025/coveo-introduces-rag-as-a-service-for-aws-agentic-ai-services", kind: official, date: 2025-12-01}

  - vendor: sinequa
    name: Sinequa (ChapsVision)
    category: memory_retrieval
    products:
      - id: sinequa-mcp-server
        name: Sinequa MCP Server
        scope: enterprise_context
        status: announced
        status_date: null  # 출시일·GA 공식 표기 없음
        layers: {L1: ●, L2: ◐, L6: ●, GOV: ●}
        x: 0
        y: 1
        xy_reason: "에이전트가 런타임에 검색 지침·필터·사내 용어를 조회해 스스로 질의 구성"
        maturity: 2
        evidence:
          - {url: "https://www.sinequa.com/wp-content/uploads/Sinequa-MCP-Server-Overview.html", kind: official, date: 2026-11-11}
      - id: sinequa-enterprise-ai-search
        name: Sinequa Enterprise AI Search
        scope: enterprise_context
        status: GA
        status_date: null  # 장기 GA 제품, 특정 날짜 미기재
        layers: {L1: ●, L6: ●, GOV: ●}
        x: 0
        y: 0
        xy_reason: "200+ 원천을 권한과 함께 색인한 하이브리드 검색"
        maturity: 1
        evidence:
          - {url: "https://ressources.chapsvision.com/en-us/sinequa-by-chapsvision-trusted-enterprise-ai-search", kind: official, date: 2026-11-11}
      - id: sinequa-chapsagents
        name: ChapsAgents
        scope: enterprise_agent_app
        status: GA
        status_date: 2026-04
        layers: {L4: ●, L6: ●, GOV: ●, OBS: ◐}
        x: 1
        y: 1
        xy_reason: "검색 기반 위에서 전사 에이전트를 구성·조율·통제"
        maturity: 3
        evidence:
          - {url: "https://www.sinequa.com/resources/blog/scaling-ai-you-can-actually-trust-introducing-chapsagents/", kind: official, date: 2026-04-22}

  - vendor: workato
    name: Workato
    category: agent_platform
    products:
      - id: workato-enterprise-mcp
        name: Workato Enterprise MCP
        scope: enterprise_context
        status: GA
        status_date: 2025-10
        layers: {L1: ●, L7: ●, GOV: ●, OBS: ●}
        x: 2
        y: -1
        xy_reason: "기록 시스템 쓰기 행동을 사람이 만든 레시피 기반 MCP 서버로 제공"
        maturity: 2
        evidence:
          - {url: "https://www.workato.com/de-DE/agentic/mcp", kind: official, date: 2026-11-11}
          - {url: "https://www.businesswire.com/news/home/20251001259763/en/Workato-Delivers-Industrys-First-Enterprise-MCP-Platform-for-AI-Agents", kind: official, date: 2025-10-01}
      - id: workato-production-mcp-servers
        name: Workato Production-ready MCP Servers
        scope: enterprise_context
        status: GA
        status_date: 2026-02
        layers: {L4: ●, L7: ●, GOV: ◐}
        x: 2
        y: -1
        xy_reason: "여러 시스템을 엮은 업무 절차를 기성 서버로 제공"
        maturity: 2
        evidence:
          - {url: "https://www.businesswire.com/news/home/20260205680021/en/Workato-Accelerates-Enterprise-AI-Adoption-with-Launch-of-Production-Ready-Model-Context-Protocol-Servers", kind: official, date: 2026-02-05}
      - id: workato-mcp-registry
        name: Workato Enterprise MCP Registry
        scope: enterprise_context
        status: announced
        status_date: null  # 발표일 미확인
        layers: {GOV: ●}
        x: 1
        y: -1
        xy_reason: "회사 내 MCP 서버 목록을 통제"
        maturity: 2
        evidence:
          - {url: "https://www.webull.com/news/15237139180315648", kind: secondary, date: null}
      - id: workato-one-agent-hub
        name: Workato ONE Agent Hub
        scope: enterprise_context
        status: GA
        status_date: 2025-08
        layers: {L4: ●, L6: ◐, GOV: ◐}
        x: 1
        y: -1
        xy_reason: "지식 원천·전사 스킬 목록과 오케스트레이션을 API로 노출"
        maturity: 2
        evidence:
          - {url: "https://www.businesswire.com/news/home/20250819305476/en/Workato-Supercharges-ONE-The-Agentic-Core-for-AI-Ready-Enterprises", kind: official, date: 2025-08-19}
```
