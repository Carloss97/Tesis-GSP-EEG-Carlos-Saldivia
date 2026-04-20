#!/usr/bin/env python3
"""Map dataset names in a rerun schedule JSON to available engine dataset keys.

Usage:
  python experiments/map_rerun_schedule_datasets.py in.json out.json
"""
import json
import sys
from pathlib import Path

def map_dataset(name: str) -> str | None:
    n = name.lower()
    if 'mne_sample' in n:
        return 'mne_sample'
    if 'bci_iv2a' in n or 'bci_competition' in n or 'bci_competition_iv_2a' in n:
        # default to subject 1 proxy
        return 'bci_iv2a_real_s1'
    if 'physionet' in n or 'eegmmidb' in n:
        return 'physionet_real'
    if 'iv100hz' in n or 'iv100hz_mat' in n:
        return 'iv100hz_mat'
    if 'iris' in n:
        return 'iris_graph_signal'
    if 'movielens' in n:
        return 'movielens_graph_signal'
    # synthetic datasets: no mapping (engine does not expose synthetic keys via availability)
    if n.startswith('synthetic'):
        return None
    # fallback: if exact name matches common keys, return as-is
    for k in ['mne_sample','iv100hz_mat','iris_graph_signal','movielens_graph_signal','physionet_real','bci_iv2a_real_s1','bci_iv2a_real_s2','bci_iv2a_real_s3']:
        if k == name:
            return k
    return None

def main():
    if len(sys.argv) < 3:
        print('Usage: map_rerun_schedule_datasets.py in.json out.json')
        raise SystemExit(2)
    pin = Path(sys.argv[1])
    pout = Path(sys.argv[2])
    sched = json.loads(pin.read_text(encoding='utf-8'))
    iters = sched.get('iterations', [])
    kept = []
    skipped = []
    for it in iters:
        ds = it.get('datasets', [])
        mapped = []
        for d in ds:
            m = map_dataset(d)
            if m:
                if m not in mapped:
                    mapped.append(m)
        if not mapped:
            skipped.append(it.get('key'))
            continue
        it['datasets'] = mapped
        kept.append(it)

    out = {'generated': sched.get('generated'), 'iterations': kept}
    pout.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Wrote', pout, 'iterations_kept=', len(kept), 'skipped=', len(skipped))
    if skipped:
        print('Skipped keys sample:', skipped[:10])

if __name__ == '__main__':
    main()
