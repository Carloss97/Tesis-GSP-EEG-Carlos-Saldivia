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
all_ok = True
for i in range(1,51):
    k = f'it{str(i).zfill(2)}'
    t = bytag.get(k)
    if not t:
        print(k, 'MISSING')
        all_ok = False
        continue
    has_raw = t.get('has_raw', False)
    has_stats = t.get('has_stats', False)
    issues = t.get('issues', [])
    status = 'OK' if has_raw and has_stats and not issues else 'PROBLEM'
    print(k, status, f'raw={has_raw}', f'stats={has_stats}', f'issues={";".join(issues)}')
    if not (has_raw and has_stats and not issues):
        all_ok = False
print('\nAll 50 completed:', all_ok)
if not all_ok:
    raise SystemExit(1)
else:
    raise SystemExit(0)
