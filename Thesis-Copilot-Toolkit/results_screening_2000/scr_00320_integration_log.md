# Integration Log: scr_00320
Started: 2026-04-16T15:33:11.563822+00:00
Description: Screening scr_00320 ds=movielens_graph_signal graph=aew miss=3ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: aew built OK
    mean | MR=3ch | seed=0 | MAE=2.3396e-02 | t=0.0054s
    nearest | MR=3ch | seed=0 | MAE=1.8112e-02 | t=0.0070s
    tikhonov | MR=3ch | seed=0 | MAE=2.9419e-02 | t=0.0140s
    tv | MR=3ch | seed=0 | MAE=2.2899e-02 | t=0.3982s
    trss | MR=3ch | seed=0 | MAE=2.6434e-02 | t=0.0331s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=8.1561e-02 | t=0.0165s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.1290e-01 | t=11.4901s
    mean | MR=3ch | seed=1 | MAE=2.1784e-02 | t=0.0202s
    nearest | MR=3ch | seed=1 | MAE=1.9343e-02 | t=0.0070s
    tikhonov | MR=3ch | seed=1 | MAE=3.2807e-02 | t=0.0089s
    tv | MR=3ch | seed=1 | MAE=2.2237e-02 | t=0.7254s
    trss | MR=3ch | seed=1 | MAE=2.8294e-02 | t=0.6278s

Completed: 2026-04-16T15:33:11.564984+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.