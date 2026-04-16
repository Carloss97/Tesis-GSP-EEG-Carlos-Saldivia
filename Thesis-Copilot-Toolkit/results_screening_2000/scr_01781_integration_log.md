# Integration Log: scr_01781
Started: 2026-04-16T09:36:09.945113+00:00
Description: Screening scr_01781 ds=bci_iv2a_real_s3 graph=gaussian miss=3ch mode=noise

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.1958e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=2.9997e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.1872s
    trss | MR=0.2 | seed=0 | MAE=4.8650e-02 | t=0.0216s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.8100e-01 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.3544e-01 | t=1.2379s
    mean | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.0295e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=3.0179e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.1886s
    trss | MR=0.2 | seed=1 | MAE=5.1583e-02 | t=0.0211s

Completed: 2026-04-16T09:36:09.945955+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.