# Integration Log: scr_01035
Started: 2026-04-16T13:01:59.744104+00:00
Description: Screening scr_01035 ds=bci_iv2a_real_s1 graph=kalofolias miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: kalofolias built OK
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.3224s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.2471e-06 | t=0.0132s
    trss | MR=0.2 | seed=0 | MAE=7.0725e-07 | t=0.0755s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0348e-05 | t=4.0015s
    tv | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.3259s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.4531e-06 | t=0.0152s
    trss | MR=0.2 | seed=1 | MAE=8.3690e-07 | t=0.1240s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.0466e-05 | t=2.3771s
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.1885s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.8998e-06 | t=0.0085s
    trss | MR=0.2 | seed=0 | MAE=9.6682e-07 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2237e-05 | t=9.5985s

Completed: 2026-04-16T13:01:59.744950+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.