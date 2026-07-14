import sys
from pathlib import Path
import json

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.append(str(SCRIPT_DIR))
from classify_no_go_for_comparison import find_best_stats_candidate, _inspect_stats_file

SCHEDULE_A = SCRIPT_DIR.parent / 'experiments' / 'schedules' / 'it01-it50_schedule_phaseA_real_varied.json'

with open(SCHEDULE_A, 'r', encoding='utf-8') as f:
    j = json.load(f)

for it in j.get('iterations', []):
    tag = it.get('tag') or it.get('key')
    datasets = it.get('datasets') or []
    dataset = datasets[0] if datasets else ''
    cand = find_best_stats_candidate(tag, dataset)
    if cand:
        hv, mc = _inspect_stats_file(cand)
        print(tag, dataset, cand.name, hv, mc)
    else:
        print(tag, dataset, 'NO_CAND')
