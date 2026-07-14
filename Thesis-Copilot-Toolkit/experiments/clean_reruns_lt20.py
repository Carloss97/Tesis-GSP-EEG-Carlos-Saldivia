#!/usr/bin/env python3
"""
Delete all existing result artifacts for the LT20 reruns defined in experiments/run_reruns_selected.py
Run from repo root.
"""
import importlib.util, sys, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / 'experiments' / 'run_reruns_selected.py'
RESULTS = ROOT / 'results'

spec = importlib.util.spec_from_file_location('runner_mod', str(RUNNER))
runner = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = runner
spec.loader.exec_module(runner)

removed = []
defs = getattr(runner, '_defs', [])
for d in defs:
    k = d.key
    for p in list(RESULTS.glob(f"{k}*")):
        try:
            if p.is_dir():
                shutil.rmtree(p)
            else:
                p.unlink()
            removed.append(str(p))
        except Exception as e:
            print("Failed to remove", p, ":", e)
print(f"Removed {len(removed)} items.")
for i,r in enumerate(removed[:200]):
    print(r)
if len(removed)>200:
    print("...and", len(removed)-200, "more")
