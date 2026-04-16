import importlib.util
import sys
import json
import traceback
from pathlib import Path

ROOT = Path('Thesis-Copilot-Toolkit')
BASE_SCRIPT = ROOT / 'experiments' / 'run_future_work_it121_it130.py'
spec = importlib.util.spec_from_file_location('base_mod', str(BASE_SCRIPT))
base_mod = importlib.util.module_from_spec(spec)
loader = spec.loader
sys.modules[spec.name] = base_mod
loader.exec_module(base_mod)

check = base_mod.load_data_availability()
availability = check.get('availability', {})
data = check.get('data', {})

meta_p = Path('Thesis-Copilot-Toolkit') / 'results_screening_2000' / 'scr_00307_run_metadata.json'
print('Reading metadata:', meta_p)
meta = json.loads(meta_p.read_text(encoding='utf-8'))
print('meta datasets:', meta.get('datasets'), 'missing_ratios:', meta.get('missing_ratios'))

# replicate progressive_confirmatory behavior for this tag
ds = meta.get('datasets', [None])[0]
if ds is None:
    raise RuntimeError('No dataset in metadata')

# choose dataset key (fallback to same key)
ds_key = ds if availability.get(ds, {}).get('ok') else list(availability.keys())[0]

graph_tag = meta.get('graphs', [None])[0] or 'knn'
# simple parse for k or sigma
if '__' in str(graph_tag):
    gparts = str(graph_tag).split('__')
    gname = gparts[0]
    gparams = {}
else:
    gname = str(graph_tag)
    gparams = {}

mlist = meta.get('missing_ratios', [0.2])
# use the best_method if available
best_method = meta.get('best_method')
methods = [best_method] if best_method else None

it_key = 'repro_confirm_scr_00307'
from dataclasses import replace
it = base_mod.IterDef(
    it_key,
    it_key,
    f'Repro confirm: scr_00307',
    'Confirmatory',
    'Repro of failing confirm',
    [ds_key],
    mode='base',
    missing_list=mlist,
    seeds=list(range(4)),
    graph_specs=[(gname, gparams)],
    methods=methods,
)

print('Running IterDef:', it)
try:
    base_mod._run_iteration(it, availability, data, operational_close_profile=False)
    print('Iteration completed successfully')
except Exception as e:
    print('Iteration raised exception:')
    traceback.print_exc()
    raise
