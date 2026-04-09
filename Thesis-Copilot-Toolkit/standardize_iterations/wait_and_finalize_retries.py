#!/usr/bin/env python3
"""Monitor de reintentos: espera que las ejecuciones 'full' terminen y lanza el estandarizador.

Lee `failed_to_retry.json` para obtener la lista de iteraciones pendientes (o acepta lista por args).
Comprueba periódicamente `rerun_logs/<it>_full_stdout.log` buscando indicadores de éxito
('Completed:' o '[done] Resultados en') o fallos ('Traceback' en stderr). Al terminar, ejecuta
`standardize_results.py` y escribe `final_retry_finalize_summary.json` con los resultados.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from datetime import datetime
import subprocess
import os


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
LOG_DIR = HERE / 'rerun_logs'
FAILED_FILE = HERE / 'failed_to_retry.json'
SUMMARY_OUT = HERE / 'final_retry_finalize_summary.json'

CHECK_INTERVAL = int(os.environ.get('WAIT_CHECK_INTERVAL', '10'))  # seconds
MAX_WAIT = int(os.environ.get('WAIT_MAX_SECONDS', str(6 * 3600)))  # default 6 hours


def load_iterations() -> list[str]:
    if FAILED_FILE.exists():
        with open(FAILED_FILE, 'r', encoding='utf-8') as f:
            j = json.load(f)
            return j.get('failed_iterations', [])
    return []


def read_file_safe(p: Path) -> str:
    try:
        if not p.exists():
            return ''
        return p.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return ''


def check_iteration_done(it: str) -> tuple[bool, str]:
    """Returns (done_flag, status). status in {'succeeded','failed','running','unknown'}"""
    out = LOG_DIR / f"{it}_full_stdout.log"
    err = LOG_DIR / f"{it}_full_stderr.log"
    sout = read_file_safe(out)
    serr = read_file_safe(err)

    # success indicators
    if 'Completed:' in sout or '[done] Resultados en' in sout or 'Resultados en:' in sout:
        return True, 'succeeded'
    # fatal Python errors
    if 'Traceback' in serr or 'Exception:' in serr or 'Error' in serr:
        return True, 'failed'
    # still running
    if sout or serr:
        return False, 'running'
    return False, 'unknown'


def run_standardizer():
    py = REPO_ROOT / '.venv' / 'Scripts' / 'python.exe'
    script = REPO_ROOT / 'Thesis-Copilot-Toolkit' / 'standardize_iterations' / 'standardize_results.py'
    print('Running standardizer:', py, script)
    try:
        subprocess.run([str(py), str(script)], cwd=REPO_ROOT)
    except Exception as e:
        print('Standardizer failed:', e)


def main():
    iterations = load_iterations()
    if not iterations:
        print('No iterations found in', FAILED_FILE)
        sys.exit(0)

    print(f"Monitoring {len(iterations)} iterations: {iterations}")
    start = time.time()
    status_map: dict[str, str] = {it: 'pending' for it in iterations}

    while True:
        all_done = True
        for it in iterations:
            if status_map.get(it) in ('succeeded', 'failed'):
                continue
            done, st = check_iteration_done(it)
            if done:
                status_map[it] = st
                print(f"{it} -> {st}")
            else:
                all_done = False
                status_map[it] = st

        if all_done:
            break

        if time.time() - start > MAX_WAIT:
            print('Max wait exceeded, exiting monitor loop')
            break

        time.sleep(CHECK_INTERVAL)

    # write summary
    summary = {
        'monitored_at': datetime.utcnow().isoformat() + 'Z',
        'results': status_map,
    }
    with open(SUMMARY_OUT, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    # run standardizer for recovered iterations
    if any(v == 'succeeded' for v in status_map.values()):
        run_standardizer()

    print('Monitor finished. Summary at', SUMMARY_OUT)


if __name__ == '__main__':
    main()
