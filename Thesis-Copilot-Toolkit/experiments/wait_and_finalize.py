"""
wait_and_finalize.py

Waits for the bulk results folder to reach `expected_count` completed iterations,
then runs `generate_b1_b4.py` to produce B1–B4 and cutoff reports.

This script is intended to be launched in background while the experiments run.
"""
from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / 'results_rms_full150'
EXPECTED = 150
POLL_INTERVAL = 30


def count_completed(results_dir: Path) -> int:
    return len(list(results_dir.glob('*_run_metadata.json')))


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--results', type=str, default=str(RESULTS_DIR))
    parser.add_argument('--expected', type=int, default=EXPECTED)
    parser.add_argument('--poll', type=int, default=POLL_INTERVAL)
    args = parser.parse_args()

    results_dir = Path(args.results)
    expected = args.expected
    poll = args.poll

    print('Waiting for experiments to complete in', results_dir)
    while True:
        if results_dir.exists():
            done = count_completed(results_dir)
        else:
            done = 0
        print(f'Completed runs: {done}/{expected}')
        if done >= expected:
            print('Detected all runs complete — generating B1–B4 and cutoffs')
            break
        time.sleep(poll)

    # run generator
    gen_script = ROOT / 'experiments' / 'generate_b1_b4.py'
    cmd = [sys.executable, str(gen_script), '--results', str(results_dir.name)]
    print('Running:', ' '.join(cmd))
    subprocess.run(cmd, check=False)
    print('generate_b1_b4 finished. Exiting.')


if __name__ == '__main__':
    main()
