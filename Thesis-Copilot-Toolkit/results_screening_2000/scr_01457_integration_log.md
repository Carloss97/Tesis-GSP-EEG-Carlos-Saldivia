# Integration Log: scr_01457
Started: 2026-04-16T08:51:17.117919+00:00
Description: Screening scr_01457 ds=bci_iv2a_real_s3 graph=gaussian miss=[0.4] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=6.5815e-02 | t=0.1873s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.6180e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=2.8663e-02 | t=0.0198s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.9513e-01 | t=1.3603s
    tv | MR=0.2 | seed=1 | MAE=6.8917e-02 | t=0.1901s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.6266e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=3.0563e-02 | t=0.0215s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.9340e-01 | t=1.7892s
    tv | MR=0.2 | seed=0 | MAE=6.5815e-02 | t=0.1933s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.1137e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.0629e-02 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.9815e-01 | t=1.2680s

Completed: 2026-04-16T08:51:17.118773+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.