#!/usr/bin/env python3
"""
Copy completed rerun artifacts into a timestamped folder for later analysis.
"""
from pathlib import Path
import shutil
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"

completed_tags = [
    'rerun_14_bci_iv2a_real_s1_gaussian__sigma1.0_trss',
    'rerun_15_bci_iv2a_real_s1_knn__k3_trss',
    'rerun_16_bci_iv2a_real_s2_gaussian__sigma1.0_trss',
    'rerun_17_bci_iv2a_real_s2_gaussian__sigma1.0_trss',
    'rerun_18_bci_iv2a_real_s2_gaussian__sigma1.0_trss',
    'rerun_19_bci_iv2a_real_s2_knn__k3_trss',
    'rerun_20_iris_graph_signal_gaussian__sigma1.0_trss',
    'rerun_21_iris_graph_signal_knn__k3_trss',
    'rerun_22_iv100hz_mat_knn__k3_trss',
    'rerun_35_iv100hz_mat_gaussian__sigma1.0_tv',
    'rerun_37_movielens_graph_signal_gaussian__sigma1.0_tv',
    'rerun_38_movielens_graph_signal_knn__k3_tv',
]

stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
target = RESULTS / f"reruns_lt5_{stamp}"
target.mkdir(parents=True, exist_ok=True)

copied = []
for tag in completed_tags:
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
        shutil.copytree(figdir, dstf)
        copied.append(dstf.relative_to(ROOT))

# copy selection CSV for reference
sel = RESULTS / 'analysis' / 'batches' / 'rerun_selection_lt5.csv'
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
