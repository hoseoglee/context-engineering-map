#!/usr/bin/env python3
"""Google Trends 로 2006년 이후 관련 기술 관심도를 받는다.

Google Trends 는 한 요청에 검색어 5개까지, 값은 그 요청 안에서 0~100 정수로 준다.
검색량이 수십 배 다른 용어를 한 요청에 넣으면 작은 쪽이 0·1 로 뭉개지므로,
**차트(패널) 하나 = 비슷한 규모의 검색어를 담은 요청 하나**로 받는다.
5개를 넘는 패널만 공통 기준어로 두 요청을 이어 붙인다.

  python3 tools/fetch_trends.py          # → data/trends/*.csv, map/trends.json
의존성: pytrends (비공식 클라이언트)
"""
from __future__ import annotations

import json
import time
from datetime import date
from pathlib import Path

from pytrends.request import TrendReq

ROOT = Path(__file__).resolve().parent.parent
END = date.today().isoformat()
# 집계 이상 구간(data/trends/README.md). 정상 구간만으로 정규화해야 해상도가 산다.
ANOM = ("2025-08", "2026-09")
CLEAN_END = "2025-07-31"
OVERLAP = ("2022-01", "2025-07")  # 두 요청을 잇는 배율 계산 구간

KO = {
    "semantic web": "시맨틱 웹", "enterprise search": "전사 검색", "master data management": "마스터 데이터 관리",
    "data warehouse": "데이터 웨어하우스", "knowledge graph": "지식그래프", "graph database": "그래프 DB",
    "data lake": "데이터 레이크", "data catalog": "데이터 카탈로그", "data fabric": "데이터 패브릭",
    "data mesh": "데이터 메시", "semantic layer": "시맨틱 레이어", "large language model": "대형 언어 모델",
    "prompt engineering": "프롬프트 엔지니어링", "vector database": "벡터 DB",
    "retrieval augmented generation": "RAG", "GraphRAG": "GraphRAG", "AI agent": "AI 에이전트",
    "model context protocol": "MCP", "context engineering": "컨텍스트 엔지니어링",
}
# 패널 id → 요청 목록(각 ≤5개). 요청이 둘 이상이면 첫 검색어(기준어)로 이어 붙인다.
PANELS = {
    "story": {"start": "2019-01-01", "requests": [
        ["retrieval augmented generation", "vector database", "GraphRAG", "model context protocol", "context engineering"]]},
    "e1": {"start": "2006-01-01", "requests": [
        ["data warehouse", "semantic web", "enterprise search", "master data management"]]},
    "e2": {"start": "2006-01-01", "requests": [
        ["knowledge graph", "graph database", "data lake", "data catalog", "data fabric"],
        ["knowledge graph", "data mesh", "semantic layer"]]},
    "e3": {"start": "2006-01-01", "requests": [
        ["AI agent", "large language model", "prompt engineering", "vector database", "retrieval augmented generation"]]},
}
GEOS = {"": "전 세계", "KR": "한국"}


def get(py: TrendReq, kw: list[str], start: str, geo: str, end: str = END):
    for attempt in range(4):
        try:
            py.build_payload(kw, timeframe=f"{start} {end}", geo=geo)
            return py.interest_over_time()
        except Exception as e:  # 429 등 — 기다렸다 재시도
            wait = 30 * (attempt + 1)
            print(f"  ! {geo or 'world'} {kw[0]}… 실패({e}); {wait}s 대기")
            time.sleep(wait)
    raise SystemExit(f"Google Trends 요청 실패: {kw}")


def fetch_geo(geo: str) -> dict:
    py = TrendReq(hl="en-US", tz=0, timeout=(10, 60))
    outdir = ROOT / "data" / "trends"
    outdir.mkdir(parents=True, exist_ok=True)
    panels = {}
    for pid, spec in PANELS.items():
        clean: dict[str, list[float]] = {}
        full: dict[str, list[float]] = {}
        dates_c: list[str] = []
        dates_f: list[str] = []
        ref_c = ref_f = None
        for j, kw in enumerate(spec["requests"]):
            for tag, end in (("clean", CLEAN_END), ("full", END)):
                df = get(py, kw, spec["start"], geo, end)
                df.to_csv(outdir / f"raw_{geo or 'world'}_{pid}_{j}_{tag}.csv")
                ds = [d.strftime("%Y-%m") for d in df.index]
                a_sum = float(df[kw[0]].sum()) or 1.0
                if tag == "clean":
                    ref_c = ref_c or a_sum; k = ref_c / a_sum; dates_c = ds; tgt = clean
                else:
                    ref_f = ref_f or a_sum; k = ref_f / a_sum; dates_f = ds; tgt = full
                for t in kw:
                    tgt.setdefault(t, [round(float(x) * k, 3) for x in df[t]])
                print(f"  {geo or 'world'} {pid}[{j}] {tag} {kw} (배율 {k:.3f})")
                time.sleep(8)
        # full 을 clean 척도로: 겹치는 정상 구간의 전체 합 비율
        idx_c = [i for i, d in enumerate(dates_c) if OVERLAP[0] <= d <= OVERLAP[1]]
        idx_f = [dates_f.index(dates_c[i]) for i in idx_c]
        sc = sum(clean[t][i] for t in clean for i in idx_c) / (sum(full[t][i] for t in full for i in idx_f) or 1)
        series, raw = {}, {}
        for t in clean:
            raw[t] = [round(x * sc, 3) for x in full[t]]
            series[t] = [
                clean[t][dates_c.index(d)] if d in dates_c else (None if ANOM[0] <= d <= ANOM[1] else raw[t][i])
                for i, d in enumerate(dates_f)
            ]
        print(f"  {pid}: 최근 구간 배율 {sc:.3f}")
        panels[pid] = {"dates": dates_f, "series": series, "raw": raw}
    return panels


def main() -> None:
    out = {"fetched": date.today().isoformat(), "end": END, "ko": KO,
           "source": "Google Trends (pytrends), 월별, 웹 검색", "geos": {}}
    for geo, name in GEOS.items():
        print(f"[{name}]")
        out["geos"][geo or "world"] = {"name": name, "panels": fetch_geo(geo)}
    (ROOT / "map" / "trends.json").write_text(json.dumps(out, ensure_ascii=False))
    print("→ map/trends.json")


if __name__ == "__main__":
    main()
