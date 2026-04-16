# Integration Log: scr_01814
Started: 2026-04-16T09:40:27.418922+00:00
Description: Screening scr_01814 ds=physionet_real graph=vknng miss=3ch mode=noise

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: vknng built OK
    mean | MR=0.2 | seed=0 | MAE=7.8230e-02 | t=0.0023s
    nearest | MR=0.2 | seed=0 | MAE=9.0465e-02 | t=0.0047s
    tikhonov | MR=0.2 | seed=0 | MAE=1.2622e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=7.7506e-02 | t=0.1485s
    trss | MR=0.2 | seed=0 | MAE=4.0270e-02 | t=0.0206s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.4073e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.9042e-01 | t=1.2720s
    mean | MR=0.2 | seed=1 | MAE=7.8011e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=8.9030e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.2661e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=7.7292e-02 | t=0.1430s
    trss | MR=0.2 | seed=1 | MAE=4.0214e-02 | t=0.0202s

Completed: 2026-04-16T09:40:27.419806+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.