#!/usr/bin/env python3
import json
import os
from datetime import datetime

SCHEDULE = 'Thesis-Copilot-Toolkit/experiments/schedules/it01-it50_schedule_final_canonical.json'
BACKUP = SCHEDULE + '.bak'
REMOVE = {'gsp', 'gsmooth', 'graph_time_tikhonov'}


def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save(obj, path):
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def main():
    if not os.path.exists(SCHEDULE):
        print('Schedule not found:', SCHEDULE)
        return
    sched = load(SCHEDULE)
    # backup
    save(sched, BACKUP)
    changed = False
    count_removed = 0
    for it in sched.get('iterations', []):
        methods = it.get('methods') or []
        new_methods = [m for m in methods if m not in REMOVE]
        if len(new_methods) != len(methods):
            removed = len(methods) - len(new_methods)
            count_removed += removed
            it['methods'] = new_methods
            changed = True
    if changed:
        sched['generated'] = datetime.utcnow().isoformat() + 'Z'
        save(sched, SCHEDULE)
    print('Done. Removed occurrences:', count_removed)


if __name__ == '__main__':
    main()
