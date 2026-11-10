# AI·에이전트 진영 컨텍스트 엔지니어링 업체 — 묶음 조사 (조사일 2026-11-11)

> 대상: 빅6(Palantir·Snowflake·Databricks·Microsoft·Google·AWS)를 뺀 **AI 모델사·에이전트 플랫폼·기억/검색 인프라** 업체.
> 근거 표기: (공식) = 회사 블로그·문서·릴리스노트, (2차) = 언론·분석 사이트. 공식 페이지가 403 등으로 열리지 않아 검색 요약만 확인한 경우 "(공식·본문 미확인)"으로 적었다.

## 선정 업체 (13개)

| 회사 | 분류(category) | 왜 관련 있나 |
|---|---|---|
| Anthropic | ai_lab | MCP·Agent Skills 표준 제정자, API 수준의 압축/컨텍스트 편집/메모리 도구, Managed Agents 메모리 |
| OpenAI | ai_lab | Frontier(공유 비즈니스 컨텍스트 + 에이전트 신원/권한), ChatGPT 회사 지식, Agents SDK |
| Glean | agent_platform | 전사 검색 출신 → Enterprise Graph + Personal Graph, 에이전트, MCP 양방향 |
| Cohere | ai_lab | North(에이전트 작업공간) + Compass(검색·권한 파이프라인, MCP 서버) — 프라이빗 배포 지향 |
| LangChain | agent_platform | 오픈소스 에이전트 프레임워크 사실상 표준, 미들웨어로 컨텍스트 조작, LangSmith 관측 |
| LlamaIndex | memory_retrieval | 문서 파싱·추출·인덱스 → "에이전트형 문서 처리"로 재정의(LlamaCloud→LlamaParse) |
| Mem0 | memory_retrieval | 에이전트 장기 기억 레이어 대표 스타트업, 그래프 메모리 내장 |
| Zep | knowledge_graph | 시간축 지식그래프(Graphiti) → "엔터프라이즈 컨텍스트 레이어"(Context Lake, Agent Skills) |
| Letta | memory_retrieval | MemGPT 계보, git 기반 "컨텍스트 저장소" 메모리 + 메모리 우선 에이전트(Letta Code) |
| Pinecone | memory_retrieval | 벡터 DB에서 "에이전트용 지식 엔진"(Nexus: 사전 컴파일된 컨텍스트)으로 이동 |
| Elastic | memory_retrieval | Elasticsearch를 "컨텍스트 엔지니어링 기반"으로 재포지셔닝, Agent Builder GA |
| Writer | enterprise_app | Knowledge Graph(그래프 RAG) + Enterprise Brain(브랜드·결정 로직·팀 기억 컨텍스트 레이어) |
| Contextual AI | agent_platform | RAG 2.0 출신, Agent Composer = 컨텍스트 관리·가드레일 하네스(기술 산업 특화) |

**제외/보류**: Weaviate(Engram 메모리 2026-06 GA — Mem0와 같은 칸이라 다음 라운드 후보), Cognee(2026-02 시드 750만 달러, 그래프 메모리 OSS — 규모 작음), Arize(관측 전용 OBS 기둥; Dynatrace 인수설은 2차 출처 1건뿐), Vectara(2026 공식 자료 검색되지 않음).

---

## 1. Anthropic

**한 줄 요약**: 모델 회사이면서 컨텍스트를 실어 나르는 **표준(MCP, Agent Skills)을 만들어 재단에 넘기고**, API 안에는 압축·정리·기억 같은 "창 관리" 부품을 직접 넣는 전략.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Model Context Protocol (MCP) | 에이전트가 외부 도구·데이터에 붙는 공통 규격 | 오픈 표준, AAIF(리눅스재단)에 이관 | L1 | https://www.techrepublic.com/article/news-anthropic-agent-skills-foundation-handover/ (2차) |
| Agent Skills | 지침+스크립트+자료를 폴더로 묶어 필요할 때만 불러오는 업무 절차 패키지 | 2025-12 오픈 표준, 2026-10-22 AAIF 기증 | L4, L6 | 같은 URL (2차) |
| 컨텍스트 편집 + 메모리 도구 (API) | 오래된 도구 결과를 자동 삭제, 파일 기반 기억 디렉터리에 저장·조회 | Public beta, 2025-09-29 | L5, L6 | https://claude.com/blog/context-management (공식) |
| 서버측 압축(Compaction) | 토큰 임계치에서 대화를 서버가 요약해 이어감 | Beta, 2026-01 (헤더 compact-2026-01-12) | L6 | https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools (공식 쿡북, 세부는 검색 요약) |
| Claude Managed Agents | 기업 에이전트를 Anthropic이 호스팅하는 실행 환경 | Public beta, 2026-04-09 | L6, L7, GOV | https://pasqualepillitteri.it/en/news/755/anthropic-managed-agents-cowork-ga-april-9-2026 (2차) |
| Managed Agents Memory | 파일시스템으로 마운트된 기억 저장소, 범위별 권한·변경 감사·롤백·다중 에이전트 공유 | Public beta, 2026-04-23 | L5, GOV | https://claude.com/blog/claude-managed-agents-memory (공식) |

**2026 움직임**: 10-22 Agent Skills를 AAIF에 기증(설치 약 2.8억 건 주장) / 04-23 Managed Agents 메모리 공개 베타 / 04-09 Managed Agents·Cowork 발표 / 01 서버측 압축 베타.

**불확실**: 압축 API의 정확한 지원 모델·임계값은 2차 요약에만 의존. Claude 앱(Enterprise) 쪽 커넥터·소비자용 메모리의 2026 상태는 이번에 확인하지 못함. Managed Agents의 GA 여부 미확인.

## 2. OpenAI

**한 줄 요약**: ChatGPT를 업무 창구로 삼고, **Frontier로 "전사 공유 컨텍스트 + 에이전트 신원·권한"을 플랫폼화**해 자사·타사 에이전트를 모두 관리하려는 전략. 노코드 빌더는 정리하고 SDK 중심으로 이동.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| OpenAI Frontier | CRM·티켓·DW를 연결한 "기업용 시맨틱 레이어" + 에이전트 온보딩·피드백 학습·신원·권한, 타사 에이전트도 관리 | 발표/제한 제공, 2026-02-05 | L1, L2(◐), L5, GOV | https://openai.com/index/introducing-openai-frontier/ (공식·본문 미확인), https://the-decoder.com/openais-frontier-gives-ai-agents-employee-like-identities-shared-context-and-enterprise-permissions/ (2차) |
| ChatGPT Company knowledge | 관리자가 승인한 커넥터로 사내 시스템을 검색, 사용자 권한 그대로 상속 | GA(Business/Enterprise/Edu), 2025-10 | L1, GOV | https://venturebeat.com/ai/openai-launches-company-knowledge-in-chatgpt-letting-you-access-your-firms (2차) |
| AgentKit — Connector Registry | ChatGPT·API 전반의 커넥터/MCP를 중앙 관리 | GA, 2025-10-06 | L1, GOV | https://openai.com/blog/introducing-agentkit (공식·본문 미확인) |
| AgentKit — Agent Builder / Evals | 시각적 워크플로우 빌더·평가 | **2026-11-30 종료 예정** (Agents SDK로 이전 권고) | L4, OBS | 같은 URL (검색 요약) |
| Agents SDK | 코드로 에이전트·핸드오프·가드레일 구성 | GA | L6, L7 | 같은 URL (검색 요약) |

