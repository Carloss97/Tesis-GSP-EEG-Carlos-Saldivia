# Integration Log: scr_00653
Started: 2026-04-16T15:02:56.523505+00:00
Description: Screening scr_00653 ds=bci_iv2a_real_s3 graph=knn miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.4 | seed=0 | MAE=1.4549e-06 | t=0.0031s
    nearest | MR=0.4 | seed=0 | MAE=1.3679e-06 | t=0.0512s
    tikhonov | MR=0.4 | seed=0 | MAE=2.0704e-06 | t=0.0463s
    tv | MR=0.4 | seed=0 | MAE=1.4549e-06 | t=0.7272s
    trss | MR=0.4 | seed=0 | MAE=1.3879e-06 | t=0.4836s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=2.8109e-06 | t=0.0188s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=5.5427e-06 | t=23.5712s
    mean | MR=0.4 | seed=1 | MAE=1.4638e-06 | t=0.0035s
    nearest | MR=0.4 | seed=1 | MAE=1.3378e-06 | t=0.0142s
    tikhonov | MR=0.4 | seed=1 | MAE=2.0699e-06 | t=0.0127s
    tv | MR=0.4 | seed=1 | MAE=1.4638e-06 | t=0.4497s
    trss | MR=0.4 | seed=1 | MAE=1.3795e-06 | t=0.7430s

Completed: 2026-04-16T15:02:56.524373+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.