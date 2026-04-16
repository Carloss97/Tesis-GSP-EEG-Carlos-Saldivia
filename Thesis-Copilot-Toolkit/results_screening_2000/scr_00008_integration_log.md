# Integration Log: scr_00008
Started: 2026-04-16T15:20:49.494772+00:00
Description: Screening scr_00008 ds=movielens_graph_signal graph=knn miss=1ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k3 built OK
    mean | MR=1ch | seed=0 | MAE=1.5664e-02 | t=0.0033s
    nearest | MR=1ch | seed=0 | MAE=1.9262e-02 | t=0.0031s
    tikhonov | MR=1ch | seed=0 | MAE=6.0658e-02 | t=0.0101s
    tv | MR=1ch | seed=0 | MAE=1.5688e-02 | t=0.5229s
    trss | MR=1ch | seed=0 | MAE=1.9064e-02 | t=0.2273s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.3184e-01 | t=0.0127s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.3726e-01 | t=26.4692s
    mean | MR=1ch | seed=1 | MAE=1.2778e-02 | t=0.0032s
    nearest | MR=1ch | seed=1 | MAE=1.7187e-02 | t=0.0357s
    tikhonov | MR=1ch | seed=1 | MAE=5.8793e-02 | t=0.0101s
    tv | MR=1ch | seed=1 | MAE=1.2799e-02 | t=0.5266s
    trss | MR=1ch | seed=1 | MAE=1.6063e-02 | t=1.0835s

Completed: 2026-04-16T15:20:49.495703+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.