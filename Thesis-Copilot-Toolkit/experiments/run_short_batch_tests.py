"""Run short smoke tests for each batch JSON.

For each batch file under `experiments/schedules/batches`, invoke
`run_schedule_pilot.py` on the first N iteration keys (default 2) and
record return codes and short stdout/stderr tails to a results file.

Usage:
  python experiments/run_short_batch_tests.py
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BATCH_DIR = ROOT / "experiments" / "schedules" / "batches"
PILOT_SCRIPT = ROOT / "experiments" / "run_schedule_pilot.py"
RESULTS_DIR = ROOT / "experiments" / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE = RESULTS_DIR / "short_batch_test_results.json"

N_KEYS = 2
TIMEOUT = 120  # seconds per batch (short smoke)

summary = []

for f in sorted(BATCH_DIR.glob("*.json")):
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
    except Exception as e:
        summary.append({"batch": f.name, "error": f"load_error: {e}"})
        continue

    its = data.get("iterations", [])
    keys = [it.get("key") for it in its if isinstance(it, dict) and it.get("key")]
    keys = [k for k in keys if k][:N_KEYS]
    if not keys:
        summary.append({"batch": f.name, "skipped": "no_iterations"})
        continue

    cmd = [sys.executable, str(PILOT_SCRIPT), "--schedule", str(f), "--tags"] + keys + ["--stop-on-error"]
    print(f"Running batch {f.name} tags={keys} ...")
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT)
        out = (res.stdout or "").strip()
        err = (res.stderr or "").strip()
        summary.append({
            "batch": f.name,
            "tags": keys,
            "returncode": res.returncode,
            "stdout_tail": out[-400:],
            "stderr_tail": err[-400:],
        })
    except subprocess.TimeoutExpired as ex:
        summary.append({"batch": f.name, "tags": keys, "error": "timeout", "detail": str(ex)})
    except Exception as ex:
        summary.append({"batch": f.name, "tags": keys, "error": "runtime_error", "detail": str(ex)})

    # short pause to avoid overwhelming the system
    time.sleep(0.25)

OUT_FILE.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print("Done. Results written to", OUT_FILE)
print(json.dumps(summary, ensure_ascii=False, indent=2))
