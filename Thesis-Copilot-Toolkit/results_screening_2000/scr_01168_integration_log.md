# Integration Log: scr_01168
Started: 2026-04-16T14:54:23.316515+00:00
Description: Screening scr_01168 ds=bci_iv2a_real_s2 graph=vknng miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: vknng built OK
    tv | MR=0.2 | seed=0 | MAE=8.7663e-07 | t=0.4568s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.9389e-06 | t=0.0149s
    trss | MR=0.2 | seed=0 | MAE=6.8105e-07 | t=0.8818s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.2636e-06 | t=24.3579s
    tv | MR=0.2 | seed=1 | MAE=9.0520e-07 | t=0.6646s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=3.9808e-06 | t=0.0123s
    trss | MR=0.2 | seed=1 | MAE=6.9861e-07 | t=0.4393s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.3107e-06 | t=14.2781s
    tv | MR=0.2 | seed=0 | MAE=8.7651e-07 | t=0.1487s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.0108e-06 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=6.5966e-07 | t=0.0206s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.8343e-06 | t=27.6156s

Completed: 2026-04-16T14:54:23.317366+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.