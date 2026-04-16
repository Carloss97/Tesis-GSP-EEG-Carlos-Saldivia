# Integration Log: scr_01760
Started: 2026-04-16T09:33:21.240333+00:00
Description: Screening scr_01760 ds=movielens_graph_signal graph=knn miss=3ch mode=noise

## Dataset: movielens_graph_signal | rows=42
  Graph: knn__k7 built OK
    mean | MR=0.2 | seed=0 | MAE=6.0272e-02 | t=0.0025s
    nearest | MR=0.2 | seed=0 | MAE=6.8363e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.8690e-01 | t=0.0056s
    tv | MR=0.2 | seed=0 | MAE=6.0069e-02 | t=0.1505s
    trss | MR=0.2 | seed=0 | MAE=7.1978e-02 | t=0.0215s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.8412e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5579e-01 | t=1.2866s
    mean | MR=0.2 | seed=1 | MAE=6.6618e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=9.0693e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=1 | MAE=1.8199e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.6543e-02 | t=0.1504s
    trss | MR=0.2 | seed=1 | MAE=7.6554e-02 | t=0.0206s

Completed: 2026-04-16T09:33:21.241149+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.