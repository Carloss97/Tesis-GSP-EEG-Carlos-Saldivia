"""Strict INS-13 comparison: Python BGSRP vs MATLAB/GSPBox BGSRP on shared inputs."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.io import loadmat, savemat

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.data.data_loader import load_synthetic_eeg, simulate_missing_channels
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals


def ensure_results_dir() -> Path:
    root = Path(__file__).resolve().parents[1]
    out = root / "results"
    out.mkdir(parents=True, exist_ok=True)
    return out


def _to_posix(p: Path) -> str:
    return p.resolve().as_posix()


def run_matlab_case(
    matlab_exec: str,
    code_dir: Path,
    gspbox_dir: Path,
    input_mat: Path,
    output_mat: Path,
    runner_m: Path,
) -> None:
    script_text = f"""
addpath('{_to_posix(code_dir)}');
addpath(genpath('{_to_posix(gspbox_dir)}'));
in = load('{_to_posix(input_mat)}');
W = in.W;
x0 = in.x0(:);
y0 = in.y0(:);
param = struct();
param.bandw = double(in.bandw);
param.gamma = double(in.gamma);
param.basis = 'lp-ture';
G = gsp_graph(W);
G = gsp_compute_fourier_basis(G);
y = gsp_BGSRP_recon(G, x0, y0, param);
save('{_to_posix(output_mat)}', 'y');
""".strip()
    runner_m.write_text(script_text, encoding="utf-8")
    subprocess.run([matlab_exec, "-batch", f"run('{_to_posix(runner_m)}')"], check=True)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    results = ensure_results_dir()
    matlab_exec = shutil.which("matlab")
    code_dir = root.parent / "Papers" / "Code-for-BGSRP-master"

    gspbox_candidates = [
        root.parent / "Tesis" / "gspbox",
        root.parent / "Papers" / "gspbox",
    ]
    gspbox_dir = next((p for p in gspbox_candidates if p.exists()), None)

    status_path = results / "ins13_strict_status.md"
    config_path = results / "ins13_strict_config.json"
    raw_path = results / "ins13_strict_matlab_compare_raw.csv"
    summary_path = results / "ins13_strict_matlab_compare_summary.csv"

    if not matlab_exec or not code_dir.exists() or gspbox_dir is None:
        reason = []
        if not matlab_exec:
            reason.append("matlab executable not found")
        if not code_dir.exists():
            reason.append("Code-for-BGSRP-master not found")
        if gspbox_dir is None:
            reason.append("gspbox path not found")
        status = "blocked"
        text = "# INS-13 Strict Status\n\n"
        text += f"- status: {status}\n"
        text += f"- reason: {', '.join(reason)}\n"
        status_path.write_text(text, encoding="utf-8")
        pd.DataFrame().to_csv(raw_path, index=False)
        pd.DataFrame().to_csv(summary_path, index=False)
        config_path.write_text(json.dumps({"status": status, "reason": reason}, indent=2), encoding="utf-8")
        print(f"Saved: {status_path}")
        return

    data = load_synthetic_eeg(n_channels=22, n_times=200, random_state=42)
    signals = data["signals"]
    positions = data["positions"]
    graph = build_graph("knng", positions, signals=signals, k=6, sigma=1.0)
    adjacency = graph["adjacency"]
    if hasattr(adjacency, "toarray"):
        adjacency = adjacency.toarray()

    rows = []
    tmp_in = results / "ins13_tmp_input.mat"
    tmp_out = results / "ins13_tmp_output.mat"
    tmp_runner = results / "ins13_tmp_runner.m"

    for seed in [1, 7, 13, 21, 42]:
        masked = simulate_missing_channels(signals[:1], missing_ratio=0.2, random_state=seed)
        y_true = signals[0]
        y_obs = masked[0]
        x0 = np.where(~np.isnan(y_obs))[0] + 1  # MATLAB 1-based
        y0 = y_obs[~np.isnan(y_obs)]

        py_rec = interpolate_signals(
            "bgsrp",
            masked,
            adjacency=adjacency,
            bandwidth=8,
            gamma=0.1,
            strict_matlab=True,
        )["reconstructed"][0]

        savemat(
            tmp_in,
            {
                "W": adjacency.astype(float),
                "x0": x0.astype(np.int32),
                "y0": y0.astype(float),
                "bandw": np.array([[8]], dtype=np.float64),
                "gamma": np.array([[0.1]], dtype=np.float64),
            },
        )

        run_matlab_case(
            matlab_exec=matlab_exec,
            code_dir=code_dir,
            gspbox_dir=gspbox_dir,
            input_mat=tmp_in,
            output_mat=tmp_out,
            runner_m=tmp_runner,
        )
        mat = loadmat(tmp_out)
        y_mat = np.ravel(mat["y"]).astype(float)

        mae_py = float(np.mean(np.abs(py_rec - y_true)))
        mae_mat = float(np.mean(np.abs(y_mat - y_true)))
        mae_gap = float(mae_py - mae_mat)
        rel_l2 = float(np.linalg.norm(py_rec - y_mat) / max(np.linalg.norm(y_mat), 1e-12))
        corr = float(np.corrcoef(py_rec, y_mat)[0, 1])

        rows.append(
            {
                "seed": seed,
                "mae_python": mae_py,
                "mae_matlab": mae_mat,
                "mae_gap_python_minus_matlab": mae_gap,
                "relative_l2_python_vs_matlab": rel_l2,
                "corr_python_vs_matlab": corr,
            }
        )

    df = pd.DataFrame(rows)
    df.to_csv(raw_path, index=False)
    summary = pd.DataFrame(
        [
            {
                "runs": int(len(df)),
                "mae_gap_mean": float(df["mae_gap_python_minus_matlab"].mean()),
                "mae_gap_std": float(df["mae_gap_python_minus_matlab"].std(ddof=0)),
                "relative_l2_mean": float(df["relative_l2_python_vs_matlab"].mean()),
                "corr_mean": float(df["corr_python_vs_matlab"].mean()),
                "strict_close": bool(
                    abs(float(df["mae_gap_python_minus_matlab"].mean())) <= 1e-3
                    and float(df["corr_python_vs_matlab"].mean()) >= 0.99
                ),
            }
        ]
    )
    summary.to_csv(summary_path, index=False)

    strict_close = bool(summary.loc[0, "strict_close"])
    status = "done" if strict_close else "proxy_or_partial"
    text = "# INS-13 Strict Status\n\n"
    text += f"- status: {status}\n"
    text += f"- strict_close: {strict_close}\n"
    text += f"- mae_gap_mean: {summary.loc[0, 'mae_gap_mean']:.6e}\n"
    text += f"- corr_mean: {summary.loc[0, 'corr_mean']:.6f}\n"
    text += "- evidence: results/ins13_strict_matlab_compare_raw.csv, results/ins13_strict_matlab_compare_summary.csv\n"
    status_path.write_text(text, encoding="utf-8")

    config = {
        "status": status,
        "matlab_exec": matlab_exec,
        "gspbox_dir": str(gspbox_dir),
        "code_dir": str(code_dir),
        "seeds": [1, 7, 13, 21, 42],
        "bandw": 8,
        "gamma": 0.1,
    }
    config_path.write_text(json.dumps(config, indent=2), encoding="utf-8")

    for p in [tmp_in, tmp_out, tmp_runner]:
        if p.exists():
            p.unlink()

    print(f"Saved: {raw_path}")
    print(f"Saved: {summary_path}")
    print(f"Saved: {status_path}")
    print(f"Saved: {config_path}")


if __name__ == "__main__":
    main()
