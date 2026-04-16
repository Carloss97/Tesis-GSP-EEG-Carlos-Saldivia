# Integration Log: scr_00596
Started: 2026-04-16T14:34:43.133787+00:00
Description: Screening scr_00596 ds=movielens_graph_signal graph=gaussian miss=[0.3] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.3 | seed=0 | MAE=6.3154e-02 | t=0.0021s
    nearest | MR=0.3 | seed=0 | MAE=6.7099e-02 | t=0.0130s
    tikhonov | MR=0.3 | seed=0 | MAE=1.0783e-01 | t=0.0087s
    tv | MR=0.3 | seed=0 | MAE=6.3139e-02 | t=0.4763s
    trss | MR=0.3 | seed=0 | MAE=7.4846e-02 | t=0.2858s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.6368e-01 | t=0.0125s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.5474e-01 | t=30.3214s
    mean | MR=0.3 | seed=1 | MAE=6.5229e-02 | t=0.0332s
    nearest | MR=0.3 | seed=1 | MAE=6.3035e-02 | t=0.0184s
    tikhonov | MR=0.3 | seed=1 | MAE=1.0873e-01 | t=0.0117s
    tv | MR=0.3 | seed=1 | MAE=6.5228e-02 | t=0.4813s
    trss | MR=0.3 | seed=1 | MAE=8.0846e-02 | t=0.3503s

Completed: 2026-04-16T14:34:43.134702+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.