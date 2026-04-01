"""Parameter optimization and benchmark with method-family split.

Families:
- instant: methods that reconstruct each time instant independently.
- tv_time: methods that explicitly model temporal/TV structure.
"""

from __future__ import annotations

import itertools
import os
from pathlib import Path
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from src.data.data_loader import load_mne_sample_dataset, load_synthetic_eeg, simulate_missing_channels
from src.evaluation import evaluate_signals
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals


INSTANT_METHODS = {
    "linear",
    "nearest",
    "mean",
    "random",
    "idw",
    "spherical_spline",
    "rbfi_tps",
    "rbfi_mq",
    "spline_surface",
    "gsp",
    "tikhonov",
    "bgsrp",
    "gsmooth",
    "puy",
    "sobolev",
}

TV_TIME_METHODS = {
    "graph_time_tikhonov",
    "trss",
    "tv",
}

GRAPH_BASED = {
    "gsp",
    "tikhonov",
    "bgsrp",
    "gsmooth",
    "graph_time_tikhonov",
    "trss",
    "tv",
    "puy",
    "sobolev",
}

POSITION_BASED = {
    "idw",
    "spherical_spline",
    "rbfi_tps",
    "rbfi_mq",
    "spline_surface",
}


def ensure_results_dir() -> Path:
    root = Path(__file__).resolve().parents[1]
    out_dir = root / "results"
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def expand_grid(grid: Dict[str, List]) -> List[Dict]:
    keys = list(grid.keys())
    vals = [grid[k] for k in keys]
    combos = []
    for tup in itertools.product(*vals):
        combos.append({k: v for k, v in zip(keys, tup)})
    return combos


def method_family(method: str) -> str:
    if method in TV_TIME_METHODS:
        return "tv_time"
    return "instant"


def build_dataset_registry(include_mne: bool) -> Dict[str, callable]:
    ds = {
        "synthetic": lambda: load_synthetic_eeg(n_channels=22, n_times=260, random_state=42),
    }
    if include_mne:
        ds["mne_sample"] = load_mne_sample_dataset
    return ds


def run_benchmark(include_mne: bool = True, max_time_samples: int = 220) -> pd.DataFrame:
    datasets = build_dataset_registry(include_mne)

    graph_spaces = {
        "knn": {"k": [4, 6]},
        "knng": {"k": [4, 6], "sigma": [0.8, 1.0]},
        "vknng": {"k": [4, 6], "alpha": [0.8, 1.0], "k_min": [2], "k_max": [8]},
        "gaussian": {"sigma": [0.8, 1.0, 1.2]},
        "nnk": {"k": [5, 7], "backend": ["internal"], "reg": [1e-6]},
        "aew": {"k": [4, 6], "sigma_dist": [1.0], "sigma_corr": [0.4, 0.6]},
        "kalofolias": {"a": [0.8, 1.0], "b": [0.8, 1.2], "max_iter": [300]},
    }

    method_spaces = {
        "linear": [{}],
        "idw": expand_grid({"power": [1.5, 2.0, 3.0]}),
        "rbfi_tps": [{}],
        "rbfi_mq": [{}],
        "spherical_spline": [{}],
        "gsp": [{}],
        "tikhonov": expand_grid({"alpha": [0.1, 0.5, 1.0]}),
        "bgsrp": expand_grid({"bandwidth": [4, 6, 8]}),
        "gsmooth": expand_grid({"lam": [0.3, 0.5, 0.7], "n_iter": [40]}),
        "graph_time_tikhonov": expand_grid({"alpha": [0.3, 0.7], "beta": [0.05, 0.15]}),
        "trss": expand_grid({"alpha": [0.6, 0.9], "beta": [0.1, 0.2], "n_iter": [80], "lr": [0.03]}),
        "tv": expand_grid({"lam": [0.1, 0.2, 0.4], "n_iter": [20], "eps": [1e-5]}),
    }

    rows = []

    for ds_name, loader in datasets.items():
        sample = loader()
        signals = sample["signals"]
        positions = sample["positions"]

        if signals.shape[0] > max_time_samples:
            signals = signals[:max_time_samples]

        masked = simulate_missing_channels(signals, missing_ratio=0.2, random_state=42)

        for graph_name, grid in graph_spaces.items():
            graph_param_list = expand_grid(grid)
            for gparams in graph_param_list:
                try:
                    graph = build_graph(graph_name, positions, signals=signals, **gparams)
                    adjacency = graph["adjacency"]
                    if hasattr(adjacency, "toarray"):
                        adjacency = adjacency.toarray()
                except Exception as exc:
                    print(f"[WARN] graph failed {ds_name}/{graph_name}/{gparams}: {exc}")
                    continue

                for method, param_list in method_spaces.items():
                    for mparams in param_list:
                        try:
                            if method in GRAPH_BASED:
                                rec = interpolate_signals(method, masked, adjacency=adjacency, **mparams)
                            elif method in POSITION_BASED:
                                rec = interpolate_signals(method, masked, positions=positions, **mparams)
                            else:
                                rec = interpolate_signals(method, masked, **mparams)

                            met = evaluate_signals(signals, rec["reconstructed"], metrics=["mae", "rmse", "snr"])
                            rows.append(
                                {
                                    "dataset": ds_name,
                                    "graph": graph_name,
                                    "graph_params": str(gparams),
                                    "method": method,
                                    "method_params": str(mparams),
                                    "family": method_family(method),
                                    "mae": met["mae"],
                                    "rmse": met["rmse"],
                                    "snr": met["snr"],
                                }
                            )
                        except Exception as exc:
                            print(f"[WARN] method failed {ds_name}/{graph_name}/{method}/{mparams}: {exc}")
                            continue

    return pd.DataFrame(rows)


