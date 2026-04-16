# Integration Log: scr_01454
Started: 2026-04-16T08:50:32.791606+00:00
Description: Screening scr_01454 ds=physionet_real graph=gaussian miss=[0.4] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=7.8018e-02 | t=0.1893s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.8347e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.4115e-02 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.0483e-01 | t=1.2600s
    tv | MR=0.2 | seed=1 | MAE=7.7312e-02 | t=0.1872s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.8352e-01 | t=0.0079s
    trss | MR=0.2 | seed=1 | MAE=3.3328e-02 | t=0.0206s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=5.0548e-01 | t=1.2783s
    tv | MR=0.2 | seed=0 | MAE=7.8018e-02 | t=0.1866s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.4145e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.6876e-02 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.0681e-01 | t=1.2551s

Completed: 2026-04-16T08:50:32.792331+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.