# Integration Log: scr_01791
Started: 2026-04-16T09:37:23.372270+00:00
Description: Screening scr_01791 ds=bci_iv2a_real_s1 graph=kalofolias miss=3ch mode=noise

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.6301e-02 | t=0.0043s
    tikhonov | MR=0.2 | seed=0 | MAE=2.0984e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.1877s
    trss | MR=0.2 | seed=0 | MAE=4.9949e-02 | t=0.0211s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.3571e-01 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.3947e-01 | t=2.7473s
    mean | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.3510e-02 | t=0.0043s
    tikhonov | MR=0.2 | seed=1 | MAE=2.0564e-01 | t=0.0063s
    tv | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.1849s
    trss | MR=0.2 | seed=1 | MAE=4.9640e-02 | t=0.0224s

Completed: 2026-04-16T09:37:23.372982+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.