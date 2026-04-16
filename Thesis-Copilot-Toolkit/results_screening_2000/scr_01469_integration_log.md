# Integration Log: scr_01469
Started: 2026-04-16T08:52:48.836573+00:00
Description: Screening scr_01469 ds=bci_iv2a_real_s3 graph=kalofolias miss=[0.4] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: kalofolias built OK
    tv | MR=0.2 | seed=0 | MAE=6.5815e-02 | t=0.1864s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7870e-01 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=2.8815e-02 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.0653e-01 | t=1.2802s
    tv | MR=0.2 | seed=1 | MAE=6.8917e-02 | t=0.1913s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.8057e-01 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=3.0572e-02 | t=0.0203s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.0458e-01 | t=1.2566s
    tv | MR=0.2 | seed=0 | MAE=6.5815e-02 | t=0.1869s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2245e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.0663e-02 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.0937e-01 | t=1.5768s

Completed: 2026-04-16T08:52:48.837275+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.