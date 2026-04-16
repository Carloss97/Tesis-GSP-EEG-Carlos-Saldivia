# Integration Log: scr_00386
Started: 2026-04-16T13:13:11.213813+00:00
Description: Screening scr_00386 ds=physionet_real graph=kalofolias miss=[0.1] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.0030s
    nearest | MR=0.1 | seed=0 | MAE=2.3639e-06 | t=0.0043s
    tikhonov | MR=0.1 | seed=0 | MAE=1.0990e-05 | t=0.0087s
    tv | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.4203s
    trss | MR=0.1 | seed=0 | MAE=1.5121e-06 | t=0.1133s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.8987e-05 | t=0.0126s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=3.3587e-05 | t=12.4791s
    mean | MR=0.1 | seed=1 | MAE=2.0496e-06 | t=0.0035s
    nearest | MR=0.1 | seed=1 | MAE=2.3187e-06 | t=0.0047s
    tikhonov | MR=0.1 | seed=1 | MAE=1.0983e-05 | t=0.0088s
    tv | MR=0.1 | seed=1 | MAE=2.0496e-06 | t=0.2259s
    trss | MR=0.1 | seed=1 | MAE=1.4845e-06 | t=0.0172s

Completed: 2026-04-16T13:13:11.214672+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.