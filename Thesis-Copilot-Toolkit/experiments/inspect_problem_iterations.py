#!/usr/bin/env python3
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / 'results' / 'postprocess_summary.json'
if not SUMMARY.exists():
    print('postprocess_summary.json not found')
    raise SystemExit(2)
J = json.loads(SUMMARY.read_text(encoding='utf-8'))
bytag = {t['tag']: t for t in J.get('tags', [])}
check = ['it10','it20','it30','it40','it50']
for k in check:
    t = bytag.get(k)
    if not t:
        print(f'{k}: MISSING')
        continue
    print('---')
    print('tag:', k)
    print('issues:', t.get('issues'))
    print('errors_count:', t.get('errors_count'))
    es = t.get('errors_sample') or []
    if es:
        print('errors_sample:')
        for e in es[:5]:
            print(' -', e)
    print('n_rows:', t.get('n_rows'))
    print('n_methods:', t.get('n_methods'))
    print('stats_methods:', t.get('stats_methods'))
    print('methods:', ','.join(t.get('methods',[])))
    meta = t.get('meta',{})
    req = meta.get('requested_datasets') if meta else None
    print('requested_datasets:', req)
    print('mae_mean, mae_std:', t.get('mae_mean'), t.get('mae_std'))
    print('time_max_sec, time_mean_sec:', t.get('time_max_sec'), t.get('time_mean_sec'))

print('\nDone')
