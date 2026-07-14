#!/usr/bin/env python3
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / 'results'
PROG = ROOT / 'experiments' / 'propose_and_try_mappings.progress.log'
FULL = ROOT / 'experiments' / 'propose_and_try_mappings.fullrun.log'

files = list(RES.rglob('rerun_*_raw.csv'))
ids = set()
for f in files:
    m = re.match(r'^rerun_(\d+)_raw\.csv$', f.name)
    if m:
        ids.add(int(m.group(1)))

ids_sorted = sorted(ids)
done = len(ids_sorted)
expected = 209
missing = [i for i in range(expected) if i not in ids_sorted]

last_progress = '(no progress log yet)'
last_full = '(no fullrun log yet)'
if PROG.exists():
    lines = PROG.read_text(encoding='utf-8').splitlines()
    last_progress = '\n'.join(lines[-5:])
if FULL.exists():
    lines = FULL.read_text(encoding='utf-8').splitlines()
    last_full = '\n'.join(lines[-60:])

print(f"DONE_COUNT:{done}")
print(f"MISSING_COUNT:{len(missing)}")
print(f"DONE_SAMPLE:{','.join(map(str, ids_sorted[-5:])) if ids_sorted else ''}")
print('LAST_PROGRESS:')
print(last_progress)
print('LAST_FULL_LOG:')
print(last_full)
