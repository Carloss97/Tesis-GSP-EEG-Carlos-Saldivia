# Integration Log: scr_00677
Started: 2026-04-16T15:15:33.631032+00:00
Description: Screening scr_00677 ds=bci_iv2a_real_s3 graph=knn miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.4 | seed=0 | MAE=1.4549e-06 | t=0.0032s
    nearest | MR=0.4 | seed=0 | MAE=1.3679e-06 | t=0.0136s
    tikhonov | MR=0.4 | seed=0 | MAE=2.4549e-06 | t=0.0086s
    tv | MR=0.4 | seed=0 | MAE=1.4549e-06 | t=0.7754s
    trss | MR=0.4 | seed=0 | MAE=1.2821e-06 | t=0.6978s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=3.1389e-06 | t=0.1768s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=6.2901e-06 | t=22.8572s
    mean | MR=0.4 | seed=1 | MAE=1.4638e-06 | t=0.0046s
    nearest | MR=0.4 | seed=1 | MAE=1.3378e-06 | t=0.2072s
    tikhonov | MR=0.4 | seed=1 | MAE=2.4538e-06 | t=0.0089s
    tv | MR=0.4 | seed=1 | MAE=1.4638e-06 | t=0.9060s
    trss | MR=0.4 | seed=1 | MAE=1.2784e-06 | t=0.7729s

Completed: 2026-04-16T15:15:33.631907+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.