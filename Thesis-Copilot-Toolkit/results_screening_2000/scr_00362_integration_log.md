# Integration Log: scr_00362
Started: 2026-04-16T13:08:24.564384+00:00
Description: Screening scr_00362 ds=physionet_real graph=gaussian miss=[0.1] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.0022s
    nearest | MR=0.1 | seed=0 | MAE=2.3639e-06 | t=0.0029s
    tikhonov | MR=0.1 | seed=0 | MAE=1.7194e-05 | t=0.0057s
    tv | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.1949s
    trss | MR=0.1 | seed=0 | MAE=1.5091e-06 | t=0.0167s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.1962e-05 | t=0.0081s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=3.8773e-05 | t=11.8607s
    mean | MR=0.1 | seed=1 | MAE=2.0496e-06 | t=0.0026s
    nearest | MR=0.1 | seed=1 | MAE=2.3187e-06 | t=0.0027s
    tikhonov | MR=0.1 | seed=1 | MAE=1.7210e-05 | t=0.0057s
    tv | MR=0.1 | seed=1 | MAE=2.0495e-06 | t=0.2006s
    trss | MR=0.1 | seed=1 | MAE=1.4817e-06 | t=0.0174s

Completed: 2026-04-16T13:08:24.565107+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.