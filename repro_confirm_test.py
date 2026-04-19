import importlib.util
import sys
from pathlib import Path

ROOT = Path('Thesis-Copilot-Toolkit')
BASE_SCRIPT = ROOT / 'experiments' / 'run_future_work_it121_it130.py'
print('Loading base script from', BASE_SCRIPT)
spec = importlib.util.spec_from_file_location('base_mod', str(BASE_SCRIPT))
base_mod = importlib.util.module_from_spec(spec)
loader = spec.loader
sys.modules['base_mod'] = base_mod
if loader is None:
    raise RuntimeError('Loader is None')
loader.exec_module(base_mod)
print('base_mod loaded')

check = base_mod.load_data_availability()
availability = check.get('availability', {})
data = check.get('data', {})
print('datasets available:', list(availability.keys()))

it = base_mod.IterDef(
    'test_confirm_scr_00199',
    'test_confirm_scr_00199',
    'test',
    'Confirmatory',
    'repro test',
    ['iris_graph_signal'],
    mode='base',
    missing_list=['2ch'],
    seeds=[0],
    graph_specs=[('knn', {'k': 3})],
    methods=["linear", "ica", "spherical_spline", "rbfi_tps"],
    # Use canonical baselines for confirmatory test
    # NOTE: 'mean' and 'nearest' are deprecated for future iterations
    # and replaced by the canonical baseline set below.
)

base_mod.RESULTS = ROOT / 'results_tmp_repro'
base_mod.RESULTS.mkdir(parents=True, exist_ok=True)

print('Starting _run_iteration test')
base_mod._run_iteration(it, availability, data, operational_close_profile=False)
print('Test _run_iteration finished')
