# Integration Log: scr_00616
Started: 2026-04-16T14:43:28.133918+00:00
Description: Screening scr_00616 ds=bci_iv2a_real_s2 graph=knng miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knng built OK
    mean | MR=0.3 | seed=0 | MAE=1.2424e-06 | t=0.0021s
    nearest | MR=0.3 | seed=0 | MAE=1.2061e-06 | t=0.0072s
    tikhonov | MR=0.3 | seed=0 | MAE=2.2223e-06 | t=0.0058s
    tv | MR=0.3 | seed=0 | MAE=1.2424e-06 | t=0.1601s
    trss | MR=0.3 | seed=0 | MAE=1.0734e-06 | t=0.0699s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=4.9293e-06 | t=0.0248s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.4639e-05 | t=26.1006s
    mean | MR=0.3 | seed=1 | MAE=1.2418e-06 | t=0.0030s
    nearest | MR=0.3 | seed=1 | MAE=1.1920e-06 | t=0.0102s
    tikhonov | MR=0.3 | seed=1 | MAE=2.2265e-06 | t=0.0090s
    tv | MR=0.3 | seed=1 | MAE=1.2418e-06 | t=0.3805s
    trss | MR=0.3 | seed=1 | MAE=1.0557e-06 | t=0.0828s

Completed: 2026-04-16T14:43:28.134677+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.