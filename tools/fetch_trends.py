#!/usr/bin/env python3
"""Google Trends 로 2006년 이후 관련 기술 관심도를 받고, 집계 이상 구간을 보정한다.

Google Trends 는 한 요청에 검색어 5개까지, 값은 그 요청 안에서 0~100 정수로 준다.
검색량이 수십 배 다른 용어를 한 요청에 넣으면 작은 쪽이 0·1 로 뭉개지므로,
**차트(패널) 하나 = 비슷한 규모의 검색어를 담은 요청 하나**로 받는다.
5개를 넘는 패널만 공통 기준어로 두 요청을 이어 붙인다.

집계 이상 구간(data/trends/README.md)은 위키백과 조회수로 보정한다:
  - 위키백과(영문) 조회수에는 이 이상이 없다(대조 문서로 확인).
  - 이상 구간 직전 3개월과 직후 1개월에서 "Trends 값 / 위키 조회수" 비율을 구하고,
    그 사이를 로그 선형으로 이어 위키 조회수에 곱한다(양 끝은 Trends 실측에 맞춰짐).
  - 위키 문서가 없거나 쓸 수 없는 용어는 같은 차트에서 보정된 용어들의
    "부풀림 배율(원본/보정)" 중앙값으로 원본을 나눈다.

  python3 tools/fetch_trends.py             # 받기 + 보정 → data/trends/*.csv, map/trends.json
  python3 tools/fetch_trends.py --no-fetch  # 받아 둔 CSV 로 보정만 다시
의존성: pytrends (비공식 클라이언트), pandas
"""
from __future__ import annotations

import json
import math
import statistics
import sys
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "trends"
END = date.today().isoformat()

# 지역별 집계 이상 구간 — 대조 검색어로 확인한 시작·끝(README 참조). 지역마다 시작이 다르다.
GEOS = {
    "world": {"geo": "", "name": "전 세계", "anom": ("2025-06", "2026-09"), "clean_end": "2025-05-31"},
    "KR": {"geo": "KR", "name": "한국", "anom": ("2025-11", "2026-09"), "clean_end": "2025-10-31"},
}
PRE_N = 3  # 이상 구간 직전 몇 개월로 비율을 잡나

KO = {
    "semantic web": "시맨틱 웹", "enterprise search": "전사 검색", "master data management": "마스터 데이터 관리",
    "data warehouse": "데이터 웨어하우스", "knowledge graph": "지식그래프", "graph database": "그래프 DB",
    "data lake": "데이터 레이크", "data catalog": "데이터 카탈로그", "data fabric": "데이터 패브릭",
    "data mesh": "데이터 메시", "semantic layer": "시맨틱 레이어", "large language model": "대형 언어 모델",
    "prompt engineering": "프롬프트 엔지니어링", "vector database": "벡터 DB",
    "retrieval augmented generation": "RAG", "GraphRAG": "GraphRAG", "AI agent": "AI 에이전트",
    "model context protocol": "MCP", "context engineering": "컨텍스트 엔지니어링",
}
# 보정용 영문 위키백과 문서. None = 문서가 없거나(리다이렉트·최근 신설로 끊김) 못 씀 → 배율 중앙값으로 보정
WIKI = {
    "retrieval augmented generation": "Retrieval-augmented generation",
    "vector database": "Vector database",
    "model context protocol": "Model Context Protocol",
    "GraphRAG": None, "context engineering": None,
    "data warehouse": "Data warehouse", "semantic web": "Semantic Web",
    "enterprise search": "Enterprise search", "master data management": "Master data management",
    "knowledge graph": "Knowledge graph", "graph database": "Graph database", "data lake": "Data lake",
    "data catalog": None, "data fabric": None,  # 리다이렉트라 조회수가 수십 건
    "data mesh": "Data mesh", "semantic layer": "Semantic layer",
    "AI agent": None,  # 'AI agent' 문서는 2026-02 본문 신설로 조회수가 끊겨 있다
    "large language model": "Large language model", "prompt engineering": "Prompt engineering",
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


# ---------- 받기 ----------
def gt_get(py, kw: list[str], start: str, geo: str, end: str):
    for attempt in range(4):
        try:
            py.build_payload(kw, timeframe=f"{start} {end}", geo=geo)
            return py.interest_over_time()
        except Exception as e:  # 429 등 — 기다렸다 재시도
            wait = 30 * (attempt + 1)
            print(f"  ! {geo or 'world'} {kw[0]}… 실패({e}); {wait}s 대기")
            time.sleep(wait)
    raise SystemExit(f"Google Trends 요청 실패: {kw}")


def fetch_gt() -> None:
    from pytrends.request import TrendReq
    py = TrendReq(hl="en-US", tz=0, timeout=(10, 60))
    for gid, g in GEOS.items():
        for pid, spec in PANELS.items():
            for j, kw in enumerate(spec["requests"]):
                for tag, end in (("clean", g["clean_end"]), ("full", END)):
                    df = gt_get(py, kw, spec["start"], g["geo"], end)
                    df.to_csv(OUT / f"raw_{gid}_{pid}_{j}_{tag}.csv")
                    print(f"  {gid} {pid}[{j}] {tag} {kw}")
                    time.sleep(8)


def fetch_wiki() -> None:
    ua = {"User-Agent": "context-engineering-map/1.0 (research script)"}
    rows = {}
    for term, art in WIKI.items():
        if not art:
            continue
        a = urllib.parse.quote(art.replace(" ", "_"), safe="")
        u = ("https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/"
             f"all-access/user/{a}/monthly/2015070100/{END.replace('-', '')[:6]}0100")
        for k in range(5):
            try:
                d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=ua), timeout=30))
                rows[term] = {i["timestamp"][:4] + "-" + i["timestamp"][4:6]: i["views"] for i in d["items"]}
                break
            except Exception as e:
                print(f"  ! wiki {art}: {e}")
                time.sleep(5 * (k + 1))
        time.sleep(1.5)
    pd.DataFrame(rows).sort_index().to_csv(OUT / "wiki_en_pageviews.csv")
    print(f"  위키 조회수 {len(rows)}개 문서 → data/trends/wiki_en_pageviews.csv")


