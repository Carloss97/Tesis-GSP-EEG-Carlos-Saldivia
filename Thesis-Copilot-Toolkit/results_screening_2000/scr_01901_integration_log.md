# Integration Log: scr_01901
Started: 2026-04-16T09:53:10.898070+00:00
Description: Screening scr_01901 ds=bci_iv2a_real_s3 graph=kalofolias miss=[0.1] mode=noise

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.1958e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=2.0341e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.1842s
    trss | MR=0.2 | seed=0 | MAE=4.8650e-02 | t=0.0216s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.3588e-01 | t=0.0088s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.4457e-01 | t=1.2387s
    mean | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.0295e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=2.0566e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.1851s
    trss | MR=0.2 | seed=1 | MAE=5.1583e-02 | t=0.0219s

Completed: 2026-04-16T09:53:10.898827+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.