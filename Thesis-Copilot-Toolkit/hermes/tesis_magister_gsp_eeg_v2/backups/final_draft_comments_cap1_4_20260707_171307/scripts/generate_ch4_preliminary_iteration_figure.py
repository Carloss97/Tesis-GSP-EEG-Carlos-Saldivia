#!/usr/bin/env python3
"""Generate the preliminary-iteration summary figure for Chapter 4.

Uses the consolidated phase-2 iteration pivot. Visibility NNK is excluded because
its implementation was later found invalid; it is not used for conclusions.
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import csv
import math

import matplotlib.pyplot as plt

ROOT = Path('/mnt/c/Users/sarlo/OneDrive/Escritorio/Proyectos/Tesis-GSP-EEG-Carlos-Saldivia/Thesis-Copilot-Toolkit')
THESIS = ROOT / 'hermes/tesis_magister_gsp_eeg_v2'
FIGURES = THESIS / 'figures'
LOGS = THESIS / 'build_logs'

LABELS = {
    'bgsrp': 'BGSRP',
    'ica': 'ICA',
    'idw': 'IDW',
    'linear': 'Lineal',
    'rbfi_tps': 'RBF TPS',
    'sobolev': 'Sobolev',
    'spherical_spline': 'Spline esférica',
    'temporal_laplacian': 'Lap. temporal',
    'tikhonov': 'Tikhonov',
    'trss': 'TRSS',
    'tv': 'TV',
}


def median(xs: list[float]) -> float:
    xs = sorted(xs)
    n = len(xs)
    return xs[n // 2] if n % 2 else 0.5 * (xs[n // 2 - 1] + xs[n // 2])


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    LOGS.mkdir(parents=True, exist_ok=True)

    pivot = ROOT / 'results/tablas_resumen/phase2_iteration_metrics_pivot.csv'
    vals: dict[str, list[float]] = defaultdict(list)
    iterations: set[str] = set()
    with pivot.open(newline='', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        methods = [m for m in (reader.fieldnames or []) if m != 'iteration']
        for row in reader:
            iterations.add(row['iteration'])
            for method in methods:
                if method == 'visibility_nnk':
                    continue
                raw = (row.get(method) or '').strip()
                if not raw:
                    continue
                try:
                    value = float(raw)
                except ValueError:
                    continue
                if math.isfinite(value):
                    vals[method].append(value)

    items = [(m, median(v), len(v)) for m, v in vals.items() if v]
    items.sort(key=lambda x: x[1])
    comparable = [x for x in items if x[0] != 'sobolev']
    outlier = [x for x in items if x[0] == 'sobolev']

    plt.rcParams.update({'font.size': 8, 'axes.titlesize': 10, 'axes.labelsize': 8})
    fig, axes = plt.subplots(
        2,
        1,
        figsize=(7.2, 4.7),
        gridspec_kw={'height_ratios': [4.2, 0.9]},
        constrained_layout=True,
    )

    ax = axes[0]
    methods = [x[0] for x in comparable]
    med = [x[1] for x in comparable]
    counts = [x[2] for x in comparable]
    y = list(range(len(methods)))
    ax.barh(y, med, color='#0072B2', edgecolor='#333333', linewidth=0.4)
    ax.set_yticks(y)
    ax.set_yticklabels([LABELS.get(m, m) for m in methods])
    ax.invert_yaxis()
    ax.set_xlabel('MAE mediano exploratorio (menor es mejor)')
    ax.set_title('Exploración preliminar: métodos consolidados por MAE')
    ax.grid(axis='x', color='#dddddd', linewidth=0.6)
    if med:
        ax.set_xlim(0, max(med) * 1.25)
    for yi, value, n in zip(y, med, counts):
        ax.text(value, yi, f'  n={n}', va='center', ha='left', fontsize=7)

    ax2 = axes[1]
    if outlier:
        method, value, n = outlier[0]
        ax2.barh([0], [value], color='#999999', edgecolor='#333333', linewidth=0.4)
        ax2.set_yticks([0])
        ax2.set_yticklabels([LABELS.get(method, method)])
        ax2.set_xlabel('Outlier de MAE mediano exploratorio')
        ax2.grid(axis='x', color='#dddddd', linewidth=0.6)
        ax2.set_xlim(0, value * 1.18)
        ax2.text(value, 0, f'  n={n}', va='center', ha='left', fontsize=7)
    else:
        ax2.axis('off')

    out = FIGURES / 'ch4_preliminary_iteration_summary.pdf'
    fig.savefig(out, bbox_inches='tight', pad_inches=0.04)
    plt.close(fig)

    with (LOGS / 'cap4_preliminary_iteration_summary_manifest.txt').open('w', encoding='utf-8') as f:
        f.write(f'source={pivot}\n')
        f.write(f'iterations_with_any_metric={len(iterations)}\n')
        f.write('excluded=visibility_nnk (implementation error; not used for conclusions)\n')
        for method, value, n in items:
            f.write(f'{method},median_mae={value},n={n}\n')

    print(out)
    print('iterations_with_any_metric', len(iterations))
    print('methods', len(items))


if __name__ == '__main__':
    main()