# ---------- 합치기·보정 ----------
def read_req(gid: str, pid: str, j: int, tag: str) -> pd.DataFrame:
    df = pd.read_csv(OUT / f"raw_{gid}_{pid}_{j}_{tag}.csv", index_col=0, parse_dates=True)
    df.index = df.index.strftime("%Y-%m")
    return df.drop(columns=["isPartial"], errors="ignore").astype(float)


def stitch(gid: str, pid: str, tag: str) -> pd.DataFrame:
    """요청 여러 개를 첫 검색어(기준어) 합계 비율로 한 척도에 잇는다."""
    out, ref = None, None
    for j, kw in enumerate(PANELS[pid]["requests"]):
        df = read_req(gid, pid, j, tag)
        s = df[kw[0]].sum() or 1.0
        ref = ref or s
        df = df * (ref / s)
        out = df if out is None else out.join(df[[c for c in df if c not in out]])
    return out


def correct(gid: str, pid: str, wiki: pd.DataFrame) -> dict:
    g = GEOS[gid]
    a0, a1 = g["anom"]
    clean, full = stitch(gid, pid, "clean"), stitch(gid, pid, "full")
    # full 을 clean 척도로: 두 요청이 겹치는 정상 구간(최근 3년여)의 전체 합 비율
    ov = [d for d in clean.index if d >= "2022-01"]
    sc = clean.loc[ov].values.sum() / (full.loc[ov].values.sum() or 1)
    raw = full * sc
    dates = list(full.index)
    anom = [d for d in dates if a0 <= d <= a1]
    pre = [d for d in dates if d < a0][-PRE_N:]
    post = [d for d in dates if d > a1][:2]  # 직후 1개월 + 집계 중인 이번 달(정수 반올림 잡음 줄이기)
    # 정상 구간 = clean 값(해상도 높음), 이상 이후 = raw(clean 척도로 맞춘 full)
    base = pd.DataFrame({t: [clean.at[d, t] if d in clean.index else raw.at[d, t] for d in dates] for t in full},
                        index=dates)
    fixed = base.copy()
    method = {}
    infl = {d: [] for d in anom}  # 월별 부풀림 배율(원본/보정) — 위키 보정된 용어에서
    has = lambda t, d: t in wiki and pd.notna(wiki[t].get(d)) and wiki[t].get(d, 0) > 100
    # 이상 이후 값은 이상 구간 최고점에 맞춰 정규화된 요청에서 오므로 정수 몇 단위밖에 안 된다.
    # 원 요청 값 평균이 3 미만이면 직후 비율을 믿지 않고 직전 비율을 그대로 유지한다.
    post_ok = lambda t: full.loc[post, t].mean() >= 3
    for t in full:
        # 직전 3개월 중 위키 문서가 온전히 한 달 이상 있던 달만 쓴다(신설 달은 하루치라 비율이 틀어짐)
        wd = list(wiki.index)
        p_ok = [d for d in pre if has(t, d) and d in wd and wd.index(d) > 0 and has(t, wd[wd.index(d) - 1])]
        if not p_ok or not all(has(t, d) for d in anom + post[:1]):
            continue
        r_pre = base.loc[p_ok, t].mean() / wiki.loc[p_ok, t].mean()
        # 위키 이번 달은 하루치뿐이라 직후 1개월 조회수를 쓰고, Trends 쪽은 2개월 평균(정수 잡음 완화)
        r_post = base.loc[post, t].mean() / wiki.at[post[0], t] if post_ok(t) else r_pre
        if r_pre <= 0 or r_post <= 0:  # 저해상도 0 값 — 비율을 못 잡음
            continue
        n = len(anom) + 1
        for k, d in enumerate(anom, start=1):
            r = math.exp(math.log(r_pre) + (math.log(r_post) - math.log(r_pre)) * k / n)
            fixed.at[d, t] = wiki.at[d, t] * r
            if fixed.at[d, t] > 0 and base.at[d, t] > 0:
                infl[d].append(base.at[d, t] / fixed.at[d, t])
        method[t] = "wiki"
    for t in full:
        if t in method:
            continue
        for d in anom:
            f = statistics.median(infl[d]) if infl[d] else None
            fixed.at[d, t] = base.at[d, t] / f if f else None
        # 중앙값 배율은 이 용어 고유의 부풀림과 다를 수 있어 구간 끝에서 실측과 어긋난다.
        # 그 어긋남을 구간에 걸쳐 0 → 끝 값으로 선형 분배해 이음매를 없앤다(직후 값이 믿을 만할 때만).
        end = fixed.at[anom[-1], t]
        if post_ok(t) and end and end > 0 and base.loc[post, t].mean() > 0:
            drift = math.log(base.loc[post, t].mean() / end)
            for k, d in enumerate(anom, start=1):
                if fixed.at[d, t]:
                    fixed.at[d, t] *= math.exp(drift * k / len(anom))
        method[t] = "median" if any(infl[d] for d in anom) else "none"
    r3 = lambda v: None if v is None or (isinstance(v, float) and math.isnan(v)) else round(float(v), 3)
    return {
        "dates": dates,
        "series": {t: [r3(v) for v in fixed[t]] for t in full},
        "raw": {t: [r3(v) for v in base[t]] for t in full},
        "method": method,
        "infl": {d: r3(statistics.median(v)) if v else None for d, v in infl.items()},
    }


def build() -> None:
    wiki = pd.read_csv(OUT / "wiki_en_pageviews.csv", index_col=0)
    wiki.index = wiki.index.astype(str)
    out = {"fetched": date.today().isoformat(), "end": END, "ko": KO,
           "source": "Google Trends (pytrends), 월별, 웹 검색 · 이상 구간 보정: 영문 위키백과 조회수(Wikimedia API)",
           "wiki": {t: a for t, a in WIKI.items() if a}, "geos": {}}
    for gid, g in GEOS.items():
        panels = {pid: correct(gid, pid, wiki) for pid in PANELS}
        out["geos"][gid] = {"name": g["name"], "anom": list(g["anom"]), "panels": panels}
        for pid, p in panels.items():
            fx = {d: v for d, v in p["infl"].items() if v}
            print(f"  {gid} {pid}: 보정 {p['method']}  부풀림 최대 {max(fx.values(), default=1):.1f}배")
    (ROOT / "map" / "trends.json").write_text(json.dumps(out, ensure_ascii=False))
    print("→ map/trends.json")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    if "--no-fetch" not in sys.argv:
        fetch_wiki()
        fetch_gt()
    build()
