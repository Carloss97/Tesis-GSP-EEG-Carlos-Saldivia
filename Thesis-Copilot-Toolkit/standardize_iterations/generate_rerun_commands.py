#!/usr/bin/env python3
"""
Genera un script PowerShell con comandos para re-ejecutar iteraciones faltantes.

Lee `Thesis-Copilot-Toolkit/standardized_results/index.json` y crea
`rerun_missing_iterations.ps1` con líneas invocando el runner canónico usando `--engine v9`.

Revisar y ajustar flags según el runner real antes de ejecutar.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / 'standardized_results' / 'index.json'
OUT_PS = Path(__file__).resolve().parent / 'rerun_missing_iterations.ps1'
VENV_PY = Path('c:\\Users\\sarlo\\OneDrive\\Escritorio\\Proyectos\\Tesis-GSP-EEG-Carlos-Saldivia\\.venv\\Scripts\\python.exe')

def load_index():
    if not INDEX.exists():
        raise FileNotFoundError(f"Index not found: {INDEX}")
    return json.loads(INDEX.read_text())['summary']

def has_artifacts_for_padded(summary, padded):
    entries = [v for v in summary.values() if v.get('padded') == padded]
    if not entries:
        return False, {}
    def any_field(field):
        return any((e['stored'].get(field) not in (None, 0) for e in entries))
    raw = any_field('raw')
    stats = any_field('stats')
    sig = any_field('significance')
    qa = any_field('qa')
    runmeta = any_field('run_metadata')
    figs = sum((e['stored'].get('figures_count') or 0) for e in entries)
    tabs = sum((e['stored'].get('tables_count') or 0) for e in entries)
    info = dict(raw=raw, stats=stats, significance=sig, qa=qa, run_metadata=runmeta, figures=figs, tables=tabs)
    # require minimal set: raw, stats, significance, qa, run_metadata, >=9 figures, >=2 tables
    ok = raw and stats and sig and qa and runmeta and figs >= 9 and tabs >= 2
    return ok, info

def main():
    summary = load_index()
    missing = []
    for n in range(1, 131):
        padded = f'it{n:03d}'
        ok, info = has_artifacts_for_padded(summary, padded)
        if not ok:
            missing.append((padded, info))

    if not missing:
        print('Todas las iteraciones 1-130 tienen los artefactos mínimos.')
        return

    lines = []
    lines.append("# Rerun missing iterations (auto-generated). Review flags before running.")
    lines.append("# Requires: adjust seeds/scenarios/dataset as needed. Uses engine v9 by default.")
    for padded, info in missing:
        it_tag = padded.replace('it0', 'it') if padded.startswith('it0') and len(padded) <=4 else padded
        # Keep original simple tag like it01 if exists in summary; otherwise use padded
        # Build a recommended command
        cmd = f"& '{VENV_PY}' experiments\\run_canonical_experiment.py --engine v9 --dataset all --scenarios all --seeds 0-24 --iteration_tag {padded} --objective \"Re-run missing artifacts standardization\""
        comment = f"# {padded}: missing -> raw={info['raw']} stats={info['stats']} sig={info['significance']} qa={info['qa']} runmeta={info['run_metadata']} figs={info['figures']} tabs={info['tables']}"
        lines.append(comment)
        lines.append(cmd)
        lines.append('')

    OUT_PS.write_text('\n'.join(lines))
    print(f'Generator wrote {OUT_PS} with {len(missing)} iterations to rerun.')

if __name__ == '__main__':
    main()
