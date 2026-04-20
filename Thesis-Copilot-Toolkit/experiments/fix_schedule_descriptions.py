"""Fix and enrich the it01-it50 schedule descriptions and methods.

This script updates each iteration entry to ensure:
- A more informative `description` and `objective`.
- At least a small set of non-baseline candidate methods are present.

Run from the repo root. It overwrites the schedule file but creates a .bak copy first.
"""
from pathlib import Path
import json

SCHEDULE = Path(__file__).resolve().parent / "schedules" / "it01-it50_schedule_final.json"

BASELINES = ["linear", "ica", "spherical_spline", "rbfi_tps"]
CANONICAL_CANDIDATES = [
    "gsp",
    "tikhonov",
    "tv",
    "trss",
    "bgsrp",
    "gsmooth",
    "idw",
    "knn",
    "nnk",
    "gaussian",
    "kalofolias",
    "sobolev_temporal",
    "graph_time_tikhonov",
    "temporal_laplacian",
]

# Methods to explicitly exclude from candidate lists
EXCLUDE = ["mean", "nearest", "directed_tv", "heat_diffusion_temporal", "wavelet_temporal"]

MIN_NONBASELINE = 3


def ensure_methods_list(methods):
    methods = list(dict.fromkeys(methods or []))
    # remove excluded
    methods = [m for m in methods if m not in EXCLUDE]
    non_baselines = [m for m in methods if m not in BASELINES]
    if len(non_baselines) >= MIN_NONBASELINE:
        return methods

    # Augment with canonical candidates while preserving existing order
    for c in CANONICAL_CANDIDATES:
        if c in EXCLUDE:
            continue
        if c not in methods:
            methods.append(c)
        non_baselines = [m for m in methods if m not in BASELINES]
        if len(non_baselines) >= MIN_NONBASELINE:
            break

    return methods


def main():
    if not SCHEDULE.exists():
        raise SystemExit(f"Schedule file not found: {SCHEDULE}")

    # backup
    bak = SCHEDULE.with_suffix('.json.bak')
    if not bak.exists():
        bak.write_text(SCHEDULE.read_text(encoding='utf-8'), encoding='utf-8')

    data = json.loads(SCHEDULE.read_text(encoding='utf-8'))
    iters = data.get('iterations', [])
    for it in iters:
        tag = it.get('tag') or it.get('key')
        datasets = it.get('datasets', [])
        ds_str = ', '.join(datasets) if datasets else 'mixed datasets'

        # update description/objective
        it['description'] = f"{tag} — Evaluate {ds_str}; compare baselines and candidate temporal/spatial methods"
        it['objective'] = (
            "Compare candidate methods (trss, tv, tikhonov, graph_time_tikhonov, "
            "temporal_laplacian, gsp, bgsrp) vs canonical baselines; ensure at least "
            f"{MIN_NONBASELINE} non-baseline methods are present."
        )

        # ensure methods include at least a few non-baselines
        orig_methods = it.get('methods', [])
        it['methods'] = ensure_methods_list(orig_methods)

        # keep fase if present, otherwise set to Phase A
        it.setdefault('fase', 'Phase A')

    data['iterations'] = iters
    SCHEDULE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Updated schedule: {SCHEDULE} (backup: {bak})")


if __name__ == '__main__':
    main()
