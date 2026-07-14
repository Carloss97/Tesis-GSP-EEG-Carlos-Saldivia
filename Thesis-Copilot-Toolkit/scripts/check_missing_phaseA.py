import json, os
ROOT='Thesis-Copilot-Toolkit'
sched_path=os.path.join(ROOT,'experiments','schedules','it01-it50_schedule_phaseA_real_varied.json')
res_dir=os.path.join(ROOT,'results')
with open(sched_path,'r',encoding='utf-8') as f:
    s=json.load(f)
keys=[it.get('key') for it in s.get('iterations',[])]
missing=[k for k in keys if not os.path.exists(os.path.join(res_dir,f'{k}_run_metadata.json'))]
print('MISSING_KEYS:', missing)
