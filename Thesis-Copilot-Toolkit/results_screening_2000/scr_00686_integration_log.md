# Integration Log: scr_00686
Started: 2026-04-16T15:19:50.096787+00:00
Description: Screening scr_00686 ds=physionet_real graph=gaussian miss=[0.4] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.4 | seed=0 | MAE=1.0497e-05 | t=0.1180s
    nearest | MR=0.4 | seed=0 | MAE=1.1571e-05 | t=0.0704s
    tikhonov | MR=0.4 | seed=0 | MAE=1.9887e-05 | t=0.0087s
    tv | MR=0.4 | seed=0 | MAE=1.0497e-05 | t=0.8995s
    trss | MR=0.4 | seed=0 | MAE=8.5510e-06 | t=0.1814s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=2.2779e-05 | t=0.0155s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=3.9930e-05 | t=31.8855s
    mean | MR=0.4 | seed=1 | MAE=1.0467e-05 | t=0.0050s
    nearest | MR=0.4 | seed=1 | MAE=1.1385e-05 | t=0.0758s
    tikhonov | MR=0.4 | seed=1 | MAE=1.9902e-05 | t=0.0481s
    tv | MR=0.4 | seed=1 | MAE=1.0467e-05 | t=0.9297s
    trss | MR=0.4 | seed=1 | MAE=8.5334e-06 | t=0.3098s

Completed: 2026-04-16T15:19:50.097725+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.