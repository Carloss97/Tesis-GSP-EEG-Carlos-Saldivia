# Integration Log: scr_01227
Started: 2026-04-16T08:22:21.144962+00:00
Description: Screening scr_01227 ds=bci_iv2a_real_s1 graph=gaussian miss=[0.2] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=6.9320e-02 | t=0.1873s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.5543e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=1.6729e-02 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.1949e-01 | t=2.9623s
    tv | MR=0.2 | seed=1 | MAE=6.8278e-02 | t=0.2035s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.5194e-01 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=1.6375e-02 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.1842e-01 | t=2.6926s
    tv | MR=0.2 | seed=0 | MAE=6.9320e-02 | t=0.1858s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.0613e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=2.1751e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.9989e-01 | t=1.8011s

Completed: 2026-04-16T08:22:21.145832+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.