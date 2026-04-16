# Integration Log: scr_01420
Started: 2026-04-16T08:46:30.401490+00:00
Description: Screening scr_01420 ds=bci_iv2a_real_s2 graph=knn miss=[0.4] mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=2.9533e-02 | t=0.1528s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6743e-01 | t=0.0084s
    trss | MR=0.2 | seed=0 | MAE=1.2914e-02 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.8139e-01 | t=1.4133s
    tv | MR=0.2 | seed=1 | MAE=2.8800e-02 | t=0.1647s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.6657e-01 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=1.2965e-02 | t=0.0204s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.8253e-01 | t=1.2786s
    tv | MR=0.2 | seed=0 | MAE=2.9530e-02 | t=0.1538s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7568e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.4213e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.8431e-01 | t=1.3284s

Completed: 2026-04-16T08:46:30.402190+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.