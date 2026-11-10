# Effective context engineering for AI agents (https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, 2025-09-29, Anthropic Applied AI team — P. Rajasekaran, E. Dixon, C. Ryan, J. Hadfield 외)

## 한 줄 요약
컨텍스트는 유한한 "attention budget"이므로, 프롬프트 작성(prompt engineering)을 넘어 **매 추론 단계마다 가장 작은 고신호(high-signal) 토큰 집합을 큐레이션**하는 것이 에이전트 설계의 핵심이며, 이를 위해 시스템 프롬프트·도구·예시 설계, just-in-time 검색, 그리고 장기 작업용 compaction / structured note-taking / sub-agent 기법을 쓴다는 실무 가이드.

## 문서가 제시하는 분류 체계 / 아키텍처
- **개념 정의**
  - Context — LLM 샘플링 시 포함되는 토큰 전체
  - Prompt engineering — 지시문(특히 system prompt)을 잘 쓰는 방법
  - Context engineering — 추론 중 컨텍스트 창에 들어갈 최적 토큰 집합을 반복적으로 큐레이션·유지하는 전략 전체(시스템 지시, 도구, MCP, 외부 데이터, 메시지 이력 포함)
  - 에이전트 정의 — LLM이 루프 안에서 자율적으로 도구를 사용하는 것
- **왜 중요한가**
  - Context rot — 토큰이 늘수록 회상 정확도가 떨어지는 현상(needle-in-a-haystack 연구)
  - Attention budget — transformer의 n² 쌍관계, 짧은 시퀀스 위주 학습 분포, position encoding interpolation 때문에 길수록 정밀도가 점진적으로 하락(절벽이 아닌 경사)
- **효과적 컨텍스트의 구성요소 (anatomy)**
  - System prompt — "적절한 고도(right altitude)": 하드코딩된 if-else식 취약 로직과 모호한 상위 지침 사이의 균형; XML 태그/Markdown 섹션 구분; 최소 프롬프트로 시작해 실패 모드 기반으로 보강
  - Tools — 에이전트와 정보/행동 공간 사이의 계약; 토큰 효율적 반환, 기능 중복 최소, 명확한 파라미터; 비대한 도구 세트가 흔한 실패 원인
  - Examples (few-shot) — 엣지케이스 나열 대신 다양하고 대표적인(canonical) 예시 큐레이션
  - Message history — 위 전체에 "정보는 풍부하되 촘촘하게" 원칙 적용
- **런타임 컨텍스트 검색**
  - Pre-inference retrieval — 임베딩 기반으로 추론 전에 미리 가져오기
  - Just-in-time retrieval — 파일 경로·저장된 쿼리·링크 같은 가벼운 식별자만 들고 있다가 도구로 필요 시 로드
    - 메타데이터 신호 활용 — 폴더 구조·이름·타임스탬프가 용도·관련성 단서
    - Progressive disclosure — 탐색하며 층층이 이해를 쌓음
  - Hybrid — 일부는 선로드(예: CLAUDE.md), 나머지는 glob/grep으로 자율 탐색. 덜 동적인 법률·재무 영역에 적합할 수 있음
- **장기(long-horizon) 작업 기법**
  - Compaction — 창 한도 근접 시 대화를 요약해 새 창에서 재시작
    - Tool result clearing — 오래된 도구 결과 원문 제거(가장 가벼운 형태)
  - Structured note-taking (agentic memory) — 창 밖에 노트를 쓰고 나중에 다시 불러옴
  - Sub-agent architectures — 깨끗한 창의 하위 에이전트가 깊이 탐색 후 압축 요약만 반환
  - 선택 기준: 대화 흐름 유지 → compaction / 마일스톤형 반복 개발 → note-taking / 병렬 탐색형 연구 → multi-agent

## 기술 항목 카드
| 기술명 | 무엇을 하나(쉬운 말) | 파이프라인 단계 | 대표 방법·시스템 예시 | 근거 수치(있으면) |
|---|---|---|---|---|
| System prompt altitude 설계 | 너무 세세하지도 모호하지도 않게 핵심 행동 지침을 씀 | 조립·주입 | 섹션 구분(XML/Markdown), 최소 프롬프트→실패 기반 보강 | — |
| Token-efficient tool design | 도구가 필요한 것만 짧게 돌려주고 쓰임새가 겹치지 않게 | 실행·도구 | "Writing tools for AI agents" 가이드, MCP | — |
| Minimal viable tool set | 도구 수를 줄여 어떤 도구를 쓸지 헷갈리지 않게 | 선별·검색 / 실행·도구 | 사람이 고르기 어려운 도구 조합은 제거 | — |
| Canonical few-shot examples | 규칙 나열 대신 대표 예시 몇 개로 기대 행동을 보여줌 | 조립·주입 | 다양·대표 예시 큐레이션 | — |
| Embedding-based pre-retrieval | 추론 전에 유사 문서를 미리 찾아 넣음 | 선별·검색 | 일반 RAG | — |
| Just-in-time context loading | 참조(경로·쿼리·링크)만 갖고 있다가 필요할 때 도구로 불러옴 | 선별·검색 / 실행·도구 | Claude Code의 targeted query, head/tail로 대용량 분석 | — |
| Metadata-as-signal | 파일명·폴더·시간 정보로 무엇이 중요한지 추론 | 선별·검색 | 디렉터리 계층, 명명 규칙, 타임스탬프 | — |
| Progressive disclosure (agentic exploration) | 조금씩 탐색하며 필요한 것만 작업기억에 유지 | 선별·검색 | 파일 크기·이름으로 복잡도/용도 추정 | — |
| Hybrid upfront + exploration | 핵심 문서는 미리 넣고 나머지는 탐색 | 조립·주입 / 선별·검색 | CLAUDE.md 선로드 + glob/grep | — |
| Compaction | 길어진 대화를 요약해 새 창으로 이어감 | 가공·압축 / 기억·갱신 | Claude Code: 이력 요약 + 최근 접근 파일 5개 유지; recall 우선→precision 개선 순서로 프롬프트 튜닝 | — |
| Tool result clearing | 이미 쓴 도구 결과 원문을 지움 | 가공·압축 | Claude Developer Platform 기능 | — |
| Structured note-taking / agentic memory | 진행상황을 외부 파일에 적어두고 리셋 후 다시 읽음 | 기억·갱신 | NOTES.md, to-do list, Claude의 Pokémon 플레이, memory tool(파일 기반, Sonnet 4.5와 함께 public beta) | 수천 게임 스텝에 걸친 집계 유지 사례 |
| Sub-agent architecture | 하위 에이전트가 깊게 파고 요약만 상위에 보고 | 실행·도구 / 가공·압축 | 멀티에이전트 리서치 시스템 | 하위 탐색 수만 토큰 → 반환 요약 약 1,000–2,000 토큰; 단일 에이전트 대비 "상당한 개선"(수치 미제시) |

