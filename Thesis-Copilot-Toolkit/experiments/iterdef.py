"""Iteration definition generator utilities.

Provides a small generator to create IterDef-like dictionaries for scheduling
experiments. Designed to be conservative: it respects a deprecation manifest
if present and filters excluded methods (e.g. deprecated TV tokens).

This module intentionally produces plain dicts (serializable) so schedules
can be reviewed/edited prior to instantiation by runner scripts.
"""
from __future__ import annotations

import json
import datetime
from pathlib import Path
from typing import Any, Dict, List, Sequence


ROOT = Path(__file__).resolve().parents[1]


def _read_manifest_exclusions() -> set:
    try:
        p = ROOT / "docs" / "deprecation_manifest.json"
        if p.exists():
            j = json.loads(p.read_text(encoding="utf-8"))
            tv_exc = j.get("tv_family_exclusions", [])
            return set(tv_exc) | {"mean", "nearest"}
    except Exception:
        pass
    return {"directed_tv", "heat_diffusion_temporal", "wavelet_temporal", "mean", "nearest"}


def generate_iterdefs(
    n: int = 50,
    seed_count: int = 6,
    datasets_pool: Sequence[str] | None = None,
    graphs_pool: Sequence[Any] | None = None,
    baselines: Sequence[str] | None = None,
    gsp_methods: Sequence[str] | None = None,
    tv_methods: Sequence[str] | None = None,
    exclusions: Sequence[str] | None = None,
) -> List[Dict[str, Any]]:
    """Generate a list of iteration-definition dictionaries.

    Each dict follows the same keys expected by the project's `IterDef`
    dataclass: `key`, `tag`, `description`, `fase`, `objective`, `datasets`,
    `mode`, `missing_list`, `seeds`, `graph_specs`, `lambdas`, `snr_levels`,
    `methods`.
    """
    if exclusions is None:
        exclusions = _read_manifest_exclusions()
    else:
        exclusions = set(exclusions) | _read_manifest_exclusions()

    datasets_pool = list(datasets_pool or [
        "synthetic_alpha", "synthetic_beta", "synthetic_broad",
        "synthetic_8ch", "synthetic_16ch", "synthetic_32ch",
        "mne_sample", "physionet_real", "bci_iv2a_real_s1", "iris_graph_signal",
    ])

    graphs_pool = list(graphs_pool or [
        ("knn", {"k": 3}), ("knn", {"k": 5}), ("gaussian", {"sigma": 1.0}), ("kalofolias", {}),
    ])

    baselines = list(baselines or ["linear", "ica", "spherical_spline", "rbfi_tps"])
    gsp_methods = list(gsp_methods or ["gsp", "tikhonov", "bgsrp", "gsmooth", "idw"])
    tv_methods = list(tv_methods or ["trss", "sobolev_temporal", "graph_time_tikhonov", "temporal_laplacian", "tv"])

    # Filter TV family by exclusions
    tv_methods = [m for m in tv_methods if m not in exclusions]

    families = [baselines, gsp_methods, tv_methods]

    iterdefs: List[Dict[str, Any]] = []
    for i in range(1, n + 1):
        tag = f"it{i:02d}"
        ds = [datasets_pool[(i - 1) % len(datasets_pool)]]
        graph = [graphs_pool[(i - 1) % len(graphs_pool)]]
        family_methods = families[(i - 1) % len(families)]

        methods = []
        # Always include baselines first then the family methods for the iteration
        for m in list(dict.fromkeys(list(baselines) + list(family_methods))):
            if m not in exclusions:
                methods.append(m)

        iterdefs.append({
            "key": tag,
            "tag": tag,
            "description": f"Auto-generated schedule {tag}",
            "fase": "auto",
            "objective": "Measure improvement vs canonical baselines",
            "datasets": ds,
            "mode": "base",
            "missing_list": [0.1, 0.2, 0.3],
            "seeds": list(range(seed_count)),
            "graph_specs": graph,
            "lambdas": [0.05, 0.1, 0.2, 0.4],
            "snr_levels": [20.0, 10.0, 5.0, 0.0],
            "methods": methods,
        })

    return iterdefs


def generate_light_profile(iterdefs: List[Dict[str, Any]], picks: Sequence[int] | None = None) -> List[Dict[str, Any]]:
    """Return a reduced subset for light-profile pilots.

    `picks` is a sequence of integer iteration indices (1-based), defaulting to [17, 48].
    The function will shrink seeds, reduce missing_list to `[0.2]` and shorten graphs.
    """
    if picks is None:
        picks = [17, 48]
    picks_set = set(int(x) for x in picks)
    out: List[Dict[str, Any]] = []
    for d in iterdefs:
        try:
            idx = int(d.get("key", "it0").lstrip("it"))
        except Exception:
            continue
        if idx in picks_set:
            d2 = dict(d)
            d2["seeds"] = [0, 1]
            d2["missing_list"] = [0.2]
            if isinstance(d2.get("graph_specs"), list) and d2["graph_specs"]:
                d2["graph_specs"] = d2["graph_specs"][:1]
            out.append(d2)
    return out


def save_iterdefs_json(iterdefs: List[Dict[str, Any]], path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    payload = {"generated": datetime.datetime.utcnow().isoformat() + "Z", "iterations": iterdefs}
    with p.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # Simple CLI for ad-hoc generation
    import argparse

    parser = argparse.ArgumentParser(description="Generate simple iteration schedule (JSON)")
    parser.add_argument("--n", type=int, default=50, help="Number of iterations to generate")
    parser.add_argument("--out", type=str, default=str(ROOT / "experiments" / "schedules" / "it01-it50_schedule.json"))
    parser.add_argument("--light-out", type=str, default=str(ROOT / "experiments" / "schedules" / "it01-it50_light_profile.json"))
    args = parser.parse_args()
    itds = generate_iterdefs(n=args.n)
    save_iterdefs_json(itds, args.out)
    light = generate_light_profile(itds)
    save_iterdefs_json(light, args.light_out)
