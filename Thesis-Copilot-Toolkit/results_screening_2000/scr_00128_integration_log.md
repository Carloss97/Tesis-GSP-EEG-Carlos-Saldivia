# Integration Log: scr_00128
Started: 2026-04-16T15:17:41.326522+00:00
Description: Screening scr_00128 ds=movielens_graph_signal graph=knn miss=2ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k5 built OK
    mean | MR=2ch | seed=0 | MAE=1.4577e-02 | t=0.0035s
    nearest | MR=2ch | seed=0 | MAE=1.3191e-02 | t=0.0061s
    tikhonov | MR=2ch | seed=0 | MAE=7.9187e-02 | t=0.0101s
    tv | MR=2ch | seed=0 | MAE=1.4587e-02 | t=1.5554s
    trss | MR=2ch | seed=0 | MAE=2.0427e-02 | t=0.8187s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.5502e-01 | t=0.0204s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.4780e-01 | t=18.9118s
    mean | MR=2ch | seed=1 | MAE=1.9048e-02 | t=0.0033s
    nearest | MR=2ch | seed=1 | MAE=2.1272e-02 | t=0.0043s
    tikhonov | MR=2ch | seed=1 | MAE=8.1472e-02 | t=0.0099s
    tv | MR=2ch | seed=1 | MAE=1.9081e-02 | t=0.5354s
    trss | MR=2ch | seed=1 | MAE=2.6570e-02 | t=0.5143s

Completed: 2026-04-16T15:17:41.327688+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.