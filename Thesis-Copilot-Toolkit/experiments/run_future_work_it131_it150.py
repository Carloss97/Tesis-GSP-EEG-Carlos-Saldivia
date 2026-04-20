"""Run new iterations it131-it150 focused on real datasets and promising methods.

This script reuses the iteration engine implemented in
`run_future_work_it121_it130.py` by importing it as a module at runtime.

Usage examples:
  # dry run / light profile (recommended)
  python experiments/run_future_work_it131_it150.py --light-profile

  # run a subset
  python experiments/run_future_work_it131_it150.py --tags it131 it132 --light-profile

Careful: full runs (no --light-profile) will be computationally expensive.
"""
from __future__ import annotations

import argparse
import importlib.util
from dataclasses import replace
from pathlib import Path
from typing import Dict


ROOT = Path(__file__).resolve().parents[1]
BASE_SCRIPT = ROOT / "experiments" / "run_future_work_it121_it130.py"


def _load_base_module():
    spec = importlib.util.spec_from_file_location("run121130", str(BASE_SCRIPT))
    mod = importlib.util.module_from_spec(spec)
    loader = spec.loader
    assert loader is not None
    import sys

    # Ensure the module has an entry in sys.modules before executing
    # so decorators/dataclasses that inspect the module namespace work.
    sys.modules[spec.name] = mod
    loader.exec_module(mod)
    return mod


