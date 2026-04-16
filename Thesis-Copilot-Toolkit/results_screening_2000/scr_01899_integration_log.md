# Integration Log: scr_01899
Started: 2026-04-16T09:52:40.605379+00:00
Description: Screening scr_01899 ds=bci_iv2a_real_s1 graph=kalofolias miss=[0.1] mode=noise

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.6301e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=2.0984e-01 | t=0.0069s
    tv | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.1880s
    trss | MR=0.2 | seed=0 | MAE=4.9949e-02 | t=0.0202s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.3571e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.3947e-01 | t=1.2683s
    mean | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.3510e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=1 | MAE=2.0564e-01 | t=0.0062s
    tv | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.1944s
    trss | MR=0.2 | seed=1 | MAE=4.9640e-02 | t=0.0206s

Completed: 2026-04-16T09:52:40.606096+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.