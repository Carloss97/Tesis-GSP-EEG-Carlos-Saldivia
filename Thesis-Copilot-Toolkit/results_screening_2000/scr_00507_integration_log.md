# Integration Log: scr_00507
Started: 2026-04-16T13:54:09.892064+00:00
Description: Screening scr_00507 ds=bci_iv2a_real_s1 graph=knng miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.0037s
    nearest | MR=0.2 | seed=0 | MAE=3.2140e-06 | t=0.0328s
    tikhonov | MR=0.2 | seed=0 | MAE=6.6345e-06 | t=0.0087s
    tv | MR=0.2 | seed=0 | MAE=3.0356e-06 | t=0.2828s
    trss | MR=0.2 | seed=0 | MAE=2.2476e-06 | t=0.0282s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0879e-05 | t=0.0139s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6050e-05 | t=13.2876s
    mean | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.0030s
    nearest | MR=0.2 | seed=1 | MAE=3.5344e-06 | t=0.0078s
    tikhonov | MR=0.2 | seed=1 | MAE=6.8394e-06 | t=0.0085s
    tv | MR=0.2 | seed=1 | MAE=3.3732e-06 | t=0.1788s
    trss | MR=0.2 | seed=1 | MAE=2.5353e-06 | t=0.2708s

Completed: 2026-04-16T13:54:09.892981+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.