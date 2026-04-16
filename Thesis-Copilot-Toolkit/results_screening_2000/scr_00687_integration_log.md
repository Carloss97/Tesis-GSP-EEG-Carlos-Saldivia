# Integration Log: scr_00687
Started: 2026-04-16T15:21:05.743709+00:00
Description: Screening scr_00687 ds=bci_iv2a_real_s1 graph=gaussian miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.4 | seed=0 | MAE=6.3033e-06 | t=0.0032s
    nearest | MR=0.4 | seed=0 | MAE=6.5281e-06 | t=0.0138s
    tikhonov | MR=0.4 | seed=0 | MAE=1.2394e-05 | t=0.0124s
    tv | MR=0.4 | seed=0 | MAE=6.3033e-06 | t=1.0532s
    trss | MR=0.4 | seed=0 | MAE=4.9195e-06 | t=0.9014s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.4165e-05 | t=0.0123s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.9519e-05 | t=29.3602s
    mean | MR=0.4 | seed=1 | MAE=6.2507e-06 | t=0.0031s
    nearest | MR=0.4 | seed=1 | MAE=6.8607e-06 | t=0.0912s
    tikhonov | MR=0.4 | seed=1 | MAE=1.2320e-05 | t=0.0087s
    tv | MR=0.4 | seed=1 | MAE=6.2507e-06 | t=0.9374s
    trss | MR=0.4 | seed=1 | MAE=4.8792e-06 | t=0.0795s

Completed: 2026-04-16T15:21:05.744570+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.