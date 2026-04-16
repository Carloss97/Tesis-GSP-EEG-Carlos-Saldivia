# Integration Log: scr_00380
Started: 2026-04-16T13:12:30.912797+00:00
Description: Screening scr_00380 ds=movielens_graph_signal graph=gaussian miss=[0.1] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.1 | seed=0 | MAE=1.4577e-02 | t=0.0031s
    nearest | MR=0.1 | seed=0 | MAE=1.3191e-02 | t=0.0043s
    tikhonov | MR=0.1 | seed=0 | MAE=7.9446e-02 | t=0.0154s
    tv | MR=0.1 | seed=0 | MAE=1.4577e-02 | t=0.5547s
    trss | MR=0.1 | seed=0 | MAE=1.9530e-02 | t=0.5236s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.5675e-01 | t=0.0132s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.4374e-01 | t=22.0742s
    mean | MR=0.1 | seed=1 | MAE=1.9048e-02 | t=0.0031s
    nearest | MR=0.1 | seed=1 | MAE=2.1272e-02 | t=0.0044s
    tikhonov | MR=0.1 | seed=1 | MAE=8.1704e-02 | t=0.0087s
    tv | MR=0.1 | seed=1 | MAE=1.9061e-02 | t=0.5408s
    trss | MR=0.1 | seed=1 | MAE=2.5699e-02 | t=0.2351s

Completed: 2026-04-16T13:12:30.913668+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.