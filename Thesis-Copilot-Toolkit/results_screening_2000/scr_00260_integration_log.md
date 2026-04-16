# Integration Log: scr_00260
Started: 2026-04-16T14:59:39.468331+00:00
Description: Screening scr_00260 ds=movielens_graph_signal graph=gaussian miss=3ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=3ch | seed=0 | MAE=2.3396e-02 | t=0.0350s
    nearest | MR=3ch | seed=0 | MAE=1.8112e-02 | t=0.0055s
    tikhonov | MR=3ch | seed=0 | MAE=1.1642e-01 | t=0.0088s
    tv | MR=3ch | seed=0 | MAE=2.3394e-02 | t=0.8158s
    trss | MR=3ch | seed=0 | MAE=2.9872e-02 | t=0.4527s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.7728e-01 | t=0.0124s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.5793e-01 | t=26.7170s
    mean | MR=3ch | seed=1 | MAE=2.1784e-02 | t=0.0031s
    nearest | MR=3ch | seed=1 | MAE=1.9343e-02 | t=0.0054s
    tikhonov | MR=3ch | seed=1 | MAE=1.1785e-01 | t=0.0087s
    tv | MR=3ch | seed=1 | MAE=2.1786e-02 | t=0.9272s
    trss | MR=3ch | seed=1 | MAE=2.9101e-02 | t=0.2788s

Completed: 2026-04-16T14:59:39.469205+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.