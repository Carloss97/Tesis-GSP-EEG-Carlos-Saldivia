# Integration Log: scr_01838
Started: 2026-04-16T09:43:53.022043+00:00
Description: Screening scr_01838 ds=physionet_real graph=knn miss=[0.1] mode=noise

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=7.8230e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=9.0465e-02 | t=0.0044s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0823e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=7.6434e-02 | t=0.1417s
    trss | MR=0.2 | seed=0 | MAE=3.9504e-02 | t=0.0204s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0720e-01 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.5461e-01 | t=1.2918s
    mean | MR=0.2 | seed=1 | MAE=7.8011e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=8.9030e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0819e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=7.6172e-02 | t=0.1407s
    trss | MR=0.2 | seed=1 | MAE=3.9500e-02 | t=0.0208s

Completed: 2026-04-16T09:43:53.022734+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.