# Integration Log: scr_01958
Started: 2026-04-16T10:00:52.912073+00:00
Description: Screening scr_01958 ds=physionet_real graph=knn miss=[0.2] mode=noise

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=7.8230e-02 | t=0.0021s
    nearest | MR=0.2 | seed=0 | MAE=9.0465e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=1.3776e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=7.7815e-02 | t=0.1478s
    trss | MR=0.2 | seed=0 | MAE=3.9396e-02 | t=0.0221s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.6342e-01 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.2369e-01 | t=2.5312s
    mean | MR=0.2 | seed=1 | MAE=7.8011e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=8.9030e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.3801e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=7.7596e-02 | t=0.1493s
    trss | MR=0.2 | seed=1 | MAE=3.9132e-02 | t=0.0210s

Completed: 2026-04-16T10:00:52.912784+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.