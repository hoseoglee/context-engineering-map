#!/usr/bin/env python3
"""research/vendors/*.md 의 yaml 데이터 블록을 모아 맵 데이터와 그림을 만든다.

산출물:
  map/products.yaml        — 전체 회사·제품 통합 데이터
  map/커버리지_히트맵.md    — 회사 × 층 표 (GitHub 에서 바로 보임)
  map/index.html           — 스택 맵 / 2축 지도 / 히트맵 / 성숙도 인터랙티브 페이지
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ADJ = yaml.safe_load((ROOT / "tools" / "adjustments.yaml").read_text()) or {}
LAYERS = ["L1", "L2", "L3", "L4", "L5", "L6", "L7", "GOV", "OBS"]
LAYER_NAMES = {
    "L1": "연결·원천", "L2": "의미(지표)", "L3": "관계·정체성", "L4": "절차·역할",
    "L5": "기억·이력", "L6": "런타임 창 관리", "L7": "실행·검증",
    "GOV": "거버넌스·권한", "OBS": "관측·평가",
}
CATEGORY_NAMES = {
    "data_platform": "데이터 플랫폼", "hyperscaler": "하이퍼스케일러", "ai_lab": "AI 연구소",
    "agent_platform": "에이전트 플랫폼", "semantic_catalog": "시맨틱·카탈로그",
    "knowledge_graph": "지식그래프", "memory_retrieval": "기억·검색", "enterprise_app": "기업 앱",
    "ontology_platform": "온톨로지 플랫폼",
}


def level(v) -> int:
    if v is None:
        return 0
    s = str(v).strip().lower()
    if s in ("●", "full", "2", "native", "yes", "true"):
        return 2
    if s in ("◐", "partial", "1", "preview"):
        return 1
    return 0


def yaml_blocks(text: str):
    for m in re.finditer(r"```ya?ml\s*\n(.*?)```", text, re.S):
        body = m.group(1)
        if "vendor" not in body:
            continue
        try:
            yield yaml.safe_load(body)
        except yaml.YAMLError as e:
            print(f"  ! yaml 파싱 실패: {e}", file=sys.stderr)


def load_vendors() -> list[dict]:
    vendors: dict[str, dict] = {}
    for md in sorted((ROOT / "research" / "vendors").glob("*.md")):
        for data in yaml_blocks(md.read_text()):
            items = data if isinstance(data, list) else data.get("vendors", [data]) if isinstance(data, dict) else []
            for v in items:
                if not isinstance(v, dict) or "vendor" not in v:
                    continue
                v["source_file"] = f"research/vendors/{md.name}"
                vendors[str(v["vendor"])] = v
    out = []
    for vid, v in vendors.items():
        prods = []
        for p in v.get("products") or []:
            lay = {k: level((p.get("layers") or {}).get(k)) for k in LAYERS}
            prods.append({
                "id": p.get("id"), "name": p.get("name"), "status": p.get("status"),
                "status_date": str(p.get("status_date") or ""),
                "layers": lay,
                "x": p.get("x"), "y": p.get("y"), "xy_reason": p.get("xy_reason", ""),
                "maturity": p.get("maturity"),
                "evidence": [e.get("url") if isinstance(e, dict) else e for e in (p.get("evidence") or [])],
                "evidence_kind": sorted({e.get("kind") for e in (p.get("evidence") or []) if isinstance(e, dict) and e.get("kind")}),
            })
        cov = {k: max([p["layers"][k] for p in prods] or [0]) for k in LAYERS}
        depth = {k: sum(1 for p in prods if p["layers"][k] == 2) for k in LAYERS}
        notes = []
        for k, o in (ADJ.get("coverage_overrides", {}).get(vid) or {}).items():
            if o["value"] > cov[k]:
                cov[k] = o["value"]
                notes.append(f"{k}: {o['reason']}")
        xs = [p["x"] for p in prods if isinstance(p["x"], (int, float))]
        ys = [p["y"] for p in prods if isinstance(p["y"], (int, float))]
        mats = [p["maturity"] for p in prods if isinstance(p["maturity"], (int, float))]
        claimed = max(mats) if mats else None
        mat = claimed
        for cap in ADJ.get("maturity_caps", []):
            if mat is not None and mat > cap["max"] and not all(cov[k] >= n for k, n in cap["unless"].items()):
                mat = cap["max"]
                notes.append(f"성숙도 {claimed}→{mat}: {cap['reason']}")
        out.append({
            "vendor": vid, "name": (ADJ.get("short_names") or {}).get(vid, v.get("name", vid)), "full_name": v.get("name", vid), "category": v.get("category", "other"),
            "source_file": v["source_file"], "products": prods, "coverage": cov, "depth": depth,
            "x": round(sum(xs) / len(xs), 2) if xs else None,
            "y": round(sum(ys) / len(ys), 2) if ys else None,
            "maturity": mat, "maturity_claimed": claimed, "adjustments": notes,
        })
    return out


def heatmap_md(vendors: list[dict]) -> str:
    def cell(v, k):
        c = v["coverage"][k]
        if c == 2:
            return f"●{v['depth'][k]}"
        return "◐" if c == 1 else ""
    lines = [
        "# 회사 × 층 커버리지 히트맵",
        "",
        "> `tools/build_map.py` 가 `research/vendors/*.md` 에서 자동 생성. 직접 고치지 말 것.",
        "> ●N = 그 층을 핵심 기능으로 가진 제품이 N개 / ◐ 부분·프리뷰·파트너 / 빈칸 근거 없음.",
        "> 성숙도는 누적 사다리 기준으로 상한을 적용한 값 (`tools/adjustments.yaml`).",
        "",
        "| 회사 | 분류 | " + " | ".join(f"{k} {LAYER_NAMES[k]}" for k in LAYERS) + " | 성숙도 | 제품 수 |",
        "|---|---|" + "---|" * len(LAYERS) + "---|---|",
    ]
    order = sorted(vendors, key=lambda v: (v["category"], -sum(v["coverage"].values())))
    for v in order:
        cells = " | ".join(cell(v, k) for k in LAYERS)
        lines.append(f"| [{v['name']}](../{v['source_file']}) | {CATEGORY_NAMES.get(v['category'], v['category'])} | {cells} | {v['maturity'] if v['maturity'] is not None else ''} | {len(v['products'])} |")
    lines += ["", "## 층별 강자 (● 보유 회사 수)", ""]
    for k in LAYERS:
        names = [v["name"] for v in vendors if v["coverage"][k] == 2]
        lines.append(f"- **{k} {LAYER_NAMES[k]}** ({len(names)}): {', '.join(names)}")
    return "\n".join(lines) + "\n"


def main() -> None:
    vendors = load_vendors()
    if not vendors:
        sys.exit("vendor 데이터 없음")
    mapdir = ROOT / "map"
    mapdir.mkdir(exist_ok=True)
    (mapdir / "products.yaml").write_text(yaml.safe_dump(vendors, allow_unicode=True, sort_keys=False))
    (mapdir / "커버리지_히트맵.md").write_text(heatmap_md(vendors))
    payload = {"layers": LAYERS, "layerNames": LAYER_NAMES, "categoryNames": CATEGORY_NAMES, "vendors": vendors}
    tpl = (ROOT / "tools" / "map_template.html").read_text()
    (mapdir / "index.html").write_text(tpl.replace("/*__DATA__*/null", json.dumps(payload, ensure_ascii=False)))
    n = sum(len(v["products"]) for v in vendors)
    print(f"회사 {len(vendors)}개, 제품 {n}개 → map/products.yaml, map/커버리지_히트맵.md, map/index.html")


if __name__ == "__main__":
    main()
