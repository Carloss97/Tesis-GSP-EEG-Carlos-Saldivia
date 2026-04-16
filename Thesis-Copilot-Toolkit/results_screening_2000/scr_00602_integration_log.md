# Integration Log: scr_00602
Started: 2026-04-16T14:35:42.297725+00:00
Description: Screening scr_00602 ds=physionet_real graph=kalofolias miss=[0.3] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: kalofolias built OK
    mean | MR=0.3 | seed=0 | MAE=7.1409e-06 | t=0.0020s
    nearest | MR=0.3 | seed=0 | MAE=8.1341e-06 | t=0.0065s
    tikhonov | MR=0.3 | seed=0 | MAE=1.4008e-05 | t=0.0057s
    tv | MR=0.3 | seed=0 | MAE=7.1409e-06 | t=0.1981s
    trss | MR=0.3 | seed=0 | MAE=5.5787e-06 | t=0.1664s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=2.0156e-05 | t=0.0122s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=3.5451e-05 | t=25.4710s
    mean | MR=0.3 | seed=1 | MAE=7.3000e-06 | t=0.0044s
    nearest | MR=0.3 | seed=1 | MAE=8.0659e-06 | t=0.0108s
    tikhonov | MR=0.3 | seed=1 | MAE=1.4097e-05 | t=0.0058s
    tv | MR=0.3 | seed=1 | MAE=7.3000e-06 | t=0.1993s
    trss | MR=0.3 | seed=1 | MAE=5.6019e-06 | t=0.0187s

Completed: 2026-04-16T14:35:42.298578+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.