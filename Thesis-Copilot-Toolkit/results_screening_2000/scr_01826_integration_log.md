# Integration Log: scr_01826
Started: 2026-04-16T09:42:08.080886+00:00
Description: Screening scr_01826 ds=physionet_real graph=aew miss=3ch mode=noise

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: aew built OK
    mean | MR=0.2 | seed=0 | MAE=7.8230e-02 | t=0.0021s
    nearest | MR=0.2 | seed=0 | MAE=9.0465e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.1223e-01 | t=0.0056s
    tv | MR=0.2 | seed=0 | MAE=7.7418e-02 | t=0.1463s
    trss | MR=0.2 | seed=0 | MAE=3.8649e-02 | t=0.0206s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2282e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.6065e-01 | t=1.2924s
    mean | MR=0.2 | seed=1 | MAE=7.8011e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=8.9030e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.1241e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=7.7204e-02 | t=0.1544s
    trss | MR=0.2 | seed=1 | MAE=3.8546e-02 | t=0.0202s

Completed: 2026-04-16T09:42:08.081664+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.