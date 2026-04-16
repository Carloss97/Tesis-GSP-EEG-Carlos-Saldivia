# Integration Log: scr_00736
Started: 2026-04-16T11:51:34.999443+00:00
Description: Screening scr_00736 ds=bci_iv2a_real_s2 graph=vknng miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: vknng built OK
    mean | MR=0.4 | seed=0 | MAE=1.7972e-06 | t=0.0021s
    nearest | MR=0.4 | seed=0 | MAE=1.7309e-06 | t=0.0084s
    tikhonov | MR=0.4 | seed=0 | MAE=2.2996e-06 | t=0.0059s
    tv | MR=0.4 | seed=0 | MAE=1.7972e-06 | t=0.1477s
    trss | MR=0.4 | seed=0 | MAE=1.7571e-06 | t=0.0207s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=4.8068e-06 | t=0.0079s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.3065e-05 | t=1.2486s
    mean | MR=0.4 | seed=1 | MAE=1.7508e-06 | t=0.0020s
    nearest | MR=0.4 | seed=1 | MAE=1.7485e-06 | t=0.0085s
    tikhonov | MR=0.4 | seed=1 | MAE=2.2562e-06 | t=0.0059s
    tv | MR=0.4 | seed=1 | MAE=1.7508e-06 | t=0.1481s
    trss | MR=0.4 | seed=1 | MAE=1.7092e-06 | t=0.0203s

Completed: 2026-04-16T11:51:35.000306+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.