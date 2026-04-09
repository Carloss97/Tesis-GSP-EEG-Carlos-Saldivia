#!/usr/bin/env python3
"""Run only dry-run (--dry-run) for each failed iteration to verify setup.

Outputs per-iteration logs to `rerun_logs/` and writes `dryrun_summary.json`.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
FAILED_FILE = HERE / 'failed_to_retry.json'
WRAPPER = HERE / 'run_iteration_wrapper.py'
PYTHON = REPO_ROOT / '.venv' / 'Scripts' / 'python.exe'
LOG_DIR = HERE / 'rerun_logs'
LOG_DIR.mkdir(parents=True, exist_ok=True)
SUMMARY_OUT = HERE / 'dryrun_summary.json'

TIMEOUT = int(os.environ.get('DRY_TIMEOUT', 120))
SLEEP_BETWEEN = 1


def load_failed_list() -> list[str]:
    if FAILED_FILE.exists():
        with open(FAILED_FILE, 'r', encoding='utf-8') as f:
            j = json.load(f)
            return j.get('failed_iterations', [])
    return []


def run_dry(iteration: str) -> dict:
    python_path = str(PYTHON) if PYTHON.exists() else sys.executable
    cmd = [python_path, str(WRAPPER), '--iteration_tag', iteration, '--dry-run']
    stdout_path = LOG_DIR / f"{iteration}_dry_stdout.log"
    stderr_path = LOG_DIR / f"{iteration}_dry_stderr.log"
    env = os.environ.copy()
    env['PYTHONUTF8'] = '1'
    env['PYTHONIOENCODING'] = 'utf-8'
    start = time.time()
    try:
        with open(stdout_path, 'wb') as out, open(stderr_path, 'wb') as err:
            proc = subprocess.run(cmd, cwd=REPO_ROOT, env=env, stdout=out, stderr=err, timeout=TIMEOUT)
        elapsed = time.time() - start
        return {'iteration': iteration, 'status': 'ok' if proc.returncode == 0 else 'failed', 'returncode': proc.returncode, 'elapsed_s': elapsed, 'stdout': str(stdout_path), 'stderr': str(stderr_path)}
    except subprocess.TimeoutExpired:
        return {'iteration': iteration, 'status': 'timed_out', 'timeout_s': TIMEOUT, 'stdout': str(stdout_path), 'stderr': str(stderr_path)}
    except Exception as e:
        return {'iteration': iteration, 'status': 'failed', 'error': str(e), 'stdout': str(stdout_path), 'stderr': str(stderr_path)}


def main() -> int:
    failed = load_failed_list()
    if not failed:
        print('No failed iterations found.')
        return 0

    print(f"Running dry-run for {len(failed)} iterations (timeout={TIMEOUT}s)")
    results = {'started_at': datetime.utcnow().isoformat() + 'Z', 'succeeded': [], 'failed': [], 'timed_out': []}

    for it in failed:
        print(f"Dry-run {it}...", flush=True)
        r = run_dry(it)
        if r['status'] == 'ok':
            results['succeeded'].append(r)
        elif r['status'] == 'timed_out':
            results['timed_out'].append(r)
        else:
            results['failed'].append(r)
        time.sleep(SLEEP_BETWEEN)

    results['finished_at'] = datetime.utcnow().isoformat() + 'Z'
    with open(SUMMARY_OUT, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print('Dry-run pass complete. Summary written to', SUMMARY_OUT)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
