# The Agent Context Layer for Trustworthy Data Agents (Snowflake Blog — Product and Technology, 2026-03-19, Josh Klahr · Rajhans Samdani)

## 한 줄 요약
"데이터와 대화하기(text→SQL)"는 기본값일 뿐이고, 기업 데이터 에이전트를 신뢰할 수 있게 만드는 핵심은 모델이 아니라 **의미(semantics)·정체성(identity)·절차(playbook)·출처(provenance)·결정 기억(memory)·정책(entitlements)을 묶은 "agent context layer"**이며, 이 레이어를 AI 에이전트(Cortex Code)로 생성·유지하는 방향으로 경제성이 바뀐다는 Snowflake의 관점 글.

## 문서가 제시하는 분류 체계 / 아키텍처
- **기업 현실의 4가지 문제** — 에이전트가 틀리는 이유
  - Siloed meaning — "고객"이 시스템마다 다른 의미
  - Missing why — 웨어하우스는 상태만 저장, 그 상태를 만든 결정·논의는 없음
  - Implicit rules — 회계연도, 자격 기준, 승인 정책, 금지 지표가 흩어지거나 암묵지
  - Conflicted truth — 재무와 CRM이 둘 다 "신뢰 원천"인데 서로 다름
- **최소 어휘(정의) 5개**
  - Analytic semantic model — 지표·차원·엔티티를 물리 데이터에 매핑한 분석 인터페이스
  - Relationship & identity layer ("ontology") — 도메인 간 개념·관계·규칙 + 동일인 식별·동의어·제약 (OWL/RDF, 큐레이션된 join graph, 개념-데이터 바인딩 중 어느 형태든 가능)
  - Business procedures — 라우팅·승인·예외·정책을 담은 버전관리 운영 플레이북
  - Evidence & provenance — 사용 소스·변환·계보·경쟁 소스 채택/기각 이유
  - Policy & entitlements — 사용자(또는 대리 에이전트)가 무엇을 조회·계산·공개할 수 있는지에 대한 기계 집행 규칙
- **실용 아키텍처: Agent Context Layer의 5개 층 (Figure 2)**
  - Analytic layer — 지표 정의(필터·조인·공식)를 한 곳에 두고 재사용; semantic views가 거버넌스된 인터페이스 역할 (예: NRR = 정의 버전 + 기본 필터 + 회계분기 시간 로직)
  - Relationship & identity layer (ontology) — 정규 엔티티(Customer 등), 타입 관계, CRM ID ↔ 지원 시스템 ID 매핑으로 도메인 간 조인 계획
  - Operational playbooks (directives) — 의도별 처리 절차: 권위 소스로 라우팅, 필수 명확화 단계, 필수 체크(예: 가격은 인증 테이블만, 특정 지표 사용 금지)
  - Provenance & explainability — 선택된 시맨틱 객체, 필터, 조인, freshness 타임스탬프, 충돌 시 선택 규칙 기록 (예: 지표 정의 v2.3→v2.4 변경, 백필 반영 설명)
  - Event & decision memory — 승인 기록·인시던트 타임라인·변경 이벤트·티켓을 엔티티에 연결해 "왜" 질문에 증거 제공
  - (정의상 Policy & entitlements는 횡단 요소로 제시됨)
- **"Agentology" vs 프롬프트 엔지니어링** — 지속·거버넌스 가능한 산출물의 5가지 이점
  - Change control(버전·리뷰), Auditability, Interoperability(BI와 에이전트가 같은 의미 기반), Governance(규칙을 강제 제약으로), Reusability
- **AI가 바꾸는 컨텍스트 구축 경제성 — 6단계 워크플로우**
  - ① 에이전트 + 큐레이션된 semantic layer(기존 대시보드·쿼리 이력 활용)로 시작 → ② 테이블 메타데이터·과거 쿼리·사용 패턴·문서·플레이북·기존 온톨로지·코드 파이프라인에서 컨텍스트 추가 → ③ 실사용 패턴 학습 → ④ 동의어·매핑·누락 관계 개선 제안 → ⑤ 사람 승인 루프 유지 → ⑥ 비용은 줄이고 커버리지는 확대

## 기술 항목 카드
| 기술명 | 무엇을 하나(쉬운 말) | 파이프라인 단계 | 대표 방법·시스템 예시 | 근거 수치(있으면) |
|---|---|---|---|---|
| Analytic semantic model / Semantic views | "매출", "NRR" 같은 말을 정확한 계산식·필터·기간으로 고정해 둠 | 가공·압축 / 거버넌스 | Snowflake semantic views, BI semantic layer | — |
| Relationship & identity layer (ontology) | 서로 다른 시스템의 같은 고객을 연결하고 테이블 간 조인 방법을 알려줌 | 선별·검색 / 가공 | OWL/RDF, curated join graph, concept bindings, MDM | plain-text data ontology(조인키·grain·cardinality 힌트) 추가 시 정확도 +20%, 도구 호출 약 −39%, 지연 약 −20% (내부 실험) |
| Synonym / alias handling & identity resolution | 같은 개념의 여러 이름·ID를 하나로 매핑 | 선별·검색 | CRM.AccountId ↔ Customer ↔ Support.OrgId | (위 실험에 포함) |
| Operational playbooks (directives) | 특정 질문 유형에 대해 정해진 처리 순서·체크를 강제 | 실행·도구 / 거버넌스 | 가격 문의 playbook: 맥락 확인 → 인증 객체로 라우팅 → 지역·통화 규칙 → 가격+유효일+출처 반환 | — |
| Authoritative-source routing | 여러 후보 중 "공식" 데이터로만 답하게 함 | 선별·검색 / 거버넌스 | certified tables / certified semantic object | — |
| Provenance & explainability | 답이 어떻게 계산됐고 지난 보고서와 왜 다른지 설명 | 평가 / 거버넌스 | 정의 버전, 필터, as-of 타임스탬프, 백필 이력 | — |
| Event & decision memory | 승인·인시던트·변경 이벤트를 엔티티에 연결해 "왜"에 답함 | 기억·갱신 | 승인 워크플로 기록, 근거 필드, deal desk 티켓 연결 | — |
| Policy & entitlements | 사용자/대리 에이전트가 볼 수 있는·계산할 수 있는·공개할 수 있는 범위를 강제 | 거버넌스·권한 | 기계 집행 규칙 | — |
| AI-assisted context generation & maintenance | 에이전트가 문서·쿼리 이력·메타데이터를 읽고 컨텍스트를 만들고 최신 유지 | 수집 / 기억·갱신 | Cortex Code, usage-pattern 학습, 개선 제안 + 사람 승인 | — |
| Versioned change control | 컨텍스트 산출물을 리뷰·버전 관리로 배포 | 거버넌스 | metric definition vX, playbook 버전 | — |
| Semantic interoperability standard | 플랫폼 간 시맨틱 레이어를 같은 형식으로 주고받음 | 거버넌스 / 조립·주입 | Open Semantic Interchange (OSI) | — |

