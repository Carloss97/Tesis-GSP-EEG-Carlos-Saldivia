# Integration Log: scr_01685
Started: 2026-04-16T09:22:38.460368+00:00
Description: Screening scr_01685 ds=bci_iv2a_real_s3 graph=kalofolias miss=2ch mode=noise

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.1958e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=2.0341e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.1847s
    trss | MR=0.2 | seed=0 | MAE=4.8650e-02 | t=0.0198s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.3588e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.4457e-01 | t=1.3115s
    mean | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.0030s
    nearest | MR=0.2 | seed=1 | MAE=6.0295e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=2.0566e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.1862s
    trss | MR=0.2 | seed=1 | MAE=5.1583e-02 | t=0.0199s

Completed: 2026-04-16T09:22:38.461313+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.