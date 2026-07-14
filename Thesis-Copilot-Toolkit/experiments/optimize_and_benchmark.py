"""Parameter optimization and benchmark with method-family split.

Families:
- instant: methods that reconstruct each time instant independently.
- tv_time: methods that explicitly model temporal/TV structure.
"""

from __future__ import annotations

import itertools
import json
import os
from pathlib import Path
from typing import Any, Callable, Dict, List

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from src.data.data_loader import load_mne_sample_dataset, load_synthetic_eeg
from src.evaluation import evaluate_signals
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals
from src.interpolation_warning_registry import clear_registry, summarize_registry


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


def build_dataset_registry(include_mne: bool) -> Dict[str, Callable[[], Dict[str, Any]]]:
    ds = {
        "synthetic": lambda: load_synthetic_eeg(n_channels=22, n_times=260, random_state=42),
    }
    if include_mne:
        ds["mne_sample"] = load_mne_sample_dataset
    return ds


def parse_csv_env_list(env_name: str, cast=float) -> List:
    raw = os.environ.get(env_name, "").strip()
    if not raw:
        return []
    return [cast(x.strip()) for x in raw.split(",") if x.strip()]


def _safe_index_group(indices: np.ndarray, n_channels: int, target_min: int = 2) -> List[int]:
    uniq = sorted({int(i) for i in indices if 0 <= int(i) < n_channels})
    if len(uniq) >= target_min:
        return uniq
    if not uniq:
        return list(range(min(target_min, n_channels)))
    out = list(uniq)
    for idx in range(n_channels):
        if idx not in out:
            out.append(idx)
        if len(out) >= target_min:
            break
    return out


def build_realistic_scenarios(positions: np.ndarray, ch_names: List[str]) -> List[Dict[str, Any]]:
    n_channels = int(positions.shape[0])
    x = positions[:, 0]
    y = positions[:, 1]

    frontal_idx = np.where(y >= np.quantile(y, 0.65))[0]
    occipital_idx = np.where(y <= np.quantile(y, 0.35))[0]
    lateral_left_idx = np.where(x <= np.quantile(x, 0.30))[0]
    lateral_right_idx = np.where(x >= np.quantile(x, 0.70))[0]
    midline_idx = np.where(np.abs(x) <= np.quantile(np.abs(x), 0.35))[0]

    scenarios = [
        {
            "scenario": "frontal_band",
            "region": "frontal",
            "electrode_type": "anterior",
            "base_indices": _safe_index_group(frontal_idx, n_channels),
        },
        {
            "scenario": "occipital_band",
            "region": "occipital",
            "electrode_type": "posterior",
            "base_indices": _safe_index_group(occipital_idx, n_channels),
        },
        {
            "scenario": "left_lateral_temporal",
            "region": "temporal",
            "electrode_type": "lateral_left",
            "base_indices": _safe_index_group(lateral_left_idx, n_channels),
        },
        {
            "scenario": "right_lateral_temporal",
            "region": "temporal",
            "electrode_type": "lateral_right",
            "base_indices": _safe_index_group(lateral_right_idx, n_channels),
        },
        {
            "scenario": "midline_central",
            "region": "central",
            "electrode_type": "midline",
            "base_indices": _safe_index_group(midline_idx, n_channels),
        },
    ]

    # Keep channel labels only for frozen protocol traceability.
    for sc in scenarios:
        sc["base_channel_names"] = [ch_names[i] if 0 <= i < len(ch_names) else f"Ch{i + 1}" for i in sc["base_indices"]]
    return scenarios


def apply_scenario_mask(
    signals: np.ndarray,
    base_indices: List[int],
    missing_ratio: float,
    seed: int,
) -> tuple[np.ndarray, List[int]]:
    n_channels = int(signals.shape[1])
    n_missing = max(1, int(round(n_channels * missing_ratio)))

    base = [idx for idx in base_indices if 0 <= idx < n_channels]
    selected = base[:n_missing]

    if len(selected) < n_missing:
        rng = np.random.default_rng(seed)
        candidates = [idx for idx in range(n_channels) if idx not in selected]
        needed = n_missing - len(selected)
        if needed > 0 and candidates:
            extra = rng.choice(candidates, size=min(needed, len(candidates)), replace=False)
            selected.extend(int(x) for x in extra)

    masked = signals.copy()
    masked[:, selected] = np.nan
    return masked, sorted(selected)


def stable_seed_from_text(text: str, base_seed: int) -> int:
    acc = base_seed
    for i, ch in enumerate(text):
        acc += (i + 1) * ord(ch)
    return int(acc)


def _ci95(std: pd.Series, n: pd.Series) -> pd.Series:
    return 1.96 * (std / np.sqrt(np.maximum(n, 1)))


