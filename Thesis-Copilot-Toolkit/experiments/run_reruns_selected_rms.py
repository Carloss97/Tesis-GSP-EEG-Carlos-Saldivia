"""
Run selected reruns (like `run_reruns_selected.py`) but override the
results folder to `results_rms` so outputs are kept separate and
identified as RMS-normalized runs.

Usage: run this script from the repo root with the project venv
and environment variables set: `NORMALIZE_DATASETS=1` and
`NORM_METHOD=rms`.
"""
import importlib.util
from dataclasses import replace
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE_SCRIPT = ROOT / 'experiments' / 'run_future_work_it121_it130.py'

# Prefer a real-runner that uses the real `mne_sample` dataset when available.
runner_path_preferred = ROOT / 'experiments' / 'run_reruns_selected_real.py'
runner_path_fallback = ROOT / 'experiments' / 'run_reruns_selected.py'
if runner_path_preferred.exists():
    runner_path = runner_path_preferred
elif runner_path_fallback.exists():
    runner_path = runner_path_fallback
else:
    raise SystemExit(f"Runner not found: {runner_path_fallback}; generate it first with generate_runner_from_selection.py")

# Load the generated runner module and override its base module RESULTS variable
spec_runner = importlib.util.spec_from_file_location('runner_mod', str(runner_path))
runner_mod = importlib.util.module_from_spec(spec_runner)
loader_runner = spec_runner.loader
sys.modules[spec_runner.name] = runner_mod
loader_runner.exec_module(runner_mod)

# The generated runner defines `mod` (the base iteration engine module).
if not hasattr(runner_mod, 'mod'):
    raise SystemExit('Generated runner does not expose `mod`. Aborting.')

runner_mod.mod.RESULTS = ROOT / 'results_rms'
runner_mod.mod.RESULTS.mkdir(parents=True, exist_ok=True)

def main():
    # Delegate to the generated runner's main, after ensuring mod.RESULTS is overridden
    if not hasattr(runner_mod, 'main'):
        raise SystemExit('Generated runner lacks main()')
    # Pass-through: call generated runner main (it will use runner_mod.mod.RESULTS)
    runner_mod.main()


if __name__ == '__main__':
    main()
