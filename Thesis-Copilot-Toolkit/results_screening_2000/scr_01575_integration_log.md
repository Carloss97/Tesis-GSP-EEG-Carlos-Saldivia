# Integration Log: scr_01575
Started: 2026-04-16T09:06:53.332819+00:00
Description: Screening scr_01575 ds=bci_iv2a_real_s1 graph=kalofolias miss=1ch mode=noise

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.6301e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=2.0984e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.1903s
    trss | MR=0.2 | seed=0 | MAE=4.9949e-02 | t=0.0206s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.3571e-01 | t=0.0083s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.3947e-01 | t=2.5848s
    mean | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.3510e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=2.0564e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.1973s
    trss | MR=0.2 | seed=1 | MAE=4.9640e-02 | t=0.0202s

Completed: 2026-04-16T09:06:53.333679+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.