**2026 움직임**: 02-05 Frontier 발표 / 2026 하반기 Agent Builder·Evals 종료 공지(11-30).

**불확실**: Frontier 공식 페이지 403으로 본문 직접 확인 못함 — "시맨틱 레이어"가 지표 정의까지 포함하는지 불분명(L2 ◐). ChatGPT 메모리·Responses API의 컨텍스트 기능 2026 변화는 조사 범위 밖.

## 3. Glean

**한 줄 요약**: 전사 검색으로 쌓은 커넥터·권한 인덱스를 **Enterprise Graph + 개인별 Personal Graph**로 확장하고, 이를 MCP로 다른 AI 도구에도 내주는 "컨텍스트 공급자" 전략.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Enterprise Graph | 사람·프로젝트·문서·시스템 관계를 묶은 회사 지식 그래프 | GA, 2025-09-25 | L1, L3 | https://www.glean.com/press/glean-introduces-third-generation-ai-assistant-new-enterprise-graph-to-enable-the-superintelligent-enterprise (공식) |
| Personal Graph | 개인의 업무·협업자·작업 방식 추정, 사용자가 보고 수정·삭제 가능 | GA, 2026-02 편집 기능 | L3, L5 | https://www.glean.com/press/gleans-latest-ai-assistant-moves-every-employee-from-insight-to-execution (공식, 날짜 미표기) |
| Glean Agents | 그래프를 쓰는 에이전트, 원격 MCP 도구 호출(2026-03), 읽기/쓰기 도구 분리(2026-08) | GA | L4, L7 | https://docs.glean.com/release-notes/releases/2026-03-11-march-release (공식) |
| Glean MCP 서버 (읽기 도구·memory via MCP) | Claude Code·Cursor·ChatGPT가 Glean 검색·기억을 쓰게 함 | GA (2026-06 확대, 2026-08 메모리 GA 보도) | L1, L5 | https://docs.glean.com/release-notes/releases/2026-06-17-june-release (공식), https://siliconangle.com/?p=830044 (2차) |
| Independent agents / AI Gateway | 고유 신원·범위 자격증명·감사 기록을 가진 자율 에이전트, 모델 라우팅 | Beta, 2026-08 | GOV, L6 | https://siliconangle.com/?p=830044 (2차) |
| Headless agent building | 에이전트를 코드로 버전관리·테스트·배포 | 발표, 2026-10-21 | L4, OBS(◐) | https://www.unite.ai/?p=491722 (2차) |

**2026 움직임**: 10-21 헤드리스 에이전트 빌드 / 08 Glean:GO — Tau 데스크톱, 독립 에이전트·AI Gateway 베타 / 06 모든 읽기 도구 MCP 노출 / 03 에이전트의 원격 MCP 호출 / 02 Personal Graph 가시화·편집.

**불확실**: Tau·Skills via MCP는 미출시. 2월 보도자료 원문에 날짜 표기 없음.

## 4. Cohere

**한 줄 요약**: 규제 산업용 **프라이빗 배포** 우선. North(에이전트 작업공간) 안에 숨어 있던 검색 엔진 Compass를 독립 관리형 서비스+MCP 서버로 분리해 내놓는 중.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| North | 직원용 에이전트 작업공간(HR·재무·IT 업무), 온프레미스 가능 | GA, 2025-08 | L4, L7, GOV | https://techcrunch.com/2025/08/06/coheres-new-ai-agent-platform-north-promises-to-keep-enterprise-data-secure/ (2차) |
| Compass Cloud | 연결→파싱→임베딩→색인→검색→재랭킹→거버넌스 7단계 관리형 검색, 검색 시 권한 적용 | Private beta, 2026-09-25 | L1, L6, GOV | https://www.unite.ai/?p=473831 (2차) |
| Compass MCP 서버 | 검색을 MCP 도구로 노출, 에이전트가 검색 범위를 좁힘 | Private beta, 2026-09-25 | L1 | 같은 URL (2차) |
| Rerank 4 (Pro/Fast) | 후보 문서 재정렬로 창에 넣을 내용 선별 | GA (Pinecone 통해 4.0 Fast 2026-07) | L6 | https://docs.pinecone.io/nexus-release-notes/2026.md (Pinecone 공식) |

**2026 움직임**: 09-25 Compass Cloud 비공개 베타 + MCP 서버 / SAP과 에이전트 파트너십(날짜 미확인).

**불확실**: 2026 자료 대부분이 2차. Cohere 뉴스룸 원문 미확인. 자체 벤치마크(nDCG 64.8→81.1)는 검증 안 됨.

## 5. LangChain

**한 줄 요약**: 오픈소스 프레임워크(LangChain/LangGraph/Deep Agents)로 **컨텍스트 조작 방식 자체를 개발자에게 주고**, 돈은 LangSmith(관측·평가·호스팅)에서 버는 구조.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| LangChain 1.x (미들웨어) | 모델 호출 전후에 요약·도구 필터·승인 등을 끼우는 미들웨어, v1.4에서 FastMCP 지원 | GA (1.0: 2025-10, 1.4: 2026) | L1, L6 | https://www.langchain.com/blog/langchain-langgraph-1dot0 (공식), https://www.langchain.com/blog/october-2026-langchain-newsletter (공식) |
| LangGraph | 상태 그래프 기반 실행, 체크포인트·사람 개입 중단점 | GA | L6, L7, L5(◐) | https://www.langchain.com/blog/langchain-langgraph-1dot0 (공식) |
| Deep Agents | 계획·하위 에이전트·파일시스템을 갖춘 오픈소스 하네스, "창을 가볍게 유지" | GA(OSS) | L4, L6 | 뉴스레터 (공식) |
| Managed Deep Agents (LangSmith) | 호스팅형 Deep Agents, v0.9에서 사용자 단위 메모리·스케줄링 | 2026-10 v0.9 | L5, L6 | 뉴스레터 (공식) |
| LangSmith (Trajectories, AI Search, Engine v2) | 트레이스 의미 검색, 하위 에이전트 포함 세션 궤적, 레드팀·비효율 탐지, 궤적→파인튜닝 데이터 | GA, 2026-10 기능 추가 | OBS, L5 | 뉴스레터 (공식) |
| LangMem | 장기 기억 추출·관리 SDK | GA(OSS) | L5 | (이번 조사에서 2026 공식 근거 미확인) |

