# Integration Log: scr_01169
Started: 2026-04-16T14:56:42.055939+00:00
Description: Screening scr_01169 ds=bci_iv2a_real_s3 graph=vknng miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: vknng built OK
    tv | MR=0.2 | seed=0 | MAE=7.3152e-07 | t=0.6460s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.4681e-06 | t=0.0128s
    trss | MR=0.2 | seed=0 | MAE=4.6083e-07 | t=0.8444s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.0451e-06 | t=8.3902s
    tv | MR=0.2 | seed=1 | MAE=7.3472e-07 | t=0.1604s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.4620e-06 | t=0.0568s
    trss | MR=0.2 | seed=1 | MAE=4.6733e-07 | t=0.6097s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.0631e-06 | t=25.5123s
    tv | MR=0.2 | seed=0 | MAE=7.3144e-07 | t=0.3011s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6018e-06 | t=0.0138s
    trss | MR=0.2 | seed=0 | MAE=4.7805e-07 | t=0.1116s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5318e-06 | t=23.0347s

Completed: 2026-04-16T14:56:42.057079+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.