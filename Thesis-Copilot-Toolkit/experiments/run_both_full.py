#!/usr/bin/env python3
"""
Wrapper to run full reruns for selection `<5` then `<20` sequentially.
It regenerates the runner from each selection, runs it (no --light-profile), and saves a snapshot.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / 'experiments' / 'generate_runner_from_selection.py'
RUN = ROOT / 'experiments' / 'run_reruns_selected.py'
SAVE = ROOT / 'experiments' / 'save_reruns_snapshot.py'

selections = [
    ('rerun_selection_lt5.csv', 'reruns_lt5'),
    ('rerun_selection_lt20.csv', 'reruns_lt20'),
]

def run_cmd(cmd, desc):
    print(f"--> {desc}: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def main():
    py = sys.executable
    for sel_name, out_name in selections:
        sel = ROOT / 'results' / 'analysis' / 'batches' / sel_name
        if not sel.exists():
            print(f"Selection not found: {sel} -- skipping {sel_name}")
            continue
        # generate runner for this selection
        run_cmd([py, str(GEN), '--selection', str(sel)], f"Generate runner for {sel_name}")
        # run the runner (full-profile)
        run_cmd([py, str(RUN)], f"Execute runner for {sel_name} (full)")
        # save snapshot
        run_cmd([py, str(SAVE), '--name', out_name], f"Save snapshot for {out_name}")
    print('All done.')

if __name__ == '__main__':
    main()
