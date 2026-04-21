"""Split a schedule JSON into batches and optionally run them in parallel.

Usage examples:
  # Create 20 batch files (dry-run)
  python experiments/run_schedule_in_batches.py --schedule experiments/schedules/it_exhaustive_from_registry.json --n-batches 20

  # Create batches and run them with 4 workers
  python experiments/run_schedule_in_batches.py --schedule experiments/schedules/it_exhaustive_from_registry.json --n-batches 20 --concurrency 4 --start

This script uses `experiments/run_schedule_pilot.py` to execute each batch.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import math
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Tuple


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEDULE = ROOT / "experiments" / "schedules" / "it_exhaustive_from_registry.json"
BATCH_DIR_DEFAULT = ROOT / "experiments" / "schedules" / "batches"
PILOT_SCRIPT = ROOT / "experiments" / "run_schedule_pilot.py"
RESULTS_DIR = ROOT / "results"


def partition(lst: List[Any], n: int) -> List[List[Any]]:
    if n <= 0:
        return [lst]
    total = len(lst)
    base = total // n
    rem = total % n
    parts: List[List[Any]] = []
    start = 0
    for i in range(n):
        size = base + (1 if i < rem else 0)
        parts.append(lst[start : start + size])
        start += size
    return parts


def write_batch_file(batch_dir: Path, base_name: str, idx: int, iterations: List[Dict[str, Any]]) -> Path:
    batch_dir.mkdir(parents=True, exist_ok=True)
    out = batch_dir / f"{base_name}.batch_{idx:03d}.json"
    payload = {
        "generated": datetime.utcnow().isoformat() + "Z",
        "iterations": iterations,
    }
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return out


def run_batch(batch_file: Path, stop_on_error: bool, light_profile: bool) -> Tuple[str, int]:
    cmd = [sys.executable, str(PILOT_SCRIPT), "--schedule", str(batch_file)]
    if stop_on_error:
        cmd.append("--stop-on-error")
    if light_profile:
        cmd.append("--light-profile")

    print(f"Starting: {' '.join(cmd)}")
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    logs = RESULTS_DIR / "batch_logs"
    logs.mkdir(parents=True, exist_ok=True)
    log_file = logs / f"{batch_file.stem}.log"
    log_file.write_text(proc.stdout or "", encoding="utf-8")

    return batch_file.name, proc.returncode


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Split schedule into batches and optionally run them in parallel")
    parser.add_argument("--schedule", type=Path, default=DEFAULT_SCHEDULE)
    parser.add_argument("--n-batches", type=int, default=20, help="Number of batches to split into")
    parser.add_argument("--concurrency", type=int, default=max(1, min(4, (os.cpu_count() or 1))), help="Parallel workers when running batches")
    parser.add_argument("--batch-dir", type=Path, default=BATCH_DIR_DEFAULT)
    parser.add_argument("--start", action="store_true", help="Start executing the batches after creating them")
    parser.add_argument("--stop-on-error", action="store_true", help="Pass --stop-on-error to pilot script")
    parser.add_argument("--light-profile", action="store_true", help="Pass --light-profile to pilot script")
    parser.add_argument("--min-size", type=int, default=1, help="Minimum iterations per batch (skip empty batches)")
    args = parser.parse_args(argv)

    if not args.schedule.exists():
        print(f"Schedule not found: {args.schedule}")
        return 2

    sched = json.loads(args.schedule.read_text(encoding="utf-8"))
    iterations = sched.get("iterations", [])
    if not iterations:
        print("Schedule contains no iterations.")
        return 0

    n_batches = min(args.n_batches, len(iterations))
    parts = partition(iterations, n_batches)

    base_name = args.schedule.stem
    batch_files: List[Path] = []
    for i, part in enumerate(parts, start=1):
        if not part or len(part) < args.min_size:
            continue
        batch_file = write_batch_file(args.batch_dir, base_name, i, part)
        batch_files.append(batch_file)

    print(f"Created {len(batch_files)} batch files in {args.batch_dir}")

    summary: Dict[str, Any] = {
        "created_batches": [str(p) for p in batch_files],
        "n_batches": len(batch_files),
        "generated": datetime.utcnow().isoformat() + "Z",
    }

    if args.start and batch_files:
        print(f"Launching {len(batch_files)} batches with concurrency={args.concurrency}")
        results: List[Dict[str, Any]] = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as ex:
            futures = {ex.submit(run_batch, bf, args.stop_on_error, args.light_profile): bf for bf in batch_files}
            for fut in concurrent.futures.as_completed(futures):
                bf = futures[fut]
                try:
                    name, code = fut.result()
                    results.append({"batch": name, "returncode": code})
                    print(f"Finished {name} -> returncode={code}")
                except Exception as exc:
                    results.append({"batch": str(bf), "error": str(exc)})
                    print(f"Batch {bf} failed: {exc}")

        summary["run_results"] = results

    out = RESULTS_DIR / "batch_run_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote summary to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
