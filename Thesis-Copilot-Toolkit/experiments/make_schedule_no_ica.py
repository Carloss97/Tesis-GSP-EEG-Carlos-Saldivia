#!/usr/bin/env python3
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
src = ROOT / 'experiments' / 'schedules' / 'it01-it50_schedule_final.json'
dst = ROOT / 'experiments' / 'schedules' / 'it10-it50_no_ica.json'
if not src.exists():
    print('source schedule not found:', src)
    raise SystemExit(2)
J = json.loads(src.read_text(encoding='utf-8'))
iterations = J.get('iterations', [])
keep = {'it10','it20','it30','it40','it50'}
new_iters = []
for it in iterations:
    key = it.get('key')
    if key in keep:
        methods = it.get('methods', None)
        if methods:
            methods = [m for m in methods if m.lower() != 'ica']
            it2 = dict(it)
            it2['methods'] = methods
            new_iters.append(it2)

out = {'iterations': new_iters}
dst.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
print('Wrote', dst)
