# Integration Log: scr_01694
Started: 2026-04-16T09:23:31.807825+00:00
Description: Screening scr_01694 ds=physionet_real graph=knng miss=2ch mode=noise

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=7.8230e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=9.0465e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.2706e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=7.7593e-02 | t=0.1535s
    trss | MR=0.2 | seed=0 | MAE=3.9411e-02 | t=0.0205s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.4388e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.9739e-01 | t=2.6080s
    mean | MR=0.2 | seed=1 | MAE=7.8011e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=8.9030e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.2761e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=7.7382e-02 | t=0.1446s
    trss | MR=0.2 | seed=1 | MAE=3.9498e-02 | t=0.0199s

Completed: 2026-04-16T09:23:31.808573+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.