## 실험·결과 요약
- 정량 실험은 없음. 근거는 관찰·사례 위주.
  - Context rot는 모든 모델에 나타나되 저하 정도는 모델별 차이(needle-in-a-haystack 계열 연구 인용).
  - Claude playing Pokémon: 메모리 구조를 지시하지 않아도 지도·업적·전투 전략 노트를 스스로 유지, 컨텍스트 리셋 후 노트를 읽고 수 시간짜리 시퀀스를 이어감.
  - 서브에이전트: 하위 에이전트가 많은 토큰을 쓰더라도 1–2k 토큰 요약만 반환, 복잡한 연구 과제에서 단일 에이전트 대비 큰 개선(별도 글 "How we built our multi-agent research system" 참조).
- 핵심 메시지: 모델이 똑똑해질수록 처방적 엔지니어링 필요가 줄고 자율성이 커지지만, 컨텍스트를 유한 자원으로 다루는 원칙은 유지. "가장 단순하게 작동하는 것부터" 권고.

## 기업·제품 언급
- **Anthropic / Claude** — 저자 회사.
- **Claude Code** — just-in-time 검색(targeted query, Bash head/tail), hybrid 전략(CLAUDE.md 선로드 + glob/grep), compaction(이력 요약 + 최근 파일 5개), to-do list 사례.
- **Claude Developer Platform** — tool result clearing 기능, memory tool(public beta, 파일 기반 외부 기억), memory & context management cookbook.
- **Model Context Protocol (MCP)** — 컨텍스트 상태 구성요소로 언급.
- **Claude Sonnet 4.5** — 출시와 함께 memory tool 공개.
- 관련 글: "Building effective AI agents", "Writing tools for AI agents – with AI agents", "How we built our multi-agent research system", "Code execution with MCP"(2025-11-04, related article).
- (Palantir/Snowflake/Databricks 언급 없음)

## 한계·미해결 과제
- Just-in-time 탐색은 사전 계산 검색보다 느리고, 도구·휴리스틱 설계가 부실하면 도구 오용·막다른 길 추적·핵심 정보 누락으로 오히려 컨텍스트를 낭비.
- Compaction은 너무 공격적이면 나중에야 중요성이 드러나는 미묘한 정보를 잃음 — 무엇을 남길지의 선택이 본질적 난제.
- 더 큰 컨텍스트 창이 나와도 context pollution·관련성 문제는 당분간 지속될 것으로 봄.
- 자율성의 적정 수준(선로드 vs 탐색)은 작업마다 다르며 일반 기준 없음.
- 정량 벤치마크·평가 방법은 제시하지 않음.

## 기술 맵 관점 메모
- **시간축(언제 컨텍스트를 넣나)**: pre-inference(선로드/RAG) ↔ just-in-time(도구로 런타임 로드) ↔ hybrid — 맵의 "주입 시점" 축으로 쓰기 좋음.
- **컨텍스트 구성요소 축**: system prompt / tools / examples / message history / external data / memory — 무엇을 엔지니어링하는가의 "대상" 분류.
- **수명(호라이즌) 축**: 단일 턴 → 멀티턴 → long-horizon(compaction·note-taking·sub-agent). 장기 작업 기법은 "가공·압축"과 "기억·갱신" 단계에 매핑.
- **에이전트 자율 vs 사람 큐레이션 스펙트럼**: 모델이 강해질수록 사람이 미리 큐레이션하는 비중이 줄어든다는 방향성 — 엔터프라이즈 semantic layer(사전 큐레이션 중심)와 대비되는 위치.
- **범용·모델측 관점의 기준 문서**: 엔터프라이즈 문서(Snowflake 등)가 "무엇을 넣을지(의미·거버넌스)"를 다룬다면, 이 글은 "어떻게 창을 운영할지(attention budget 관리)"를 다룸 — 맵에서 두 층(데이터 의미층 vs 런타임 창 관리층)을 분리하는 근거.