**2026 움직임**: 10-15 Interrupt 발표 정리 — Managed Deep Agents v0.9, LangSmith Engine v2·Trajectories·AI Search·파인튜닝, LangChain 1.4 FastMCP / 2026 상반기 Deep Agents 본격화.

**불확실**: LangGraph 1.2 등 세부 버전은 2차 출처. LangMem의 현재 상태 미확인.

## 6. LlamaIndex

**한 줄 요약**: "RAG 프레임워크"에서 **문서를 정확히 파싱·추출해 에이전트에 넣는 "에이전트형 문서 처리" 회사**로 좁혀 재정의(LlamaCloud→LlamaParse 브랜드 통합).

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| LlamaParse (구 LlamaCloud 플랫폼) | 복잡한 문서(PDF·표·이미지) 파싱, 분류 | GA, 2026-02 리브랜딩 | L1 | https://llamaindex.ai/blog/llamaindex-newsletter-2026-02-24 (공식) |
| LlamaExtract / Extract v2.5 | 스키마 기반 구조화 추출, 페이지 단위 인용(바운딩박스) | GA, v2.5 2026-10-01 | L1, L7(근거) | https://www.unite.ai/llamaindex-launches-extract-v2-5-with-accuracy-and-grounding-gains/ (2차), 뉴스레터 (공식) |
| Index (LlamaCloud Index) | 관리형 검색 색인 | GA | L1, L6 | 뉴스레터 (공식) |
| LlamaAgents / Workflows | 문서 에이전트 빌더, 이벤트 기반 워크플로우 오케스트레이션 | LlamaAgents 프리뷰, Workflows 1.0 | L4, L6 | 뉴스레터 (공식), https://rywalker.com/research/llamaindex (2차) |
| LlamaParse MCP 서버 | Parse·Classify·Extract·Index를 MCP로 노출 (EU 리전 포함) | GA, 2026-06/08 | L1 | https://developers.llamaindex.ai/llamaparse/changelog/2026-08/ (공식) |
| LiteParse | 로컬 실행 오픈소스 파서 | GA(OSS), 2026-03-19 | L1 | (2차 요약) |

**2026 움직임**: 10-01 Extract v2.5 / 08 .NET SDK·EU MCP / 06 MCP 서버에 Extract·Index 추가 / 03 LiteParse / 02 LlamaCloud→LlamaParse.

**불확실**: LlamaAgents GA 여부 미확인. 사용자 수(30만+)는 회사 주장.

## 7. Mem0

**한 줄 요약**: 어떤 에이전트에도 붙는 **범용 장기 기억 레이어**. 2026년엔 알고리즘을 갈아엎고 그래프 메모리를 내장, 코딩 에이전트·자동화 도구 플러그인으로 저변 확대.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Mem0 Platform (관리형) | 대화에서 사실 추출·저장·검색, 프로젝트별 설정 | GA | L5, L6 | https://docs.mem0.ai/changelog/highlights (공식) |
| 새 메모리 알고리즘 (SDK v2/v3) | 하이브리드 검색, 추가 전용(ADD-only) 추출, 내장 그래프 메모리(외부 그래프DB 불필요) | GA, 2026-04-14 | L3(◐), L5 | 같은 URL (공식) |
| Memory Decay | 최근 사용 기억 쪽으로 검색 순위 가중(삭제 아님) | GA(옵트인), 2026-05 | L6 | 같은 URL (공식) |
| Mem0 OSS / OpenMemory | 자가 호스팅 SDK, 로컬 MCP 메모리 서버 | GA(OSS) | L5, L1 | https://docs.mem0.ai/changelog/sdk (공식) |
| 통합 플러그인 (MCP·n8n·Zapier·Strands·Vercel 등) | 코딩 에이전트·워크플로우 도구에 기억 액션 제공 | GA, 2026-06~08 | L1 | highlights (공식) |

**2026 움직임**: 08-24 DeepSeek Harness·Strands 통합 / 07-30 n8n·Zapier / 05 Memory Decay / 04-14 알고리즘 재작성(LoCoMo 71.4→91.6 자사 주장), 외부 그래프 스토어 제거.

**불확실**: 2025-10 시리즈A(총 2,400만 달러) 이후 2026 투자 없음. 벤치마크는 Zep과 상호 반박 중.

## 8. Zep

**한 줄 요약**: 대화 기억 서비스에서 출발해 **"신뢰할 수 있는 에이전트를 위한 엔터프라이즈 컨텍스트 레이어"**로 재포지셔닝 — 업무 데이터를 시간축 그래프로 통합하고, 에이전트 실행 기록에서 스킬을 뽑아낸다.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Graphiti (OSS) | 사실이 바뀌면 지우지 않고 유효기간을 기록하는 시간축 지식그래프, 의미+키워드+그래프 검색 | GA(OSS, Apache 2.0) | L3, L5 | https://github.com/getzep/graphiti (공식) |
| Context Lake / Context Graphs | Slack·Drive·Snowflake·Databricks 등을 동기화해 통제된 그래프로, 런타임 질의 | GA | L1, L3 | https://www.getzep.com/ (공식) |
| Zep Agent Skills | 에이전트 작업 트레이스를 따라야 할 스킬로 변환 | 발표, 2026-11-05 | L4, L5 | https://www.getzep.com/ (공식, 블로그 제목) |
| Agent memory | 사용자별 최신 기억 유지 | GA | L5 | 같은 URL (공식) |
| 거버넌스 (ABAC·보존·법적보관·감사·BYOK/BYOC) | 에이전트별로 꺼낼 수 있는 컨텍스트·스킬 통제 | GA | GOV | 같은 URL (공식) |

**2026 움직임**: 11-05 Agent Skills / 10-29 "사실마다 두 개의 타임라인" 글 / 04 451 Research 리포트 / 2026 중 "context engineering platform"→"enterprise context layer" 메시지 전환.

**불확실**: Graphiti 별 수 등 지표는 출처마다 다름. 벤치마크 수치 논쟁(Mem0 반박) 미해결.

## 9. Letta

**한 줄 요약**: MemGPT 계보의 상태 보존 에이전트 회사. 2026-03 **서버측 메모리 도구를 버리고 git으로 관리되는 파일 "컨텍스트 저장소"**로 기억을 옮기고, 메모리 우선 코딩/로컬 에이전트 Letta Code를 주력으로 전환.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Letta Code (+SDK) | 모델 무관 에이전트 하네스, 로컬 컴퓨터에서 행동, 지속 기억 | 주력, 2026-03-16 | L5, L6, L7 | https://letta.com/blog/our-next-phase (공식) |
| Context Repositories (MemFS) | 기억을 git 백업 파일로 저장, 에이전트가 bash로 직접 편집 | 2026-03 도입 | L5 | 같은 URL (공식) |
| 클라이언트측 서브에이전트 (구 sleep-time) | 유휴 시간에 기억 정리·통합을 클라이언트에서 수행 | 2026-03 전환 | L5, L6 | 같은 URL (공식), https://letta.com/blog/sleep-time-compute (공식, 2025-04) |
| Letta API (서버) | 에이전트 기본 원시 기능 제공, 도구 규칙·템플릿·Filesystem·서버 MCP 등은 단계적 폐지 | GA(축소 중) | L1(◐), L5 | our-next-phase (공식) |

