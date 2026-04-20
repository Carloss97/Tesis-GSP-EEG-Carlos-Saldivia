"""Remap accepted NO-GO entries to best available multi-method _stats.csv files.

Heuristics:
 - Prefer files containing the dataset substring and with highest method count.
 - Avoid files with "confirm_000" in their name unless no other valid candidate exists.
 - Fallback to any valid _stats.csv with highest method_count.

This script backups the current `no_go_accepted_provisional.csv` to
`no_go_accepted_provisional_backup.csv` and writes the new file in place.
It also writes `no_go_accepted_provisional_remap_trace.csv` with chosen candidates.

Run inside the `eegrasp` env:
  conda activate eegrasp
  python Thesis-Copilot-Toolkit/scripts/remap_accepted_stats.py
"""
from pathlib import Path
import pandas as pd
import math
import shutil
import json

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'results'
ACCEPTED = RESULTS / 'no_go_accepted_provisional.csv'
BACKUP = RESULTS / 'no_go_accepted_provisional_backup.csv'
TRACE = RESULTS / 'no_go_accepted_provisional_remap_trace.csv'

SCHED_A = ROOT / 'experiments' / 'schedules' / 'it01-it50_schedule_phaseA_real_varied.json'
SCHED_B = ROOT / 'experiments' / 'schedules' / 'it01-it50_schedule_phaseB_real_mne_sample.json'

# utils

def inspect_stats(path: Path):
    try:
        if not path.exists():
            return False, 0
        df = pd.read_csv(path)
        col = None
        for c in ('mae_median', 'mae_mean'):
            if c in df.columns:
                col = c
                break
        if col is None:
            return False, 0
        if 'method' in df.columns:
            try:
                mcount = int(df['method'].nunique())
            except Exception:
                mcount = len(df.index)
        else:
            mcount = len(df.index)
        ok = False
        for v in df[col].values:
            try:
                if pd.notna(v) and not math.isinf(float(v)):
                    ok = True
                    break
            except Exception:
                continue
        return ok, int(mcount)
    except Exception:
        return False, 0


# collect schedule entries (unique)
entries = []
for sched in (SCHED_A, SCHED_B):
    if not sched.exists():
        continue
    j = json.loads(sched.read_text(encoding='utf-8'))
    for it in j.get('iterations', []):
        tag = it.get('tag') or it.get('key') or ''
        datasets = it.get('datasets') or []
        dataset = datasets[0] if datasets else ''
        entries.append((tag, dataset))

# unique preserve order
seen = set()
uniq_entries = []
for t, d in entries:
    k = (t, d)
    if k not in seen:
        seen.add(k)
        uniq_entries.append(k)

# gather candidates
cands = list(RESULTS.rglob('*_stats.csv'))
# pre-inspect candidates
cand_info = {}
for p in cands:
    ok, mcount = inspect_stats(p)
    cand_info[p] = (ok, mcount)

# helper to choose best

def choose_for(tag, dataset):
    # prefer dataset match
    dataset_lower = (dataset or '').lower()
    best = None
    best_mc = -1
    # try dataset matches first (avoid confirm_000)
    for p, (ok, mc) in cand_info.items():
        if not ok:
            continue
        name = p.name.lower()
        if dataset_lower and dataset_lower in name and 'confirm_000' not in name:
            if mc > best_mc:
                best = p
                best_mc = mc
    if best:
        return best, cand_info[best]
    # try dataset matches including confirm_000
    for p, (ok, mc) in cand_info.items():
        if not ok:
            continue
        name = p.name.lower()
        if dataset_lower and dataset_lower in name:
            if mc > best_mc:
                best = p
                best_mc = mc
    if best:
        return best, cand_info[best]
    # else choose any non-confirm with highest mc
    for p, (ok, mc) in cand_info.items():
        if not ok:
            continue
        if 'confirm_000' in p.name.lower():
            continue
        if mc > best_mc:
            best = p
            best_mc = mc
    if best:
        return best, cand_info[best]
    # last resort: any confirm_000 valid
    for p, (ok, mc) in cand_info.items():
        if not ok:
            continue
        if 'confirm_000' in p.name.lower():
            if mc > best_mc:
                best = p
                best_mc = mc
    if best:
        return best, cand_info[best]
    return None, (False, 0)

# backup original accepted
if ACCEPTED.exists():
    shutil.copy2(ACCEPTED, BACKUP)

rows = []
trace_rows = []
for tag, dataset in uniq_entries:
    best, (ok, mc) = choose_for(tag, dataset)
    if best:
        rows.append({'tag': tag, 'dataset': dataset, 'stats_path': str(best)})
        trace_rows.append({'tag': tag, 'dataset': dataset, 'chosen': str(best), 'has_valid': ok, 'method_count': int(mc)})
    else:
        # leave empty stats_path if none found
        rows.append({'tag': tag, 'dataset': dataset, 'stats_path': ''})
        trace_rows.append({'tag': tag, 'dataset': dataset, 'chosen': '', 'has_valid': False, 'method_count': 0})

# write new accepted
ACCEPTED.write_text('tag,dataset,stats_path\n', encoding='utf-8')
with ACCEPTED.open('a', encoding='utf-8') as f:
    for r in rows:
        f.write(f"{r['tag']},{r['dataset']},{r['stats_path']}\n")

# write trace
import csv
with TRACE.open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['tag', 'dataset', 'chosen', 'has_valid', 'method_count'])
    w.writeheader()
    for r in trace_rows:
        w.writerow(r)

print('Remap complete. Wrote', ACCEPTED)
print('Trace:', TRACE)
valids = [r for r in trace_rows if r['has_valid']]
print('Entries total:', len(trace_rows), 'valid mapped:', len(valids))
