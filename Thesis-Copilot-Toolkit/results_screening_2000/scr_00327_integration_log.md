# Integration Log: scr_00327
Started: 2026-04-16T15:34:49.134563+00:00
Description: Screening scr_00327 ds=bci_iv2a_real_s1 graph=knn miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.0199s
    nearest | MR=0.1 | seed=0 | MAE=1.3708e-06 | t=0.0383s
    tikhonov | MR=0.1 | seed=0 | MAE=4.5749e-06 | t=0.0096s
    tv | MR=0.1 | seed=0 | MAE=1.3024e-06 | t=0.7615s
    trss | MR=0.1 | seed=0 | MAE=9.1525e-07 | t=0.2686s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=9.3331e-06 | t=0.0273s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.4248e-05 | t=17.7872s
    mean | MR=0.1 | seed=1 | MAE=1.2372e-06 | t=0.0035s
    nearest | MR=0.1 | seed=1 | MAE=1.2545e-06 | t=0.0045s
    tikhonov | MR=0.1 | seed=1 | MAE=4.5276e-06 | t=0.0280s
    tv | MR=0.1 | seed=1 | MAE=1.2371e-06 | t=0.4783s
    trss | MR=0.1 | seed=1 | MAE=8.4390e-07 | t=0.1628s

Completed: 2026-04-16T15:34:49.157037+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.