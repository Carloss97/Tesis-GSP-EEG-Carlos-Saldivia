# Integration Log: scr_00470
Started: 2026-04-16T13:41:04.572748+00:00
Description: Screening scr_00470 ds=physionet_real graph=gaussian miss=[0.2] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=5.2059e-06 | t=0.0031s
    nearest | MR=0.2 | seed=0 | MAE=5.7680e-06 | t=0.0092s
    tikhonov | MR=0.2 | seed=0 | MAE=1.8190e-05 | t=0.0094s
    tv | MR=0.2 | seed=0 | MAE=5.2059e-06 | t=0.3795s
    trss | MR=0.2 | seed=0 | MAE=3.9094e-06 | t=0.7456s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2274e-05 | t=0.0813s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.9213e-05 | t=9.6967s
    mean | MR=0.2 | seed=1 | MAE=5.2168e-06 | t=0.0024s
    nearest | MR=0.2 | seed=1 | MAE=5.8832e-06 | t=0.0049s
    tikhonov | MR=0.2 | seed=1 | MAE=1.8186e-05 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=5.2168e-06 | t=0.1897s
    trss | MR=0.2 | seed=1 | MAE=3.9520e-06 | t=0.0185s

Completed: 2026-04-16T13:41:04.573472+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.