**2026 움직임**: 03-16 "다음 단계" — Letta Code 주력화, 기억 구조 전환, 2026-04 중순까지 템플릿·Filesystem 폐지.

**불확실**: "Letta Agent" 개명(2026-07)은 2차 1건뿐이라 미반영. 이후 GA·가격 미확인.

## 10. Pinecone

**한 줄 요약**: 벡터 DB에서 **"에이전트용 지식 엔진"**으로 — 질문 시점에 원문을 찾는 대신, 권한·버전·출처·PII 태그를 붙인 컨텍스트를 **미리 컴파일**해 두고 선언형 질의로 꺼낸다.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Pinecone Nexus (Context Compiler + Composable Retriever, KnowQL) | 지식을 사전 컴파일한 산출물로 만들고 선언형 언어로 조회 | GA, 2026-08-06 | L1, L3(◐), L6, GOV(◐) | https://docs.pinecone.io/nexus-release-notes/2026.md (공식), https://infoq.com/news/2026/07/pinecon-nexus-knowledge-engine (2차) |
| Pinecone Assistant (+Assistant MCP 서버) | 문서 업로드→청킹·검색·인용 답변 관리형 RAG | GA, MCP 2026-03-26 | L1, L6 | release notes (공식) |
| Pinecone MCP 서버 | 인덱스를 에이전트 도구로 노출 | GA, 2026-03-26 | L1 | 같은 URL (공식) |
| 전문(Full-text) 검색 + Documents API | 키워드+벡터 하이브리드 | GA, 2026-09-02 | L1, L6 | 같은 URL (공식) |
| RBAC 확장 / SAML·SCIM | 조직·프로젝트 역할 | GA, 2026-07 | GOV | 같은 URL (공식) |

**2026 움직임**: 09-02 전문 검색 / 08-25 BYOC / 08-06 Nexus GA / 07-01 Nexus 공개 프리뷰 / 05 얼리액세스 / 03-26 MCP 서버 GA.

**불확실**: Nexus "작업 완료율 100%·토큰 90% 절감"은 자사 수치. Context Compiler 세부는 공식 릴리스노트에 없음(2차 근거).

## 11. Elastic

**한 줄 요약**: 검색엔진을 **"컨텍스트 엔지니어링의 토대"**로 재정의 — 하이브리드 검색·ES|QL·보안을 묶은 Agent Builder로 데이터 옆에서 에이전트를 만들고, 에이전트 트레이스를 다시 컨텍스트로 되먹임.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Agent Builder | 인덱스·데이터스트림을 도구로 삼는 에이전트, MCP·A2A 지원 | GA, 2026-01-22 | L1, L6, L7 | https://www.businesswire.com/news/home/20260122544127/en/ (공식·본문 미확인), https://www.helpnetsecurity.com/2026/01/23/elastic-agent-builder-2/ (2차) |
| Elastic Workflows | 오케스트레이션·실행 담당 | Tech preview, 2026-01 | L4, L7 | https://www.constellationr.com/insights/news/elastics-agent-builder-generally-available-elastic-workflows-tech-preview (2차) |
| 하이브리드 검색 / ES|QL 도구 | 벡터+키워드 검색, 질의 언어 기반 도구 | GA | L1, L6 | https://www.elastic.co/search-labs/blog/context-engineering-for-agents (공식) |
| 트레이스→컨텍스트 피드백 (OTel) | 에이전트 상호작용 트레이스를 새 컨텍스트 소스로 재사용 | GA(구성 패턴) | L5, OBS | 같은 블로그 (공식) |
| 보안·권한(문서 수준 보안) | 기존 Elastic RBAC 적용 | GA | GOV | (2차 요약) |

**2026 움직임**: 01-22 Agent Builder GA + Workflows 기술 프리뷰 / AWS Agentic AI 전문 파트너.

**불확실**: 보도자료 원문 403. 메모리 전용 기능 유무 미확인.

## 12. Writer

**한 줄 요약**: 마케팅·매출 조직용 풀스택 에이전트 플랫폼. 그래프 RAG(Knowledge Graph) 위에 **브랜드 규칙·결정 로직·팀 기억을 묶은 "Enterprise Brain" 컨텍스트 레이어**를 얹는 중.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Knowledge Graph | 사내 문서·웹페이지를 그래프 기반 RAG로 근거 제공 | GA | L1, L3 | https://atlan.com/know/ai-agent/context-layer/writer-knowledge-graph-vs-enterprise-context-layer/ (2차) |
| Enterprise Brain | 브랜드 지식·결정 로직·실시간 업무 데이터(계정·캠페인)를 모든 에이전트 밑에 깔린 통제된 컨텍스트로 | Early access, 2026-09-09 | L2(◐), L3, L4, GOV | https://www.cmswire.com/customer-experience/writer-launches-enterprise-brain-to-unify-ai-agent-context/ (2차) |
| Agent Memory | 팀 단위로 결정·선호를 세션 넘어 유지 | GA, 2026-09-09 | L5 | 같은 URL (2차) |
| AI HQ (Agent Builder, Writer Home) | 에이전트 개발·100+ 사전 에이전트 | GA, 2025-04-10 | L4, L7 | https://writer.com/blog/writer-ai-hq-press-release/ (공식) |
| Skills 라이브러리 | 200+ 업무 스킬 | GA | L4 | (2차 요약) |

**2026 움직임**: 09-09 Enterprise Brain(EA)·Agent Memory·Writer Meet·Writer for Slack(GA).

**불확실**: Writer 공식 블로그의 Enterprise Brain 원문 미확인. Knowledge Graph와 Enterprise Brain의 관계(대체/상위) 불분명.

## 13. Contextual AI

**한 줄 요약**: "RAG 2.0" 연구진 회사. 반도체·항공·제조 같은 **기술 문서 중심 업무에서 컨텍스트 관리와 가드레일을 맡는 하네스(Agent Composer)**로 확장.

| 제품 | 무엇을 하나 | 상태 | 층 | 근거 |
|---|---|---|---|---|
| Agent Composer | 검색 도구·MCP·LLM 부품을 시각/YAML/자연어로 조합, 컨텍스트 관리·가드레일 | Public preview, 2026-01-27 | L4, L6, L7 | https://docs.contextual.ai/release-notes/2026.md (공식) |
| Datastores (+Global Datastores) | 문서 파싱·색인 저장소, 데모용 공용 저장소 | GA, 2026-02-10 | L1 | 같은 URL (공식) |
| Grounded generation / 출처 표시 | 답변에 근거·웹 검색 출처 첨부 | GA, 2026-02-02 | L7 | 같은 URL (공식) |
| Reranker / Parser | 지시 따르는 재랭커, 문서 파서 | GA | L1, L6 | https://contextual.ai/platform (공식) |

