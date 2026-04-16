# Integration Log: scr_02000
Started: 2026-04-16T10:07:36.089328+00:00
Description: Screening scr_02000 ds=movielens_graph_signal graph=gaussian miss=[0.2] mode=noise

## Dataset: movielens_graph_signal | rows=42
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=6.0272e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.8363e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.6023e-01 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=5.9909e-02 | t=0.1861s
    trss | MR=0.2 | seed=0 | MAE=6.8727e-02 | t=0.0200s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.6738e-01 | t=0.0082s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.4497e-01 | t=1.2662s
    mean | MR=0.2 | seed=1 | MAE=6.6618e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=9.0693e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.5992e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.6499e-02 | t=0.1873s
    trss | MR=0.2 | seed=1 | MAE=7.5924e-02 | t=0.0209s

Completed: 2026-04-16T10:07:36.090028+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.