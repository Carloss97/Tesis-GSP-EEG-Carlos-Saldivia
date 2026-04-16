# Integration Log: scr_00620
Started: 2026-04-16T14:46:52.440934+00:00
Description: Screening scr_00620 ds=movielens_graph_signal graph=knng miss=[0.3] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knng built OK
    mean | MR=0.3 | seed=0 | MAE=6.3154e-02 | t=0.0032s
    nearest | MR=0.3 | seed=0 | MAE=6.7099e-02 | t=0.0128s
    tikhonov | MR=0.3 | seed=0 | MAE=9.5991e-02 | t=0.0118s
    tv | MR=0.3 | seed=0 | MAE=6.3085e-02 | t=0.6251s
    trss | MR=0.3 | seed=0 | MAE=7.6223e-02 | t=0.0759s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.5151e-01 | t=0.0137s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.5359e-01 | t=23.4683s
    mean | MR=0.3 | seed=1 | MAE=6.5229e-02 | t=0.0032s
    nearest | MR=0.3 | seed=1 | MAE=6.3035e-02 | t=0.0846s
    tikhonov | MR=0.3 | seed=1 | MAE=9.8146e-02 | t=0.0113s
    tv | MR=0.3 | seed=1 | MAE=6.5224e-02 | t=0.4644s
    trss | MR=0.3 | seed=1 | MAE=8.1062e-02 | t=0.3402s

Completed: 2026-04-16T14:46:52.441932+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.