# Integration Log: scr_00236
Started: 2026-04-16T14:47:38.270036+00:00
Description: Screening scr_00236 ds=movielens_graph_signal graph=knn miss=3ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k5 built OK
    mean | MR=3ch | seed=0 | MAE=2.3396e-02 | t=0.0030s
    nearest | MR=3ch | seed=0 | MAE=1.8112e-02 | t=0.0054s
    tikhonov | MR=3ch | seed=0 | MAE=8.2395e-02 | t=0.0163s
    tv | MR=3ch | seed=0 | MAE=2.3348e-02 | t=0.1986s
    trss | MR=3ch | seed=0 | MAE=2.8858e-02 | t=0.1447s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.5506e-01 | t=0.0167s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.5059e-01 | t=22.9964s
    mean | MR=3ch | seed=1 | MAE=2.1784e-02 | t=0.0031s
    nearest | MR=3ch | seed=1 | MAE=1.9343e-02 | t=0.0386s
    tikhonov | MR=3ch | seed=1 | MAE=8.5319e-02 | t=0.0087s
    tv | MR=3ch | seed=1 | MAE=2.1819e-02 | t=0.5167s
    trss | MR=3ch | seed=1 | MAE=3.0587e-02 | t=0.9739s

Completed: 2026-04-16T14:47:38.270905+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.