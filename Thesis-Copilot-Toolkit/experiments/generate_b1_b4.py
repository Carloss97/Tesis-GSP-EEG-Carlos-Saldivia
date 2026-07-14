"""
generate_b1_b4.py

Aggregate results from a bulk run (results_rms_full150 by default), compute
TV vs Instant medians and percent gain, classify into B1–B4 and emit
Markdown cutoff reports for <5% and <20%.

Usage:
  python experiments/generate_b1_b4.py --results results_rms_full150
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Dict, Any, List

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
BASE_SCRIPT = ROOT / 'experiments' / 'run_future_work_it121_it130.py'

# load base module to reuse _significance
spec = importlib.util.spec_from_file_location('base_mod', str(BASE_SCRIPT))
base_mod = importlib.util.module_from_spec(spec)
loader = spec.loader
assert loader is not None
import sys as _sys
# ensure module is present in sys.modules so dataclasses and introspection work
_sys.modules[spec.name] = base_mod
loader.exec_module(base_mod)

def analyze_results(results_dir: Path) -> List[Dict[str, Any]]:
    entries: List[Dict[str, Any]] = []
    for raw_path in sorted(results_dir.glob('*_raw.csv')):
        tag = raw_path.name.replace('_raw.csv', '')
        try:
            df = pd.read_csv(raw_path)
            if df.empty:
                continue
            sig = base_mod._significance(df).iloc[0]
            gain = float(sig.get('gain_pct', 0.0))
            tv_m = float(sig.get('tv_median', float('nan')))
            inst_m = float(sig.get('instant_median', float('nan')))
            p = float(sig.get('p_value', float('nan')))
            decision = str(sig.get('decision', 'NO-GO'))
            entries.append({
                'tag': tag,
                'gain_pct': gain,
                'tv_median': tv_m,
                'instant_median': inst_m,
                'p_value': p,
                'decision': decision,
            })
        except Exception as exc:
            print(f"Failed to analyze {tag}: {exc}")
    return entries


def classify(entries: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    for e in entries:
        g = e['gain_pct']
        if g >= 20.0:
            b1.append(e)
        elif g >= 5.0:
            b2.append(e)
        elif g >= 0.0:
            b3.append(e)
        else:
            b4.append(e)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}


def write_outputs(results_dir: Path, entries: List[Dict[str, Any]], groups: Dict[str, List[Dict[str, Any]]]):
    out_csv = results_dir / 'b1_b2_b3_b4.csv'
    pd.DataFrame(entries).sort_values('gain_pct', ascending=False).to_csv(out_csv, index=False)

    summary_md = [
        '# B1–B4 Classification',
        '',
        f'- Total runs analyzed: {len(entries)}',
        f'- B1 (gain ≥20%): {len(groups["B1"]) }',
        f'- B2 (5% ≤ gain <20%): {len(groups["B2"]) }',
        f'- B3 (0% ≤ gain <5%): {len(groups["B3"]) }',
        f'- B4 (gain <0%): {len(groups["B4"]) }',
        '',
        '## Lists by group',
    ]

    for k in ['B1', 'B2', 'B3', 'B4']:
        summary_md.append(f'### {k} ({len(groups[k])})')
        summary_md.append('')
        summary_md.append('| tag | gain_pct | p_value | decision |')
        summary_md.append('|---|---:|---:|---|')
        for e in sorted(groups[k], key=lambda x: x['gain_pct'], reverse=True):
            summary_md.append(f"| {e['tag']} | {e['gain_pct']:.2f}% | {e['p_value']:.3e} | {e['decision']} |")
        summary_md.append('')

    (results_dir / 'b1_b2_b3_b4.md').write_text('\n'.join(summary_md), encoding='utf-8')

    # cutoffs
    cutoff_lt5 = [e for e in entries if e['gain_pct'] < 5.0]
    cutoff_lt20 = [e for e in entries if e['gain_pct'] < 20.0]

    def write_cutoff(path: Path, name: str, items: List[Dict[str, Any]]):
        md = [f'# Cutoff: {name}', '', f'Total: {len(items)}', '', '| tag | gain_pct | p_value | decision |', '|---|---:|---:|---|']
        for e in sorted(items, key=lambda x: x['gain_pct']):
            md.append(f"| {e['tag']} | {e['gain_pct']:.2f}% | {e['p_value']:.3e} | {e['decision']} |")
        path.write_text('\n'.join(md), encoding='utf-8')

    write_cutoff(results_dir / 'cutoff_lt5.md', '<5%', cutoff_lt5)
    write_cutoff(results_dir / 'cutoff_lt20.md', '<20%', cutoff_lt20)

    # JSON
    (results_dir / 'b1_b2_b3_b4.json').write_text(json.dumps(groups, ensure_ascii=False, indent=2), encoding='utf-8')


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--results', type=str, default='results_rms_full150')
    args = parser.parse_args()

    results_dir = ROOT / args.results
    if not results_dir.exists():
        print('Results folder not found:', results_dir)
        sys.exit(1)

    entries = analyze_results(results_dir)
    groups = classify(entries)
    write_outputs(results_dir, entries, groups)
    print('B1–B4 generation complete. Files written to', results_dir)


if __name__ == '__main__':
    main()
