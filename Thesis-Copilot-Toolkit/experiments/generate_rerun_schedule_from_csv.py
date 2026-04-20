#!/usr/bin/env python3
"""Generate a pilot rerun schedule JSON from rerun selection CSV.

Usage:
  python experiments/generate_rerun_schedule_from_csv.py --mode lt5 --out experiments/schedules/it01-it50_rerun_missing_nonbaseline_lt5.json --limit 0

Defaults: mode=lt5 -> uses `results/analysis/batches/rerun_selection_lt5.csv`
"""
from pathlib import Path
import json
import argparse
import pandas as pd
import re
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
BATCH = ROOT / 'results' / 'analysis' / 'batches'
SCHED_DIR = ROOT / 'experiments' / 'schedules'

def parse_graph_token(token: str):
    # token examples: 'k3', 'sigma1', 'sigma1.0', 'k4', 'alpha1'
    m = re.match(r'^k(\d+)$', token)
    if m:
        return {'k': int(m.group(1))}
    m = re.match(r'^sigma(?:_corr)?([0-9]+(?:\.[0-9]+)?)$', token)
    if m:
        return {'sigma': float(m.group(1))}
    m = re.match(r'^alpha([0-9]+(?:\.[0-9]+)?)$', token)
    if m:
        return {'alpha': float(m.group(1))}
    # fallback: try to extract any float in token
    m = re.search(r'([0-9]+(?:\.[0-9]+)?)', token)
    if m:
        try:
            return {token.split('_')[0]: float(m.group(1))}
        except Exception:
            return {token: True}
    return {token: True}

def parse_graph_spec(graph: str):
    parts = graph.split('__') if isinstance(graph, str) else [graph]
    method = parts[0]
    params = {}
    for token in parts[1:]:
        p = parse_graph_token(token)
        params.update(p)
    return [method, params]

def make_tag(dataset: str, graph: str, miss: float, method: str, idx: int):
    gsan = graph.replace('__', '_').replace(' ', '_')
    dsan = dataset.replace(' ', '_')
    msan = method.replace(' ', '_')
    mr = str(miss).replace('.', '_')
    return f"rr{idx:03d}_{dsan}_{gsan}_{mr}_{msan}"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['lt5','lt20','all'], default='lt5')
    parser.add_argument('--out', type=Path, default=SCHED_DIR / 'it01-it50_rerun_missing_nonbaseline_lt5.json')
    parser.add_argument('--limit', type=int, default=0, help='Limit number of iterations (0 = all)')
    parser.add_argument('--seeds', type=int, default=5, help='Number of seeds per iteration (0 = default schedule seeds)')
    args = parser.parse_args()

    src = BATCH / (f'rerun_selection_lt5.csv' if args.mode == 'lt5' else f'rerun_selection_lt20.csv' if args.mode == 'lt20' else 'rerun_candidates_target200.csv')
    if not src.exists():
        raise SystemExit(f"Source CSV not found: {src}")

    df = pd.read_csv(src)
    if args.limit > 0:
        df = df.head(args.limit)

    iterations = []
    for i, row in enumerate(df.itertuples(index=False), start=1):
        dataset = str(row.dataset)
        graph = str(row.graph)
        miss = float(row.missing_ratio)
        best = str(row.best_method)

        key = f"rr{i:03d}"
        tag = make_tag(dataset, graph, miss, best, i)
        graph_spec = parse_graph_spec(graph)
        seeds = list(range(args.seeds)) if args.seeds > 0 else [0,1,2,3,4,5]

        it = {
            'key': key,
            'tag': tag,
            'description': 'Rerun missing non-baseline coverage',
            'fase': 'rerun',
            'objective': f'Add runs for method {best} at combo {dataset}|{graph}|{miss}',
            'datasets': [dataset],
            'mode': 'base',
            'missing_list': [miss],
            'seeds': seeds,
            'graph_specs': [graph_spec],
            'lambdas': [],
            'snr_levels': [],
            'methods': [best],
        }
        iterations.append(it)

    out = {'generated': datetime.utcnow().isoformat() + 'Z', 'iterations': iterations}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Wrote schedule:', args.out)
    print('Iterations:', len(iterations))

if __name__ == '__main__':
    main()
