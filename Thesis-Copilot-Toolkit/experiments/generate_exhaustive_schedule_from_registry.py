#!/usr/bin/env python3
"""
Generate an exhaustive schedule from the canonical registry.

Produces:
 - Thesis-Copilot-Toolkit/experiments/schedules/it_exhaustive_from_registry.json
 - Thesis-Copilot-Toolkit/experiments/schedules/it_exhaustive_analysis.json

Usage:
  python Thesis-Copilot-Toolkit/experiments/generate_exhaustive_schedule_from_registry.py
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


def expand_method_names(methods, mappings, remove_methods):
    out = []
    for m in methods:
        if m in remove_methods:
            continue
        mapped = mappings.get(m, m)
        if mapped not in out:
            out.append(mapped)
    return out


def build_param_space():
    return {
        'knn': [{'k': 3}, {'k': 5}, {'k': 7}, {'k': 9}],
        'knng': [
            {'k': 3, 'sigma': 0.5},
            {'k': 3, 'sigma': 1.0},
            {'k': 5, 'sigma': 1.0},
            {'k': 7, 'sigma': 2.0}
        ],
        'vknng': [
            {'k': 5, 'sigma': 1.0, 'alpha': 0.5},
            {'k': 5, 'sigma': 2.0, 'alpha': 1.0},
            {'k': 7, 'sigma': 1.0, 'alpha': 0.5}
        ],
        'nnk': [{'k': 3}, {'k': 5}],
        'aew': [{'alpha': 0.1}, {'alpha': 0.5}],
        'kalofolias': [{'alpha': 0.1}, {'alpha': 1.0}],
        # Legacy alias support
        'kaliofolias': [{'alpha': 0.1}, {'alpha': 1.0}],
        'e-nn': [{'radius': 0.5}, {'radius': 1.0}],
        'visibility_nnk': [{'k': 3, 'visibility_threshold': 0.5}, {'k': 5, 'visibility_threshold': 0.8}]
    }


def scenario_groups():
    # Balanced groups: percentage-based and few-electrode, each with random/nearby variants
    percent_random = [f"{p}pct_random" for p in (10, 20, 30, 40)]
    percent_nearby = [f"{p}pct_nearby" for p in (10, 20, 30, 40)]
    few_random = [f"{n}ch_random" for n in (1, 2, 3)]
    few_nearby = [f"{n}ch_nearby" for n in (1, 2, 3)]

    return {
        'percent_random': {'labels': percent_random, 'missing_list': [0.10, 0.20, 0.30, 0.40], 'mode': 'random'},
        'percent_nearby': {'labels': percent_nearby, 'missing_list': [0.10, 0.20, 0.30, 0.40], 'mode': 'nearby'},
        'few_random': {'labels': few_random, 'missing_counts': [1, 2, 3], 'mode': 'random'},
        'few_nearby': {'labels': few_nearby, 'missing_counts': [1, 2, 3], 'mode': 'nearby'},
    }


def main():
    registry_path = 'Thesis-Copilot-Toolkit/experiments/canonical_registry.json'
    analysis_path = 'Thesis-Copilot-Toolkit/experiments/schedules/analysis_report.json'
    out_schedule = 'Thesis-Copilot-Toolkit/experiments/schedules/it_exhaustive_from_registry.json'
    out_report = 'Thesis-Copilot-Toolkit/experiments/schedules/it_exhaustive_analysis.json'

    registry = load(registry_path)
    mappings = registry.get('mappings', {})
    remove_methods = set(registry.get('remove_methods', []))

    # determine dataset variants from analysis report if available, else use registry datasets
    dataset_variants = []
    if os.path.exists(analysis_path):
        ar = load(analysis_path)
        for d in ar.get('dataset_variants', []):
            dataset_variants.append((d.get('dataset'), d.get('variant')))
    if not dataset_variants:
        for d in registry.get('datasets', []):
            dataset_variants.append((d, None))

    # method families
    methods_instant = expand_method_names(registry.get('methods_instantaneous', []), mappings, remove_methods)
    methods_tv = expand_method_names(registry.get('methods_tv', []), mappings, remove_methods)
    baselines = expand_method_names(registry.get('baselines', []), mappings, remove_methods)

    # parameter grid per graph
    param_space = build_param_space()

    # core defaults
    defaults = {
        'missing_list': [0.1, 0.2, 0.3],
        'seeds': [0, 1, 2],
        'lambdas': [0.05, 0.1, 0.2, 0.4],
        'snr_levels': [20.0, 10.0, 5.0, 0.0]
    }

    iterations = []
    graph_counts = defaultdict(int)
    method_counts = defaultdict(int)
    idx = 1

    for (dataset, variant) in dataset_variants:
        for graph in registry.get('graph_constructors', []):
            graph = mappings.get(graph, graph)
            if graph == 'kaliofolias':
                graph = 'kalofolias'
            params_list = param_space.get(graph, [{}])
            groups = scenario_groups()
            for params in params_list:
                for gname, ginfo in groups.items():
                    scenarios = ginfo.get('labels', [])
                    missing_list_grp = ginfo.get('missing_list')
                    missing_counts_grp = ginfo.get('missing_counts')
                    missing_mode = ginfo.get('mode', 'random')

                    # visibility_nnk: TV-only, otherwise produce instant + TV
                    if graph == 'visibility_nnk':
                        methods = list(dict.fromkeys(methods_tv))
                        key = f"itX{idx:04d}"
                        it = {
                            'key': key,
                            'tag': key,
                            'description': f"Exhaustive {key} — dataset={dataset}{('/'+variant) if variant else ''} graph={graph} params={params} ({gname}, TV methods)",
                            'fase': 'auto',
                            'objective': 'Exhaustive coverage (TV methods only for visibility graph).',
                            'datasets': [dataset],
                            'dataset_variant': variant if variant else None,
                            'mode': 'base',
                            'scenarios': scenarios,
                            'missing_mode': missing_mode,
                            'seeds': defaults['seeds'],
                            'graph_specs': [[graph, params]],
                            'lambdas': defaults['lambdas'],
                            'snr_levels': defaults['snr_levels'],
                            'methods': methods
                        }
                        if missing_list_grp:
                            it['missing_list'] = missing_list_grp
                        if missing_counts_grp:
                            it['missing_counts'] = missing_counts_grp
                        iterations.append(it)
                        graph_counts[graph] += 1
                        for m in methods:
                            method_counts[m] += 1
                        idx += 1
                        continue

                    # Instant iteration
                    inst_methods = list(dict.fromkeys(baselines + methods_instant))
                    key = f"itX{idx:04d}"
                    it_inst = {
                        'key': key,
                        'tag': key,
                        'description': f"Exhaustive {key} — dataset={dataset}{('/'+variant) if variant else ''} graph={graph} params={params} ({gname}, instant methods)",
                        'fase': 'auto',
                        'objective': 'Exhaustive coverage (instantaneous methods).',
                        'datasets': [dataset],
                        'dataset_variant': variant if variant else None,
                        'mode': 'base',
                        'scenarios': scenarios,
                        'missing_mode': missing_mode,
                        'seeds': defaults['seeds'],
                        'graph_specs': [[graph, params]],
                        'lambdas': defaults['lambdas'],
                        'snr_levels': defaults['snr_levels'],
                        'methods': inst_methods
                    }
                    if missing_list_grp:
                        it_inst['missing_list'] = missing_list_grp
                    if missing_counts_grp:
                        it_inst['missing_counts'] = missing_counts_grp
                    iterations.append(it_inst)
                    graph_counts[graph] += 1
                    for m in inst_methods:
                        method_counts[m] += 1
                    idx += 1

                    # TV iteration
                    tv_methods_list = list(dict.fromkeys(methods_tv))
                    key = f"itX{idx:04d}"
                    it_tv = {
                        'key': key,
                        'tag': key,
                        'description': f"Exhaustive {key} — dataset={dataset}{('/'+variant) if variant else ''} graph={graph} params={params} ({gname}, TV methods)",
                        'fase': 'auto',
                        'objective': 'Exhaustive coverage (TV methods).',
                        'datasets': [dataset],
                        'dataset_variant': variant if variant else None,
                        'mode': 'base',
                        'scenarios': scenarios,
                        'missing_mode': missing_mode,
                        'seeds': defaults['seeds'],
                        'graph_specs': [[graph, params]],
                        'lambdas': defaults['lambdas'],
                        'snr_levels': defaults['snr_levels'],
                        'methods': tv_methods_list
                    }
                    if missing_list_grp:
                        it_tv['missing_list'] = missing_list_grp
                    if missing_counts_grp:
                        it_tv['missing_counts'] = missing_counts_grp
                    iterations.append(it_tv)
                    graph_counts[graph] += 1
                    for m in tv_methods_list:
                        method_counts[m] += 1
                    idx += 1

    schedule = {'generated': datetime.utcnow().isoformat() + 'Z', 'iterations': iterations}
    save(schedule, out_schedule)

    report = {
        'generated': datetime.utcnow().isoformat() + 'Z',
        'num_iterations': len(iterations),
        'graph_counts': dict(graph_counts),
        'method_counts': dict(method_counts),
        'out_schedule': out_schedule
    }
    save(report, out_report)

    print('Exhaustive schedule generated:', out_schedule)
    print('Analysis saved to:', out_report)


if __name__ == '__main__':
    main()
