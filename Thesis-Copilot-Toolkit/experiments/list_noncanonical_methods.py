import json

SCHEDULE = 'Thesis-Copilot-Toolkit/experiments/schedules/it01-it50_schedule_final_canonical.json'

with open(SCHEDULE, 'r', encoding='utf-8') as f:
    s = json.load(f)

found = []
for it in s.get('iterations', []):
    key = it.get('key')
    methods = it.get('methods', []) or []
    hits = []
    for bad in ('gsp', 'gsmooth', 'graph_time_tikhonov'):
        if bad in methods:
            hits.append(bad)
    if hits:
        found.append((key, hits))

for k, h in found:
    print(k, h)

print('\nTotal iterations with non-canonical methods:', len(found))
