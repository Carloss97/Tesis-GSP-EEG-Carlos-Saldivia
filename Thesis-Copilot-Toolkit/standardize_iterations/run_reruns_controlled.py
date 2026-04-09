#!/usr/bin/env python3
"""
Runner controlado para ejecutar los reruns listados en `rerun_missing_iterations.ps1`.

Comportamiento:
- Ejecuta cada comando hasta `it130` (inclusive), en orden.
- Omite iteraciones marcadas como explícitas en `EXPLICIT_SKIP` o cuyo recuento de figuras excede
  `SKIP_FIGS_THRESHOLD` (esperado pesado).
- Para cada ejecución exitosa vuelve a correr `standardize_results.py --min N --max N --yes`
  para recoger los artefactos generados.
- Cada ejecución tiene un timeout configurable (`PER_RUN_TIMEOUT_S`). Si excede el timeout,
  el proceso se mata y la iteración se añade a `long_runs_to_resume.json` para retomarla mañana.
- Registra logs en `rerun_logs/` y genera `rerun_execution_summary.json` al final.
"""
import json
import os
import re
import shlex
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
RERUN_PS = SCRIPT_DIR / 'rerun_missing_iterations.ps1'
INDEX = REPO_ROOT / 'Thesis-Copilot-Toolkit' / 'standardized_results' / 'index.json'
LOG_DIR = SCRIPT_DIR / 'rerun_logs'
LOG_DIR.mkdir(exist_ok=True)

# Policy / thresholds
SKIP_FIGS_THRESHOLD = 30  # skip iterations with expected figures >= this
EXPLICIT_SKIP = {'it120'}  # user suggested skip
PER_RUN_TIMEOUT_S = 3600  # 1 hour per iteration before marking for resume
MAX_ITER_NUM = 130

def load_index_summary():
    if not INDEX.exists():
        return {}
    j = json.loads(INDEX.read_text())
    return j.get('summary', {})

def aggregate_by_padded(summary):
    agg = {}
    for tag, v in summary.items():
        padded = v.get('padded')
        if not padded:
            continue
        entry = agg.setdefault(padded, {'figures':0,'tables':0,'raw':False,'stats':False,'significance':False,'qa':False,'run_metadata':False})
        st = v.get('stored',{})
        entry['figures'] += int(st.get('figures_count') or 0)
        entry['tables'] += int(st.get('tables_count') or 0)
        entry['raw'] = entry['raw'] or bool(st.get('raw'))
        entry['stats'] = entry['stats'] or bool(st.get('stats'))
        entry['significance'] = entry['significance'] or bool(st.get('significance'))
        entry['qa'] = entry['qa'] or bool(st.get('qa'))
        entry['run_metadata'] = entry['run_metadata'] or bool(st.get('run_metadata'))
    return agg

def parse_ps_commands(ps_path):
    if not ps_path.exists():
        raise FileNotFoundError(ps_path)
    cmds = []
    for ln in ps_path.read_text(encoding='utf-8').splitlines():
        ln = ln.strip()
        if not ln or ln.startswith('#'):
            continue
        # expect lines like: & 'C:\...\.venv\Scripts\python.exe' experiments\run_... --iteration_tag it004 ...
        m = re.match(r"^&\s*'(?P<py>[^']+)'\s+(?P<rest>.+)$", ln)
        if m:
            py = m.group('py')
            rest = m.group('rest')
            # Redirect canonical runner calls to the wrapper that understands the generated flags
            rest = rest.replace('run_canonical_experiment.py', 'run_iteration_wrapper.py')
            # Find iteration tag
            mm = re.search(r'--iteration_tag\s+(?P<tag>\S+)', rest)
            tag = mm.group('tag') if mm else None
            cmds.append({'raw_line': ln, 'python': py, 'rest': rest, 'iteration_tag': tag})
        else:
            # fallback: try to extract iteration tag only
            mm = re.search(r'--iteration_tag\s+(?P<tag>\S+)', ln)
            tag = mm.group('tag') if mm else None
            cmds.append({'raw_line': ln, 'python': None, 'rest': ln, 'iteration_tag': tag})
    return cmds

def run_command(py, rest, iteration_tag, timeout_s):
    # normalize rest to use forward slashes to avoid shlex treating backslashes as escapes
    rest_fixed = rest.replace('\\', '/')
    args = shlex.split(rest_fixed, posix=True)
    cmd = [py] + args if py else args
    t0 = time.time()
    try:
        env = os.environ.copy()
        env['PYTHONUTF8'] = '1'
        env['PYTHONIOENCODING'] = 'utf-8'
        p = subprocess.run(cmd, cwd=REPO_ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timeout_s)
        elapsed = time.time() - t0
        return {'returncode': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr, 'elapsed': elapsed, 'timed_out': False}
    except subprocess.TimeoutExpired as te:
        # Attempt to terminate child if any
        try:
            te.process and te.process.kill()
        except Exception:
            pass
        elapsed = time.time() - t0
        out = getattr(te, 'output', '') or ''
        err = getattr(te, 'stderr', '') or ''
        return {'returncode': None, 'stdout': out, 'stderr': err, 'elapsed': elapsed, 'timed_out': True}
    except Exception as e:
        elapsed = time.time() - t0
        return {'returncode': -1, 'stdout': '', 'stderr': str(e), 'elapsed': elapsed, 'timed_out': False}