def save_outputs(df: pd.DataFrame, out_dir: Path) -> None:
    full_csv = out_dir / "opt_benchmark_full.csv"
    df.to_csv(full_csv, index=False)

    if df.empty:
        print("No results to save.")
        return

    rank_all = df.sort_values(["mae", "rmse"], ascending=[True, True]).reset_index(drop=True)
    rank_all.to_csv(out_dir / "opt_benchmark_rank_all.csv", index=False)

    best_by_family = (
        df.sort_values(["mae", "rmse"], ascending=[True, True])
        .groupby(["dataset", "family"], as_index=False)
        .first()
    )
    best_by_family.to_csv(out_dir / "opt_benchmark_best_by_family.csv", index=False)

    best_by_method = (
        df.groupby(["dataset", "graph", "method", "family"], as_index=False)
        .agg(mae=("mae", "mean"), rmse=("rmse", "mean"), snr=("snr", "mean"))
        .sort_values("mae")
    )
    best_by_method.to_csv(out_dir / "opt_benchmark_mean_by_method.csv", index=False)

    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x="family", y="mae", hue="dataset")
    plt.title("MAE distribution by family")
    plt.tight_layout()
    plt.savefig(out_dir / "opt_family_mae_boxplot.png", dpi=180)
    plt.close()

    pivot = (
        df.groupby(["graph", "method"], as_index=False)["mae"]
        .mean()
        .pivot(index="method", columns="graph", values="mae")
    )
    plt.figure(figsize=(11, 8))
    sns.heatmap(pivot, annot=False, cmap="viridis")
    plt.title("Mean MAE by method and graph")
    plt.tight_layout()
    plt.savefig(out_dir / "opt_heatmap_mae_graph_method.png", dpi=180)
    plt.close()


def main() -> None:
    include_mne = os.environ.get("INCLUDE_MNE", "1") == "1"
    max_time_samples = int(os.environ.get("MAX_TIME_SAMPLES", "220"))

    out_dir = ensure_results_dir()
    df = run_benchmark(include_mne=include_mne, max_time_samples=max_time_samples)
    save_outputs(df, out_dir)

    if not df.empty:
        print(df.sort_values("mae").head(25))
    print(f"Saved optimization outputs in: {out_dir}")


if __name__ == "__main__":
    main()
