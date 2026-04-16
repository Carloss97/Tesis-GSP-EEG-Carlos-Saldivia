# Integration Log: scr_01772
Started: 2026-04-16T09:35:07.785865+00:00
Description: Screening scr_01772 ds=movielens_graph_signal graph=gaussian miss=3ch mode=noise

## Dataset: movielens_graph_signal | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=6.0272e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.8363e-02 | t=0.0045s
    tikhonov | MR=0.2 | seed=0 | MAE=2.1314e-01 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=6.0227e-02 | t=0.1880s
    trss | MR=0.2 | seed=0 | MAE=6.8666e-02 | t=0.0207s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.9879e-01 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5826e-01 | t=1.2832s
    mean | MR=0.2 | seed=1 | MAE=6.6618e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=9.0693e-02 | t=0.0048s
    tikhonov | MR=0.2 | seed=1 | MAE=2.0837e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.6600e-02 | t=0.1861s
    trss | MR=0.2 | seed=1 | MAE=7.4382e-02 | t=0.0208s

Completed: 2026-04-16T09:35:07.786568+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.