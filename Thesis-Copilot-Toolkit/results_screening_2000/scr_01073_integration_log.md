# Integration Log: scr_01073
Started: 2026-04-16T13:22:32.645046+00:00
Description: Screening scr_01073 ds=bci_iv2a_real_s3 graph=aew miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: aew built OK
    tv | MR=0.2 | seed=0 | MAE=7.3128e-07 | t=0.1874s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5097e-06 | t=0.0126s
    trss | MR=0.2 | seed=0 | MAE=3.6818e-07 | t=0.1861s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5319e-06 | t=20.6019s
    tv | MR=0.2 | seed=1 | MAE=7.3452e-07 | t=0.1538s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5058e-06 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=3.7758e-07 | t=0.0202s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.5359e-06 | t=18.2334s
    tv | MR=0.2 | seed=0 | MAE=7.3131e-07 | t=0.1572s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6885e-06 | t=0.0089s
    trss | MR=0.2 | seed=0 | MAE=3.9960e-07 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.1862e-06 | t=15.0430s

Completed: 2026-04-16T13:22:32.645760+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.