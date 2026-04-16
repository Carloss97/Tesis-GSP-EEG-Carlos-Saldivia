# Integration Log: scr_01120
Started: 2026-04-16T14:00:39.232624+00:00
Description: Screening scr_01120 ds=bci_iv2a_real_s2 graph=gaussian miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.6849s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.5387e-06 | t=0.0125s
    trss | MR=0.2 | seed=0 | MAE=3.6928e-07 | t=0.4561s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1729e-05 | t=13.4485s
    tv | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.2167s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.5777e-06 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=3.8400e-07 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.1742e-05 | t=2.4434s
    tv | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.1999s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.8591e-06 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=4.0866e-07 | t=0.0212s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.4146e-05 | t=22.9736s

Completed: 2026-04-16T14:00:39.233614+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.