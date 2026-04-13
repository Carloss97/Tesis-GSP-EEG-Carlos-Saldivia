#!/usr/bin/env python3
import csv
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'results'
files = sorted(RESULTS.glob('rerun_*_raw.csv'))
sum_time = 0.0
count = 0
for f in files:
    try:
        with f.open('r', encoding='utf-8') as fh:
            # skip empty lines; DictReader needs header
            lines = [l for l in fh if l.strip()]
            if not lines:
                continue
            reader = csv.DictReader(lines)
            if 'time_sec' not in reader.fieldnames:
                continue
            for row in reader:
                t = row.get('time_sec','')
                try:
                    if t is None or t == '':
                        continue
                    tt = float(t)
                    sum_time += tt
                    count += 1
                except Exception:
                    continue
    except Exception:
        continue
mean = (sum_time/count) if count else None
# read selection lt20
sel = RESULTS / 'analysis' / 'batches' / 'rerun_selection_lt20.csv'
total_needed = 0
if sel.exists():
    with sel.open('r', encoding='utf-8') as fh:
        rdr = csv.DictReader(fh)
        for r in rdr:
            try:
                total_needed += int(r.get('additional_needed') or 0)
            except Exception:
                continue
else:
    print('Selection file not found:', sel)
    total_needed = None
# report
print('sampled_files=', len(files))
print('sampled_rows=', count)
if mean is None:
    print('mean_time_per_row: N/A (no data)')
else:
    print(f'mean_time_per_row={mean:.6f}s')
print('total_needed_rows=', total_needed)
if mean is not None and total_needed:
    total_seconds = mean * total_needed
    def fmt(s):
        h = int(s//3600)
        m = int((s%3600)//60)
        sec = int(s%60)
        return f'{h}h {m}m {sec}s'
    print('estimated_total_seconds=', int(total_seconds), fmt(total_seconds))
    print('estimates:')
    for factor,label in [(0.5,'optimistic (x0.5)'),(1.0,'mean'),(2.0,'pessimistic (x2)')]:
        s = total_seconds * factor
        print(f'  {label}:', fmt(s))
print('done')
