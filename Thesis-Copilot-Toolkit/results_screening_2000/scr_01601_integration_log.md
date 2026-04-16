# Integration Log: scr_01601
Started: 2026-04-16T09:10:46.088806+00:00
Description: Screening scr_01601 ds=bci_iv2a_real_s3 graph=vknng miss=1ch mode=noise

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: vknng built OK
    mean | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.1958e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.4137e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=6.5968e-02 | t=0.1413s
    trss | MR=0.2 | seed=0 | MAE=6.2314e-02 | t=0.0191s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.6175e-01 | t=0.0079s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.8992e-01 | t=1.4020s
    mean | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.0295e-02 | t=0.0048s
    tikhonov | MR=0.2 | seed=1 | MAE=1.4360e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.8823e-02 | t=0.1423s
    trss | MR=0.2 | seed=1 | MAE=6.3908e-02 | t=0.0194s

Completed: 2026-04-16T09:10:46.089516+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.