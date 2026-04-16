# Integration Log: scr_01346
Started: 2026-04-16T08:37:03.516368+00:00
Description: Screening scr_01346 ds=physionet_real graph=gaussian miss=[0.3] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=7.8018e-02 | t=0.1878s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.8347e-01 | t=0.0083s
    trss | MR=0.2 | seed=0 | MAE=3.4115e-02 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.0483e-01 | t=1.2713s
    tv | MR=0.2 | seed=1 | MAE=7.7312e-02 | t=0.1846s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.8352e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=3.3328e-02 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=5.0548e-01 | t=1.2740s
    tv | MR=0.2 | seed=0 | MAE=7.8018e-02 | t=0.1848s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.4145e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.6876e-02 | t=0.0183s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.0681e-01 | t=1.2943s

Completed: 2026-04-16T08:37:03.517242+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.