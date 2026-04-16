# Integration Log: scr_00608
Started: 2026-04-16T14:40:22.755228+00:00
Description: Screening scr_00608 ds=movielens_graph_signal graph=kalofolias miss=[0.3] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: kalofolias built OK
    mean | MR=0.3 | seed=0 | MAE=6.3154e-02 | t=0.0031s
    nearest | MR=0.3 | seed=0 | MAE=6.7099e-02 | t=0.0104s
    tikhonov | MR=0.3 | seed=0 | MAE=2.0013e-01 | t=0.0087s
    tv | MR=0.3 | seed=0 | MAE=6.3154e-02 | t=0.7400s
    trss | MR=0.3 | seed=0 | MAE=9.3986e-02 | t=1.0863s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.9739e-01 | t=0.0138s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.8094e-01 | t=19.9355s
    mean | MR=0.3 | seed=1 | MAE=6.5229e-02 | t=0.0046s
    nearest | MR=0.3 | seed=1 | MAE=6.3035e-02 | t=0.0182s
    tikhonov | MR=0.3 | seed=1 | MAE=1.9358e-01 | t=0.0788s
    tv | MR=0.3 | seed=1 | MAE=6.5229e-02 | t=0.6437s
    trss | MR=0.3 | seed=1 | MAE=9.5034e-02 | t=0.5108s

Completed: 2026-04-16T14:40:22.756112+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.