## 실험·결과 요약
- 내부 실험 1건: 여러 semantic view를 함께 써야 답할 수 있는 질의 세트로 평가(최종 답 정확도, 총 지연, 도구 호출 수).
  - Best-practice 베이스라인에 **평문 "data ontology"**(조인 키, 테이블 grain, cardinality/fanout 힌트)만 추가 → 정확도 +20%, 평균 도구 호출 약 39% 감소, 종단 지연 약 20% 개선.
  - 질의 예: "내 담당 계정의 오픈 에스컬레이션과 계정별 위험 ARR" — CRM→Customer→Support→Contract/ARR를 Customer grain에서 조인하는 계획.
- 그 외는 시나리오 예시(NRR, 가격 문의, 이탈률 차이 설명, 할인 승인 사유)로 각 층의 역할을 보여줄 뿐 정량 결과는 없음. 실험 세부(데이터 규모, 모델, 질의 수)는 미공개.

## 기업·제품 언급
- **Semantic views (Snowflake)** — analytic layer의 거버넌스된 인터페이스. 지표·차원·필터 정의를 한 곳에 두고 에이전트·BI가 공유; 도메인 간 오케스트레이션의 기반으로 소개.
- **Cortex Code (Snowflake)** — 강력한 AI 에이전트로서 문서·지식그래프·온톨로지·채팅·기록 시스템을 읽어 agent context를 생성·갱신하는 역할로 제시.
- **Cortex Agents (Snowflake)** — 디자인 파트너 프로그램 대상, 데이터 에이전트를 구축하는 제품으로 언급.
- **Snowflake Intelligence** — 비즈니스 가드레일을 통합한 "unified intelligence layer"로 소개.
- **Open Semantic Interchange (OSI)** — 업계 표준화 노력, 시맨틱/컨텍스트 레이어의 플랫폼 간 상호운용 목적.
- (참고: 페이지 하단 내비게이션에 "Snowflake CoWork" 등 제품명이 있으나 본문 내용과 무관. **Horizon, Cortex Analyst, Cortex Search 등은 본문에서 언급되지 않음.**)
- 일반 카테고리 언급: BI semantic layer, MDM, data catalog, knowledge graph, OWL/RDF.
- (Palantir/Databricks 언급 없음)

## 한계·미해결 과제
- 근거 수치가 단일 내부 실험이며 설정·규모·모델이 비공개 — 재현 불가.
- 시맨틱 레이어는 구축 비용이 크고 빠르게 낡으며(drift) 비즈니스 속도를 못 따라감 — AI 자동 생성으로 완화된다고 주장하나 검증된 결과는 미제시.
- 충돌하는 진실(재무 vs CRM)의 조정 규칙을 어떻게 정의·유지할지는 원칙 수준.
- 사람 승인 루프 의존 — 완전 자동화는 아님.
- 플랫폼 간 상호운용 표준(OSI 등)은 아직 형성 중.
- 저자가 벤더라 자사 제품 중심 서술(마케팅 성격).

## 기술 맵 관점 메모
- **"의미층(semantic) ↔ 관계층(ontology)" 2단 구조**: 단일 도메인 지표 신뢰 = semantic model, 도메인 간 연결 = identity/relationship layer. Palantir Ontology(관계+액션 중심)와 Snowflake semantic views(지표 중심)를 같은 축 위 다른 위치로 배치 가능.
- **컨텍스트 레이어 5요소(semantics·identity·procedure·provenance·memory)+policy**를 엔터프라이즈 솔루션 비교표의 열로 그대로 쓰기 좋음 — Databricks(Unity Catalog·metric views), Palantir(Ontology·Actions), Snowflake(semantic views·Cortex)를 칸별 매핑.
- **산출물 지속성 축**: 프롬프트(휘발·불투명) ↔ 버전관리된 거버넌스 산출물(agentology) — Anthropic 글의 런타임 창 관리와 상보적인 "정적 큐레이션 자산" 층.
- **컨텍스트 생산 방식 축**: 사람 수작업 큐레이션 → AI 보조 생성·유지(사용 로그 학습 + 사람 승인) — 맵에 "context ops / 유지보수" 단계를 별도 노드로 둘 근거.
- **"Why" 질문 = decision memory**: 상태(state) 데이터와 결정 이력(event/decision) 데이터를 구분하는 축 — 금융 논문의 temporal graph·audit trail과 연결.
- **표준화 축**: OSI 같은 상호운용 표준 → MCP(도구 층 표준)와 나란히 "의미 층 표준"으로 배치.
