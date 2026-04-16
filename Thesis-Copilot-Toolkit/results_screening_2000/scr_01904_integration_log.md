# Integration Log: scr_01904
Started: 2026-04-16T09:53:46.067782+00:00
Description: Screening scr_01904 ds=movielens_graph_signal graph=kalofolias miss=[0.1] mode=noise

## Dataset: movielens_graph_signal | rows=42
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=6.0272e-02 | t=0.0022s
    nearest | MR=0.2 | seed=0 | MAE=6.8363e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=3.6125e-01 | t=0.0056s
    tv | MR=0.2 | seed=0 | MAE=6.0272e-02 | t=0.1462s
    trss | MR=0.2 | seed=0 | MAE=1.1162e-01 | t=0.0207s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.3968e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.9431e-01 | t=1.2851s
    mean | MR=0.2 | seed=1 | MAE=6.6618e-02 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=9.0693e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=3.4640e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.6618e-02 | t=0.1482s
    trss | MR=0.2 | seed=1 | MAE=9.9262e-02 | t=0.0197s

Completed: 2026-04-16T09:53:46.068484+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.