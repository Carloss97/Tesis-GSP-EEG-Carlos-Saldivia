# Integration Log: scr_01226
Started: 2026-04-16T08:22:04.871198+00:00
Description: Screening scr_01226 ds=physionet_real graph=gaussian miss=[0.2] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=7.8019e-02 | t=0.1869s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.8523e-01 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=3.4168e-02 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.0724e-01 | t=1.2537s
    tv | MR=0.2 | seed=1 | MAE=7.7313e-02 | t=0.1855s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.8530e-01 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=3.3383e-02 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=5.0789e-01 | t=1.2714s
    tv | MR=0.2 | seed=0 | MAE=7.8019e-02 | t=0.1860s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.4291e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=3.6950e-02 | t=0.0184s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.0883e-01 | t=1.2984s

Completed: 2026-04-16T08:22:04.872060+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.