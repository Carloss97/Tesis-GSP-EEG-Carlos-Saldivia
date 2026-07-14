import json, os
ROOT='Thesis-Copilot-Toolkit'
sched_path=os.path.join(ROOT,'experiments','schedules','it01-it50_schedule_phaseA_real_varied.json')
res_dir=os.path.join(ROOT,'results')
with open(sched_path,'r',encoding='utf-8') as f:
    s=json.load(f)
keys=[it.get('key') for it in s.get('iterations',[])]
summary=[]
for k in keys:
    md_path=os.path.join(res_dir,f'{k}_run_metadata.json')
    if not os.path.exists(md_path):
        summary.append((k,'MISSING'))
        continue
    try:
        md=json.load(open(md_path,'r',encoding='utf-8'))
        qa=md.get('qa',{})
        status=qa.get('status','UNKNOWN') if isinstance(qa,dict) else 'UNKNOWN'
    except Exception as e:
        status=f'ERROR_READ:{e}'
    summary.append((k,status))

nogos=[k for k,s in summary if s!='OK']
print('TOTAL:', len(keys))
print('NON-OK COUNT:', len(nogos))
for k,s in summary:
    print(k, s)
