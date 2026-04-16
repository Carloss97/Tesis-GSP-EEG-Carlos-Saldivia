# Integration Log: scr_00710
Started: 2026-04-16T15:33:26.535526+00:00
Description: Screening scr_00710 ds=physionet_real graph=kalofolias miss=[0.4] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: kalofolias built OK
    mean | MR=0.4 | seed=0 | MAE=1.0497e-05 | t=0.0236s
    nearest | MR=0.4 | seed=0 | MAE=1.1571e-05 | t=0.0233s
    tikhonov | MR=0.4 | seed=0 | MAE=1.6031e-05 | t=0.0123s
    tv | MR=0.4 | seed=0 | MAE=1.0497e-05 | t=0.9730s
    trss | MR=0.4 | seed=0 | MAE=8.5625e-06 | t=0.5772s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=2.0937e-05 | t=0.0662s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=3.6576e-05 | t=22.6188s
    mean | MR=0.4 | seed=1 | MAE=1.0467e-05 | t=0.0192s
    nearest | MR=0.4 | seed=1 | MAE=1.1385e-05 | t=0.0289s
    tikhonov | MR=0.4 | seed=1 | MAE=1.6027e-05 | t=0.0139s
    tv | MR=0.4 | seed=1 | MAE=1.0467e-05 | t=0.9776s
    trss | MR=0.4 | seed=1 | MAE=8.5455e-06 | t=0.4545s

Completed: 2026-04-16T15:33:26.537031+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.