def standardize_iteration(py, num):
    # call standardize_results.py for the single iteration
    script = SCRIPT_DIR / 'standardize_results.py'
    if not script.exists():
        return {'ok': False, 'error': 'standardize_results.py not found'}
    cmd = [py, str(script), '--min', str(num), '--max', str(num), '--yes']
    try:
        p = subprocess.run(cmd, cwd=REPO_ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=300)
        return {'ok': p.returncode == 0, 'returncode': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr}
    except Exception as e:
        return {'ok': False, 'error': str(e)}

def save_json(path, data):
    path.write_text(json.dumps(data, indent=2))

def main():
    summary = load_index_summary()
    agg = aggregate_by_padded(summary)
    cmds = parse_ps_commands(RERUN_PS)

    run_log = []
    skipped = []
    long_runs = []
    failed = []

    for item in cmds:
        tag = item.get('iteration_tag')
        if not tag:
            # cannot determine iteration tag, skip
            run_log.append({'iteration': None, 'status': 'skipped', 'reason': 'no_iteration_tag', 'line': item.get('raw_line')})
            continue
        # normalize padded tag to itNNN
        m = re.match(r'it(\d{1,3})', tag)
        if not m:
            run_log.append({'iteration': tag, 'status': 'skipped', 'reason': 'unexpected_tag_format'})
            continue
        num = int(m.group(1))
        if num > MAX_ITER_NUM:
            run_log.append({'iteration': tag, 'status': 'skipped', 'reason': f'above_max_{MAX_ITER_NUM}'})
            continue

        padded = f'it{num:03d}'
        # decide to skip heavy ones
        info = agg.get(padded, {})
        figs = info.get('figures', 0)
        if padded in EXPLICIT_SKIP or figs >= SKIP_FIGS_THRESHOLD:
            skipped.append({'iteration': padded, 'figures': figs, 'reason': 'explicit_skip' if padded in EXPLICIT_SKIP else 'expected_heavy'})
            run_log.append({'iteration': padded, 'status': 'skipped', 'reason': skipped[-1]['reason'], 'figures': figs})
            continue

        # execute
        print(f"Starting {padded} (figures={figs})...")
        res = run_command(item.get('python'), item.get('rest'), padded, PER_RUN_TIMEOUT_S)
        stdout_path = LOG_DIR / f"{padded}_stdout.log"
        stderr_path = LOG_DIR / f"{padded}_stderr.log"
        stdout_path.write_text(res.get('stdout') or '')
        stderr_path.write_text(res.get('stderr') or '')

        entry = {'iteration': padded, 'command': item.get('raw_line'), 'timed_out': res.get('timed_out'), 'elapsed_s': res.get('elapsed'), 'returncode': res.get('returncode'), 'stdout': str(stdout_path.name), 'stderr': str(stderr_path.name), 'timestamp': datetime.utcnow().isoformat() + 'Z'}

        if res.get('timed_out'):
            long_runs.append({'iteration': padded, 'elapsed_s': res.get('elapsed'), 'reason': 'timeout'})
            entry['status'] = 'timed_out'
            run_log.append(entry)
            # do not attempt standardization
            save_json(SCRIPT_DIR / 'long_runs_to_resume.json', long_runs)
            continue

        if res.get('returncode') != 0:
            entry['status'] = 'failed'
            failed.append(entry)
            run_log.append(entry)
            save_json(SCRIPT_DIR / 'failed_runs.json', failed)
            continue

        # success
        entry['status'] = 'success'
        run_log.append(entry)
        # standardize this iteration
        std = standardize_iteration(item.get('python') or str(Path(sys.executable)), num)
        std_log_path = LOG_DIR / f"{padded}_standardize.log"
        std_log_path.write_text(json.dumps(std, indent=2))

    # save summaries
    save_json(SCRIPT_DIR / 'rerun_execution_summary.json', {'run_log': run_log, 'skipped': skipped, 'long_runs': long_runs, 'failed': failed, 'generated_at': datetime.utcnow().isoformat() + 'Z'})
    if skipped:
        save_json(SCRIPT_DIR / 'skipped_iterations.json', skipped)
    if long_runs:
        save_json(SCRIPT_DIR / 'long_runs_to_resume.json', long_runs)
    if failed:
        save_json(SCRIPT_DIR / 'failed_runs.json', failed)

    print('Runner finished. Logs and summaries in', LOG_DIR)

if __name__ == '__main__':
    main()
