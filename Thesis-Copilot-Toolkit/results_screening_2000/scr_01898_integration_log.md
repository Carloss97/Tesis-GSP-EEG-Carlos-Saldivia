# Integration Log: scr_01898
Started: 2026-04-16T09:52:20.359364+00:00
Description: Screening scr_01898 ds=physionet_real graph=kalofolias miss=[0.1] mode=noise

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=7.8230e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=9.0465e-02 | t=0.0043s
    tikhonov | MR=0.2 | seed=0 | MAE=2.3252e-01 | t=0.0059s
    tv | MR=0.2 | seed=0 | MAE=7.8230e-02 | t=0.1866s
    trss | MR=0.2 | seed=0 | MAE=5.8466e-02 | t=0.0203s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.7138e-01 | t=0.0079s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.5658e-01 | t=1.2518s
    mean | MR=0.2 | seed=1 | MAE=7.8011e-02 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=8.9030e-02 | t=0.0045s
    tikhonov | MR=0.2 | seed=1 | MAE=2.3369e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=7.8011e-02 | t=0.1875s
    trss | MR=0.2 | seed=1 | MAE=5.8197e-02 | t=0.0204s

Completed: 2026-04-16T09:52:20.360263+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.