#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH_RUN = ROOT / "experiments" / "run_future_work_it121_it130.py"

spec = importlib.util.spec_from_file_location("run121130_base", str(PATH_RUN))
mod = importlib.util.module_from_spec(spec)
loader = spec.loader
assert loader is not None
loader.exec_module(mod)

availability = mod.load_data_availability()
print(json.dumps(availability, indent=2, ensure_ascii=False))
