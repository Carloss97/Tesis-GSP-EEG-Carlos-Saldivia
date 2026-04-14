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
