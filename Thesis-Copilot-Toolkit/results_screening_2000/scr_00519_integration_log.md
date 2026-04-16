# Integration Log: scr_00519
Started: 2026-04-16T13:58:36.917528+00:00
Description: Screening scr_00519 ds=bci_iv2a_real_s1 graph=vknng miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: vknng built OK
    mean | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.0032s
    nearest | MR=0.2 | seed=0 | MAE=3.2140e-06 | t=0.0089s
    tikhonov | MR=0.2 | seed=0 | MAE=5.1700e-06 | t=0.0118s
    tv | MR=0.2 | seed=0 | MAE=3.0354e-06 | t=0.3233s
    trss | MR=0.2 | seed=0 | MAE=2.2787e-06 | t=0.0422s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.0390e-06 | t=0.0171s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3698e-05 | t=22.0210s
    mean | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.0032s
    nearest | MR=0.2 | seed=1 | MAE=3.5344e-06 | t=0.0080s
    tikhonov | MR=0.2 | seed=1 | MAE=5.4540e-06 | t=0.0118s
    tv | MR=0.2 | seed=1 | MAE=3.3732e-06 | t=0.2118s
    trss | MR=0.2 | seed=1 | MAE=2.6015e-06 | t=0.0188s

Completed: 2026-04-16T13:58:36.918370+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.