def _build_iteration_defs(base) -> Dict[str, object]:
    IterDef = base.IterDef
    real = [
        "physionet_real",
        "bci_iv2a_real_s1",
        "bci_iv2a_real_s2",
        "bci_iv2a_real_s3",
        "iv100hz_mat",
    ]

    # Runtime exclusions (2026-04-18): keep historical artifacts but avoid scheduling
    # these methods/datasets for new runs unless explicitly reviewed.
    # Also exclude legacy instant methods 'mean' and 'nearest' from scheduling.
    EXCLUDED_METHODS = {"heat_diffusion_temporal", "wavelet_temporal", "directed_tv", "mean", "nearest"}
    EXCLUDED_DATASETS = {"iv100hz_mat"}
    # Filter the default real dataset list to avoid the excluded datasets
    real = [d for d in real if d not in EXCLUDED_DATASETS]

    defs = [
        IterDef("it131", "it131_heatdiff_trss_directed_tv_real", "Compare heat-diffusion, TRSS and directed-TV on real EEG", "Phase 19: Focused real-data comparison", "Compare `heat_diffusion_temporal`, `trss`, and `directed_tv` on clinical/BCI datasets.", real, seeds=list(range(6)), graph_specs=[("knn", {"k": 3}), ("gaussian", {"sigma": 1.0}), ("kalofolias", {})], missing_list=[0.1, 0.2, 0.3], methods=["heat_diffusion_temporal", "trss", "directed_tv", "tv", "linear"]),

        IterDef("it132", "it132_trss_hyperparam_sweep", "TRSS hyperparameter sweep (lambda/alpha) on real data", "Phase 19: Hyperparam tuning", "Grid-search TRSS alpha/beta via lambda-mode proxy (TV-family grid)", ["physionet_real", "bci_iv2a_real_s1", "iv100hz_mat"], mode="lambda", seeds=list(range(4)), graph_specs=[("knn", {"k": 3})], lambdas=[0.05, 0.1, 0.2, 0.4]),

        IterDef("it133", "it133_directed_tv_iter_sweep", "Directed-TV iteration sweep", "Phase 19: Temporal method tuning", "Assess directed-TV sensitivity to iteration counts and missing ratios", real, seeds=list(range(6)), graph_specs=[("knn", {"k": 3}), ("gaussian", {"sigma": 1.0})], missing_list=[0.1, 0.2, 0.3, 0.4], methods=["directed_tv"]),

        IterDef("it134", "it134_bci_holdout_subjectwise_detailed", "BCI subject-wise holdout (detailed)", "Phase 19: BCI holdout", "Per-subject holdout robustness for top methods", ["bci_iv2a_real_s1", "bci_iv2a_real_s2", "bci_iv2a_real_s3"], seeds=list(range(8)), graph_specs=[("knn", {"k": 3})], missing_list=[0.1, 0.2, 0.3], methods=["trss", "directed_tv", "heat_diffusion_temporal"]),

        IterDef("it135", "it135_physionet_long_seeds", "Physionet stability with extended seeds", "Phase 20: Stability", "Increase seeds for physionet to assess variability", ["physionet_real"], seeds=list(range(12)), graph_specs=[("knn", {"k": 3})], missing_list=[0.1, 0.2, 0.3], methods=["trss", "heat_diffusion_temporal", "tv"]),

        IterDef("it136", "it136_runtime_profiling_real", "Runtime profiling for top methods on real datasets", "Phase 20: Practicality", "Collect runtime statistics for candidate methods", real, seeds=list(range(3)), graph_specs=[("knn", {"k": 3})], missing_list=[0.2], methods=["trss", "heat_diffusion_temporal", "tv", "linear"]),

        IterDef("it137", "it137_heatdiff_graph_variants", "Heat-diffusion across graph constructors", "Phase 20: Graph sensitivity", "Evaluate `heat_diffusion_temporal` with several graph constructors", real, seeds=list(range(5)), graph_specs=[("knn", {"k": 3}), ("knn", {"k": 5}), ("gaussian", {"sigma": 0.6}), ("gaussian", {"sigma": 1.0}), ("kalofolias", {})], missing_list=[0.2, 0.3], methods=["heat_diffusion_temporal"]),

        IterDef("it138", "it138_tv_family_vs_instant_real", "TV-family vs Instant on real data", "Phase 20: Family comparison", "Compare TV/Time family against best instant methods on real datasets", real, seeds=list(range(5)), graph_specs=[("knn", {"k": 3})], missing_list=[0.1, 0.2, 0.3], methods=["trss", "tv", "graph_time_tikhonov", "linear"]),

        IterDef("it139", "it139_visibility_graphs_evaluation", "Visibility graphs methods evaluation", "Phase 20: Temporal grid", "Test `visibility_graphs`, `temporal_laplacian`, `sobolev_temporal` against heat-diffusion", real, seeds=list(range(4)), graph_specs=[("knn", {"k": 3})], missing_list=[0.1, 0.2], methods=["visibility_graphs", "temporal_laplacian", "sobolev_temporal", "heat_diffusion_temporal"]),

        IterDef("it140", "it140_puy_vs_trss_real", "Puy vs TRSS on real datasets", "Phase 20: Method contrast", "Compare `puy` with `trss` on clinical/BCI datasets", real, seeds=list(range(6)), graph_specs=[("knn", {"k": 3})], missing_list=[0.1, 0.2, 0.3], methods=["puy", "trss"]),

        IterDef("it141", "it141_multiobjective_real_pareto", "Multiobjective Pareto on real datasets", "Phase 21: Multiobjective", "Collect MAE/RMSE/DTW/SNR/runtime for Pareto analysis", ["physionet_real", "bci_iv2a_real_s1"], seeds=list(range(5)), graph_specs=[("knn", {"k": 3}), ("gaussian", {"sigma": 1.0})], missing_list=[0.1, 0.2], methods=["trss", "tv", "heat_diffusion_temporal", "linear"]),

        IterDef("it142", "it142_confidence_bootstrap_real", "Bootstrap CI for key combos on real datasets", "Phase 21: CI stability", "Run with more seeds to enable bootstrap CI estimation per dataset", ["physionet_real", "bci_iv2a_real_s1", "iv100hz_mat"], seeds=list(range(10)), graph_specs=[("knn", {"k": 3})], missing_list=[0.2]),

        IterDef("it143", "it143_graph_density_real", "Graph density calibration for real data", "Phase 21: Graph calibration", "Sweep k and sigma for graphs on real datasets to check density sensitivity", real, seeds=list(range(4)), graph_specs=[("knn", {"k": 3}), ("knn", {"k": 5}), ("knn", {"k": 7}), ("gaussian", {"sigma": 0.6}), ("gaussian", {"sigma": 1.0})], missing_list=[0.2, 0.3], methods=["trss", "heat_diffusion_temporal"]),

        IterDef("it144", "it144_noise_robustness_real", "Noise robustness (non-gaussian) on real data", "Phase 21: Noise", "Stress-test selected methods under SNR variations", ["physionet_real", "iv100hz_mat"], mode="noise", seeds=list(range(4)), snr_levels=[25.0, 15.0, 5.0, 0.0, -5.0], graph_specs=[("knn", {"k": 3})], methods=["trss", "heat_diffusion_temporal", "tv"]),

        IterDef("it145", "it145_temporal_methods_grid", "Temporal-methods grid on real datasets", "Phase 22: Temporal exploration", "Grid over temporal solvers (sobolev_temporal, heat_diffusion, visibility_graphs)", real, seeds=list(range(4)), graph_specs=[("knn", {"k": 3})], missing_list=[0.1, 0.2], methods=["sobolev_temporal", "heat_diffusion_temporal", "visibility_graphs", "temporal_laplacian"]),

        IterDef("it146", "it146_directed_tv_low_missing", "Directed TV focused on low missing ratios", "Phase 22: Low-MR focus", "Assess directed-TV advantage under mild missingness", real, seeds=list(range(6)), graph_specs=[("knn", {"k": 3})], missing_list=[0.05, 0.1], methods=["directed_tv", "trss", "heat_diffusion_temporal"]),

        IterDef("it147", "it147_trss_high_missing", "TRSS under high missingness", "Phase 22: Stress missingness", "Evaluate TRSS in high missing ratios (hard case)", real, seeds=list(range(6)), graph_specs=[("knn", {"k": 3})], missing_list=[0.3, 0.4], methods=["trss"]),

        IterDef("it148", "it148_holdout_physionet_runs", "Physionet run/session holdout", "Phase 22: Holdout analysis", "Perform run/session holdout analysis (proxy) on physionet to test generalization", ["physionet_real"], seeds=list(range(6)), graph_specs=[("knn", {"k": 3})], missing_list=[0.2], methods=["trss", "heat_diffusion_temporal"]),

        IterDef("it149", "it149_synthetic_real_transfer", "Transfer of tuned hyperparams from real to synthetic", "Phase 23: Transfer test", "Apply best hyperparams from real datasets to synthetic proxies to test transfer", ["physionet_real", "synthetic_alpha", "synthetic_beta"], seeds=list(range(4)), graph_specs=[("knn", {"k": 3})], missing_list=[0.2], methods=["trss", "heat_diffusion_temporal"]),

        IterDef("it150", "it150_decision_matrix_update", "Update decision matrix after focused experiments", "Phase 23: Decision update", "Aggregate focused experiments and emit conditional decision matrix for final recommendation", ["physionet_real", "bci_iv2a_real_s1", "bci_iv2a_real_s2"], seeds=list(range(4)), graph_specs=[("knn", {"k": 3})], missing_list=[0.2]),
    ]

    # Remove excluded methods from per-iteration method lists to avoid accidental reruns.
    for it in defs:
        if getattr(it, "methods", None):
            it.methods = [m for m in it.methods if m not in EXCLUDED_METHODS]
        if getattr(it, "datasets", None):
            it.datasets = [d for d in it.datasets if d not in EXCLUDED_DATASETS]

    return {it.key: it for it in defs}


