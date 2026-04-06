# Integration Log: it102_compute_time_tv_vs_instant
Started: 2026-04-06T17:43:15.570609+00:00
Description: Computational complexity and runtime analysis TV vs Instant

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.1027e-06 | t=0.0040s
    nearest | MR=0.2 | seed=0 | MAE=4.7139e-06 | t=0.0077s
    tikhonov | MR=0.2 | seed=0 | MAE=7.5688e-06 | t=0.0128s
    tv | MR=0.2 | seed=0 | MAE=4.0280e-06 | t=0.2895s
    trss | MR=0.2 | seed=0 | MAE=2.6830e-06 | t=0.0342s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3185e-05 | t=0.0159s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5291e-05 | t=7.2782s
    mean | MR=0.2 | seed=1 | MAE=4.0539e-06 | t=0.0036s
    nearest | MR=0.2 | seed=1 | MAE=4.6000e-06 | t=0.0077s
    tikhonov | MR=0.2 | seed=1 | MAE=7.5259e-06 | t=0.0124s
    tv | MR=0.2 | seed=1 | MAE=3.9759e-06 | t=0.2902s
    trss | MR=0.2 | seed=1 | MAE=2.6503e-06 | t=0.0356s

Completed: 2026-04-06T17:43:15.572055+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.