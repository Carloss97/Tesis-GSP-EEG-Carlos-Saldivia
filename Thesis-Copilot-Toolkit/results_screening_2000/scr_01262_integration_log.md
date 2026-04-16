# Integration Log: scr_01262
Started: 2026-04-16T08:26:37.526615+00:00
Description: Screening scr_01262 ds=physionet_real graph=knng miss=[0.2] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=7.5604e-02 | t=0.1461s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1106e-01 | t=0.0091s
    trss | MR=0.2 | seed=0 | MAE=2.9097e-02 | t=0.0198s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.9611e-01 | t=2.6895s
    tv | MR=0.2 | seed=1 | MAE=7.4899e-02 | t=0.1597s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.1083e-01 | t=0.0084s
    trss | MR=0.2 | seed=1 | MAE=2.8234e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.9672e-01 | t=2.6187s
    tv | MR=0.2 | seed=0 | MAE=7.6758e-02 | t=0.1464s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3835e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=2.9748e-02 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.7141e-01 | t=2.6130s

Completed: 2026-04-16T08:26:37.527325+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.