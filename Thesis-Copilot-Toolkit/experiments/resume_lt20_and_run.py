#!/usr/bin/env python3
"""
Resume LT20 reruns: detect missing tags and run them in-process,
logging progress to experiments/resume_lt20_and_run.log and
saving a snapshot when finished.
"""
import importlib.util
import sys
import traceback
import time
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / 'experiments' / 'run_reruns_selected.py'
SAVE_SCRIPT = ROOT / 'experiments' / 'save_reruns_snapshot.py'
RESULTS = ROOT / 'results'
LOG = ROOT / 'experiments' / 'resume_lt20_and_run.log'

def load_runner_module(path: Path):
    spec = importlib.util.spec_from_file_location('runner_mod', str(path))
    runner = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = runner
    spec.loader.exec_module(runner)
    return runner


def main():
    with open(LOG, 'a', encoding='utf-8') as fh:
        fh.write('\n=== resume_lt20_and_run.py START %s ===\n' % time.ctime())
        try:
            runner = load_runner_module(RUNNER)
        except Exception:
            fh.write('Failed to load runner module:\n')
            fh.write(traceback.format_exc())
            raise

        defs = getattr(runner, '_defs', [])
        base_mod = getattr(runner, 'mod', None)
        if base_mod is None:
            fh.write('Base iteration engine (mod) not found in runner module.\n')
            raise SystemExit(1)

        keys = [d.key for d in defs]
        missing = [k for k in keys if not (RESULTS / f"{k}_raw.csv").exists()]

        fh.write('Total tags: %d, missing: %d\n' % (len(keys), len(missing)))
        print('Total tags:', len(keys), 'missing:', len(missing))

        if not missing:
            fh.write('No missing tags; nothing to run.\n')
            print('No missing tags; nothing to run.')
            return

        # load availability/data once
        try:
            av = base_mod.load_data_availability()
            availability = av['availability']
            data = av['data']
        except Exception:
            fh.write('Failed to load data availability:\n')
            fh.write(traceback.format_exc())
            raise

        for k in missing:
            it = next((d for d in defs if d.key == k), None)
            if it is None:
                fh.write(f'UNKNOWN KEY {k}\n')
                continue

            fh.write(f"\n>> START {k} at {time.ctime()}\n")
            fh.flush()
            print('Starting', k)
            try:
                base_mod._run_iteration(it, availability, data, operational_close_profile=False)
                fh.write(f"<< OK {k} at {time.ctime()}\n")
                print('Done', k)
            except Exception:
                fh.write('<< ERROR\n')
                fh.write(traceback.format_exc())
                fh.write('\n')
                fh.flush()
                print('Error running', k)
                # continue with next tag

        fh.write('\nAll missing tags processed.\n')

        # attempt to save snapshot
        if SAVE_SCRIPT.exists():
            fh.write('Saving snapshot using save_reruns_snapshot.py\n')
            fh.flush()
            try:
                subprocess.run([sys.executable, str(SAVE_SCRIPT), '--name', 'reruns_lt20'], check=True, stdout=fh, stderr=subprocess.STDOUT)
                fh.write('Snapshot saved.\n')
            except subprocess.CalledProcessError:
                fh.write('Snapshot command failed:\n')
                fh.write(traceback.format_exc())
        else:
            fh.write('Snapshot script not found: %s\n' % str(SAVE_SCRIPT))

        fh.write('=== resume_lt20_and_run.py END %s ===\n' % time.ctime())

if __name__ == '__main__':
    main()
