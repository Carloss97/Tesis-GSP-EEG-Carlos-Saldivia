#!/usr/bin/env python3
"""
Retry failed iterations listed in rerun_execution_summary.json.
Runs each failed command by invoking the extracted python executable directly
(to avoid PowerShell quoting issues), sets a per-iteration timeout, and
writes a `retry_execution_summary.json` with results.
"""
import os
import json
import re
import shlex
import subprocess
import time
from datetime import datetime

HERE = os.path.abspath(os.path.dirname(__file__))
REPO_ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
# Commands in the rerun list are relative to the Thesis-Copilot-Toolkit folder
WORK_DIR = os.path.join(REPO_ROOT, 'Thesis-Copilot-Toolkit')
SUMMARY_IN = os.path.join(HERE, 'rerun_execution_summary.json')
SUMMARY_OUT = os.path.join(HERE, 'retry_execution_summary.json')
LOG_DIR = os.path.join(HERE, 'rerun_logs')
os.makedirs(LOG_DIR, exist_ok=True)

PER_ITER_TIMEOUT = 7200  # seconds (2 hours)

def load_summary():
    if not os.path.exists(SUMMARY_IN):
        return {'failed': []}
    with open(SUMMARY_IN, 'r', encoding='utf-8') as f:
        return json.load(f)

def parse_command(cmd_str):
    # Expect PowerShell style: & 'C:\path\to\python.exe' rest...
    m = re.match(r"\s*&\s*'([^']+)'\s*(.*)", cmd_str)
    if m:
        python_path = m.group(1)
        rest = m.group(2)
    else:
        # Fallback: try to split the command - assume first token is the python exe
        parts = cmd_str.strip().split()
        python_path = parts[0] if parts else None
        rest = ' '.join(parts[1:]) if len(parts) > 1 else ''
    # Normalize backslashes to forward slashes to make shlex parsing safe
    rest = rest.replace('\\', '/')
    args = shlex.split(rest, posix=True)
    return python_path, args


def make_abs_script_path(arg0):
    if os.path.isabs(arg0):
        return arg0
    # First try relative to the Thesis-Copilot-Toolkit folder
    candidate = os.path.join(WORK_DIR, arg0)
    if os.path.exists(candidate):
        return candidate
    # Then try repo root
    candidate2 = os.path.join(REPO_ROOT, arg0)
    if os.path.exists(candidate2):
        return candidate2
    # Fallback: return the candidate under WORK_DIR (may not exist)
    return candidate


def run_one(iteration, cmd_str):
    python_path, args = parse_command(cmd_str)
    if not python_path:
        python_path = os.path.join(REPO_ROOT, '.venv', 'Scripts', 'python.exe')
    # Always call the wrapper which adapts the generated flags to the
    # appropriate per-iteration runner and enforces UTF-8.
    wrapper_rel = os.path.join('Thesis-Copilot-Toolkit', 'standardize_iterations', 'run_iteration_wrapper.py')
    abs_wrapper = make_abs_script_path(wrapper_rel)
    cmd = [python_path, abs_wrapper, '--iteration_tag', iteration]

    stdout_path = os.path.join(LOG_DIR, f"{iteration}_retry_stdout.log")
    stderr_path = os.path.join(LOG_DIR, f"{iteration}_retry_stderr.log")

    start = time.time()
    try:
        env = os.environ.copy()
        env['PYTHONUTF8'] = '1'
        env['PYTHONIOENCODING'] = 'utf-8'
        with open(stdout_path, 'wb') as out, open(stderr_path, 'wb') as err:
            proc = subprocess.run(cmd, cwd=WORK_DIR, env=env, stdout=out, stderr=err, timeout=PER_ITER_TIMEOUT)
        elapsed = time.time() - start
        return {'iteration': iteration, 'status': 'ok' if proc.returncode == 0 else 'failed', 'returncode': proc.returncode, 'elapsed_s': elapsed, 'stdout': stdout_path, 'stderr': stderr_path}
    except subprocess.TimeoutExpired:
        return {'iteration': iteration, 'status': 'timed_out', 'timeout_s': PER_ITER_TIMEOUT, 'stdout': stdout_path, 'stderr': stderr_path}
    except Exception as e:
        # Log exception
        try:
            with open(stderr_path, 'a', encoding='utf-8') as ef:
                ef.write('Exception: ' + str(e) + '\n')
        except Exception:
            pass
        return {'iteration': iteration, 'status': 'failed', 'error': str(e), 'stdout': stdout_path, 'stderr': stderr_path}


def main():
    in_summary = load_summary()
    failed = in_summary.get('failed', [])
    if not failed:
        print('No failed iterations to retry.')
        return

    results = {'started_at': datetime.utcnow().isoformat() + 'Z', 'succeeded': [], 'failed': [], 'timed_out': []}

    for entry in failed:
        iteration = entry.get('iteration')
        cmd_str = entry.get('command')
        print(f"Retrying {iteration}...")
        r = run_one(iteration, cmd_str)
        if r['status'] == 'ok':
            results['succeeded'].append(r)
        elif r['status'] == 'timed_out':
            results['timed_out'].append(r)
        else:
            results['failed'].append(r)
        # small delay between runs
        time.sleep(1)

    results['finished_at'] = datetime.utcnow().isoformat() + 'Z'
    with open(SUMMARY_OUT, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

    # If any succeeded, run the standardizer once to pick up new artifacts
    if results['succeeded']:
        try:
            std_py = os.path.join(REPO_ROOT, '.venv', 'Scripts', 'python.exe')
            std_script = os.path.join(REPO_ROOT, 'Thesis-Copilot-Toolkit', 'standardize_iterations', 'standardize_results.py')
            print('Updating standardized index...')
            subprocess.run([std_py, std_script], cwd=REPO_ROOT)
        except Exception as e:
            print('Standardizer run failed:', e)

    print('Retry run complete. Summary at', SUMMARY_OUT)

if __name__ == '__main__':
    main()
