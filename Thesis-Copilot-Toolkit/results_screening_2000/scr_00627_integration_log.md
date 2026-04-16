# Integration Log: scr_00627
Started: 2026-04-16T14:48:38.014776+00:00
Description: Screening scr_00627 ds=bci_iv2a_real_s1 graph=vknng miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: vknng built OK
    mean | MR=0.3 | seed=0 | MAE=4.4732e-06 | t=0.0031s
    nearest | MR=0.3 | seed=0 | MAE=4.7753e-06 | t=0.0101s
    tikhonov | MR=0.3 | seed=0 | MAE=6.3377e-06 | t=0.0086s
    tv | MR=0.3 | seed=0 | MAE=4.4728e-06 | t=0.4782s
    trss | MR=0.3 | seed=0 | MAE=3.4547e-06 | t=0.0235s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=9.7429e-06 | t=0.0336s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.4347e-05 | t=22.4445s
    mean | MR=0.3 | seed=1 | MAE=4.4548e-06 | t=0.0061s
    nearest | MR=0.3 | seed=1 | MAE=4.6851e-06 | t=0.0497s
    tikhonov | MR=0.3 | seed=1 | MAE=6.3290e-06 | t=0.0458s
    tv | MR=0.3 | seed=1 | MAE=4.4544e-06 | t=1.2217s
    trss | MR=0.3 | seed=1 | MAE=3.4242e-06 | t=0.0526s

Completed: 2026-04-16T14:48:38.016288+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.