def main():
    base = _load_base_module()
    defs = _build_iteration_defs(base)
    keys = list(defs.keys())

    parser = argparse.ArgumentParser(description="Run focused future-work iterations it131-it150")
    parser.add_argument("--tags", nargs="+", default=keys, choices=keys, help="Subset of iterations to run.")
    parser.add_argument("--stop-on-error", action="store_true", help="Stop on first error.")
    parser.add_argument("--light-profile", action="store_true", help="Use reduced seeds/graphs for faster execution.")
    args = parser.parse_args()

    # Check data availability via base module helper
    check = base.load_data_availability()
    availability = check["availability"]
    data = check["data"]

    failed = []
    completed = []

    for k in args.tags:
        it = defs[k]
        if args.light_profile:
            it = replace(
                it,
                seeds=[0, 1],
                missing_list=[0.2] if it.mode == "base" else it.missing_list,
                methods=list(base.BASELINE_METHODS) + ["tikhonov", "tv", "trss"] if it.mode in {"base", "noise"} else it.methods,
                graph_specs=it.graph_specs[:1],
                lambdas=it.lambdas[:3],
                snr_levels=it.snr_levels[:3],
            )
        try:
            base._run_iteration(it, availability, data, operational_close_profile=False)
            completed.append(k)
            print(f"[OK] {k}")
        except Exception as exc:
            failed.append({"iteration": k, "error": str(exc)})
            print(f"[SKIPPED] {k}: {exc}")
            if args.stop_on_error:
                raise

    if failed:
        (base.RESULTS / "it131_it150_skipped_iterations.json").write_text(
            base.json.dumps(failed, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    print("Completed:", ",".join(completed))
    if failed:
        print("Skipped:", ",".join([f["iteration"] for f in failed]))


if __name__ == "__main__":
    main()
