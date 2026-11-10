# Context Engineering Tech Map

AI에 **회사 지식을 어떻게 넣어 주는가**(context injection / context engineering)를 다룬 최근 논문·기술 자료를 모으고,
연구 기술과 기업 솔루션(Palantir, Snowflake, Databricks, AI 회사 등)의 **기술 맵**을 만드는 저장소.

## 구성
| 경로 | 내용 |
|---|---|
| [`sources/`](sources/README.md) | 원문 목록과 라이선스. CC BY 4.0 논문 5편은 PDF 포함, 나머지 3편은 링크만 |
| [`notes/`](notes/) | 8개 자료를 끝까지 읽고 같은 형식으로 정리한 노트 (분류 체계 · 기술 카드 · 기업 언급 · 한계 · 맵 관점 메모) |
| [`docs/기술맵_설계안.md`](docs/기술맵_설계안.md) | 기술을 어떻게 나누고 어떤 그림으로 그릴지 정리한 설계안 |
| `map/` | (예정) 기술 카드 데이터 `nodes.yaml` 과 그림 |

## 읽을 순서
1. [A Survey of Context Engineering for LLMs](https://arxiv.org/abs/2507.13334) — 전체 지도 · [노트](notes/2507.13334.md)
2. [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — 실무 전략 · [노트](notes/anthropic_effective_context_engineering.md)
3. [Snowflake — The Agent Context Layer for Trustworthy Data Agents](https://www.snowflake.com/en/blog/agent-context-layer-trustworthy-data-agents/) — 기업 아키텍처 · [노트](notes/snowflake_agent_context_layer.md)
4. [ACE: Agentic Context Engineering](https://arxiv.org/abs/2510.04618) — 진화하는 컨텍스트 · [노트](notes/2510.04618.md)
5. [Context Kubernetes](https://arxiv.org/abs/2604.11623) — 지식 오케스트레이션·권한 · [노트](notes/2604.11623.md)
6. [Ontology-Constrained Neural Reasoning (FAOS)](https://arxiv.org/abs/2604.00555) — 온톨로지 결합 · [노트](notes/2604.00555.md)
7. [Beyond LLM Wrappers: Three-Engine Architecture for Financial AI](https://arxiv.org/abs/2610.39230) — 지식그래프+계산+검증 · [노트](notes/2610.39230.md)
8. [Memory for Autonomous LLM Agents](https://arxiv.org/abs/2603.07670) — 에이전트 기억 · [노트](notes/2603.07670.md)

## 라이선스
- 노트와 설계 문서: CC BY 4.0
- `sources/papers/*.pdf`: 각 원저자 저작물, CC BY 4.0 조건으로 재배포 (출처는 `sources/README.md`)
