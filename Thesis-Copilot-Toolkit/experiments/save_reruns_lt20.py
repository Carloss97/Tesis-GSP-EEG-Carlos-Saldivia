#!/usr/bin/env python3
"""
Copy all rerun artifacts found in `results/` into a timestamped folder.
This script collects files named `rerun_*_raw.csv` and associated artifacts.
"""
from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"

stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
target = RESULTS / f"reruns_lt20_{stamp}"
target.mkdir(parents=True, exist_ok=True)

copied = []
raw_files = sorted(RESULTS.glob('rerun_*_raw.csv'))
for raw in raw_files:
    tag = raw.name.replace('_raw.csv', '')
    patterns = [
        f"{tag}_raw.csv",
        f"{tag}_stats.csv",
        f"{tag}_significance.csv",
        f"{tag}_qa_report.md",
        f"{tag}_run_metadata.json",
        f"{tag}_integration_log.md",
    ]
    for p in patterns:
        src = RESULTS / p
        if src.exists():
            dst = target / src.name
            shutil.copy2(src, dst)
            copied.append(dst.relative_to(ROOT))
    figdir = RESULTS / f"{tag}_figures"
    if figdir.exists() and figdir.is_dir():
        dstf = target / figdir.name
        try:
            shutil.copytree(figdir, dstf)
            copied.append(dstf.relative_to(ROOT))
        except FileExistsError:
            pass

# copy selection CSV for reference if present
sel = RESULTS / 'analysis' / 'batches' / 'rerun_selection_lt20.csv'
if sel.exists():
    sel_dst_dir = target / 'analysis_batches'
    sel_dst_dir.mkdir(exist_ok=True)
    shutil.copy2(sel, sel_dst_dir / sel.name)
    copied.append((sel_dst_dir / sel.name).relative_to(ROOT))

# copy the generated runner for reproducibility
runner = ROOT / 'experiments' / 'run_reruns_selected.py'
if runner.exists():
    shutil.copy2(runner, target / runner.name)
    copied.append((target / runner.name).relative_to(ROOT))

print('Target folder:', target)
print('Copied files:')
for c in copied:
    print('-', c)

print('\nDone.')
