# Integration Log: scr_00704
Started: 2026-04-16T15:32:33.317705+00:00
Description: Screening scr_00704 ds=movielens_graph_signal graph=gaussian miss=[0.4] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.4 | seed=0 | MAE=9.1473e-02 | t=0.0054s
    nearest | MR=0.4 | seed=0 | MAE=1.0507e-01 | t=0.0947s
    tikhonov | MR=0.4 | seed=0 | MAE=1.2549e-01 | t=0.0203s
    tv | MR=0.4 | seed=0 | MAE=9.1504e-02 | t=0.7941s
    trss | MR=0.4 | seed=0 | MAE=1.1199e-01 | t=0.2675s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.6275e-01 | t=0.0711s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.5168e-01 | t=35.3591s
    mean | MR=0.4 | seed=1 | MAE=8.7528e-02 | t=0.0031s
    nearest | MR=0.4 | seed=1 | MAE=9.3427e-02 | t=0.0138s
    tikhonov | MR=0.4 | seed=1 | MAE=1.2596e-01 | t=0.0102s
    tv | MR=0.4 | seed=1 | MAE=8.7522e-02 | t=1.0902s
    trss | MR=0.4 | seed=1 | MAE=1.0576e-01 | t=0.3318s

Completed: 2026-04-16T15:32:33.320063+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.