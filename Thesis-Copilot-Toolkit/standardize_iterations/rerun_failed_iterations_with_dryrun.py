#!/usr/bin/env python3
"""Two-phase rerun helper: dry-run (fast checks) then full run for passing iterations.

Writes per-iteration logs to `rerun_logs/` and a summary `retry_with_dryrun_summary.json`.
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
SUMMARY_OUT = HERE / 'retry_with_dryrun_summary.json'

DRY_TIMEOUT = int(os.environ.get('DRY_TIMEOUT', 300))
FULL_TIMEOUT = int(os.environ.get('PER_ITER_TIMEOUT', 10800))
SLEEP_BETWEEN = 2


def load_failed_list() -> list[str]:
    if FAILED_FILE.exists():
        with open(FAILED_FILE, 'r', encoding='utf-8') as f:
            j = json.load(f)
            return j.get('failed_iterations', [])
    return []


def run_cmd(cmd: list[str], stdout_path: Path, stderr_path: Path, timeout: int) -> dict:
    env = os.environ.copy()
    env['PYTHONUTF8'] = '1'
    env['PYTHONIOENCODING'] = 'utf-8'
    start = time.time()
    try:
        with open(stdout_path, 'wb') as out, open(stderr_path, 'wb') as err:
            proc = subprocess.run(cmd, cwd=REPO_ROOT, env=env, stdout=out, stderr=err, timeout=timeout)
        elapsed = time.time() - start
        return {'returncode': proc.returncode, 'elapsed_s': elapsed}
    except subprocess.TimeoutExpired:
        return {'timeout': True}
    except Exception as e:
        return {'error': str(e)}


def main() -> int:
    failed = load_failed_list()
    if not failed:
        print('No failed iterations found to retry.')
        return 0

    print(f"Starting two-phase reattempts for {len(failed)} iterations (dry_timeout={DRY_TIMEOUT}s, full_timeout={FULL_TIMEOUT}s)")
    results = {'started_at': datetime.utcnow().isoformat() + 'Z', 'succeeded': [], 'failed': [], 'timed_out': []}

    python_path = str(PYTHON) if PYTHON.exists() else sys.executable
    wrapper_path = str(WRAPPER)

    for it in failed:
        print(f"Dry-run {it} ...", flush=True)
        dry_stdout = LOG_DIR / f"{it}_dry_stdout.log"
        dry_stderr = LOG_DIR / f"{it}_dry_stderr.log"
        cmd_dry = [python_path, wrapper_path, '--iteration_tag', it, '--dry-run']
        r = run_cmd(cmd_dry, dry_stdout, dry_stderr, DRY_TIMEOUT)
        if r.get('timeout'):
            results['timed_out'].append({'iteration': it, 'phase': 'dry', 'timeout_s': DRY_TIMEOUT, 'stdout': str(dry_stdout), 'stderr': str(dry_stderr)})
            continue
        if r.get('error'):
            results['failed'].append({'iteration': it, 'phase': 'dry', 'error': r['error'], 'stdout': str(dry_stdout), 'stderr': str(dry_stderr)})
            continue
        if r.get('returncode', 1) != 0:
            results['failed'].append({'iteration': it, 'phase': 'dry', 'returncode': r.get('returncode'), 'stdout': str(dry_stdout), 'stderr': str(dry_stderr)})
            continue

        # dry-run passed, run full
        print(f"Full-run {it} ...", flush=True)
        full_stdout = LOG_DIR / f"{it}_full_stdout.log"
        full_stderr = LOG_DIR / f"{it}_full_stderr.log"
        cmd_full = [python_path, wrapper_path, '--iteration_tag', it]
        # Optionally run full runs with a light profile to speed up retries
        if os.environ.get('USE_LIGHT_PROFILE', '') == '1':
            cmd_full.append('--light-profile')
        r2 = run_cmd(cmd_full, full_stdout, full_stderr, FULL_TIMEOUT)
        if r2.get('timeout'):
            results['timed_out'].append({'iteration': it, 'phase': 'full', 'timeout_s': FULL_TIMEOUT, 'stdout': str(full_stdout), 'stderr': str(full_stderr)})
            continue
        if r2.get('error'):
            results['failed'].append({'iteration': it, 'phase': 'full', 'error': r2['error'], 'stdout': str(full_stdout), 'stderr': str(full_stderr)})
            continue
        if r2.get('returncode', 1) != 0:
            results['failed'].append({'iteration': it, 'phase': 'full', 'returncode': r2.get('returncode'), 'stdout': str(full_stdout), 'stderr': str(full_stderr)})
            continue

        results['succeeded'].append({'iteration': it, 'elapsed_s': r2.get('elapsed_s', 0), 'stdout': str(full_stdout), 'stderr': str(full_stderr)})
        time.sleep(SLEEP_BETWEEN)

    results['finished_at'] = datetime.utcnow().isoformat() + 'Z'
    with open(SUMMARY_OUT, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

    print('Completed two-phase reattempts. Summary saved to', SUMMARY_OUT)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
