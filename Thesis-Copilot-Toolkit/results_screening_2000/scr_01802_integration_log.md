# Integration Log: scr_01802
Started: 2026-04-16T09:38:47.989708+00:00
Description: Screening scr_01802 ds=physionet_real graph=knng miss=3ch mode=noise

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=7.8230e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=9.0465e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.2706e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=7.7593e-02 | t=0.1449s
    trss | MR=0.2 | seed=0 | MAE=3.9411e-02 | t=0.0200s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.4388e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.9739e-01 | t=2.0179s
    mean | MR=0.2 | seed=1 | MAE=7.8011e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=8.9030e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.2761e-01 | t=0.0059s
    tv | MR=0.2 | seed=1 | MAE=7.7382e-02 | t=0.1460s
    trss | MR=0.2 | seed=1 | MAE=3.9498e-02 | t=0.0206s

Completed: 2026-04-16T09:38:47.990568+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.