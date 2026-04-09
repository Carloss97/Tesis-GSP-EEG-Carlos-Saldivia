#!/usr/bin/env python3
"""Rerun failed iterations sequentially using the iteration wrapper.

Writes per-iteration stdout/stderr to `rerun_logs/` and produces
`retry_run_now_summary.json` when finished.
"""
from __future__ import annotations

import json
import os
import subprocess
import time
import sys
from pathlib import Path
from datetime import datetime

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
FAILED_FILE = HERE / 'failed_to_retry.json'
WRAPPER = HERE / 'run_iteration_wrapper.py'
PYTHON = REPO_ROOT / '.venv' / 'Scripts' / 'python.exe'
LOG_DIR = HERE / 'rerun_logs'
LOG_DIR.mkdir(parents=True, exist_ok=True)
SUMMARY_OUT = HERE / 'retry_run_now_summary.json'
PER_ITER_TIMEOUT = int(os.environ.get('PER_ITER_TIMEOUT', 10800))  # seconds
SLEEP_BETWEEN = 2


def load_failed_list() -> list[str]:
    if FAILED_FILE.exists():
        with open(FAILED_FILE, 'r', encoding='utf-8') as f:
            j = json.load(f)
            return j.get('failed_iterations', [])
    # fallback: inspect retry_execution_summary.json
    summary_in = HERE / 'retry_execution_summary.json'
    if summary_in.exists():
        with open(summary_in, 'r', encoding='utf-8') as f:
            j = json.load(f)
            return [e.get('iteration') for e in j.get('failed', [])]
    return []


def run_iteration(iteration: str) -> dict:
    python_path = str(PYTHON) if PYTHON.exists() else sys.executable
    wrapper_path = str(WRAPPER)
    cmd = [python_path, wrapper_path, '--iteration_tag', iteration]

    stdout_path = str(LOG_DIR / f"{iteration}_retry_now_stdout.log")
    stderr_path = str(LOG_DIR / f"{iteration}_retry_now_stderr.log")

    start = time.time()
    env = os.environ.copy()
    env['PYTHONUTF8'] = '1'
    env['PYTHONIOENCODING'] = 'utf-8'
    try:
        with open(stdout_path, 'wb') as out, open(stderr_path, 'wb') as err:
            proc = subprocess.run(cmd, cwd=REPO_ROOT, env=env, stdout=out, stderr=err, timeout=PER_ITER_TIMEOUT)
        elapsed = time.time() - start
        return {'iteration': iteration, 'status': 'ok' if proc.returncode == 0 else 'failed', 'returncode': proc.returncode, 'elapsed_s': elapsed, 'stdout': stdout_path, 'stderr': stderr_path}
    except subprocess.TimeoutExpired:
        return {'iteration': iteration, 'status': 'timed_out', 'timeout_s': PER_ITER_TIMEOUT, 'stdout': stdout_path, 'stderr': stderr_path}
    except Exception as e:
        try:
            with open(stderr_path, 'a', encoding='utf-8') as ef:
                ef.write('Exception: ' + str(e) + '\n')
        except Exception:
            pass
        return {'iteration': iteration, 'status': 'failed', 'error': str(e), 'stdout': stdout_path, 'stderr': stderr_path}


def main():
    failed = load_failed_list()
    if not failed:
        print('No failed iterations found to retry.')
        return 0

    print(f"Starting reattempts for {len(failed)} iterations (per-iter timeout={PER_ITER_TIMEOUT}s)")
    results = {'started_at': datetime.utcnow().isoformat() + 'Z', 'succeeded': [], 'failed': [], 'timed_out': []}

    for it in failed:
        print(f"Running {it} ...", flush=True)
        r = run_iteration(it)
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

    print('Completed reattempts. Summary saved to', SUMMARY_OUT)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
