#!/usr/bin/env python3
"""
Generate a runnable experiment runner from a rerun selection CSV.
This creates `experiments/run_reruns_selected.py` which defines IterDef entries
(one per combo) and reuses the base runner in `run_future_work_it121_it130.py`.

Usage:
  python experiments/generate_runner_from_selection.py --selection results/analysis/batches/rerun_selection_lt5.csv

The generated runner will NOT be executed by this script. You can review it
and run it manually when ready.
"""
from pathlib import Path
import pandas as pd
import argparse

ROOT = Path(__file__).resolve().parents[1]
BATCH = ROOT / 'results' / 'analysis' / 'batches'
GEN_OUT = ROOT / 'experiments' / 'run_reruns_selected.py'
BASE_RUN = ROOT / 'experiments' / 'run_future_work_it121_it130.py'

parser = argparse.ArgumentParser()
parser.add_argument('--selection', type=str, default=str(BATCH / 'rerun_selection_lt5.csv'))
args = parser.parse_args()
sel_path = Path(args.selection)
if not sel_path.exists():
    print('Selection CSV not found at', sel_path)
    raise SystemExit(1)

df = pd.read_csv(sel_path)

# Helper to parse graph tag like 'knn__k3' or 'gaussian__sigma1'
def parse_graph_tag(tag: str):
    if '__' in tag:
        parts = tag.split('__')
        g = parts[0]
        params = {}
        rest = '__'.join(parts[1:])
        # attempt parse simple key/value pairs like k3 or sigma1 or k4_sigma1
        for token in rest.split('_'):
            if token.startswith('k') and token[1:].isdigit():
                params['k'] = int(token[1:])
            elif token.startswith('sigma'):
                try:
                    params['sigma'] = float(token.replace('sigma',''))
                except Exception:
                    pass
        return g, params
    return tag, {}

# Build runner content
header = f"""
# Auto-generated runner from selection {sel_path.name}
# Use with caution: this script will call the iteration engine and execute runs.
import importlib.util
from dataclasses import replace
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE_SCRIPT = ROOT / 'experiments' / 'run_future_work_it121_it130.py'

# load base module
spec = importlib.util.spec_from_file_location('run121130', str(BASE_SCRIPT))
mod = importlib.util.module_from_spec(spec)
loader = spec.loader
import sys as _sys
_sys.modules[spec.name] = mod
loader.exec_module(mod)

IterDef = mod.IterDef

_defs = []
"""

body_lines = []
count = 0
for i, row in df.iterrows():
    dataset = row.get('dataset')
    graph = row.get('graph')
    missing_ratio = row.get('missing_ratio')
    method = row.get('best_method') if 'best_method' in row.index else row.get('method')
    key = f"rerun_{i}_{dataset}_{graph}_{method}".replace(' ', '_')
    tag = key
    description = f"Rerun combo: {dataset} {graph} {method} mr={missing_ratio}"
    datasets_list = [dataset]
    # parse graph
    gname, gparams = parse_graph_tag(str(graph))
    graph_specs = [(gname, gparams)]
    methods_list = [method]
    missing_list = [missing_ratio] if pd.notna(missing_ratio) and missing_ratio != '' else [0.2]
    # create an IterDef line
    line = f"_defs.append(IterDef('{key}', '{tag}', '{description}', 'Rerun', 'Auto-generated rerun', {datasets_list}, seeds=list(range(6)), graph_specs={graph_specs}, missing_list={missing_list}, methods={methods_list}))"
    body_lines.append(line)
    count += 1

footer = """
def main():
    keys = [d.key for d in _defs]
    parser = mod.argparse.ArgumentParser(description='Run selected reruns')
    parser.add_argument('--tags', nargs='+', default=keys, choices=keys, help='Subset to run')
    parser.add_argument('--light-profile', action='store_true')
    parser.add_argument('--stop-on-error', action='store_true')
    args = parser.parse_args()

    failed = []
    completed = []
    availability = mod.load_data_availability()['availability']
    data = mod.load_data_availability()['data']

    for k in args.tags:
        it = next((d for d in _defs if d.key == k), None)
        if it is None:
            print('Unknown tag', k)
            continue
        try:
            if args.light_profile:
                it = replace(it, seeds=[0,1])
            mod._run_iteration(it, availability, data, operational_close_profile=False)
            completed.append(k)
            print('[OK]', k)
        except Exception as exc:
            failed.append({'iteration': k, 'error': str(exc)})
            print('[SKIPPED]', k, exc)
            if args.stop_on_error:
                raise

    print('Completed:', completed)
    if failed:
        (mod.RESULTS / 'rerun_selected_skipped.json').write_text(mod.json.dumps(failed, ensure_ascii=False, indent=2), encoding='utf-8')

if __name__ == '__main__':
    main()
"""

content = header + '\n'.join(body_lines) + '\n' + footer
GEN_OUT.write_text(content, encoding='utf-8')
print('Generated runner at', GEN_OUT)
print('Defs written:', count)
print('Review the generated script before running it (it will execute jobs).')
