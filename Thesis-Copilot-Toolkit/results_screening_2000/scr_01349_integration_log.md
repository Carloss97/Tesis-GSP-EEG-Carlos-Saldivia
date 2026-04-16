# Integration Log: scr_01349
Started: 2026-04-16T08:37:46.711510+00:00
Description: Screening scr_01349 ds=bci_iv2a_real_s3 graph=gaussian miss=[0.3] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=6.5815e-02 | t=0.1835s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.6180e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=2.8663e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.9513e-01 | t=1.2684s
    tv | MR=0.2 | seed=1 | MAE=6.8917e-02 | t=0.1864s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.6266e-01 | t=0.0079s
    trss | MR=0.2 | seed=1 | MAE=3.0563e-02 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.9340e-01 | t=1.2949s
    tv | MR=0.2 | seed=0 | MAE=6.5815e-02 | t=0.1857s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.1137e-01 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=3.0629e-02 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.9815e-01 | t=1.3266s

Completed: 2026-04-16T08:37:46.712359+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.