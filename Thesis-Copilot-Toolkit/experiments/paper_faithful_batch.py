"""Extended experiment batch with saved artifacts for graph-based analysis."""

import os
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from src.data.data_loader import load_mne_sample_dataset, load_synthetic_eeg, simulate_missing_channels
from src.evaluation import evaluate_signals
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals


def ensure_results_dir() -> Path:
    root = Path(__file__).resolve().parents[1]
    results_dir = root / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    return results_dir


def run_batch(include_mne: bool = True) -> pd.DataFrame:
    datasets = {
        "synthetic": lambda: load_synthetic_eeg(n_channels=22, n_times=250, random_state=42),
    }
    if include_mne:
        datasets["mne_sample"] = load_mne_sample_dataset

    graph_methods = [
        ("knn", {"k": 4}),
        ("knng", {"k": 6, "sigma": 0.9}),
        ("vknng", {"k": 5, "alpha": 1.0, "k_min": 3, "k_max": 9}),
        ("gaussian", {"sigma": 1.0}),
        ("nnk", {"k": 6, "backend": "internal", "reg": 1e-6}),
        ("aew", {"k": 5, "sigma_dist": 1.0, "sigma_corr": 0.5}),
        ("kalofolias", {}),
    ]

    interpolators = [
        "linear",
        "idw",
        "rbfi_tps",
        "rbfi_mq",
        "spline_surface",
        "spherical_spline",
        "gsp",
        "tikhonov",
        "bgsrp",
        "gsmooth",
        "graph_time_tikhonov",
        "trss",
        "tv",
        "puy",
        "sobolev",
    ]

    graph_based = {
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
    position_based = {"idw", "rbfi_tps", "rbfi_mq", "spline_surface", "spherical_spline"}

    rows = []
    for ds_name, loader in datasets.items():
        sample = loader()
        signals = sample["signals"]
        positions = sample["positions"]

        # Limit sample size in heavy datasets to keep run time bounded.
        max_rows = int(os.environ.get("MAX_TIME_SAMPLES", "250"))
        if signals.shape[0] > max_rows:
            signals = signals[:max_rows]

        masked = simulate_missing_channels(signals, missing_ratio=0.2, random_state=42)

        for graph_name, graph_params in graph_methods:
            try:
                graph = build_graph(graph_name, positions, signals=signals, **graph_params)
                adjacency = graph["adjacency"]
                if hasattr(adjacency, "toarray"):
                    adjacency = adjacency.toarray()
            except Exception as exc:
                print(f"[WARN] Graph failed {ds_name}/{graph_name}: {exc}")
                continue

            for interp in interpolators:
                try:
                    if interp in graph_based:
                        rec = interpolate_signals(interp, masked, adjacency=adjacency)
                    elif interp in position_based:
                        rec = interpolate_signals(interp, masked, positions=positions)
                    else:
                        rec = interpolate_signals(interp, masked)

                    metrics = evaluate_signals(signals, rec["reconstructed"], metrics=["mae", "rmse", "snr"])
                    rows.append(
                        {
                            "dataset": ds_name,
                            "graph": graph_name,
                            "method": interp,
                            "mae": metrics["mae"],
                            "rmse": metrics["rmse"],
                            "snr": metrics["snr"],
                        }
                    )
                except Exception as exc:
                    print(f"[WARN] Interpolator failed {ds_name}/{graph_name}/{interp}: {exc}")
                    continue

    return pd.DataFrame(rows)


def save_artifacts(df: pd.DataFrame, out_dir: Path) -> None:
    csv_path = out_dir / "paper_faithful_results.csv"
    df.to_csv(csv_path, index=False)

    if df.empty:
        print("No results generated.")
        return

    rank_mae = df.sort_values("mae").reset_index(drop=True)
    rank_mae.to_csv(out_dir / "paper_faithful_rank_mae.csv", index=False)

    plt.figure(figsize=(14, 6))
    sns.boxplot(data=df, x="method", y="mae", hue="dataset")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(out_dir / "mae_by_method_dataset.png", dpi=180)
    plt.close()

    pivot = df.pivot_table(index="method", columns="graph", values="mae", aggfunc="mean")
    plt.figure(figsize=(10, 8))
    sns.heatmap(pivot, annot=True, fmt=".3f", cmap="viridis")
    plt.title("MAE mean by Interpolator vs Graph")
    plt.tight_layout()
    plt.savefig(out_dir / "heatmap_mae_method_graph.png", dpi=180)
    plt.close()

    pivot_snr = df.pivot_table(index="method", columns="graph", values="snr", aggfunc="mean")
    plt.figure(figsize=(10, 8))
    sns.heatmap(pivot_snr, annot=True, fmt=".2f", cmap="magma")
    plt.title("SNR mean by Interpolator vs Graph")
    plt.tight_layout()
    plt.savefig(out_dir / "heatmap_snr_method_graph.png", dpi=180)
    plt.close()


if __name__ == "__main__":
    include_mne = os.environ.get("INCLUDE_MNE", "1") == "1"
    out_dir = ensure_results_dir()
    df_results = run_batch(include_mne=include_mne)
    save_artifacts(df_results, out_dir)
    print(df_results.sort_values("mae").head(20))
    print(f"Saved artifacts in: {out_dir}")
