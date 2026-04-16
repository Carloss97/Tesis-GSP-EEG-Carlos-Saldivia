# Integration Log: scr_01640
Started: 2026-04-16T09:16:29.678972+00:00
Description: Screening scr_01640 ds=movielens_graph_signal graph=knn miss=2ch mode=noise

## Dataset: movielens_graph_signal | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=6.0272e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.8363e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.6124e-01 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=5.9600e-02 | t=0.1450s
    trss | MR=0.2 | seed=0 | MAE=7.0172e-02 | t=0.0200s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.6820e-01 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5556e-01 | t=1.3019s
    mean | MR=0.2 | seed=1 | MAE=6.6618e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=9.0693e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=1 | MAE=1.5962e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.6341e-02 | t=0.1447s
    trss | MR=0.2 | seed=1 | MAE=7.5916e-02 | t=0.0202s

Completed: 2026-04-16T09:16:29.679675+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.