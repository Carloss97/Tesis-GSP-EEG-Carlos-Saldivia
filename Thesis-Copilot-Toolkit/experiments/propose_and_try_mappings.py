#!/usr/bin/env python3
"""
Propose mappings for missing reruns and optionally test-run mapped iterations.
Usage:
  python experiments/propose_and_try_mappings.py --max-test 20 --light --force-synthetic
"""
from pathlib import Path
import importlib.util
import sys
import json
import re
import difflib
import argparse
from dataclasses import replace

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / 'experiments' / 'run_reruns_selected.py'
RESULTS = ROOT / 'results'
MAPPING_JSON = ROOT / 'experiments' / 'rerun_mapping_lt20.json'
MAPPING_CSV = ROOT / 'experiments' / 'rerun_mapping_lt20.csv'


def load_runner(path: Path):
    spec = importlib.util.spec_from_file_location('runner_mod', str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def normalize(s: str) -> str:
    return re.sub(r'[^0-9a-z]', '', str(s).lower())


def tokens(s: str):
    return [t for t in re.split(r'[^0-9a-z]+', str(s).lower()) if len(t) > 2]


def special_map(ds_name: str, availability_keys: list, availability: dict, force_synthetic: bool):
    n = ds_name.lower()
    # bci proxies -> all available bci_iv2a_real_*
    if 'bci' in n or 'competition' in n:
        cand = [k for k in availability_keys if k.startswith('bci_iv2a_real') and availability.get(k, {}).get('ok')]
        if cand:
            return cand
    if 'physionet' in n or 'eegmmidb' in n:
        if 'physionet_real' in availability_keys and availability.get('physionet_real', {}).get('ok'):
            return ['physionet_real']
    if 'iv100' in n or '100hz' in n:
        if 'iv100hz_mat' in availability_keys and availability.get('iv100hz_mat', {}).get('ok'):
            return ['iv100hz_mat']
    if 'iris' in n:
        if 'iris_graph_signal' in availability_keys and availability.get('iris_graph_signal', {}).get('ok'):
            return ['iris_graph_signal']
    if 'movielens' in n or 'movielens_graph' in n:
        if 'movielens_graph_signal' in availability_keys and availability.get('movielens_graph_signal', {}).get('ok'):
            return ['movielens_graph_signal']
    if 'mne_sample' in n:
        # prefer physionet_real for EEG proxies
        if 'physionet_real' in availability_keys and availability.get('physionet_real', {}).get('ok'):
            return ['physionet_real']
        # else fallback to first bci
        cand = [k for k in availability_keys if k.startswith('bci_iv2a_real') and availability.get(k, {}).get('ok')]
        if cand:
            return cand
    if 'synthetic' in n and force_synthetic:
        # as last resort map synthetic -> physionet_real if available
        if 'physionet_real' in availability_keys and availability.get('physionet_real', {}).get('ok'):
            return ['physionet_real']
    return []


def rank_candidates(ds_name: str, availability_keys: list, availability: dict):
    cand = []
    dn = normalize(ds_name)
    d_tokens = set(tokens(ds_name))
    for k in availability_keys:
        if not availability.get(k, {}).get('ok'):
            continue
        kn = normalize(k)
        k_tokens = set(tokens(k))

        if dn == kn:
            score = 1.0
        elif dn in kn or kn in dn:
            score = 0.9
        else:
            overlap = 0.0
            if d_tokens and k_tokens:
                overlap = len(d_tokens & k_tokens) / max(1, len(d_tokens | k_tokens))
            ratio = difflib.SequenceMatcher(None, ds_name.lower(), k.lower()).ratio()
            score = max(0.2 + 0.6 * overlap, ratio * 0.8)
        cand.append((k, score))
    cand.sort(key=lambda x: x[1], reverse=True)
    return cand


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-test', type=int, default=20, help='Max number of mapped iterations to test-run')
    parser.add_argument('--light', action='store_true', help='Run mapped iterations in light mode (reduced seeds)')
    parser.add_argument('--force-synthetic', action='store_true', help='Allow mapping synthetic datasets to real as last resort')
    parser.add_argument('--run-all-mapped', action='store_true', help='Attempt to run all mapped iterations (can be long)')
    args = parser.parse_args()

    mod = load_runner(RUNNER)
    defs = getattr(mod, '_defs', [])
    base_mod = getattr(mod, 'mod', None)
    if base_mod is None:
        print('Base module (mod) not found in runner; aborting')
        sys.exit(1)

    check = base_mod.load_data_availability()
    availability = check['availability']
    data = check['data']
    availability_keys = [k for k, v in availability.items() if v.get('ok')]

    # determine missing
    missing_defs = [d for d in defs if not (RESULTS / f"{d.key}_raw.csv").exists()]
    print(f"Total defs: {len(defs)}, missing: {len(missing_defs)}")

    mapping = {'availability_keys': availability_keys, 'mappings': {}, 'per_iteration': {}}

    for it in missing_defs:
        proposed = []
        for ds in it.datasets:
            # special heuristics
            s = special_map(ds, availability_keys, availability, args.force_synthetic)
            if s:
                # high confidence
                for x in s:
                    proposed.append((ds, x, 0.95))
                continue

            cand = rank_candidates(ds, availability_keys, availability)
            for k, score in cand:
                if score >= 0.5:
                    proposed.append((ds, k, round(float(score), 3)))
                else:
                    # keep low-scoring candidates for completeness but mark low
                    pass

        # dedupe preserving order per dataset
        proposed_keys = []
        for ds, k, sc in proposed:
            if k not in proposed_keys:
                proposed_keys.append(k)
        mapping['per_iteration'][it.key] = {
            'requested': it.datasets,
            'proposed': proposed_keys,
            'details': [(ds, k, sc) for ds, k, sc in proposed],
        }

    # write mapping JSON and CSV
    with open(MAPPING_JSON, 'w', encoding='utf-8') as fh:
        json.dump(mapping, fh, ensure_ascii=False, indent=2)

    with open(MAPPING_CSV, 'w', encoding='utf-8') as fh:
        fh.write('iteration,requested,proposed\n')
        for k, v in mapping['per_iteration'].items():
            fh.write(f"{k},'{v['requested']}'," + '"' + ",".join(v['proposed']) + '"' + '\n')

    print('Mapping written to:', MAPPING_JSON)
    print('CSV summary written to:', MAPPING_CSV)

    # select which to test
    mapped_items = [k for k, v in mapping['per_iteration'].items() if v['proposed']]
    if not mapped_items:
        print('No mapped iterations proposed.')
        return

    to_run = mapped_items if args.run_all_mapped else mapped_items[: args.max_test]
    print(f"Testing {len(to_run)} mapped iterations (light={args.light}).")

    results = {'attempted': [], 'ok': [], 'failed': []}
    for key in to_run:
        it = next((d for d in defs if d.key == key), None)
        if it is None:
            results['failed'].append({'iteration': key, 'error': 'definition not found'})
            continue
        props = mapping['per_iteration'][key]['proposed']
        if not props:
            results['failed'].append({'iteration': key, 'error': 'no proposed datasets'})
            continue

        use_it = replace(it, datasets=props)
        if args.light:
            small_seeds = [0]
            small_missing = [it.missing_list[0]] if it.missing_list else [0.2]
            use_it = replace(use_it, seeds=small_seeds, missing_list=small_missing, graph_specs=it.graph_specs[:1], methods=it.methods[:1] if it.methods else None)

        print('Running', key, '->', props)
        try:
            base_mod._run_iteration(use_it, availability, data, operational_close_profile=False)
            results['ok'].append(key)
            print('OK', key)
        except Exception as exc:
            results['failed'].append({'iteration': key, 'error': str(exc)})
            print('FAILED', key, exc)

    # save run attempt summary
    out_summary = ROOT / 'experiments' / 'propose_mapping_run_summary.json'
    out_summary.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Summary written to', out_summary)
    print('Done.')


if __name__ == '__main__':
    main()
