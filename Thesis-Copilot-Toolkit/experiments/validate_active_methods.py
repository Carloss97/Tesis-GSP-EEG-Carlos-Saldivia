"""Validate active interpolation methods and export closure artifacts."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from src.data.data_loader import load_synthetic_eeg, simulate_missing_channels
from src.evaluation import evaluate_signals
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals

ACTIVE_METHODS = [
    # INS-xx
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
    "gsmooth",
    "bgsrp",
    "puy",
    "sobolev",
    # TVT-xx
    "graph_time_tikhonov",
    "trss",
    "sobolev_temporal",
    "tv",
    "temporal_laplacian",
    "spline_temporal",
    "directed_tv",
    "adaptive_temporal",
]

GRAPH_METHOD = "knng"

POSITION_BASED = {
    "idw",
    "spherical_spline",
    "rbfi_tps",
    "rbfi_mq",
    "spline_surface",
}

GRAPH_BASED = {
    "gsp",
    "tikhonov",
    "gsmooth",
    "bgsrp",
    "puy",
    "sobolev",
    "graph_time_tikhonov",
    "trss",
    "sobolev_temporal",
    "tv",
    "temporal_laplacian",
    "spline_temporal",
    "directed_tv",
    "adaptive_temporal",
}

METHOD_PARAMS = {
    "random": {"random_state": 42},
    "idw": {"power": 2.0},
    "tikhonov": {"alpha": 0.5},
    "gsmooth": {"lam": 0.5, "n_iter": 40},
    "bgsrp": {"bandwidth": 6, "gamma": 0.1, "reg": 1e-6},
    "puy": {"alpha": 0.2},
    "sobolev": {"alpha": 0.2, "order": 2},
    "graph_time_tikhonov": {"alpha": 0.5, "beta": 0.1},
    "trss": {"alpha": 0.8, "beta": 0.1, "n_iter": 40, "lr": 0.03},
    "sobolev_temporal": {"alpha": 0.8, "beta": 0.1, "n_iter": 40, "lr": 0.03},
    "tv": {"lam": 0.2, "n_iter": 20, "eps": 1e-5},
    "temporal_laplacian": {"alpha": 0.5, "beta": 0.1},
    "spline_temporal": {"alpha": 0.5, "s_temporal": 1.0},
    "directed_tv": {"alpha": 0.5, "beta": 0.1, "n_iter": 20, "eps": 1e-5},
    "adaptive_temporal": {"alpha": 0.5, "beta": 0.1, "gamma": 0.8, "n_iter": 20},
}


def ensure_results_dir() -> Path:
    root = Path(__file__).resolve().parents[1]
    out = root / "results"
    out.mkdir(parents=True, exist_ok=True)
    return out


def main() -> None:
    out_dir = ensure_results_dir()

    sample = load_synthetic_eeg(n_channels=22, n_times=220, random_state=42)
    signals = sample["signals"]
    positions = sample["positions"]

    masked = simulate_missing_channels(signals, missing_ratio=0.2, random_state=123)

    graph = build_graph(GRAPH_METHOD, positions, signals=signals, k=6, sigma=1.0)
    adjacency = graph["adjacency"]
    if hasattr(adjacency, "toarray"):
        adjacency = adjacency.toarray()

    rows = []
    for method in ACTIVE_METHODS:
        params = dict(METHOD_PARAMS.get(method, {}))
        call_kwargs = dict(params)
        if method in POSITION_BASED:
            call_kwargs["positions"] = positions
        if method in GRAPH_BASED:
            call_kwargs["adjacency"] = adjacency

        try:
            rec = interpolate_signals(method, masked, **call_kwargs)
            reconstructed = rec["reconstructed"]
            finite = bool(np.isfinite(reconstructed).all())
            shape_ok = reconstructed.shape == signals.shape
            metrics = evaluate_signals(signals, reconstructed, metrics=["mae", "rmse", "dtw", "snr"])
            status = "pass" if (finite and shape_ok) else "fail"
            rows.append(
                {
                    "method": method,
                    "status": status,
                    "finite": finite,
                    "shape_ok": shape_ok,
                    "mae": float(metrics["mae"]),
                    "rmse": float(metrics["rmse"]),
                    "dtw": float(metrics["dtw"]),
                    "snr": float(metrics["snr"]),
                    "error": "",
                }
            )
        except Exception as exc:
            rows.append(
                {
                    "method": method,
                    "status": "fail",
                    "finite": False,
                    "shape_ok": False,
                    "mae": np.nan,
                    "rmse": np.nan,
                    "dtw": np.nan,
                    "snr": np.nan,
                    "error": str(exc),
                }
            )

    df = pd.DataFrame(rows).sort_values(["status", "method"], ascending=[False, True])
    out_csv = out_dir / "paper_faithful_active_methods_validation.csv"
    df.to_csv(out_csv, index=False)

    passed = int((df["status"] == "pass").sum())
    failed = int((df["status"] == "fail").sum())
    out_md = out_dir / "paper_faithful_active_methods_validation.md"
    out_md.write_text(
        "\n".join(
            [
                "# Active Methods Validation (paper-faithful closure)",
                "",
                f"- total_methods: {len(df)}",
                f"- passed: {passed}",
                f"- failed: {failed}",
                f"- evidence_csv: {out_csv.name}",
            ]
        ),
        encoding="utf-8",
    )

    out_cfg = out_dir / "paper_faithful_active_methods_validation_config.json"
    out_cfg.write_text(
        json.dumps(
            {
                "dataset": "synthetic",
                "n_channels": int(signals.shape[1]),
                "n_times": int(signals.shape[0]),
                "graph_method": GRAPH_METHOD,
                "missing_ratio": 0.2,
                "active_methods": ACTIVE_METHODS,
                "passes": passed,
                "fails": failed,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    if failed > 0:
        raise SystemExit(f"Validation failed for {failed} method(s). See {out_csv}.")

    print(f"Saved: {out_csv}")
    print(f"Saved: {out_md}")
    print(f"Saved: {out_cfg}")


if __name__ == "__main__":
    main()
