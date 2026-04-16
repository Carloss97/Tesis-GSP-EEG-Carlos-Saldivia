# Integration Log: scr_01928
Started: 2026-04-16T09:57:13.277243+00:00
Description: Screening scr_01928 ds=movielens_graph_signal graph=vknng miss=[0.1] mode=noise

## Dataset: movielens_graph_signal | rows=42
  Graph: vknng built OK
    mean | MR=0.2 | seed=0 | MAE=6.0272e-02 | t=0.0025s
    nearest | MR=0.2 | seed=0 | MAE=6.8363e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.4520e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=5.8728e-02 | t=0.1408s
    trss | MR=0.2 | seed=0 | MAE=7.2164e-02 | t=0.0203s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.5342e-01 | t=0.0138s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5659e-01 | t=2.5313s
    mean | MR=0.2 | seed=1 | MAE=6.6618e-02 | t=0.0023s
    nearest | MR=0.2 | seed=1 | MAE=9.0693e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.4675e-01 | t=0.0056s
    tv | MR=0.2 | seed=1 | MAE=6.5962e-02 | t=0.1422s
    trss | MR=0.2 | seed=1 | MAE=7.9673e-02 | t=0.0196s

Completed: 2026-04-16T09:57:13.278019+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.