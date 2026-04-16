# Integration Log: scr_01242
Started: 2026-04-16T08:24:34.303384+00:00
Description: Screening scr_01242 ds=iv100hz_mat graph=gaussian miss=[0.2] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=1.1596e-02 | t=0.2165s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.6542e-02 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.6568e-03 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.3597e-02 | t=1.3357s
    tv | MR=0.2 | seed=1 | MAE=1.1192e-02 | t=0.1862s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=3.6616e-02 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=3.6372e-03 | t=0.0186s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=6.3610e-02 | t=1.2505s
    tv | MR=0.2 | seed=0 | MAE=1.1190e-02 | t=0.2084s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.7473e-02 | t=0.0083s
    trss | MR=0.2 | seed=0 | MAE=5.2136e-03 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.9050e-02 | t=1.2515s

Completed: 2026-04-16T08:24:34.304181+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.