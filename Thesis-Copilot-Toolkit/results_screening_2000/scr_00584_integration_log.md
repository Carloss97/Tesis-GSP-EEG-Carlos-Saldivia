# Integration Log: scr_00584
Started: 2026-04-16T14:28:25.967745+00:00
Description: Screening scr_00584 ds=movielens_graph_signal graph=gaussian miss=[0.3] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.3 | seed=0 | MAE=6.3154e-02 | t=0.0353s
    nearest | MR=0.3 | seed=0 | MAE=6.7099e-02 | t=0.0101s
    tikhonov | MR=0.3 | seed=0 | MAE=1.3290e-01 | t=0.0088s
    tv | MR=0.3 | seed=0 | MAE=6.3152e-02 | t=0.9019s
    trss | MR=0.3 | seed=0 | MAE=7.4500e-02 | t=0.3503s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.7905e-01 | t=0.0176s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.6321e-01 | t=15.4612s
    mean | MR=0.3 | seed=1 | MAE=6.5229e-02 | t=0.0031s
    nearest | MR=0.3 | seed=1 | MAE=6.3035e-02 | t=0.0102s
    tikhonov | MR=0.3 | seed=1 | MAE=1.3082e-01 | t=0.0101s
    tv | MR=0.3 | seed=1 | MAE=6.5229e-02 | t=1.1702s
    trss | MR=0.3 | seed=1 | MAE=7.9224e-02 | t=0.7549s

Completed: 2026-04-16T14:28:25.968806+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.