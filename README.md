# Context Engineering Tech Map

AI에 **회사 지식을 어떻게 넣어 주는가**(context injection / context engineering)를 다룬 최근 논문·기술 자료를 모으고,
연구 기술과 기업 솔루션(Palantir, Snowflake, Databricks, AI 회사 등)의 **기술 맵**을 만드는 저장소.

## 🗺 맵 보기
**https://hoseoglee.github.io/context-engineering-map/map/** — 스택 맵 · 2축 지도 · 히트맵 · 성숙도 · 관심도 추이 (조사일 2026-11-11)

- **범위: 기업 규모 컨텍스트 플랫폼**(Gartner가 2026-08 "AI Context Platforms"로 처음 시장 개요를 낸 영역) — 회사 전체의 데이터·의미·지식·권한을 여러 AI와 사람에게 공급·통제하는 솔루션. 에이전트 하나 안의 SDK·대화 기억·창 압축은 제외, 기업용 AI 앱은 "소비 계층"으로 따로 표시. 판정: [`tools/scope.yaml`](tools/scope.yaml)
- **관심도 추이**: Google Trends 2006~ 월별 (전 세계·한국). ⚠️ 2025-08~2026-09는 Google Trends 집계 이상 구간이라 해석에서 제외 — 근거: [`data/trends/README.md`](data/trends/README.md)
- 정적 표 버전(회사 × 층 솔루션 이름): [`map/커버리지_히트맵.md`](map/커버리지_히트맵.md)

## 구성
| 경로 | 내용 |
|---|---|
| [`sources/`](sources/README.md) | 원문 목록과 라이선스. CC BY 4.0 논문 5편은 PDF 포함, 나머지 3편은 링크만 |
| [`notes/`](notes/) | 8개 자료를 끝까지 읽고 같은 형식으로 정리한 노트 (분류 체계 · 기술 카드 · 기업 언급 · 한계 · 맵 관점 메모) |
| [`docs/기술맵_설계안.md`](docs/기술맵_설계안.md) | 기술을 어떻게 나누고 어떤 그림으로 그릴지 정리한 설계안 |
| [`research/vendors/`](research/vendors/) | 회사별 솔루션 조사 (Palantir, Snowflake, Databricks, Microsoft, Google, AWS + 유사 기업 36곳: 데이터측·AI측·전사 플랫폼 추가분). 공통 기준: [`docs/포지셔닝_조사_가이드.md`](docs/포지셔닝_조사_가이드.md) |
| [`data/trends/`](data/trends/) | Google Trends 원본 CSV와 집계 이상 구간 검증 (`tools/fetch_trends.py` 로 재수집) |
| `map/` | 조사 데이터를 합친 `products.yaml`, 히트맵, 인터랙티브 맵 `index.html` (`python3 tools/build_map.py` 로 재생성) |
| `tools/adjustments.yaml` · `tools/scope.yaml` · `tools/trend_events.yaml` | 수동 보정(본문-데이터 불일치, 누적 성숙도 상한, 표시 이름) · 범위 판정 · 차트 사건(출처 필수) |

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
