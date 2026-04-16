# Integration Log: scr_01658
Started: 2026-04-16T09:18:28.227157+00:00
Description: Screening scr_01658 ds=physionet_real graph=gaussian miss=2ch mode=noise

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=7.8230e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=9.0465e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=3.4005e-01 | t=0.0059s
    tv | MR=0.2 | seed=0 | MAE=7.8230e-02 | t=0.1869s
    trss | MR=0.2 | seed=0 | MAE=5.8366e-02 | t=0.0205s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.2279e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.4772e-01 | t=2.7897s
    mean | MR=0.2 | seed=1 | MAE=7.8011e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=8.9030e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=3.4220e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=7.8011e-02 | t=0.1841s
    trss | MR=0.2 | seed=1 | MAE=5.8094e-02 | t=0.0206s

Completed: 2026-04-16T09:18:28.227854+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.