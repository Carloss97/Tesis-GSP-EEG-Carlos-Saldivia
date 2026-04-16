# Integration Log: scr_00699
Started: 2026-04-16T15:28:05.540558+00:00
Description: Screening scr_00699 ds=bci_iv2a_real_s1 graph=gaussian miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.4 | seed=0 | MAE=6.3033e-06 | t=0.0052s
    nearest | MR=0.4 | seed=0 | MAE=6.5281e-06 | t=0.0587s
    tikhonov | MR=0.4 | seed=0 | MAE=1.2394e-05 | t=0.0392s
    tv | MR=0.4 | seed=0 | MAE=6.3033e-06 | t=1.0677s
    trss | MR=0.4 | seed=0 | MAE=4.9195e-06 | t=0.5038s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.4165e-05 | t=0.0193s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.9519e-05 | t=34.4338s
    mean | MR=0.4 | seed=1 | MAE=6.2507e-06 | t=0.0033s
    nearest | MR=0.4 | seed=1 | MAE=6.8607e-06 | t=0.0137s
    tikhonov | MR=0.4 | seed=1 | MAE=1.2320e-05 | t=0.0093s
    tv | MR=0.4 | seed=1 | MAE=6.2507e-06 | t=0.7976s
    trss | MR=0.4 | seed=1 | MAE=4.8792e-06 | t=0.4671s

Completed: 2026-04-16T15:28:05.541584+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.