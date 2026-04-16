# Integration Log: scr_00555
Started: 2026-04-16T14:12:14.586338+00:00
Description: Screening scr_00555 ds=bci_iv2a_real_s1 graph=knn miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.3 | seed=0 | MAE=4.4732e-06 | t=0.0021s
    nearest | MR=0.3 | seed=0 | MAE=4.7753e-06 | t=0.0064s
    tikhonov | MR=0.3 | seed=0 | MAE=8.0728e-06 | t=0.0065s
    tv | MR=0.3 | seed=0 | MAE=4.4729e-06 | t=0.1538s
    trss | MR=0.3 | seed=0 | MAE=3.2552e-06 | t=0.0188s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.1815e-05 | t=0.0082s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.7093e-05 | t=20.2168s
    mean | MR=0.3 | seed=1 | MAE=4.4548e-06 | t=0.0021s
    nearest | MR=0.3 | seed=1 | MAE=4.6851e-06 | t=0.0063s
    tikhonov | MR=0.3 | seed=1 | MAE=8.0413e-06 | t=0.0057s
    tv | MR=0.3 | seed=1 | MAE=4.4545e-06 | t=0.1600s
    trss | MR=0.3 | seed=1 | MAE=3.2339e-06 | t=0.0185s

Completed: 2026-04-16T14:12:14.587291+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.