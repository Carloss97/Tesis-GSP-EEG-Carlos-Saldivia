# Integration Log: scr_00748
Started: 2026-04-16T11:52:16.621110+00:00
Description: Screening scr_00748 ds=bci_iv2a_real_s2 graph=aew miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: aew built OK
    mean | MR=0.4 | seed=0 | MAE=1.7972e-06 | t=0.0020s
    nearest | MR=0.4 | seed=0 | MAE=1.7309e-06 | t=0.0092s
    tikhonov | MR=0.4 | seed=0 | MAE=2.4862e-06 | t=0.0058s
    tv | MR=0.4 | seed=0 | MAE=1.7969e-06 | t=0.1569s
    trss | MR=0.4 | seed=0 | MAE=1.5431e-06 | t=0.0197s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=4.9566e-06 | t=0.0078s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.5013e-05 | t=1.3081s
    mean | MR=0.4 | seed=1 | MAE=1.7508e-06 | t=0.0020s
    nearest | MR=0.4 | seed=1 | MAE=1.7485e-06 | t=0.0086s
    tikhonov | MR=0.4 | seed=1 | MAE=2.4518e-06 | t=0.0058s
    tv | MR=0.4 | seed=1 | MAE=1.7505e-06 | t=0.1508s
    trss | MR=0.4 | seed=1 | MAE=1.5152e-06 | t=0.0201s

Completed: 2026-04-16T11:52:16.621932+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.