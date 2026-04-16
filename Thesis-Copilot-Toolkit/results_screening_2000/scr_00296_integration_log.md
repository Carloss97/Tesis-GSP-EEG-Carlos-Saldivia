# Integration Log: scr_00296
Started: 2026-04-16T15:19:33.056339+00:00
Description: Screening scr_00296 ds=movielens_graph_signal graph=knng miss=3ch mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knng built OK
    mean | MR=3ch | seed=0 | MAE=2.3396e-02 | t=0.0054s
    nearest | MR=3ch | seed=0 | MAE=1.8112e-02 | t=0.0056s
    tikhonov | MR=3ch | seed=0 | MAE=6.8339e-02 | t=0.0090s
    tv | MR=3ch | seed=0 | MAE=2.3310e-02 | t=0.9695s
    trss | MR=3ch | seed=0 | MAE=2.8734e-02 | t=1.1069s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.4244e-01 | t=0.0128s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.4549e-01 | t=24.8890s
    mean | MR=3ch | seed=1 | MAE=2.1784e-02 | t=0.0031s
    nearest | MR=3ch | seed=1 | MAE=1.9343e-02 | t=0.0307s
    tikhonov | MR=3ch | seed=1 | MAE=7.1964e-02 | t=0.0087s
    tv | MR=3ch | seed=1 | MAE=2.1863e-02 | t=0.7515s
    trss | MR=3ch | seed=1 | MAE=3.1063e-02 | t=0.1739s

Completed: 2026-04-16T15:19:33.057274+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.