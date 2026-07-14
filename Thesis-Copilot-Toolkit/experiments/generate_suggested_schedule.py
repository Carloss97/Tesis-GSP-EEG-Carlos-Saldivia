#!/usr/bin/env python3
"""
Analyze canonical schedule, clean descriptions, and produce suggested schedules.

Outputs:
 - experiments/schedules/it01-it50_schedule_final_canonical_cleaned.json
 - experiments/schedules/it01-it50_schedule_suggested_compact.json
 - experiments/schedules/it01-it50_schedule_suggested_expanded.json
 - experiments/schedules/analysis_report.json

Run:
  python Thesis-Copilot-Toolkit/experiments/generate_suggested_schedule.py
"""
import json
import os
from collections import defaultdict
from datetime import datetime


def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save(obj, path):
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def clean_text(s, remove_terms):
    if not isinstance(s, str):
        return s
    out = s
    for t in remove_terms:
        out = out.replace(t, '').replace('  ', ' ')
    return out.strip()


def choose_graphs_for_dataset(dataset):
    # heuristic: iris is small, skip heavy graphs
    if dataset == 'iris':
        return ['knn', 'knng']
    return ['knn', 'knng', 'kaliofolias', 'nnk']


def params_for_graph(graph):
    if graph == 'knn':
        return [{'k': 3}, {'k': 5}]
    if graph == 'knng':
        return [{'sigma': 1.0, 'k': 5}, {'sigma': 2.0, 'k': 7}]
    if graph == 'nnk':
        return [{'k': 3}, {'k': 5}]
    return [{}]


def build_iteration_template(base, new_key, dataset, variant, graph_spec, methods, idx):
    it = dict(base)  # shallow copy
    # replace identifying fields
    it['key'] = new_key
    it['tag'] = new_key
    it['description'] = f"Auto-suggested {new_key} — dataset={dataset}{('/'+variant) if variant else ''} graph={graph_spec[0]}"
    it['datasets'] = [dataset]
    if variant:
        it['dataset_variant'] = variant
    it['graph_specs'] = [graph_spec]
    it['methods'] = methods
    return it


