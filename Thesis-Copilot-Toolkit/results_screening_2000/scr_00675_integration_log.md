# Integration Log: scr_00675
Started: 2026-04-16T15:12:58.913704+00:00
Description: Screening scr_00675 ds=bci_iv2a_real_s1 graph=knn miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.4 | seed=0 | MAE=6.3033e-06 | t=0.0021s
    nearest | MR=0.4 | seed=0 | MAE=6.5281e-06 | t=0.0096s
    tikhonov | MR=0.4 | seed=0 | MAE=9.9214e-06 | t=0.0092s
    tv | MR=0.4 | seed=0 | MAE=6.3026e-06 | t=0.1785s
    trss | MR=0.4 | seed=0 | MAE=4.5071e-06 | t=0.0215s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.3029e-05 | t=0.0129s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.8238e-05 | t=29.3230s
    mean | MR=0.4 | seed=1 | MAE=6.2507e-06 | t=0.0032s
    nearest | MR=0.4 | seed=1 | MAE=6.8607e-06 | t=0.0141s
    tikhonov | MR=0.4 | seed=1 | MAE=9.8460e-06 | t=0.0088s
    tv | MR=0.4 | seed=1 | MAE=6.2500e-06 | t=0.3491s
    trss | MR=0.4 | seed=1 | MAE=4.5047e-06 | t=0.2449s

Completed: 2026-04-16T15:12:58.914642+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.