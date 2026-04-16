# Integration Log: scr_00224
Started: 2026-04-16T14:41:26.146012+00:00
Description: Screening scr_00224 ds=movielens_graph_signal graph=knn miss=3ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k3 built OK
    mean | MR=3ch | seed=0 | MAE=2.3396e-02 | t=0.0038s
    nearest | MR=3ch | seed=0 | MAE=1.8112e-02 | t=0.0073s
    tikhonov | MR=3ch | seed=0 | MAE=6.5259e-02 | t=0.0089s
    tv | MR=3ch | seed=0 | MAE=2.3205e-02 | t=0.1875s
    trss | MR=3ch | seed=0 | MAE=2.9574e-02 | t=0.3601s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.3796e-01 | t=0.0362s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.4391e-01 | t=27.7671s
    mean | MR=3ch | seed=1 | MAE=2.1784e-02 | t=0.0030s
    nearest | MR=3ch | seed=1 | MAE=1.9343e-02 | t=0.0725s
    tikhonov | MR=3ch | seed=1 | MAE=7.0419e-02 | t=0.0086s
    tv | MR=3ch | seed=1 | MAE=2.1938e-02 | t=0.5003s
    trss | MR=3ch | seed=1 | MAE=3.3783e-02 | t=0.5278s

Completed: 2026-04-16T14:41:26.147222+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.