def main():
    schedule_path = 'Thesis-Copilot-Toolkit/experiments/schedules/it01-it50_schedule_final_canonical.json'
    registry_path = 'Thesis-Copilot-Toolkit/experiments/canonical_registry.json'

    schedule = load(schedule_path)
    registry = load(registry_path)

    iterations = schedule.get('iterations', [])

    # collect defaults from first iteration
    defaults = {}
    if iterations:
        first = iterations[0]
        for k in ('missing_list', 'seeds', 'lambdas', 'snr_levels'):
            if k in first:
                defaults[k] = first[k]

    # detect dataset variants
    datasets = []
    seen = set()
    for it in iterations:
        ds = it.get('datasets', [])
        if not ds:
            continue
        d = ds[0]
        variant = it.get('dataset_variant')
        key = (d, variant)
        if key not in seen:
            seen.add(key)
            datasets.append({'dataset': d, 'variant': variant})

    # analyze graph & method usage
    graph_counts = defaultdict(int)
    method_counts = defaultdict(int)
    for it in iterations:
        for g in it.get('graph_specs', []):
            if isinstance(g, list) and g:
                graph_counts[g[0]] += 1
        for m in it.get('methods', []):
            method_counts[m] += 1

    # terms to remove from free-text descriptions
    remove_terms = ['graph_time_tikhonov', 'gsp', 'gsmooth']

    # Clean descriptions/objectives in canonical schedule
    cleaned = dict(schedule)
    cleaned['generated'] = datetime.utcnow().isoformat() + 'Z'
    for it in cleaned.get('iterations', []):
        it['description'] = clean_text(it.get('description', ''), remove_terms)
        it['objective'] = clean_text(it.get('objective', ''), remove_terms)

    cleaned_path = 'Thesis-Copilot-Toolkit/experiments/schedules/it01-it50_schedule_final_canonical_cleaned.json'
    save(cleaned, cleaned_path)

    # Build suggested schedules
    # method sets
    baselines = registry.get('baselines', [])
    instant_methods = list(dict.fromkeys(baselines + ['tikhonov', 'rbfi_tps']))
    tv_methods = registry.get('methods_tv', [])

    compact_iters = []
    expanded_iters = []

    base_template = {
        'fase': 'auto',
        'mode': 'base',
        'missing_list': defaults.get('missing_list', [0.1, 0.2, 0.3]),
        'seeds': defaults.get('seeds', [0,1,2]),
        'lambdas': defaults.get('lambdas', [0.05, 0.1, 0.2, 0.4]),
        'snr_levels': defaults.get('snr_levels', [20.0, 10.0, 5.0, 0.0])
    }

    idx = 1
    # Compact: for each dataset variant try 3 graphs x 2 params, alternate between instant/tv
    for d in datasets:
        ds_name = d['dataset']
        variant = d['variant']
        graphs = choose_graphs_for_dataset(ds_name)[:3]
        for gi, g in enumerate(graphs):
            params_list = params_for_graph(g)
            for pj, params in enumerate(params_list):
                methods = instant_methods if ((gi + pj) % 2 == 0) else tv_methods
                key = f"itS{idx:03d}"
                graph_spec = [g, params]
                it = build_iteration_template(base_template, key, ds_name, variant, graph_spec, methods, idx)
                compact_iters.append(it)
                idx += 1

    # Expanded: exhaustively combine recommended graphs x params x both method sets
    idx = 1
    for d in datasets:
        ds_name = d['dataset']
        variant = d['variant']
        graphs = choose_graphs_for_dataset(ds_name)
        for g in graphs:
            params_list = params_for_graph(g)
            for params in params_list:
                for methods in (instant_methods, tv_methods):
                    key = f"itE{idx:03d}"
                    graph_spec = [g, params]
                    it = build_iteration_template(base_template, key, ds_name, variant, graph_spec, methods, idx)
                    expanded_iters.append(it)
                    idx += 1

    compact_schedule = {'generated': datetime.utcnow().isoformat() + 'Z', 'iterations': compact_iters}
    expanded_schedule = {'generated': datetime.utcnow().isoformat() + 'Z', 'iterations': expanded_iters}

    compact_path = f'Thesis-Copilot-Toolkit/experiments/schedules/it01-it{len(compact_iters):02d}_schedule_suggested_compact.json'
    expanded_path = f'Thesis-Copilot-Toolkit/experiments/schedules/it01-it{len(expanded_iters):03d}_schedule_suggested_expanded.json'

    save(compact_schedule, compact_path)
    save(expanded_schedule, expanded_path)

    report = {
        'generated': datetime.utcnow().isoformat() + 'Z',
        'dataset_variants': datasets,
        'original_iterations': len(iterations),
        'compact_iterations': len(compact_iters),
        'expanded_iterations': len(expanded_iters),
        'graph_counts': dict(graph_counts),
        'method_counts': dict(method_counts),
        'cleaned_schedule': cleaned_path,
        'compact_schedule': compact_path,
        'expanded_schedule': expanded_path,
        'notes': [
            'Compact schedule tries a smaller, alternating coverage per dataset.',
            'Expanded schedule exhaustively combines chosen graphs, parameter sweeps, and both method families.',
            'Recommendation: run compact first as pilot, then run expanded for full coverage if resources allow.'
        ]
    }

    report_path = 'Thesis-Copilot-Toolkit/experiments/schedules/analysis_report.json'
    save(report, report_path)

    print('Analysis complete.')
    print('Cleaned canonical schedule:', cleaned_path)
    print('Compact suggested schedule:', compact_path)
    print('Expanded suggested schedule:', expanded_path)
    print('Report:', report_path)


if __name__ == '__main__':
    main()
