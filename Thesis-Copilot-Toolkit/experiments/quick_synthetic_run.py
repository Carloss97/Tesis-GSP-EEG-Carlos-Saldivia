"""Quick synthetic run for fast pipeline validation."""

from src.data.data_loader import load_synthetic_eeg, simulate_missing_channels
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals
from src.evaluation import evaluate_signals


def main() -> None:
    sample = load_synthetic_eeg(n_channels=16, n_times=150, random_state=42)
    signals = sample["signals"]
    positions = sample["positions"]
    signals_missing = simulate_missing_channels(signals, missing_ratio=0.2, random_state=42)

    graph_methods = [
        ("knn", {"k": 4}),
        ("gaussian", {"sigma": 1.0}),
        ("vknng", {"k": 4, "alpha": 1.0, "k_min": 2, "k_max": 8}),
    ]
    interp_methods = [
        "linear",
        "gsp",
        "tikhonov",
        "gsmooth",
        "idw",
        "rbfi_tps",
    ]

    rows = []
    for g_name, g_params in graph_methods:
        graph = build_graph(g_name, positions, signals=signals, **g_params)
        adjacency = graph["adjacency"]
        if hasattr(adjacency, "toarray"):
            adjacency = adjacency.toarray()

        for interp in interp_methods:
            if interp in {"gsp", "tikhonov", "gsmooth"}:
                rec = interpolate_signals(interp, signals_missing, adjacency=adjacency)
            elif interp in {"idw", "rbfi_tps"}:
                rec = interpolate_signals(interp, signals_missing, positions=positions)
            else:
                rec = interpolate_signals(interp, signals_missing)

            metrics = evaluate_signals(signals, rec["reconstructed"], metrics=["mae", "rmse", "snr"])
            rows.append((g_name, interp, metrics["mae"], metrics["rmse"], metrics["snr"]))

    rows.sort(key=lambda x: x[2])
    print("graph,interpolator,mae,rmse,snr")
    for r in rows:
        print(f"{r[0]},{r[1]},{r[2]:.6f},{r[3]:.6f},{r[4]:.6f}")


if __name__ == "__main__":
    main()
