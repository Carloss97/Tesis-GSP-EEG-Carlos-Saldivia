# Integration Log: scr_01757
Started: 2026-04-16T09:32:46.896199+00:00
Description: Screening scr_01757 ds=bci_iv2a_real_s3 graph=knn miss=3ch mode=noise

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: knn__k7 built OK
    mean | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.1958e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=2.3262e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=6.5967e-02 | t=0.1616s
    trss | MR=0.2 | seed=0 | MAE=5.4204e-02 | t=0.0206s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.4858e-01 | t=0.0082s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.7525e-01 | t=1.2418s
    mean | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=6.0295e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=2.3380e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.8822e-02 | t=0.1602s
    trss | MR=0.2 | seed=1 | MAE=5.6299e-02 | t=0.0209s

Completed: 2026-04-16T09:32:46.897078+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.