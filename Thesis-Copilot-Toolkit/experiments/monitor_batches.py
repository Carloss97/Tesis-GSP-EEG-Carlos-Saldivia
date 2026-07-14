"""Simple monitor for batch runs.

Prints progress (number of batch logs present) every `--poll` seconds and tails last lines
from the most-recent batch logs. Intended to run alongside `run_schedule_in_batches.py`.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import List


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SUMMARY = ROOT / "results" / "batch_run_summary.json"
DEFAULT_LOGS = ROOT / "results" / "batch_logs"
DEFAULT_BATCH_DIR = ROOT / "experiments" / "schedules" / "batches"


def load_created_stems(summary_path: Path, batch_dir: Path) -> List[str]:
    if summary_path.exists():
        try:
            d = json.loads(summary_path.read_text(encoding="utf-8"))
            created = d.get("created_batches", [])
            stems = [Path(p).stem for p in created]
            if stems:
                return stems
        except Exception:
            pass

    # fallback: list batch dir
    if batch_dir.exists():
        return [p.stem for p in sorted(batch_dir.glob("*.json"))]
    return []


def tail_lines(p: Path, n: int = 20) -> str:
    try:
        with p.open("rb") as fh:
            fh.seek(0, 2)
            size = fh.tell()
            block = bytearray()
            blk_size = 1024
            while size > 0 and len(block) < 65536 and block.count(b"\n") <= n:
                read_size = min(blk_size, size)
                fh.seek(size - read_size)
                block.extend(fh.read(read_size))
                size -= read_size
            text = block.decode(errors="ignore")
            lines = text.splitlines()
            return "\n".join(lines[-n:])
    except Exception as e:
        return f"<failed to read {p}: {e}>"


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--batch-summary", type=Path, default=DEFAULT_SUMMARY)
    p.add_argument("--logs-dir", type=Path, default=DEFAULT_LOGS)
    p.add_argument("--batch-dir", type=Path, default=DEFAULT_BATCH_DIR)
    p.add_argument("--poll", type=int, default=30, help="Poll interval in seconds")
    p.add_argument("--tail", type=int, default=10, help="Lines to tail from recent logs")
    args = p.parse_args(argv)

    created_stems = load_created_stems(args.batch_summary, args.batch_dir)
    total = len(created_stems)
    if total == 0:
        print("No batch files found (nothing to monitor). Check --batch-summary or --batch-dir.")
        return 1

    print(f"Monitoring {total} batches. Poll every {args.poll}s. Logs: {args.logs_dir}")

    seen = set()
    try:
        while True:
            timestamp = datetime.utcnow().isoformat() + "Z"
            logs = sorted(args.logs_dir.glob("*.log")) if args.logs_dir.exists() else []
            completed = [p.stem for p in logs]
            n_completed = sum(1 for s in created_stems if s in completed)
            print(f"[{timestamp}] Completed {n_completed}/{total} batches (log files present: {len(logs)})")

            # show the most recent completed logs
            recent = [p for p in logs if p.stem in created_stems]
            recent = recent[-3:]
            for r in recent:
                if r.name not in seen:
                    print(f"--- Tail {r.name} ---")
                    print(tail_lines(r, args.tail))
                    print("--- end ---")
                    seen.add(r.name)

            if n_completed >= total:
                print("All batch logs present. Monitoring complete.")
                return 0

            time.sleep(args.poll)
    except KeyboardInterrupt:
        print("Monitor interrupted by user")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
