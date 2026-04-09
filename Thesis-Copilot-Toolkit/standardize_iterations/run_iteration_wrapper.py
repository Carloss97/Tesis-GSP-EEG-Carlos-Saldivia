#!/usr/bin/env python3
"""
Wrapper to adapt generated rerun commands to repository runners.

Accepts generated flags like `--engine`, `--dataset`, `--scenarios`,
`--seeds`, `--iteration_tag` and dispatches to the appropriate
experiment script. Also forces UTF-8 for subprocesses to avoid
Windows encoding errors.

Usage: called by the runner (no direct user interaction required).
"""
from __future__ import annotations

import os
import re
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Optional


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
EXPERIMENTS_DIR = REPO_ROOT / 'Thesis-Copilot-Toolkit' / 'experiments'


def extract_iteration(argv: list[str]) -> Optional[str]:
    # look for --iteration_tag <itXXX>
    for i, a in enumerate(argv):
        if a == '--iteration_tag' and i + 1 < len(argv):
            return argv[i + 1]
        if a.startswith('--iteration_tag='):
            return a.split('=', 1)[1]
    # fallback: --tags
    for i, a in enumerate(argv):
        if a == '--tags' and i + 1 < len(argv):
            return argv[i + 1]
        if a.startswith('--tags='):
            return a.split('=', 1)[1]
    return None


def choose_script_for_iteration(tag: str) -> Path:
    m = re.match(r'it(\d{1,3})', tag)
    if not m:
        # default to canonical
        return EXPERIMENTS_DIR / 'run_canonical_experiment.py'
    num = int(m.group(1))
    if 101 <= num <= 104:
        return EXPERIMENTS_DIR / 'run_future_work_it101_it104.py'
    if 105 <= num <= 120:
        return EXPERIMENTS_DIR / 'run_future_work_it105_it120.py'
    if 121 <= num <= 130:
        return EXPERIMENTS_DIR / 'run_future_work_it121_it130.py'
    return EXPERIMENTS_DIR / 'run_canonical_experiment.py'


def main(argv: list[str] | None = None) -> int:
    argv = list(argv or sys.argv[1:])
    tag = extract_iteration(argv)
    # detect dry-run and light-profile forwarding
    dry_run = any(a == '--dry-run' or a.startswith('--dry-run=') for a in argv)
    light_profile = any(a == '--light-profile' or a.startswith('--light-profile=') for a in argv)

    # If we have a tag and a per-iteration runner, call it with --tags <tag>
    if tag:
        target = choose_script_for_iteration(tag)
        if target.name.startswith('run_future_work_'):
            cmd = [sys.executable, '-u', str(target), '--tags', tag]
            if light_profile:
                cmd.append('--light-profile')
        else:
            # canonical runner: force rerun
            cmd = [sys.executable, '-u', str(target), '--force-rerun']
            if dry_run:
                cmd.append('--dry-run')
            if light_profile:
                cmd.append('--light-profile')
    else:
        # No iteration tag found: default to canonical with force flag
        target = EXPERIMENTS_DIR / 'run_canonical_experiment.py'
        cmd = [sys.executable, '-u', str(target), '--force-rerun']
        if dry_run:
            cmd.append('--dry-run')
        if light_profile:
            cmd.append('--light-profile')

    print(f"Wrapper: invoking {' '.join(shlex.quote(c) for c in cmd)}", flush=True)

    env = os.environ.copy()
    env['PYTHONUTF8'] = '1'
    env['PYTHONIOENCODING'] = 'utf-8'
    env['PYTHONUNBUFFERED'] = '1'

    try:
        p = subprocess.run(cmd, cwd=REPO_ROOT, env=env)
        return p.returncode or 0
    except Exception as e:
        print('Wrapper execution failed:', e, file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
