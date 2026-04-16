# Integration Log: scr_01556
Started: 2026-04-16T09:04:36.304573+00:00
Description: Screening scr_01556 ds=movielens_graph_signal graph=gaussian miss=1ch mode=noise

## Dataset: movielens_graph_signal | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=6.0272e-02 | t=0.0023s
    nearest | MR=0.2 | seed=0 | MAE=6.8363e-02 | t=0.0049s
    tikhonov | MR=0.2 | seed=0 | MAE=2.1314e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=6.0227e-02 | t=0.1845s
    trss | MR=0.2 | seed=0 | MAE=6.8666e-02 | t=0.0190s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.9879e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5826e-01 | t=1.3350s
    mean | MR=0.2 | seed=1 | MAE=6.6618e-02 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=9.0693e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=2.0837e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.6600e-02 | t=0.1841s
    trss | MR=0.2 | seed=1 | MAE=7.4382e-02 | t=0.0193s

Completed: 2026-04-16T09:04:36.305270+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.