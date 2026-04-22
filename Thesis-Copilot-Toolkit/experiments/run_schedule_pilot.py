"""Run a pilot schedule (light-profile) by loading a schedule JSON and
executing iterations using the existing runner engine (it121-it130 engine).

This script is conservative: it will catch per-iteration failures and write
a `pilot_skipped_iterations.json` file under `Thesis-Copilot-Toolkit/results/`
if any iterations are skipped.

Usage:
  python experiments/run_schedule_pilot.py --schedule experiments/schedules/it01-it50_light_profile.json
"""
from __future__ import annotations

import argparse
import json
import importlib.util
import sys
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[1]
SCHEDULE_DEFAULT = ROOT / "experiments" / "schedules" / "it01-it50_light_profile.json"
BASE_RUNNER = ROOT / "experiments" / "run_future_work_it121_it130.py"


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    loader = spec.loader
    assert loader is not None
    sys.modules[spec.name] = mod
    loader.exec_module(mod)
    return mod


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run pilot schedule (light-profile)")
    parser.add_argument("--schedule", type=Path, default=SCHEDULE_DEFAULT)
    parser.add_argument("--tags", nargs="*", default=None, help="Optional subset of iteration keys to run (e.g. it17 it48)")
    parser.add_argument("--stop-on-error", action="store_true")
    parser.add_argument("--light-profile", action="store_true", help="Use operational-close profile in base runner")
    args = parser.parse_args(argv)

    if not args.schedule.exists():
        print(f"Schedule not found: {args.schedule}")
        return 2
    # Normalize schedule file in-place to canonical method names (idempotent)
    try:
        norm_mod = _load_module(ROOT / "experiments" / "normalize_schedule_methods.py", "normalize_schedule_methods")
        norm_mod.normalize_file(args.schedule)
    except Exception as exc:
        print(f"Schedule normalization failed: {exc}")

    sched = json.loads(args.schedule.read_text(encoding="utf-8"))
    iters = sched.get("iterations", [])
    if args.tags:
        iters = [it for it in iters if it.get("key") in set(args.tags)]

    if not iters:
        print("No iterations selected in schedule.")
        return 0

    base = _load_module(BASE_RUNNER, "run121130_base")

    # Ensure results dir exists
    base.RESULTS.mkdir(parents=True, exist_ok=True)

    check = base.load_data_availability()
    availability = check["availability"]
    data = check["data"]

    failed: List[Dict[str, Any]] = []
    completed: List[str] = []

    for d in iters:
        key = d.get("key")
        print(f"--- Running pilot iteration: {key}")
        try:
            # Prepare and map graph_specs (support shorthand mappings)
            raw_graph_specs = d.get("graph_specs", [])
            mapped_graph_specs = []
            for g in raw_graph_specs:
                # Expecting entries like [method, params]
                if isinstance(g, list) and len(g) == 2:
                    method_raw = str(g[0])
                    params = dict(g[1]) if isinstance(g[1], dict) else {}
                    # Small alias map for legacy names and shorthands (defensive)
                    alias_map = {
                        "e-nn": "epsilon_ball",
                        "knn_gaussian": "knng",
                        "vknn_gaussian": "vknng",
                        "kaliofolias": "kalofolias",
                    }
                    method_key = method_raw.lower()
                    method = alias_map.get(method_key, method_raw)

                    # Normalize parameters for known shorthands
                    if method == "epsilon_ball":
                        if "radius" in params:
                            params["epsilon"] = params.pop("radius")

                    # Normalize legacy graph parameters to current constructor signatures.
                    if method == "aew":
                        if "alpha" in params and "beta" not in params:
                            params["beta"] = params.pop("alpha")
                        params.setdefault("k", 4)
                        params.setdefault("sigma", "median")

                    if method == "kalofolias":
                        if "alpha" in params and "a" not in params:
                            params["a"] = params.pop("alpha")
                        params.setdefault("a", 1.0)
                        params.setdefault("b", 1.0)

                    mapped_graph_specs.append([method, params])
                else:
                    mapped_graph_specs.append(g)

            # Construct base.IterDef instance from dict
            it = base.IterDef(
                key=d.get("key"),
                tag=d.get("tag"),
                description=d.get("description", ""),
                fase=d.get("fase", "auto"),
                objective=d.get("objective", ""),
                datasets=d.get("datasets", []),
                mode=d.get("mode", "base"),
                missing_list=d.get("missing_list", [0.2]),
                seeds=d.get("seeds", [0, 1]),
                graph_specs=[tuple(g) if isinstance(g, list) and len(g) == 2 else g for g in mapped_graph_specs],
                lambdas=d.get("lambdas", []),
                snr_levels=d.get("snr_levels", []),
                methods=d.get("methods", None),
            )

            base._run_iteration(it, availability, data, operational_close_profile=bool(args.light_profile))
            completed.append(key)
            print(f"[OK] {key}")
        except Exception as exc:
            failed.append({"iteration": key, "error": str(exc)})
            print(f"[SKIPPED] {key}: {exc}")
            if args.stop_on_error:
                break

    if failed:
        out = base.RESULTS / "pilot_skipped_iterations.json"
        out.write_text(json.dumps(failed, ensure_ascii=False, indent=2), encoding="utf-8")

    print("Pilot completed. Success:", completed)
    if failed:
        print("Skipped:", [f["iteration"] for f in failed])
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
