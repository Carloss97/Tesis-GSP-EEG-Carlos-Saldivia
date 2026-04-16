# Integration Log: scr_01478
Started: 2026-04-16T08:53:34.954705+00:00
Description: Screening scr_01478 ds=physionet_real graph=knng miss=[0.4] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=7.5604e-02 | t=0.1446s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1106e-01 | t=0.0086s
    trss | MR=0.2 | seed=0 | MAE=2.9097e-02 | t=0.0206s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.9611e-01 | t=1.2823s
    tv | MR=0.2 | seed=1 | MAE=7.4899e-02 | t=0.1443s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.1083e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=2.8234e-02 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.9672e-01 | t=1.2672s
    tv | MR=0.2 | seed=0 | MAE=7.6758e-02 | t=0.1464s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3835e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=2.9748e-02 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.7141e-01 | t=1.2863s

Completed: 2026-04-16T08:53:34.955594+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.