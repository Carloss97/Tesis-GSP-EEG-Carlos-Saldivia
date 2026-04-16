# Integration Log: scr_01910
Started: 2026-04-16T09:54:05.784715+00:00
Description: Screening scr_01910 ds=physionet_real graph=knng miss=[0.1] mode=noise

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=7.8230e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=9.0465e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=1.2706e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=7.7593e-02 | t=0.1464s
    trss | MR=0.2 | seed=0 | MAE=3.9411e-02 | t=0.0206s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.4388e-01 | t=0.0082s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.9739e-01 | t=1.2675s
    mean | MR=0.2 | seed=1 | MAE=7.8011e-02 | t=0.0022s
    nearest | MR=0.2 | seed=1 | MAE=8.9030e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.2761e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=7.7382e-02 | t=0.1488s
    trss | MR=0.2 | seed=1 | MAE=3.9498e-02 | t=0.0203s

Completed: 2026-04-16T09:54:05.785582+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.