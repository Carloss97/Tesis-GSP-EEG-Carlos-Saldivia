# Integration Log: scr_00404
Started: 2026-04-16T13:19:56.631156+00:00
Description: Screening scr_00404 ds=movielens_graph_signal graph=knng miss=[0.1] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knng built OK
    mean | MR=0.1 | seed=0 | MAE=1.4577e-02 | t=0.0021s
    nearest | MR=0.1 | seed=0 | MAE=1.3191e-02 | t=0.0028s
    tikhonov | MR=0.1 | seed=0 | MAE=6.3960e-02 | t=0.0129s
    tv | MR=0.1 | seed=0 | MAE=1.4572e-02 | t=0.1502s
    trss | MR=0.1 | seed=0 | MAE=1.8736e-02 | t=0.1972s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.4176e-01 | t=0.0143s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.4232e-01 | t=17.8663s
    mean | MR=0.1 | seed=1 | MAE=1.9048e-02 | t=0.0208s
    nearest | MR=0.1 | seed=1 | MAE=2.1272e-02 | t=0.0061s
    tikhonov | MR=0.1 | seed=1 | MAE=6.8756e-02 | t=0.0089s
    tv | MR=0.1 | seed=1 | MAE=1.9106e-02 | t=0.3340s
    trss | MR=0.1 | seed=1 | MAE=2.7825e-02 | t=0.0215s

Completed: 2026-04-16T13:19:56.632020+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.