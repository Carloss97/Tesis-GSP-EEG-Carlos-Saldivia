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
import importlib.util
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


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    loader = spec.loader
    assert loader is not None
    sys.modules[spec.name] = mod
    loader.exec_module(mod)
    return mod


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

    # Prepare logs and read batch size for skip ratio heuristics
    logs = RESULTS_DIR / "batch_logs"
    logs.mkdir(parents=True, exist_ok=True)
    log_file = logs / f"{batch_file.stem}.log"
    try:
        payload = json.loads(batch_file.read_text(encoding="utf-8"))
        total_iters = len(payload.get("iterations", []))
    except Exception:
        total_iters = 0

    # thresholds
    MIN_SKIP_COUNT = 3
    SKIP_RATIO_THRESHOLD = 0.2 if total_iters > 0 else 0.5

    # Run pilot and stream stdout to monitor skips/errors in real time
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    skipped = 0
    errors_found = 0
    try:
        # iterate lines as they are produced
        assert proc.stdout is not None
        with open(log_file, "w", encoding="utf-8") as lf:
            for raw_line in proc.stdout:
                lf.write(raw_line)
                lf.flush()
                line = raw_line.strip()
                # simple heuristics to detect problems
                if "[SKIPPED]" in line or "Skipped:" in line or "SKIPPED" in line:
                    skipped += 1
                    # if many skips relative to batch size, stop this batch
                    if skipped >= MIN_SKIP_COUNT or (total_iters > 0 and (skipped / total_iters) >= SKIP_RATIO_THRESHOLD):
                        print(f"Stopping {batch_file.name}: detected {skipped} skipped iterations (threshold exceeded)")
                        proc.kill()
                        break
                if "Traceback" in line or line.startswith("Exception") or "Error" in line:
                    errors_found += 1
                    print(f"Stopping {batch_file.name}: detected error line: {line}")
                    proc.kill()
                    break
        proc.wait()
    except Exception as exc:
        try:
            proc.kill()
        except Exception:
            pass
        with open(log_file, "a", encoding="utf-8") as lf:
            lf.write(f"\n[RUNNER ERROR] {exc}\n")

    return batch_file.name, (proc.returncode if proc.returncode is not None else -1)


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

    # Normalize schedule file in-place to canonical method names (idempotent)
    try:
        norm_mod = _load_module(ROOT / "experiments" / "normalize_schedule_methods.py", "normalize_schedule_methods")
        norm_mod.normalize_file(args.schedule)
    except Exception as exc:
        print(f"Schedule normalization failed: {exc}")

    sched = json.loads(args.schedule.read_text(encoding="utf-8"))
    raw_iterations = sched.get("iterations", [])
    if not raw_iterations:
        print("Schedule contains no iterations.")
        return 0

    iterations: List[Dict[str, Any]] = []
    skipped_invalid: List[Dict[str, Any]] = []
    for idx, it in enumerate(raw_iterations, start=1):
        if not isinstance(it, dict):
            skipped_invalid.append({"index": idx, "reason": "not_an_object"})
            continue
        if not it.get("tag"):
            skipped_invalid.append({"index": idx, "reason": "missing_tag", "key": it.get("key")})
            continue
        if not it.get("datasets"):
            skipped_invalid.append({"index": idx, "reason": "missing_datasets", "key": it.get("key") or it.get("tag")})
            continue
        iterations.append(it)

    if skipped_invalid:
        print(f"Skipped invalid iterations during batching: {len(skipped_invalid)}")

    if not iterations:
        print("No valid iterations left after validation.")
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
        "skipped_invalid_iterations": skipped_invalid,
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
