# Integration Log: scr_00080
Started: 2026-04-16T14:53:45.489443+00:00
Description: Screening scr_00080 ds=movielens_graph_signal graph=knng miss=1ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knng built OK
    mean | MR=1ch | seed=0 | MAE=1.5664e-02 | t=0.0063s
    nearest | MR=1ch | seed=0 | MAE=1.9262e-02 | t=0.0070s
    tikhonov | MR=1ch | seed=0 | MAE=6.3105e-02 | t=0.0058s
    tv | MR=1ch | seed=0 | MAE=1.5667e-02 | t=0.3587s
    trss | MR=1ch | seed=0 | MAE=1.7907e-02 | t=0.3458s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.3564e-01 | t=0.0166s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.3829e-01 | t=25.1687s
    mean | MR=1ch | seed=1 | MAE=1.2778e-02 | t=0.0034s
    nearest | MR=1ch | seed=1 | MAE=1.7187e-02 | t=0.0032s
    tikhonov | MR=1ch | seed=1 | MAE=6.2042e-02 | t=0.0314s
    tv | MR=1ch | seed=1 | MAE=1.2805e-02 | t=0.1891s
    trss | MR=1ch | seed=1 | MAE=1.5893e-02 | t=0.0211s

Completed: 2026-04-16T14:53:45.490336+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.