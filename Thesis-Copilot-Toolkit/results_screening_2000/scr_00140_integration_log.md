# Integration Log: scr_00140
Started: 2026-04-16T15:25:04.368098+00:00
Description: Screening scr_00140 ds=movielens_graph_signal graph=knn miss=2ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k7 built OK
    mean | MR=2ch | seed=0 | MAE=1.4577e-02 | t=0.0039s
    nearest | MR=2ch | seed=0 | MAE=1.3191e-02 | t=0.0057s
    tikhonov | MR=2ch | seed=0 | MAE=9.5868e-02 | t=0.0091s
    tv | MR=2ch | seed=0 | MAE=1.4581e-02 | t=0.3892s
    trss | MR=2ch | seed=0 | MAE=2.1503e-02 | t=0.3076s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.6674e-01 | t=0.0348s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.5122e-01 | t=34.6443s
    mean | MR=2ch | seed=1 | MAE=1.9048e-02 | t=0.0050s
    nearest | MR=2ch | seed=1 | MAE=2.1272e-02 | t=0.0065s
    tikhonov | MR=2ch | seed=1 | MAE=9.6293e-02 | t=0.0133s
    tv | MR=2ch | seed=1 | MAE=1.9060e-02 | t=0.4195s
    trss | MR=2ch | seed=1 | MAE=2.6096e-02 | t=0.3694s

Completed: 2026-04-16T15:25:04.369140+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.