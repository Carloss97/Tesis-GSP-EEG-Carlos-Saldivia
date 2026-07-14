#!/usr/bin/env python3
"""
Copy rerun artifacts into a timestamped folder.
Usage: python experiments/save_reruns_snapshot.py --name reruns_lt5
"""
from pathlib import Path
from datetime import datetime
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="reruns_snapshot")
args = parser.parse_args()

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
target = RESULTS / f"{args.name}_{stamp}"
target.mkdir(parents=True, exist_ok=True)

copied = []
# copy files matching rerun_* (raw, stats, significance, qa, metadata, integration_log)
suffixes = ("_raw.csv", "_stats.csv", "_significance.csv", "_qa_report.md", "_run_metadata.json", "_integration_log.md")
for p in sorted(RESULTS.iterdir()):
    if p.is_file() and p.name.startswith("rerun_") and p.name.endswith(suffixes):
        dst = target / p.name
        shutil.copy2(p, dst)
        copied.append(dst.relative_to(ROOT))
# copy rerun_*_figures directories
for p in sorted(RESULTS.iterdir()):
    if p.is_dir() and p.name.startswith("rerun_") and p.name.endswith("_figures"):
        dst = target / p.name
        try:
            shutil.copytree(p, dst)
            copied.append(dst.relative_to(ROOT))
        except FileExistsError:
            pass
# copy selection CSVs if present
sel_folder = RESULTS / 'analysis' / 'batches'
if sel_folder.exists():
    for f in ['rerun_selection_lt5.csv', 'rerun_selection_lt20.csv', 'rerun_selection_all.csv']:
        src = sel_folder / f
        if src.exists():
            dst_dir = target / 'analysis_batches'
            dst_dir.mkdir(exist_ok=True)
            shutil.copy2(src, dst_dir / src.name)
            copied.append((dst_dir / src.name).relative_to(ROOT))
# copy the current runner for reproducibility
runner = ROOT / 'experiments' / 'run_reruns_selected.py'
if runner.exists():
    shutil.copy2(runner, target / runner.name)
    copied.append((target / runner.name).relative_to(ROOT))

print('Target folder:', target)
print('Copied files:')
for c in copied:
    print('-', c)
print('\nDone.')
