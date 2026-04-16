# Integration Log: scr_01856
Started: 2026-04-16T09:46:59.240272+00:00
Description: Screening scr_01856 ds=movielens_graph_signal graph=knn miss=[0.1] mode=noise

## Dataset: movielens_graph_signal | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=6.0272e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.8363e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=1.6124e-01 | t=0.0056s
    tv | MR=0.2 | seed=0 | MAE=5.9600e-02 | t=0.1461s
    trss | MR=0.2 | seed=0 | MAE=7.0172e-02 | t=0.0204s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.6820e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5556e-01 | t=1.4923s
    mean | MR=0.2 | seed=1 | MAE=6.6618e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=9.0693e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.5962e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.6341e-02 | t=0.1444s
    trss | MR=0.2 | seed=1 | MAE=7.5916e-02 | t=0.0197s

Completed: 2026-04-16T09:46:59.241132+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.