# Integration Log: scr_01778
Started: 2026-04-16T09:35:22.477593+00:00
Description: Screening scr_01778 ds=physionet_real graph=gaussian miss=3ch mode=noise

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=7.8230e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=9.0465e-02 | t=0.0045s
    tikhonov | MR=0.2 | seed=0 | MAE=3.3854e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=7.8230e-02 | t=0.1852s
    trss | MR=0.2 | seed=0 | MAE=5.8188e-02 | t=0.0206s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.2228e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.4700e-01 | t=1.3197s
    mean | MR=0.2 | seed=1 | MAE=7.8011e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=8.9030e-02 | t=0.0050s
    tikhonov | MR=0.2 | seed=1 | MAE=3.4067e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=7.8011e-02 | t=0.1845s
    trss | MR=0.2 | seed=1 | MAE=5.7913e-02 | t=0.0199s

Completed: 2026-04-16T09:35:22.478281+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.