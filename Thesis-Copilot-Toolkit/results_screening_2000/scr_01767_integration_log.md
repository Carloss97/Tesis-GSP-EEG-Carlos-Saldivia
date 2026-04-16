# Integration Log: scr_01767
Started: 2026-04-16T09:33:56.857690+00:00
Description: Screening scr_01767 ds=bci_iv2a_real_s1 graph=gaussian miss=3ch mode=noise

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.6301e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=3.0775e-01 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.1860s
    trss | MR=0.2 | seed=0 | MAE=4.9949e-02 | t=0.0210s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.8203e-01 | t=0.0082s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.1478e-01 | t=1.6124s
    mean | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.3510e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=1 | MAE=3.0151e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.1851s
    trss | MR=0.2 | seed=1 | MAE=4.9640e-02 | t=0.0213s

Completed: 2026-04-16T09:33:56.858567+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.