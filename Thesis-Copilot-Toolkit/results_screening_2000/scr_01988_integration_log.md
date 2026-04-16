# Integration Log: scr_01988
Started: 2026-04-16T10:05:55.308931+00:00
Description: Screening scr_01988 ds=movielens_graph_signal graph=gaussian miss=[0.2] mode=noise

## Dataset: movielens_graph_signal | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=6.0272e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.8363e-02 | t=0.0044s
    tikhonov | MR=0.2 | seed=0 | MAE=2.1314e-01 | t=0.0061s
    tv | MR=0.2 | seed=0 | MAE=6.0227e-02 | t=0.1894s
    trss | MR=0.2 | seed=0 | MAE=6.8666e-02 | t=0.0199s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.9879e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5826e-01 | t=2.6367s
    mean | MR=0.2 | seed=1 | MAE=6.6618e-02 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=9.0693e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=2.0837e-01 | t=0.0072s
    tv | MR=0.2 | seed=1 | MAE=6.6600e-02 | t=0.2162s
    trss | MR=0.2 | seed=1 | MAE=7.4382e-02 | t=0.0208s

Completed: 2026-04-16T10:05:55.309636+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.