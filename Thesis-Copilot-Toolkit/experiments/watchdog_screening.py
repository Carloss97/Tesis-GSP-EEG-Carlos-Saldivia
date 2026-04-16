"""
Watchdog for the screening-stage run.

Monitors `results_screening_2000` for progress (new `_run_metadata.json` files).
If no progress is observed for `--threshold` minutes, the watchdog will attempt to
restart the screening runner (`run_screening_2000.py --light-profile --n N`).

Usage (from repo root):
  $env:PYTHONPATH='Thesis-Copilot-Toolkit'; & .venv\Scripts\python.exe Thesis-Copilot-Toolkit\experiments\watchdog_screening.py

This script is intentionally simple and conservative: it logs restarts and
avoids rapid repeated restarts by waiting after a restart.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parents[1]


def count_completed(results_dir: Path) -> int:
    return len(list(results_dir.glob("*_run_metadata.json")))


def now_ts() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")


def main():
    parser = argparse.ArgumentParser(description='Watchdog for screening results')
    parser.add_argument('--results', type=str, default='results_screening_2000')
    parser.add_argument('--threshold', type=int, default=60, help='minutes of inactivity before restart')
    parser.add_argument('--poll', type=int, default=300, help='poll interval in seconds')
    parser.add_argument('--run-cmd', type=str, default=str(ROOT / 'experiments' / 'run_screening_2000.py'))
    parser.add_argument('--run-args', type=str, default='--light-profile --n 2000')
    args = parser.parse_args()

    results_dir = ROOT / args.results
    threshold_sec = args.threshold * 60
    poll = args.poll
    run_cmd = args.run_cmd
    run_args = args.run_args

    logfile = results_dir / 'watchdog_log.txt'
    logfile.parent.mkdir(parents=True, exist_ok=True)

    last_count = count_completed(results_dir) if results_dir.exists() else 0
    last_activity = time.time()
    restarts = 0

    with open(logfile, 'a', encoding='utf-8') as fh:
        fh.write(f"{now_ts()} WATCHDOG START. initial_count={last_count}\n")

    while True:
        try:
            current = count_completed(results_dir)
            if current > last_count:
                last_count = current
                last_activity = time.time()
                with open(logfile, 'a', encoding='utf-8') as fh:
                    fh.write(f"{now_ts()} PROGRESS: count={current}\n")
            else:
                idle = time.time() - last_activity
                with open(logfile, 'a', encoding='utf-8') as fh:
                    fh.write(f"{now_ts()} IDLE: count={current} idle_sec={int(idle)}\n")
                if idle > threshold_sec:
                    # attempt restart
                    with open(logfile, 'a', encoding='utf-8') as fh:
                        fh.write(f"{now_ts()} STALLED for {int(idle)}s — attempting restart #{restarts+1}\n")
                    cmd = [sys.executable, run_cmd] + run_args.split()
                    # start as a detached background process (platform dependent)
                    try:
                        subprocess.Popen(cmd, cwd=str(ROOT))
                        restarts += 1
                        last_activity = time.time()
                        with open(logfile, 'a', encoding='utf-8') as fh:
                            fh.write(f"{now_ts()} STARTED: {' '.join(cmd)}\n")
                        # wait a bit before next check to avoid rapid respawns
                        time.sleep(60)
                    except Exception as exc:
                        with open(logfile, 'a', encoding='utf-8') as fh:
                            fh.write(f"{now_ts()} RESTART-FAILED: {exc}\n")

            time.sleep(poll)
        except KeyboardInterrupt:
            with open(logfile, 'a', encoding='utf-8') as fh:
                fh.write(f"{now_ts()} WATCHDOG STOPPED BY USER\n")
            raise
        except Exception as exc:
            with open(logfile, 'a', encoding='utf-8') as fh:
                fh.write(f"{now_ts()} ERROR: {exc}\n")
            time.sleep(poll)


if __name__ == '__main__':
    main()
