#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH_RUN = ROOT / "experiments" / "run_future_work_it121_it130.py"

spec = importlib.util.spec_from_file_location("run121130_base", str(PATH_RUN))
mod = importlib.util.module_from_spec(spec)
loader = spec.loader
assert loader is not None
# Ensure module is discoverable by dataclasses and subimports
sys.modules[spec.name] = mod
loader.exec_module(mod)

result = mod.load_data_availability()
info = result.get("availability", result)
print(json.dumps(info, indent=2, ensure_ascii=False))
