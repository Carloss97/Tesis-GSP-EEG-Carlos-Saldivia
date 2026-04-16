# Integration Log: scr_01793
Started: 2026-04-16T09:37:55.005243+00:00
Description: Screening scr_01793 ds=bci_iv2a_real_s3 graph=kalofolias miss=3ch mode=noise

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.1958e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=2.0341e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.1884s
    trss | MR=0.2 | seed=0 | MAE=4.8650e-02 | t=0.0217s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.3588e-01 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.4457e-01 | t=1.2514s
    mean | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.0295e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=2.0566e-01 | t=0.0056s
    tv | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.1858s
    trss | MR=0.2 | seed=1 | MAE=5.1583e-02 | t=0.0205s

Completed: 2026-04-16T09:37:55.006048+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.