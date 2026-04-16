# Integration Log: scr_00152
Started: 2026-04-16T15:31:26.815647+00:00
Description: Screening scr_00152 ds=movielens_graph_signal graph=gaussian miss=2ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=2ch | seed=0 | MAE=1.4577e-02 | t=0.0064s
    nearest | MR=2ch | seed=0 | MAE=1.3191e-02 | t=0.0070s
    tikhonov | MR=2ch | seed=0 | MAE=1.1244e-01 | t=0.0831s
    tv | MR=2ch | seed=0 | MAE=1.4577e-02 | t=0.8140s
    trss | MR=2ch | seed=0 | MAE=1.9136e-02 | t=0.0878s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.7704e-01 | t=0.0391s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.5397e-01 | t=18.1124s
    mean | MR=2ch | seed=1 | MAE=1.9048e-02 | t=0.0037s
    nearest | MR=2ch | seed=1 | MAE=2.1272e-02 | t=0.0056s
    tikhonov | MR=2ch | seed=1 | MAE=1.1240e-01 | t=0.0278s
    tv | MR=2ch | seed=1 | MAE=1.9049e-02 | t=0.5474s
    trss | MR=2ch | seed=1 | MAE=2.4474e-02 | t=0.1397s

Completed: 2026-04-16T15:31:26.846670+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.