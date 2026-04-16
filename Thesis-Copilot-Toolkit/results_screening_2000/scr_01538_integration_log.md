# Integration Log: scr_01538
Started: 2026-04-16T09:01:26.611560+00:00
Description: Screening scr_01538 ds=physionet_real graph=knn miss=1ch mode=noise

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: knn__k7 built OK
    mean | MR=0.2 | seed=0 | MAE=7.8230e-02 | t=0.0023s
    nearest | MR=0.2 | seed=0 | MAE=9.0465e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.7572e-01 | t=0.0056s
    tv | MR=0.2 | seed=0 | MAE=7.8040e-02 | t=0.1511s
    trss | MR=0.2 | seed=0 | MAE=4.2119e-02 | t=0.0198s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.1473e-01 | t=0.0085s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.6685e-01 | t=1.5645s
    mean | MR=0.2 | seed=1 | MAE=7.8011e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=8.9030e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.7580e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=7.7820e-02 | t=0.1505s
    trss | MR=0.2 | seed=1 | MAE=4.1446e-02 | t=0.0194s

Completed: 2026-04-16T09:01:26.612434+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.