**2026 움직임**: 02-10 공용 데이터스토어 / 01-27 Agent Composer 공개 프리뷰(제조사 근본원인분석 8시간→20분 주장).

**불확실**: 경영진 교체(임시 CEO) 보도는 2차 1건 — 회사 상황 확인 필요. Composer GA 시점 미확인.

---

## 데이터 블록

```yaml
- vendor: anthropic
  name: Anthropic
  category: ai_lab
  products:
    - id: anthropic-mcp
      name: Model Context Protocol
      status: GA
      status_date: 2025-12
      layers: {L1: ●}
      x: 1
      y: 1
      xy_reason: "도구·데이터 연결 규격, 에이전트가 런타임에 도구를 발견해 씀"
      maturity: 2
      evidence: [ {url: "https://www.techrepublic.com/article/news-anthropic-agent-skills-foundation-handover/", kind: secondary, date: 2026-10-22} ]
    - id: anthropic-agent-skills
      name: Agent Skills
      status: GA
      status_date: 2026-10
      layers: {L4: ●, L6: ◐}
      x: 1
      y: -1
      xy_reason: "사람이 작성한 절차 패키지, 필요 시 점진적 로드"
      maturity: 2
      evidence: [ {url: "https://www.techrepublic.com/article/news-anthropic-agent-skills-foundation-handover/", kind: secondary, date: 2026-10-22} ]
    - id: anthropic-context-editing-memory-tool
      name: Context editing + Memory tool (API)
      status: preview
      status_date: 2025-09
      layers: {L5: ●, L6: ●}
      x: 0
      y: 2
      xy_reason: "에이전트가 스스로 기억을 쓰고 창을 정리"
      maturity: 1
      evidence: [ {url: "https://claude.com/blog/context-management", kind: official, date: 2025-09-29} ]
    - id: anthropic-compaction
      name: Server-side compaction
      status: preview
      status_date: 2026-01
      layers: {L6: ●}
      x: 0
      y: 2
      xy_reason: "런타임 자동 요약"
      maturity: 1
      evidence: [ {url: "https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools", kind: official, date: 2026-03-20} ]
    - id: anthropic-managed-agents-memory
      name: Claude Managed Agents + Memory
      status: preview
      status_date: 2026-04
      layers: {L5: ●, L6: ●, L7: ●, GOV: ●}
      x: 1
      y: 2
      xy_reason: "호스팅 에이전트가 세션 경험을 기억에 축적, 범위 권한·감사·롤백"
      maturity: 5
      evidence: [ {url: "https://claude.com/blog/claude-managed-agents-memory", kind: official, date: 2026-04-23} ]
- vendor: openai
  name: OpenAI
  category: ai_lab
  products:
    - id: openai-frontier
      name: OpenAI Frontier
      status: announced
      status_date: 2026-02
      layers: {L1: ●, L2: ◐, L5: ◐, GOV: ●}
      x: 1
      y: 0
      xy_reason: "시스템 연결로 공유 업무 컨텍스트 구성 + 피드백 학습"
      maturity: 3
      evidence: [ {url: "https://openai.com/index/introducing-openai-frontier/", kind: official, date: 2026-02-05}, {url: "https://the-decoder.com/openais-frontier-gives-ai-agents-employee-like-identities-shared-context-and-enterprise-permissions/", kind: secondary, date: 2026-02-05} ]
    - id: openai-company-knowledge
      name: ChatGPT Company knowledge
      status: GA
      status_date: 2025-10
      layers: {L1: ●, GOV: ●}
      x: -1
      y: 1
      xy_reason: "질문에 답하려 사내 소스를 런타임 검색, 권한 상속"
      maturity: 1
      evidence: [ {url: "https://venturebeat.com/ai/openai-launches-company-knowledge-in-chatgpt-letting-you-access-your-firms", kind: secondary, date: 2025-10-23} ]
    - id: openai-connector-registry
      name: AgentKit Connector Registry
      status: GA
      status_date: 2025-10
      layers: {L1: ●, GOV: ●}
      x: 0
      y: -1
      xy_reason: "관리자가 커넥터·MCP를 중앙 등록"
      maturity: 2
      evidence: [ {url: "https://openai.com/blog/introducing-agentkit", kind: official, date: 2025-10-06} ]
    - id: openai-agents-sdk
      name: Agents SDK
      status: GA
      status_date: 2025-03
      layers: {L6: ●, L7: ●}
      x: 1
      y: 1
      xy_reason: "코드 기반 오케스트레이션·가드레일"
      maturity: 4
      evidence: [ {url: "https://openai.com/blog/introducing-agentkit", kind: official, date: 2025-10-06} ]
- vendor: glean
  name: Glean
  category: agent_platform
  products:
    - id: glean-enterprise-graph
      name: Enterprise Graph
      status: GA
      status_date: 2025-09
      layers: {L1: ●, L3: ●, GOV: ●}
      x: 0
      y: 0
      xy_reason: "커넥터로 자동 구축되는 관계 그래프, 권한 반영"
      maturity: 1
      evidence: [ {url: "https://www.glean.com/press/glean-introduces-third-generation-ai-assistant-new-enterprise-graph-to-enable-the-superintelligent-enterprise", kind: official, date: 2025-09-25} ]
    - id: glean-personal-graph
      name: Personal Graph
      status: GA
      status_date: 2026-02
      layers: {L3: ●, L5: ●}
      x: 1
      y: 2
      xy_reason: "사용 행동에서 개인 업무 맥락을 자동 추정, 사용자가 교정"
      maturity: 5
      evidence: [ {url: "https://www.glean.com/press/gleans-latest-ai-assistant-moves-every-employee-from-insight-to-execution", kind: official, date: 2026-02-17} ]
    - id: glean-agents
      name: Glean Agents
      status: GA
      status_date: 2026-03
      layers: {L4: ●, L7: ●, GOV: ◐}
      x: 1
      y: 1
      xy_reason: "원격 MCP 도구로 업무 실행, 읽기/쓰기 분리"
      maturity: 3
      evidence: [ {url: "https://docs.glean.com/release-notes/releases/2026-03-11-march-release", kind: official, date: 2026-03-11}, {url: "https://docs.glean.com/release-notes/releases/2026-08-18-august-release", kind: official, date: 2026-08-18} ]
    - id: glean-mcp-server
      name: Glean MCP server (read tools, memory)
      status: GA
      status_date: 2026-06
      layers: {L1: ●, L5: ◐}
      x: 0
      y: 1
      xy_reason: "외부 에이전트가 런타임에 Glean 컨텍스트를 끌어씀"
      maturity: 2
      evidence: [ {url: "https://docs.glean.com/release-notes/releases/2026-06-17-june-release", kind: official, date: 2026-06-17}, {url: "https://siliconangle.com/?p=830044", kind: secondary, date: 2026-08} ]
    - id: glean-independent-agents
      name: Independent agents / AI Gateway
      status: preview
      status_date: 2026-08
      layers: {GOV: ●, L6: ◐}
      x: 2
      y: 1
      xy_reason: "고유 신원·자격증명·감사 기록을 가진 자율 실행"
      maturity: 3
      evidence: [ {url: "https://siliconangle.com/?p=830044", kind: secondary, date: 2026-08} ]
    - id: glean-headless-agent-building
      name: Headless agent building
      status: announced
      status_date: 2026-10
      layers: {L4: ●, OBS: ◐}
      x: 1
      y: -1
      xy_reason: "에이전트를 코드로 버전관리·테스트"
      maturity: 4
      evidence: [ {url: "https://www.unite.ai/?p=491722", kind: secondary, date: 2026-10-21} ]
- vendor: cohere
  name: Cohere
  category: ai_lab
  products:
    - id: cohere-north
      name: North
      status: GA
      status_date: 2025-08
      layers: {L4: ●, L7: ●, GOV: ●}
      x: 1
      y: 0
      xy_reason: "직원 업무 에이전트 작업공간, 프라이빗 배포"
      maturity: 2
      evidence: [ {url: "https://techcrunch.com/2025/08/06/coheres-new-ai-agent-platform-north-promises-to-keep-enterprise-data-secure/", kind: secondary, date: 2025-08-06} ]
    - id: cohere-compass-cloud
      name: Compass Cloud (+MCP server)
      status: preview
      status_date: 2026-09
      layers: {L1: ●, L6: ●, GOV: ●}
      x: -1
      y: 1
      xy_reason: "에이전트가 MCP로 검색 범위를 정해 런타임 검색, 검색 시 권한"
      maturity: 2
      evidence: [ {url: "https://www.unite.ai/?p=473831", kind: secondary, date: 2026-09-25} ]
    - id: cohere-rerank
      name: Rerank 4
      status: GA
      status_date: 2026-07
      layers: {L6: ●}
      x: -1
      y: 1
      xy_reason: "질의별 후보 재정렬로 창 내용 선별"
      maturity: 1
      evidence: [ {url: "https://docs.pinecone.io/nexus-release-notes/2026.md", kind: official, date: 2026-07-01} ]
- vendor: langchain
  name: LangChain
  category: agent_platform
  products:
    - id: langchain-langchain-middleware
      name: LangChain 1.x (middleware, FastMCP)
      status: GA
      status_date: 2026-10
      layers: {L1: ●, L6: ●, GOV: ◐}
      x: 1
      y: 1
      xy_reason: "요약·도구 선택·승인을 미들웨어로 런타임 조작"
      maturity: 3
      evidence: [ {url: "https://www.langchain.com/blog/langchain-langgraph-1dot0", kind: official, date: 2025-10-22}, {url: "https://www.langchain.com/blog/october-2026-langchain-newsletter", kind: official, date: 2026-10-15} ]
    - id: langchain-langgraph
      name: LangGraph
      status: GA
      status_date: 2025-10
      layers: {L5: ◐, L6: ●, L7: ●}
      x: 1
      y: 0
      xy_reason: "개발자가 그래프 정의, 실행 중 상태 보존·중단점"
      maturity: 3
      evidence: [ {url: "https://www.langchain.com/blog/langchain-langgraph-1dot0", kind: official, date: 2025-10-22} ]
    - id: langchain-deep-agents
      name: Deep Agents / Managed Deep Agents
      status: GA
      status_date: 2026-10
      layers: {L4: ●, L5: ●, L6: ●}
      x: 1
      y: 2
      xy_reason: "계획·하위 에이전트·파일시스템으로 스스로 컨텍스트 관리, 사용자 메모리"
      maturity: 3
      evidence: [ {url: "https://www.langchain.com/blog/october-2026-langchain-newsletter", kind: official, date: 2026-10-15} ]
    - id: langchain-langsmith
      name: LangSmith
      status: GA
      status_date: 2026-10
      layers: {OBS: ●, L5: ◐}
      x: 0
      y: 1
      xy_reason: "트레이스·궤적 분석에서 개선·파인튜닝 데이터 생산"
      maturity: 5
      evidence: [ {url: "https://www.langchain.com/blog/october-2026-langchain-newsletter", kind: official, date: 2026-10-15} ]
- vendor: llamaindex
  name: LlamaIndex
  category: memory_retrieval
  products:
    - id: llamaindex-llamaparse
      name: LlamaParse (formerly LlamaCloud)
      status: GA
      status_date: 2026-02
      layers: {L1: ●}
      x: -1
      y: -1
      xy_reason: "문서를 사전에 파싱·색인하는 파이프라인"
      maturity: 1
      evidence: [ {url: "https://llamaindex.ai/blog/llamaindex-newsletter-2026-02-24", kind: official, date: 2026-02-24} ]
    - id: llamaindex-extract
      name: LlamaExtract (Extract v2.5)
      status: GA
      status_date: 2026-10
      layers: {L1: ●, L7: ◐}
      x: 0
      y: -1
      xy_reason: "사람이 정의한 스키마로 구조화 추출, 페이지 인용"
      maturity: 4
      evidence: [ {url: "https://www.unite.ai/llamaindex-launches-extract-v2-5-with-accuracy-and-grounding-gains/", kind: secondary, date: 2026-10-01}, {url: "https://llamaindex.ai/blog/llamaindex-newsletter-2026-02-24", kind: official, date: 2026-02-24} ]
    - id: llamaindex-index
      name: LlamaCloud Index
      status: GA
      status_date: 2026-02
      layers: {L1: ●, L6: ◐}
      x: -1
      y: 0
      xy_reason: "관리형 검색 색인"
      maturity: 1
      evidence: [ {url: "https://llamaindex.ai/blog/llamaindex-newsletter-2026-02-24", kind: official, date: 2026-02-24} ]
    - id: llamaindex-llamaagents-workflows
      name: LlamaAgents / Workflows
      status: preview
      status_date: 2026-02
      layers: {L4: ●, L6: ●}
      x: 1
      y: 0
      xy_reason: "문서 업무 에이전트를 워크플로우로 정의"
      maturity: 2
      evidence: [ {url: "https://llamaindex.ai/blog/llamaindex-newsletter-2026-02-24", kind: official, date: 2026-02-24}, {url: "https://rywalker.com/research/llamaindex", kind: secondary, date: 2026} ]
    - id: llamaindex-mcp
      name: LlamaParse MCP server
      status: GA
      status_date: 2026-08
      layers: {L1: ●}
      x: -1
      y: 1
      xy_reason: "에이전트가 파싱·추출·색인을 도구로 호출"
      maturity: 2
      evidence: [ {url: "https://developers.llamaindex.ai/llamaparse/changelog/2026-08/", kind: official, date: 2026-08} ]
- vendor: mem0
  name: Mem0
  category: memory_retrieval
  products:
    - id: mem0-platform
      name: Mem0 Platform (v3 algorithm, built-in graph memory)
      status: GA
      status_date: 2026-04
      layers: {L3: ◐, L5: ●, L6: ◐}
      x: 0
      y: 2
      xy_reason: "대화에서 사실을 자동 추출·축적하고 런타임 검색"
      maturity: 5
      evidence: [ {url: "https://docs.mem0.ai/changelog/highlights", kind: official, date: 2026-04-14} ]
    - id: mem0-memory-decay
      name: Memory Decay
      status: GA
      status_date: 2026-05
      layers: {L6: ●}
      x: 0
      y: 2
      xy_reason: "최근 사용 기억에 가중치, 자동 순위 조정"
      maturity: 5
      evidence: [ {url: "https://docs.mem0.ai/changelog/highlights", kind: official, date: 2026-05-08} ]
    - id: mem0-oss-openmemory
      name: Mem0 OSS / OpenMemory MCP
      status: GA
      status_date: 2026-04
      layers: {L1: ●, L5: ●}
      x: 0
      y: 2
      xy_reason: "자가 호스팅 기억 레이어, MCP로 여러 도구 공유"
      maturity: 2
      evidence: [ {url: "https://docs.mem0.ai/changelog/sdk", kind: official, date: 2026-04-14} ]
    - id: mem0-integrations
      name: Integrations (n8n, Zapier, Strands, coding-agent plugins)
      status: GA
      status_date: 2026-08
      layers: {L1: ●}
      x: 1
      y: 1
      xy_reason: "워크플로우·코딩 에이전트에 기억 액션 삽입"
      maturity: 1
      evidence: [ {url: "https://docs.mem0.ai/changelog/highlights", kind: official, date: 2026-08-24} ]
- vendor: zep
  name: Zep
  category: knowledge_graph
  products:
    - id: zep-graphiti
      name: Graphiti
      status: GA
      status_date: null  # 출시 시점 미확인
      layers: {L3: ●, L5: ●, L6: ◐}
      x: 0
      y: 2
      xy_reason: "에피소드에서 엔티티·관계를 자동 추출, 시간 유효기간 관리"
      maturity: 2
      evidence: [ {url: "https://github.com/getzep/graphiti", kind: official, date: 2026-11-11} ]
    - id: zep-context-lake
      name: Context Lake / Context Graphs
      status: GA
      status_date: 2026-10
      layers: {L1: ●, L3: ●, GOV: ●}
      x: 0
      y: 1
      xy_reason: "선택한 업무 소스를 동기화해 그래프화, 런타임 질의"
      maturity: 2
      evidence: [ {url: "https://www.getzep.com/", kind: official, date: 2026-11-11} ]
    - id: zep-agent-skills
      name: Zep Agent Skills
      status: announced
      status_date: 2026-11
      layers: {L4: ●, L5: ●}
      x: 1
      y: 2
      xy_reason: "에이전트 실행 트레이스에서 스킬을 자동 생성"
      maturity: 5
      evidence: [ {url: "https://www.getzep.com/", kind: official, date: 2026-11-05} ]
    - id: zep-agent-memory
      name: Agent memory (user memory)
      status: GA
      status_date: null  # 출시 시점 미확인
      layers: {L5: ●}
      x: 0
      y: 2
      xy_reason: "사용자별 최신 기억 자동 유지"
      maturity: 2
      evidence: [ {url: "https://www.getzep.com/", kind: official, date: 2026-11-11} ]
- vendor: letta
  name: Letta
  category: memory_retrieval
  products:
    - id: letta-code
      name: Letta Code (+SDK)
      status: GA
      status_date: 2026-03
      layers: {L5: ●, L6: ●, L7: ●}
      x: 1
      y: 2
      xy_reason: "로컬에서 행동하는 메모리 우선 에이전트"
      maturity: 5
      evidence: [ {url: "https://letta.com/blog/our-next-phase", kind: official, date: 2026-03-16} ]
    - id: letta-context-repositories
      name: Context Repositories (MemFS)
      status: GA
      status_date: 2026-03
      layers: {L5: ●}
      x: 0
      y: 2
      xy_reason: "에이전트가 git 백업 파일 기억을 직접 편집"
      maturity: 5
      evidence: [ {url: "https://letta.com/blog/our-next-phase", kind: official, date: 2026-03-16} ]
    - id: letta-reflection-subagents
      name: Client-side reflection subagents (ex sleep-time)
      status: GA
      status_date: 2026-03
      layers: {L5: ●, L6: ●}
      x: 0
      y: 2
      xy_reason: "유휴 시간에 기억을 스스로 정리·통합"
      maturity: 5
      evidence: [ {url: "https://letta.com/blog/our-next-phase", kind: official, date: 2026-03-16}, {url: "https://letta.com/blog/sleep-time-compute", kind: official, date: 2025-04} ]
    - id: letta-api
      name: Letta API (server)
      status: GA
      status_date: 2026-03
      layers: {L1: ◐, L5: ●}
      x: 0
      y: 1
      xy_reason: "에이전트 상태 원시 기능, 서버측 부가기능은 폐지 중"
      maturity: 2
      evidence: [ {url: "https://letta.com/blog/our-next-phase", kind: official, date: 2026-03-16} ]
- vendor: pinecone
  name: Pinecone
  category: memory_retrieval
  products:
    - id: pinecone-nexus
      name: Pinecone Nexus
      status: GA
      status_date: 2026-08
      layers: {L1: ●, L3: ◐, L6: ●, GOV: ◐}
      x: 0
      y: -1
      xy_reason: "설계한 컨텍스트를 사전 컴파일, 선언형 질의로 조회"
      maturity: 2
      evidence: [ {url: "https://docs.pinecone.io/nexus-release-notes/2026.md", kind: official, date: 2026-08-06}, {url: "https://infoq.com/news/2026/07/pinecon-nexus-knowledge-engine", kind: secondary, date: 2026-07} ]
    - id: pinecone-assistant
      name: Pinecone Assistant (+MCP server)
      status: GA
      status_date: 2026-03
      layers: {L1: ●, L6: ●}
      x: -1
      y: 0
      xy_reason: "업로드 문서 기반 인용 답변"
      maturity: 1
      evidence: [ {url: "https://docs.pinecone.io/nexus-release-notes/2026.md", kind: official, date: 2026-03-26} ]
    - id: pinecone-mcp-server
      name: Pinecone MCP server
      status: GA
      status_date: 2026-03
      layers: {L1: ●}
      x: -1
      y: 1
      xy_reason: "에이전트가 인덱스를 도구로 직접 조회"
      maturity: 2
      evidence: [ {url: "https://docs.pinecone.io/nexus-release-notes/2026.md", kind: official, date: 2026-03-26} ]
    - id: pinecone-fulltext-search
      name: Full-text search + Documents API
      status: GA
      status_date: 2026-09
      layers: {L1: ●, L6: ◐}
      x: -1
      y: 0
      xy_reason: "하이브리드 검색 기반"
      maturity: 1
      evidence: [ {url: "https://docs.pinecone.io/nexus-release-notes/2026.md", kind: official, date: 2026-09-02} ]
    - id: pinecone-rbac
      name: Expanded RBAC / SAML-SCIM
      status: GA
      status_date: 2026-07
      layers: {GOV: ●}
      x: 0
      y: -1
      xy_reason: "조직·프로젝트 역할 관리"
      maturity: 1
      evidence: [ {url: "https://docs.pinecone.io/nexus-release-notes/2026.md", kind: official, date: 2026-07-13} ]
- vendor: elastic
  name: Elastic
  category: memory_retrieval
  products:
    - id: elastic-agent-builder
      name: Agent Builder
      status: GA
      status_date: 2026-01
      layers: {L1: ●, L6: ●, L7: ◐, GOV: ●}
      x: 0
      y: 1
      xy_reason: "인덱스·ES|QL을 도구로 런타임 검색, MCP·A2A"
      maturity: 2
      evidence: [ {url: "https://www.businesswire.com/news/home/20260122544127/en/Elastic-Announces-General-Availability-of-Agent-Builder-with-Expanded-Capabilities", kind: official, date: 2026-01-22}, {url: "https://www.helpnetsecurity.com/2026/01/23/elastic-agent-builder-2/", kind: secondary, date: 2026-01-23} ]
    - id: elastic-workflows
      name: Elastic Workflows
      status: preview
      status_date: 2026-01
      layers: {L4: ●, L7: ●}
      x: 1
      y: -1
      xy_reason: "사람이 정의한 실행 흐름"
      maturity: 2
      evidence: [ {url: "https://www.constellationr.com/insights/news/elastics-agent-builder-generally-available-elastic-workflows-tech-preview", kind: secondary, date: 2026-01-22} ]
    - id: elastic-hybrid-search-esql
      name: Hybrid search / ES|QL tools
      status: GA
      status_date: 2026-01
      layers: {L1: ●, L6: ●}
      x: -1
      y: 1
      xy_reason: "질의별 하이브리드 검색·집계"
      maturity: 1
      evidence: [ {url: "https://www.elastic.co/search-labs/blog/context-engineering-for-agents", kind: official, date: 2025} ]
    - id: elastic-trace-feedback
      name: Agent trace feedback (OTel)
      status: GA
      status_date: 2026-01
      layers: {L5: ◐, OBS: ●}
      x: 0
      y: 2
      xy_reason: "에이전트 트레이스를 새 컨텍스트 소스로 재투입"
      maturity: 5
      evidence: [ {url: "https://www.elastic.co/search-labs/blog/context-engineering-for-agents", kind: official, date: 2025} ]
- vendor: writer
  name: Writer
  category: enterprise_app
  products:
    - id: writer-knowledge-graph
      name: Knowledge Graph
      status: GA
      status_date: null  # 출시 시점 미확인
      layers: {L1: ●, L3: ●}
      x: -1
      y: -1
      xy_reason: "업로드 문서·웹페이지를 그래프 RAG로 근거화"
      maturity: 1
      evidence: [ {url: "https://atlan.com/know/ai-agent/context-layer/writer-knowledge-graph-vs-enterprise-context-layer/", kind: secondary, date: 2026} ]
    - id: writer-enterprise-brain
      name: Enterprise Brain
      status: preview
      status_date: 2026-09
      layers: {L2: ◐, L3: ●, L4: ●, GOV: ●}
      x: 1
      y: -1
      xy_reason: "브랜드 규칙·결정 로직을 통제된 레이어로 큐레이션"
      maturity: 4
      evidence: [ {url: "https://www.cmswire.com/customer-experience/writer-launches-enterprise-brain-to-unify-ai-agent-context/", kind: secondary, date: 2026-09-09} ]
    - id: writer-agent-memory
      name: Agent Memory
      status: GA
      status_date: 2026-09
      layers: {L5: ●}
      x: 1
      y: 2
      xy_reason: "팀 결정·선호를 세션 넘어 자동 유지"
      maturity: 5
      evidence: [ {url: "https://www.cmswire.com/customer-experience/writer-launches-enterprise-brain-to-unify-ai-agent-context/", kind: secondary, date: 2026-09-09} ]
    - id: writer-ai-hq
      name: AI HQ (Agent Builder, Writer Home, Skills)
      status: GA
      status_date: 2025-04
      layers: {L4: ●, L7: ●}
      x: 2
      y: -1
      xy_reason: "사전 제작 에이전트·스킬로 업무 실행"
      maturity: 3
      evidence: [ {url: "https://writer.com/blog/writer-ai-hq-press-release/", kind: official, date: 2025-04-10} ]
- vendor: contextual_ai
  name: Contextual AI
  category: agent_platform
  products:
    - id: contextual-agent-composer
      name: Agent Composer
      status: preview
      status_date: 2026-01
      layers: {L4: ●, L6: ●, L7: ●}
      x: 1
      y: 0
      xy_reason: "사람이 워크플로우 설계, 실행 중 에이전틱 검색으로 컨텍스트 관리"
      maturity: 4
      evidence: [ {url: "https://docs.contextual.ai/release-notes/2026.md", kind: official, date: 2026-01-27} ]
    - id: contextual-datastores
      name: Datastores (+Global Datastores)
      status: GA
      status_date: 2026-02
      layers: {L1: ●}
      x: -1
      y: -1
      xy_reason: "문서 사전 파싱·색인"
      maturity: 1
      evidence: [ {url: "https://docs.contextual.ai/release-notes/2026.md", kind: official, date: 2026-02-10} ]
    - id: contextual-grounded-generation
      name: Grounded generation / attributions
      status: GA
      status_date: 2026-02
      layers: {L7: ●}
      x: -1
      y: 0
      xy_reason: "답변에 근거 출처 첨부로 검증 가능"
      maturity: 4
      evidence: [ {url: "https://docs.contextual.ai/release-notes/2026.md", kind: official, date: 2026-02-02} ]
    - id: contextual-reranker-parser
      name: Reranker / Parser
      status: GA
      status_date: null  # 출시 시점 미확인
      layers: {L1: ●, L6: ●}
      x: -1
      y: 0
      xy_reason: "질의별 문서 선별"
      maturity: 1
      evidence: [ {url: "https://contextual.ai/platform", kind: official, date: 2026-11-11} ]
```
