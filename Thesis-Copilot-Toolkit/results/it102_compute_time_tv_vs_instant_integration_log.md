# Integration Log: it102_compute_time_tv_vs_instant
Started: 2026-04-09T17:46:25.957967+00:00
Description: Computational complexity and runtime analysis TV vs Instant

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1027e-06 | t=0.0022s
    nearest | MR=0.2 | seed=0 | MAE=4.7139e-06 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=7.5688e-06 | t=0.0059s
    tv | MR=0.2 | seed=0 | MAE=4.0280e-06 | t=0.1435s
    trss | MR=0.2 | seed=0 | MAE=2.6830e-06 | t=0.0172s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3185e-05 | t=0.0078s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5291e-05 | t=1.3188s
    mean | MR=0.2 | seed=1 | MAE=4.0539e-06 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=4.6000e-06 | t=0.0041s
    tikhonov | MR=0.2 | seed=1 | MAE=7.5259e-06 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=3.9759e-06 | t=0.1399s
    trss | MR=0.2 | seed=1 | MAE=2.6503e-06 | t=0.0170s

Completed: 2026-04-09T17:46:25.958855+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.