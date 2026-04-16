# Integration Log: scr_01820
Started: 2026-04-16T09:41:53.732946+00:00
Description: Screening scr_01820 ds=movielens_graph_signal graph=vknng miss=3ch mode=noise

## Dataset: movielens_graph_signal | rows=42
  Graph: vknng built OK
    mean | MR=0.2 | seed=0 | MAE=6.0272e-02 | t=0.0024s
    nearest | MR=0.2 | seed=0 | MAE=6.8363e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.4520e-01 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=5.8728e-02 | t=0.1426s
    trss | MR=0.2 | seed=0 | MAE=7.2164e-02 | t=0.0202s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.5342e-01 | t=0.0084s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5659e-01 | t=1.3163s
    mean | MR=0.2 | seed=1 | MAE=6.6618e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=9.0693e-02 | t=0.0049s
    tikhonov | MR=0.2 | seed=1 | MAE=1.4675e-01 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=6.5962e-02 | t=0.1407s
    trss | MR=0.2 | seed=1 | MAE=7.9673e-02 | t=0.0205s

Completed: 2026-04-16T09:41:53.733722+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.