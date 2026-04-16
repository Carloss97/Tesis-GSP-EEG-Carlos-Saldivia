# Integration Log: scr_00500
Started: 2026-04-16T13:52:40.714909+00:00
Description: Screening scr_00500 ds=movielens_graph_signal graph=kalofolias miss=[0.2] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=4.4107e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=4.5789e-02 | t=0.0049s
    tikhonov | MR=0.2 | seed=0 | MAE=2.0299e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=4.4107e-02 | t=0.1501s
    trss | MR=0.2 | seed=0 | MAE=7.0222e-02 | t=0.0194s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9956e-01 | t=0.0079s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7808e-01 | t=20.0557s
    mean | MR=0.2 | seed=1 | MAE=4.2780e-02 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=4.0779e-02 | t=0.0060s
    tikhonov | MR=0.2 | seed=1 | MAE=2.0421e-01 | t=0.0065s
    tv | MR=0.2 | seed=1 | MAE=4.2780e-02 | t=0.1889s
    trss | MR=0.2 | seed=1 | MAE=7.3915e-02 | t=0.0182s

Completed: 2026-04-16T13:52:40.715621+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.