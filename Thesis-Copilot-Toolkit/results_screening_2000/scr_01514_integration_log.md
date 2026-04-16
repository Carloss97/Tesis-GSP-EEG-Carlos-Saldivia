# Integration Log: scr_01514
Started: 2026-04-16T08:58:06.932742+00:00
Description: Screening scr_01514 ds=physionet_real graph=knn miss=1ch mode=noise

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=7.8230e-02 | t=0.0027s
    nearest | MR=0.2 | seed=0 | MAE=9.0465e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0823e-01 | t=0.0056s
    tv | MR=0.2 | seed=0 | MAE=7.6434e-02 | t=0.1411s
    trss | MR=0.2 | seed=0 | MAE=3.9504e-02 | t=0.0192s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0720e-01 | t=0.0087s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.5461e-01 | t=1.3363s
    mean | MR=0.2 | seed=1 | MAE=7.8011e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=8.9030e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0819e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=7.6172e-02 | t=0.1413s
    trss | MR=0.2 | seed=1 | MAE=3.9500e-02 | t=0.0203s

Completed: 2026-04-16T08:58:06.933612+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.