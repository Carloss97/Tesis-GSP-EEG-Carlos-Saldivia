# Integration Log: scr_00688
Started: 2026-04-16T15:22:05.465450+00:00
Description: Screening scr_00688 ds=bci_iv2a_real_s2 graph=gaussian miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.4 | seed=0 | MAE=1.7972e-06 | t=0.0031s
    nearest | MR=0.4 | seed=0 | MAE=1.7309e-06 | t=0.0803s
    tikhonov | MR=0.4 | seed=0 | MAE=3.4382e-06 | t=0.1030s
    tv | MR=0.4 | seed=0 | MAE=1.7972e-06 | t=0.7099s
    trss | MR=0.4 | seed=0 | MAE=1.4569e-06 | t=0.6355s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=5.4208e-06 | t=0.0462s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.7600e-05 | t=32.4177s
    mean | MR=0.4 | seed=1 | MAE=1.7508e-06 | t=0.0031s
    nearest | MR=0.4 | seed=1 | MAE=1.7485e-06 | t=0.1195s
    tikhonov | MR=0.4 | seed=1 | MAE=3.3985e-06 | t=0.0104s
    tv | MR=0.4 | seed=1 | MAE=1.7508e-06 | t=0.9720s
    trss | MR=0.4 | seed=1 | MAE=1.4107e-06 | t=0.2412s

Completed: 2026-04-16T15:22:05.466898+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.