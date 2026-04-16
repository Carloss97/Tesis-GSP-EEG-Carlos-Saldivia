# Integration Log: scr_01940
Started: 2026-04-16T09:58:53.695147+00:00
Description: Screening scr_01940 ds=movielens_graph_signal graph=aew miss=[0.1] mode=noise

## Dataset: movielens_graph_signal | rows=42
  Graph: aew built OK
    mean | MR=0.2 | seed=0 | MAE=6.0272e-02 | t=0.0022s
    nearest | MR=0.2 | seed=0 | MAE=6.8363e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=7.0952e-02 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=5.5382e-02 | t=0.1437s
    trss | MR=0.2 | seed=0 | MAE=6.4171e-02 | t=0.0225s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.4714e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.1137e-01 | t=1.3313s
    mean | MR=0.2 | seed=1 | MAE=6.6618e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=9.0693e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=8.2520e-02 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=6.5150e-02 | t=0.1439s
    trss | MR=0.2 | seed=1 | MAE=7.1197e-02 | t=0.0207s

Completed: 2026-04-16T09:58:53.695848+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.