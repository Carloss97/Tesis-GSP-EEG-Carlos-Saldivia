"""Generate schedule files for iterations it01..it50 and a light-profile subset.

This script uses `iterdef.py` to produce JSON schedules that can be
inspected and later consumed by runner logic. It does NOT execute any
experiments.
"""
from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
from typing import List


ROOT = Path(__file__).resolve().parents[1]
ITERDEF_PATH = ROOT / "experiments" / "iterdef.py"


def _load_iterdef_module():
    spec = importlib.util.spec_from_file_location("iterdef_module", str(ITERDEF_PATH))
    mod = importlib.util.module_from_spec(spec)
    loader = spec.loader
    assert loader is not None
    import sys

    sys.modules[spec.name] = mod
    loader.exec_module(mod)
    return mod


def main(argv: List[str] | None = None):
    parser = argparse.ArgumentParser(description="Generate it01-it50 schedule and a light-profile subset")
    parser.add_argument("--n", type=int, default=50, help="Number of iterations to generate")
    parser.add_argument("--out", type=Path, default=ROOT / "experiments" / "schedules" / "it01-it50_schedule.json")
    parser.add_argument("--light-out", type=Path, default=ROOT / "experiments" / "schedules" / "it01-it50_light_profile.json")
    parser.add_argument("--picks", type=str, default="17,48", help="Comma-separated 1-based iteration indices for light-profile picks")
    args = parser.parse_args(argv)

    mod = _load_iterdef_module()
    itds = mod.generate_iterdefs(n=args.n)
    picks = [int(x) for x in args.picks.split(",") if x.strip()]
    light = mod.generate_light_profile(itds, picks=picks)

    mod.save_iterdefs_json(itds, args.out)
    mod.save_iterdefs_json(light, args.light_out)

    print(f"Wrote full schedule: {args.out}")
    print(f"Wrote light-profile schedule: {args.light_out} (picks={picks})")
    print(f"Iterations generated: {len(itds)}; light subset: {len(light)}")


if __name__ == "__main__":
    main()
