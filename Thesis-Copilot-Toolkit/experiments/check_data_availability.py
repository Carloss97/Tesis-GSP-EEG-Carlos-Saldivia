"""Check data availability using the engine's loader and write JSON result.

Usage: python experiments/check_data_availability.py
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

mod_path = ROOT / "experiments" / "run_future_work_it121_it130.py"
spec = importlib.util.spec_from_file_location("run_engine", str(mod_path))
mod = importlib.util.module_from_spec(spec)
loader = spec.loader
assert loader is not None
loader.exec_module(mod)

avail = mod.load_data_availability()

out_dir = ROOT / "experiments" / "results"
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / "data_availability.json"
out_file.write_text(json.dumps(avail, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(avail, ensure_ascii=False, indent=2))
#!/usr/bin/env python3
import importlib.util, sys, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'experiments' / 'run_future_work_it121_it130.py'
spec = importlib.util.spec_from_file_location('engine', str(BASE))
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)
info = mod.load_data_availability()['availability']
print(json.dumps(info, ensure_ascii=False, indent=2))
