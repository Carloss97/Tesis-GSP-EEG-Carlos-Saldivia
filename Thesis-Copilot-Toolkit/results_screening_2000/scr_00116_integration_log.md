# Integration Log: scr_00116
Started: 2026-04-16T15:11:02.558096+00:00
Description: Screening scr_00116 ds=movielens_graph_signal graph=knn miss=2ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k3 built OK
    mean | MR=2ch | seed=0 | MAE=1.4577e-02 | t=0.0033s
    nearest | MR=2ch | seed=0 | MAE=1.3191e-02 | t=0.0353s
    tikhonov | MR=2ch | seed=0 | MAE=6.0689e-02 | t=0.0129s
    tv | MR=2ch | seed=0 | MAE=1.4582e-02 | t=0.4683s
    trss | MR=2ch | seed=0 | MAE=1.8472e-02 | t=0.3999s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.3736e-01 | t=0.0205s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.4103e-01 | t=21.2353s
    mean | MR=2ch | seed=1 | MAE=1.9048e-02 | t=0.0033s
    nearest | MR=2ch | seed=1 | MAE=2.1272e-02 | t=0.0044s
    tikhonov | MR=2ch | seed=1 | MAE=6.5891e-02 | t=0.0102s
    tv | MR=2ch | seed=1 | MAE=1.9183e-02 | t=0.3486s
    trss | MR=2ch | seed=1 | MAE=2.7762e-02 | t=0.2669s

Completed: 2026-04-16T15:11:02.558991+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.