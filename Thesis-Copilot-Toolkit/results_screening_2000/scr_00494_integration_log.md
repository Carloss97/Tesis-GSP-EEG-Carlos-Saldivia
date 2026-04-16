# Integration Log: scr_00494
Started: 2026-04-16T13:48:59.369845+00:00
Description: Screening scr_00494 ds=physionet_real graph=kalofolias miss=[0.2] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=5.2059e-06 | t=0.0031s
    nearest | MR=0.2 | seed=0 | MAE=5.7680e-06 | t=0.0081s
    tikhonov | MR=0.2 | seed=0 | MAE=1.2858e-05 | t=0.0119s
    tv | MR=0.2 | seed=0 | MAE=5.2059e-06 | t=0.5795s
    trss | MR=0.2 | seed=0 | MAE=3.9163e-06 | t=0.2187s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9720e-05 | t=0.0245s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.4688e-05 | t=8.9182s
    mean | MR=0.2 | seed=1 | MAE=5.2168e-06 | t=0.0030s
    nearest | MR=0.2 | seed=1 | MAE=5.8832e-06 | t=0.0084s
    tikhonov | MR=0.2 | seed=1 | MAE=1.2860e-05 | t=0.0086s
    tv | MR=0.2 | seed=1 | MAE=5.2168e-06 | t=0.6120s
    trss | MR=0.2 | seed=1 | MAE=3.9591e-06 | t=0.2160s

Completed: 2026-04-16T13:48:59.370536+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.