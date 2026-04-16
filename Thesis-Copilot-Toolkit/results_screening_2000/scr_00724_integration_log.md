# Integration Log: scr_00724
Started: 2026-04-16T15:42:43.921456+00:00
Description: Screening scr_00724 ds=bci_iv2a_real_s2 graph=knng miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knng built OK
    mean | MR=0.4 | seed=0 | MAE=1.7972e-06 | t=0.0032s
    nearest | MR=0.4 | seed=0 | MAE=1.7309e-06 | t=0.0718s
    tikhonov | MR=0.4 | seed=0 | MAE=2.5911e-06 | t=0.0432s
    tv | MR=0.4 | seed=0 | MAE=1.7972e-06 | t=0.8939s
    trss | MR=0.4 | seed=0 | MAE=1.5530e-06 | t=0.6507s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=5.0482e-06 | t=0.0485s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.5276e-05 | t=29.3169s
    mean | MR=0.4 | seed=1 | MAE=1.7508e-06 | t=0.0038s
    nearest | MR=0.4 | seed=1 | MAE=1.7485e-06 | t=0.0147s
    tikhonov | MR=0.4 | seed=1 | MAE=2.5520e-06 | t=0.0571s
    tv | MR=0.4 | seed=1 | MAE=1.7508e-06 | t=0.9607s
    trss | MR=0.4 | seed=1 | MAE=1.5240e-06 | t=0.4533s

Completed: 2026-04-16T15:42:43.922449+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.