def build_stat_summary(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    grouped = (
        df.groupby(["dataset", "scenario", "region", "electrode_type", "missing_ratio", "method", "family"], as_index=False)
        .agg(
            runs=("mae", "size"),
            mae_mean=("mae", "mean"),
            mae_std=("mae", "std"),
            rmse_mean=("rmse", "mean"),
            rmse_std=("rmse", "std"),
            dtw_mean=("dtw", "mean"),
            dtw_std=("dtw", "std"),
            snr_mean=("snr", "mean"),
            snr_std=("snr", "std"),
        )
        .fillna(0.0)
    )

    grouped["mae_ci95"] = _ci95(grouped["mae_std"], grouped["runs"])
    grouped["rmse_ci95"] = _ci95(grouped["rmse_std"], grouped["runs"])
    grouped["dtw_ci95"] = _ci95(grouped["dtw_std"], grouped["runs"])
    grouped["snr_ci95"] = _ci95(grouped["snr_std"], grouped["runs"])
    return grouped.sort_values(["dataset", "scenario", "missing_ratio", "mae_mean"]).reset_index(drop=True)


def build_topk_table(df_stats: pd.DataFrame, top_k: int) -> pd.DataFrame:
    if df_stats.empty:
        return pd.DataFrame()
    ranked = df_stats.sort_values(["dataset", "scenario", "missing_ratio", "family", "mae_mean", "dtw_mean"])
    return (
        ranked.groupby(["dataset", "scenario", "missing_ratio", "family"], as_index=False)
        .head(top_k)
        .reset_index(drop=True)
    )


def run_benchmark(
    include_mne: bool = True,
    max_time_samples: int = 220,
    missing_levels: List[float] | None = None,
    random_seed: int = 42,
) -> tuple[pd.DataFrame, Dict[str, Any]]:
    clear_registry()
    datasets = build_dataset_registry(include_mne)
    missing_levels = missing_levels or [0.10, 0.20, 0.30, 0.40]

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

    graph_filter = set(parse_csv_env_list("B2_GRAPH_NAMES", cast=str) or parse_csv_env_list("B1_GRAPH_NAMES", cast=str))
    method_filter = set(parse_csv_env_list("B2_METHOD_NAMES", cast=str) or parse_csv_env_list("B1_METHOD_NAMES", cast=str))
    max_scenarios = int(os.environ.get("B2_MAX_SCENARIOS", os.environ.get("B1_MAX_SCENARIOS", "5")))

    if graph_filter:
        graph_spaces = {k: v for k, v in graph_spaces.items() if k in graph_filter}
    if method_filter:
        method_spaces = {k: v for k, v in method_spaces.items() if k in method_filter}

    rows = []
    protocol_config: Dict[str, Any] = {
        "seed": random_seed,
        "missing_levels": [float(x) for x in missing_levels],
        "datasets": {},
        "metrics": ["mae", "rmse", "dtw", "snr"],
        "graph_names": list(graph_spaces.keys()),
        "method_names": list(method_spaces.keys()),
    }

    for ds_name, loader in datasets.items():
        sample = loader()
        signals = sample["signals"]
        positions = sample["positions"]
        info = sample.get("info", {})
        ch_names = list(info.get("ch_names", [f"Ch{i + 1}" for i in range(signals.shape[1])]))

        if signals.shape[0] > max_time_samples:
            signals = signals[:max_time_samples]

        scenarios = build_realistic_scenarios(positions, ch_names)[:max_scenarios]
        protocol_config["datasets"][ds_name] = {
            "n_channels": int(signals.shape[1]),
            "n_times": int(signals.shape[0]),
            "scenario_count": len(scenarios),
            "scenarios": scenarios,
        }

        for scenario in scenarios:
            scenario_name = scenario["scenario"]
            scenario_seed = stable_seed_from_text(f"{ds_name}:{scenario_name}", random_seed)

            for missing_ratio in missing_levels:
                ratio_seed = scenario_seed + int(missing_ratio * 1000)
                masked, selected_indices = apply_scenario_mask(
                    signals=signals,
                    base_indices=scenario["base_indices"],
                    missing_ratio=float(missing_ratio),
                    seed=ratio_seed,
                )

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

                                    met = evaluate_signals(signals, rec["reconstructed"], metrics=["mae", "rmse", "dtw", "snr"])
                                    rows.append(
                                        {
                                            "dataset": ds_name,
                                            "scenario": scenario_name,
                                            "region": scenario["region"],
                                            "electrode_type": scenario["electrode_type"],
                                            "missing_ratio": float(missing_ratio),
                                            "missing_count": int(len(selected_indices)),
                                            "missing_indices": ",".join(str(i) for i in selected_indices),
                                            "mask_seed": int(ratio_seed),
                                            "graph": graph_name,
                                            "graph_params": str(gparams),
                                            "method": method,
                                            "method_params": str(mparams),
                                            "family": method_family(method),
                                            "mae": met["mae"],
                                            "rmse": met["rmse"],
                                            "dtw": met["dtw"],
                                            "snr": met["snr"],
                                        }
                                    )
                                except Exception as exc:
                                    print(
                                        f"[WARN] method failed {ds_name}/{scenario_name}/{missing_ratio}/{graph_name}/{method}/{mparams}: {exc}"
                                    )
                                    continue

    return pd.DataFrame(rows), protocol_config


def save_outputs(
    df: pd.DataFrame,
    out_dir: Path,
    protocol_config: Dict[str, Any],
    artifact_prefix: str,
    top_k: int,
) -> None:
    full_csv = out_dir / "opt_benchmark_full.csv"
    df.to_csv(full_csv, index=False)

    raw_path = out_dir / f"{artifact_prefix}_raw.csv"
    summary_path = out_dir / f"{artifact_prefix}_summary.csv"
    cfg_path = out_dir / f"{artifact_prefix}_config.json"
    rank_path = out_dir / f"{artifact_prefix}_ranking_final.csv"
    topk_path = out_dir / f"{artifact_prefix}_topk_by_family_scenario.csv"
    warn_path = out_dir / f"{artifact_prefix}_warnings_registry.csv"

    df.to_csv(raw_path, index=False)
    cfg_path.write_text(json.dumps(protocol_config, indent=2), encoding="utf-8")

    # Keep B1 canonical files in sync when using B1 prefix.
    if artifact_prefix == "opt_benchmark_b1_protocol":
        df.to_csv(out_dir / "opt_benchmark_b1_protocol_raw.csv", index=False)
        (out_dir / "opt_benchmark_b1_protocol_config.json").write_text(
            json.dumps(protocol_config, indent=2),
            encoding="utf-8",
        )

    if df.empty:
        print("No results to save.")
        return

    rank_all = df.sort_values(["mae", "rmse", "dtw"], ascending=[True, True, True]).reset_index(drop=True)
    rank_all.to_csv(out_dir / "opt_benchmark_rank_all.csv", index=False)

    best_by_family = (
        df.sort_values(["mae", "rmse", "dtw"], ascending=[True, True, True])
        .groupby(["dataset", "scenario", "missing_ratio", "family"], as_index=False)
        .first()
    )
    best_by_family.to_csv(out_dir / "opt_benchmark_best_by_family.csv", index=False)

    best_by_method = (
        df.groupby(["dataset", "scenario", "missing_ratio", "graph", "method", "family"], as_index=False)
        .agg(mae=("mae", "mean"), rmse=("rmse", "mean"), dtw=("dtw", "mean"), snr=("snr", "mean"))
        .sort_values("mae")
    )
    best_by_method.to_csv(out_dir / "opt_benchmark_mean_by_method.csv", index=False)

    summary = build_stat_summary(df)
    summary.to_csv(summary_path, index=False)
    if artifact_prefix == "opt_benchmark_b1_protocol":
        summary.to_csv(out_dir / "opt_benchmark_b1_protocol_summary.csv", index=False)

    ranking = summary.sort_values(["mae_mean", "rmse_mean", "dtw_mean", "snr_mean"], ascending=[True, True, True, False])
    ranking.to_csv(rank_path, index=False)

    topk = build_topk_table(summary, top_k=top_k)
    topk.to_csv(topk_path, index=False)

    warnings_df = pd.DataFrame(summarize_registry(reset=True))
    if warnings_df.empty:
        warnings_df = pd.DataFrame(
            columns=["method", "warning_code", "severity", "decision", "count", "sample_message"]
        )
    warnings_df.to_csv(warn_path, index=False)

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
    missing_levels = parse_csv_env_list("B2_MISSING_LEVELS", cast=float) or parse_csv_env_list("B1_MISSING_LEVELS", cast=float) or [0.10, 0.20, 0.30, 0.40]
    random_seed = int(os.environ.get("B2_RANDOM_SEED", os.environ.get("B1_RANDOM_SEED", "42")))
    artifact_prefix = os.environ.get("B2_ARTIFACT_PREFIX", "opt_benchmark_b2_full_scale")
    top_k = int(os.environ.get("B2_TOP_K", "3"))

    out_dir = ensure_results_dir()
    df, protocol_config = run_benchmark(
        include_mne=include_mne,
        max_time_samples=max_time_samples,
        missing_levels=missing_levels,
        random_seed=random_seed,
    )
    protocol_config["artifact_prefix"] = artifact_prefix
    protocol_config["top_k"] = top_k
    save_outputs(df, out_dir, protocol_config, artifact_prefix=artifact_prefix, top_k=top_k)

    if not df.empty:
        print(df.sort_values("mae").head(25))
    print(f"Saved optimization outputs in: {out_dir}")


if __name__ == "__main__":
    main()
