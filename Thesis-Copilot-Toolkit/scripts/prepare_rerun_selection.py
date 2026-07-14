#!/usr/bin/env python3
"""
Prepare rerun selection CSVs from `rerun_candidates_target200.csv`.
Usage:
  python scripts/prepare_rerun_selection.py --mode all
  python scripts/prepare_rerun_selection.py --mode "<5"    # n_current < 5
  python scripts/prepare_rerun_selection.py --mode "<20"   # n_current < 20

Outputs:
 - results/analysis/batches/rerun_selection_<mode>.csv
"""
from pathlib import Path
import argparse
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
BATCH = ROOT / 'results' / 'analysis' / 'batches'
SRC = BATCH / 'rerun_candidates_target200.csv'

parser = argparse.ArgumentParser()
parser.add_argument('--mode', choices=['all','<5','<20'], default='all')
args = parser.parse_args()

if not SRC.exists():
    print('Source rerun_candidates_target200.csv not found at', SRC)
    raise SystemExit(1)

df = pd.read_csv(SRC)
mode = args.mode
if mode == 'all':
    sel = df.copy()
elif mode == '<5':
    sel = df[df['n_current'] < 5].copy()
elif mode == '<20':
    sel = df[df['n_current'] < 20].copy()
else:
    sel = df.copy()

out = BATCH / f'rerun_selection_{mode.replace("<", "lt")}.csv'
sel.to_csv(out, index=False)
print('Wrote', out)
print('Combos:', len(sel), 'total additional runs:', sel['additional_needed'].sum())
